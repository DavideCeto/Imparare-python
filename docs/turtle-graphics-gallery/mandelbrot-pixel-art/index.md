---
hide:
    - toc
---
# Pixel Art di Mandelbrot

Alla fine di questo laboratorio sarai in grado di:

- Usare l'aritmetica dei numeri complessi in Python per verificare l'appartenenza a Mandelbrot
- Disegnare un'immagine raster posizionando punti colorati su una griglia usando `dot()`
- Capire cosa significa "tempo di fuga" e come produce gradienti di colore

Una versione pixel art a bassa risoluzione dell'insieme di Mandelbrot — uno degli oggetti matematici più famosi mai scoperti. Il colore di ogni pixel ti dice quanto velocemente l'iterazione di Mandelbrot "fugge" all'infinito, o (nero) se rimane limitata per sempre.

!!! mascot-welcome "Benvenuto all'Insieme di Mandelbrot!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    L'insieme di Mandelbrot sembra infinitamente complesso ma è calcolato da una singola regola:
    `z = z² + c`. Applicala ripetutamente e chiedi: `z` fugge o resta vicino a zero?
    Programmiamo insieme!

## Come Funziona

Per ogni pixel `(px, py)` in una griglia, calcoliamo un numero complesso `c` nell'intervallo `[-2.5, 1] × [-1.25, 1.25]`. Poi applichiamo ripetutamente `z = z² + c` iniziando da `z = 0`. Se `|z| > 2`, il punto è "fuggito" — lo coloriamo in base a quanti passi ci sono voluti. Se non fugge mai dopo `max_iter` passi, è nell'insieme di Mandelbrot e colorato di nero.

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
max_iter = 20

colors = ['black', 'navy', 'blue', 'royalblue', 'deepskyblue',
          'cyan', 'green', 'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        cr = -2.5 + px * 3.5 / cols
        ci = -1.25 + py * 2.5 / rows
        z = complex(0, 0)
        c = complex(cr, ci)
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
    L'insieme di Mandelbrot è la regione **nera** — punti che non fuggono mai.
    Sembrerà una macchia irregolare, o una forma riconoscibile?
    Fai la tua previsione — poi clicca Esegui per scoprirlo! (Questo è lento — sii paziente!)

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
max_iter = 20

colors = ['black', 'navy', 'blue', 'royalblue', 'deepskyblue',
          'cyan', 'green', 'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        cr = -2.5 + px * 3.5 / cols
        ci = -1.25 + py * 2.5 / rows
        z = complex(0, 0)
        c = complex(cr, ci)
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z * z + c
            count += 1
        color_idx = min(count, len(colors) - 1)
        monty.goto(-150 + px * pixel, -125 + py * pixel)
        monty.dot(pixel + 1, colors[color_idx])`);
</script>

Anche a bassa risoluzione, il **cardioide** (a forma di cuore) corpo principale e il rigonfiamento rotondo alla sua sinistra sono riconoscibili. Avevi indovinato?

## Come Funziona

`complex(cr, ci)` crea un numero complesso `c = cr + ci·i`. L'iterazione chiave `z = z * z + c` calcola `z²` usando la moltiplicazione complessa integrata di Python — nessuna trigonometria necessaria! `abs(z)` dà `√(real² + imag²)`, la distanza dall'origine.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `cr = -2.5 + px * 3.5 / cols` | Mappa la colonna del pixel alla posizione sull'asse reale |
| `ci = -1.25 + py * 2.5 / rows` | Mappa la riga del pixel alla posizione sull'asse immaginario |
| `z = z * z + c` | L'iterazione di Mandelbrot |
| `while abs(z) <= 2` | Si ferma quando z fugge dal raggio 2 |
| `count` | Numero di iterazioni = tempo di fuga = colore |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Zoom nel Rigonfiamento"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia l'intervallo per fare zoom: `cr = -1.5 + px * 0.5 / cols` e `ci = -0.5 + py * 1.0 / rows`.
    Prevedi come sembrerà la regione con lo zoom — poi eseguilo per esplorare!

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
max_iter = 30

colors = ['black', 'navy', 'blue', 'royalblue', 'deepskyblue',
          'cyan', 'limegreen', 'yellow', 'orange', 'red', 'white']

for py in range(rows):
    for px in range(cols):
        cr = -1.5 + px * 0.5 / cols
        ci = -0.5 + py * 1.0 / rows
        z = complex(0, 0)
        c = complex(cr, ci)
        count = 0
        while abs(z) <= 2 and count < max_iter:
            z = z * z + c
            count += 1
        color_idx = min(count, len(colors) - 1)
        monty.goto(-150 + px * pixel, -125 + py * pixel)
        monty.dot(pixel + 1, colors[color_idx])`);
</script>

Fare zoom rivela più dettagli nella regione di confine — appaiono piccoli rigonfiamenti che sembrano proprio come la forma principale. Questa auto-similarità a ogni livello di zoom è la proprietà distintiva di un frattale!

## Esperimenti

1. **Aumenta la risoluzione.** Cambia `cols = 80` e `rows = 66` con `pixel = 4`. Più dettaglio, più lento. Saprai che ha funzionato quando il corpo principale ha bordi più netti.

2. **Più colori.** Estendi la lista `colors` a 20 voci con un arcobaleno completo. Saprai che ha funzionato quando la regione di confine mostra più fasce di colore.

3. **Aumenta max_iter.** Cambia `max_iter = 50`. I punti vicino al confine hanno bisogno di più iterazioni per fuggire. Saprai che ha funzionato quando il dettaglio del confine migliora.

4. **Prova uno zoom diverso.** Usa `cr = -0.75 + px * 0.02 / cols` e `ci = -0.1 + py * 0.02 / rows` per fare zoom nella "valle dei cavallucci marini". Saprai che ha funzionato quando vedi una forma di Mandelbrot in miniatura.

!!! mascot-celebration "La Matematica Incontra l'Arte!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai calcolato uno degli oggetti matematici più famosi della storia usando
    `z = z*z + c` — solo una riga di codice! L'insieme di Mandelbrot è infinitamente complesso
    eppure emerge dall'iterazione più semplice possibile.
    Prossimo: **Pixel Art dell'Insieme di Julia** — il cugino di Mandelbrot.
