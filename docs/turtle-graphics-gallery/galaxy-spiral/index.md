---
hide:
    - toc
---
# Bracci a Spirale della Galassia

Alla fine di questo laboratorio sarai in grado di:

- Modellare i bracci a spirale di una galassia usando spirali logaritmiche distanziate di 180°
- Disperdere punti stellari lungo i bracci a spirale con offset casuali
- Usare dimensioni e colori di punto diversi per simulare la luminosità stellare

Una galassia a spirale a due bracci con punti stellari dispersi che formano i bracci, un rigonfiamento centrale denso, e stelle di sfondo. I bracci seguono spirali logaritmiche, proprio come la Via Lattea.

!!! mascot-welcome "Benvenuto alla Galassia!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Galassie come la Via Lattea hanno bracci a spirale che seguono curve logaritmiche.
    In questo laboratorio costruirai una mini galassia usando quella stessa matematica!
    Programmiamo insieme!

## Come Funziona

Per ogni braccio, posiziona punti a posizioni `r = scale * exp(b * theta)` per theta da 0 a 3π. Il secondo braccio è distanziato di π (180°). Ogni punto stellare ottiene una dispersione casuale dalla sua posizione ideale. Il rigonfiamento centrale è un ammasso denso di punti a piccoli raggi.

## Codice di Esempio

```python
import turtle
import math
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

b = 0.25
arm_colors = ['white', 'lightyellow']

for arm in range(2):
    offset = arm * math.pi
    for i in range(300):
        theta = i * math.pi * 3 / 300
        r = 12 * math.exp(b * theta)
        angle = theta + offset
        scatter = random.gauss(0, 4)
        x = (r + scatter) * math.cos(angle)
        y = (r + scatter) * math.sin(angle)
        monty.penup()
        monty.goto(x, y)
        size = random.choice([2, 2, 2, 3, 4])
        monty.dot(size, arm_colors[arm])

for _ in range(200):
    r = random.gauss(0, 20)
    a = random.uniform(0, 2 * math.pi)
    monty.penup()
    monty.goto(r * math.cos(a), r * math.sin(a))
    monty.dot(random.choice([2, 3, 4]), 'white')

for _ in range(80):
    x = random.uniform(-180, 180)
    y = random.uniform(-140, 140)
    monty.penup()
    monty.goto(x, y)
    monty.dot(1, 'lightgray')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni braccio ha 300 punti dispersi attorno a una spirale logaritmica.
    I bracci sembreranno curve strette o nuvole diffuse di stelle?
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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

b = 0.25
arm_colors = ['white', 'lightyellow']

for arm in range(2):
    offset = arm * math.pi
    for i in range(300):
        theta = i * math.pi * 3 / 300
        r = 12 * math.exp(b * theta)
        angle = theta + offset
        scatter = random.gauss(0, 4)
        x = (r + scatter) * math.cos(angle)
        y = (r + scatter) * math.sin(angle)
        monty.penup()
        monty.goto(x, y)
        size = random.choice([2, 2, 2, 3, 4])
        monty.dot(size, arm_colors[arm])

for _ in range(200):
    r = random.gauss(0, 20)
    a = random.uniform(0, 2 * math.pi)
    monty.penup()
    monty.goto(r * math.cos(a), r * math.sin(a))
    monty.dot(random.choice([2, 3, 4]), 'white')

for _ in range(80):
    x = random.uniform(-180, 180)
    y = random.uniform(-140, 140)
    monty.penup()
    monty.goto(x, y)
    monty.dot(1, 'lightgray')`);
</script>

**Nuvole diffuse** — la dispersione Gaussiana fa sembrare i bracci come fasce sfocate invece di linee sottili, proprio come le vere foto di galassie. Avevi indovinato?

## Come Funziona

`random.gauss(0, 4)` aggiunge una dispersione casuale Gaussiana (a campana). La maggior parte delle stelle è vicina alla spirale ideale, ma alcune si allontanano. Il rigonfiamento centrale usa `random.gauss(0, 20)` — un ammasso più compatto.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `b = 0.25` | Parametro di strettezza della spirale |
| `math.exp(b * theta)` | Spirale logaritmica — cresce esponenzialmente |
| `offset = arm * math.pi` | Ruota il secondo braccio di 180° |
| `random.gauss(0, 4)` | Dispersione Gaussiana attorno al percorso della spirale |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Terzo Braccio"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `range(2)` in `range(3)` e `offset = arm * math.pi` in `offset = arm * 2 * math.pi / 3`.
    Una galassia a tre bracci! Quale offset di angolo serve a ogni braccio?

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

b = 0.25
arm_colors = ['white', 'lightyellow', 'lightblue']

for arm in range(3):
    offset = arm * 2 * math.pi / 3
    for i in range(300):
        theta = i * math.pi * 3 / 300
        r = 12 * math.exp(b * theta)
        angle = theta + offset
        scatter = random.gauss(0, 4)
        x = (r + scatter) * math.cos(angle)
        y = (r + scatter) * math.sin(angle)
        monty.penup()
        monty.goto(x, y)
        size = random.choice([2, 2, 2, 3, 4])
        monty.dot(size, arm_colors[arm])

for _ in range(200):
    r = random.gauss(0, 20)
    a = random.uniform(0, 2 * math.pi)
    monty.penup()
    monty.goto(r * math.cos(a), r * math.sin(a))
    monty.dot(random.choice([2, 3, 4]), 'white')`);
</script>

Tre bracci distanziati di 120° — come la Galassia del Triangolo, che in realtà ha questa struttura!

## Esperimenti

1. **Cambia la dispersione.** Cambia `random.gauss(0, 4)` in `random.gauss(0, 10)`. Saprai che ha funzionato quando i bracci sembrano più sfocati e diffusi.

2. **Spirale più stretta.** Cambia `b = 0.25` in `b = 0.4`. Saprai che ha funzionato quando i bracci si avvolgono più ripidamente verso l'interno.

3. **Galassia più grande.** Cambia `12` in `8` e `range(300)` in `range(500)`. Saprai che ha funzionato quando i bracci si estendono più lontano e hanno più stelle.

4. **Colora per distanza.** Rendi le stelle interne gialle e quelle esterne blu — stelle più calde vicino al centro, più fredde al bordo. Saprai che ha funzionato quando il gradiente di colore segue i bracci.

!!! mascot-celebration "Hai Costruito una Galassia!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai modellato i bracci di una galassia a spirale con spirali logaritmiche e dispersione Gaussiana!
    I veri astrofisici usano gli stessi modelli matematici per mappare la Via Lattea.
    Prossimo: **Onde Concentriche** — anelli concentrici che simulano increspature d'acqua.
