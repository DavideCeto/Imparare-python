---
hide:
    - toc
---
# Regioni Colorate di Voronoi

Alla fine di questo laboratorio sarai in grado di:

- Usare la formula della distanza `dx*dx + dy*dy` per trovare il più vicino tra diversi punti
- Classificare ogni cella di una griglia in base al suo seme più vicino (classificazione del vicino più prossimo)
- Colorare un'immagine raster con una griglia di chiamate a `dot()`

Sparpaglia una dozzina di punti "seme" sul canvas, poi colora ogni punto dello schermo per farlo corrispondere a qualunque seme sia più vicino. Il risultato è un diagramma di Voronoi — una mappa a vetrata colorata di territori che appare ovunque in natura e nella scienza: macchie di giraffa, ali di libellula, pareti cellulari, persino mappe di quale stazione dei pompieri serve la tua casa. Il nostro programma controlla una griglia 50×50 di celle, un punto colorato alla volta.

!!! mascot-welcome "Benvenuto alla Mappatura dei Territori!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Dodici punti seme stanno per spartire l'intero canvas in dodici
    regni. L'unica legge in questa terra: appartieni a qualunque seme
    tu sia più vicino. Formula della distanza, a te!

## Come Funziona

Per ogni centro di cella `(x, y)` in una griglia 50×50, il programma misura la distanza al quadrato `dx*dx + dy*dy` verso tutti i 12 semi e ricorda quale seme era più vicino. (La distanza al quadrato è sufficiente — se `a*a < b*b` per lunghezze positive, allora `a < b` — quindi saltiamo la radice quadrata e risparmiamo tempo.) La cella viene poi marcata con un `dot()` nel colore del seme vincitore. Sono 2.500 punti e 30.000 controlli di distanza, ed è esattamente come funziona la classificazione del vicino più prossimo nel vero apprendimento automatico.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

seeds = [
    [-150, 130, 'crimson'],
    [-30, 165, 'darkorange'],
    [110, 150, 'gold'],
    [175, 55, 'yellowgreen'],
    [95, -20, 'forestgreen'],
    [165, -140, 'mediumturquoise'],
    [30, -105, 'deepskyblue'],
    [-70, -165, 'royalblue'],
    [-155, -75, 'mediumorchid'],
    [-175, 40, 'hotpink'],
    [-45, 20, 'sandybrown'],
    [40, 60, 'palevioletred'],
]

cell = 8
for gy in range(-25, 25):
    for gx in range(-25, 25):
        x = gx * cell + 4
        y = gy * cell + 4
        best = 0
        best_d = 999999
        for i in range(len(seeds)):
            dx = x - seeds[i][0]
            dy = y - seeds[i][1]
            d = dx * dx + dy * dy
            if d < best_d:
                best_d = d
                best = i
        monty.goto(x, y)
        monty.dot(12, seeds[best][2])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda la lista dei semi e trova il seme più vicino al centro dello
    schermo, il punto (0, 0). Quale colore si impossesserà del centro del canvas?
    Scegli il tuo colore, poi esegui il programma per vedere se hai scelto bene!

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
monty.penup()

seeds = [
    [-150, 130, 'crimson'],
    [-30, 165, 'darkorange'],
    [110, 150, 'gold'],
    [175, 55, 'yellowgreen'],
    [95, -20, 'forestgreen'],
    [165, -140, 'mediumturquoise'],
    [30, -105, 'deepskyblue'],
    [-70, -165, 'royalblue'],
    [-155, -75, 'mediumorchid'],
    [-175, 40, 'hotpink'],
    [-45, 20, 'sandybrown'],
    [40, 60, 'palevioletred'],
]

cell = 8
for gy in range(-25, 25):
    for gx in range(-25, 25):
        x = gx * cell + 4
        y = gy * cell + 4
        best = 0
        best_d = 999999
        for i in range(len(seeds)):
            dx = x - seeds[i][0]
            dy = y - seeds[i][1]
            d = dx * dx + dy * dy
            if d < best_d:
                best_d = d
                best = i
        monty.goto(x, y)
        monty.dot(12, seeds[best][2])

for s in seeds:
    monty.goto(s[0], s[1])
    monty.dot(10, 'black')
    monty.dot(4, 'white')`);
</script>

Il centro appartiene a **sandybrown** — il seme a `(-45, 20)` è solo a circa 49 pixel da `(0, 0)`, più vicino di qualunque altro seme. Avevi indovinato?

## Come Funziona

Ogni confine nell'immagine finita è un insieme di punti che sono *esattamente in parità* tra due semi — la bisettrice perpendicolare della linea che li congiunge. Ecco perché tutti i confini sono linee rette e ogni regione è un poligono convesso. E qui c'è la connessione con la classificazione: se i semi fossero esempi etichettati ("questo punto è arancione, quello è blu"), allora colorare ogni pixel in base al suo seme più vicino è esattamente l'algoritmo del vicino più prossimo (1-nearest-neighbor) che i sistemi di apprendimento automatico usano per classificare nuovi dati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `d = dx * dx + dy * dy` | Distanza al quadrato da questa cella a un seme — non serve la radice quadrata |
| `if d < best_d:` | Tiene traccia del seme più vicino trovato finora |
| `monty.dot(12, seeds[best][2])` | Colora la cella con il colore del seme vincitore |
| `x = gx * cell + 4` | Trasforma un indice di griglia in coordinata del centro della cella |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Hai Fondato un Nuovo Regno"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa mappa più piccola ha solo 5 semi. Aggiungi un sesto seme inserendo la riga
    `[0, 150, 'orange'],` nella lista dei semi. Dove apparirà il nuovo territorio
    arancione, e quali regioni dovranno restringersi per fargli spazio?

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
monty.penup()

seeds = [
    [-120, 100, 'crimson'],
    [120, 110, 'deepskyblue'],
    [-100, -120, 'gold'],
    [110, -100, 'mediumorchid'],
    [0, -10, 'yellowgreen'],
]

cell = 16
for gy in range(-12, 13):
    for gx in range(-12, 13):
        x = gx * cell
        y = gy * cell
        best = 0
        best_d = 999999
        for i in range(len(seeds)):
            dx = x - seeds[i][0]
            dy = y - seeds[i][1]
            d = dx * dx + dy * dy
            if d < best_d:
                best_d = d
                best = i
        monty.goto(x, y)
        monty.dot(22, seeds[best][2])

for s in seeds:
    monty.goto(s[0], s[1])
    monty.dot(10, 'black')
    monty.dot(4, 'white')`);
</script>

Il nuovo regno arancione appare nella zona centro-alta della mappa, stringendo tra loro le regioni crimson e deepskyblue — ogni nuovo seme ruba territorio solo ai suoi vicini più prossimi.

## Esperimenti

1. **Sposta una capitale.** Cambia il seme sandybrown nel primo laboratorio da `[-45, 20, ...]` a `[-45, 120, ...]`. Saprai che ha funzionato quando il centro della mappa cambia colore e tutto il bordo superiore viene ridisegnato con nuovi confini.

2. **Mostra i pixel.** Cambia `monty.dot(12, ...)` in `monty.dot(7, ...)`. Saprai che ha funzionato quando appaiono spazi bianchi tra i punti e puoi vedere che l'immagine è in realtà una griglia 50×50.

3. **Distanza Manhattan.** Sostituisci `d = dx * dx + dy * dy` con `d = abs(dx) + abs(dy)`. Saprai che ha funzionato quando i confini diventano bordi diagonali a forma di diamante — questa è la distanza Manhattan, misurata come un taxi che guida su una griglia di strade.

4. **Tredici regni.** Aggiungi `[0, 0, 'black'],` alla lista dei semi del primo laboratorio. Saprai che ha funzionato quando si apre una regione scura esattamente al centro della mappa.

!!! mascot-celebration "Il Vicino più Prossimo Vince!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato la formula della distanza 30.000 volte per costruire un vero diagramma
    di Voronoi — la stessa matematica dietro i pattern cellulari in natura e i
    classificatori del vicino più prossimo nell'apprendimento automatico!
    Prossimo: **Tassellatura a Rombi di Penrose** — il famoso pattern che non si ripete mai, costruito da rombi dorati e blu.
