---
hide:
    - toc
---
# Spirografo

Alla fine di questo laboratorio sarai in grado di:

- Tracciare un ipotrocoide (cerchio che rotola all'interno) usando equazioni parametriche
- Capire come `R`, `r`, e `d` controllano il conteggio di petali e anelli
- Vedere come il rapporto `R/r` determina quando la curva si chiude

Un pattern Spirografo — le curve fatte da un cerchio che rotola dentro un cerchio più grande. Cambiare i tre parametri `R` (raggio esterno), `r` (raggio interno), e `d` (distanza della penna dal centro) produce centinaia di pattern diversi.

!!! mascot-welcome "Benvenuto allo Spirografo!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli Spirografi erano un giocattolo famoso negli anni '70 — ora puoi programmarne uno!
    Un piccolo cerchio rotola dentro un cerchio grande, con una penna attaccata al piccolo cerchio.
    Il risultato: belle curve ad anello chiamate ipotrocoidi. Programmiamolo!

## Come Funziona

`x(t) = (R-r)*cos(t) + d*cos((R-r)/r * t)`
`y(t) = (R-r)*sin(t) - d*sin((R-r)/r * t)`

`R` è il raggio del cerchio esterno, `r` quello interno, `d` l'offset della penna dal centro interno.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 130
r = 50
d = 90
steps = 3000
colors = ['royalblue', 'crimson', 'forestgreen']

monty.pencolor('royalblue')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps * r
    x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `R/r = 130/50 = 2,6`. La curva si avvolge `R/r` volte — quanti petali approssimativamente?
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

R = 130
r = 50
d = 90
steps = 3000

monty.pencolor('royalblue')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps * r
    x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

Una curva Spirografo ad anelli — il cerchio interno rotola 2,6 volte per ogni orbita completa, creando anelli sovrapposti. Avevi indovinato?

## Come Funziona

Quando `R/r` è un rapporto di piccoli interi (come 5/2), la curva si chiude perfettamente dopo un piccolo numero di anelli. Quando non è una frazione semplice, la curva impiega molti anelli per chiudersi — o non si chiude mai del tutto.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `R = 130` | Raggio del cerchio esterno |
| `r = 50` | Raggio del cerchio interno rotolante |
| `d = 90` | Distanza della penna dal centro interno |
| `(R-r)*cos(t) + d*cos(...)` | Posizione x parametrica |
| `steps * r` | Più anelli per cerchi interni più grandi |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Usa Interi Esatti"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia in `R=100, r=40, d=70`. Questo dà `R/r = 5/2` esattamente — un rapporto di piccoli interi.
    La curva dovrebbe chiudersi perfettamente dopo 2 orbite e avere 5 petali. Prevedi ed esegui!

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

R = 100
r = 40
d = 70
steps = 3000

monty.pencolor('crimson')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps * r
    x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

`R/r = 100/40 = 5/2` → un perfetto ipotrocoide a 5 petali che si chiude ordinatamente dopo 2 orbite.

## Esperimenti

1. **Prova R=120, r=30 (rapporto 4:1).** Saprai che ha funzionato quando appare una curva a 4 lobi.

2. **Cambia d a un valore molto piccolo.** Prova `d = 10`. Saprai che ha funzionato quando la curva sembra quasi circolare.

3. **Cambia d più grande di r.** Prova `d = 120` con i parametri originali. Saprai che ha funzionato quando gli anelli interni diventano più grandi.

4. **Prova un epitrocoide** (cerchio che rotola all'esterno). Cambia `(R - r)` in `(R + r)` nella formula. Saprai che ha funzionato quando appare uno stile diverso di curva ad anello.

!!! mascot-celebration "Spirografo Completo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato la matematica dietro un vero giocattolo degli anni '70!
    Queste curve si chiamano ipotrocoidi — sono usate nell'ingegneria per progettare
    i motori rotativi Wankel. Prossimo: **Curva a Farfalla** — un classico trigonometrico.
