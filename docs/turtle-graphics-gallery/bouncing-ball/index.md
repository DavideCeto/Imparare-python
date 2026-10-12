---
hide:
    - toc
---
# Pallina che Rimbalza

Alla fine di questo laboratorio sarai in grado di:

- Animare una tartaruga aggiornando la sua posizione in un ciclo usando variabili di velocità
- Invertire la velocità quando la pallina colpisce un muro (`vx = -vx`)
- Usare `turtle.tracer(0)` e `turtle.update()` per un'animazione fluida

Una pallina colorata rimbalza dentro un confine rettangolare. A ogni fotogramma, la pallina si muove della sua velocità, e quando colpisce un muro, la componente di velocità si inverte — simulando una collisione elastica.

!!! mascot-welcome "Benvenuto alla Pallina che Rimbalza!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo è il tuo primo programma turtle **animato** — la tartaruga si muove continuamente
    dentro un ciclo, e vedi un movimento fluido sullo schermo!
    Programmiamo insieme!

## Come Funziona

Due variabili `vx` e `vy` memorizzano la velocità della pallina. Ogni passo: `x += vx`, `y += vy`. Se `x` raggiunge i limiti del muro, `vx = -vx` (inverte la direzione orizzontale). Se `y` raggiunge i limiti, `vy = -vy`. `turtle.tracer(0)` disattiva il disegno automatico così controlliamo quando aggiornare lo schermo.

## Codice di Esempio

```python
import turtle
screen = turtle.Screen()
screen.tracer(0)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('royalblue')
ball.penup()
ball.speed(0)

x, y = 0, 0
vx, vy = 3, 2
boundary = 150

for _ in range(400):
    x += vx
    y += vy
    if x > boundary or x < -boundary:
        vx = -vx
    if y > boundary or y < -boundary:
        vy = -vy
    ball.goto(x, y)
    screen.update()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La pallina inizia a (0,0) con velocità (3,2).
    Dopo aver rimbalzato su tutti i quattro muri molte volte, tornerà a (0,0)?
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
screen = turtle.Screen()
screen.tracer(0)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('royalblue')
ball.penup()
ball.speed(0)

box = turtle.Turtle()
box.penup()
box.goto(-150, -150)
box.pendown()
box.pencolor('gray')
for _ in range(4):
    box.forward(300)
    box.left(90)
box.hideturtle()

x, y = 0, 0
vx, vy = 3, 2
boundary = 145

for _ in range(400):
    x += vx
    y += vy
    if x > boundary or x < -boundary:
        vx = -vx
    if y > boundary or y < -boundary:
        vy = -vy
    ball.goto(x, y)
    screen.update()`);
</script>

La pallina rimbalza attorno alla scatola — invertendo direzione ogni volta che colpisce un muro. Avevi indovinato sul ritorno all'origine?

## Come Funziona

`screen.tracer(0)` dice a turtle di non disegnare automaticamente dopo ogni comando. `screen.update()` forza un singolo ridisegno dello schermo. Questo dà un'animazione fluida invece di sfarfallio. La posizione `(x, y)` della pallina è aggiornata a ogni passo, e il controllo dei limiti `x > boundary` rileva le collisioni con i muri.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `screen.tracer(0)` | Disabilita l'aggiornamento automatico per un'animazione fluida |
| `vx, vy = 3, 2` | Vettore di velocità iniziale |
| `if x > boundary: vx = -vx` | Inverte la velocità x alla collisione con il muro |
| `screen.update()` | Ridisegna lo schermo (un fotogramma) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Traccia"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi `ball.pendown()` prima del ciclo per lasciare una traccia.
    Il percorso della pallina traccerà un pattern geometrico — prevedi come sembrerà!

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
screen = turtle.Screen()
screen.tracer(0)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('crimson')
ball.penup()
ball.speed(0)

x, y = 0, 0
vx, vy = 5, 3
boundary = 145

ball.goto(x, y)
ball.pendown()
ball.pensize(1)

for _ in range(600):
    x += vx
    y += vy
    if x > boundary or x < -boundary:
        vx = -vx
    if y > boundary or y < -boundary:
        vy = -vy
    ball.goto(x, y)
    screen.update()`);
</script>

La traccia disegna una figura simile a Lissajous! Con vx=5, vy=3 (rapporto 5:3), il percorso alla fine ritorna al suo punto di partenza dopo aver tracciato un pattern geometrico complesso.

## Esperimenti

1. **Fai lasciare una traccia colorata alla pallina.** Cambia il colore ogni volta che un muro viene colpito. Saprai che ha funzionato quando la traccia cambia colore a ogni rimbalzo.

2. **Due palline.** Crea una seconda tartaruga `ball2` con una velocità di partenza diversa. Saprai che ha funzionato quando due palline rimbalzano indipendentemente.

3. **Accelera nel tempo.** Aggiungi `vx *= 1.002; vy *= 1.002` a ogni passo. Saprai che ha funzionato quando la pallina rimbalza gradualmente più velocemente.

4. **Simulazione di gravità.** Aggiungi `vy -= 0.1` a ogni passo e imposta `if y < -boundary: vy = abs(vy) * 0.9`. Saprai che ha funzionato quando la pallina cade e rimbalza come per gravità.

!!! mascot-celebration "Animato!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scritto il tuo primo ciclo di animazione — posizione, velocità, rilevamento di collisione!
    Questi sono i mattoni fondamentali di ogni videogioco basato sulla fisica.
    Prossimo: **Quadrante dell'Orologio** — lancette animate che mostrano l'ora attuale.
