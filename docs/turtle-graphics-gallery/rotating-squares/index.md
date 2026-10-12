---
hide:
    - toc
---
# Illusione dei Quadrati Rotanti

Alla fine di questo laboratorio sarai in grado di:

- Disegnare quadrati concentrici che ognuno ruota leggermente dal precedente
- Capire come una piccola rotazione per quadrato crea una forte illusione di rotazione
- Controllare la forza dell'illusione variando il passo di rotazione

Quadrati concentrici, ognuno ruotato di pochi gradi dal precedente — ma perfettamente statici. Il sistema visivo umano interpreta la rotazione graduale come un movimento rotatorio reale. Questa è l'illusione ottica dei "quadrati rotanti".

!!! mascot-welcome "Benvenuto all'Illusione dei Quadrati Rotanti!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il tuo cervello vede movimento dove non ce n'è — pura geometria statica!
    Questa è una delle illusioni ottiche geometriche più famose dell'Op Art.
    Programmiamo insieme!

## Come Funziona

Disegna 20 quadrati concentrici. Ogni quadrato è ruotato di 5° in più del precedente. I quadrati si restringono anche verso l'interno di una quantità fissa. La combinazione di rotazione + restringimento crea l'illusione di un movimento a spirale/rotante.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

n_squares = 20
start_size = 160
rot_step = 5

for i in range(n_squares):
    size = start_size - i * 7
    if size <= 0:
        break
    angle = i * rot_step
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(angle)
    monty.forward(size * math.sqrt(2) / 2)
    monty.setheading(angle + 135)
    monty.pendown()
    monty.pensize(max(1, 3 - i // 7))
    color_val = int(255 * i / n_squares)
    for _ in range(4):
        monty.forward(size)
        monty.left(90)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni quadrato è ruotato di 5° in più del precedente — sono tutti stazionari.
    Sembrerà una pila di quadrati, o apparirà ruotante?
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

n_squares = 20
start_size = 160
rot_step = 5
colors = ['navy', 'royalblue', 'steelblue', 'deepskyblue']

for i in range(n_squares):
    size = start_size - i * 7
    if size <= 0:
        break
    angle = i * rot_step
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(angle)
    monty.forward(size * math.sqrt(2) / 2)
    monty.setheading(angle + 135)
    monty.pencolor(colors[i % len(colors)])
    monty.pendown()
    monty.pensize(2)
    for _ in range(4):
        monty.forward(size)
        monty.left(90)`);
</script>

L'immagine **sembra girare** — ma è completamente statica. Avevi indovinato? L'illusione è più forte quando guardi leggermente al fianco dell'immagine.

## Come Funziona

L'angolo di ogni quadrato viene trovato andando avanti dal centro a 45° (diagonale) e poi girando per disegnare il quadrato. L'illusione funziona perché il nostro sistema visivo estrapola il movimento dal gradiente di rotazione graduale — "legge" la progressione degli angoli come una sequenza temporale invece che una disposizione spaziale.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `angle = i * rot_step` | Ogni quadrato ruotato di 5° in più del precedente |
| `setheading(angle + 135)` | Inizia a disegnare dall'angolo corretto |
| `size - i * 7` | I quadrati si restringono mentre si avvicinano al centro |
| `forward(size * sqrt(2) / 2)` | Distanza fino all'angolo lungo la diagonale |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Falla Girare Più Velocemente"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `rot_step = 5` in `rot_step = 10`. L'illusione di rotazione sarà più forte o più debole?
    Prevedi, poi esegui per scoprirlo!

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

n_squares = 20
start_size = 160
rot_step = 10
colors = ['darkred', 'crimson', 'orangered', 'darkorange']

for i in range(n_squares):
    size = start_size - i * 7
    if size <= 0:
        break
    angle = i * rot_step
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(angle)
    monty.forward(size * math.sqrt(2) / 2)
    monty.setheading(angle + 135)
    monty.pencolor(colors[i % len(colors)])
    monty.pendown()
    monty.pensize(2)
    for _ in range(4):
        monty.forward(size)
        monty.left(90)`);
</script>

`rot_step = 10` crea una disposizione che sembra più caotica e può apparire come una rotazione più veloce ad alcuni osservatori.

## Esperimenti

1. **Prova rot_step = 45.** I quadrati alternano tra due orientamenti. Saprai che ha funzionato quando vedi solo due orientamenti sovrapposti.

2. **Usa nero e bianco alternati.** Imposta i colori su `['black', 'white']`. Saprai che ha funzionato quando l'alto contrasto rende l'illusione ancora più forte.

3. **Usa esagoni invece di quadrati.** Cambia il ciclo interno per disegnare 6 lati di lunghezza `size/1.5` con `left(60)`. Saprai che ha funzionato quando appaiono esagoni.

4. **Disegna sia in senso orario sia antiorario.** Esegui il ciclo due volte — una con `rot_step = 5` e una con `-5`. Saprai che ha funzionato quando appaiono due illusioni a spirale che girano in direzioni opposte.

!!! mascot-celebration "Il Tuo Cervello È Stato Ingannato!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito una vera illusione ottica interamente da quadrati statici!
    L'Op Art (Arte Ottica) usa la matematica e la geometria per ingannare il sistema visivo.
    Prossimo: **Illusione del Muro del Caffè** — linee orizzontali parallele che sembrano inclinate.
