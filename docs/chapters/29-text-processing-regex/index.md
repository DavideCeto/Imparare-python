---
title: Elaborazione del Testo ed Espressioni Regolari
description: Impara le espressioni regolari — search, findall, split, sub, le classi di caratteri, i quantificatori, i gruppi, e i pattern compilati
generated_by: claude skill chapter-content-generator
date: 2026-06-28 14:50:00
version: 0.09
---

# Elaborazione del Testo ed Espressioni Regolari

Alla fine di questa lezione sarai in grado di:

- Scrivere **espressioni regolari** di base per far corrispondere pattern nel testo
- Usare `re.search()`, `re.findall()`, `re.split()`, e `re.sub()` per cercare e trasformare il testo
- Costruire pattern usando classi di caratteri, quantificatori, ancore, e gruppi
- Usare le **stringhe raw** (`r"..."`) per evitare confusione con le barre inverse

Le espressioni regolari (regex) sono un mini-linguaggio per descrivere pattern di testo.
Con una singola regex, puoi trovare numeri di telefono, validare indirizzi email, o estrarre dati da migliaia di righe di testo.

!!! mascot-welcome "Benvenuto/a al Capitolo 29!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le espressioni regolari sembrano spaventose all'inizio — ma una volta che imparerai i blocchi costitutivi, sono incredibilmente potenti.
    Una riga di regex può fare quello che richiederebbe 20 righe di metodi delle stringhe.
    Decifriamo il mistero! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Modulo `re`

Importa il modulo delle regex di Python con `import re`.

Le funzioni principali sono:

| Funzione | Restituisce | Usala quando |
|----------|---------|---------|
| `re.search(pattern, text)` | Oggetto match o `None` | Controlli se il pattern appare ovunque |
| `re.findall(pattern, text)` | Lista di tutte le corrispondenze | Vuoi ogni occorrenza |
| `re.split(pattern, text)` | Lista di pezzi | Vuoi dividere il testo in base a un pattern |
| `re.sub(pattern, replacement, text)` | Nuova stringa | Vuoi sostituire le corrispondenze |

## Stringhe Raw

I pattern regex usano molto le barre inverse — `\d`, `\w`, `\s`.
Nelle normali stringhe Python, `\d` viene trattato come una sequenza di escape speciale.
Per evitare confusione, scrivi sempre i pattern regex come **stringhe raw** mettendo `r` prima della virgoletta: `r"\d"`.

```python
# Senza raw string: Python interpreta \n come un a capo
pattern = "\n"   # carattere di a capo

# Con la raw string: Python passa \n così com'è al motore delle regex
pattern = r"\n"  # i due caratteri barra rovesciata + n
```

**Regola: usa sempre `r"..."` per i pattern regex.**

## Elementi di Base del Pattern

Prima di scrivere veri pattern, ecco i blocchi costitutivi:

| Pattern | Corrisponde a |
|---------|---------|
| `.` | Qualsiasi carattere singolo (eccetto il ritorno a capo) |
| `\d` | Una cifra (0–9) |
| `\w` | Un carattere di parola (lettera, cifra, underscore) |
| `\s` | Un carattere di spazio bianco (spazio, tab, ritorno a capo) |
| `\D` | Non una cifra |
| `\W` | Non un carattere di parola |
| `\S` | Non uno spazio bianco |
| `^` | Inizio della stringa |
| `$` | Fine della stringa |

## Quantificatori

I quantificatori controllano quante volte si ripete un elemento del pattern:

| Quantificatore | Significato | Esempio |
|-----------|---------|---------|
| `*` | 0 o più volte | `\d*` — zero o più cifre |
| `+` | 1 o più volte | `\d+` — una o più cifre |
| `?` | 0 o 1 volta | `\d?` — cifra opzionale |
| `{n}` | Esattamente n volte | `\d{3}` — esattamente 3 cifre |
| `{n,m}` | Tra n e m volte | `\d{2,4}` — da 2 a 4 cifre |

## `re.search()` — Trova la Prima Corrispondenza

`re.search(pattern, text)` scorre `text` cercando la prima posizione dove il pattern corrisponde.
Restituisce un **oggetto match** se trovato, oppure `None` se non trovato.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto cerca un pattern di numero di telefono in diverse stringhe.
    Quali stringhe pensi che corrisponderanno al pattern `\d{3}-\d{4}`?
    Fai la tua previsione — poi eseguilo!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `import re

texts = [
    "Call me at 555-1234!",
    "My number is 867-5309.",
    "No number here.",
    "Fax: 123-4567 or 987-6543"
]

for t in texts:
    match = re.search(r"\\d{3}-\\d{4}", t)
    if match:
        print(f"Trovato in: {t!r}")
        print(f"  Corrispondenza: {match.group()}")
    else:
        print(f"Nessuna corrispondenza in: {t!r}")`);
</script>

`match.group()` restituisce il testo che è stato trovato.

## `re.findall()` — Trova Tutte le Corrispondenze

`re.findall(pattern, text)` restituisce una **lista** di ogni corrispondenza non sovrapposta.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `import re

text = "Prices: $5.99, $12.00, $3.50, and $100.00"

prices = re.findall(r"\\$\\d+\\.\\d{2}", text)
print("Prezzi trovati:", prices)

# Trova tutte le parole (sequenze di lettere):
words = re.findall(r"[A-Za-z]+", text)
print("Parole trovate:", words)`);
</script>

### Guardalo: Il Laboratorio di Corrispondenza Regex

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il laboratorio sotto inizia con il pattern `\d{3}-\d{4}`. Leggi i chip sotto
    il riquadro del pattern, poi prevedi: **quali parti del testo di esempio si
    illumineranno — e quante corrispondenze segnalerà findall?**

<iframe src="../../sims/regex-match-lab/main.html" height="372" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Regex Match Lab](../../sims/regex-match-lab/index.md){ .md-button }

Ora sperimenta: elimina il `-` dal pattern e guarda le corrispondenze cambiare istantaneamente. Prova ogni pulsante preset, poi costruisci il tuo proprio pattern un carattere alla volta. La striscia dei chip traduce sempre il tuo pattern in inglese semplice — la regex smette di essere magica una volta che riesci a leggerla ad alta voce.

## Classi di Caratteri

Una **classe di caratteri** è un insieme di caratteri tra parentesi quadre. Corrisponde a qualsiasi singolo carattere nell'insieme.

| Pattern | Corrisponde a |
|---------|---------|
| `[aeiou]` | Qualsiasi vocale minuscola |
| `[A-Z]` | Qualsiasi lettera maiuscola |
| `[a-z]` | Qualsiasi lettera minuscola |
| `[0-9]` | Qualsiasi cifra (come `\d`) |
| `[^aeiou]` | Qualsiasi carattere che NON è una vocale |

## `re.split()` — Dividi in Base al Pattern

`re.split(pattern, text)` divide il testo ovunque il pattern corrisponda — come `str.split()` ma con il potere della regex.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `import re

# Divide su qualsiasi punteggiatura (,  ;  :  o spazio):
sentence = "apples, bananas; oranges: mangoes kiwis"
fruits = re.split(r"[,;:\\s]+", sentence)
print("Frutti:", fruits)

# Divide su più spazi bianchi:
text = "hello    world\\t\\tpython"
words = re.split(r"\\s+", text)
print("Parole:", words)`);
</script>

## `re.sub()` — Sostituisci le Corrispondenze

`re.sub(pattern, replacement, text)` sostituisce ogni corrispondenza con la stringa di sostituzione.

```python
import re

# Rimuove tutte le cifre da una stringa:
cleaned = re.sub(r"\d", "", "Hello123World456")
print(cleaned)   # "HelloWorld"

# Sostituisce più spazi con uno solo:
normalized = re.sub(r"\s+", " ", "too   many    spaces")
print(normalized)   # "too many spaces"
```

## Ancore: Inizio e Fine

`^` corrisponde all'inizio della stringa.
`$` corrisponde alla fine.

```python
# Corrisponde solo se la stringa inizia con "Hello":
if re.search(r"^Hello", text):
    print("Inizia con Hello")

# Corrisponde solo se la stringa finisce con una cifra:
if re.search(r"\d$", text):
    print("Finisce con una cifra")
```

## Alternanza con `|`

`|` significa "oppure" — corrisponde al pattern di sinistra o a quello di destra.

```python
import re

pattern = r"cat|dog|rabbit"
matches = re.findall(pattern, "I have a cat, a dog, and a rabbit.")
print(matches)   # ['cat', 'dog', 'rabbit']
```

## Gruppi con le Parentesi

Le parentesi `()` creano un **gruppo** — ti permettono di catturare parti specifiche di una corrispondenza.

```python
import re

text = "Born: 2010-06-15"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if match:
    year, month, day = match.group(1), match.group(2), match.group(3)
    print(f"Anno={year}, Mese={month}, Giorno={day}")
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `import re

emails = [
    "alice@example.com",
    "bob.smith@school.edu",
    "not-an-email",
    "carol@work.org"
]

# Pattern semplice per le email: parola@parola.parola
pattern = r"(\\w[\\w.]+)@(\\w+\\.\\w+)"

for email in emails:
    match = re.search(pattern, email)
    if match:
        user, domain = match.group(1), match.group(2)
        print(f"Valida: utente={user}, dominio={domain}")
    else:
        print(f"Non valida: {email!r}")`);
</script>

## Escape dei Caratteri Speciali

Alcuni caratteri hanno un significato speciale nella regex: `.`, `*`, `+`, `?`, `(`, `)`, `[`, `]`, `{`, `}`, `^`, `$`, `|`, `\`.
Per farli corrispondere letteralmente, fai l'escape con una barra inversa: `\.` corrisponde a un punto letterale.

```python
# Corrisponde a un punto letterale (non a "qualsiasi carattere"):
re.findall(r"\d+\.\d+", "3.14 and 2.71 and hello.world")
# → ['3.14', '2.71']
```

## Pattern Regex Compilati

Se usi lo stesso pattern molte volte, **compilalo** prima per una migliore prestazione:

```python
import re

digit_pattern = re.compile(r"\d+")   # compilato una volta sola

for text in many_strings:
    matches = digit_pattern.findall(text)   # usato più volte
```

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Estrai i Numeri di Telefono"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto dovrebbe estrarre tutti i numeri di telefono dal testo.
    Il pattern corrisponde solo a numeri di 3 cifre. Correggi il pattern per corrispondere al formato completo `NNN-NNN-NNNN`!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-5"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-5')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-5')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-5"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-5"></div>
  </div>
</div>
<script>
initCmLab('-5', `import re

text = "Contact us at 800-555-1234 or 415-867-5309. Fax: 888-123-4567."

# Bug: il pattern trova solo 3 cifre!
phones = re.findall(r"\\d{3}", text)
print("Trovati:", phones)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Usa `re.findall(r"\b\w{5}\b", text)` per trovare tutte le parole di 5 lettere in una frase. `\b` è un confine di parola.
   **Saprai che ha funzionato quando** vedi solo parole di 5 lettere.

2. Usa `re.sub(r"\b\d+\b", "NUM", "I have 3 cats and 12 birds")` per sostituire tutti i numeri con "NUM".
   **Saprai che ha funzionato quando** vedi `"I have NUM cats and NUM birds"`.

3. Valida una password: almeno 8 caratteri, almeno una cifra. Usa `re.search(r"^.{8,}$", pw)` e `re.search(r"\d", pw)`.
   **Saprai che ha funzionato quando** `"abc12345"` passa e `"abc123"` fallisce (troppo corta).

4. Usa `re.split(r"\s*,\s*", "Alice , Bob,  Carol, Dave")` per dividere una lista separata da virgole ignorando gli spazi extra.
   **Saprai che ha funzionato quando** vedi quattro nomi puliti.

5. Compila il pattern `r"\d{4}"` e usalo per trovare tutti gli anni di 4 cifre in una frase sulla storia.
   **Saprai che ha funzionato quando** vedi una lista di anni.

!!! mascot-celebration "Mago delle Regex!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Le espressioni regolari sono un superpotere — un singolo pattern può cercare attraverso milioni di righe di testo!
    Appaiono nel web scraping, nella validazione dei dati, nell'analisi dei log, e in quasi ogni compito di elaborazione del testo.
    Hai appena aggiunto uno strumento serio alla tua cassetta degli attrezzi da programmatore. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
