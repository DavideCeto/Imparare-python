---
hide:
    - toc
---
# Frattale a T-Square

Alla fine di questo laboratorio sarai in grado di:

- Disegnare un frattale dove ogni quadrato genera quattro quadrati di metà dimensione ai suoi angoli
- Capire perché quattro chiamate ricorsive creano un intricato intreccio sovrapposto
- Vedere come colori di riempimento alterni e profondità creano un effetto visivo stratificato

Un quadrato centrale fa germogliare quattro quadrati più piccoli ai suoi angoli, ognuno dei quali ne fa germogliare altri quattro — fino a 5 livelli di profondità. La geometria sovrapposta crea un intreccio tassellato sorprendente di luce e ombra.

!!! mascot-welcome "Benvenuto al Frattale a T-Square!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il T-Square è diverso dai frattali ad albero — ogni ramo si divide in QUATTRO
    rami più piccoli! Il risultato riempie completamente il canvas con quadrati sovrapposti.
    Programmiamo insieme!

## Come Funziona

`tsquare(cx, cy, size, depth)` disegna un quadrato centrato su `(cx, cy)`. Se `depth > 0`, disegna ricorsivamente quattro quadrati di `size/2` ai quattro angoli.

Posizioni degli angoli:
- In alto a sinistra: `(cx - size/2, cy + size/2)`
- In alto a destra: `(cx + size/2, cy + size/2)`
- In basso a sinistra: `(cx - size/2, cy - size/2)`
- In basso a destra: `(cx + size/2, cy - size/2)`

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_square(cx, cy, size, color):
    half = size / 2
    monty.penup()
    monty.goto(cx - half, cy - half)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def tsquare(cx, cy, size, depth):
    colors = ['navy', 'royalblue', 'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    draw_square(cx, cy, size, color)
    if depth > 0:
        half = size / 2
        for dx, dy in [(-half, half), (half, half), (-half, -half), (half, -half)]:
            tsquare(cx + dx, cy + dy, half, depth - 1)

tsquare(0, 0, 280, 5)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A ogni livello, appaiono 4 nuovi quadrati. Dopo 5 livelli, quanti quadrati totali
    saranno stati disegnati? (Suggerimento: 1 + 4 + 16 + 64 + 256 + 1024 = ?)
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

def draw_square(cx, cy, size, color):
    half = size / 2
    monty.penup()
    monty.goto(cx - half, cy - half)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def tsquare(cx, cy, size, depth):
    colors = ['navy', 'royalblue', 'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    draw_square(cx, cy, size, color)
    if depth > 0:
        half = size / 2
        for dx, dy in [(-half, half), (half, half), (-half, -half), (half, -half)]:
            tsquare(cx + dx, cy + dy, half, depth - 1)

tsquare(0, 0, 280, 5)`);
</script>

`1 + 4 + 16 + 64 + 256 + 1024 = 1365` quadrati totali disegnati. Avevi indovinato?

## Come Funziona

I quadrati successivi (più profondi) si disegnano sopra quelli precedenti. Poiché i quadrati più profondi sono del colore più chiaro (bianco), appaiono come luci brillanti sui quadrati di sfondo più scuri. Questo crea l'effetto di profondità stratificato.

Le quattro posizioni d'angolo `(±half, ±half)` sono calcolate con una list comprehension su `[(-half, half), (half, half), (-half, -half), (half, -half)]` — molto più chiaro di quattro chiamate separate.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `draw_square(cx, cy, size, color)` | Disegna un quadrato centrato |
| `half = size / 2` | I sotto-quadrati sono metà della dimensione del genitore |
| `for dx, dy in [...]` | Cicla sui quattro offset d'angolo |
| `tsquare(cx + dx, cy + dy, half, depth - 1)` | Ricorre a ogni angolo |
| Lista di colori | Più profondo = più chiaro — crea l'aspetto visivo stratificato |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova la Profondità 3"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `depth=5` in `depth=3`. Quanti quadrati totali verranno disegnati?
    (1 + 4 + 16 + 64 = ?). Prevedi, poi esegui per vedere la struttura più semplice.

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

def draw_square(cx, cy, size, color):
    half = size / 2
    monty.penup()
    monty.goto(cx - half, cy - half)
    monty.setheading(0)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
    monty.end_fill()

def tsquare(cx, cy, size, depth):
    colors = ['navy', 'royalblue', 'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
    color = colors[min(depth, len(colors) - 1)]
    draw_square(cx, cy, size, color)
    if depth > 0:
        half = size / 2
        for dx, dy in [(-half, half), (half, half), (-half, -half), (half, -half)]:
            tsquare(cx + dx, cy + dy, half, depth - 1)

tsquare(0, 0, 280, 3)`);
</script>

`1 + 4 + 16 + 64 = 85` quadrati — molto più rapido da disegnare e mostra chiaramente la struttura angolare gerarchica.

## Esperimenti

1. **Usa colori caldi.** Cambia la lista `colors` in `['darkred', 'red', 'orange', 'gold', 'yellow', 'white']`. Saprai che ha funzionato quando il frattale diventa caldo.

2. **Usa un quadrato di partenza di dimensione diversa.** Cambia `tsquare(0, 0, 280, 5)` in `tsquare(0, 0, 240, 6)`. Più profondità ma più piccolo. Saprai che ha funzionato quando il frattale è più denso.

3. **Prova divisioni a 3 vie.** Ricorri solo su 3 angoli invece di 4 (rimuovine uno dalla lista). Saprai che ha funzionato quando il pattern diventa asimmetrico.

4. **Solo contorno.** Rimuovi `begin_fill()` ed `end_fill()`. Saprai che ha funzionato quando sono disegnati solo i bordi dei quadrati.

!!! mascot-celebration "Quattro Angoli d'Infinito!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scoperto come quattro chiamate ricorsive — una per angolo — creano un pattern
    che tassella completamente il piano. Questo è il potere della ricorsione a 4 vie!
    Prossimo: **Curva C di Lévy** — un frattale che costruisce l'ala di un dragone.
