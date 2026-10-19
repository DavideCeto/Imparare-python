---
title: Input e Output su File
description: Leggi e scrivi file usando open(), l'istruzione with, le modalità dei file, l'iterazione sulle righe, e la gestione dei CSV
generated_by: claude skill chapter-content-generator
date: 2026-06-28 16:30:00
version: 0.09
---

# Input e Output su File

Alla fine di questa lezione sarai in grado di:

- Aprire un file per leggere o scrivere usando `open()` e l'istruzione `with`
- Leggere il contenuto di un file con `read()`, `readlines()`, e l'iterazione sulle righe
- Scrivere e aggiungere testo a un file con `write()`
- Leggere e scrivere semplici file CSV usando il modulo `csv` di Python

I programmi diventano molto più utili quando possono salvare dati tra un'esecuzione e l'altra.
Con l'I/O su file, i tuoi programmi possono ricordare i punteggi più alti, elaborare file di testo, e condividere dati con altri programmi.

!!! mascot-welcome "Benvenuto/a al Capitolo 26!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Oggi i tuoi programmi smettono di dimenticare tutto quando si chiudono!
    I file permettono ai tuoi programmi di salvare e caricare dati — un superpotere che apre un mondo completamente nuovo di progetti.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

!!! mascot-warning "L'I/O su File Richiede un Vero Ambiente Python"
    ![Monty with a warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Le vere operazioni su file — `open()`, `write()`, `read()` — accedono al disco del tuo computer.
    L'ambiente browser di Skulpt non può farlo, quindi i laboratori interattivi sotto **simulano** il comportamento dei file usando stringhe e liste Python.
    Per eseguire il vero codice `open()`/`with` mostrato nei blocchi di codice, usa **Thonny**, **VS Code**, o qualsiasi installazione Python locale.

## La Riga di Comando e la Navigazione nel File System

I file vivono in un **file system** organizzato come cartelle dentro cartelle.
Quando esegui uno script Python dal terminale, Python cerca i file in relazione alla **cartella di lavoro attuale** — la cartella in cui vive lo script.

```
cd foldername    # move into a folder
cd ..            # move up one level
ls               # list files (Mac/Linux)
dir              # list files (Windows)
```

## `open()` e le Modalità dei File

`open(filename, mode)` apre un file e restituisce un **oggetto file**.

La modalità dice a Python cosa vuoi fare con il file:

| Modalità | Significato |
|------|---------|
| `"r"` | Lettura (predefinita) — il file deve esistere |
| `"w"` | Scrittura — crea il file o sovrascrive il contenuto esistente |
| `"a"` | Aggiunta (append) — aggiunge alla fine senza eliminare il contenuto esistente |
| `"b"` | Binario — usato con `"rb"` o `"wb"` per immagini e altri file binari |

## L'Istruzione `with` — Gestione Sicura dei File

L'**istruzione `with`** apre un file, esegue il blocco indentato, poi chiude automaticamente il file — anche se si verifica un errore.

```python
with open("greeting.txt", "w") as f:
    f.write("Ciao da Python!\n")
# qui il file viene chiuso automaticamente
```

Usa sempre `with open(...)`. Previene il bug più comune sui file: dimenticare di chiudere il file.

## Scrivere su un File

`file.write(text)` scrive del testo nel file. **Non** aggiunge automaticamente un ritorno a capo — devi aggiungere tu stesso `"\n"`.

**Vero Python (Thonny / VS Code):**
```python
with open("notes.txt", "w") as f:
    f.write("Riga 1: Ciao, Python!\n")
    f.write("Riga 2: Sto scrivendo in un file.\n")
    f.write("Riga 3: È divertente!\n")
```

**Simulazione Skulpt** — usando una lista come "file" virtuale:

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto usa una lista per simulare la scrittura su un file e poi la lettura.
    In quale ordine appariranno le righe quando le leggiamo?
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
initCmLab('', `# File virtuale — una lista che conserva le righe "scritte"
virtual_file = []

def write_line(text):
    virtual_file.append(text)

# "Scrivi" tre righe:
write_line("Riga 1: Ciao, Python!")
write_line("Riga 2: Sto scrivendo in un file.")
write_line("Riga 3: È divertente!")

# "Rileggi" quello che abbiamo scritto:
print("Contenuto del file:")
for line in virtual_file:
    print(line)

print(f"\\nRighe totali: {len(virtual_file)}")`);
</script>

## Leggere da un File

Tre metodi leggono il contenuto di un file:

- `f.read()` — legge l'intero file come una grande stringa
- `f.readlines()` — legge tutte le righe in una lista (ogni riga include `\n`)
- `f.readline()` — legge una riga alla volta

**Vero Python:**
```python
with open("notes.txt") as f:
    content = f.read()
    print(content)
```

**Simulazione Skulpt** — dividendo una stringa multilinea:

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
initCmLab('-2', `# Simula un file di testo con una stringa su più righe:
file_content = "apple\\nbanana\\nmango\\nkiwi"

# Simula readlines() usando split("\\n"):
lines = file_content.split("\\n")
print("Numero di righe:", len(lines))
print()
for i, line in enumerate(lines, 1):
    print(f"  Riga {i}: {line.strip()}")`);
</script>

Nota la chiamata `.strip()` — rimuove gli spazi bianchi e `\n` dalle estremità delle righe.

## Iterare sulle Righe di un File

Il modo più pulito di elaborare un file riga per riga è un semplice ciclo `for`:

```python
with open("data.txt") as f:
    for line in f:
        line = line.strip()
        if line:   # salta le righe vuote
            print(line)
```

## Elaborazione del Testo con `strip()` e `lower()`

Quando elabori il contenuto di un file, pulisci sempre il testo prima:

- `.strip()` — rimuove gli spazi bianchi iniziali e finali
- `.lower()` — converte in minuscolo per confronti senza distinzione tra maiuscole e minuscole
- `.split()` — divide una riga in parole

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
initCmLab('-3', `# Simula un file disordinato con un elenco di parole:
words_text = "  Apple  \\nbanana\\n  MANGO\\nkiwi  \\n"

clean_words = []
for line in words_text.split("\\n"):
    word = line.strip().lower()
    if word:                        # salta le righe vuote
        clean_words.append(word)

print("Parole ripulite:", clean_words)
print("Ordinate:       ", sorted(clean_words))
print("Parola più lunga:", max(clean_words, key=len))`);
</script>

## Aggiungere a un File

La modalità `"a"` aggiunge alla fine di un file senza eliminare il contenuto esistente:

```python
with open("log.txt", "a") as f:
    f.write("Nuova voce aggiunta.\n")
```

Eseguilo più volte e il log crescerà — ogni esecuzione aggiunge una nuova riga.

## File CSV

**CSV** (Comma-Separated Values, valori separati da virgola) è uno dei formati di file più comuni per i dati tabulari.
Ogni riga è una linea; le colonne sono separate da virgole.

```
name,age,score
Alice,14,95
Bob,13,87
Carol,15,91
```

Il modulo `csv` di Python legge e scrive i file CSV in modo pulito.
`csv.DictReader` prende qualsiasi iterabile di stringhe — quindi possiamo passare direttamente `csv_text.splitlines()`, senza bisogno di un oggetto file.

`splitlines()` divide una stringa multilinea in una lista di righe — esattamente ciò di cui ha bisogno `csv.DictReader`.

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
initCmLab('-4', `import csv

csv_text = """name,age,score
Alice,14,95
Bob,13,87
Carol,15,91"""

# splitlines() funziona in Skulpt — non serve il modulo io
reader = csv.DictReader(csv_text.splitlines())
for row in reader:
    print(f"{row['name']}: età {row['age']}, punteggio {row['score']}")`);
</script>

`csv.DictReader` usa la prima riga (l'intestazione) come nomi delle colonne e ti dà ogni riga come un dizionario.

## Contare la Frequenza delle Parole — Un Mini Caso di Studio

Leggere del testo diventa potente quando inizi a fare domande su di esso. Un esercizio classico è contare quante volte appare ogni parola in un pezzo di testo — la stessa idea di base usata dai motori di ricerca e dai filtri antispam.

Il vero codice leggerebbe il testo da un file con `open()`; qui simuliamo un breve estratto con una stringa così gira direttamente nel browser. La punteggiatura viene rimossa un carattere alla volta prima di dividere il testo in parole:

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto conta le frequenze delle parole in un breve estratto.
    Quale parola pensi che apparirà più volte? Fai la tua previsione — poi eseguilo!

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
initCmLab('-6', `excerpt = "call me ishmael. some years ago, never mind how long precisely, having little or no money in my purse, i thought i would sail about a little and see the watery part of the world"

punctuation = ".,!?;:'-()"

clean = excerpt.lower()
for mark in punctuation:
    clean = clean.replace(mark, "")

words = clean.split()

counts = {}
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

for word, count in sorted(counts.items()):
    print(f"{word}: {count}")`);
</script>

Avevi indovinato? Parole brevi e comuni come "the" e "i" si ripetono di più in questo estratto — con un intero libro di testo, quel pattern diventa ancora più marcato.

Il Capitolo 29 mostra un modo più veloce di rimuovere la punteggiatura e dividere il testo usando le espressioni regolari.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Elabora il CSV"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto legge i punteggi degli studenti da una stringa CSV.
    Aggiungi del codice per calcolare e stampare la **media** dei punteggi dopo il ciclo.
    Dovrai prima convertire le stringhe dei punteggi in interi!

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
initCmLab('-5', `import csv

csv_text = "name,score\\nAlice,95\\nBob,87\\nCarol,91\\nDave,73"
reader = csv.DictReader(csv_text.splitlines())

total = 0
count = 0
for row in reader:
    score = int(row["score"])
    total += score
    count += 1
    print(f"{row['name']}: {score}")

# Aggiungi: calcola e stampa il punteggio medio`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia il CSV per aggiungere una quarta colonna `"grade"` con valori A/B/C. Stampa solo le righe dove grade == `"A"`.
   **Saprai che ha funzionato quando** appare solo la riga di Alice.

2. Usa `virtual_file` (una lista) per simulare una lista di cose da fare: "scrivi" tre compiti, poi stampa ognuno numerato 1, 2, 3.
   **Saprai che ha funzionato quando** ogni compito si stampa sulla sua riga numerata.

3. Conta quante parole appaiono in una stringa di testo multilinea usando `split()` e stampa il totale.
   **Saprai che ha funzionato quando** vedi il numero corretto di parole.

4. Leggi le righe da una stringa e filtra via qualsiasi riga che contiene la parola `"skip"`.
   **Saprai che ha funzionato quando** le righe contenenti "skip" non appaiono nell'output.

5. In Thonny o VS Code, crea un file chiamato `fruits.txt`, scrivi cinque nomi di frutta (uno per riga), poi riaprilo e stampa ogni riga con il suo numero di riga.
   **Saprai che ha funzionato quando** tutti i cinque frutti si stampano in un vero terminale Python con i loro numeri.

!!! mascot-celebration "Esperto di I/O su File!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    I tuoi programmi possono ora salvare e caricare dati dai file — inclusi i fogli di calcolo CSV!
    Questo apre la porta alla vera elaborazione dei dati, ai file di log, alla memorizzazione delle configurazioni, e molto altro.
    Per la vera esperienza, apri Thonny e pratica `open()` sul tuo computer. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
