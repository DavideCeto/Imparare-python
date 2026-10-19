# Parametri delle Funzioni: Disegnare Quadrati Ovunque

Alla fine di questa lezione sarai in grado di:

- Aggiungere **parametri** a una funzione così chi la chiama può passare dei valori
- Chiamare la stessa funzione più volte con colori e posizioni diverse
- Usare `penup()` e `goto()` per riposizionare la tartaruga senza disegnare

Una funzione può fare molte cose diverse se le dai dei **parametri** — input che riceve da chi la chiama. In questo laboratorio, scriverai una funzione `square()` che accetta un colore e una posizione, poi la chiamerai quattro volte per dipingere quattro quadrati di colore diverso attorno al canvas.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sai già come definire una funzione. Oggi farai funzioni che possono ricevere istruzioni!
    Una funzione con parametri è come una macchina distributrice — premi un bottone (passi un valore)
    e ottieni esattamente quello che hai chiesto. Programmiamo insieme!

## Parametri: Input per le Funzioni

Un **parametro** è una variabile dentro le parentesi di una funzione che riceve un valore quando la funzione viene chiamata:

```python
def square(my_color, x, y):
    # my_color, x e y vengono forniti da chi chiama la funzione
    monty.color(my_color)
    ...
```

Quando chiami `square('red', -50, 80)`, Python imposta `my_color = 'red'`, `x = -50`, e `y = 80` automaticamente — nessuna assegnazione extra necessaria.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

size = 60
angle = 90

def square(my_color, x, y):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(my_color)
    monty.begin_fill()
    for i in range(4):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()

square('red',    -80,  80)
square('orange',  20,  80)
square('green',  -80, -20)
square('blue',    20, -20)
monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `square()` viene chiamata quattro volte con quattro colori diversi e quattro posizioni diverse.
    Quanti quadrati appariranno sul canvas, e dove saranno?
    Fai la tua previsione — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato direttamente su questa pagina.
Nessun account necessario — tutto gira nel tuo browser.

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
monty.shape('turtle')

size = 60
angle = 90

def square(my_color, x, y):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(my_color)
    monty.begin_fill()
    for i in range(4):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()

square('red',    -80,  80)
square('orange',  20,  80)
square('green',  -80, -20)
square('blue',    20, -20)
monty.hideturtle()`);
</script>

Avevi indovinato? Quattro quadrati riempiti in una griglia 2×2 — rosso e arancione in alto, verde e blu in basso.

## Come Funziona

`penup()` alza la penna così non appare nessuna linea mentre la tartaruga viaggia verso la nuova posizione. `goto(x, y)` muove la tartaruga a quella coordinata esatta. `pendown()` abbassa la penna così il disegno riprende. Questo pattern penup/goto/pendown è come inizi qualsiasi forma a una posizione specifica.

Ogni volta che `square()` viene chiamata con argomenti diversi, Python crea nuove copie di `my_color`, `x`, e `y` dentro la funzione — i valori della chiamata precedente sono spariti. La funzione li usa, finisce, e aspetta di essere chiamata di nuovo.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def square(my_color, x, y):` | Definisce `square` con 3 parametri: colore, posizione orizzontale, posizione verticale |
| `monty.penup()` | Alza la penna — nessuna linea disegnata mentre si muove |
| `monty.goto(x, y)` | Muove la tartaruga alle coordinate `(x, y)` |
| `monty.pendown()` | Abbassa la penna — il disegno riprende |
| `square('red', -80, 80)` | Chiama la funzione: `my_color='red'`, `x=-80`, `y=80` |

!!! mascot-tip "La Griglia del Canvas"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Il centro del canvas è `(0, 0)`. `x` positiva va a destra, negativa va a sinistra.
    `y` positiva va in alto, negativa va in basso. Quindi `(-80, 80)` è in alto a sinistra e `(20, -20)` è in basso a destra.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Quinto Quadrato"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto disegna quattro quadrati usando la funzione `square()`.
    Aggiungi **una riga** in fondo per disegnare un quinto quadrato viola centrato a `(-30, 30)`.

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
monty.shape('turtle')

size = 60
angle = 90

def square(my_color, x, y):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(my_color)
    monty.begin_fill()
    for i in range(4):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()

square('red',    -80,  80)
square('orange',  20,  80)
square('green',  -80, -20)
square('blue',    20, -20)
# Aggiungi qui una riga per disegnare un quadrato viola in (-30, 30)
monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice dei quattro quadrati. Prevedi prima, poi esegui!

1. Cambia `size = 60` in `size = 40`.
   **Saprai che ha funzionato quando** tutti e quattro i quadrati sono più piccoli.

2. Aggiungi un quarto parametro `my_size` alla definizione della funzione, e usalo in `forward(my_size)` invece di `forward(size)`. Poi passa dimensioni diverse in ogni chiamata.
   **Saprai che ha funzionato quando** i quattro quadrati sono tutti di dimensioni diverse.

3. Aggiungi `monty.pensize(3)` dentro la funzione, prima del ciclo.
   **Saprai che ha funzionato quando** tutti e quattro i quadrati hanno un contorno più spesso.

4. Cambia il `range(4)` dentro la funzione in `range(3)` e `angle` in `120`.
   **Saprai che ha funzionato quando** vedi quattro triangoli riempiti invece di quadrati.

5. Usa un ciclo `for` per chiamare `square()` sei volte con colori da una lista.
   **Saprai che ha funzionato quando** sei forme appaiono attraverso il canvas.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    I parametri rendono le funzioni flessibili — scrivi una volta, usa ovunque con valori diversi.
    Nel prossimo laboratorio incontrerai la libreria `random` e lascerai che Python scelga colori e posizioni per te!
    Programmiamo insieme!
