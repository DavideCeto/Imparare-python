---
hide:
    - toc
---
# Nervatura della Foglia

Alla fine di questo laboratorio sarai in grado di:

- Disegnare contorni curvi lisci da molti piccoli passi `goto()`
- Curvare una linea gradualmente usando piccoli passi `forward()` + `left()`
- Usare cicli annidati per costruire tre livelli di venature: centrale, secondaria, terziaria

Tieni una foglia controluce e vedrai una bellissima rete ramificata: una venatura centrale spessa, venature secondarie che si staccano a intervalli regolari, e minuscole venature terziarie che si ramificano da quelle. Questo laboratorio disegna tutta questa struttura a tre livelli — un vero pezzo di anatomia vegetale — in circa 60 righe di Python.

!!! mascot-welcome "Benvenuto alla Nervatura della Foglia!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le venature sono l'impianto idraulico di una foglia — portano l'acqua
    fuori e il cibo dentro. Oggi costruirai una foglia strato per strato:
    prima il contorno, poi la venatura centrale, poi venature che si
    ramificano da altre venature. Botanica incontra i cicli!

## Come Funziona

Il contorno è formato da due archi speculari: per ogni lato, un ciclo calcola punti con `x = side * half * sin(pi * t)` mentre `t` va dalla base alla punta, il che fa rigonfiare nel mezzo e arrivare a una punta a entrambe le estremità. Poi una venatura centrale spessa corre dritta su per il mezzo. Un ciclo annidato aggiunge il dettaglio: il ciclo esterno percorre 9 posizioni su per la venatura centrale, e per ogni lato disegna una venatura secondaria usando molti piccoli passi `forward(4)` + `left(1.5)` così la venatura si curva dolcemente verso la punta — e ogni 4° passo si ferma per disegnare una minuscola venatura terziaria prima di continuare.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

base_y = -170
tip_y = 170
half = 105

monty.pensize(3)
monty.pencolor('darkgreen')
monty.fillcolor('palegreen')
monty.penup()
monty.goto(0, base_y)
monty.pendown()
monty.begin_fill()
steps = 50
for side in [1, -1]:
    for i in range(steps + 1):
        if side == 1:
            t = i * 1.0 / steps
        else:
            t = 1.0 - i * 1.0 / steps
        x = side * half * math.sin(math.pi * t)
        y = base_y + (tip_y - base_y) * t
        monty.goto(x, y)
monty.end_fill()

monty.penup()
monty.goto(0, base_y)
monty.setheading(90)
monty.pendown()
monty.pensize(5)
monty.pencolor('darkgreen')
monty.goto(0, tip_y)

for i in range(1, 10):
    t = i / 10.0
    y = base_y + (tip_y - base_y) * t
    reach = half * math.sin(math.pi * t) * 0.85
    for side in [1, -1]:
        monty.penup()
        monty.goto(0, y)
        monty.setheading(90 - side * 60)
        monty.pendown()
        monty.pensize(2)
        monty.pencolor('forestgreen')
        n = int(reach / 4)
        for step in range(n):
            monty.forward(4)
            monty.left(side * 1.5)
            if step > 0 and step % 4 == 0:
                px = monty.xcor()
                py = monty.ycor()
                ph = monty.heading()
                monty.pensize(1)
                monty.pencolor('seagreen')
                monty.setheading(ph - side * 45)
                monty.forward(7)
                monty.penup()
                monty.goto(px, py)
                monty.setheading(ph)
                monty.pendown()
                monty.pensize(2)
                monty.pencolor('forestgreen')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo delle venature secondarie è `for i in range(1, 10)`, e in
    ogni posizione disegna una venatura a **destra** e una a **sinistra**.
    Quante venature secondarie avrà in totale la foglia finita?
    Contale, poi clicca Esegui!

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

base_y = -170
tip_y = 170
half = 105

monty.pensize(3)
monty.pencolor('darkgreen')
monty.fillcolor('palegreen')
monty.penup()
monty.goto(0, base_y)
monty.pendown()
monty.begin_fill()
steps = 50
for side in [1, -1]:
    for i in range(steps + 1):
        if side == 1:
            t = i * 1.0 / steps
        else:
            t = 1.0 - i * 1.0 / steps
        x = side * half * math.sin(math.pi * t)
        y = base_y + (tip_y - base_y) * t
        monty.goto(x, y)
monty.end_fill()

monty.penup()
monty.goto(0, base_y)
monty.setheading(90)
monty.pendown()
monty.pensize(5)
monty.pencolor('darkgreen')
monty.goto(0, tip_y)

for i in range(1, 10):
    t = i / 10.0
    y = base_y + (tip_y - base_y) * t
    reach = half * math.sin(math.pi * t) * 0.85
    for side in [1, -1]:
        monty.penup()
        monty.goto(0, y)
        monty.setheading(90 - side * 60)
        monty.pendown()
        monty.pensize(2)
        monty.pencolor('forestgreen')
        n = int(reach / 4)
        for step in range(n):
            monty.forward(4)
            monty.left(side * 1.5)
            if step > 0 and step % 4 == 0:
                px = monty.xcor()
                py = monty.ycor()
                ph = monty.heading()
                monty.pensize(1)
                monty.pencolor('seagreen')
                monty.setheading(ph - side * 45)
                monty.forward(7)
                monty.penup()
                monty.goto(px, py)
                monty.setheading(ph)
                monty.pendown()
                monty.pensize(2)
                monty.pencolor('forestgreen')`);
</script>

**18 venature** — 9 posizioni per 2 lati. Avevi indovinato?

## Come Funziona

Guarda bene come le venature ottengono la loro lunghezza: `reach = half * math.sin(math.pi * t) * 0.85` è la *stessa* formula del seno usata per il contorno, ridotta in scala. Questo garantisce che ogni venatura si adatti dentro la foglia — venature lunghe nella parte grassa centrale, corte vicino alla punta e alla base. La curva nasce girando solo di 1.5° dopo ogni passo di 4 pixel: 20 piccole svolte si somma­no in una curvatura liscia verso la punta, esattamente come le vere venature secondarie si inarcano verso l'alto. Le venature terziarie usano un trucco di salva-e-ripristina — ricordano posizione e direzione, scattano via a 45°, poi tornano con `goto` e continuano.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `x = side * half * math.sin(math.pi * t)` | L'arco del contorno: larghezza zero alla base e alla punta, massima nel mezzo |
| `monty.forward(4)` + `monty.left(side * 1.5)` | Molti piccoli passi e svolte creano una venatura curva e liscia |
| `reach = half * math.sin(math.pi * t) * 0.85` | Le venature sono più lunghe nel mezzo della foglia, più corte vicino alle estremità |
| `if step > 0 and step % 4 == 0:` | Ogni 4° passo, si ferma e fa germinare una minuscola venatura terziaria |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Questa foglia semplificata compila ed esegue — ma tutte le 18
    venature secondarie crescono solo sul **lato destro**! Una riga ha
    scordato di usare la variabile `side`. Trovala, correggila, e rendi
    di nuovo verde il lato sinistro.

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

base_y = -170
tip_y = 170
half = 105

monty.pensize(3)
monty.pencolor('darkgreen')
monty.fillcolor('palegreen')
monty.penup()
monty.goto(0, base_y)
monty.pendown()
monty.begin_fill()
steps = 50
for side in [1, -1]:
    for i in range(steps + 1):
        if side == 1:
            t = i * 1.0 / steps
        else:
            t = 1.0 - i * 1.0 / steps
        x = side * half * math.sin(math.pi * t)
        y = base_y + (tip_y - base_y) * t
        monty.goto(x, y)
monty.end_fill()

monty.penup()
monty.goto(0, base_y)
monty.pendown()
monty.pensize(5)
monty.goto(0, tip_y)

for i in range(1, 10):
    t = i / 10.0
    y = base_y + (tip_y - base_y) * t
    reach = half * math.sin(math.pi * t) * 0.85
    for side in [1, -1]:
        monty.penup()
        monty.goto(0, y)
        monty.setheading(90 - 60)
        monty.pendown()
        monty.pensize(2)
        monty.pencolor('forestgreen')
        n = int(reach / 4)
        for step in range(n):
            monty.forward(4)
            monty.left(side * 1.5)`);
</script>

Il bug è `monty.setheading(90 - 60)` — dovrebbe essere `monty.setheading(90 - side * 60)`. Senza `side`, entrambi i "lati" partono puntando in alto a destra, così la metà sinistra della foglia resta vuota.

## Esperimenti

1. **Fai crescere una foglia di salice.** Cambia `half = 105` in `half = 55`. Saprai che ha funzionato quando la foglia diventa lunga e stretta con venature corte.

2. **Aggiungi più venature.** Cambia `range(1, 10)` in `range(1, 14)` e `t = i / 10.0` in `t = i / 14.0`. Saprai che ha funzionato quando la foglia ha 26 venature secondarie ammassate più vicine.

3. **Curva di più.** Cambia `monty.left(side * 1.5)` in `monty.left(side * 3)`. Saprai che ha funzionato quando le venature si inarcano verso l'alto in curve marcate come una foglia tropicale.

4. **Colori d'autunno.** Cambia `'palegreen'` in `'gold'` e `'forestgreen'` in `'chocolate'`. Saprai che ha funzionato quando la tua foglia sembra pronta a cadere in ottobre.

!!! mascot-celebration "Un Occhio da Botanico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Contorno, venatura centrale, secondaria, terziaria — hai costruito
    una foglia nel modo in cui lo fa una pianta, un livello di struttura
    alla volta, con cicli annidati. Prossimo: **Doppia Elica del DNA** —
    due onde sinusoidali e uno spostamento di fase di 180° costruiscono
    la molecola della vita.
