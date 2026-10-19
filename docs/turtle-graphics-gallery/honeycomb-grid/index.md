---
hide:
    - toc
---
# Griglia a Nido d'Ape

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `hexagon(x, y, size)` e chiamarla da cicli annidati
- Capire il pattern delle **righe con offset** per tassellare gli esagoni
- Vedere perché gli esagoni tassellano il piano perfettamente mentre i quadrati lasciano spazi

Decine di esagoni riempiti tassellano il canvas alternando giallo e arancione — un nido d'ape perfetto proprio come un alveare.

!!! mascot-welcome "Benvenuto al Nido d'Ape!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli esagoni sono speciali: tassellano il piano perfettamente senza spazi o sovrapposizioni.
    In questo laboratorio scoprirai come posizionarli usando un ordinato trucco a righe con offset.
    Programmiamo insieme!

## Come Funziona la Tassellatura

Ogni esagono è disegnato da una funzione. La chiave per la tassellatura sono le righe con offset:
- Le righe dispari si spostano a destra di metà larghezza di un esagono
- La spaziatura verticale tra le righe è l'altezza dell'esagono × 0,75

L'altezza dell'esagono è `size * 2` (da vertice a vertice) e la larghezza è `size * sqrt(3)` (da lato piatto a lato piatto, circa `size * 1.732`).

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def hexagon(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(30)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(6):
        monty.forward(size)
        monty.left(60)
    monty.end_fill()

size = 30
colors = ['gold', 'orange']
h = size * 2                     # altezza di un esagono con la punta in alto
col_w = size * math.sqrt(3)      # larghezza di un esagono con la punta in alto

for row in range(7):
    for col in range(8):
        offset = col_w / 2 if row % 2 == 1 else 0
        x = -200 + col * col_w + offset
        y = 150 - row * h * 0.75
        hexagon(x, y, size, colors[(row + col) % 2])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Un esagono ha 6 lati. L'angolo esterno a ogni angolo è `360 / 6 = 60°`.
    Dopo aver disegnato tutti i 6 lati, quanti gradi totali ha girato Monty?
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

def hexagon(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(30)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(6):
        monty.forward(size)
        monty.left(60)
    monty.end_fill()

size = 30
colors = ['gold', 'orange']
h = size * 2                     # altezza di un esagono con la punta in alto
col_w = size * math.sqrt(3)      # larghezza di un esagono con la punta in alto

for row in range(7):
    for col in range(8):
        offset = col_w / 2 if row % 2 == 1 else 0
        x = -200 + col * col_w + offset
        y = 150 - row * h * 0.75
        hexagon(x, y, size, colors[(row + col) % 2])`);
</script>

6 × 60° = **360°** — una rotazione completa, proprio come ogni poligono regolare. Avevi indovinato?

## Come Funziona

La funzione `hexagon()` usa `setheading(30)` così ogni esagono inizia a un angolo di 30°, producendo un esagono **con la punta in alto**. Reimpostare la direzione all'inizio di ogni chiamata è essenziale — non sai mai a che angolo si trovi Monty quando la funzione viene chiamata.

La formula dell'offset `col_w / 2 if row % 2 == 1 else 0` sposta le righe dispari a destra di metà della larghezza dell'esagono, sfalsandole: così ogni esagono si incastra nello spazio tra due esagoni della riga sopra.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def hexagon(x, y, size, color)` | Funzione riutilizzabile: disegna un esagono alla posizione (x,y) |
| `monty.setheading(30)` | Inizia a 30° per disegnare un esagono con la punta in alto — critico per la tassellatura corretta |
| `monty.left(60)` | Angolo esterno di un esagono (360/6) |
| `h = size * 2` | Altezza di un esagono con la punta in alto (da vertice a vertice) |
| `col_w = size * math.sqrt(3)` | Larghezza di un esagono con la punta in alto (da lato piatto a lato piatto) |
| `offset = col_w / 2 if row % 2 == 1 else 0` | Le righe dispari si spostano a destra di metà larghezza dell'esagono |
| `y = 150 - row * h * 0.75` | Le righe si sovrappongono del 25% dell'altezza così gli esagoni si incastrano |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna esagoni ma non tassellano — ci sono spazi vuoti e sovrapposizioni!
    La formula dell'offset di riga è sbagliata. Correggila in modo che le righe dispari si spostino esattamente di metà larghezza dell'esagono.

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

def hexagon(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(30)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(6):
        monty.forward(size)
        monty.left(60)
    monty.end_fill()

size = 30
colors = ['gold', 'orange']
h = size * 2
col_w = size * math.sqrt(3)

for row in range(7):
    for col in range(8):
        offset = col_w if row % 2 == 1 else 0
        x = -200 + col * col_w + offset
        y = 150 - row * h * 0.75
        hexagon(x, y, size, colors[(row + col) % 2])`);
</script>

Cambia `col_w` in `col_w / 2` nella riga dell'offset — lo spostamento dovrebbe essere metà della larghezza dell'esagono, non la larghezza intera.

## Esperimenti

1. **Cambia i colori.** Usa `['royalblue', 'navy']` per un nido d'ape blu. Saprai che ha funzionato quando i colori cambiano ma la tassellatura resta perfetta.

2. **Rendi gli esagoni più grandi.** Cambia `size = 30` in `size = 45` e riduci gli intervalli di riga/colonna. Saprai che ha funzionato quando meno esagoni, più grandi, tassellano il canvas.

3. **Rimuovi il riempimento.** Elimina le righe `begin_fill()` e `end_fill()` dalla funzione. Saprai che ha funzionato quando il nido d'ape mostra solo i contorni.

4. **Colora solo per riga.** Cambia `colors[(row + col) % 2]` in `colors[row % 2]`. Tutte le celle in una riga diventano dello stesso colore. Saprai che ha funzionato quando appaiono fasce orizzontali di colore alternato.

!!! mascot-celebration "Lavoro Incredibile!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un motore di tassellatura completo con una funzione, cicli annidati e geometria a righe con offset!
    Le api hanno scoperto questo pattern milioni di anni fa — e ora conosci la matematica che c'è dietro.
    Prossimo: **Skyline Urbano** — comporre una scena da funzioni riutilizzabili per edifici.
