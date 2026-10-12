---
hide:
    - toc
---
# Skyline Urbano

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `building()` con più parametri
- Comporre una scena da molte chiamate di funzione con argomenti diversi
- Disegnare finestre con cicli annidati dentro una funzione di disegno

Dieci grattacieli di altezze e tonalità variate si allineano attraverso il canvas,
le loro finestre gialle che brillano contro le sagome scure.

!!! mascot-welcome "Benvenuto allo Skyline Urbano!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio scriverai una funzione che disegna un intero edificio — mura e finestre —
    poi la chiamerai 10 volte per costruire una città completa. Programmiamo insieme!

## Come Funziona la Scena

La funzione `building(x, w, h, color)` disegna un rettangolo riempito nella posizione `x`,
con larghezza `w`, altezza `h`, e riempimento `color`. Poi cicla per aggiungere punti gialli per le finestre.

Dopo aver definito la funzione una volta, la chiamiamo 10 volte con argomenti diversi —
ogni chiamata produce un grattacielo completamente diverso.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def building(x, w, h, color):
    monty.penup()
    monty.goto(x, -180)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()
    for row in range(h // 35):
        for col in range(w // 20):
            monty.penup()
            monty.goto(x + 10 + col * 18, -160 + row * 30)
            monty.dot(8, 'yellow')

data = [(-280,45,110,'#2d2d2d'),(-225,50,160,'#3a3a3a'),(-165,40,90,'#252525'),
        (-115,55,200,'#333'),(-50,60,140,'#2a2a2a'),(20,50,170,'#383838'),
        (80,45,120,'#2d2d2d'),(135,55,90,'#303030'),(200,50,180,'#3a3a3a'),
        (260,40,100,'#282828')]

for d in data:
    building(*d)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione `building()` viene chiamata 10 volte, ognuna con valori `h` (altezza) diversi.
    Quale edificio sarà il più alto — il primo disegnato o l'ultimo?
    Scorri la lista dei dati e fai la tua previsione — poi clicca Esegui per scoprirlo!

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

def building(x, w, h, color):
    monty.penup()
    monty.goto(x, -180)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()
    for row in range(h // 35):
        for col in range(w // 20):
            monty.penup()
            monty.goto(x + 10 + col * 18, -160 + row * 30)
            monty.dot(8, 'yellow')

data = [(-280,45,110,'dimgray'),(-225,50,160,'darkslategray'),(-165,40,90,'gray'),
        (-115,55,200,'slategray'),(-50,60,140,'dimgray'),(20,50,170,'darkgray'),
        (80,45,120,'slategray'),(135,55,90,'gray'),(200,50,180,'darkslategray'),
        (260,40,100,'dimgray')]

for d in data:
    building(*d)`);
</script>

L'edificio più alto ha `h=200` — è la 4ª voce a `x=-115`. Avevi indovinato?

## Come Funziona

`for side in [w, h, w, h]` è un ciclo intelligente su una lista di lunghezze: lato destro, in alto, lato sinistro, in basso — disegnando il rettangolo senza scrivere a mano quattro chiamate `forward` separate.

`building(*d)` usa l'**operatore di spacchettamento** `*` per distribuire una tupla `(x, w, h, color)` in quattro argomenti separati, così non devi scrivere `building(d[0], d[1], d[2], d[3])`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def building(x, w, h, color)` | Funzione con quattro parametri: posizione, larghezza, altezza, colore |
| `for side in [w, h, w, h]` | Disegna quattro lati in un ciclo usando una lista |
| `h // 35` | Divisione intera: numero di righe di finestre che entrano |
| `w // 20` | Numero di colonne di finestre che entrano |
| `building(*d)` | Spacchetta la tupla `d` negli argomenti della funzione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Tetto"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione `building()` sotto disegna muri e finestre ma non ha nessun dettaglio sul tetto.
    Aggiungi **due righe** dopo `end_fill()` per disegnare un sottile rettangolo rosso (`height = 10`) attraverso il tetto.

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

def building(x, w, h, color):
    monty.penup()
    monty.goto(x, -180)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()
    # ADD: draw a red rooftop rectangle here
    for row in range(h // 35):
        for col in range(w // 20):
            monty.penup()
            monty.goto(x + 10 + col * 18, -160 + row * 30)
            monty.dot(8, 'yellow')

building(-100, 80, 150, 'slategray')
building(30, 60, 120, 'dimgray')
building(110, 70, 180, 'darkslategray')`);
</script>

Dopo `end_fill()` aggiungi: `monty.penup(); monty.goto(x, -180+h)` poi disegna un rettangolo rosso riempito `w × 10`.

## Esperimenti

1. **Aggiungi un cielo.** Prima di chiamare qualsiasi edificio, disegna un grande rettangolo riempito blu scuro che copre tutto lo sfondo del canvas. Saprai che ha funzionato quando lo skyline si trova contro un cielo notturno.

2. **Aggiungi una luna.** Dopo il cielo, aggiungi `monty.penup(); monty.goto(100, 100); monty.dot(60, 'lightyellow')`. Saprai che ha funzionato quando un cerchio luminoso appare sopra lo skyline.

3. **Cambia il colore delle finestre.** Sostituisci `'yellow'` con `'white'`. Saprai che ha funzionato quando le finestre sembrano luci fluorescenti da ufficio.

4. **Fai una città più larga.** Aggiungi altri 5 edifici alla lista `data`. Saprai che ha funzionato quando lo skyline si estende più lontano attraverso il canvas.

!!! mascot-celebration "Lavoro Fantastico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai composto un'intera scena da una singola funzione riutilizzabile!
    È esattamente così che funzionano i motori di gioco, gli strumenti CAD, e i renderer di mappe dietro le quinte.
    Prossimo: **Bracci del Fiocco di Neve** — usare una funzione per costruire simmetria a sei pieghe.
