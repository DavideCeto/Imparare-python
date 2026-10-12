---
hide:
    - toc
---
# Collezione di Fiocchi di Neve di Lindenmayer

Alla fine di questo laboratorio sarai in grado di:

- Costruire una libreria di diversi insiemi di regole del sistema-L e disegnarli in una griglia
- Confrontare come regole diverse producono forme di fiocchi di neve e frattali visivamente distinte
- Capire come lo stesso interprete produce risultati completamente diversi da regole diverse

Sei diversi fiocchi di neve a sistema-L mostrati in una griglia 2×3 — curva di Koch, punta di freccia di Sierpiński, garza esagonale, cristallo, Koch quadratico, e dragone. Stesso interprete, sei insiemi di regole completamente diversi.

!!! mascot-welcome "Benvenuto alla Collezione di Fiocchi di Neve!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Lo stesso interprete del sistema-L disegna pattern completamente diversi
    solo cambiando le regole. Questo è il potere del design guidato dai dati!
    Costruiamo una collezione di sei fiocchi di neve!

## Come Funziona

Una funzione `lsystem(axiom, rules, depth)` espande la stringa assioma. Una funzione `draw_lsystem(sentence, step, angle, x, y, heading)` la interpreta e la disegna. Sei diverse combinazioni `(axiom, rules, angle, depth)` riempiono una griglia.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def expand(axiom, rules, depth):
    s = axiom
    for _ in range(depth):
        s = ''.join(rules.get(c, c) for c in s)
    return s

def draw(sentence, step, angle, x, y, heading):
    stack = []
    monty.penup(); monty.goto(x, y)
    monty.setheading(heading); monty.pendown()
    for c in sentence:
        if c in 'FG':
            monty.forward(step)
        elif c == '+':
            monty.left(angle)
        elif c == '-':
            monty.right(angle)
        elif c == '[':
            stack.append((monty.pos(), monty.heading()))
        elif c == ']':
            p, h = stack.pop()
            monty.penup(); monty.goto(p)
            monty.setheading(h); monty.pendown()

systems = [
    ('F', {'F': 'F+F-F-F+F'}, 3, 90, 4),
    ('F-G-G', {'F': 'F-G+F+G-F', 'G': 'GG'}, 4, 120, 5),
    ('F++F++F', {'F': 'F-F++F-F'}, 4, 60, 5),
    ('X', {'X': 'X+YF+', 'Y': '-FX-Y'}, 10, 90, 4),
    ('F', {'F': 'F+F-F-FF+F+F-F'}, 2, 90, 3),
    ('F', {'F': 'F+F-F-F+F', 'G': 'GG'}, 3, 90, 4),
]

positions = [(-160, 0), (0, 0), (160, 0), (-160, -130), (0, -130), (160, -130)]
colors = ['royalblue', 'crimson', 'forestgreen', 'darkorange', 'purple', 'teal']
steps = [5, 4, 5, 5, 6, 5]

for i, (axiom, rules, depth, angle, _step) in enumerate(systems):
    sentence = expand(axiom, rules, depth)
    x, y = positions[i]
    monty.pencolor(colors[i])
    monty.pensize(1)
    draw(sentence, steps[i], angle, x, y, 0)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Sei insiemi di regole, sei angoli diversi (60° o 90°), sei profondità diverse.
    Ogni fiocco di neve sembrerà unico, o sembreranno tutti simili?
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

def expand(axiom, rules, depth):
    s = axiom
    for _ in range(depth):
        s = ''.join(rules.get(c, c) for c in s)
    return s

def draw(sentence, step, angle, x, y, heading):
    stack = []
    monty.penup(); monty.goto(x, y)
    monty.setheading(heading); monty.pendown()
    for c in sentence:
        if c in 'FG':
            monty.forward(step)
        elif c == '+':
            monty.left(angle)
        elif c == '-':
            monty.right(angle)
        elif c == '[':
            stack.append((monty.pos(), monty.heading()))
        elif c == ']':
            p, h = stack.pop()
            monty.penup(); monty.goto(p)
            monty.setheading(h); monty.pendown()

systems = [
    ('F', {'F': 'F+F-F-F+F'}, 3, 90, 4),
    ('F-G-G', {'F': 'F-G+F+G-F', 'G': 'GG'}, 4, 120, 5),
    ('F++F++F', {'F': 'F-F++F-F'}, 4, 60, 5),
    ('X', {'X': 'X+YF+', 'Y': '-FX-Y'}, 10, 90, 4),
    ('F+F+F+F', {'F': 'F-F+FF+F-F'}, 3, 90, 4),
    ('F', {'F': 'F[+F]F[-F]F'}, 4, 25, 6),
]

positions = [(-160, 40), (0, 40), (160, 40), (-160, -90), (0, -90), (160, -90)]
colors = ['royalblue', 'crimson', 'forestgreen', 'darkorange', 'purple', 'teal']
steps = [5, 4, 5, 5, 5, 3]

for i, (axiom, rules, depth, angle, _) in enumerate(systems):
    sentence = expand(axiom, rules, depth)
    x, y = positions[i]
    monty.pencolor(colors[i])
    monty.pensize(1)
    draw(sentence, steps[i], angle, x, y, 0)`);
</script>

**Sei forme completamente diverse** da sei insiemi di regole — curva di Koch, Sierpiński, esagonale, dragone, Koch quadratico, e una pianta. Stesso interprete, dati diversi. Avevi indovinato?

## Come Funziona

`''.join(rules.get(c, c) for c in s)` usa un'espressione generatrice per sostituire ogni carattere con la sua regola (o se stesso se non esiste una regola). Questo è un espansore del sistema-L in una riga. La funzione `draw()` è un interprete turtle universale per il sistema-L.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `''.join(rules.get(c,c) for c in s)` | Applicazione di un passo di regola |
| `if c in 'FG'` | Sia F sia G sono comandi avanti-disegna |
| `stack.append((pos, heading))` | Salva lo stato a `[` |
| `systems = [...]` | Ogni tupla: assioma, regole, profondità, angolo, inutilizzato |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Settimo Sistema"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi un settimo sistema-L alla lista usando le regole del fiocco di neve di Koch:
    `axiom = 'F--F--F'`, `rules = {'F': 'F+F--F+F'}`, `angle = 60`, `depth = 4`.
    Dove lo posizionerai? Prevedi come apparirà!

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def expand(axiom, rules, depth):
    s = axiom
    for _ in range(depth):
        s = ''.join(rules.get(c, c) for c in s)
    return s

def draw(sentence, step, angle, x, y, heading):
    stack = []
    monty.penup(); monty.goto(x, y)
    monty.setheading(heading); monty.pendown()
    for c in sentence:
        if c in 'FG':
            monty.forward(step)
        elif c == '+':
            monty.left(angle)
        elif c == '-':
            monty.right(angle)
        elif c == '[':
            stack.append((monty.pos(), monty.heading()))
        elif c == ']':
            p, h = stack.pop()
            monty.penup(); monty.goto(p)
            monty.setheading(h); monty.pendown()

monty.pencolor('teal')
monty.pensize(1)
sentence = expand('F--F--F', {'F': 'F+F--F+F'}, 4)
draw(sentence, 5, 60, -60, 30, 0)`);
</script>

Il fiocco di neve di Koch — uno dei frattali più famosi, prodotto da un'unica regola a due caratteri.

## Esperimenti

1. **Aumenta la profondità su un sistema.** Cambia la profondità di un sistema da 4 a 5. Saprai che ha funzionato quando quel frattale è più dettagliato (e impiega più tempo per essere disegnato).

2. **Colora per profondità.** In `draw()`, cambia il colore della penna ogni volta che viene chiamato `F` (scorrendo attraverso una tavolozza). Saprai che ha funzionato quando il frattale ha gradienti di colore.

3. **Cambia tutti gli angoli a 45.** Alcuni sistemi sembreranno drasticamente diversi, alcuni simili. Saprai che ha funzionato quando le forme cambiano a una geometria basata su 45°.

4. **Progetta la tua propria regola.** Inventa una nuova combinazione `(axiom, rules, angle)` e vedi cosa produce. Saprai che ha funzionato quando appare un nuovo pattern.

!!! mascot-celebration "Una Galleria di Frattali!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un motore universale per il sistema-L che disegna qualsiasi insieme di regole!
    Questo è il potere di separare i dati (regole) dall'algoritmo (interprete) —
    un programma, infinite uscite possibili.
    Prossimo: **Ciclo di Arte Generativa** — il gran finale!
