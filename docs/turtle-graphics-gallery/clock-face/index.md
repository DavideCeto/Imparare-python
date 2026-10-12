---
hide:
    - toc
---
# Quadrante dell'Orologio

Alla fine di questo laboratorio sarai in grado di:

- Disegnare un quadrante di orologio con tacche e numeri delle ore
- Convertire ore, minuti, e secondi in angoli per le lancette dell'orologio
- Usare `setheading()` per puntare ogni lancetta all'angolo corretto

Un quadrante di orologio analogico completo — anello esterno con 60 tacche, 12 ore numerate, e tre lancette (ore, minuti, secondi) disegnate ad angoli calcolati.

!!! mascot-welcome "Benvenuto al Quadrante dell'Orologio!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Un orologio analogico è un problema matematico: convertire il tempo in angoli!
    La lancetta dei minuti si muove di `6° per minuto`, la lancetta delle ore si muove di `0,5° per minuto`.
    Calcoliamolo e disegniamolo!

## Come Funziona

Angoli per le lancette: `second_angle = 90 - seconds * 6`, `minute_angle = 90 - minutes * 6 - seconds * 0.1`, `hour_angle = 90 - hours * 30 - minutes * 0.5`. Una funzione `draw_hand(angle, length, width)` disegna una lancetta all'angolo dato.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_tick(angle, length, width):
    monty.penup()
    r = 130
    rad = math.radians(angle)
    monty.goto(r * math.cos(rad), r * math.sin(rad))
    monty.setheading(angle + 180)
    monty.pendown()
    monty.pensize(width)
    monty.forward(length)

for i in range(60):
    angle = 90 - i * 6
    if i % 5 == 0:
        draw_tick(angle, 15, 3)
    else:
        draw_tick(angle, 8, 1)

monty.pencolor('black')
for h in range(1, 13):
    angle = 90 - h * 30
    rad = math.radians(angle)
    monty.penup()
    monty.goto(100 * math.cos(rad) - 8, 100 * math.sin(rad) - 8)
    monty.write(str(h), font=('Arial', 9, 'bold'))

def draw_hand(angle, length, color, width):
    rad = math.radians(angle)
    monty.penup()
    monty.goto(0, 0)
    monty.pendown()
    monty.pencolor(color)
    monty.pensize(width)
    monty.goto(length * math.cos(rad), length * math.sin(rad))

hours, minutes, seconds = 10, 10, 30
sec_angle = 90 - seconds * 6
min_angle = 90 - minutes * 6 - seconds * 0.1
hr_angle = 90 - hours * 30 - minutes * 0.5

draw_hand(hr_angle, 60, 'black', 4)
draw_hand(min_angle, 90, 'black', 3)
draw_hand(sec_angle, 110, 'red', 1)
monty.penup(); monty.goto(0, 0); monty.dot(8, 'black')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice imposta `hours=10, minutes=10, seconds=30`.
    Prima di eseguire, guarda un orologio analogico e immagina dove dovrebbero puntare le lancette.
    Fai la tua previsione — poi clicca Esegui!

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

def draw_tick(angle, length, width):
    monty.penup()
    r = 130
    rad = math.radians(angle)
    monty.goto(r * math.cos(rad), r * math.sin(rad))
    monty.setheading(angle + 180)
    monty.pendown()
    monty.pensize(width)
    monty.pencolor('black')
    monty.forward(length)

for i in range(60):
    angle = 90 - i * 6
    if i % 5 == 0:
        draw_tick(angle, 15, 3)
    else:
        draw_tick(angle, 8, 1)

for h in range(1, 13):
    angle = 90 - h * 30
    rad = math.radians(angle)
    monty.penup()
    monty.goto(100 * math.cos(rad) - 5, 100 * math.sin(rad) - 7)
    monty.pencolor('black')
    monty.write(str(h), font=('Arial', 9, 'bold'))

def draw_hand(angle, length, color, width):
    rad = math.radians(angle)
    monty.penup()
    monty.goto(0, 0)
    monty.pendown()
    monty.pencolor(color)
    monty.pensize(width)
    monty.goto(length * math.cos(rad), length * math.sin(rad))

hours, minutes, seconds = 10, 10, 30
sec_angle = 90 - seconds * 6
min_angle = 90 - minutes * 6 - seconds * 0.1
hr_angle = 90 - hours * 30 - minutes * 0.5

draw_hand(hr_angle, 60, 'black', 4)
draw_hand(min_angle, 90, 'black', 3)
draw_hand(sec_angle, 110, 'red', 1)
monty.penup(); monty.goto(0, 0); monty.dot(8, 'black')`);
</script>

Un orologio che mostra **10:10:30** — la lancetta delle ore tra 10 e 11 (già passata le 10), la lancetta dei minuti a 2 (10 minuti), la lancetta dei secondi a 3 (30 secondi). Avevi indovinato?

## Come Funziona

Angoli dell'orologio:
- Ogni **secondo** = 6° in senso orario = −6° nell'angolo turtle
- Ogni **minuto** = 6° in senso orario; il secondo muove anche leggermente la lancetta dei minuti (0,1° per secondo)
- Ogni **ora** = 30° in senso orario; il minuto muove anche la lancetta delle ore (0,5° per minuto)

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `sec_angle = 90 - seconds * 6` | 0s = ore 12 = 90°, ogni secondo = −6° |
| `min_angle = 90 - minutes*6 - seconds*0.1` | La lancetta dei minuti si muove fluidamente |
| `hr_angle = 90 - hours*30 - minutes*0.5` | La lancetta delle ore si muove tra le ore |
| `i % 5 == 0` | Ogni 5ª tacca è una tacca lunga dell'ora |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia l'Ora"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia in `hours=3, minutes=45, seconds=0`.
    Prima di eseguire, visualizza dove punterà ogni lancetta. Poi esegui per verificare!

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

def draw_tick(angle, length, width):
    monty.penup()
    r = 130
    rad = math.radians(angle)
    monty.goto(r * math.cos(rad), r * math.sin(rad))
    monty.setheading(angle + 180)
    monty.pendown()
    monty.pensize(width)
    monty.pencolor('navy')
    monty.forward(length)

for i in range(60):
    angle = 90 - i * 6
    if i % 5 == 0:
        draw_tick(angle, 15, 3)
    else:
        draw_tick(angle, 8, 1)

for h in range(1, 13):
    angle = 90 - h * 30
    rad = math.radians(angle)
    monty.penup()
    monty.goto(100 * math.cos(rad) - 5, 100 * math.sin(rad) - 7)
    monty.pencolor('navy')
    monty.write(str(h), font=('Arial', 9, 'bold'))

def draw_hand(angle, length, color, width):
    rad = math.radians(angle)
    monty.penup(); monty.goto(0, 0); monty.pendown()
    monty.pencolor(color); monty.pensize(width)
    monty.goto(length * math.cos(rad), length * math.sin(rad))

hours, minutes, seconds = 3, 45, 0
sec_angle = 90 - seconds * 6
min_angle = 90 - minutes * 6 - seconds * 0.1
hr_angle = 90 - hours * 30 - minutes * 0.5

draw_hand(hr_angle, 60, 'navy', 4)
draw_hand(min_angle, 90, 'navy', 3)
draw_hand(sec_angle, 110, 'red', 1)
monty.penup(); monty.goto(0, 0); monty.dot(8, 'navy')`);
</script>

Ore 3:45:00 — la lancetta dei minuti a 9, la lancetta delle ore a 3/4 del percorso tra 3 e 4 (perché 45 minuti = 3/4 del percorso verso l'ora successiva).

## Esperimenti

1. **Mostra l'ora attuale.** Usa il modulo `datetime` di Python: `import datetime; now = datetime.datetime.now()` poi `hours = now.hour % 12; minutes = now.minute; seconds = now.second`. Saprai che ha funzionato quando l'orologio mostra l'ora reale attuale.

2. **Aggiungi un quadrante colorato.** Disegna un cerchio riempito di un colore chiaro dietro le tacche. Saprai che ha funzionato quando l'orologio ha uno sfondo colorato.

3. **Rendi colorate le lancette.** Usa colori diversi per le lancette di ore, minuti, e secondi. Saprai che ha funzionato quando ogni lancetta è visivamente distinta.

4. **Aggiungi numeri romani.** Sostituisci le etichette numeriche con numeri romani. Saprai che ha funzionato quando `I`, `II`, `III`... appaiono attorno all'orologio.

!!! mascot-celebration "Tic Tac!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un quadrante di orologio analogico funzionante da zero usando la matematica degli angoli!
    La stessa formula `angle = 90 - n * step` funziona per qualsiasi display simile a un orologio.
    Prossimo: **Disegnatore di Spirografi** — spirografo interattivo con parametri cambianti.
