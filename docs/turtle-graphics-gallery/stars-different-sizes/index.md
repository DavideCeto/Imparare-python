---
hide:
    - toc
---
# Stelle di Diverse Dimensioni

Alla fine di questo laboratorio sarai in grado di:

- Disegnare una stella a 5 punte usando il trucco dell'**angolo esterno di 144°**
- Scrivere una funzione `star(x, y, size, color)` con quattro parametri
- Disperdere più stelle attraverso il canvas usando `random`

Quindici stelle oro e rosse di varie dimensioni sono disperse su un canvas scuro,
ognuna disegnata con lo stesso trucco a cinque righe — una perfetta scorciatoia poligonale.

!!! mascot-welcome "Benvenuto a Stelle di Diverse Dimensioni!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sapevi che puoi disegnare una stella a 5 punte girando di 144° a ogni punta?
    In questo laboratorio imparerai perché, poi disperderai stelle di diverse dimensioni attraverso il canvas!
    Programmiamo insieme!

## Come Funziona la Stella

L'angolo esterno di una stella a 5 punte è **144°** (non il solito `360 / 5 = 72°` del poligono).
Questo perché la stella salta un vertice ogni volta, così l'angolo effettivo è `2 × 72° = 144°`.
Cinque lati × 144° = 720° = due rotazioni complete — che è esattamente come funziona geometricamente la punta di una stella.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.screen().bgcolor('black') if hasattr(monty, 'screen') else None
random.seed(7)

def star(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()

colors = ['gold','yellow','orange','red','white']

for _ in range(15):
    x = random.randint(-250, 250)
    y = random.randint(-180, 180)
    size = random.randint(20, 100)
    c = random.choice(colors)
    star(x, y, size, c)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione `star()` disegna 5 linee e gira di 144° ogni volta.
    5 × 144° = 720°. Sono **due** rotazioni complete. La tartaruga finirà rivolta nella stessa direzione in cui ha iniziato?
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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(7)

def star(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()

colors = ['gold','yellow','orange','red','white']

for _ in range(15):
    x = random.randint(-250, 250)
    y = random.randint(-180, 180)
    size = random.randint(20, 100)
    c = random.choice(colors)
    star(x, y, size, c)`);
</script>

Sì — 720° = 2 rotazioni complete, così la tartaruga finisce rivolta esattamente nella direzione in cui ha iniziato. Avevi indovinato?

## Come Funziona

La funzione `star()` usa `goto(x, y)` per saltare al primo punto della stella, poi disegna 5 linee di `size` pixel, girando di 144° a destra dopo ognuna.

Poiché 5 × 144° = 720° (esattamente due cerchi completi), l'ultima linea fa atterrare la tartaruga di nuovo all'inizio rivolta nella direzione originale — chiudendo la stella perfettamente senza nessuna matematica extra.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def star(x, y, size, color)` | Funzione a quattro parametri: posizione, dimensione, e colore |
| `monty.goto(x, y)` | Salta al punto di partenza della stella |
| `for _ in range(5)` | Disegna 5 punte della stella |
| `monty.right(144)` | 144° = l'angolo esterno di una stella a 5 punte |
| `random.randint(20, 100)` | Dimensione casuale tra 20 e 100 pixel |

!!! mascot-tip "Perché 144°?"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Un pentagono regolare ha angolo esterno 72°. Una stella salta un vertice ogni passo,
    così l'angolo raddoppia: 2 × 72° = **144°**. Per una stella a 6 punte l'angolo sarebbe 2 × 60° = 120°.

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna forme ma sembrano pentagoni, non stelle!
    Trova e correggi l'unico numero sbagliato nella funzione `star()`.

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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(7)

def star(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(5):
        monty.forward(size)
        monty.right(72)
    monty.end_fill()

colors = ['gold','yellow','orange','red']

for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-150, 150)
    size = random.randint(30, 80)
    star(x, y, size, random.choice(colors))`);
</script>

Cambia `monty.right(72)` in `monty.right(144)` — 72° disegna un pentagono regolare; 144° disegna una stella.

## Esperimenti

1. **Disegna una stella a 6 punte.** Cambia `range(5)` in `range(6)` e `right(144)` in `right(120)`. Saprai che ha funzionato quando appare una forma a Stella di David.

2. **Fai un cielo notturno.** Aggiungi prima uno sfondo: disegna un grande rettangolo nero riempito prima di chiamare il ciclo delle stelle. Saprai che ha funzionato quando le stelle brillano contro uno sfondo scuro.

3. **Tutte della stessa dimensione.** Cambia `random.randint(20, 100)` in un valore fisso `60`. Saprai che ha funzionato quando tutte le stelle sono uniformi in dimensione ma ancora disperse casualmente.

4. **Stelle sovrapposte.** Rimuovi `random.seed(7)` e aumenta il conteggio a `range(30)`. Ogni esecuzione crea un campo stellare unico. Saprai che ha funzionato quando due esecuzioni non si assomigliano mai.

!!! mascot-celebration "Lavoro Stellare!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato il trucco della stella a 144°, scritto una funzione a quattro parametri, e usato `random`
    per disperdere forme attraverso il canvas. Stai pensando come un vero programmatore creativo!
    Prossimo: **Semaforo** — decomporre un oggetto del mondo reale in primitive di disegno.
