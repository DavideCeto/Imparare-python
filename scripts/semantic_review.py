#!/usr/bin/env python3
"""
Revisione semantica della traduzione EN -> IT con Claude.

Per ogni coppia di file (inglese, italiano) chiede a Claude, tramite la CLI
`claude -p` (usa il login di Claude Code, non serve una API key), di
confrontare il significato e restituire i problemi in JSON strutturato.

I risultati sono salvati per file in <out>/semantic/ e riusati finché né il
file inglese né quello italiano cambiano: si può interrompere e riprendere.

Esempi:
  # Solo i capitoli, 4 richieste in parallelo
  python scripts/semantic_review.py --only 'chapters/*'

  # Un singolo file, con Opus
  python scripts/semantic_review.py --only 'chapters/05-*/index.md' --model opus

  # Rigenera solo il report dai risultati già salvati
  python scripts/semantic_review.py --report-only
"""

import argparse
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

PROMPT_VERSION = "1"
CHUNK_CHARS = 30_000  # dimensione massima (testo EN) di ogni richiesta

SYSTEM_PROMPT = """\
Sei un revisore esperto di traduzioni dall'inglese all'italiano per un manuale
di programmazione Python rivolto a studenti di circa 10-13 anni (sito MkDocs,
laboratori interattivi Skulpt con la grafica turtle, mascotte "Monty").

Ricevi una sezione del testo inglese originale e la corrispondente sezione
italiana. Confronta il SIGNIFICATO e segnala solo problemi reali:

- meaning: il senso è cambiato o è sbagliato (anche fatti tecnici su Python)
- omission: frase, elemento di lista, opzione di quiz o informazione mancante
- addition: contenuto aggiunto che non c'è nell'originale
- code: codice, codice inline, nomi di funzioni/variabili, URL o percorsi
  modificati (le stringhe e i commenti dentro il codice POSSONO essere tradotti)
- prediction: una domanda di previsione, un "Avevi indovinato?" o una risposta
  di quiz non corrisponde più a ciò che il codice fa davvero o all'originale
- terminology: termine tecnico tradotto in modo errato o incoerente nella sezione
- untranslated: prosa rimasta in inglese che andava tradotta
- grammar: errori di grammatica o frasi innaturali in italiano
- tone: registro non adatto agli studenti (troppo formale, oscuro)

Convenzioni del progetto: NON segnalarle come errori.
- Restano in inglese: parole chiave e sintassi Python, nomi di funzioni e
  metodi, codice inline, URL e percorsi, nomi propri e di prodotto (Monty,
  Skulpt, Python, Jupyter, Docker...), il tipo degli admonition (`!!! mascot-tip`),
  le chiavi del front matter, l'HTML/JS dei laboratori, i pulsanti Run/Reset.
- Restano in inglese i titoli dei concetti nelle liste "Concepts Covered" /
  "Concetti trattati" e nei file della learning graph.
- "turtle" può restare in inglese ("la turtle").
- Il valore di title/description nel front matter va tradotto.
- Un adattamento libero va bene se il significato e l'intento didattico
  restano gli stessi: non segnalare differenze di stile accettabili.

Severità:
- critical: uno studente imparerebbe qualcosa di sbagliato, oppure codice,
  quiz o laboratorio non funzionano più o non corrispondono al testo
- major: informazione persa, aggiunta o distorta in modo rilevante
- minor: grammatica, terminologia, scorrevolezza

Scrivi spiegazioni e suggerimenti in italiano. Cita brevi frammenti esatti
(max ~200 caratteri) del testo EN e IT. Se la traduzione è corretta,
restituisci una lista di problemi vuota. Valuta la sezione da 1 (pessima) a 5
(ottima)."""

SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "integer", "minimum": 1, "maximum": 5},
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "severity": {"enum": ["critical", "major", "minor"]},
                    "category": {"enum": ["meaning", "omission", "addition",
                                          "code", "prediction", "terminology",
                                          "untranslated", "grammar", "tone"]},
                    "english": {"type": "string"},
                    "italian": {"type": "string"},
                    "explanation": {"type": "string"},
                    "suggestion": {"type": "string"},
                },
                "required": ["severity", "category", "english", "italian",
                             "explanation", "suggestion"],
            },
        },
    },
    "required": ["score", "issues"],
}

SEVERITY_ORDER = {"critical": 0, "major": 1, "minor": 2}


def split_h2(text):
    """Divide il testo in sezioni che iniziano con '## ', ignorando i fence."""
    sections, current, in_fence = [], [], False
    for line in text.splitlines(keepends=True):
        if line.startswith("```"):
            in_fence = not in_fence
        if line.startswith("## ") and not in_fence and current:
            sections.append("".join(current))
            current = []
        current.append(line)
    sections.append("".join(current))
    return sections


def make_chunks(en_text, it_text):
    """Coppie (en, it) da inviare. I file grandi sono divisi per sezioni H2,
    ma solo se EN e IT hanno lo stesso numero di sezioni (allineamento sicuro)."""
    if len(en_text) <= CHUNK_CHARS:
        return [(en_text, it_text)]
    en_s, it_s = split_h2(en_text), split_h2(it_text)
    if len(en_s) != len(it_s):
        return [(en_text, it_text)]
    chunks, en_buf, it_buf = [], "", ""
    for a, b in zip(en_s, it_s):
        if en_buf and len(en_buf) + len(a) > CHUNK_CHARS:
            chunks.append((en_buf, it_buf))
            en_buf, it_buf = "", ""
        en_buf += a
        it_buf += b
    chunks.append((en_buf, it_buf))
    return chunks


def ask_claude(en, it, rel, part, total, model, workdir):
    prompt = (f"File: {rel} (parte {part}/{total})\n\n"
              f"<english>\n{en}\n</english>\n\n<italian>\n{it}\n</italian>")
    cmd = ["claude", "-p", "--model", model, "--tools", "",
           "--no-session-persistence", "--system-prompt", SYSTEM_PROMPT,
           "--output-format", "json", "--json-schema", json.dumps(SCHEMA)]
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                          timeout=900, cwd=workdir)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip()[:500])
    data = json.loads(proc.stdout)
    if data.get("is_error") or "structured_output" not in data:
        raise RuntimeError(str(data.get("result", data))[:500])
    return data["structured_output"], data.get("total_cost_usd", 0.0)


def review_file(rel, en_path, it_path, cache_path, model, workdir):
    en_text = en_path.read_text(encoding="utf-8")
    it_text = it_path.read_text(encoding="utf-8")
    digest = hashlib.sha256(
        (PROMPT_VERSION + model + en_text + "\0" + it_text).encode()).hexdigest()
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        if cached.get("hash") == digest:
            return rel, cached, True

    chunks = make_chunks(en_text, it_text)
    issues, scores, cost = [], [], 0.0
    for n, (en, it) in enumerate(chunks, 1):
        out, c = ask_claude(en, it, rel, n, len(chunks), model, workdir)
        cost += c or 0.0
        scores.append(out["score"])
        for issue in out["issues"]:
            issue["part"] = n
            issues.append(issue)

    result = {"file": rel, "hash": digest, "model": model,
              "score": min(scores), "parts": len(chunks),
              "cost_usd": round(cost, 4), "issues": issues}
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(result, indent=2, ensure_ascii=False),
                          encoding="utf-8")
    return rel, result, False


def one_line(text):
    """Comprime una citazione su una riga, per non rompere il Markdown."""
    return re.sub(r"\s+", " ", text).strip()


def write_report(sem_dir, out_dir):
    results = [json.loads(p.read_text(encoding="utf-8"))
               for p in sorted(sem_dir.rglob("*.json"))]
    counts = {"critical": 0, "major": 0, "minor": 0}
    for r in results:
        for i in r["issues"]:
            counts[i["severity"]] += 1

    def rank(r):
        sev = min((SEVERITY_ORDER[i["severity"]] for i in r["issues"]),
                  default=9)
        return sev, r["score"], r["file"]

    lines = ["# Revisione semantica della traduzione", "",
             f"- File revisionati: {len(results)}",
             f"- Problemi: {counts['critical']} critici · {counts['major']} "
             f"importanti · {counts['minor']} minori",
             f"- Costo stimato: ${sum(r.get('cost_usd', 0) for r in results):.2f}",
             "", "| File | Voto | Critici | Importanti | Minori |",
             "|---|---|---|---|---|"]
    ranked = sorted(results, key=rank)
    for r in ranked:
        c = [sum(i["severity"] == s for i in r["issues"])
             for s in ("critical", "major", "minor")]
        if any(c) or r["score"] < 5:
            lines.append(f"| `{r['file']}` | {r['score']} | {c[0]} | {c[1]} "
                         f"| {c[2]} |")
    lines.append("")

    for r in ranked:
        if not r["issues"]:
            continue
        lines += [f"## `{r['file']}` — voto {r['score']}/5", ""]
        for i in sorted(r["issues"], key=lambda i: SEVERITY_ORDER[i["severity"]]):
            lines += [f"- **{i['severity']}** · {i['category']}"
                      + (f" · parte {i['part']}" if r["parts"] > 1 else ""),
                      f"    - EN: {one_line(i['english'])}",
                      f"    - IT: {one_line(i['italian'])}",
                      f"    - Perché: {one_line(i['explanation'])}",
                      f"    - Proposta: {one_line(i['suggestion'])}"]
        lines.append("")
    report = out_dir / "semantic.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    return report, counts


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--en", default="../Imparare-python/docs",
                    help="cartella docs inglese")
    ap.add_argument("--it", default="docs", help="cartella docs italiana")
    ap.add_argument("--out", default="logs/translation-check",
                    help="cartella dei risultati")
    ap.add_argument("--only", action="append", default=[],
                    help="glob sul percorso relativo (ripetibile), "
                         "es. 'chapters/*'")
    ap.add_argument("--skip", action="append",
                    default=[".ipynb_checkpoints/*", "*/.ipynb_checkpoints/*"],
                    help="glob da escludere (ripetibile)")
    ap.add_argument("--model", default="sonnet",
                    help="modello Claude (sonnet, opus, ...)")
    ap.add_argument("--jobs", type=int, default=4,
                    help="richieste in parallelo")
    ap.add_argument("--limit", type=int, help="rivedi al massimo N file")
    ap.add_argument("--report-only", action="store_true",
                    help="rigenera il report senza chiamare Claude")
    args = ap.parse_args()

    en_root, it_root, out_dir = Path(args.en), Path(args.it), Path(args.out)
    sem_dir = out_dir / "semantic"

    if not args.report_only:
        rels = sorted(p.relative_to(en_root).as_posix()
                      for p in en_root.rglob("*.md")
                      if (it_root / p.relative_to(en_root)).exists())
        if args.only:
            rels = [r for r in rels
                    if any(fnmatch.fnmatch(r, g) for g in args.only)]
        rels = [r for r in rels
                if not any(fnmatch.fnmatch(r, g) for g in args.skip)]
        if args.limit:
            rels = rels[:args.limit]
        print(f"File da revisionare: {len(rels)} (modello {args.model}, "
              f"{args.jobs} in parallelo)")

        failed = []
        # cwd vuota: la CLI non carica CLAUDE.md o impostazioni del progetto
        with tempfile.TemporaryDirectory() as workdir, \
                ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {
                pool.submit(review_file, rel, en_root / rel, it_root / rel,
                            sem_dir / (rel + ".json"), args.model,
                            workdir): rel
                for rel in rels}
            for done, fut in enumerate(as_completed(futures), 1):
                rel = futures[fut]
                try:
                    _, res, cached = fut.result()
                    tag = "cache" if cached else f"${res['cost_usd']:.3f}"
                    print(f"[{done}/{len(rels)}] {rel}: voto {res['score']}, "
                          f"{len(res['issues'])} problemi ({tag})", flush=True)
                except Exception as e:  # noqa: BLE001 — continua con gli altri
                    failed.append(rel)
                    print(f"[{done}/{len(rels)}] {rel}: ERRORE {e}",
                          file=sys.stderr, flush=True)
        if failed:
            print(f"\n{len(failed)} file falliti (rilancia per riprovare): "
                  f"{failed}", file=sys.stderr)

    report, counts = write_report(sem_dir, out_dir)
    print(f"\nProblemi: {counts['critical']} critici, {counts['major']} "
          f"importanti, {counts['minor']} minori")
    print(f"Report: {report}")


if __name__ == "__main__":
    main()
