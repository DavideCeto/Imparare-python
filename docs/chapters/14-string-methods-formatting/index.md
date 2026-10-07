---
title: Metodi delle Stringhe e Formattazione
description: Padroneggia l'indicizzazione e lo slicing delle stringhe, split/join/replace, le f-string, e la formattazione multilinea per un output di programma pulito
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:20:00
version: 0.09
---

# Metodi delle Stringhe e Formattazione

Alla fine di questa lezione sarai in grado di:

- Accedere a singoli caratteri usando l'**indicizzazione delle stringhe** ed estrarre sottostringhe usando lo **slicing**
- Usare `split()`, `join()`, `replace()`, `find()`, `startswith()`, ed `endswith()` per lavorare con il testo
- Costruire stringhe di output pulite usando le **f-string** — il modo moderno di Python per incorporare variabili nel testo
- Formattare output multilinea per far sembrare i tuoi programmi professionali

Le stringhe sono ovunque nella programmazione. Nomi utente, messaggi, nomi di file, indirizzi web — tutto testo.
Python ti dà un enorme set di strumenti di metodi delle stringhe così puoi tagliare, cercare, sostituire, e formattare il testo con solo poche righe di codice.

!!! mascot-welcome "Benvenuto/a al Capitolo 14!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le stringhe sono uno degli strumenti più utili nella tua cassetta degli attrezzi Python!
    Oggi imparerai come tagliarle, cercarle, sostituire parti, e formattare un output bellissimo.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Indicizzazione delle Stringhe

Ogni carattere in una stringa ha un **numero di posizione** chiamato **indice**.
Python inizia a contare da zero — quindi il primo carattere è all'indice `0`, il secondo all'`1`, e così via.

Accedi a un carattere usando le parentesi quadre: `word[index]`.

```
word = "Python"
         P  y  t  h  o  n
index:   0  1  2  3  4  5
```

Puoi anche contare all'indietro dalla fine usando numeri negativi:

```
         P   y   t   h   o   n
index:   0   1   2   3   4   5
         -6  -5  -4  -3  -2  -1
```

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
initCmLab('', `word = "Python"
print("First character:", word[0])
print("Third character:", word[2])
print("Last character:", word[-1])
print("Second to last:", word[-2])`);
</script>

## Slicing delle Stringhe

Lo **slicing** estrae una porzione (una "fetta") di una stringa.
La sintassi è `word[start:end]` — ti dà i caratteri da `start` fino a (ma NON includendo) `end`.

```python
word = "Python"
print(word[0:3])   # "Pyt" — indexes 0, 1, 2
print(word[2:5])   # "tho" — indexes 2, 3, 4
print(word[:3])    # "Pyt" — same as [0:3]
print(word[3:])    # "hon" — from 3 to the end
print(word[:])     # "Python" — the whole string
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di eseguire il codice sotto, prevedi cosa stamperà `"programming"[3:8]`.
    Conta i caratteri partendo dall'indice 0. Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `s = "programming"
print(s[3:8])
print(s[:4])
print(s[-4:])
print(s[::2])   # every other character (step of 2)`);
</script>

Avevi indovinato? `s[3:8]` ti dà `"gramm"` — i caratteri nelle posizioni 3, 4, 5, 6, e 7.

La notazione `::2` è uno **step** — `s[::2]` prende ogni secondo carattere.

### Guardalo: Fai lo Slice con le Tue Mani

Lo slicer sotto trasforma la notazione di slicing in qualcosa che puoi afferrare. Trascina la maniglia verde di **start** e la maniglia rossa di **end** e guarda la notazione `word[2:7]` aggiornarsi dal vivo. Prima di trascinare qualcosa, prevedi: **dove devono stare le due maniglie per estrarre `"ROCKS"`?**

<iframe src="../../sims/string-slicer/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim String Slicer](../../sims/string-slicer/index.md){ .md-button }

Nota che la maniglia rossa di fine sta sempre **una posizione dopo** l'ultima lettera selezionata — l'indice di fine non è mai incluso. Clicca su qualsiasi singola tessera per vedere l'indicizzazione semplice come `word[3]`, scrivi la tua parola, oppure clicca **New Challenge** per esercitarti.

## Split, Join, e Replace

Tre dei metodi delle stringhe più usati sono `split()`, `join()`, e `replace()`.

Prima di guardare gli esempi, ecco un'anteprima veloce:
- `split()` spezza una stringa in una **lista** di pezzi
- `join()` incolla di nuovo insieme una lista di stringhe
- `replace()` scambia ogni occorrenza di una sottostringa con un'altra

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
initCmLab('-3', `sentence = "the quick brown fox"

# split() — break into words
words = sentence.split()
print("Words:", words)
print("Number of words:", len(words))

# join() — glue back together with dashes
dashed = "-".join(words)
print("Dashed:", dashed)

# replace() — swap one word for another
new_sentence = sentence.replace("fox", "python")
print("Replaced:", new_sentence)`);
</script>

| Metodo | Cosa fa | Esempio |
|--------|-------------|---------|
| `s.split()` | Divide sugli spazi | `"a b c".split()` → `["a","b","c"]` |
| `s.split(",")` | Divide sulle virgole | `"a,b,c".split(",")` → `["a","b","c"]` |
| `"-".join(lst)` | Unisce con dei trattini | `"-".join(["a","b"])` → `"a-b"` |
| `s.replace("x","y")` | Sostituisce x con y | `"fox".replace("x","t")` → `"fot"` |

## Cercare nelle Stringhe

Python ti offre diversi metodi per cercare dentro una stringa:

- `s.find("x")` — restituisce l'indice della prima occorrenza di `"x"`, o `-1` se non trovata
- `s.startswith("x")` — restituisce `True` se la stringa inizia con `"x"`
- `s.endswith("x")` — restituisce `True` se la stringa finisce con `"x"`
- `s.isdigit()` — restituisce `True` se tutti i caratteri sono cifre (nessuna lettera, nessuno spazio)
- `s.isalpha()` — restituisce `True` se tutti i caratteri sono lettere
- `s.isalnum()` — restituisce `True` se tutti i caratteri sono lettere o cifre

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
initCmLab('-4', `filename = "report2024.pdf"

print("Find '.pdf':", filename.find(".pdf"))
print("Starts with 'report':", filename.startswith("report"))
print("Ends with '.pdf':", filename.endswith(".pdf"))

code = "ABC123"
print("isalnum:", code.isalnum())
print("isdigit:", code.isdigit())
print("isalpha:", code.isalpha())`);
</script>

## Le f-String — Il Modo Moderno di Formattare il Testo

Una **f-string** (letterale di stringa formattata) ti permette di incorporare variabili direttamente dentro una stringa.
Metti una `f` prima della virgoletta di apertura e racchiudi ogni variabile in parentesi graffe `{}`.

Prima delle f-string, dovevi scrivere cose come:

```python
name = "Monty"
score = 95
print("Hello, " + name + "! Your score is " + str(score) + ".")
```

Con una f-string, diventa molto più pulito:

```python
print(f"Hello, {name}! Your score is {score}.")
```

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
initCmLab('-5', `name = "Monty"
score = 95
max_score = 100
percentage = score / max_score * 100

print(f"Hello, {name}!")
print(f"Your score: {score}/{max_score}")
print(f"Percentage: {percentage:.1f}%")   # .1f = 1 decimal place`);
</script>

Il codice di formato `:.1f` dentro le parentesi graffe dice "mostra 1 cifra decimale."
Prova a cambiarlo in `:.2f` per due cifre decimali.

## Confronto di Stringhe

Puoi confrontare le stringhe con `==`, `<`, e `>`.
Python confronta le stringhe alfabeticamente, carattere per carattere.

```python
print("apple" == "apple")   # True
print("apple" == "Apple")   # False — case-sensitive!
print("apple" < "banana")   # True — a comes before b
print("zebra" > "ant")      # True — z comes after a
```

Le maiuscole contano! `"apple" != "Apple"`. Usa `.lower()` su entrambi i lati se vuoi un confronto senza distinzione tra maiuscole e minuscole.

## Formattazione Multilinea delle Stringhe

Puoi creare una stringa che si estende su più righe usando le triple virgolette `"""..."""`.
Questo è perfetto per messaggi più lunghi o template:

```python
name = "Monty"
chapter = 14

report = f"""
===== Progress Report =====
Student:  {name}
Chapter:  {chapter}
Status:   Complete!
===========================
"""
print(report)
```

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Correggi il Saluto"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe stampare un saluto elegante usando una f-string,
    ma usa ancora il vecchio stile di concatenazione con `+` e si dimentica `str()` attorno al numero.
    Riscrivi la riga `print()` come una singola f-string per risolvere entrambi i problemi!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-6"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-6')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-6')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-6"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-6"></div>
  </div>
</div>
<script>
initCmLab('-6', `player = "Monty"
level = 5

# Rewrite this as one f-string:
print("Player: " + player + ", Level: " + str(level))`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Prova `"Python"[::-1]` — è uno slice con step `-1`.
   **Saprai che ha funzionato quando** vedi `nohtyP` (la stringa invertita!).

2. Usa `split(",")` per dividere la stringa `"red,green,blue,yellow"` e stampa ogni colore sulla sua riga.
   **Saprai che ha funzionato quando** vedi quattro righe, un colore ciascuna.

3. Usa `replace()` per censurare la parola `"bad"` in `"This is a bad example"`, sostituendola con `"***"`.
   **Saprai che ha funzionato quando** l'output legge `This is a *** example`.

4. Scrivi una f-string che mostra un ordine di pizza: ingrediente (ad es. `"cheese"`) e prezzo (ad es. `8.50`) con due cifre decimali.
   **Saprai che ha funzionato quando** vedi qualcosa come `Pizza: cheese — $8.50`.

5. Usa `startswith()` per controllare se un nome di file finisce con `".py"`. Stampa `"Python file!"` oppure `"Not a Python file"`.
   **Saprai che ha funzionato quando** `"hello.py"` dà un risultato e `"hello.txt"` dà l'altro.

!!! mascot-celebration "Maestro delle Stringhe!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato l'indicizzazione, lo slicing, split, join, replace, le f-string, e altro ancora!
    Queste competenze sulle stringhe appaiono in quasi ogni vero programma Python — dalle app web alla data science.
    Stai costruendo una cassetta degli attrezzi davvero impressionante! Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
