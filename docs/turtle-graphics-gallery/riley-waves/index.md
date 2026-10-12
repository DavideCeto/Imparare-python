---
hide:
    - toc
---
# Onde di Bridget Riley

Alla fine di questo laboratorio sarai in grado di:

- Disegnare una serie di curve a onda sinusoidale parallele con ampiezza variabile
- Creare un'illusione visiva di una superficie ondulata usando solo linee statiche
- Controllare la forma dell'onda con parametri di frequenza e ampiezza

Ispirato alla pittrice Op Art Bridget Riley, questo pattern disegna righe di curve sinusoidali nere ondulate su uno sfondo bianco. L'ampiezza variabile fa sembrare che alcune parti del canvas si rigonfino e si ritirino.

!!! mascot-welcome "Benvenuto alle Onde di Bridget Riley!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Bridget Riley è un'artista britannica che crea pattern che sembrano muoversi.
    I suoi dipinti degli anni '60 usano solo bianco e nero, eppure sembrano vibrare!
    Programmiamo i suoi pattern d'onda!

## Come Funziona

Disegna molte curve sinusoidali orizzontali a posizioni y uniformemente spaziate. Ogni curva ha la stessa frequenza x. L'ampiezza di ogni curva varia — massima al centro, che si assottiglia verso i bordi. Questo crea l'illusione di una superficie che si rigonfia o ondeggia.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

n_waves = 18
wave_width = 320
freq = 3
max_amp = 20
y_spacing = 16

monty.pensize(1)
monty.pencolor('black')

for row in range(n_waves):
    center_distance = abs(row - n_waves / 2) / (n_waves / 2)
    amp = max_amp * (1 - center_distance ** 2)
    y_base = (row - n_waves / 2) * y_spacing
    steps = 200
    monty.penup()
    for i in range(steps + 1):
        x = -wave_width / 2 + wave_width * i / steps
        y = y_base + amp * math.sin(freq * 2 * math.pi * i / steps)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)
    monty.penup()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Le righe centrali hanno un'ampiezza maggiore delle righe ai bordi.
    Questo creerà un pattern piatto, o il centro sembrerà rigonfiarsi verso l'esterno?
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

n_waves = 18
wave_width = 320
freq = 3
max_amp = 20
y_spacing = 16

monty.pensize(1)
monty.pencolor('black')

for row in range(n_waves):
    center_distance = abs(row - n_waves / 2) / (n_waves / 2)
    amp = max_amp * (1 - center_distance ** 2)
    y_base = (row - n_waves / 2) * y_spacing
    steps = 200
    monty.penup()
    for i in range(steps + 1):
        x = -wave_width / 2 + wave_width * i / steps
        y = y_base + amp * math.sin(freq * 2 * math.pi * i / steps)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)
    monty.penup()`);
</script>

Il centro **sembra rigonfiarsi** — le onde di ampiezza maggiore nel mezzo creano l'illusione di una superficie 3D. Avevi indovinato?

## Come Funziona

`center_distance = abs(row - n_waves/2) / (n_waves/2)` va da 0 (centro) a 1 (bordi). L'ampiezza `max_amp * (1 - center_distance^2)` segue una forma parabolica — massima al centro, che si assottiglia a quasi zero ai bordi. Questo gradiente crea l'illusione del rigonfiamento.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `center_distance` | Quanto è lontana questa riga dal centro (0=centro, 1=bordo) |
| `amp = max_amp * (1 - center_distance^2)` | Ampiezza parabolica — grande al centro, piccola ai bordi |
| `amp * math.sin(freq * 2 * pi * i / steps)` | Onda sinusoidale all'ampiezza di questa riga |
| `freq = 3` | Numero di cicli d'onda completi per riga |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova Più Onde"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `n_waves = 18` in `n_waves = 30` e `freq = 5`.
    Più onde con frequenza più alta — l'illusione sarà più forte o diversa?
    Prevedi, poi eseguila!

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

n_waves = 30
wave_width = 320
freq = 5
max_amp = 14
y_spacing = 10

monty.pensize(1)
monty.pencolor('black')

for row in range(n_waves):
    center_distance = abs(row - n_waves / 2) / (n_waves / 2)
    amp = max_amp * (1 - center_distance ** 2)
    y_base = (row - n_waves / 2) * y_spacing
    steps = 200
    monty.penup()
    for i in range(steps + 1):
        x = -wave_width / 2 + wave_width * i / steps
        y = y_base + amp * math.sin(freq * 2 * math.pi * i / steps)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)
    monty.penup()`);
</script>

Più onde e frequenza più alta creano un aspetto più denso e vibrante — molto simile ai dipinti originali di Riley.

## Esperimenti

1. **Usa un'ampiezza lineare invece di parabolica.** Cambia in `amp = max_amp * (1 - center_distance)`. Saprai che ha funzionato quando l'ampiezza si assottiglia linearmente invece che parabolicamente.

2. **Aggiungi spostamenti di fase.** Aggiungi `+ row * 0.2` all'argomento del seno. Saprai che ha funzionato quando le onde si spostano diagonalmente invece di essere perfettamente allineate.

3. **Varia la frequenza.** Usa `freq = 2 + row / 3` così le righe interne hanno frequenza più alta. Saprai che ha funzionato quando la frequenza dell'onda cambia da riga a riga.

4. **Usa due colori.** Riempi le aree sopra l'onda di nero e sotto di bianco. Saprai che ha funzionato quando appaiono fasce nere e bianche alternate.

!!! mascot-celebration "Vibrante di Matematica!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato Op Art ispirata a Bridget Riley!
    Questi pattern furono progettati negli anni '60 usando riga e compasso — ora puoi programmarli.
    Prossimo: **Esagoni in Espansione** — anelli esagonali concentrici.
