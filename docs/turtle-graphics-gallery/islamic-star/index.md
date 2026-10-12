---
hide:
    - toc
---
# Stella Geometrica Islamica

Alla fine di questo laboratorio sarai in grado di:

- Costruire una stella a 8 punte usando solo linee rette e angoli di 45°
- Tassellare il pattern della stella attraverso una griglia usando la traslazione (offset per quantità fisse)
- Capire come l'arte geometrica islamica usa regole angolari esatte

Un pattern ripetuto di stelle a 8 punte e forme a croce — il tipo trovato nei lavori di piastrelle delle moschee e nei manoscritti persiani — costruito interamente da segmenti di linea retta ad angoli di 45°.

!!! mascot-welcome "Benvenuto alla Stella Islamica!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    L'arte geometrica islamica usa solo riga e compasso — nessuna curva a mano libera.
    Questo laboratorio costruisce uno dei pattern più comuni: la griglia di stelle a 8 punte!
    Programmiamo insieme!

## Come Funziona

Una stella a 8 punte è disegnata come due quadrati sovrapposti ruotati di 45° l'uno dall'altro, entrambi centrati sullo stesso punto. Una funzione `star8(cx, cy, size, color)` disegna una stella a un centro dato. Il ciclo esterno tassella le stelle in una griglia, spostando ogni stella di una spaziatura fissa.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def star8(cx, cy, size, color):
    monty.pencolor(color)
    for angle_offset in [0, 45]:
        monty.penup()
        monty.goto(cx, cy)
        monty.setheading(angle_offset - 135)
        monty.forward(size)
        monty.setheading(angle_offset)
        monty.pendown()
        for _ in range(4):
            monty.forward(size * 1.4)
            monty.left(90)

spacing = 90
colors = ['navy', 'royalblue']
for row in range(-2, 3):
    for col in range(-2, 3):
        cx = col * spacing
        cy = row * spacing
        color = colors[(row + col) % 2]
        star8(cx, cy, 30, color)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Due quadrati ruotati di 45° l'uno dall'altro formano una stella a 8 punte.
    Le stelle tassellate si collegheranno alle loro punte, o ci saranno spazi vuoti?
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

def star8(cx, cy, size, color):
    monty.pencolor(color)
    for angle_offset in [0, 45]:
        monty.penup()
        monty.goto(cx, cy)
        monty.setheading(angle_offset - 135)
        monty.forward(size)
        monty.setheading(angle_offset)
        monty.pendown()
        for _ in range(4):
            monty.forward(size * 1.4)
            monty.left(90)

spacing = 90
colors = ['navy', 'royalblue']
for row in range(-2, 3):
    for col in range(-2, 3):
        cx = col * spacing
        cy = row * spacing
        color = colors[(row + col) % 2]
        star8(cx, cy, 30, color)`);
</script>

Le stelle formano un pattern a griglia ripetuto — come i lavori di piastrelle islamiche. Avevi indovinato sugli spazi vuoti?

## Come Funziona

Una stella a 8 punte è due quadrati ruotati di 45° l'uno dall'altro, che condividono lo stesso centro. Il ciclo `for angle_offset in [0, 45]` disegna ogni quadrato in sequenza. Prima di disegnare, la tartaruga cammina dal centro `(cx, cy)` fino all'angolo di partenza del quadrato: `setheading(angle_offset - 135)` la punta verso l'angolo, e `forward(size)` fa i passi per arrivarci. Poiché entrambi i quadrati sono posizionati dallo stesso centro, la loro sovrapposizione forma una stella simmetrica a 8 punte.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `for angle_offset in [0, 45]` | Disegna due quadrati — uno ruotato di 45° dall'altro |
| `setheading(angle_offset - 135)` poi `forward(size)` | Cammina dal centro della stella all'angolo di partenza del quadrato |
| `size * 1.4` | Lunghezza del lato adattata così i due quadrati creano punte |
| `spacing = 90` | Distanza tra i centri delle stelle |
| `(row + col) % 2` | Alterna i colori in pattern a scacchiera |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia la Spaziatura"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `spacing = 90` in `spacing = 60`. Le stelle si sovrapporranno, si separeranno, o si toccheranno perfettamente?
    Prevedi, poi eseguilo per scoprirlo!

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

def star8(cx, cy, size, color):
    monty.pencolor(color)
    for angle_offset in [0, 45]:
        monty.penup()
        monty.goto(cx, cy)
        monty.setheading(angle_offset - 135)
        monty.forward(size)
        monty.setheading(angle_offset)
        monty.pendown()
        for _ in range(4):
            monty.forward(size * 1.4)
            monty.left(90)

spacing = 90
colors = ['darkred', 'darkorange']
for row in range(-2, 3):
    for col in range(-2, 3):
        cx = col * spacing
        cy = row * spacing
        color = colors[(row + col) % 2]
        star8(cx, cy, 30, color)`);
</script>

A `spacing = 60` le stelle si toccano perfettamente alle loro punte, e lo spazio rimanente tra di esse forma le forme a croce viste nei veri lavori di piastrelle islamiche.

## Esperimenti

1. **Riempi le stelle.** Aggiungi `begin_fill()` prima ed `end_fill()` dopo il ciclo interno. Saprai che ha funzionato quando i contorni delle stelle sono riempiti.

2. **Usa oro e navy.** Cambia la lista dei colori in `['navy', 'gold']`. Saprai che ha funzionato quando la scacchiera alterna stelle navy e oro.

3. **Stelle più grandi.** Cambia `size = 30` in `size = 40`. Saprai che ha funzionato quando le stelle sono più grandi e la spaziatura tra loro diminuisce.

4. **Prova una singola stella centrata.** Rimuovi i cicli esterni e chiama `star8(0, 0, 80, 'darkred')`. Saprai che ha funzionato quando una grande stella a 8 punte riempie lo schermo.

!!! mascot-celebration "Pattern Completato!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai ricreato un pattern di 1000 anni usato in moschee e palazzi!
    L'arte geometrica dimostra che la matematica e la bellezza non sono opposti — sono la stessa cosa.
    Prossimo: **Categoria 6 — Pattern di Natura e Scienza!**
