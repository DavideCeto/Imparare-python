#!/usr/bin/env python3
"""
Controllo strutturale della traduzione EN -> IT.

Confronta ogni file .md della versione inglese con il corrispondente file
italiano e segnala le differenze che di solito indicano un errore di
traduzione: codice modificato, blocchi mancanti, paragrafi non tradotti,
risposte dei quiz cambiate, lunghezze anomale.

Nessuna dipendenza esterna (solo libreria standard).

Esempio:
  python scripts/check_translation.py \
      --en ../Imparare-python/docs --it docs \
      --out logs/translation-check
"""

import argparse
import difflib
import json
import re
from pathlib import Path

FENCE_RE = re.compile(r"^```[^\n]*\n(.*?)^```", re.DOTALL | re.MULTILINE)
LAB_RE = re.compile(r"initCmLab\(\s*'[^']*'\s*,\s*`(.*?)`\s*\)", re.DOTALL)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
QUIZ_ANSWER_RE = re.compile(r"\*\*([A-F])\*\*")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")

# Elementi strutturali da contare: nome -> regex (MULTILINE)
COUNTERS = {
    "headings": re.compile(r"^#{1,6} ", re.MULTILINE),
    "admonitions": re.compile(r"^\s*(?:!!!|\?\?\?\+?) ", re.MULTILINE),
    "code_blocks": re.compile(r"^```", re.MULTILINE),
    "skulpt_labs": re.compile(r"initCmLab\("),
    "iframes": re.compile(r"<iframe"),
    "images": IMAGE_RE,
    "table_rows": re.compile(r"^\|", re.MULTILINE),
    "list_items": re.compile(r"^\s*(?:[-*+]|\d+\.) ", re.MULTILINE),
    "quiz_questions": re.compile(r"^#### \d+\.", re.MULTILINE),
}

# Parole molto frequenti: servono a capire se un paragrafo è rimasto in inglese
EN_WORDS = set("""the and is are you your this that with for of to in it be can
will what when how which have has was were they their there from by or not an
if then each into about would should could just like""".split())
IT_WORDS = set("""il lo la le gli di che è e un una per con non sono del della
dei delle nel nella al alla questo questa come quando se ogni puoi tuo tua
anche più si da ma o cosa""".split())

SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}


def strip_frontmatter(text):
    return FRONTMATTER_RE.sub("", text, count=1)


def extract_code(text):
    """Tutti i blocchi di codice (fenced + laboratori Skulpt), in ordine."""
    blocks = [m.group(1) for m in FENCE_RE.finditer(text)]
    blocks += [m.group(1) for m in LAB_RE.finditer(text)]
    return blocks


def code_skeleton(code):
    """Codice senza commenti e senza contenuto delle stringhe.

    Se due blocchi hanno lo stesso scheletro, la differenza riguarda solo
    commenti o testo nelle stringhe (traduzione legittima); altrimenti è
    cambiata la logica del programma.
    """
    code = re.sub(r'"""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\'', '""', code)
    code = re.sub(r'"(?:\\.|[^"\\\n])*"', '""', code)
    code = re.sub(r"'(?:\\.|[^'\\\n])*'", "''", code)
    code = re.sub(r"#.*", "", code)
    return [ln.rstrip() for ln in code.splitlines() if ln.strip()]


def prose_paragraphs(text):
    """Paragrafi di prosa: senza codice, HTML, frontmatter."""
    text = strip_frontmatter(text)
    text = FENCE_RE.sub("", text)
    text = re.sub(r"<script>.*?</script>", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"`[^`\n]+`", "", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text)]
    return [p for p in paras if len(p) > 0]


def looks_english(para):
    words = re.findall(r"[a-zàèéìòù']+", para.lower())
    if len(words) < 8:
        return False
    en = sum(w in EN_WORDS for w in words)
    it = sum(w in IT_WORDS for w in words)
    return en >= 4 and en > 2 * it


def check_pair(rel, en_text, it_text):
    issues = []

    def add(sev, kind, msg, detail=None):
        issues.append({"severity": sev, "kind": kind, "message": msg,
                       "detail": detail})

    # 1. Codice
    en_code, it_code = extract_code(en_text), extract_code(it_text)
    if len(en_code) != len(it_code):
        add("error", "code-count",
            f"blocchi di codice: EN {len(en_code)}, IT {len(it_code)}")
    for i, (a, b) in enumerate(zip(en_code, it_code), 1):
        if a == b:
            continue
        diff = "\n".join(difflib.unified_diff(
            a.splitlines(), b.splitlines(), "EN", "IT", lineterm="", n=1))
        if code_skeleton(a) == code_skeleton(b):
            add("info", "code-strings",
                f"blocco di codice #{i}: cambiati solo commenti/stringhe", diff)
        else:
            add("error", "code-logic",
                f"blocco di codice #{i}: la logica del codice è diversa", diff)

    # 2. Struttura
    for name, rx in COUNTERS.items():
        a, b = len(rx.findall(en_text)), len(rx.findall(it_text))
        if a != b:
            sev = "error" if name in ("skulpt_labs", "quiz_questions",
                                      "admonitions", "iframes") else "warning"
            add(sev, f"count-{name}", f"{name}: EN {a}, IT {b}")

    # 3. Risposte dei quiz
    if rel.endswith("quiz.md"):
        a = QUIZ_ANSWER_RE.findall(en_text)
        b = QUIZ_ANSWER_RE.findall(it_text)
        if a != b:
            pos = [i + 1 for i, (x, y) in enumerate(zip(a, b)) if x != y]
            add("error", "quiz-answers",
                f"lettere delle risposte diverse (EN {''.join(a)}, "
                f"IT {''.join(b)}; posizioni {pos})")

    # 4. Immagini e link
    for name, rx in (("images", IMAGE_RE), ("links", LINK_RE)):
        a, b = rx.findall(en_text), rx.findall(it_text)
        missing = sorted(set(a) - set(b))
        if missing:
            add("warning", f"{name}-changed",
                f"{name} presenti in EN ma non in IT: {missing[:5]}"
                + (" ..." if len(missing) > 5 else ""))

    # 5. Lunghezza della prosa
    en_len = sum(len(p) for p in prose_paragraphs(en_text))
    it_len = sum(len(p) for p in prose_paragraphs(it_text))
    if en_len > 300:
        ratio = it_len / en_len
        if ratio < 0.85:
            add("warning", "length",
                f"prosa IT molto più corta (rapporto {ratio:.2f}): "
                "possibili omissioni")
        elif ratio > 1.6:
            add("warning", "length",
                f"prosa IT molto più lunga (rapporto {ratio:.2f}): "
                "possibili aggiunte")

    # 6. Paragrafi rimasti in inglese
    en_paras = set(prose_paragraphs(en_text))
    leftover = [p for p in prose_paragraphs(it_text)
                if looks_english(p) or (p in en_paras and len(p) > 60
                                        and looks_english(p))]
    if leftover:
        add("warning", "untranslated",
            f"{len(leftover)} paragrafo/i sembrano ancora in inglese",
            "\n\n".join(p[:200] for p in leftover[:5]))

    return issues


def write_report(results, missing, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "structural.json").write_text(
        json.dumps({"missing": missing, "files": results}, indent=2,
                   ensure_ascii=False), encoding="utf-8")

    totals = {"error": 0, "warning": 0, "info": 0}
    for issues in results.values():
        for i in issues:
            totals[i["severity"]] += 1

    lines = ["# Controllo strutturale della traduzione", "",
             f"- File con problemi: {len(results)}",
             f"- Errori: {totals['error']} · Avvisi: {totals['warning']} · "
             f"Info: {totals['info']}", ""]
    if missing:
        lines += ["## File mancanti", ""] + [f"- `{m}`" for m in missing] + [""]

    def file_rank(item):
        return min(SEVERITY_ORDER[i["severity"]] for i in item[1]), item[0]

    for rel, issues in sorted(results.items(), key=file_rank):
        lines += [f"## `{rel}`", ""]
        for i in sorted(issues, key=lambda i: SEVERITY_ORDER[i["severity"]]):
            lines.append(f"- **{i['severity']}** `{i['kind']}` — {i['message']}")
            if i["detail"]:
                lines += ["", "  ```", *("  " + ln for ln in
                                          i["detail"].splitlines()), "  ```",
                          ""]
        lines.append("")
    (out_dir / "structural.md").write_text("\n".join(lines), encoding="utf-8")
    return totals


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--en", default="../Imparare-python/docs",
                    help="cartella docs inglese")
    ap.add_argument("--it", default="docs", help="cartella docs italiana")
    ap.add_argument("--out", default="logs/translation-check",
                    help="cartella dove scrivere il report")
    args = ap.parse_args()

    en_root, it_root = Path(args.en), Path(args.it)
    en_files = {p.relative_to(en_root).as_posix() for p in en_root.rglob("*.md")}
    it_files = {p.relative_to(it_root).as_posix() for p in it_root.rglob("*.md")}
    missing = [f"IT manca: {f}" for f in sorted(en_files - it_files)]
    missing += [f"EN manca: {f}" for f in sorted(it_files - en_files)]

    results = {}
    for rel in sorted(en_files & it_files):
        en_text = (en_root / rel).read_text(encoding="utf-8")
        it_text = (it_root / rel).read_text(encoding="utf-8")
        issues = check_pair(rel, en_text, it_text)
        if issues:
            results[rel] = issues

    totals = write_report(results, missing, Path(args.out))
    print(f"Coppie confrontate: {len(en_files & it_files)}")
    print(f"File con problemi: {len(results)} — errori {totals['error']}, "
          f"avvisi {totals['warning']}, info {totals['info']}")
    print(f"Report: {Path(args.out) / 'structural.md'}")


if __name__ == "__main__":
    main()
