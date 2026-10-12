---
hide:
    - toc
---
# Pixel Art dell'Insieme di Julia

Alla fine di questo laboratorio sarai in grado di:

- Modificare l'iterazione di Mandelbrot per calcolare un insieme di Julia scambiando `z` e `c`
- Capire come cambiare una costante complessa `c` produce forme drammaticamente diverse
- Confrontare insiemi di Julia connessi contro disconnessi (polvere di Fatou)

L'insieme di Julia per `c = -0,7 + 0,27i` — una forma connessa e avvolgente a volte chiamata il "coniglio di Douady". Cambia `c` e l'intera forma si trasforma; alcuni valori danno spirali, altri danno polvere.

!!! mascot-welcome "Benvenuto all'Insieme di Julia!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nell'insieme di Mandelbrot, `c` cambia per ogni pixel e `z` inizia a 0.
    In un insieme di Julia, `c` è **fisso** e `z` inizia alla posizione di ogni pixel.
    Scambiare questi due ruoli dà un frattale completamente diverso!
    Programmiamo insieme!

## Come Funziona

Per ogni pixel `(px, py)`, imposta `z = (posizione complessa del pixel)` e `c = -0,7 + 0,27j` (fisso). Applica ripetutamente `z = z² + c`. Colora per tempo di fuga. L'insieme di punti che non fugge mai è l'insieme di Julia.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

cols = 60
rows = 50
pixel = 5
max_iter = 25
c = complex(-0.7, 0.27)

colors = ['black', 'darkblue', 'navy', 'blue', 'mediumblue',
          'royalblue', 'deepskyblue', 'cyan', 'limegreen',
          'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        zr = -1.5 + px * 3.0 / cols
        zi = -1.25 + py * 2.5 / rows
        z = complex(zr, zi)
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z * z + c
            count += 1
        color_idx = min(count, len(colors) - 1)
        monty.goto(-150 + px * pixel, -125 + py * pixel)
        monty.dot(pixel + 1, colors[color_idx])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    L'insieme di Julia per `c = -0,7 + 0,27i` è una macchia connessa con un confine avvolgente.
    Sembrerà più simile a Mandelbrot, o completamente diverso?
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
monty.penup()

cols = 60
rows = 50
pixel = 5
max_iter = 25
c = complex(-0.7, 0.27)

colors = ['black', 'darkblue', 'navy', 'blue', 'mediumblue',
          'royalblue', 'deepskyblue', 'cyan', 'limegreen',
          'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        zr = -1.5 + px * 3.0 / cols
        zi = -1.25 + py * 2.5 / rows
        z = complex(zr, zi)
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z * z + c
            count += 1
        color_idx = min(count, len(colors) - 1)
        monty.goto(-150 + px * pixel, -125 + py * pixel)
        monty.dot(pixel + 1, colors[color_idx])`);
</script>

L'insieme di Julia sembra molto **diverso** da Mandelbrot — è una forma simmetrica, avvolgente, e connessa. Avevi indovinato?

## Come Funziona

La differenza chiave da Mandelbrot:
- **Mandelbrot**: `z = 0`, `c = posizione_pixel` — testa ogni punto come parametro
- **Julia**: `z = posizione_pixel`, `c = fisso` — testa ogni punto come valore iniziale

L'insieme di Julia è connesso se e solo se `c` è dentro l'insieme di Mandelbrot.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `c = complex(-0.7, 0.27)` | Parametro fisso — determina la forma di Julia |
| `z = complex(zr, zi)` | Valore iniziale = posizione attuale del pixel |
| `z = z * z + c` | Stessa iterazione di Mandelbrot — ma `c` non cambia mai |
| `zr = -1.5 + px * 3.0 / cols` | Mappa il pixel alla coordinata x del piano z complesso |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova un Valore c Diverso"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `c = complex(-0.7, 0.27)` in `c = complex(0.285, 0.01)`.
    Ogni valore di `c` crea un insieme di Julia completamente diverso. Prevedi se sembrerà
    simile o molto diverso — poi eseguilo per esplorare!

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
monty.penup()

cols = 60
rows = 50
pixel = 5
max_iter = 25
c = complex(0.285, 0.01)

colors = ['black', 'darkblue', 'navy', 'blue', 'mediumblue',
          'royalblue', 'deepskyblue', 'cyan', 'limegreen',
          'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        zr = -1.5 + px * 3.0 / cols
        zi = -1.25 + py * 2.5 / rows
        z = complex(zr, zi)
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z * z + c
            count += 1
        color_idx = min(count, len(colors) - 1)
        monty.goto(-150 + px * pixel, -125 + py * pixel)
        monty.dot(pixel + 1, colors[color_idx])`);
</script>

`c = 0,285 + 0,01i` è molto vicino al bordo dell'insieme di Mandelbrot — l'insieme di Julia risultante ha un confine piumato e a spirale.

## Esperimenti

1. **Prova `c = complex(-0.4, 0.6)`.** Questo crea una forma "a dragone". Saprai che ha funzionato quando vedi una forma frastagliata e asimmetrica.

2. **Prova `c = complex(0.0, 1.0)`.** Questo è fuori dall'insieme di Mandelbrot — l'insieme di Julia diventa "polvere di Fatou" (punti dispersi disconnessi). Saprai che ha funzionato quando la maggior parte dei pixel è colorata, non nera.

3. **max_iter più alto.** Cambia `max_iter = 50`. Più iterazioni rivelano un dettaglio del confine più fine. Saprai che ha funzionato quando la transizione tra i colori è più fluida.

4. **Allarga la vista.** Cambia `zr = -2.0 + px * 4.0 / cols` e `zi = -1.67 + py * 3.33 / rows`. Saprai che ha funzionato quando l'intero insieme di Julia entra nella cornice.

!!! mascot-celebration "Due Frattali, Una Regola!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Gli insiemi di Mandelbrot e Julia usano *esattamente la stessa iterazione* — solo con z e c scambiati!
    Quel piccolo cambiamento ti dà una famiglia infinita di frattali diversi da un'unica formula.
    Prossimo: **Tappeto di Sierpiński** — suddivisione ricorsiva a 8 vie.
