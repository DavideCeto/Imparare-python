---
hide:
    - toc
---
# Fetta di Caleidoscopio

Alla fine di questo laboratorio sarai in grado di:

- Costruire un pattern completo ripetendo una "fetta" a diversi angoli di rotazione
- Rispecchiare le copie alterne invertendo l'angolo dentro ogni fetta
- Convertire un raggio e un angolo in `(x, y)` con `cos` e `sin`

Un vero caleidoscopio usa specchi per far rimbalzare un piccolo cuneo di vetro colorato in un cerchio completo di simmetria. Questo programma fa la stessa cosa con la matematica: disegna una fetta di 30° fatta di quattro forme riempite, poi la ripete 12 volte attorno al centro — rispecchiando ogni altra copia così i bordi si allineano come una riflessione.

!!! mascot-welcome "Benvenuto al Caleidoscopio!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ecco un segreto: progettiamo SOLO UNA piccola fetta di questo pattern.
    La rotazione e la riflessione fanno tutto il resto del lavoro.
    Questo è il trucco magico dietro ogni caleidoscopio!

## Come Funziona

Ogni forma nella fetta è memorizzata come una lista di coppie `(raggio, angolo)` misurate dal centro. Per disegnare la fetta alla rotazione `base`, aggiungiamo `base` a ogni angolo, poi convertiamo in coordinate dello schermo con `x = r * cos(a)` e `y = r * sin(a)`. Per le copie rispecchiate usiamo `base + wedge - off` invece di `base + off`, che ribalta la fetta come una riflessione in uno specchio.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

sections = 12
wedge = 360 / sections

shapes = [
    ['gold', [(30, 3), (95, 13), (65, 26)]],
    ['crimson', [(45, 6), (110, 2), (165, 7), (110, 18)]],
    ['royalblue', [(85, 24), (150, 15), (178, 27)]],
    ['darkorchid', [(120, 10), (185, 12), (150, 21)]],
]

def draw_slice(base, mirror):
    for color, points in shapes:
        corners = []
        for r, off in points:
            if mirror == 1:
                ang = base + off
            else:
                ang = base + wedge - off
            a = math.radians(ang)
            corners.append((r * math.cos(a), r * math.sin(a)))
        monty.penup()
        monty.color(color, color)
        monty.goto(corners[0])
        monty.pendown()
        monty.begin_fill()
        for corner in corners:
            monty.goto(corner)
        monty.goto(corners[0])
        monty.end_fill()

for i in range(sections):
    if i % 2 == 0:
        draw_slice(i * wedge, 1)
    else:
        draw_slice(i * wedge, -1)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo gira 12 volte, e ogni fetta contiene esattamente un triangolo dorato.
    Quanti triangoli dorati conterai nel pattern finito?
    Fai la tua previsione, poi clicca Esegui!

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

sections = 12
wedge = 360 / sections

shapes = [
    ['gold', [(30, 3), (95, 13), (65, 26)]],
    ['crimson', [(45, 6), (110, 2), (165, 7), (110, 18)]],
    ['royalblue', [(85, 24), (150, 15), (178, 27)]],
    ['darkorchid', [(120, 10), (185, 12), (150, 21)]],
]

def draw_slice(base, mirror):
    for color, points in shapes:
        corners = []
        for r, off in points:
            if mirror == 1:
                ang = base + off
            else:
                ang = base + wedge - off
            a = math.radians(ang)
            corners.append((r * math.cos(a), r * math.sin(a)))
        monty.penup()
        monty.color(color, color)
        monty.goto(corners[0])
        monty.pendown()
        monty.begin_fill()
        for corner in corners:
            monty.goto(corner)
        monty.goto(corners[0])
        monty.end_fill()

for i in range(sections):
    if i % 2 == 0:
        draw_slice(i * wedge, 1)
    else:
        draw_slice(i * wedge, -1)

monty.penup()
monty.goto(0, 0)
monty.dot(30, 'gold')
monty.dot(16, 'crimson')`);
</script>

**12 triangoli dorati** — uno per fetta, perché il ciclo chiama `draw_slice` dodici volte. Avevi indovinato?

## Come Funziona

Guarda attentamente dove due fette si incontrano: il pattern su un lato è un'immagine speculare dell'altro. Questo succede perché le fette con numero dispari usano `base + wedge - off`, che misura gli angoli all'indietro dal bordo lontano del cuneo. Senza quel ribaltamento otterresti una semplice rotazione (come una girandola); con esso ottieni la vera simmetria caleidoscopica, dove ogni confine tra le fette agisce come una linea speculare.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `wedge = 360 / sections` | Divide il cerchio in 12 cunei uguali di 30° |
| `ang = base + off` | Ruota un punto nella fetta numero `i` |
| `ang = base + wedge - off` | Stesso punto, ma ribaltato — una riflessione speculare |
| `corners.append((r * math.cos(a), r * math.sin(a)))` | Converte raggio + angolo in una posizione `(x, y)` |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Questo programma dovrebbe disegnare tutte le 12 fette, ma manca quasi
    tutto il caleidoscopio! Guarda attentamente le due chiamate a `draw_slice`
    dentro il ciclo. Riesci a individuare cosa non cambia mai — e a correggerlo?

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

sections = 12
wedge = 360 / sections

shapes = [
    ['gold', [(30, 3), (95, 13), (65, 26)]],
    ['crimson', [(45, 6), (110, 2), (165, 7), (110, 18)]],
    ['royalblue', [(85, 24), (150, 15), (178, 27)]],
    ['darkorchid', [(120, 10), (185, 12), (150, 21)]],
]

def draw_slice(base, mirror):
    for color, points in shapes:
        corners = []
        for r, off in points:
            if mirror == 1:
                ang = base + off
            else:
                ang = base + wedge - off
            a = math.radians(ang)
            corners.append((r * math.cos(a), r * math.sin(a)))
        monty.penup()
        monty.color(color, color)
        monty.goto(corners[0])
        monty.pendown()
        monty.begin_fill()
        for corner in corners:
            monty.goto(corner)
        monty.goto(corners[0])
        monty.end_fill()

for i in range(sections):
    if i % 2 == 0:
        draw_slice(wedge, 1)
    else:
        draw_slice(wedge, -1)

monty.penup()
monty.goto(0, 0)
monty.dot(30, 'gold')
monty.dot(16, 'crimson')`);
</script>

Il bug: entrambe le chiamate passano `wedge` come angolo base, così ogni fetta finisce nello stesso punto. Cambiale in `draw_slice(i * wedge, 1)` e `draw_slice(i * wedge, -1)` e il cerchio completo di 12 fette ritorna.

## Esperimenti

1. **Prova 8 sezioni.** Cambia `sections = 12` in `sections = 8`. Il cuneo cresce automaticamente a 45°. Saprai che ha funzionato quando il pattern ha 8 bracci con piccoli spazi tra loro.

2. **Ricolora il vetro.** Cambia `'crimson'` in `'limegreen'` e `'royalblue'` in `'deeppink'`. Saprai che ha funzionato quando i grandi dardi cambiano colore in tutte le 12 fette contemporaneamente.

3. **Riprogetta una forma.** Nella forma `'darkorchid'`, cambia il raggio `185` in `120`. Saprai che ha funzionato quando i punti viola si avvicinano al centro attorno a tutta la ruota.

4. **Rompi lo specchio.** Cambia `draw_slice(i * wedge, -1)` in `draw_slice(i * wedge, 1)` così ogni copia usa la stessa direzione. Saprai che ha funzionato quando il pattern smette di riflettersi e inizia a girare — diventa una girandola invece di un caleidoscopio.

!!! mascot-celebration "Una Fetta, Dodici Riflessioni!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai progettato un cuneo di 30° e hai lasciato che rotazione + riflessione costruissero il resto.
    È esattamente così che funziona la simmetria nei fiocchi di neve, nei mandala, e nei veri caleidoscopi.
    Prossimo: **Tassellatura a Girandola** — un triangolo che tassella il piano dividendosi infinitamente in cinque copie di se stesso.
