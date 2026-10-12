---
hide:
    - toc
---
# Muro di Mattoni

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `brick()` e chiamarla da cicli annidati
- Applicare il pattern delle **righe con offset** per scalare le righe alterne
- Usare `pencolor` e `fillcolor` separatamente per aggiungere contorni a forme riempite

Otto righe di mattoni rosso-marrone caldo riempiono il canvas, ogni riga scalata
di metà mattone — proprio come un vero muro posato da un muratore.

!!! mascot-welcome "Benvenuto al Muro di Mattoni!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La posa dei mattoni ha un segreto: le righe alterne sono spostate di metà mattone così le crepe
    non si allineano e il muro resta forte. Programmerai subito questo stesso pattern!
    Programmiamo insieme!

## Come Funziona il Muro

La funzione `brick(x, y, w, h, color)` disegna un rettangolo riempito con un contorno scuro.
Il pattern dell'offset: se `row % 2 == 1` (una riga dispari), sposta la x di partenza di metà larghezza di un mattone.
Questo scala le righe così ogni mattone attraversa la giunzione di due mattoni sotto di esso.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def brick(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.pencolor('black')
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

bw, bh = 70, 28
colors = ['firebrick', 'brown', 'darkred']

for row in range(8):
    offset = bw // 2 if row % 2 == 1 else 0
    for col in range(-3, 5):
        x = col * bw + offset - 180
        y = -150 + row * bh
        brick(x, y, bw - 3, bh - 3, colors[(row + col) % 3])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Le righe dispari (`row % 2 == 1`) sono spostate a destra di `bw // 2 = 35` pixel.
    I mattoni della riga 1 (dispari) si allineeranno con le giunzioni della riga 0, o con i centri dei mattoni della riga 0?
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

def brick(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.pencolor('black')
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

bw, bh = 70, 28
colors = ['firebrick', 'brown', 'darkred']

for row in range(8):
    offset = bw // 2 if row % 2 == 1 else 0
    for col in range(-3, 5):
        x = col * bw + offset - 180
        y = -150 + row * bh
        brick(x, y, bw - 3, bh - 3, colors[(row + col) % 3])`);
</script>

I mattoni della riga 1 si allineano con i **centri** dei mattoni della riga 0 — questo è ciò che lo rende un vero legame a offset. Avevi indovinato?

## Come Funziona

`monty.fillcolor(color)` e `monty.pencolor('black')` impostano i colori di riempimento e contorno indipendentemente. Questo è come disegni forme riempite con un bordo visibile — `monty.color(c)` imposta entrambi allo stesso colore, ma `fillcolor`/`pencolor` ti permettono di separarli.

`offset = bw // 2 if row % 2 == 1 else 0` è l'**espressione ternaria** di Python: un `if/else` compatto su una riga. Si legge: "imposta offset a metà mattone se la riga è dispari, altrimenti zero."

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.fillcolor(color)` | Imposta il colore di riempimento separatamente dal contorno |
| `monty.pencolor('black')` | Imposta il colore del contorno su nero |
| `offset = bw // 2 if row % 2 == 1 else 0` | Ternario: sposta le righe dispari di metà mattone |
| `for side in [w, h, w, h]` | Disegna quattro lati in un ciclo |
| `colors[(row + col) % 3]` | Scorre tre tonalità di mattone attraverso il muro |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna una griglia di mattoni ma NON sono scalati — tutte le righe si allineano!
    Correggi l'unica riga che calcola l'offset così le righe alterne si spostino di metà larghezza di un mattone.

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

def brick(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.pencolor('black')
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

bw, bh = 70, 28

for row in range(8):
    offset = 0
    for col in range(-3, 5):
        x = col * bw + offset - 180
        y = -150 + row * bh
        brick(x, y, bw - 3, bh - 3, 'firebrick')`);
</script>

Cambia `offset = 0` in `offset = bw // 2 if row % 2 == 1 else 0`.

## Esperimenti

1. **Cambia i colori dei mattoni.** Sostituisci `['firebrick','brown','darkred']` con `['lightyellow','beige','wheat']` per un muro di pietra chiara. Saprai che ha funzionato quando il colore del muro cambia completamente.

2. **Fai mattoni più alti.** Cambia `bh = 28` in `bh = 40`. Saprai che ha funzionato quando ci sono meno righe di mattoni più alti.

3. **Prova l'offset a legame corrente.** Cambia l'offset in `bw // 3` per un pattern diverso chiamato legame corrente. Saprai che ha funzionato quando lo scalamento è un terzo di mattone invece di metà.

4. **Aggiungi la malta.** Cambia `bh - 3` in `bh - 5` e `bw - 3` in `bw - 6`. Gli spazi più grandi mostrano più "malta" tra i mattoni. Saprai che ha funzionato quando gli spazi scuri diventano più larghi.

!!! mascot-celebration "Lavoro Incredibile!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato un muro di mattoni completo con righe a offset, colori di riempimento e contorno separati,
    e un ciclo di tre tonalità di colore — questa è vera maestria in Python!
    Prossimo: **Stelle di Diverse Dimensioni** — la geometria di una stella a 5 punte.
