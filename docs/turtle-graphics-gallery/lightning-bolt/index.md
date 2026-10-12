---
hide:
    - toc
---
# Fulmine

Alla fine di questo laboratorio sarai in grado di:

- Usare la ricorsione per dividere una linea retta in uno zigzag frastagliato
- Capire come la ricorsione ramificata crea forme simili all'elettricità in natura
- Controllare la profondità e lo spostamento per variare la frastagliatezza del fulmine

Un fulmine simulato disegnato sostituendo ricorsivamente ogni segmento retto con una versione curvata e a zigzag. Il risultato è una forma irregolare e ramificata che imita strettamente un vero fulmine.

!!! mascot-welcome "Benvenuto al Fulmine!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il vero fulmine segue il percorso di minima resistenza elettrica.
    Il risultato sembra casuale — ma ha un pattern ricorsivo che possiamo programmare!
    Programmiamo insieme!

## Come Funziona

`lightning(x1, y1, x2, y2, depth)` divide il segmento in due metà con il punto medio spostato lateralmente di una quantità casuale. Alla profondità 0, disegna semplicemente il segmento. A ogni profondità, lo spostamento si restringe, creando una frastagliatezza auto-simile.

## Codice di Esempio

```python
import turtle
import math
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
turtle.bgcolor('black')
random.seed(7)

def lightning(x1, y1, x2, y2, depth):
    if depth == 0:
        monty.penup()
        monty.goto(x1, y1)
        monty.pendown()
        monty.goto(x2, y2)
        return
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    perp_x = -dy * 0.3
    perp_y = dx * 0.3
    offset = random.uniform(-1, 1)
    mx += perp_x * offset
    my += perp_y * offset
    monty.pencolor('yellow')
    monty.pensize(max(1, depth))
    lightning(x1, y1, mx, my, depth - 1)
    lightning(mx, my, x2, y2, depth - 1)

lightning(-50, 150, 50, -150, 5)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Iniziamo con una linea verticale e la dividiamo per 5 livelli di profondità.
    Il risultato sembrerà una linea retta, uno zigzag, o un vero fulmine?
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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
turtle.bgcolor('black')
random.seed(7)

def lightning(x1, y1, x2, y2, depth):
    if depth == 0:
        monty.penup()
        monty.goto(x1, y1)
        monty.pendown()
        monty.goto(x2, y2)
        return
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    perp_x = -dy * 0.3
    perp_y = dx * 0.3
    offset = random.uniform(-1, 1)
    mx += perp_x * offset
    my += perp_y * offset
    monty.pencolor('yellow')
    monty.pensize(max(1, depth))
    lightning(x1, y1, mx, my, depth - 1)
    lightning(mx, my, x2, y2, depth - 1)

lightning(-50, 150, 50, -150, 5)`);
</script>

Un **fulmine frastagliato** — lo spostamento ricorsivo crea la forma irregolare e ramificata. Avevi indovinato?

## Come Funziona

Il vettore perpendicolare `(-dy, dx)` è perpendicolare a `(dx, dy)` — una rotazione di 90°. Moltiplicare per `0,3` limita lo spostamento al 30% della lunghezza del segmento. `random.uniform(-1, 1)` sceglie un lato casuale. La ricorsione rende ogni sotto-segmento altrettanto frastagliato.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `if depth == 0` | Caso base: disegna il segmento |
| `mx, my = midpoint` | Trova il punto medio da spostare |
| `perp_x = -dy * 0.3` | Direzione dello spostamento perpendicolare |
| `random.uniform(-1, 1)` | Lato casuale e quantità |
| `pensize(max(1, depth))` | Linee più spesse a profondità minore (fulmine principale) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia la Profondità"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `depth=5` in `depth=3`. Il fulmine avrà meno pieghe.
    Poi prova `depth=7`. Prevedi cosa cambia a ogni profondità!

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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
turtle.bgcolor('black')
random.seed(7)

def lightning(x1, y1, x2, y2, depth):
    if depth == 0:
        monty.penup()
        monty.goto(x1, y1)
        monty.pendown()
        monty.goto(x2, y2)
        return
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    perp_x = -dy * 0.3
    perp_y = dx * 0.3
    offset = random.uniform(-1, 1)
    mx += perp_x * offset
    my += perp_y * offset
    monty.pencolor('yellow')
    monty.pensize(max(1, depth))
    lightning(x1, y1, mx, my, depth - 1)
    lightning(mx, my, x2, y2, depth - 1)

lightning(-50, 150, 50, -150, 7)`);
</script>

La profondità 7 produce un fulmine molto più dettagliato e realistico con piccole frastagliature ovunque.

## Esperimenti

1. **Rimuovi il seme.** Elimina `random.seed(7)`. Ogni esecuzione produce un fulmine diverso. Saprai che ha funzionato quando il fulmine cambia ogni volta.

2. **Disegna più fulmini.** Chiama `lightning()` tre volte con posizioni x di partenza diverse. Saprai che ha funzionato quando appaiono tre fulmini separati.

3. **Cambia il colore del fulmine in bianco.** Cambia `monty.pencolor('yellow')` in `monty.pencolor('white')`. Saprai che ha funzionato quando il fulmine sembra una vera foto di tempesta.

4. **Aumenta lo spostamento.** Cambia `0.3` in `0.6`. Saprai che ha funzionato quando il fulmine ha pieghe più larghe e drammatiche.

!!! mascot-celebration "Elettrizzante!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato lo spostamento ricorsivo per simulare il fulmine — lo stesso algoritmo usato nella
    generazione di terreni nei videogiochi e negli effetti visivi dei film!
    Prossimo: **Bracci a Spirale della Galassia** — spirali di Archimede e logaritmiche con nuvole di punti.
