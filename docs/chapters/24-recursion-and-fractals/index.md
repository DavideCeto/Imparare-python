---
title: Ricorsione e Frattali
description: Scopri la ricorsione — funzioni che chiamano sé stesse — con i casi base, gli stack di chiamate, le lambda, e un bellissimo albero frattale ricorsivo
generated_by: claude skill chapter-content-generator
date: 2026-06-28 14:00:00
version: 0.09
---

# Ricorsione e Frattali

Alla fine di questa lezione sarai in grado di:

- Spiegare cos'è la **ricorsione** e perché ogni funzione ricorsiva ha bisogno di un **caso base**
- Seguire passo passo una semplice funzione ricorsiva
- Scrivere una **lambda** (funzione anonima su una riga) e passare funzioni come argomenti
- Costruire un **albero frattale** ricorsivo usando la grafica turtle

La ricorsione è una delle idee più sorprendenti della programmazione — una funzione che chiama sé stessa.
Una volta che la capisci, vedrai i frattali in un modo completamente nuovo.

!!! mascot-welcome "Benvenuto/a al Capitolo 24!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La ricorsione suona spaventosa, ma è davvero solo una funzione che sa come scomporre un problema grande in una versione più piccola dello stesso problema.
    Iniziamo in modo semplice, poi costruiamo qualcosa di bellissimo. Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Concetto di Ricorsione

La **ricorsione** succede quando una funzione chiama sé stessa.
Pensa alle bambole russe matrioska — ogni bambola contiene una versione più piccola di sé stessa, fino a quella minuscola e solida al centro.

La bambola solida al centro è il **caso base** — il punto dove la funzione si ferma e non chiama più sé stessa.
Senza un caso base, la funzione chiamerebbe sé stessa per sempre (o finché Python non finisce lo spazio dello stack e genera un `RecursionError`).

L'esempio ricorsivo più semplice è il conto alla rovescia:

```python
def countdown(n):
    if n <= 0:          # BASE CASE — stop here
        print("Go!")
        return
    print(n)
    countdown(n - 1)    # RECURSIVE CALL — call itself with a smaller problem
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
initCmLab('', `def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(5)`);
</script>

## Il Caso Base

Ogni funzione ricorsiva **deve** avere un caso base.
Il caso base è la condizione che ferma la ricorsione e restituisce un valore senza chiamare di nuovo la funzione.

Se dimentichi il caso base, Python alla fine genera `RecursionError: maximum recursion depth exceeded` dopo circa 1000 chiamate annidate.

Una funzione ricorsiva ben progettata:
1. Controlla prima il caso base
2. Fa la chiamata ricorsiva con una versione *più piccola* o *più semplice* dell'input

## La Profondità della Ricorsione e lo Stack delle Chiamate

Ogni volta che una funzione chiama sé stessa, Python salva lo stato attuale in memoria (lo **stack delle chiamate**, call stack).
Questo significa che la ricorsione usa memoria — e Python limita lo stack a circa 1.000 livelli di profondità per default.

Per la maggior parte dei programmi degli studenti questo è più che sufficiente. Ma per ricorsioni molto profonde (come grandi frattali), potresti aver bisogno di ridurre la profondità.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione ricorsiva `factorial` sotto calcola `n!` (n fattoriale).
    Cosa pensi che restituisca `factorial(5)`? Ricorda: `5! = 5 × 4 × 3 × 2 × 1`.
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
initCmLab('-2', `def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive call

print("5! =", factorial(5))
print("7! =", factorial(7))
print("10! =", factorial(10))`);
</script>

Avevi indovinato? `5! = 120`. Seguendolo passo passo: `5 * factorial(4)` → `5 * 4 * factorial(3)` → ... → `5 * 4 * 3 * 2 * 1`.

### Guardalo: Lo Stack delle Chiamate in Azione

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni chiamata ricorsiva ottiene il suo proprio **frame** su uno stack, ognuno
    ricordando il suo `n`. Per `factorial(4)`, prevedi: **quanto alta diventerà la torre
    di frame prima che inizi a scendere di nuovo?** Esegui passo passo e conta!

<iframe src="../../sims/recursion-call-stack/main.html" height="562" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Recursion Call Stack](../../sims/recursion-call-stack/index.md){ .md-button }

Guarda le due fasi: i frame si accumulano **verso l'alto** con moltiplicazioni in pausa (`4 × ?`) finché non raggiungono il caso base dorato, poi le risposte scorrono di nuovo **verso il basso** mentre ogni frame finisce il suo calcolo. Poi scegli **Missing Base Case** dal menu a tendina per vedere esattamente perché ogni funzione ricorsiva ha bisogno di una regola di arresto.

## Funzioni Lambda

Una **lambda** è una piccola funzione anonima scritta su una riga.
La sintassi è: `lambda parametri: espressione`.

```python
square = lambda x: x * x
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7
```

Le lambda sono più utili quando hai bisogno di una funzione breve come argomento per un'altra funzione, come `sorted(key=...)` o `map()`.

## Funzioni come Argomenti

In Python, le funzioni sono **oggetti di prima classe** — puoi passarle come argomenti ad altre funzioni.

Prima di provarlo, nota cosa significa: quando una funzione prende un'altra funzione come parametro, la funzione esterna può chiamarla su qualsiasi input senza sapere in anticipo cosa fa.

```python
def apply(func, value):
    return func(value)

print(apply(abs, -7))         # 7
print(apply(str.upper, "hi")) # "HI"
print(apply(lambda x: x**2, 5))  # 25
```

## Funzioni Annidate

Puoi definire una funzione dentro un'altra funzione. La funzione interna può accedere alle variabili della funzione esterna.

La **parola chiave `nonlocal`** permette a una funzione interna di modificare una variabile dalla sua funzione (esterna) racchiudente — in modo simile a come `global` permette a una funzione di modificare una variabile globale.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count   # tells Python: use the outer count, not a new local one
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3
```

## Frattali con Ricorsione e Turtle

Un **frattale** è un pattern che si ripete a scale sempre più piccole.
Le funzioni ricorsive sono perfette per disegnare i frattali perché ogni ramo è una versione più piccola dell'intero.

L'**albero frattale** funziona così: disegna un tronco, poi in cima al tronco, disegna due rami ad angoli diversi — e ogni ramo è un albero più piccolo.

Prima del codice, i parametri chiave sono:
- `length` — lunghezza del ramo attuale
- `angle` — quanto si allarga ogni ramo a sinistra e a destra
- Quando `length < 5`, smetti di disegnare (caso base)

<div class="cm-lab">
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
initCmLab('-3', `import turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)   # point upward
t.penup()
t.goto(0, -180)
t.pendown()

def draw_tree(length, angle):
    if length < 5:   # base case: stop for tiny branches
        return
    t.pensize(max(1, length // 10))
    t.forward(length)
    t.left(angle)
    draw_tree(length * 0.7, angle)   # left branch (smaller)
    t.right(angle * 2)
    draw_tree(length * 0.7, angle)   # right branch (smaller)
    t.left(angle)
    t.backward(length)

draw_tree(80, 25)
t.hideturtle()`);
</script>

Prova a cambiare l'angolo da `25` a `35` oppure a `15` per vedere come cambia la forma dell'albero!

!!! mascot-tip "La Magia del Backtracking"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Nota `t.backward(length)` alla fine di `draw_tree`. Questo è la tartaruga che torna a dove era partita *prima* di disegnare il ramo attuale.
    Senza questo, la tartaruga vagherebbe via. Il backtracking è ciò che fa funzionare il disegno ricorsivo — riporta sempre la tartaruga a dove l'hai trovata.

### Guardalo: Scolpisci un Frattale con gli Slider

Modificare il codice della tartaruga e rieseguire funziona, ma gli slider rivelano quanto è *sensibile* un frattale ai suoi parametri. Nell'esploratore sotto, ogni livello di ricorsione ha il suo colore — il tronco marrone è il livello 0, e i rametti più verdi sono le chiamate più profonde. Prima di trascinare qualcosa, prevedi: **cosa succede al contatore "recursive calls" ogni volta che aumenti la profondità di 1?**

<iframe src="../../sims/fractal-tree-explorer/main.html" height="552" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Fractal Tree Explorer](../../sims/fractal-tree-explorer/index.md){ .md-button }

Raddoppia circa ogni volta — questo è il pattern delle due chiamate ricorsive che hai appena scritto in `draw_tree`. Quando trovi un albero che ti piace, clicca **Snapshot**, continua a esplorare, e confronta con il fantasma grigio. Riesci a progettare un salice piangente? Un tumbleweed?

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi Colore all'Albero Frattale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    L'albero frattale si disegna nel colore predefinito. Modifica la funzione `draw_tree` così che:
    - I rami con `length >= 40` siano disegnati in `"brown"` (tronco/rami principali)
    - I rami più corti (length < 40) siano disegnati in `"green"` (foglie)
    Aggiungi una chiamata `t.pencolor()` all'inizio della funzione per impostare il colore in base alla lunghezza.

<div class="cm-lab">
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
initCmLab('-4', `import turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup(); t.goto(0, -180); t.pendown()

def draw_tree(length, angle):
    if length < 5:
        return
    # Add: set color to "brown" if length >= 40, else "green"
    t.pensize(max(1, length // 10))
    t.forward(length)
    t.left(angle)
    draw_tree(length * 0.7, angle)
    t.right(angle * 2)
    draw_tree(length * 0.7, angle)
    t.left(angle)
    t.backward(length)

draw_tree(80, 25)
t.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia il moltiplicatore `0.7` in `draw_tree` in `0.6`. L'albero si ramificherà più velocemente.
   **Saprai che ha funzionato quando** l'albero è più corto e più cespuglioso.

2. Cambia l'angolo da `25` a `40`.
   **Saprai che ha funzionato quando** i rami si allargano molto di più.

3. Scrivi una funzione ricorsiva `sum_list(lst)` che somma tutti gli elementi di una lista senza usare `sum()` di Python.
   **Saprai che ha funzionato quando** `sum_list([1, 2, 3, 4, 5])` restituisce `15`.

4. Scrivi una funzione ricorsiva `reverse_string(s)` che inverte una stringa.
   Caso base: se `len(s) <= 1`, restituisci `s`. Altrimenti restituisci `reverse_string(s[1:]) + s[0]`.
   **Saprai che ha funzionato quando** `reverse_string("hello")` restituisce `"olleh"`.

5. Usa una lambda con `sorted()` per ordinare `["banana", "apple", "fig", "kiwi"]` per la lunghezza della stringa.
   **Saprai che ha funzionato quando** le parole più corte appaiono prima.

!!! mascot-celebration "Maestro della Ricorsione!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai capito una delle idee più potenti e belle di tutta la programmazione!
    Ricorsione, frattali, lambda, e funzioni-come-argomenti — questi concetti appaiono nel codice professionale ogni giorno.
    Il prossimo passo: la programmazione orientata agli oggetti! Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
