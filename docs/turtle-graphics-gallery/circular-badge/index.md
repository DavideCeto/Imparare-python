---
hide:
    - toc
---
# Distintivo Circolare con Nome

Alla fine di questo laboratorio sarai in grado di:

- Disporre caratteri di testo in un cerchio posizionando ognuno a una posizione angolare calcolata
- Usare `setheading()` per far rivolgere ogni carattere verso l'esterno dal centro
- Combinare testo circolare con decorazioni interne per creare un design di distintivo completo

Un distintivo circolare con un nome disposto attorno al perimetro, due anelli decorativi, e un cerchio riempito al centro. I caratteri sono rivolti verso l'esterno per essere leggibili da fuori il cerchio.

!!! mascot-welcome "Benvenuto al Distintivo Circolare!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il testo circolare appare su monete, francobolli, e sigilli ufficiali.
    In questo laboratorio calcolerai tu stesso la posizione e la rotazione di ogni lettera!
    Programmiamo insieme!

## Come Funziona

Per `n` caratteri spaziati uniformemente attorno a un cerchio di raggio `r`, il carattere `i` è posizionato all'angolo `i * 360 / n` gradi. `setheading(angle + 90)` fa rivolgere la tartaruga verso l'esterno (90° = in alto = radialmente verso l'esterno quando angle=0).

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

name = "PYTHON PROGRAMMER"
n = len(name)
r = 110

monty.pencolor('navy')
monty.goto(0, -r)
monty.pendown()
monty.circle(r)
monty.penup()
monty.goto(0, -(r - 12))
monty.pendown()
monty.circle(r - 12)
monty.penup()

for i, ch in enumerate(name):
    angle_deg = 90 - i * 360 / n
    angle_rad = math.radians(angle_deg)
    x = r * math.cos(angle_rad)
    y = r * math.sin(angle_rad)
    monty.goto(x, y)
    monty.setheading(-angle_deg + 90)
    monty.pencolor('navy')
    monty.write(ch, align='center', font=('Arial', 11, 'bold'))

monty.goto(0, 0)
monty.dot(60, 'navy')
monty.pencolor('white')
monty.goto(-30, -8)
monty.write('PYTHON', font=('Arial', 9, 'bold'))
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni carattere è ruotato per essere rivolto verso l'esterno. Il nome sarà leggibile attorno al cerchio,
    o alcune lettere saranno sottosopra in basso?
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
monty.penup()

name = "PYTHON PROGRAMMER"
n = len(name)
r = 110

monty.pencolor('navy')
monty.goto(0, -r)
monty.pendown()
monty.circle(r)
monty.penup()
monty.goto(0, -(r - 12))
monty.pendown()
monty.circle(r - 12)
monty.penup()

for i, ch in enumerate(name):
    angle_deg = 90 - i * 360 / n
    angle_rad = math.radians(angle_deg)
    x = r * math.cos(angle_rad)
    y = r * math.sin(angle_rad)
    monty.goto(x, y)
    monty.setheading(-angle_deg + 90)
    monty.pencolor('navy')
    monty.write(ch, align='center', font=('Arial', 11, 'bold'))

monty.goto(0, 0)
monty.dot(60, 'navy')
monty.pencolor('white')
monty.goto(-30, -8)
monty.write('PYTHON', font=('Arial', 9, 'bold'))`);
</script>

Le lettere in alto sono leggibili, ma le lettere in basso sono **sottosopra** — perché la tartaruga è rivolta verso l'esterno, le lettere in basso sono rivolte verso l'interno. Avevi indovinato?

## Come Funziona

La tartaruga è sempre rivolta "verso l'esterno" dal centro. Per le lettere in alto (posizione ore 12), "verso l'esterno" è in alto — e il testo si legge correttamente. Per le lettere in basso (ore 6), "verso l'esterno" è in basso — il testo appare sottosopra. La vera composizione tipografica circolare si adatta a questo invertendo la metà inferiore.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `angle_deg = 90 - i * 360 / n` | Inizia in alto (90°), va in senso orario |
| `setheading(-angle_deg + 90)` | Rivolto verso l'esterno dal centro |
| `align='center'` | Centra ogni carattere sulla sua posizione |
| `monty.dot(60, 'navy')` | Cerchio riempito al centro |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Nome"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `name = "PYTHON PROGRAMMER"` con il tuo nome ripetuto per riempire il cerchio.
    Prova a riempirlo con spazi o asterischi per riempire l'anello uniformemente.

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
monty.penup()

name = "* CODING IS FUN * KEEP CODING! "
n = len(name)
r = 120

monty.pencolor('darkred')
monty.goto(0, -r)
monty.pendown()
monty.circle(r)
monty.penup()
monty.goto(0, -(r - 12))
monty.pendown()
monty.circle(r - 12)
monty.penup()

for i, ch in enumerate(name):
    angle_deg = 90 - i * 360 / n
    angle_rad = math.radians(angle_deg)
    x = r * math.cos(angle_rad)
    y = r * math.sin(angle_rad)
    monty.goto(x, y)
    monty.setheading(-angle_deg + 90)
    monty.pencolor('darkred')
    monty.write(ch, align='center', font=('Arial', 10, 'bold'))

monty.goto(0, 0)
monty.dot(70, 'darkred')
monty.pencolor('white')
monty.goto(-22, -8)
monty.write('CODE', font=('Arial', 10, 'bold'))`);
</script>

Gli asterischi agiscono come separatori tra il testo ripetuto, proprio come sulle monete vere!

## Esperimenti

1. **Inverti la metà inferiore.** Per i caratteri dove `angle_deg < -90 or angle_deg > 270`, aggiungi 180° alla direzione. Saprai che ha funzionato quando tutti i caratteri sono leggibili.

2. **Usa una dimensione di carattere diversa.** Cambia la dimensione del carattere e adatta `r` di conseguenza. Saprai che ha funzionato quando appaiono lettere più grandi o più piccole attorno all'anello.

3. **Aggiungi una decorazione a stella.** Dopo il cerchio, disegna una stella a 5 punte dentro il punto centrale. Saprai che ha funzionato quando una stella appare nel mezzo.

4. **Fai un distintivo planetario.** Usa cerchi concentrici a raggi diversi e metti il nome del pianeta attorno all'anello esterno. Saprai che ha funzionato quando sembra un sigillo planetario.

!!! mascot-celebration "Il Tuo Distintivo È Pronto!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai calcolato il posizionamento del testo circolare usando angoli e `goto()` — la stessa matematica
    usata nella coniazione delle monete e nel design dei sigilli ufficiali!
    Prossimo: **Nome in Lettere Blocco** — disegnare grandi lettere in contorno da segmenti di linea.
