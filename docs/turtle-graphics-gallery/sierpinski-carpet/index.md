---
hide:
    - toc
---
# Tappeto di Sierpiński

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione ricorsiva a 8 vie (non 2 o 3 — otto!)
- Capire come una suddivisione a 9 con un buco centrale crea il Tappeto di Sierpiński
- Calcolare quanta dell'area originale resta a ogni livello di profondità

Un quadrato diviso in 9 sotto-quadrati uguali, il centro rimosso, poi ciascuno degli 8 sotto-quadrati rimanenti suddiviso di nuovo — per 4 livelli. Il reticolo di buchi diventa più denso a ogni livello.

!!! mascot-welcome "Benvenuto al Tappeto di Sierpiński!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il Triangolo di Sierpiński divideva i triangoli in 3. Ora dividiamo i quadrati in 9
    e rimuoviamo il centro — dando 8 chiamate ricorsive per livello!
    Programmiamo insieme!

## Come Funziona

`carpet(x, y, size, depth)` disegna un quadrato riempito. Se `depth > 0`, divide il quadrato in una griglia 3×3 e ricorre sugli 8 sotto-quadrati non centrali. Il sotto-quadrato centrale è lasciato vuoto (sfondo bianco).

Le 8 posizioni: tutte le 9 posizioni della griglia meno (1, 1) — il centro.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_square(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def carpet(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue', 'lightblue', 'lightcyan']
    draw_square(x, y, size, colors[min(depth, len(colors) - 1)])
    if depth > 0:
        third = size / 3
        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    continue
                carpet(x + col * third, y + row * third, third, depth - 1)

carpet(-160, -160, 320, 4)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Alla profondità 4, la frazione riempita rimanente è `(8/9)^4 ≈ 62%` dell'area originale.
    Il tappeto sembrerà principalmente riempito, o principalmente buchi?
    Fai la tua previsione — poi clicca Esegui per scoprirlo!

## Provalo Ora

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

<div class="cm-lab">
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
initCmLab('', `import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_square(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def carpet(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue', 'lightblue', 'lightcyan']
    draw_square(x, y, size, colors[min(depth, len(colors) - 1)])
    if depth > 0:
        third = size / 3
        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    continue
                carpet(x + col * third, y + row * third, third, depth - 1)

carpet(-160, -160, 320, 4)`);
</script>

**Principalmente riempito** — rimane `(8/9)^4 ≈ 62%` alla profondità 4, quindi più della metà dell'area è ancora colorata. Ma i buchi sono chiaramente visibili a più scale. Avevi indovinato?

## Come Funziona

`for row in range(3): for col in range(3)` genera tutte le 9 posizioni dei sotto-quadrati. `if row == 1 and col == 1: continue` salta il centro. I restanti 8 ottengono chiamate ricorsive.

Alla profondità `n`, la frazione di area rimanente è `(8/9)^n`. Mentre la profondità → ∞, questo si avvicina a 0 — il Tappeto di Sierpiński ha area zero ma lunghezza del confine infinita.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `third = size / 3` | Divide il quadrato in terzi |
| `for row, col in range(3), range(3)` | Genera tutte le 9 posizioni dei sotto-quadrati |
| `if row==1 and col==1: continue` | Salta il centro — il buco distintivo |
| `carpet(x + col*third, y + row*third, ...)` | Ricorre su ciascuno degli 8 sotto-quadrati |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova la Profondità 3"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `depth=4` in `depth=3`. L'area rimanente è `(8/9)^3 ≈ 70%`.
    Conta i buchi centrali visibili a ogni livello — quanti ce ne sono alla profondità 3?
    Prevedi (1 + 8 + 64 = ?) poi controlla!

<div class="cm-lab">
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
initCmLab('-2', `import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_square(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def carpet(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue', 'lightblue', 'lightcyan']
    draw_square(x, y, size, colors[min(depth, len(colors) - 1)])
    if depth > 0:
        third = size / 3
        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    continue
                carpet(x + col * third, y + row * third, third, depth - 1)

carpet(-160, -160, 320, 3)`);
</script>

`1 + 8 + 64 = 73` buchi alla profondità 3 — un grande buco centrale, 8 buchi medi, 64 piccoli buchi.

## Esperimenti

1. **Usa colori caldi.** Sostituisci i blu con `['darkred', 'orangered', 'orange', 'gold', 'lightyellow']`. Saprai che ha funzionato quando il tappeto diventa arancione/rosso.

2. **Salta una cella diversa.** Cambia `if row == 1 and col == 1` in `if row == 0 and col == 0` (salta in basso a sinistra). Saprai che ha funzionato quando i buchi appaiono negli angoli invece che al centro.

3. **Salta due celle.** Aggiungi una condizione extra `or (row == 0 and col == 2)`. Saprai che ha funzionato quando appaiono due tipi di buchi.

4. **Prova la profondità 5.** Molto più lento ma più dettagliato. Saprai che ha funzionato quando vedi piccoli buchi quadrati a più scale.

!!! mascot-celebration "Ricorsione a Otto Vie!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato 8 chiamate ricorsive — più di qualsiasi frattale precedente in questa galleria!
    Mentre la profondità → ∞, il tappeto ha area zero ma è ancora "misurabilmente" 2D.
    Prossimo: **Felce di Barnsley** — un frattale disegnato da trasformazioni casuali.
