---
hide:
    - toc
---
# Delta del Fiume

Alla fine di questo laboratorio sarai in grado di:

- Far crescere un fiume che si dirama usando `random.randint()` e `random.uniform()`
- Potare i rami che diventano troppo sottili o che escono dal canvas
- Usare `random.seed()` per far ripetere esattamente un disegno casuale

Un fiume largo entra dalla parte alta del canvas e si apre a ventaglio in decine di ruscelli sempre più sottili, proprio come un vero delta fluviale che incontra il mare. Ogni esecuzione del programma *potrebbe* essere diversa — ma `random.seed()` blocca un particolare delta così puoi studiarlo.

!!! mascot-welcome "Benvenuto al Delta del Fiume!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I fiumi non seguono una formula — vagano e si dividono a caso.
    In questo laboratorio userai il modulo `random` di Python per far
    crescere un delta nello stesso modo in cui lo fa la natura: una decisione
    di ramificazione alla volta!

## Come Funziona

Il programma mantiene una lista di rami attivi, ognuno con una posizione, una direzione e una larghezza. A ogni passo, ogni ramo si divide a caso in 1 o 2 figli con un piccolo cambiamento casuale di direzione; la divisione rende i figli più sottili. I rami che diventano più sottili di 1 pixel o che escono dal canvas vengono potati (rimossi dalla lista) — è questo che fa sfumare il delta in modo naturale.

## Codice di Esempio

```python
import turtle
import random
import math
random.seed(42)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
screen = turtle.Screen()
screen.bgcolor('wheat')

def river_color(w):
    if w > 7:
        return 'navy'
    elif w > 5:
        return 'royalblue'
    elif w > 3:
        return 'steelblue'
    elif w > 2:
        return 'dodgerblue'
    else:
        return 'deepskyblue'

branches = [[0, 190, 270, 10.0]]
for step in range(44):
    new_branches = []
    for b in branches:
        x = b[0]
        y = b[1]
        h = b[2]
        w = b[3]
        kids = random.randint(1, 2)
        for k in range(kids):
            nh = h + random.uniform(-22, 22)
            if nh < 240:
                nh = 240
            if nh > 300:
                nh = 300
            if kids == 2:
                nw = w * 0.8
            else:
                nw = w * 0.96
            length = random.uniform(16, 28)
            rad = math.radians(nh)
            nx = x + length * math.cos(rad)
            ny = y + length * math.sin(rad)
            if nw < 1 or abs(nx) > 195 or ny < -195:
                continue
            monty.penup()
            monty.goto(x, y)
            monty.pendown()
            monty.pensize(nw)
            monty.pencolor(river_color(nw))
            monty.goto(nx, ny)
            new_branches.append([nx, ny, nh, nw])
    branches = new_branches[:40]
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il fiume inizia largo 10 pixel, ogni divisione moltiplica la larghezza di
    un ramo per 0,8, e i rami più sottili di 1 pixel scompaiono.
    Pensi che il delta starà ancora scorrendo quando raggiungerà la metà
    inferiore del canvas? Fai la tua previsione, poi clicca Esegui!

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
import random
import math
random.seed(42)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
screen = turtle.Screen()
screen.bgcolor('wheat')

def river_color(w):
    if w > 7:
        return 'navy'
    elif w > 5:
        return 'royalblue'
    elif w > 3:
        return 'steelblue'
    elif w > 2:
        return 'dodgerblue'
    else:
        return 'deepskyblue'

branches = [[0, 190, 270, 10.0]]
for step in range(44):
    new_branches = []
    for b in branches:
        x = b[0]
        y = b[1]
        h = b[2]
        w = b[3]
        kids = random.randint(1, 2)
        for k in range(kids):
            nh = h + random.uniform(-22, 22)
            if nh < 240:
                nh = 240
            if nh > 300:
                nh = 300
            if kids == 2:
                nw = w * 0.8
            else:
                nw = w * 0.96
            length = random.uniform(16, 28)
            rad = math.radians(nh)
            nx = x + length * math.cos(rad)
            ny = y + length * math.sin(rad)
            if nw < 1 or abs(nx) > 195 or ny < -195:
                continue
            monty.penup()
            monty.goto(x, y)
            monty.pendown()
            monty.pensize(nw)
            monty.pencolor(river_color(nw))
            monty.goto(nx, ny)
            new_branches.append([nx, ny, nh, nw])
    branches = new_branches[:40]`);
</script>

Sì — i ruscelli più sottili in `deepskyblue` arrivano in profondità nella metà inferiore prima di sfumare sotto 1 pixel. Avevi indovinato?

## Come Funziona

Questa è ramificazione *stocastica* (casuale), e funziona diversamente dai frattali deterministici come l'Albero Frattale. Lì, ogni ramo si divide esattamente nello stesso modo, quindi il risultato è perfettamente prevedibile. Qui, `random.randint(1, 2)` decide quanti figli ottiene ogni ramo e `random.uniform(-22, 22)` piega leggermente ogni figlio, così nessuna lineage somiglia a un'altra. La potatura — il `continue` che salta i rami troppo sottili o fuori dai limiti — è ciò che impedisce alla casualità di scorrere senza controllo. Poiché `random.seed(42)` avvia il generatore di numeri casuali da un punto fisso, le stesse scelte "casuali" avvengono a ogni esecuzione.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `random.seed(42)` | Blocca la sequenza casuale così ogni esecuzione disegna lo stesso delta |
| `kids = random.randint(1, 2)` | Ogni ramo continua a caso (1) o si divide in due (2) |
| `if nw < 1 or abs(nx) > 195 or ny < -195:` | Pota i rami troppo sottili o fuori dal canvas |
| `branches = new_branches[:40]` | I figli diventano i rami attivi per il passo successivo (limitati a 40) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto non sostituisce mai i vecchi rami con quelli nuovi,
    quindi il fiume non cresce mai oltre i suoi primi segmenti!
    Aggiungi `branches = new_branches[:40]` come ultima riga del
    ciclo `for step` (indentata di quattro spazi) ed eseguilo di nuovo.

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
import random
import math
random.seed(42)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
screen = turtle.Screen()
screen.bgcolor('wheat')

def river_color(w):
    if w > 7:
        return 'navy'
    elif w > 5:
        return 'royalblue'
    elif w > 3:
        return 'steelblue'
    elif w > 2:
        return 'dodgerblue'
    else:
        return 'deepskyblue'

branches = [[0, 190, 270, 10.0]]
for step in range(44):
    new_branches = []
    for b in branches:
        x = b[0]
        y = b[1]
        h = b[2]
        w = b[3]
        kids = random.randint(1, 2)
        for k in range(kids):
            nh = h + random.uniform(-22, 22)
            if nh < 240:
                nh = 240
            if nh > 300:
                nh = 300
            if kids == 2:
                nw = w * 0.8
            else:
                nw = w * 0.96
            length = random.uniform(16, 28)
            rad = math.radians(nh)
            nx = x + length * math.cos(rad)
            ny = y + length * math.sin(rad)
            if nw < 1 or abs(nx) > 195 or ny < -195:
                continue
            monty.penup()
            monty.goto(x, y)
            monty.pendown()
            monty.pensize(nw)
            monty.pencolor(river_color(nw))
            monty.goto(nx, ny)
            new_branches.append([nx, ny, nh, nw])
    # aggiungi qui la riga mancante`);
</script>

Senza quella riga, `branches` resta bloccato al segmento di partenza, quindi il programma si limita a ridisegnare brevi monconi in alto 44 volte. Con essa, ogni generazione di figli diventa la generazione successiva di genitori — e il delta scorre.

## Esperimenti

1. **Cambia il seme.** Prova `random.seed(7)` o il tuo numero fortunato. Saprai che ha funzionato quando appare un delta completamente diverso — stesse regole, nuovo fiume.

2. **Forza una divisione a ogni passo.** Cambia `random.randint(1, 2)` in `random.randint(2, 2)`. Saprai che ha funzionato quando il delta diventa corto e cespuglioso — dividersi sempre fa assottigliare i ruscelli molto più in fretta.

3. **Inizia con un fiume più potente.** Cambia la larghezza iniziale `10.0` in `14.0`. Saprai che ha funzionato quando i ruscelli sopravvivono più a lungo e il delta raggiunge più in basso sul canvas.

4. **Lascialo vagare di più.** Cambia `random.uniform(-22, 22)` in `random.uniform(-40, 40)`. Saprai che ha funzionato quando i ruscelli zigzagano selvaggiamente invece di scorrere quasi dritti verso il basso.

!!! mascot-celebration "Hai Fatto Crescere un Fiume!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena usato la casualità *con regole* — divisione, assottigliamento, potatura — per far
    crescere qualcosa che sembra vivo. È così che la natura costruisce delta, fulmini,
    e anche vasi sanguigni!
    Prossimo: **Ramo di Corallo** — ramificazione recursiva con torsioni casuali e
    colori che sfumano dal rosso profondo al rosa.
