---
title: Libreria Standard e JSON
description: Esplora la libreria standard di Python — moduli personalizzati, json, sys, os, collections, itertools, datetime — e impara a leggere/scrivere file JSON
generated_by: claude skill chapter-content-generator
date: 2026-06-28 14:30:00
version: 0.09
---

# Libreria Standard e JSON

Alla fine di questa lezione sarai in grado di:

- Creare il tuo proprio modulo Python e usare il guardiano `__name__ == "__main__"`
- Caricare e salvare dati in **formato JSON** usando `json.loads()`, `json.dumps()`, `json.load()`, e `json.dump()`
- Usare i moduli chiave della libreria standard: `sys`, `os`, `collections`, `itertools`, e `datetime`
- Controllare se un file esiste e gestire i percorsi dei file con `os.path`

Python viene fornito con un'enorme libreria di moduli pronti all'uso.
Questo capitolo esplora i più utili e ti insegna come organizzare il tuo codice in moduli.

!!! mascot-welcome "Benvenuto/a al Capitolo 27!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La libreria standard di Python è come un'enorme cassetta degli attrezzi — viene gratis con ogni installazione di Python.
    Oggi esploreremo gli strumenti più utili e imparerai a lavorare con JSON, il formato di dati universale del web.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Creare Moduli Personalizzati

Un **modulo** è semplicemente un file `.py` che contiene funzioni e variabili che vuoi riutilizzare.
Qualsiasi file Python può essere importato da un altro file nella stessa cartella.

Supponi di creare `mymath.py`:

```python
# mymath.py
PI = 3.14159

def circle_area(r):
    return PI * r * r

def circle_circumference(r):
    return 2 * PI * r
```

Poi nel tuo programma principale:

```python
import mymath
print(mymath.circle_area(5))
```

## Il Guardiano `__name__ == "__main__"`

Quando Python importa un modulo, esegue tutto il codice al livello più alto.
Questo può causare problemi se il tuo modulo contiene codice di test che vuoi eseguire solo direttamente — non quando viene importato.

Il **guardiano `__name__ == "__main__"`** racchiude il codice di test così che giri solo quando il file viene eseguito direttamente:

```python
# mymath.py
def circle_area(r):
    return 3.14159 * r * r

if __name__ == "__main__":
    # This block only runs when you run mymath.py directly
    # It does NOT run when you do: import mymath
    print("Testing circle_area:", circle_area(5))
```

Metti sempre il codice di test e la logica dello script dentro questo guardiano nei file dei moduli.

## Il Modulo `sys`

Il modulo `sys` ti dà informazioni sull'interprete Python stesso.

| Attributo/Funzione | Cosa fornisce |
|-------------------|-----------------|
| `sys.path` | Lista delle cartelle dove Python cerca i moduli |
| `sys.version` | Stringa della versione di Python |
| `sys.argv` | Argomenti della riga di comando passati allo script |
| `sys.exit()` | Esce immediatamente dal programma |
| `sys.stdin`, `sys.stdout` | Stream di input/output standard |

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
initCmLab('', `import sys

print("Python version:", sys.version[:6])
print("Platform:", sys.platform)
print("Module search paths (first 2):", sys.path[:2])`);
</script>

## Il Modulo `os` e la Gestione dei Percorsi dei File

Il modulo `os` permette a Python di parlare con il sistema operativo — creando cartelle, elencando file, lavorando con i percorsi dei file.

`os.path` è il sottomodulo per le operazioni sui percorsi dei file.
Prima di provarle, ecco le funzioni chiave:

| Funzione | Scopo |
|----------|-------|
| `os.getcwd()` | Ottiene la cartella di lavoro attuale |
| `os.listdir(path)` | Elenca i file in una cartella |
| `os.path.exists(path)` | Controlla se un file/cartella esiste |
| `os.path.join(a, b)` | Unisce le parti di un percorso in sicurezza (funziona su Windows e Mac) |
| `os.path.basename(path)` | Ottiene solo il nome del file da un percorso |
| `os.path.dirname(path)` | Ottiene solo la parte della cartella |

```python
import os

print(os.getcwd())                          # current directory
print(os.path.exists("notes.txt"))          # True or False
print(os.path.join("folder", "file.txt"))   # "folder/file.txt"
```

## JSON — Il Formato di Dati Universale

**JSON** (JavaScript Object Notation) è un formato di testo per memorizzare dati strutturati.
Assomiglia quasi esattamente ai dizionari e alle liste di Python:

```json
{
  "name": "Alice",
  "age": 14,
  "scores": [95, 87, 91],
  "active": true
}
```

JSON si usa ovunque — API web, file di configurazione, database, e scambio di dati tra programmi.
Il modulo `json` di Python converte tra stringhe JSON e oggetti Python.

| Tipo Python | Tipo JSON |
|-------------|-----------|
| `dict` | oggetto `{}` |
| `list` | array `[]` |
| `str` | stringa `""` |
| `int`, `float` | numero |
| `True`/`False` | `true`/`false` |
| `None` | `null` |

## `json.loads()` e `json.dumps()`

Due funzioni convertono tra testo JSON e oggetti Python:

- `json.loads(text)` — **carica** JSON da una stringa in oggetti Python ("loads" = load string)
- `json.dumps(obj)` — **scarica** oggetti Python in una stringa JSON ("dumps" = dump string)

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto converte una stringa JSON in un dizionario Python, poi di nuovo in JSON.
    Le due stringhe JSON sembreranno identiche? Ci sono differenze di formattazione?
    Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `import json

# JSON string → Python object
json_text = '{"name": "Alice", "score": 95, "active": true}'
data = json.loads(json_text)

print("Type:", type(data))
print("Name:", data["name"])
print("Score:", data["score"])

# Python object → JSON string
data["score"] = 98   # update the score
new_json = json.dumps(data, indent=2)
print("\\nUpdated JSON:")
print(new_json)`);
</script>

`indent=2` rende il JSON leggibile dall'uomo con un'indentazione di 2 spazi.

### Guardalo: Il Mappatore dei Tipi

JSON assomiglia quasi esattamente a Python — che è esattamente il motivo per cui inganna le persone. Nel mappatore sotto, modifica il JSON a sinistra e guarda cosa costruisce `json.loads()` a destra. Prima di toccarlo, prevedi: **cosa diventano in Python `true` e `null` di JSON?**

<iframe src="../../sims/json-python-mapper/main.html" height="442" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim JSON to Python Type Mapper](../../sims/json-python-mapper/index.md){ .md-button }

Clicca il preset **The tricky trio** per vedere tutte e tre le famose differenze in una volta, poi prova entrambi i preset **Broken** — le virgolette singole e le virgole finali sono legali in Python ma fanno andare in crash l'analisi JSON. Passa il mouse su qualsiasi valore colorato a destra per vedere i nomi dei suoi tipi in entrambi i mondi.

## Leggere e Scrivere JSON da File

`json.load(file)` legge JSON direttamente da un file aperto.
`json.dump(data, file)` scrive JSON direttamente su un file aperto.

Questi richiedono un vero ambiente Python (Thonny, VS Code) perché hanno bisogno di un vero accesso al disco.

```python
import json

# Write JSON to a file (run in Thonny or VS Code):
data = {"players": ["Alice", "Bob"], "high_score": 1500}
with open("game.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON from a file:
with open("game.json") as f:
    loaded = json.load(f)

print(loaded["high_score"])   # 1500
```

Nel laboratorio Skulpt sotto usiamo `json.dumps()` → `json.loads()` per mostrare lo stesso andirivieni senza bisogno di un file sul disco.

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
initCmLab('-3', `import json

data = {
    "game": "Python Quest",
    "players": ["Alice", "Bob", "Carol"],
    "high_score": 2400
}

# Convert to a JSON string (like writing to a file):
json_string = json.dumps(data, indent=2)
print("JSON string:")
print(json_string)

# Parse back (like reading from a file):
loaded = json.loads(json_string)
print("Game:", loaded["game"])
print("Players:", loaded["players"])
print("High score:", loaded["high_score"])`);
</script>

## Il Modulo `collections`

`collections` fornisce tipi di contenitori specializzati:

- `Counter` — conta quante volte appare ogni elemento
- `defaultdict` — un dict che crea valori predefiniti automaticamente
- `OrderedDict` — un dict che ricorda l'ordine di inserimento (meno necessario da Python 3.7)
- `deque` — una coda a doppia estremità che è più veloce di una lista per aggiungere/rimuovere da entrambe le estremità

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)             # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(count["apple"])    # 3
print(count.most_common(2))  # [('apple', 3), ('banana', 2)]
```

## Il Modulo `datetime`

`datetime` fornisce oggetti di data e ora:

```python
from datetime import datetime, date

now = datetime.now()
print(now.year, now.month, now.day)
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # formatted string

today = date.today()
print(today)
```

## Il Modulo `itertools`

`itertools` fornisce strumenti efficienti per lavorare con gli iteratori:

- `itertools.chain(a, b)` — unisce due iterabili uno dopo l'altro
- `itertools.combinations(seq, r)` — tutte le combinazioni di lunghezza r
- `itertools.permutations(seq, r)` — tutte le permutazioni di lunghezza r
- `itertools.cycle(seq)` — ripete una sequenza per sempre

```python
from itertools import combinations

players = ["A", "B", "C", "D"]
pairs = list(combinations(players, 2))
print(pairs)   # [('A','B'), ('A','C'), ('A','D'), ('B','C'), ('B','D'), ('C','D')]
```

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Usa Counter"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto conta le parole in una frase, ma usa il pattern manuale `dict.get()` del Capitolo 21.
    Sostituiscilo con `Counter` dal modulo `collections` per contare le stesse parole in meno righe!

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
initCmLab('-4', `text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()

# Replace this manual counting with collections.Counter:
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
print("Most common:", max(word_count, key=word_count.get))`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Usa `json.dumps({"active": True, "count": None}, indent=2)`. Stampa il risultato e nota come `True` e `None` di Python diventano `true` e `null` di JSON.
   **Saprai che ha funzionato quando** vedi `true` e `null` nell'output.

2. Usa `Counter` per trovare il carattere più comune nella stringa `"mississippi"`.
   **Saprai che ha funzionato quando** vedi che `"i"` è il più comune con un conteggio di 4.

3. Usa `json.loads()` per analizzare `'[1, 2, 3, 4, 5]'` (un array JSON) in una lista Python, poi stampa la sua somma.
   **Saprai che ha funzionato quando** vedi `15`.

4. Usa `datetime.now().strftime("%A")` per stampare il giorno della settimana di oggi.
   **Saprai che ha funzionato quando** vedi il nome del giorno della settimana attuale.

5. Usa `itertools.combinations("ABCD", 2)` per elencare tutte le 6 combinazioni di due lettere.
   **Saprai che ha funzionato quando** vedi 6 tuple.

!!! mascot-celebration "Professionista della Libreria Standard!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai esplorato la vasta libreria standard di Python e padroneggiato JSON — il linguaggio del web!
    Questi strumenti appariranno praticamente in ogni progetto Python del mondo reale su cui lavorerai.
    Stai pensando come uno sviluppatore professionista ora. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
