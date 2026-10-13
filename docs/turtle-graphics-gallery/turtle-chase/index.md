---
hide:
    - toc
---
# Caccia tra Tartarughe

Alla fine di questo laboratorio sarai in grado di:

- Eseguire due tartarughe contemporaneamente dentro un singolo ciclo di animazione
- Puntare una tartaruga verso un'altra usando `math.atan2(dy, dx)`
- Rilevare una "cattura" confrontando la distanza al quadrato tra le tartarughe

Una tartaruga preda verde vaga a caso per il canvas mentre una tartaruga cacciatrice rossa la insegue — ogni fotogramma il cacciatore ripunta dritto verso la preda e fa un passo leggermente più grande. La caccia finisce nel momento in cui il cacciatore arriva entro 10 pixel.

!!! mascot-welcome "Benvenuto alla Caccia tra Tartarughe!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Due tartarughe, un canvas: una vagabonda e una cacciatrice.
    Questo è il tuo primo programma dove due personaggi *interagiscono*!
    Programmiamolo insieme!

## Come Funziona

Ogni fotogramma fa tre cose. La preda gira di una quantità casuale (fino a ±30°) e fa un passo in avanti di 3.5 pixel — una passeggiata casuale. Il cacciatore calcola il vettore verso la preda (`dx`, `dy`), lo converte in una direzione con `math.atan2(dy, dx)`, e fa un passo in avanti di 4.0 pixel — leggermente più veloce della preda, così guadagna sempre terreno. Infine, se la distanza al quadrato `dx*dx + dy*dy` scende sotto 100 (cioè 10 pixel), la preda viene catturata.

## Codice di Esempio

```python
import turtle
import math
import random

random.seed(42)
screen = turtle.Screen()
screen.tracer(0)

# ... create prey (green) and hunter (red) turtles ...

for frame in range(300):
    prey.right(random.uniform(-30, 30))
    prey.forward(3.5)
    dx = prey.xcor() - hunter.xcor()
    dy = prey.ycor() - hunter.ycor()
    hunter.setheading(math.degrees(math.atan2(dy, dx)))
    hunter.forward(4.0)
    if dx * dx + dy * dy < 100:
        break
    screen.update()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il cacciatore si muove di 4.0 pixel per fotogramma; la preda solo di
    3.5. Il cacciatore catturerà la preda prima che finiscano i 300
    fotogrammi? Fai la tua ipotesi, poi clicca Esegui e guarda la
    caccia!

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
import random

random.seed(42)

screen = turtle.Screen()
screen.tracer(0)

prey = turtle.Turtle()
prey.shape('turtle')
prey.color('forestgreen')
prey.pensize(2)
prey.penup()
prey.goto(100, 120)
prey.pendown()
prey.speed(0)

hunter = turtle.Turtle()
hunter.shape('turtle')
hunter.color('crimson')
hunter.pensize(2)
hunter.penup()
hunter.goto(-150, -140)
hunter.pendown()
hunter.speed(0)

caught = False
for frame in range(300):
    prey.right(random.uniform(-30, 30))
    prey.forward(3.5)
    if abs(prey.xcor()) > 160 or abs(prey.ycor()) > 160:
        angle = math.atan2(-prey.ycor(), -prey.xcor())
        prey.setheading(math.degrees(angle))
    dx = prey.xcor() - hunter.xcor()
    dy = prey.ycor() - hunter.ycor()
    hunter.setheading(math.degrees(math.atan2(dy, dx)))
    hunter.forward(4.0)
    if dx * dx + dy * dy < 100:
        caught = True
    screen.update()
    if caught:
        break

if caught:
    sign = turtle.Turtle()
    sign.hideturtle()
    sign.penup()
    sign.pencolor('black')
    sign.goto(hunter.xcor(), hunter.ycor() + 25)
    sign.write('Caught!', False, 'center')
screen.update()`);
</script>

Il cacciatore si avvicina e appare "Caught!" — con un vantaggio di velocità di 0.5 pixel per fotogramma e una mira perfettamente dritta, il cacciatore vince sempre, prima o poi. Avevi indovinato?

## Come Funziona

`math.atan2(dy, dx)` restituisce l'angolo del vettore `(dx, dy)` — a differenza del semplice `atan(dy/dx)` gestisce tutti e quattro i quadranti e non divide mai per zero. `math.degrees()` converte i radianti nei gradi che `setheading()` si aspetta. Nota il controllo del muro: quando la preda vaga oltre ±160, punta indietro verso il centro `(0, 0)` usando lo stesso trucco `atan2` — puntare verso un bersaglio e fuggire verso la salvezza sono la stessa matematica.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `prey.right(random.uniform(-30, 30))` | Passeggiata casuale: piccola svolta casuale ogni fotogramma |
| `math.atan2(dy, dx)` | Angolo dal cacciatore alla preda, sicuro in tutti i quadranti |
| `hunter.forward(4.0)` | Il cacciatore è 0.5 px/fotogramma più veloce della preda |
| `dx * dx + dy * dy < 100` | Entro 10 px — la distanza al quadrato evita `sqrt` |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Dai un Cervello alla Preda"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione aggiunge un istinto di fuga: quando il cacciatore
    arriva entro 80 pixel, la preda smette di vagare e corre
    **direttamente via**. La preda è ancora più lenta — una guida più
    intelligente le permetterà di sopravvivere a tutti i 300 fotogrammi?
    Fai una previsione, poi eseguilo!

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
import random

random.seed(42)

screen = turtle.Screen()
screen.tracer(0)

prey = turtle.Turtle()
prey.shape('turtle')
prey.color('forestgreen')
prey.pensize(2)
prey.penup()
prey.goto(100, 120)
prey.pendown()
prey.speed(0)

hunter = turtle.Turtle()
hunter.shape('turtle')
hunter.color('crimson')
hunter.pensize(2)
hunter.penup()
hunter.goto(-150, -140)
hunter.pendown()
hunter.speed(0)

caught = False
for frame in range(300):
    dx = prey.xcor() - hunter.xcor()
    dy = prey.ycor() - hunter.ycor()
    if dx * dx + dy * dy < 6400:
        prey.setheading(math.degrees(math.atan2(dy, dx)))
    else:
        prey.right(random.uniform(-30, 30))
    if abs(prey.xcor()) > 160 or abs(prey.ycor()) > 160:
        angle = math.atan2(-prey.ycor(), -prey.xcor())
        prey.setheading(math.degrees(angle))
    prey.forward(3.5)
    dx = prey.xcor() - hunter.xcor()
    dy = prey.ycor() - hunter.ycor()
    hunter.setheading(math.degrees(math.atan2(dy, dx)))
    hunter.forward(4.0)
    if dx * dx + dy * dy < 100:
        caught = True
    screen.update()
    if caught:
        break

sign = turtle.Turtle()
sign.hideturtle()
sign.penup()
sign.pencolor('black')
if caught:
    sign.goto(hunter.xcor(), hunter.ycor() + 25)
    sign.write('Caught!', False, 'center')
else:
    sign.goto(prey.xcor(), prey.ycor() + 25)
    sign.write('Got away!', False, 'center')
screen.update()`);
</script>

La preda in fuga sopravvive molto più a lungo della vagabonda casuale — correre direttamente via annulla la maggior parte del vantaggio di velocità del cacciatore, ma i muri continuano a costringerla a girare. Una guida intelligente conta quanto la velocità!

## Esperimenti

1. **Pareggia le velocità.** Imposta anche il passo del cacciatore a 3.5. Saprai che ha funzionato quando il cacciatore non riesce più a chiudere il divario e appare "Got away!".

2. **Aggiungi un secondo cacciatore.** Crea `hunter2` che parte da (150, -140) con la stessa logica di caccia. Saprai che ha funzionato quando la preda viene messa all'angolo tra due tartarughe rosse.

3. **Mira pigra.** Fai ripuntare il cacciatore solo ogni 10° fotogramma (`if frame % 10 == 0:`). Saprai che ha funzionato quando il percorso rosso diventa una serie di segmenti rettilinei che restano indietro rispetto alla preda.

4. **Riduci il raggio di cattura.** Cambia `100` in `25` (5 pixel). Saprai che ha funzionato quando il cacciatore deve praticamente toccare la preda per vincere.

!!! mascot-celebration "Maestro della Caccia!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Due personaggi che interagiscono, matematica di puntamento, e
    rilevamento delle collisioni — hai appena scritto il ciclo
    fondamentale di ogni scena di inseguimento nei videogiochi!
    Prossimo: **Motivo di Reazione-Diffusione** — pattern da pelle
    animale dalla pura matematica chimica.
