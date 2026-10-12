---
hide:
    - toc
---
# Banco di Pesci

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `fish(x, y, size)` che disegna una forma animale riconoscibile
- Capire come una funzione con argomenti diversi crea variazione visiva
- Combinare archi `circle()`, triangoli, e punti per costruire un pesce con corpo, pinna caudale, e occhio

Una dozzina di pesci blu di dimensioni variate nuotano verso sinistra attraverso il canvas in un banco liberamente raggruppato — ognuno disegnato dalla stessa funzione.

!!! mascot-welcome "Benvenuto al Banco di Pesci!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio vedrai come una singola funzione può generare un intero banco di pesci —
    ognuno leggermente diverso in dimensione e posizione ma costruito dallo stesso codice.
    Programmiamo insieme!

## Come Funziona il Pesce

Ogni pesce è costruito da tre parti:

1. Un **corpo**: un ovale a punta fatto di due archi `circle()` che si incontrano al naso e alla coda
2. Una **pinna caudale**: un piccolo triangolo riempito attaccato dietro il corpo
3. Un **occhio**: un punto bianco con una pupilla nera, vicino al naso

La tartaruga inizia al naso del pesce (la punta sinistra), traccia un arco lungo la pancia fino al
punto della coda, gira, e traccia un secondo arco lungo il dorso per ritornare al naso. Poi
salta al punto della coda per disegnare la pinna triangolare, e infine timbra due punti per l'occhio.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(3)

def fish(x, y, size):
    # body: a pointed oval made of two arcs
    monty.penup()
    monty.goto(x, y)          # nose of the fish
    monty.setheading(-60)
    monty.pendown()
    monty.color('midnightblue', 'steelblue')
    monty.begin_fill()
    monty.circle(size, 120)   # belly arc
    monty.left(60)
    monty.circle(size, 120)   # back arc
    monty.end_fill()
    # tail fin: a triangle at the back
    monty.penup()
    monty.goto(x + size * 1.73, y)
    monty.pendown()
    monty.begin_fill()
    monty.goto(x + size * 2.3, y + size * 0.5)
    monty.goto(x + size * 2.3, y - size * 0.5)
    monty.goto(x + size * 1.73, y)
    monty.end_fill()
    # eye near the nose
    monty.penup()
    monty.goto(x + size * 0.5, y + size * 0.15)
    monty.dot(size // 3, 'white')
    monty.dot(size // 6, 'black')

for _ in range(12):
    x = random.randint(-180, 60)
    y = random.randint(-160, 160)
    size = random.randint(15, 45)
    fish(x, y, size)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il corpo è disegnato con **due** archi `monty.circle(size, 120)`.
    Il corpo finito sarà un cerchio completo, un semicerchio, o un ovale a punta?
    Fai la tua previsione, poi eseguilo per scoprirlo!

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(3)

def fish(x, y, size):
    # body: a pointed oval made of two arcs
    monty.penup()
    monty.goto(x, y)          # nose of the fish
    monty.setheading(-60)
    monty.pendown()
    monty.color('midnightblue', 'steelblue')
    monty.begin_fill()
    monty.circle(size, 120)   # belly arc
    monty.left(60)
    monty.circle(size, 120)   # back arc
    monty.end_fill()
    # tail fin: a triangle at the back
    monty.penup()
    monty.goto(x + size * 1.73, y)
    monty.pendown()
    monty.begin_fill()
    monty.goto(x + size * 2.3, y + size * 0.5)
    monty.goto(x + size * 2.3, y - size * 0.5)
    monty.goto(x + size * 1.73, y)
    monty.end_fill()
    # eye near the nose
    monty.penup()
    monty.goto(x + size * 0.5, y + size * 0.15)
    monty.dot(size // 3, 'white')
    monty.dot(size // 6, 'black')

for _ in range(12):
    x = random.randint(-180, 60)
    y = random.randint(-160, 160)
    size = random.randint(15, 45)
    fish(x, y, size)`);
</script>

I due archi si incontrano in punte nette al naso e alla coda — un **ovale a punta**, esattamente
la forma giusta per il corpo di un pesce. Avevi indovinato?

## Come Funziona

Ogni chiamata a `circle(size, 120)` disegna un arco di 120° — un lato curvo del corpo. La tartaruga
inizia al naso puntando a `-60` gradi così il primo arco si curva verso il basso lungo la pancia e
atterra esattamente sul punto della coda. `left(60)` punta la tartaruga per il secondo arco, che si curva
verso l'alto lungo il dorso e ritorna esattamente al naso. Due archi, una forma chiusa.

La pinna caudale è un triangolo disegnato con tre chiamate a `goto()`: dal punto della coda verso due
angoli dietro il pesce e ritorno. Poiché si trova tra `begin_fill()` ed `end_fill()`,
viene fuori solida.

Infine, `dot()` disegna un cerchio riempito alla posizione della tartaruga — un grande punto bianco con
un punto nero più piccolo sopra fa un semplice occhio. L'occhio è ciò che fa sembrare vivo il pesce!

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.setheading(-60)` | Punta la tartaruga così il primo arco si curva lungo la pancia |
| `monty.circle(size, 120)` | Disegna un arco di 120° — un lato curvo del corpo |
| `monty.left(60)` | Gira al punto della coda così il secondo arco si curva indietro lungo la parte superiore |
| Tre chiamate `monty.goto(...)` | Disegna la pinna caudale triangolare dietro il corpo |
| `monty.dot(size // 3, 'white')` | Timbra il bianco dell'occhio vicino al naso |
| `random.randint(15, 45)` | Dimensione casuale per ogni pesce |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Colora Ogni Pesce Diversamente"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Tutti i pesci sono dello stesso `'steelblue'`. Aggiungi un parametro `color` a `fish()` e usalo
    per riempire ogni pesce con un colore casuale da una lista. Aggiorna la definizione della funzione e la chiamata.

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(3)

fish_colors = ['steelblue','royalblue','teal','cornflowerblue','deepskyblue']

def fish(x, y, size, color):
    # body: a pointed oval made of two arcs
    monty.penup()
    monty.goto(x, y)          # nose of the fish
    monty.setheading(-60)
    monty.pendown()
    monty.color('midnightblue', color)
    monty.begin_fill()
    monty.circle(size, 120)   # belly arc
    monty.left(60)
    monty.circle(size, 120)   # back arc
    monty.end_fill()
    # tail fin: a triangle at the back
    monty.penup()
    monty.goto(x + size * 1.73, y)
    monty.pendown()
    monty.begin_fill()
    monty.goto(x + size * 2.3, y + size * 0.5)
    monty.goto(x + size * 2.3, y - size * 0.5)
    monty.goto(x + size * 1.73, y)
    monty.end_fill()
    # eye near the nose
    monty.penup()
    monty.goto(x + size * 0.5, y + size * 0.15)
    monty.dot(size // 3, 'white')
    monty.dot(size // 6, 'black')

for _ in range(12):
    x = random.randint(-180, 60)
    y = random.randint(-160, 160)
    size = random.randint(15, 45)
    c = random.choice(fish_colors)
    fish(x, y, size, c)`);
</script>

Il `fish()` aggiornato prende `color` come quarto argomento e lo passa a `monty.color()` come
colore di riempimento, mentre il contorno resta `'midnightblue'`.

## Esperimenti

1. **Aggiungi uno sfondo blu.** Prima del ciclo, disegna un grande rettangolo riempito azzurro chiaro come l'oceano. Saprai che ha funzionato quando i pesci nuotano contro uno sfondo blu.

2. **Fai un singolo pesce gigante.** Rimuovi il ciclo e chiama `fish(-100, 0, 80)` direttamente. Saprai che ha funzionato quando un grande pesce riempie il canvas.

3. **Aggiungi una pinna dorsale.** Dentro `fish()`, dopo la pinna caudale, disegna un piccolo triangolo sopra il corpo: `goto(x + size * 0.6, y + size * 0.4)`, poi riempi un triangolo attraverso `(x + size * 0.85, y + size * 0.85)` e `(x + size * 1.2, y + size * 0.4)`. Saprai che ha funzionato quando ogni pesce ha una pinna sul dorso.

4. **Fai crescere il banco.** Cambia `range(12)` in `range(25)`. Saprai che ha funzionato quando l'acqua diventa affollata — qualche pesce si sovrappone?

!!! mascot-celebration "Lavoro Splendido!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un'intera scena sottomarina da una funzione chiamata 12 volte!
    Una funzione, infinita variazione — questa è la magia del codice parametrizzato.
    Prossimo: **Catena Montuosa** — stratificare forme per creare profondità.
