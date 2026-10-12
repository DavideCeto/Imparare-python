---
hide:
    - toc
---
# Triangolo di Sierpiński

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione ricorsiva che disegna un triangolo e lo suddivide in tre triangoli più piccoli
- Capire perché i "buchi" in un triangolo di Sierpiński non vengono mai riempiti — sono lo spazio centrale della ricorsione
- Vedere come la profondità controlla quanti livelli di buchi auto-simili appaiono

Un triangolo fatto interamente di triangoli — ognuno contenente triangoli più piccoli, ognuno contenente altri ancora più piccoli. Il centro di ogni triangolo resta vuoto, creando un reticolo frattale di buchi infiniti.

!!! mascot-welcome "Benvenuto al Triangolo di Sierpiński!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il Triangolo di Sierpiński è una delle forme più famose in tutta la matematica.
    Sembra complicato ma emerge da una regola ricorsiva meravigliosamente semplice.
    Programmiamo insieme!

## Come Funziona

`sierpinski(x, y, size, depth)` disegna un triangolo equilatero riempito a `(x, y)`.
Se `depth > 0`, disegna ricorsivamente tre triangoli di metà dimensione ai tre angoli del triangolo attuale. Lo spazio centrale non viene mai disegnato — resta naturalmente vuoto.

Tre posizioni d'angolo:
- In basso a sinistra: `(x, y)`
- In basso a destra: `(x + size, y)`
- In alto: `(x + size/2, y + size * sqrt(3)/2)`

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def triangle(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()

def sierpinski(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue',
              'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    triangle(x, y, size, color)
    if depth > 0:
        half = size / 2
        h = half * math.sqrt(3) / 2
        sierpinski(x, y, half, depth - 1)
        sierpinski(x + half, y, half, depth - 1)
        sierpinski(x + half / 2, y + h * 2, half, depth - 1)

monty.penup()
monty.goto(-160, -140)
monty.pendown()
sierpinski(-160, -140, 320, 5)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Alla profondità 5, quanti piccoli triangoli verranno disegnati?
    (Suggerimento: alla profondità 0 è 1, alla profondità 1 è 3, alla profondità 2 è 9 …)
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

def triangle(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()

def sierpinski(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue',
              'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    triangle(x, y, size, color)
    if depth > 0:
        half = size / 2
        h = half * math.sqrt(3) / 2
        sierpinski(x, y, half, depth - 1)
        sierpinski(x + half, y, half, depth - 1)
        sierpinski(x + half / 2, y + h * 2, half, depth - 1)

sierpinski(-160, -140, 320, 5)`);
</script>

Alla profondità 5, vengono disegnati `3^5 = 243` triangoli solidi. Avevi indovinato?

## Come Funziona

La funzione disegna prima il triangolo esterno completo (nel colore della profondità attuale), poi disegna ricorsivamente tre triangoli più piccoli agli angoli. Ogni nuova chiamata sovrascrive gli angoli — lo spazio centrale non viene mai coperto perché non c'è una quarta chiamata ricorsiva per il centro.

Profondità diverse ottengono colori diversi — blu più scuri per triangoli più profondi (più piccoli) — creando un gradiente di colore visibile dall'esterno all'interno.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors[min(depth, len(colors)-1)]` | Mappa la profondità a un colore — più profondo = più chiaro |
| `if depth > 0:` | Controllo del caso base — ferma alla profondità 0 |
| `half = size / 2` | I sotto-triangoli sono metà della dimensione del genitore |
| Tre chiamate `sierpinski()` | Ricorre sugli angoli in basso a sinistra, in basso a destra, in alto |
| Nessuna chiamata per il centro | Lo spazio centrale resta vuoto — questo è il buco frattale |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Riduci alla Profondità 3"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `depth=5` in `depth=3`. Quanti triangoli verranno disegnati? (3^3 = ?)
    Fai la tua previsione, poi eseguila per contare i buchi visibili.

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

def triangle(x, y, size, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()

def sierpinski(x, y, size, depth):
    colors = ['royalblue', 'cornflowerblue', 'deepskyblue',
              'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    triangle(x, y, size, color)
    if depth > 0:
        half = size / 2
        h = half * math.sqrt(3) / 2
        sierpinski(x, y, half, depth - 1)
        sierpinski(x + half, y, half, depth - 1)
        sierpinski(x + half / 2, y + h * 2, half, depth - 1)

sierpinski(-160, -140, 320, 3)`);
</script>

Alla profondità 3: `3^3 = 27` triangoli e `(3^3 - 1)/2 = 13` buchi visibili. La struttura è già chiaramente auto-simile.

## Esperimenti

1. **Usa colori caldi.** Cambia `colors` in `['darkred', 'red', 'orange', 'gold', 'yellow', 'white']`. Saprai che ha funzionato quando il triangolo passa a tonalità calde.

2. **Prova una profondità molto profonda.** Cambia in `depth=7`. Sarà lento ma estremamente dettagliato. Saprai che ha funzionato quando i triangoli interni sono della dimensione di un pixel.

3. **Rimuovi il riempimento.** Invece di `begin_fill()`/`end_fill()`, disegna solo il contorno. Saprai che ha funzionato quando vedi solo i bordi di ogni triangolo.

4. **Inverti: disegna gli spazi vuoti.** Disegna solo i triangoli dove `depth == 0`, usando riempimento bianco ovunque altro come sfondo. Saprai che ha funzionato quando il pattern sembra la classica versione "a buchi".

!!! mascot-celebration "Maestria Ricorsiva!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un frattale con buchi infiniti da una regola ricorsiva di tre righe!
    Nota come appaiono `3^depth` triangoli — il potere della ricorsione esponenziale.
    Prossimo: **Albero Frattale** — ricorsione ramificata che sembra proprio un vero albero.
