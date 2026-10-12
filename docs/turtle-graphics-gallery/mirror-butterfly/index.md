---
hide:
    - toc
---
# Farfalla a Specchio

Alla fine di questo laboratorio sarai in grado di:

- Creare simmetria bilaterale negando le coordinate x di una lista di punti di passaggio
- Disegnare l'ala destra di una farfalla usando punti di passaggio `goto()`, poi rifletterla automaticamente
- Capire come `(x, y) → (-x, y)` produce una perfetta riflessione a specchio

Una farfalla colorata costruita da due liste di coordinate — l'ala destra disegnata da punti di passaggio, l'ala sinistra creata automaticamente negando tutte le coordinate x. Una lista, due ali.

!!! mascot-welcome "Benvenuto alla Farfalla a Specchio!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni farfalla ha simmetria bilaterale (a specchio) — l'ala sinistra è esattamente
    lo specchio della destra. Nel codice, rispecchiare è solo un carattere: un segno meno!
    Programmiamo insieme!

## Come Funziona

L'ala destra è definita come una lista di punti di passaggio `(x, y)`. Per ottenere l'ala sinistra, creiamo una nuova lista dove ogni `x` è negata: `(-x, y)`. Disegniamo entrambe le ali usando `goto()` e `begin_fill()`/`end_fill()`.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

right_wing = [
    (0, 0), (20, 40), (60, 80), (100, 90), (130, 60),
    (120, 20), (90, -10), (60, -20), (30, -30), (10, -40), (0, -50),
    (20, -80), (50, -100), (60, -70), (40, -60), (20, -50), (0, 0)
]

left_wing = [(-x, y) for x, y in right_wing]

def draw_wing(waypoints, color):
    monty.penup()
    monty.goto(waypoints[0])
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for x, y in waypoints[1:]:
        monty.goto(x, y)
    monty.end_fill()

draw_wing(right_wing, 'darkorange')
draw_wing(left_wing, 'darkorange')

monty.penup()
monty.goto(0, -120)
monty.pendown()
monty.pencolor('black')
monty.pensize(3)
monty.setheading(90)
monty.forward(200)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    L'ala sinistra è creata con `(-x, y)`. Sembrerà un perfetto specchio della destra,
    o sembrerà sottosopra?
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

right_wing = [
    (0, 0), (20, 40), (60, 80), (100, 90), (130, 60),
    (120, 20), (90, -10), (60, -20), (30, -30), (10, -40), (0, -50),
    (20, -80), (50, -100), (60, -70), (40, -60), (20, -50), (0, 0)
]

left_wing = [(-x, y) for x, y in right_wing]

def draw_wing(waypoints, color):
    monty.penup()
    monty.goto(waypoints[0])
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for x, y in waypoints[1:]:
        monty.goto(x, y)
    monty.end_fill()

draw_wing(right_wing, 'darkorange')
draw_wing(left_wing, 'darkorange')

monty.penup()
monty.goto(0, -120)
monty.pendown()
monty.pencolor('black')
monty.pensize(3)
monty.setheading(90)
monty.forward(200)`);
</script>

Uno **specchio perfetto** — negare x ribalta la forma da sinistra a destra senza cambiare dall'alto in basso. Avevi indovinato?

## Come Funziona

`[(-x, y) for x, y in right_wing]` è una list comprehension che trasforma ogni coppia di coordinate. Il `-` davanti a `x` ribalta orizzontalmente. La `y` resta invariata così non c'è ribaltamento verticale.

Il corpo nero è disegnato come una linea verticale dalla coda alla testa usando `setheading(90)` (dritto verso l'alto) e `forward(200)`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `right_wing = [(x,y), ...]` | Punti di passaggio che definiscono la forma dell'ala destra |
| `[(-x, y) for x, y in right_wing]` | Specchio: nega tutte le coordinate x |
| `monty.goto(x, y)` | Muove la tartaruga a ogni punto di passaggio, disegnando mentre va |
| `begin_fill()` / `end_fill()` | Riempie la forma dell'ala |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Rifletti Verticalmente Invece"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `(-x, y)` in `(x, -y)` per rifletterlo verticalmente invece che orizzontalmente.
    Prevedi come sembrerà il risultato — poi eseguilo per controllare!

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

right_wing = [
    (0, 0), (20, 40), (60, 80), (100, 90), (130, 60),
    (120, 20), (90, -10), (60, -20), (30, -30), (10, -40), (0, -50),
    (20, -80), (50, -100), (60, -70), (40, -60), (20, -50), (0, 0)
]

bottom_wing = [(x, -y) for x, y in right_wing]

def draw_wing(waypoints, color):
    monty.penup()
    monty.goto(waypoints[0])
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for x, y in waypoints[1:]:
        monty.goto(x, y)
    monty.end_fill()

draw_wing(right_wing, 'darkorange')
draw_wing(bottom_wing, 'royalblue')`);
</script>

`(x, -y)` ribalta dall'alto verso il basso — l'ala inferiore è il riflesso verticale dell'ala destra, in un colore diverso per distinguerle.

## Esperimenti

1. **Aggiungi segni sull'ala.** Dopo aver disegnato le ali riempite, aggiungi una lista `right_inner` più piccola con meno punti e disegnala con `pencolor('black')` senza riempimento. Saprai che ha funzionato quando le ali hanno contorni.

2. **Cambia il corpo.** Sostituisci il corpo a linea retta con una serie di punti di dimensione decrescente. Saprai che ha funzionato quando il corpo sembra segmentato.

3. **Usa 4 ali.** Disegna anche `left_wing` e `bottom_wing` per fare una libellula a quattro ali. Saprai che ha funzionato quando quattro ali si irradiano dal centro.

4. **Aggiungi antenne.** Dopo il corpo, disegna due linee sottili dalla cima del corpo che curvano verso l'esterno. Saprai che ha funzionato quando la farfalla ha antenne.

!!! mascot-celebration "Bellissima Simmetria!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato `(-x, y)` per creare una perfetta simmetria bilaterale — la stessa matematica usata
    nell'animazione computerizzata per rispecchiare i lati sinistro e destro di un personaggio!
    Prossimo: **Piastrelle di Truchet** — tessere casuali che formano pattern globali inaspettati.
