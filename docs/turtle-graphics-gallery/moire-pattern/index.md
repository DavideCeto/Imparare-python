---
hide:
    - toc
---
# Motivo Moiré

Alla fine di questo laboratorio sarai in grado di:

- Disegnare due insiemi sovrapposti di linee ad angoli leggermente diversi
- Capire come l'interferenza tra due griglie crea pattern Moiré
- Controllare la dimensione del pattern Moiré cambiando la differenza di angolo

Quando due insiemi di linee quasi parallele si sovrappongono a un leggero angolo, producono drammatici pattern di interferenza — onde di "battimento" a grande scala che sembrano pulsare attraverso il canvas. Questo è l'effetto Moiré.

!!! mascot-welcome "Benvenuto ai Motivi Moiré!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I motivi Moiré appaiono sugli schermi TV quando qualcuno indossa una camicia a quadri —
    la griglia di pixel dello schermo interferisce con il pattern del tessuto!
    Programmiamone uno noi stessi!

## Come Funziona

Disegna due insiemi di linee parallele uniformemente spaziate. Un insieme è orizzontale; il secondo è ruotato di un piccolo angolo (3°). Dove le linee dei due insiemi si incrociano, si rafforzano; dove divergono, si formano spazi vuoti. Il risultato è un pattern d'onda a grande scala.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

spacing = 8
n_lines = 40
length = 320

def draw_lines(angle_deg):
    monty.setheading(angle_deg + 90)
    perpendicular = math.radians(angle_deg)
    for i in range(-n_lines, n_lines):
        d = i * spacing
        cx = d * math.cos(perpendicular)
        cy = d * math.sin(perpendicular)
        start_angle = math.radians(angle_deg)
        monty.penup()
        monty.goto(cx - length/2 * math.cos(start_angle),
                   cy - length/2 * math.sin(start_angle))
        monty.pendown()
        monty.goto(cx + length/2 * math.cos(start_angle),
                   cy + length/2 * math.sin(start_angle))

monty.pencolor('navy')
monty.pensize(1)
draw_lines(0)

monty.pencolor('royalblue')
monty.pensize(1)
draw_lines(3)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Due insiemi di linee, uno ruotato di solo 3° dall'altro.
    La leggera differenza di angolo sarà visibile come linee separate, o come un pattern di battimento?
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

spacing = 8
n_lines = 40
length = 320

def draw_lines(angle_deg):
    perpendicular = math.radians(angle_deg + 90)
    line_dir = math.radians(angle_deg)
    for i in range(-n_lines, n_lines):
        d = i * spacing
        cx = d * math.cos(perpendicular)
        cy = d * math.sin(perpendicular)
        monty.penup()
        monty.goto(cx - length/2 * math.cos(line_dir),
                   cy - length/2 * math.sin(line_dir))
        monty.pendown()
        monty.goto(cx + length/2 * math.cos(line_dir),
                   cy + length/2 * math.sin(line_dir))

monty.pencolor('navy')
monty.pensize(1)
draw_lines(0)

monty.pencolor('royalblue')
monty.pensize(1)
draw_lines(3)`);
</script>

Appare un **pattern di battimento a grande scala** — fasce di linee dense e sparse che si alternano attraverso il canvas. Avevi indovinato?

## Come Funziona

Il periodo Moiré (la distanza tra i "battimenti") è approssimativamente `spacing / sin(angle_difference)`. Con `spacing=8` e `angle=3°`, il periodo di battimento ≈ `8 / sin(3°) ≈ 153 pixel`. Ecco perché vedi circa 2 frange complete attraverso il canvas.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `spacing = 8` | Distanza tra le linee parallele |
| `draw_lines(0)` | Primo insieme — linee orizzontali |
| `draw_lines(3)` | Secondo insieme — rotazione di 3° |
| `math.cos(perpendicular)` | Posizione della linea perpendicolare alla sua direzione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia l'Angolo"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `draw_lines(3)` in `draw_lines(10)`.
    Un angolo più grande significa un periodo Moiré più piccolo — più battimenti per schermo.
    Prevedi: quante fasce appariranno a 10°?

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

spacing = 8
n_lines = 40
length = 320

def draw_lines(angle_deg):
    perpendicular = math.radians(angle_deg + 90)
    line_dir = math.radians(angle_deg)
    for i in range(-n_lines, n_lines):
        d = i * spacing
        cx = d * math.cos(perpendicular)
        cy = d * math.sin(perpendicular)
        monty.penup()
        monty.goto(cx - length/2 * math.cos(line_dir),
                   cy - length/2 * math.sin(line_dir))
        monty.pendown()
        monty.goto(cx + length/2 * math.cos(line_dir),
                   cy + length/2 * math.sin(line_dir))

monty.pencolor('darkred')
monty.pensize(1)
draw_lines(0)

monty.pencolor('darkorange')
monty.pensize(1)
draw_lines(10)`);
</script>

A 10°, le fasce sono più strette e più numerose — il periodo Moiré si restringe mentre l'angolo cresce.

## Esperimenti

1. **Usa cerchi concentrici.** Sostituisci gli insiemi di linee con due insiemi di cerchi concentrici con spaziature di raggio leggermente diverse. Saprai che ha funzionato quando appaiono anelli Moiré.

2. **Prova una differenza di 1°.** Usa `draw_lines(0)` e `draw_lines(1)`. Saprai che ha funzionato quando appaiono solo 1–2 fasce molto larghe (periodo grande).

3. **Aggiungi un terzo insieme.** Aggiungi `draw_lines(6)`. Saprai che ha funzionato quando appare un pattern di interferenza più complesso.

4. **Usa griglie di punti invece di linee.** Disegna punti su una griglia regolare, poi disegna una seconda griglia ruotata di 3°. Saprai che ha funzionato quando appare un pattern Moiré esagonale.

!!! mascot-celebration "Pattern di Interferenza!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai creato un motivo Moiré — la stessa fisica descrive l'interferenza della luce,
    i battimenti del suono, e il mixing delle onde radio. Geometria, ottica, e fisica in un'unica immagine!
    Prossimo: **Onde di Bridget Riley** — curve parallele ondulate.
