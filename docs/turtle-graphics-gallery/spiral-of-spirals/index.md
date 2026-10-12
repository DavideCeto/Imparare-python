---
hide:
    - toc
---
# Spirale di Spirali

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione riutilizzabile `mini_spiral(x, y, facing)` che disegna una piccola spirale
- Disporre più istanze di spirale in un cerchio usando `math.cos()` e `math.sin()`
- Capire come un micro-pattern ripetuto a scala macro crea complessità simile a un frattale

Dodici piccole spirali quadrate sono disposte in un anello, ognuna ruotata per guardare verso l'esterno dal centro. Da lontano l'intera disposizione sembra un singolo scoppio rotante.

!!! mascot-welcome "Benvenuto alla Spirale di Spirali!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo laboratorio combina due idee: la spirale che già conosci e il trucco della rotazione-attorno-a-un-cerchio
    dalla girandola. Insieme creano qualcosa di molto più ricco di entrambe da sole.
    Programmiamo insieme!

## Come Funziona

Una funzione `mini_spiral()` disegna una piccola spirale quadrata di 30 passi a una data posizione `(x, y)` e direzione iniziale `heading`. Il ciclo esterno posiziona 12 di queste spirali uniformemente attorno a un cerchio di raggio 150, ognuna rivolta verso l'esterno (heading = angolo dal centro).

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def mini_spiral(x, y, facing, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(facing)
    monty.pendown()
    monty.color(color)
    step = 2
    for _ in range(30):
        monty.forward(step)
        monty.right(90)
        step += 1.5

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue',
          'purple', 'violet', 'crimson', 'darkorange', 'forestgreen', 'royalblue']

radius = 150
for i in range(12):
    angle = i * 30
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    mini_spiral(x, y, angle, colors[i])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni piccola spirale inizia rivolta verso l'esterno dal centro.
    Le 12 piccole spirali si sovrapporranno tra loro, o resteranno separate?
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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def mini_spiral(x, y, facing, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(facing)
    monty.pendown()
    monty.color(color)
    step = 2
    for _ in range(30):
        monty.forward(step)
        monty.right(90)
        step += 1.5

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue',
          'purple', 'violet', 'crimson', 'darkorange', 'forestgreen', 'royalblue']

radius = 150
for i in range(12):
    angle = i * 30
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    mini_spiral(x, y, angle, colors[i])`);
</script>

Le spirali per la maggior parte **restano separate** — ognuna inizia lunga 30 segmenti e cresce verso l'interno verso lo spazio centrale. Avevi indovinato?

## Come Funziona

`setheading(angle)` fa sì che ogni spirale sia rivolta verso l'esterno — la direzione è uguale all'angolo attorno al cerchio. Questo perché l'angolo di posizione e l'angolo rivolto verso l'esterno sono lo stesso numero quando misurati dalla direzione Est.

Il ciclo esterno genera le coordinate con `x = r·cos(angle)`, `y = r·sin(angle)` — la conversione standard da polare a cartesiano.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def mini_spiral(x, y, facing, color)` | Funzione riutilizzabile: disegna una piccola spirale |
| `monty.setheading(facing)` | Punta ogni spirale verso l'esterno dal centro |
| `radius = 150` | Distanza dal centro all'inizio di ogni spirale |
| `angle = i * 30` | 12 spirali × 30° = cerchio completo di 360° |
| `x = radius * math.cos(math.radians(angle))` | Da polare a cartesiano x |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia la Dimensione dell'Anello"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cosa succede se cambi `radius = 150` in `radius = 80`?
    Prevedi se le spirali si sovrapporranno — poi eseguilo per controllare!

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def mini_spiral(x, y, facing, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(facing)
    monty.pendown()
    monty.color(color)
    step = 2
    for _ in range(30):
        monty.forward(step)
        monty.right(90)
        step += 1.5

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue',
          'purple', 'violet', 'crimson', 'darkorange', 'forestgreen', 'royalblue']

radius = 80
for i in range(12):
    angle = i * 30
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    mini_spiral(x, y, angle, colors[i])`);
</script>

Con `radius = 80` le spirali si sovrappongono significativamente al centro — l'anello più piccolo le compatta più stretto della dimensione propria delle spirali, creando un nucleo denso e aggrovigliato.

## Esperimenti

1. **Prova 6 spirali.** Cambia `range(12)` in `range(6)` e `i * 30` in `i * 60`. Saprai che ha funzionato quando appaiono solo sei spirali, più distanziate.

2. **Rendi tutte le spirali dello stesso colore.** Rimuovi il parametro `colors` e scrivi a mano `monty.color('navy')`. Saprai che ha funzionato quando tutte le spirali sono dello stesso blu profondo.

3. **Rivolgile verso l'interno.** Cambia `mini_spiral(x, y, angle, ...)` in `mini_spiral(x, y, angle + 180, ...)`. Ora ogni spirale è rivolta verso il centro. Saprai che ha funzionato quando le spirali crescono verso l'interno invece che verso l'esterno.

4. **Usa mini-spirali esagonali.** Cambia `right(90)` dentro `mini_spiral` in `right(60)`. Saprai che ha funzionato quando ogni piccola spirale ha angoli esagonali.

!!! mascot-celebration "Meta-Spirali!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai disposto micro-pattern in un macro-pattern usando la stessa matematica del cerchio
    dalla girandola. Questa idea di "pattern di pattern" è un concetto fondamentale nel design frattale!
    Prossimo: **Spirale Pentagonale a Fasce Colorate** — l'ultima spirale in questa categoria.
