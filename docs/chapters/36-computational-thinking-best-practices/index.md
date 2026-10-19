---
title: Pensiero Computazionale e Buone Pratiche
description: Padroneggia le abitudini dei programmatori esperti — scomposizione, astrazione, DRY, nomi significativi, refactoring, pensiero test-driven, e pair programming
generated_by: claude skill chapter-content-generator
date: 2026-06-28 16:00:00
version: 0.09
---

# Pensiero Computazionale e Buone Pratiche

Alla fine di questa lezione sarai in grado di:

- Applicare i quattro pilastri del **pensiero computazionale**: scomposizione, riconoscimento dei pattern, astrazione, design degli algoritmi
- Seguire i principi **DRY** (Don't Repeat Yourself) e di **modularità**
- Scrivere **nomi significativi** e commenti utili
- Descrivere il **pensiero test-driven** e come fare debug in modo sistematico
- Capire il **controllo di versione** e il **pair programming**

Scrivere codice che funziona è solo metà del lavoro. I programmatori esperti scrivono codice che funziona *e* che è facile da leggere, cambiare, e condividere con altri. Questo capitolo raccoglie le abitudini che separano i buoni programmatori da quelli eccellenti.

!!! mascot-welcome "Benvenuto/a al Capitolo 36!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Hai imparato gli strumenti di Python — ora è il momento di imparare come *pensare* da programmatore.
    Le abitudini di questo capitolo renderanno ogni progetto futuro più fluido e più piacevole.
    Saliamo di livello! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Pensiero Computazionale — Quattro Pilastri

Il **pensiero computazionale** è un framework per risolvere problemi che ti permette di affrontare qualsiasi problema complesso con un computer.
Ha quattro competenze chiave:

| Pilastro | Significato | Esempio |
|--------|---------|---------|
| **Scomposizione** | Scomponi un grande problema in problemi più piccoli | "Costruisci un'app di quiz" → "Memorizza le domande", "Chiedi all'utente", "Controlla la risposta", "Traccia il punteggio" |
| **Riconoscimento dei Pattern** | Individua somiglianze e ripetizioni | Ogni domanda del quiz ha: testo, scelte, risposta corretta |
| **Astrazione** | Concentrati sui dettagli essenziali; nascondi quelli non necessari | Una funzione `ask_question(q)` nasconde i dettagli di input/output |
| **Design degli Algoritmi** | Scrivi una soluzione chiara, passo dopo passo | "Finché restano domande: chiedine una, registra la risposta, controlla il risultato" |

Queste quattro competenze non sono specifiche di Python — si applicano a qualsiasi linguaggio di programmazione, qualsiasi campo, qualsiasi problema.

## La Scomposizione in Pratica

Un errore comune dei principianti è provare a scrivere un intero programma in una volta.
La **scomposizione** significa prima scomporre il problema, poi programmare un pezzo alla volta.

```
Problem: Build a word guessing game
│
├── Read a secret word
├── Show blanks (one _ per letter)
├── Accept one guess per turn
│   ├── Validate: is it a single letter?
│   └── Check: is the letter in the word?
├── Reveal matched letters
├── Track wrong guesses (max 6)
└── Announce win or loss
```

Ogni foglia di questo albero è abbastanza piccola da essere programmata in una singola funzione.

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
initCmLab('', `def make_display(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)

def is_solved(secret, guessed):
    return all(ch in guessed for ch in secret)

# Simula un turno (senza input reale):
secret  = "python"
guessed = set("p_t")
wrong   = ["x", "z"]

print("Parola:", make_display(secret, guessed))
print("Tentativi sbagliati:", wrong)
print("Risolto?", is_solved(secret, guessed))

guessed = set("python")
print("Dopo tutte le lettere:", make_display(secret, guessed))
print("Risolto?", is_solved(secret, guessed))`);
</script>

## DRY — Don't Repeat Yourself

Il **principio DRY** dice: ogni pezzo di conoscenza dovrebbe avere esattamente una rappresentazione nel tuo codice.

Se la stessa logica appare in due punti, una correzione di bug o un cambiamento deve essere fatto due volte — ed è facile aggiornare uno e dimenticare l'altro.

**Codice wet (ripeti te stesso):**
```python
score1 = max(0, min(100, score1))
score2 = max(0, min(100, score2))
score3 = max(0, min(100, score3))
```

**Codice dry (una funzione fa il lavoro):**
```python
def clamp(value):
    return max(0, min(100, value))

score1 = clamp(score1)
score2 = clamp(score2)
score3 = clamp(score3)
```

Ancora meglio — applicalo a una lista:
```python
scores = [clamp(s) for s in scores]
```

## Modularità

La **modularità** significa organizzare il codice in unità indipendenti e riutilizzabili (funzioni, classi, moduli).
Un programma ben strutturato ha molte piccole funzioni, ognuna che fa una cosa chiaramente.

**Segnali che la tua funzione NON è modulare:**
- È più lunga di 20-30 righe
- Il suo nome contiene "and" (ad es. `validate_and_save`)
- Fa I/O e calcoli insieme

**Fai il refactor in pezzi più piccoli:**

```python
# Prima: una funzione lunga
def process(data):
    cleaned = [x.strip().lower() for x in data if x.strip()]
    unique  = list(set(cleaned))
    sorted_ = sorted(unique)
    return sorted_

# Dopo: tre passaggi con un nome
def clean(data):
    return [x.strip().lower() for x in data if x.strip()]

def deduplicate(data):
    return list(set(data))

def process(data):
    return sorted(deduplicate(clean(data)))
```

## Nomi Significativi

I nomi delle variabili e delle funzioni sono il tuo strumento di documentazione più potente.
Un lettore che non può eseguire il codice dovrebbe comunque capirlo solo dai nomi.

| Cattivo | Migliore | Perché |
|-----|--------|-----|
| `x` | `elapsed_seconds` | Descrive il significato |
| `lst` | `student_names` | Descrive il contenuto |
| `do_thing()` | `calculate_average()` | Descrive cosa restituisce |
| `check(x)` | `is_valid_email(text)` | Descrive cosa controlla |
| `n` | `num_retries` | Nessuna traduzione mentale necessaria |

**Regola per i booleani:** nominali come una domanda sì/no — `is_logged_in`, `has_errors`, `can_retry`.

## Quando Commentare

I commenti spiegano il **perché**, non il **cosa**. Il codice ben nominato ti dice già cosa — i commenti ti dicono perché quella fosse la scelta giusta.

```python
# SBAGLIATO: ripete quello che dice già il codice
i = i + 1   # incrementa i di 1

# GIUSTO: spiega il motivo che non è evidente
# Parti da 1 perché la prima riga è sempre un'intestazione
for row in rows[1:]:
    process(row)
```

Non scrivere nessun commento se il codice si spiega da solo.
Scrivi un commento quando un futuro lettore (incluso il futuro te stesso) si chiederebbe "perché l'hanno fatto in quel modo?"

!!! mascot-tip "La Regola del Tre"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Se scrivi la stessa logica una volta — lasciala così. Due volte — aggiungi un commento che nota il pattern. Tre volte — estraila in una funzione.
    Questo si chiama la "regola del tre" e ti impedisce di astrarre troppo presto prima di essere sicuro che il pattern sia reale.

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
initCmLab('-2', `def clamp(value, lo=0, hi=100):
    return max(lo, min(hi, value))

def letter_grade(score):
    clamped = clamp(score)
    if clamped >= 90: return "A"
    if clamped >= 80: return "B"
    if clamped >= 70: return "C"
    if clamped >= 60: return "D"
    return "F"

# Prova con valori che devono essere limitati:
test_scores = [110, 95, 82, 73, 65, -5, 45]
for s in test_scores:
    print(f"  {s:4d} → limitato={clamp(s):3d}, voto={letter_grade(s)}")`);
</script>

## Pseudocodice e Design degli Algoritmi

Lo **pseudocodice** è una descrizione passo dopo passo di un algoritmo scritta in inglese semplice, non in un vero linguaggio di programmazione.
Ti permette di pianificare prima di programmare — e cattura i problemi prima che tu abbia passato tempo a scrivere la sintassi.

```
ALGORITHM: Find the most frequent word

1. Split the text into a list of words
2. Convert each word to lowercase
3. Create an empty frequency dictionary
4. For each word in the list:
   a. If the word is already in the dictionary, add 1
   b. Otherwise, set its count to 1
5. Find the key with the highest value
6. Return that key and its count
```

Solo dopo traduci in Python. L'algoritmo è chiaro — la programmazione è solo trascrizione.

## Pensiero Test-Driven

Gli sviluppatori professionisti scrivono i **test** prima (o insieme) al codice.
Anche se non scrivi funzioni di test formali, pensa in termini di test:

1. **Cosa dovrebbe restituire la funzione per un input normale?**
2. **Cosa dovrebbe fare con un input vuoto?**
3. **Cosa dovrebbe fare con un input non valido?**
4. **Qual è il caso limite?** (Lista vuota, zero, numero negativo, stringa molto lunga)

```python
def word_frequency(text):
    words = text.lower().split()
    freq  = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

# Casi di prova mentali:
print(word_frequency(""))               # {} — input vuoto
print(word_frequency("cat cat dog"))    # {'cat': 2, 'dog': 1}
print(word_frequency("A a A"))          # {'a': 3} — non distingue maiuscole e minuscole
```

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
initCmLab('-3', `def word_frequency(text):
    words = text.lower().split()
    freq  = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def most_common(freq):
    if not freq:
        return None, 0
    word = max(freq, key=freq.get)
    return word, freq[word]

text = "the quick brown fox jumps over the lazy dog the fox"
freq = word_frequency(text)
print("Frequenze:", freq)
word, count = most_common(freq)
print(f"La più frequente: '{word}' ({count} volte)")`);
</script>

## Strategie di Debug

Quando il codice non funziona, resisti all'impulso di cambiare le cose a caso finché non funziona "magicamente".
Usa un approccio sistematico:

1. **Leggi il traceback** — l'ultima riga è l'errore; risali per trovare da dove viene
2. **Stampa lo stato** — aggiungi istruzioni `print()` subito prima dell'errore per vedere cosa contengono davvero le variabili
3. **Semplifica** — sostituisci le espressioni complesse con quelle più semplici finché il bug non scompare
4. **Debug della papera di gomma** (rubber duck debugging) — spiega il tuo codice ad alta voce, riga per riga, a un ascoltatore immaginario; il bug spesso si rivela da solo
5. **Cerca il messaggio di errore** — copia il testo dell'errore in un motore di ricerca; qualcuno lo ha già visto prima

## Refactoring

Il **refactoring** significa migliorare la struttura del codice senza cambiare cosa fa.
È normale scrivere prima codice disordinato, poi fare il refactor una volta che il programma funziona.

Mosse di refactoring comuni:
- Estrarre un blocco ripetuto in una funzione nominata
- Rinominare una variabile per renderla più descrittiva
- Sostituire una lunga catena di `if/elif` con una ricerca in un dizionario
- Dividere una lunga funzione in due più piccole

## Controllo di Versione con Git

**Git** è lo strumento standard per tracciare i cambiamenti al codice nel tempo.
Anche lavorando da solo, git ti permette di:
- Tornare a qualsiasi versione precedente del tuo progetto
- Vedere esattamente cosa è cambiato tra le versioni
- Lavorare su esperimenti rischiosi senza paura di rompere il codice funzionante

Il flusso di lavoro di base:

```bash
git init              # start tracking a project
git add myfile.py     # stage a changed file
git commit -m "Add score tracker"  # save a snapshot
git log               # see history of commits
```

## Pair Programming

Il **pair programming** significa che due persone lavorano su un computer — una persona scrive (il "driver"), una persona rivede e suggerisce (il "navigator").

La ricerca mostra che il pair programming:
- Cattura i bug prima che vengano committati
- Diffonde la conoscenza tra i compagni di squadra
- Produce codice più pulito al primo tentativo

Anche praticare il pair programming con un compagno di classe per 20 minuti costruisce abitudini migliori.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Fai il Refactor di Questo Codice"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto funziona ma viola il DRY — la logica di calcolo del voto è ripetuta tre volte.
    Fai il refactor in una singola funzione `letter_grade(score)` e usala in tutti e tre i punti!

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
initCmLab('-4', `# Codice WET — la logica dei voti è ripetuta tre volte:
score1 = 87
if score1 >= 90: grade1 = "A"
elif score1 >= 80: grade1 = "B"
elif score1 >= 70: grade1 = "C"
else: grade1 = "F"

score2 = 73
if score2 >= 90: grade2 = "A"
elif score2 >= 80: grade2 = "B"
elif score2 >= 70: grade2 = "C"
else: grade2 = "F"

score3 = 95
if score3 >= 90: grade3 = "A"
elif score3 >= 80: grade3 = "B"
elif score3 >= 70: grade3 = "C"
else: grade3 = "F"

print(f"Punteggio 1: {score1} → {grade1}")
print(f"Punteggio 2: {score2} → {grade2}")
print(f"Punteggio 3: {score3} → {grade3}")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Applica i quattro pilastri del pensiero computazionale a "Scrivi un programma che ordina una lista di nomi alfabeticamente." Scrivi la scomposizione come commenti prima di programmare.
   **Saprai che ha funzionato quando** hai sotto-passaggi chiari prima di qualsiasi codice Python.

2. Fai il refactor delle funzioni `word_frequency` + `most_common` in una singola funzione `analyze_text(text)` che restituisce un dict con sia la chiave `"frequencies"` sia `"top_word"`.
   **Saprai che ha funzionato quando** `analyze_text("cat cat dog")["top_word"]` restituisce `"cat"`.

3. Scrivi una funzione `safe_divide(a, b)` che restituisce `a / b` normalmente, ma restituisce `None` (non un errore) quando `b == 0`. Scrivi almeno 3 casi di test.
   **Saprai che ha funzionato quando** tutti e tre i casi di test stampano il risultato previsto.

4. Prendi qualsiasi funzione che hai scritto in un capitolo precedente e rinomina tutte le variabili per renderle più descrittive. Sembra più leggibile?
   **Saprai che ha funzionato quando** la funzione si legge quasi come l'inglese senza commenti.

5. Trova un compagno e prova il pair programming: una persona scrive la soluzione dell'esperimento 3 mentre l'altra lo legge ad alta voce e suggerisce miglioramenti.
   **Saprai che ha funzionato quando** scopri almeno un miglioramento attraverso la discussione.

!!! mascot-celebration "Mentalità da Programmatore Esperto Sbloccata!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora pensi come un programmatore professionista — con scomposizione, astrazione, codice DRY, nomi significativi, e debug sistematico nella tua cassetta degli attrezzi.
    Restano due capitoli: machine learning e reti neurali. La frontiera dell'informatica è proprio davanti! Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
