---
hide:
    - toc
---
# Disegnatore di Spirografi

Alla fine di questo laboratorio sarai in grado di:

- Disegnare una famiglia di curve ipotrocoidi che si animano una dopo l'altra
- Usare una lista di insiemi di parametri per creare una sequenza di diversi pattern Spirografo
- Capire come cambiare `R`, `r`, e `d` produce forme completamente diverse

Un disegnatore di Spirografi che scorre tra 6 diversi insiemi di parametri, disegnando ognuno in un colore diverso per costruire un display stratificato di curve ipotrocoidi sovrapposte.

!!! mascot-welcome "Benvenuto al Disegnatore di Spirografi!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio lo Spirografo si disegna da solo — scorrendo automaticamente tra 6 diversi
    insiemi di parametri, costruendo un display stratificato!
    Programmiamo insieme!

## Come Funziona

Una lista di tuple `(R, r, d, color)` definisce 6 insiemi di parametri Spirografo. Il ciclo esterno le scorre; il ciclo interno disegna ogni ipotrocoide. `tracer(0)` e `update()` mantengono l'animazione fluida.

## Codice di Esempio

```python
import turtle
import math

screen = turtle.Screen()
screen.tracer(0)
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

params = [
    (130, 50, 90, 'royalblue'),
    (100, 40, 70, 'crimson'),
    (120, 30, 80, 'forestgreen'),
    (110, 45, 85, 'darkorange'),
    (140, 60, 100, 'purple'),
    (100, 25, 75, 'teal'),
]

for R, r, d, color in params:
    monty.pencolor(color)
    monty.pensize(1)
    steps = 2000
    monty.penup()
    t0 = 0
    x0 = (R-r)*math.cos(t0) + d*math.cos((R-r)/r*t0)
    y0 = (R-r)*math.sin(t0) - d*math.sin((R-r)/r*t0)
    monty.goto(x0, y0)
    monty.pendown()
    for i in range(1, steps + 1):
        t = 2 * math.pi * i / steps * r
        x = (R-r)*math.cos(t) + d*math.cos((R-r)/r*t)
        y = (R-r)*math.sin(t) - d*math.sin((R-r)/r*t)
        monty.goto(x, y)
        if i % 50 == 0:
            screen.update()
    screen.update()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Sei diversi insiemi di parametri in sei colori diversi.
    Le curve si sovrapporranno ordinatamente, o creeranno un disordine caotico?
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

screen = turtle.Screen()
screen.tracer(0)
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

params = [
    (130, 50, 90, 'royalblue'),
    (100, 40, 70, 'crimson'),
    (120, 30, 80, 'forestgreen'),
    (110, 45, 85, 'darkorange'),
    (140, 60, 100, 'purple'),
    (100, 25, 75, 'teal'),
]

for R, r, d, color in params:
    monty.pencolor(color)
    monty.pensize(1)
    steps = 2000
    monty.penup()
    t0 = 0
    x0 = (R-r)*math.cos(t0) + d*math.cos((R-r)/r*t0)
    y0 = (R-r)*math.sin(t0) - d*math.sin((R-r)/r*t0)
    monty.goto(x0, y0)
    monty.pendown()
    for i in range(1, steps + 1):
        t = 2 * math.pi * i / steps * r
        x = (R-r)*math.cos(t) + d*math.cos((R-r)/r*t)
        y = (R-r)*math.sin(t) - d*math.sin((R-r)/r*t)
        monty.goto(x, y)
        if i % 50 == 0:
            screen.update()
    screen.update()`);
</script>

Sei curve Spirografo colorate, ognuna con una forma diversa, che costruiscono una composizione stratificata. Avevi indovinato sulla sovrapposizione?

## Come Funziona

Ogni tripletta `(R, r, d)` produce una curva completamente unica. Poiché tutte le curve sono disegnate dallo stesso centro, si sovrappongono come strati in un dipinto. `if i % 50 == 0: screen.update()` aggiorna il display ogni 50 punti per mostrare il progresso del disegno.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `params = [...]` | Lista di tuple `(R, r, d, color)` |
| `for R, r, d, color in params` | Spacchetta ogni insieme di parametri |
| `if i % 50 == 0: screen.update()` | Mostra il progresso ogni 50 passi |
| `screen.tracer(0)` | Controllo manuale sull'aggiornamento dello schermo |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Progetta il Tuo Insieme"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Sostituisci la lista `params` con 3 insiemi di parametri di tua scelta.
    Prova a fare curve che abbiano ognuna un numero diverso di anelli (il rapporto R/r lo determina).
    Quali rapporti scegli?

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

screen = turtle.Screen()
screen.tracer(0)
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

params = [
    (120, 40, 80, 'royalblue'),
    (120, 24, 80, 'crimson'),
    (120, 15, 80, 'gold'),
]

for R, r, d, color in params:
    monty.pencolor(color)
    monty.pensize(1)
    steps = 2000
    monty.penup()
    t0 = 0
    x0 = (R-r)*math.cos(t0) + d*math.cos((R-r)/r*t0)
    y0 = (R-r)*math.sin(t0) - d*math.sin((R-r)/r*t0)
    monty.goto(x0, y0)
    monty.pendown()
    for i in range(1, steps + 1):
        t = 2 * math.pi * i / steps * r
        x = (R-r)*math.cos(t) + d*math.cos((R-r)/r*t)
        y = (R-r)*math.sin(t) - d*math.sin((R-r)/r*t)
        monty.goto(x, y)
        if i % 50 == 0:
            screen.update()
    screen.update()`);
</script>

Con lo stesso `R=120` e `d=80` ma valori `r` diversi (40, 24, 15), le tre curve hanno rispettivamente 3, 5, e 8 anelli — corrispondendo a `R/r`.

## Esperimenti

1. **Aggiungi più curve.** Estendi `params` a 10 voci. Saprai che ha funzionato quando appare una composizione più densa e colorata.

2. **Usa colori pastello.** Sostituisci i colori con tonalità più chiare. Saprai che ha funzionato quando le curve sovrapposte producono un aspetto più dolce.

3. **Pulisci e ridisegna.** Aggiungi `screen.clearscreen()` tra le curve — una alla volta. Saprai che ha funzionato quando ogni curva appare da sola prima della successiva.

4. **Varia il conteggio dei passi.** Usa più passi per rapporti `R/r` più alti. Saprai che ha funzionato quando le curve complesse sembrano più lisciate.

!!! mascot-celebration "Macchina dell'Arte!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Il tuo codice genera arte automaticamente da una lista di parametri — una macchina dell'arte!
    Questa è l'essenza dell'arte generativa: codice che produce immagini da regole.
    Prossimo: **Categoria 11 — Pattern Avanzati!**
