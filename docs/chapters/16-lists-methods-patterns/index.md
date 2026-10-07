---
title: Liste — Metodi e Pattern
description: Padroneggia i metodi delle liste per aggiungere, rimuovere, ordinare, e iterare — più le list comprehension, le pile, e le code
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:40:00
version: 0.09
---

# Liste — Metodi e Pattern

Alla fine di questa lezione sarai in grado di:

- Aggiungere elementi con `append()`, `insert()`, ed `extend()`, e rimuovere elementi con `remove()`, `pop()`, e `clear()`
- Ordinare e invertire una lista con `sort()` e `reverse()`
- Costruire liste dinamicamente dentro un ciclo `for` oppure usando una **list comprehension**
- Usare una lista come una **pila** (ultimo entrato, primo uscito) oppure una **coda** (primo entrato, primo uscito)

Le liste diventano davvero potenti una volta che puoi aggiungere, rimuovere, e riorganizzare i loro elementi.
In questo capitolo vedrai pattern che compaiono ogni giorno nei veri programmi Python.

!!! mascot-welcome "Benvenuto/a al Capitolo 16!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto a far lavorare di più le tue liste? Oggi imparerai ad aggiungere elementi, rimuovere elementi,
    ordinare la tua collezione, e persino costruire automaticamente liste completamente nuove!
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Aggiungere Elementi a una Lista

Ci sono tre metodi per aggiungere elementi.

Prima di provarli, definiamo ciascuno chiaramente:

- `append(x)` — aggiunge `x` alla **fine** della lista
- `insert(i, x)` — aggiunge `x` **prima** dell'elemento all'indice `i`
- `extend(other_list)` — aggiunge ogni elemento di `other_list` alla fine

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
initCmLab('', `fruits = ["apple", "banana"]
print("Start:", fruits)

fruits.append("mango")
print("After append:", fruits)

fruits.insert(1, "kiwi")   # insert "kiwi" at index 1
print("After insert:", fruits)

extras = ["grape", "lemon"]
fruits.extend(extras)
print("After extend:", fruits)`);
</script>

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Dopo `fruits.insert(1, "kiwi")`, come appare la lista?
    Quale elemento viene spinto all'indice 2? Fai la tua previsione — poi eseguilo!

Avevi indovinato? `insert(1, "kiwi")` posiziona `"kiwi"` nella posizione 1, spingendo `"banana"` alla posizione 2.

## Rimuovere Elementi da una Lista

Ci sono tre metodi per rimuovere elementi:

- `remove(x)` — rimuove la **prima** occorrenza del valore `x` (genera `ValueError` se non trovato)
- `pop()` — rimuove e restituisce l'**ultimo** elemento (oppure `pop(i)` rimuove all'indice `i`)
- `clear()` — rimuove **tutti** gli elementi, lasciando una lista vuota

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
initCmLab('-2', `items = ["a", "b", "c", "d", "e"]
print("Start:", items)

items.remove("c")
print("After remove('c'):", items)

last = items.pop()
print("Popped:", last)
print("After pop:", items)

second = items.pop(1)
print("Popped index 1:", second)
print("After pop(1):", items)`);
</script>

## Ordinare e Invertire

`sort()` riorganizza gli elementi di una lista in ordine crescente (alfabetico per le stringhe, dal più piccolo per i numeri).
`reverse()` inverte l'ordine — l'ultimo diventa il primo.

Entrambi i metodi modificano la lista **sul posto** — la lista originale cambia.

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
initCmLab('-3', `scores = [73, 100, 87, 55, 92]
print("Before sort:", scores)

scores.sort()
print("After sort:", scores)

scores.reverse()
print("After reverse:", scores)

words = ["banana", "apple", "cherry"]
words.sort()
print("Sorted words:", words)`);
</script>

## Trovare Elementi con `index()` e `count()`

- `list.index(x)` — restituisce l'indice della prima occorrenza di `x`
- `list.count(x)` — conta quante volte appare `x`

```python
colors = ["red", "blue", "red", "green", "red"]
print(colors.index("blue"))   # 1
print(colors.count("red"))    # 3
```

## Iterare su una Lista

Il modo più comune per lavorare con ogni elemento di una lista è un ciclo `for`:

```python
for item in my_list:
    # do something with item
```

Puoi anche iterare e costruire una nuova lista allo stesso tempo — chiamato il pattern **ciclo-con-costruzione-di-lista**:

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
initCmLab('-4', `scores = [73, 100, 87, 55, 92]
doubled = []

for s in scores:
    doubled.append(s * 2)

print("Original:", scores)
print("Doubled: ", doubled)`);
</script>

## List Comprehension

Una **list comprehension** è un modo più corto per costruire una nuova lista a partire da una esistente.
Racchiude il ciclo e l'espressione in una singola riga dentro parentesi quadre.

Prima della comprehension, assicurati di capire la versione con il ciclo:

```python
# The long way:
doubled = []
for s in scores:
    doubled.append(s * 2)

# The short way (list comprehension):
doubled = [s * 2 for s in scores]
```

Entrambe producono esattamente lo stesso risultato. La comprehension si legge come l'inglese: "s per 2, per ogni s in scores."

Puoi anche aggiungere un filtro `if`:

```python
passing = [s for s in scores if s >= 70]   # only scores 70 and above
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
initCmLab('-5', `scores = [73, 100, 87, 55, 92, 68]

doubled  = [s * 2 for s in scores]
passing  = [s for s in scores if s >= 70]
graded   = ["pass" if s >= 70 else "fail" for s in scores]

print("Doubled:", doubled)
print("Passing:", passing)
print("Graded: ", graded)`);
</script>

## Liste Annidate

Una **lista annidata** è una lista che contiene altre liste come elementi.
Pensala come una griglia — righe e colonne.

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid[0])      # [1, 2, 3] — first row
print(grid[1][2])   # 6 — row 1, column 2
```

## Liste come Pile e Code

Una **pila** (stack) è una collezione "ultimo entrato, primo uscito" — come una pila di piatti. Aggiungi e rimuovi dalla cima.
Usa `append()` per impilare e `pop()` per togliere dalla cima:

```python
stack = []
stack.append("a")   # push
stack.append("b")
stack.append("c")
print(stack.pop())  # "c" — last in, first out
```

Una **coda** (queue) è "primo entrato, primo uscito" — come una fila alla mensa.
Usa `append()` per aggiungere in fondo e `pop(0)` per rimuovere dal fronte:

```python
queue = []
queue.append("first")
queue.append("second")
queue.append("third")
print(queue.pop(0))   # "first" — first in, first out
```

### Guardalo: Stessi Elementi, Uscite Diverse

Il simulatore sotto alimenta le **stesse lettere** in una pila di piatti e in una fila d'attesa. Prima di rimuovere qualsiasi cosa, prevedi: **dopo aver aggiunto A, B, C, D, quale lettera esce prima dalla pila — e quale esce prima dalla coda?**

<iframe src="../../sims/stack-queue-simulator/main.html" height="512" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Stack and Queue Simulator](../../sims/stack-queue-simulator/index.md){ .md-button }

Svuota entrambe le strutture e confronta le due strisce di storico: la pila restituisce D, C, B, A (al contrario!) mentre la coda restituisce A, B, C, D (lo stesso ordine). Una minuscola differenza nel codice — `pop()` contro `pop(0)` — ribalta tutta la storia.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Costruisci una Lista Filtrata"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto cerca di costruire una lista dei soli numeri pari da `numbers`,
    ma la list comprehension ha un bug nella sua condizione `if`.
    Correggilo così che `evens` contenga solo numeri pari!

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
initCmLab('-6', `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bug: this keeps odd numbers, not even ones!
evens = [n for n in numbers if n % 2 == 1]

print("Evens:", evens)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Inizia con una lista vuota. Usa `append()` per aggiungere i numeri da 1 a 5. Stampa la lista.
   **Saprai che ha funzionato quando** vedi `[1, 2, 3, 4, 5]`.

2. Crea una lista di cinque nomi. Ordinala alfabeticamente e stampala.
   **Saprai che ha funzionato quando** i nomi appaiono in ordine A-Z.

3. Scrivi una list comprehension che trasforma `["hello", "world", "python"]` in tutto maiuscolo.
   **Saprai che ha funzionato quando** vedi `["HELLO", "WORLD", "PYTHON"]`.

4. Simula una pila di tre pancake. Impila "bottom", "middle", "top". Toglierne uno. Stampa la pila rimanente.
   **Saprai che ha funzionato quando** "top" viene rimosso e rimangono due pancake.

5. Crea una lista annidata per una griglia 3×3. Stampa il valore centrale (riga 1, colonna 1).
   **Saprai che ha funzionato quando** vedi il numero nella posizione `[1][1]`.

!!! mascot-celebration "Campione delle Liste!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato append, insert, remove, sort, le comprehension, le pile, e le code!
    Le liste sono uno dei cavalli di battaglia di Python — userai questi pattern in quasi ogni programma che costruirai da qui in avanti. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
