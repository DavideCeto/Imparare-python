---
hide:
    - toc
---
# Ramo di Corallo

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione recursiva dove ogni chiamata genera un numero *casuale* di nuove chiamate
- Variare gli angoli dei rami casualmente con `random.uniform(-40, 40)`
- Spostare i colori dal rosso scuro alla base al rosa pallido alle punte usando la profondità

Un singolo tronco rosso scuro si alza dal fondo del mare ed esplode in un ventaglio di rami — alcuni nodi fanno germinare un ramo, alcuni due, alcuni tre — finendo in una nuvola di punte rosa pallido. Questa è ricorsione come nell'Albero Frattale, ma con la casualità della natura mescolata dentro.

!!! mascot-welcome "Benvenuto alla Barriera Corallina!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il corallo vero non si dirama mai in modo perfettamente uniforme — ogni
    bivio è un po' diverso. In questo laboratorio la tua funzione recursiva
    tirerà i dadi a ogni ramo, proprio come il corallo che cresce nell'oceano!

## Come Funziona

La funzione `branch` disegna un segmento, poi chiama `random.randint(1, 3)` per decidere quanti sotto-rami generare — questa si chiama ricorsione ad *arità variabile* perché il numero di chiamate recursive varia. Ogni figlio gira di una quantità casuale tra -40° e +40° ed è un po' più corto del suo genitore. Il parametro `depth` conta a quanti livelli di profondità siamo, e sceglie sia la dimensione della penna (spessa alla base, sottile alle punte) sia il colore da una lista che va dal rosso scuro al rosa.

## Codice di Esempio

```python
import turtle
import random
random.seed(8)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['darkred', 'firebrick', 'crimson', 'palevioletred', 'hotpink', 'lightpink', 'pink', 'mistyrose']

def branch(x, y, heading, length, depth):
    if depth >= 8 or length < 3:
        return
    monty.penup()
    monty.goto(x, y)
    monty.setheading(heading)
    monty.pensize(8 - depth)
    monty.pencolor(colors[depth])
    monty.pendown()
    monty.forward(length)
    nx = monty.xcor()
    ny = monty.ycor()
    kids = random.randint(1, 3)
    for k in range(kids):
        turn = random.uniform(-40, 40)
        branch(nx, ny, heading + turn, length * 0.72, depth + 1)

branch(0, -185, 90, 95, 0)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questo programma è pieno di scelte casuali, ma inizia con
    `random.seed(8)`. Se clicchi Esegui due volte di fila, otterrai
    **lo stesso corallo entrambe le volte o uno diverso ogni volta**?
    Fai la tua ipotesi, poi eseguilo due volte per controllare!

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
import random
random.seed(8)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['darkred', 'firebrick', 'crimson', 'palevioletred', 'hotpink', 'lightpink', 'pink', 'mistyrose']

def branch(x, y, heading, length, depth):
    if depth >= 8 or length < 3:
        return
    monty.penup()
    monty.goto(x, y)
    monty.setheading(heading)
    monty.pensize(8 - depth)
    monty.pencolor(colors[depth])
    monty.pendown()
    monty.forward(length)
    nx = monty.xcor()
    ny = monty.ycor()
    kids = random.randint(1, 3)
    for k in range(kids):
        turn = random.uniform(-40, 40)
        branch(nx, ny, heading + turn, length * 0.72, depth + 1)

branch(0, -185, 90, 95, 0)`);
</script>

Lo stesso corallo, ogni volta — `random.seed(8)` riavvia il generatore di numeri casuali esattamente dallo stesso punto, quindi ogni scelta "casuale" si ripete. Avevi indovinato?

## Come Funziona

Confronta questo con l'Albero Frattale, dove ogni ramo si divide sempre esattamente in 2 figli ad angoli fissi. Qui `kids = random.randint(1, 3)` rende l'*arità* (numero di chiamate recursive) casuale: un nodo con 1 figlio crea un braccio lungo e spelacchiato, mentre un nodo con 3 figli crea un ventaglio denso. Il gradiente di colore è guidato interamente dalla `depth`: alla profondità 0 il tronco usa `colors[0]` ('darkred'), e ogni livello più profondo avanza di un passo nella lista verso 'mistyrose'. La dimensione della penna fa lo stesso trucco al contrario con `8 - depth`, così il corallo è spesso dove è scuro e delicato dove è pallido.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `kids = random.randint(1, 3)` | Ogni nodo genera 1, 2 o 3 sotto-rami — ricorsione ad arità variabile |
| `turn = random.uniform(-40, 40)` | Ogni figlio si piega di una quantità casuale entro ±40° |
| `monty.pencolor(colors[depth])` | I livelli più profondi usano colori più chiari: base rosso scuro, punte rosa |
| `if depth >= 8 or length < 3:` | Il caso base — ferma la ricorsione così non può andare avanti per sempre |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Fai Crescere un Corallo Più Folto"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nel programma qui sotto, `random.randint(1, 3)` è stato cambiato in
    `random.randint(2, 3)`, così ogni nodo genera **almeno due**
    sotto-rami. Questo corallo sarà più folto o più scarno di prima?
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
import random
random.seed(8)

monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['darkred', 'firebrick', 'crimson', 'palevioletred', 'hotpink', 'lightpink', 'pink', 'mistyrose']

def branch(x, y, heading, length, depth):
    if depth >= 8 or length < 3:
        return
    monty.penup()
    monty.goto(x, y)
    monty.setheading(heading)
    monty.pensize(8 - depth)
    monty.pencolor(colors[depth])
    monty.pendown()
    monty.forward(length)
    nx = monty.xcor()
    ny = monty.ycor()
    kids = random.randint(2, 3)
    for k in range(kids):
        turn = random.uniform(-40, 40)
        branch(nx, ny, heading + turn, length * 0.72, depth + 1)

branch(0, -185, 90, 95, 0)`);
</script>

Molto più folto — garantire almeno 2 figli a ogni nodo raddoppia più o meno i rami a ogni livello, così la chioma rosa diventa una nuvola densa.

## Esperimenti

1. **Tira nuovi dadi.** Cambia `random.seed(8)` con un altro numero ed esegui un po' di volte. Saprai che ha funzionato quando ogni seme fa crescere il suo corallo unico.

2. **Calma l'acqua.** Cambia `random.uniform(-40, 40)` in `random.uniform(-15, 15)`. Saprai che ha funzionato quando il corallo cresce più dritto e simile a un albero invece di espandersi lateralmente.

3. **Allunga i rami.** Cambia `length * 0.72` in `length * 0.78`. Saprai che ha funzionato quando il corallo cresce più alto e slanciato, raggiungendo più in alto sul canvas.

4. **Crea un corallo di sole.** Sostituisci la lista di colori con `['darkorange', 'orange', 'gold', 'yellow', 'khaki', 'lightyellow', 'ivory', 'white']`. Saprai che ha funzionato quando il corallo brilla arancione alla base e bianco alle punte.

!!! mascot-celebration "Una Barriera Tutta Tua!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ricorsione più casualità è uguale a forme simili a quelle della vita —
    l'hai appena dimostrato! Ogni valore di seme è un corallo diverso che
    aspetta di essere scoperto. Prossimo: **Nervatura della Foglia** —
    disegna una foglia e dalle uno scheletro realistico di venature,
    profondo tre livelli.
