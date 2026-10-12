---
hide:
    - toc
---
# Ciclo di Arte Generativa

Alla fine di questo laboratorio sarai in grado di:

- Combinare più tecniche della tartaruga — spirali, ciclo di colori, coordinate polari — in un unico programma fluido
- Usare un ciclo di parametri per generare automaticamente una famiglia di immagini correlate
- Capire l'arte generativa: codice che produce output visivo unico governato da regole

Il gran finale della galleria — un ciclo di arte generativa che combina spirali, ciclo di colori, posizionamento ad angolo d'oro, e curve parametriche per produrre una composizione unica e complessa ogni volta che il seme cambia.

!!! mascot-welcome "Benvenuto al Ciclo di Arte Generativa!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sei arrivato all'ultimo laboratorio della galleria!
    Questo programma combina ogni tecnica della galleria in un'unica composizione.
    Ogni seme produce un'opera d'arte diversa — programmiamo la macchina dell'arte!

## Come Funziona

Il programma esegue tre strati:

1. **Punti a spirale dorata** — 300 punti colorati posizionati secondo l'angolo d'oro
2. **Rosa parametrica** — una curva a rosa sovrapposta in bianco semi-trasparente
3. **Spirali annidate** — 6 mini-spirali in posizioni calcolate dalla curva a rosa

Insieme formano una composizione complessa e stratificata.

## Codice di Esempio

```python
import turtle
import math
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

seed = 7
random.seed(seed)
golden = 137.508

palette = ['royalblue', 'crimson', 'forestgreen', 'darkorange', 'purple', 'teal']

for n in range(300):
    angle = math.radians(n * golden)
    r = 7 * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    sz = max(2, int(8 - r / 25))
    monty.dot(sz, palette[n % len(palette)])

k = 5
scale = 120
steps = 800
monty.pencolor('navy')
monty.pensize(1)
monty.penup()
for i in range(steps + 1):
    theta = 2 * math.pi * i / steps
    r2 = scale * math.cos(k * theta)
    x = r2 * math.cos(theta)
    y = r2 * math.sin(theta)
    if i == 0:
        monty.goto(x, y); monty.pendown()
    else:
        monty.goto(x, y)

for arm in range(6):
    arm_angle = math.radians(arm * 60)
    cx = 70 * math.cos(arm_angle)
    cy = 70 * math.sin(arm_angle)
    monty.pencolor(palette[arm])
    monty.pensize(1)
    for i in range(30):
        step_r = i * 1.5
        a = math.radians(arm * 60 + i * 30)
        sx = cx + step_r * math.cos(a)
        sy = cy + step_r * math.sin(a)
        monty.penup()
        monty.goto(sx, sy)
        monty.pendown()
        monty.dot(2, palette[arm])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Tre strati — punti dorati, una curva a rosa, e 6 mini-spirali — tutti centrati insieme.
    Gli strati sembreranno separati e disordinati, o si combineranno in un'immagine unificata?
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

seed = 7
random.seed(seed)
golden = 137.508

palette = ['royalblue', 'crimson', 'forestgreen', 'darkorange', 'purple', 'teal']

for n in range(300):
    angle = math.radians(n * golden)
    r = 7 * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    sz = max(2, int(8 - r / 25))
    monty.dot(sz, palette[n % len(palette)])

k = 5
scale = 120
steps = 800
monty.pencolor('navy')
monty.pensize(1)
monty.penup()
for i in range(steps + 1):
    theta = 2 * math.pi * i / steps
    r2 = scale * math.cos(k * theta)
    x = r2 * math.cos(theta)
    y = r2 * math.sin(theta)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)

for arm in range(6):
    arm_angle = math.radians(arm * 60)
    cx = 70 * math.cos(arm_angle)
    cy = 70 * math.sin(arm_angle)
    monty.pencolor(palette[arm])
    monty.pensize(1)
    for i in range(30):
        step_r = i * 1.5
        a = math.radians(arm * 60 + i * 30)
        sx = cx + step_r * math.cos(a)
        sy = cy + step_r * math.sin(a)
        monty.penup()
        monty.goto(sx, sy)
        monty.pendown()
        monty.dot(2, palette[arm])`);
</script>

Una **composizione complessa e stratificata** — i tre strati si intrecciano per formare un'opera d'arte unificata. Avevi indovinato?

## Come Funziona

I punti dorati riempiono lo sfondo con texture di colore. La curva a rosa fornisce geometria strutturale. Le mini-spirali aggiungono punti focali nelle posizioni dei petali della rosa. Quando tutti e tre gli strati condividono lo stesso centro e sistema di coordinate, si compongono naturalmente insieme.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `golden = 137.508` | Angolo d'oro — punti spaziati in modo ottimale |
| `math.cos(k * theta)` | Curva a rosa — 5 petali con k=5 |
| `arm * 60` | Sei bracci spaziati di 60° |
| `palette[n % len(palette)]` | Assegnazione di colore ciclica |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Seme"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `seed = 7` in `seed = 99`.
    Prevedi: quale parte della composizione cambierà? (Non tutti e tre gli strati usano `random`!)
    Eseguilo per scoprire quali strati sono deterministici e quali sono casuali.

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

seed = 99
random.seed(seed)
golden = 137.508

palette = ['navy', 'royalblue', 'deepskyblue', 'steelblue', 'lightblue', 'cyan']

for n in range(300):
    angle = math.radians(n * golden)
    r = 7 * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    sz = max(2, int(8 - r / 25))
    monty.dot(sz, palette[n % len(palette)])

k = 7
scale = 110
steps = 800
monty.pencolor('darkblue')
monty.pensize(1)
monty.penup()
for i in range(steps + 1):
    theta = 2 * math.pi * i / steps
    r2 = scale * math.cos(k * theta)
    x = r2 * math.cos(theta)
    y = r2 * math.sin(theta)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)

for arm in range(7):
    arm_angle = math.radians(arm * 360/7)
    cx = 65 * math.cos(arm_angle)
    cy = 65 * math.sin(arm_angle)
    monty.pencolor(palette[arm % len(palette)])
    for i in range(25):
        step_r = i * 1.5
        a = math.radians(arm * 360/7 + i * 30)
        sx = cx + step_r * math.cos(a)
        sy = cy + step_r * math.sin(a)
        monty.penup(); monty.goto(sx, sy); monty.pendown()
        monty.dot(2, palette[arm % len(palette)])`);
</script>

Tavolozza blu, rosa a 7 petali, 7 bracci a spirale — una composizione completamente diversa ma ugualmente strutturata.

## Esperimenti

1. **Usa uno sfondo scuro.** Aggiungi `turtle.bgcolor('black')` e cambia la tavolozza in colori brillanti. Saprai che ha funzionato quando i punti brillano contro lo sfondo scuro.

2. **Prova k=8 per la rosa.** Cambia `k = 5` in `k = 8`. Ricorda: un k pari dà 2k petali = 16 petali! Saprai che ha funzionato quando appare una rosa più complessa.

3. **Aggiungi un quarto strato.** Aggiungi una figura di Lissajous disegnata sopra in bianco. Saprai che ha funzionato quando un terzo tipo di curva si aggiunge alla composizione.

4. **Cicla attraverso i semi 1–6.** Pulisci lo schermo tra i semi e disegna sei varianti automaticamente. Saprai che ha funzionato quando 6 composizioni diverse sono generate in sequenza.

!!! mascot-celebration "Hai Completato la Galleria!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Sei arrivato in fondo a tutti i 100 pattern di grafica turtle — da una semplice spirale quadrata
    a un'opera d'arte generativa stratificata! Hai imparato cicli, funzioni, ricorsione, frattali,
    matematica parametrica, sistemi-L, e molto altro. Continua a programmare — il canvas è infinito!
