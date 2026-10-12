---
hide:
    - toc
---
# Nome in Lettere Blocco

Alla fine di questo laboratorio sarai in grado di:

- Memorizzare forme di lettere come liste di punti di passaggio di tratto e disegnarle con `goto()`
- Costruire un mini font e renderizzare qualsiasi parola usando le tue definizioni di lettera
- Capire come funzionano i font vettoriali — forme definite come percorsi di coordinate

Ogni lettera di un nome è disegnata come una serie di "tratti" di linea — liste di punti di passaggio `(x, y)`. Muovere la penna lungo i tratti disegna il contorno della lettera. Così funzionavano i primi font dei computer.

!!! mascot-welcome "Benvenuto alle Lettere Blocco!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Prima che esistessero i font TrueType, i computer disegnavano le lettere così — come liste memorizzate di segmenti di linea.
    Questo laboratorio costruisce un mini font basato su tratti da zero!
    Programmiamo insieme!

## Come Funziona

Ogni lettera è definita come una lista di tratti; ogni tratto è una lista di punti di passaggio `(x, y)` in un riquadro di coordinate 0–1. Una funzione `draw_letter(ch, ox, oy, scale)` scala e trasla i punti di passaggio e disegna ogni tratto.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

font = {
    'P': [[(0,0),(0,1),(0.6,1),(0.6,0.6),(0,0.6)], [(0,0.5),(0,0)]],
    'Y': [[(0,1),(0.5,0.5),(1,1)], [(0.5,0.5),(0.5,0)]],
    'T': [[(0,1),(1,1)], [(0.5,1),(0.5,0)]],
    'H': [[(0,0),(0,1)], [(1,0),(1,1)], [(0,0.5),(1,0.5)]],
    'O': [[(0,0),(1,0),(1,1),(0,1),(0,0)]],
    'N': [[(0,0),(0,1),(1,0),(1,1)]],
}

def draw_letter(ch, ox, oy, scale):
    strokes = font.get(ch.upper(), [])
    for stroke in strokes:
        monty.penup()
        monty.goto(ox + stroke[0][0]*scale, oy + stroke[0][1]*scale)
        monty.pendown()
        for x, y in stroke[1:]:
            monty.goto(ox + x*scale, oy + y*scale)

word = "PYTHON"
scale = 50
gap = 12
total = len(word) * (scale + gap)
ox = -total / 2

monty.pencolor('royalblue')
monty.pensize(3)
for i, ch in enumerate(word):
    draw_letter(ch, ox + i * (scale + gap), -scale/2, scale)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il dizionario del font ha 6 lettere — ognuna definita come una lista di percorsi di tratto.
    La parola "PYTHON" sembrerà lettere blocco leggibili, o linee confuse?
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

font = {
    'P': [[(0,0),(0,1),(0.6,1),(0.6,0.6),(0,0.6)]],
    'Y': [[(0,1),(0.5,0.5),(1,1)], [(0.5,0.5),(0.5,0)]],
    'T': [[(0,1),(1,1)], [(0.5,1),(0.5,0)]],
    'H': [[(0,0),(0,1)], [(1,0),(1,1)], [(0,0.5),(1,0.5)]],
    'O': [[(0,0),(1,0),(1,1),(0,1),(0,0)]],
    'N': [[(0,0),(0,1),(1,0),(1,1)]],
}

def draw_letter(ch, ox, oy, scale):
    strokes = font.get(ch.upper(), [])
    for stroke in strokes:
        monty.penup()
        monty.goto(ox + stroke[0][0]*scale, oy + stroke[0][1]*scale)
        monty.pendown()
        for x, y in stroke[1:]:
            monty.goto(ox + x*scale, oy + y*scale)

word = "PYTHON"
scale = 50
gap = 12
total = len(word) * (scale + gap)
ox = -total / 2

monty.pencolor('royalblue')
monty.pensize(3)
for i, ch in enumerate(word):
    draw_letter(ch, ox + i * (scale + gap), -scale/2, scale)`);
</script>

**Lettere blocco leggibili** — ogni lettera disegnata dai suoi tratti di punti di passaggio. Avevi indovinato?

## Come Funziona

Il font memorizza ogni lettera come "tratti" (liste di punti di passaggio in coordinate unitarie 0–1). `draw_letter()` li scala di `scale` e li sposta di `ox, oy`. Questo è esattamente come funzionano i font PostScript e SVG — solo con più punti di passaggio per lettera.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `font = {'P': [[...], ...], ...}` | Dizionario: lettera → lista di tratti |
| `font.get(ch.upper(), [])` | Cerca i tratti, predefinito vuoto |
| `ox + stroke[0][0]*scale` | Scala x dall'intervallo 0–1 all'intervallo in pixel |
| `gap = 12` | Spaziatura tra le lettere |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Nuova Lettera"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi una voce `'A'` al dizionario `font`.
    `'A'` ha due linee inclinate e una traversa.
    Aggiungila e cambia la parola per includere `'A'` — riesci a definire correttamente i tratti?

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

font = {
    'A': [[(0,0),(0.5,1),(1,0)], [(0.2,0.4),(0.8,0.4)]],
    'P': [[(0,0),(0,1),(0.6,1),(0.6,0.6),(0,0.6)]],
    'Y': [[(0,1),(0.5,0.5),(1,1)], [(0.5,0.5),(0.5,0)]],
    'T': [[(0,1),(1,1)], [(0.5,1),(0.5,0)]],
    'H': [[(0,0),(0,1)], [(1,0),(1,1)], [(0,0.5),(1,0.5)]],
    'O': [[(0,0),(1,0),(1,1),(0,1),(0,0)]],
    'N': [[(0,0),(0,1),(1,0),(1,1)]],
}

def draw_letter(ch, ox, oy, scale):
    strokes = font.get(ch.upper(), [])
    for stroke in strokes:
        monty.penup()
        monty.goto(ox + stroke[0][0]*scale, oy + stroke[0][1]*scale)
        monty.pendown()
        for x, y in stroke[1:]:
            monty.goto(ox + x*scale, oy + y*scale)

word = "PATH"
scale = 60
gap = 14
total = len(word) * (scale + gap)
ox = -total / 2

monty.pencolor('darkred')
monty.pensize(4)
for i, ch in enumerate(word):
    draw_letter(ch, ox + i * (scale + gap), -scale/2, scale)`);
</script>

La `'A'` è definita con due tratti inclinati e una traversa — stile lettera blocco leggibile!

## Esperimenti

1. **Aggiungi più lettere.** Definisci `'E'`, `'I'`, `'L'`, `'F'`, `'Z'` usando linee orizzontali e verticali. Saprai che ha funzionato quando puoi scrivere nuove parole.

2. **Aggiungi il riempimento.** Per lettere chiuse come `'O'`, chiama `begin_fill()` e `end_fill()` attorno a ogni tratto chiuso. Saprai che ha funzionato quando l'interno della lettera è riempito.

3. **Fai lettere arcobaleno.** Assegna un colore diverso a ogni lettera. Saprai che ha funzionato quando ogni lettera della parola è di un colore diverso.

4. **Scala in base alla posizione del carattere.** Rendi le prime lettere piccole e quelle successive più grandi variando `scale`. Saprai che ha funzionato quando la parola sembra crescere di dimensione da sinistra a destra.

!!! mascot-celebration "Hai Costruito un Font!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai memorizzato forme di lettere come dati e le hai renderizzate con `goto()` — lo stesso
    principio usato dai font PostScript e dal rendering del testo SVG.
    Prossimo: **Categoria 10 — Pattern di Animazione!**
