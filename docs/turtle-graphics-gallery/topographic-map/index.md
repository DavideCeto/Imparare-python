---
hide:
    - toc
---
# Mappa Topografica

Alla fine di questo laboratorio sarai in grado di:

- Tracciare anelli di curve di livello chiusi in coordinate polari con `math.sin()` e `math.cos()`
- Perturbare il raggio di un cerchio con onde sinusoidali per creare coste naturali e ondulate
- Colorare fasce di elevazione riempiendo gli anelli dall'esterno verso l'interno

Le vere mappe degli escursionisti mostrano le montagne come anelli di curve di livello annidati: ogni anello è una linea di uguale elevazione, e i colori avanzano dal verde delle pianure attraverso la roccia marrone fino a una vetta bianca. Questo laboratorio disegna un'intera isola in questo modo — otto anelli ondulati, riempiti dall'esterno verso l'interno così ogni elevazione più alta si dipinge sopra l'ultima.

!!! mascot-welcome "Benvenuto alla Mappa Topografica!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I cartografi schiacciano montagne 3D su carta piatta usando le curve
    di livello — e tu stai per diventare il cartografo. Prendi la
    bussola: stiamo disegnando un'isola che non è mai esistita, un
    livello di elevazione alla volta!

## Come Funziona

Ogni anello è un cerchio in coordinate polari il cui raggio ondula mentre l'angolo gira intorno: `r = base_r * (1 + 0.10*sin(3*theta) + 0.06*sin(7*theta + 1))`. Aggiungere due onde sinusoidali di frequenze diverse (3 e 7) fa sembrare la costa naturale invece che perfettamente rotonda, e poiché l'ondulazione è una *percentuale* di `base_r`, le protuberanze sono grandi sugli anelli esterni e dolci vicino alla vetta — e gli anelli non possono mai incrociarsi. Il ciclo disegna prima l'anello più grande e procede verso l'interno, così ogni anello riempito più piccolo si dipinge sopra quello sotto di lui, esattamente come impilare strati di elevazione.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
screen = turtle.Screen()
screen.bgcolor('lightsteelblue')

colors = ['darkgreen', 'forestgreen', 'yellowgreen', 'darkkhaki', 'peru', 'sienna', 'rosybrown', 'white']

def contour_r(base_r, theta):
    wobble = 0.10 * math.sin(3 * theta) + 0.06 * math.sin(7 * theta + 1)
    return base_r * (1 + wobble)

steps = 90
for ring in range(8):
    base_r = 160 - ring * 18
    monty.penup()
    monty.pencolor('saddlebrown')
    monty.fillcolor(colors[ring])
    monty.pensize(1)
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        r = contour_r(base_r, theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
            monty.begin_fill()
        else:
            monty.goto(x, y)
    monty.end_fill()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La formula dell'ondulazione include `math.sin(3 * theta)`, l'ondulazione
    più forte. Mentre percorri un giro intorno alla costa dell'isola,
    quante grandi protuberanze (penisole) incontrerai — 3, 7 o 10?
    Fai la tua ipotesi, poi clicca Esegui!

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
screen = turtle.Screen()
screen.bgcolor('lightsteelblue')

colors = ['darkgreen', 'forestgreen', 'yellowgreen', 'darkkhaki', 'peru', 'sienna', 'rosybrown', 'white']

def contour_r(base_r, theta):
    wobble = 0.10 * math.sin(3 * theta) + 0.06 * math.sin(7 * theta + 1)
    return base_r * (1 + wobble)

steps = 90
for ring in range(8):
    base_r = 160 - ring * 18
    monty.penup()
    monty.pencolor('saddlebrown')
    monty.fillcolor(colors[ring])
    monty.pensize(1)
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        r = contour_r(base_r, theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
            monty.begin_fill()
        else:
            monty.goto(x, y)
    monty.end_fill()`);
</script>

**3 grandi penisole** — `sin(3 * theta)` si ripete 3 volte per giro, e il più rapido `sin(7 * theta)` aggiunge solo piccole increspature sopra. Avevi indovinato?

## Come Funziona

Leggere la lista dei colori racconta tutta la storia dell'elevazione: l'anello 0 (il più grande, disegnato per primo) è la pianura `'darkgreen'`, e ogni anello verso l'interno avanza attraverso verdi più chiari, kaki e marroni fino a quando l'anello 7 è la vetta `'white'`. Questo funziona solo grazie all'ordine della pittura — il riempimento della turtle non ha idea di cosa sia "l'altezza", ma riempire dall'esterno verso l'interno fa sì che ogni anello più piccolo coprа il centro di quello più grande, lasciando visibile solo una fascia colorata. Le vere mappe topografiche usano lo stesso trucco: la fascia *tra* due curve di livello ottiene un colore di elevazione. Lo sfondo `bgcolor` blu interpreta l'oceano intorno alla costa più esterna.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `wobble = 0.10 * math.sin(3 * theta) + 0.06 * math.sin(7 * theta + 1)` | Due onde sinusoidali creano una costa bitorzoluta ma liscia |
| `return base_r * (1 + wobble)` | L'ondulazione si scala con la dimensione dell'anello, così gli anelli non si incrociano mai |
| `base_r = 160 - ring * 18` | Ogni anello è più piccolo di 18 pixel — dall'esterno verso l'interno, da basso ad alto |
| `monty.fillcolor(colors[ring])` | Fasce di elevazione: rive verdi, pendii marroni, vetta bianca |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Rimodella l'Isola"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nel programma qui sotto, `math.sin(3 * theta)` è stato cambiato in
    `math.sin(6 * theta)`. Prevedi: quante grandi penisole avrà la nuova
    costa? Eseguilo e contale!

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
screen = turtle.Screen()
screen.bgcolor('lightsteelblue')

colors = ['darkgreen', 'forestgreen', 'yellowgreen', 'darkkhaki', 'peru', 'sienna', 'rosybrown', 'white']

def contour_r(base_r, theta):
    wobble = 0.10 * math.sin(6 * theta) + 0.06 * math.sin(7 * theta + 1)
    return base_r * (1 + wobble)

steps = 90
for ring in range(8):
    base_r = 160 - ring * 18
    monty.penup()
    monty.pencolor('saddlebrown')
    monty.fillcolor(colors[ring])
    monty.pensize(1)
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        r = contour_r(base_r, theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
            monty.begin_fill()
        else:
            monty.goto(x, y)
    monty.end_fill()`);
</script>

Sei penisole — il primo numero dentro `sin(n * theta)` è esattamente quante volte quello schema di protuberanze si ripete intorno all'isola.

## Esperimenti

1. **Rendila più scoscesa.** Cambia `0.10` in `0.20`. Saprai che ha funzionato quando la costa cresce di fiordi drammatici e gli anelli si stringono vicini tra loro.

2. **Sposta il terreno.** Cambia `math.sin(7 * theta + 1)` in `math.sin(7 * theta + 4)`. Saprai che ha funzionato quando le piccole increspature si spostano in punti diversi della costa.

3. **Approfondisci l'oceano.** Cambia `screen.bgcolor('lightsteelblue')` in `screen.bgcolor('midnightblue')`. Saprai che ha funzionato quando l'isola brilla contro un mare scuro da carta nautica notturna.

4. **Ribalta l'elevazione.** Inverti la lista dei colori (metti `'white'` primo e `'darkgreen'` ultimo). Saprai che ha funzionato quando la mappa diventa un cratere innevato a forma di anello con un fondovalle verde al centro.

!!! mascot-celebration "Cartografo Esperto!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Coordinate polari, ondulazioni sinusoidali a strati, e pittura
    dall'esterno verso l'interno — hai trasformato la matematica in una
    mappa degna dello zaino di un esploratore. Esplora la **Galleria di
    Grafica Turtle** per la tua prossima sfida!
