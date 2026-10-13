---
hide:
    - toc
---
# Griglia Scintillante

Alla fine di questo laboratorio sarai in grado di:

- Posizionare barre e punti con precisione su una griglia usando cicli annidati e calcoli di coordinate
- Sovrapporre forme nell'ordine giusto così i disegni successivi si trovano sopra quelli precedenti
- Spiegare come il contrasto locale inganna i tuoi occhi facendoti vedere punti che lampeggiano

Uno sfondo scuro, un reticolo di "strade" grigio medio, e un nitido punto bianco a ogni intersezione. Quando guardi in giro per l'immagine, fantomatici punti scuri lampeggiano dentro quelli bianchi — ma solo alle intersezioni che *non* stai guardando direttamente. Inseguine uno e svanisce! Questa è l'illusione della griglia scintillante, scoperta nel 1994.

!!! mascot-welcome "Benvenuto alla Griglia Scintillante!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questa è una delle illusioni più potenti mai trovate — i tuoi occhi
    vedranno punti neri lampeggiare dentro punti che il codice dipinge
    puro bianco. Venticinque punti bianchi, zero neri. Costruiamola!

## Come Funziona

Prima `screen.bgcolor` riempie lo sfondo di grigio scuro. Un ciclo disegna cinque barre verticali e cinque orizzontali grigie, distanziate di `gap` pixel, usando una funzione di supporto per rettangoli riempiti. Poi un ciclo annidato visita tutte le 25 intersezioni e timbra un punto bianco su ognuna. I punti sono leggermente più larghi delle barre, così sporgono nei quadrati scuri — quella piccola sovrapposizione è ciò che rende il lampeggio così forte.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
screen = turtle.Screen()
screen.bgcolor('#282828')

bar = 10
gap = 70

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

for i in range(-2, 3):
    filled_rect(i * gap - bar / 2, -180, bar, 360, 'gray')
    filled_rect(-180, i * gap - bar / 2, 360, bar, 'gray')

for i in range(-2, 3):
    for j in range(-2, 3):
        monty.penup()
        monty.goto(i * gap, j * gap)
        monty.dot(16, 'white')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice timbra esattamente 25 punti bianchi e non ne disegna mai
    uno scuro. Quando lasci vagare gli occhi per la griglia finita,
    tutti e 25 i punti resteranno bianchi? Fai la tua ipotesi, poi
    clicca Esegui!

## Prova Ora

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
screen = turtle.Screen()
screen.bgcolor('#282828')

bar = 10
gap = 70

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

for i in range(-2, 3):
    filled_rect(i * gap - bar / 2, -180, bar, 360, 'gray')
    filled_rect(-180, i * gap - bar / 2, 360, bar, 'gray')

for i in range(-2, 3):
    for j in range(-2, 3):
        monty.penup()
        monty.goto(i * gap, j * gap)
        monty.dot(16, 'white')`);
</script>

Punti scuri lampeggiano alle intersezioni nell'angolo del tuo occhio, ma il punto che fissi resta bianco. Avevi indovinato?

## Come Funziona

Le cellule nella tua retina misurano la luminosità confrontando un punto con ciò che lo circonda — un trucco chiamato inibizione laterale. A un'intersezione, un punto bianco è circondato da quattro strade grigie luminose, così il suo segnale di luminosità viene spinto giù con forza e per un momento viene letto come scuro. La tua visione centrale (la fovea) usa zone di confronto molto più piccole, così il punto che guardi direttamente viene misurato correttamente e resta bianco. Ecco perché i fantasmi scuri danzano sempre appena fuori portata.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `screen.bgcolor('#282828')` | Sfondo grigio scuro — i quadrati tra le strade |
| `filled_rect(i * gap - bar / 2, -180, bar, 360, 'gray')` | Una strada verticale, centrata sulla linea della griglia `i` |
| `for i in range(-2, 3):` | Cinque linee della griglia a -140, -70, 0, 70, 140 |
| `monty.dot(16, 'white')` | Punto bianco, più largo della strada di 10 pixel, a ognuno dei 25 incroci |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Disastro — tutti e 25 i punti bianchi sono spariti da questa
    versione, eppure il ciclo che timbra i punti c'è di sicuro. Niente è
    stato eliminato, ma due blocchi di codice sono stati scambiati.
    Riesci a capire perché i punti sono invisibili e a correggerlo?

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
screen = turtle.Screen()
screen.bgcolor('#282828')

bar = 10
gap = 70

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

for i in range(-2, 3):
    for j in range(-2, 3):
        monty.penup()
        monty.goto(i * gap, j * gap)
        monty.dot(16, 'white')

for i in range(-2, 3):
    filled_rect(i * gap - bar / 2, -180, bar, 360, 'gray')
    filled_rect(-180, i * gap - bar / 2, 360, bar, 'gray')`);
</script>

I punti vengono disegnati *per primi*, poi le barre grigie vengono dipinte proprio sopra di essi — la grafica turtle sovrappone le forme nell'ordine di disegno, come strati di vernice. Sposta il ciclo dei punti sotto il ciclo delle barre e i punti riappariranno sopra.

## Esperimenti

1. **Rimpicciolisci i punti.** Cambia `monty.dot(16, 'white')` in `monty.dot(10, 'white')` così i punti corrispondono esattamente alla larghezza della strada. Saprai che ha funzionato quando i punti non sporgono più nei quadrati scuri — il lampeggio è più debole?

2. **Schiarisci le strade.** Cambia entrambe le stringhe `'gray'` in `'lightgray'`. Saprai che ha funzionato quando le strade sono quasi bianche — la versione classica di questo esperimento fa svanire la scintillazione.

3. **Stringi la griglia.** Cambia `gap = 70` in `gap = 45` ed entrambi i cicli della griglia `range(-2, 3)` in `range(-3, 4)`. Saprai che ha funzionato quando appare una griglia 7 × 7 di 49 punti e il lampeggio diventa ancora più affollato.

4. **Prova una versione colorata.** Cambia il colore dei punti in `'yellow'` e lo sfondo in `'#102040'`. Saprai che ha funzionato quando punti gialli scintillano su una griglia blu scuro — i punti fantasma appaiono ancora!

!!! mascot-celebration "Ora li Vedi, Ora No!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito una delle illusioni più potenti della scienza con due
    cicli e 25 punti bianchi — e hai imparato perché l'ordine di disegno
    conta quanto le coordinate. Prossimo: **Triangolo Impossibile** — un
    oggetto che non può esistere, disegnato in 30 righe.
