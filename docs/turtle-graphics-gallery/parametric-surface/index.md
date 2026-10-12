---
hide:
    - toc
---
# Proiezione di Superficie Parametrica

Alla fine di questo laboratorio sarai in grado di:

- Definire una superficie 3D con equazioni parametriche `x(u,v)`, `y(u,v)`, `z(u,v)`
- Proiettare coordinate 3D su 2D usando una proiezione isometrica o in prospettiva
- Disegnare una mesh wireframe collegando punti adiacenti della superficie

Una superficie parametrica 3D — una sella, un toro, o un'onda — proiettata sul canvas 2D usando la proiezione isometrica. La mesh wireframe mostra la forma e la curvatura della superficie senza ombreggiatura.

!!! mascot-welcome "Benvenuto alla Proiezione 3D!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La grafica 3D inizia qui: calcola x, y, z per ogni punto su una superficie,
    poi proietta su 2D combinando le tre coordinate.
    Questa è la base di tutto il rendering 3D!
    Programmiamo insieme!

## Come Funziona

Per una superficie a sella: `x = u`, `y = v`, `z = u^2 - v^2`. Proietta sullo schermo: `sx = (x - y) * cos30`, `sy = (x + y) * sin30 + z`. Disegna le linee della griglia collegando punti adiacenti sia nella direzione u sia in quella v.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

n = 14
scale = 18
pts = []

for i in range(n):
    row = []
    for j in range(n):
        u = (i - n/2) / (n/4)
        v = (j - n/2) / (n/4)
        x = u * scale
        y = v * scale
        z = (u*u - v*v) * scale / 2
        cos30 = math.cos(math.radians(30))
        sin30 = math.sin(math.radians(30))
        sx = (x - y) * cos30
        sy = (x + y) * sin30 + z
        row.append((sx, sy))
    pts.append(row)

monty.pensize(1)

for i in range(n):
    monty.penup()
    monty.pencolor('royalblue')
    for j in range(n):
        if j == 0:
            monty.goto(pts[i][j]); monty.pendown()
        else:
            monty.goto(pts[i][j])

for j in range(n):
    monty.penup()
    monty.pencolor('steelblue')
    for i in range(n):
        if i == 0:
            monty.goto(pts[i][j]); monty.pendown()
        else:
            monty.goto(pts[i][j])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Una superficie a sella ha l'equazione `z = u² - v²` — si curva verso l'alto in una direzione e verso il basso nell'altra.
    La proiezione mostrerà una forma di sella chiara, o sembrerà piatta?
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

n = 14
scale = 18
pts = []

for i in range(n):
    row = []
    for j in range(n):
        u = (i - n/2) / (n/4)
        v = (j - n/2) / (n/4)
        x = u * scale
        y = v * scale
        z = (u*u - v*v) * scale / 2
        cos30 = math.cos(math.radians(30))
        sin30 = math.sin(math.radians(30))
        sx = (x - y) * cos30
        sy = (x + y) * sin30 + z
        row.append((sx, sy))
    pts.append(row)

monty.pensize(1)

for i in range(n):
    monty.penup()
    monty.pencolor('royalblue')
    for j in range(n):
        if j == 0:
            monty.goto(pts[i][j])
            monty.pendown()
        else:
            monty.goto(pts[i][j])

for j in range(n):
    monty.penup()
    monty.pencolor('steelblue')
    for i in range(n):
        if i == 0:
            monty.goto(pts[i][j])
            monty.pendown()
        else:
            monty.goto(pts[i][j])`);
</script>

Una chiara **forma a sella 3D** — la superficie si curva verso l'alto in una direzione diagonale e verso il basso nell'altra. Avevi indovinato?

## Come Funziona

La proiezione isometrica combina x, y, z in due coordinate dello schermo: `sx = (x - y) * cos(30°)` e `sy = (x + y) * sin(30°) + z`. Gli angoli di 30° creano la vista isometrica a "gabinetto". Disegnare linee della griglia sia nella direzione u sia in quella v produce la mesh wireframe.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `u = (i - n/2) / (n/4)` | Mappa l'indice della griglia a un parametro a valore reale |
| `z = (u*u - v*v) * scale / 2` | Equazione della superficie a sella |
| `sx = (x - y) * cos30` | Proiezione isometrica x |
| `sy = (x + y) * sin30 + z` | Proiezione isometrica y con altezza z |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia in una Superficie Ondulata"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `z = (u*u - v*v) * scale / 2` in `z = scale * math.sin(u) * math.cos(v)`.
    Questa è una superficie ondulata — prevedi come apparirà!

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

n = 14
scale = 18
pts = []

for i in range(n):
    row = []
    for j in range(n):
        u = (i - n/2) / (n/4) * math.pi
        v = (j - n/2) / (n/4) * math.pi
        x = u * scale / math.pi
        y = v * scale / math.pi
        z = scale * math.sin(u) * math.cos(v)
        cos30 = math.cos(math.radians(30))
        sin30 = math.sin(math.radians(30))
        sx = (x - y) * cos30
        sy = (x + y) * sin30 + z
        row.append((sx, sy))
    pts.append(row)

monty.pensize(1)

for i in range(n):
    monty.penup()
    monty.pencolor('crimson')
    for j in range(n):
        if j == 0:
            monty.goto(pts[i][j]); monty.pendown()
        else:
            monty.goto(pts[i][j])

for j in range(n):
    monty.penup()
    monty.pencolor('darkorange')
    for i in range(n):
        if i == 0:
            monty.goto(pts[i][j]); monty.pendown()
        else:
            monty.goto(pts[i][j])`);
</script>

Una superficie ondulata — picchi e valli ondulate come un'onda oceanica congelata!

## Esperimenti

1. **Prova una sfera.** Usa `x = scale*sin(u)*cos(v)`, `y = scale*sin(u)*sin(v)`, `z = scale*cos(u)` con u da 0 a π e v da 0 a 2π. Saprai che ha funzionato quando appare un wireframe sferico.

2. **Cambia l'angolo di proiezione.** Sostituisci 30° con 45°. Saprai che ha funzionato quando la superficie si vede da un punto di vista diverso.

3. **Aumenta la densità.** Cambia `n = 20`. Saprai che ha funzionato quando il wireframe è più denso con più linee della griglia.

4. **Prova un toro.** `x = (R + r*cos(v))*cos(u)`, `y = (R + r*cos(v))*sin(u)`, `z = r*sin(v)`. Saprai che ha funzionato quando appare una forma a ciambella.

!!! mascot-celebration "3D dal 2D!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai proiettato una superficie parametrica 3D su 2D usando la matematica isometrica!
    Questa è la base di ogni motore di gioco 3D e software CAD.
    Prossimo: **Collezione di Fiocchi di Neve di Lindenmayer** — più fiocchi di neve a sistema-L.
