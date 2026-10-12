---
hide:
    - toc
---
# Pianta a Sistema-L

Alla fine di questo laboratorio sarai in grado di:

- Applicare regole del sistema di Lindenmayer (sistema-L) per espandere una stringa su più generazioni
- Interpretare una stringa del sistema-L come comandi di disegno della tartaruga: `F` = avanti, `+/-` = gira, `[/]` = ramifica
- Capire come `[` e `]` implementano uno stack di posizione per creare strutture ramificate

Una pianta a sistema-L cresce da una stringa seme di un carattere. Applicare le regole di riscrittura per 5 generazioni produce una lunga stringa di comandi della tartaruga che disegna una pianta realistica con rami, foglie, e steli.

!!! mascot-welcome "Benvenuto alla Pianta a Sistema-L!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nel 1968, il biologo Aristid Lindenmayer inventò i sistemi-L per modellare come crescono le piante.
    L'idea fondamentale: una breve stringa di regole si espande in strutture ramificate complesse!
    Programmiamone uno insieme!

## Come Funziona

Inizia con l'assioma `"F"`. Applica le regole `{'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}` per 5 generazioni. Interpreta il risultato: `F`=avanti, `+`=sinistra 25°, `-`=destra 25°, `[`=salva lo stato, `]`=ripristina lo stato.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
axiom = 'X'
sentence = axiom

for _ in range(5):
    new_sentence = ''
    for ch in sentence:
        new_sentence += rules.get(ch, ch)
    sentence = new_sentence

stack = []
monty.penup()
monty.goto(0, -150)
monty.setheading(90)
monty.pendown()
monty.pencolor('saddlebrown')
step = 3
angle = 25

for ch in sentence:
    if ch == 'F':
        monty.pencolor('saddlebrown')
        monty.forward(step)
    elif ch == '+':
        monty.left(angle)
    elif ch == '-':
        monty.right(angle)
    elif ch == '[':
        stack.append((monty.pos(), monty.heading()))
    elif ch == ']':
        pos, heading = stack.pop()
        monty.penup()
        monty.goto(pos)
        monty.setheading(heading)
        monty.pendown()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Le regole del sistema-L si espandono per 5 generazioni. Una breve regola produce una lunga stringa.
    Il risultato sembrerà un pattern geometrico, o una pianta vera?
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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
axiom = 'X'
sentence = axiom

for _ in range(5):
    new_sentence = ''
    for ch in sentence:
        new_sentence += rules.get(ch, ch)
    sentence = new_sentence

stack = []
monty.penup()
monty.goto(0, -150)
monty.setheading(90)
monty.pendown()
step = 3
angle = 25

for ch in sentence:
    if ch == 'F':
        monty.pencolor('saddlebrown')
        monty.forward(step)
    elif ch == '+':
        monty.left(angle)
    elif ch == '-':
        monty.right(angle)
    elif ch == '[':
        stack.append((monty.pos(), monty.heading()))
    elif ch == ']':
        pos, heading = stack.pop()
        monty.penup()
        monty.goto(pos)
        monty.setheading(heading)
        monty.pendown()`);
</script>

Una **pianta ramificata** — le regole producono una struttura botanica simile a un frattale con un tronco centrale e rami annidati. Avevi indovinato?

## Come Funziona

`[` salva la posizione e la direzione attuali della tartaruga in uno stack. `]` le ripristina, riportando la tartaruga dove si è ramificata. Questo approccio basato su stack è come funzionano tutti i sistemi-L ramificati — nessuna ricorsione necessaria!

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `rules.get(ch, ch)` | Se non c'è regola per `ch`, lascialo invariato |
| `stack.append((pos, heading))` | Salva lo stato della tartaruga al punto di ramificazione |
| `stack.pop()` | Ripristina lo stato della tartaruga dopo il sotto-ramo |
| `for _ in range(5)` | 5 generazioni di applicazione della regola |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia l'Angolo"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `angle = 25` in `angle = 40`. La pianta sembrerà più larga, più stretta, o uguale?
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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

rules = {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}
axiom = 'X'
sentence = axiom

for _ in range(5):
    new_sentence = ''
    for ch in sentence:
        new_sentence += rules.get(ch, ch)
    sentence = new_sentence

stack = []
monty.penup()
monty.goto(0, -150)
monty.setheading(90)
monty.pendown()
step = 3
angle = 40

for ch in sentence:
    if ch == 'F':
        monty.pencolor('saddlebrown')
        monty.forward(step)
    elif ch == '+':
        monty.left(angle)
    elif ch == '-':
        monty.right(angle)
    elif ch == '[':
        stack.append((monty.pos(), monty.heading()))
    elif ch == ']':
        pos, heading = stack.pop()
        monty.penup()
        monty.goto(pos)
        monty.setheading(heading)
        monty.pendown()`);
</script>

A 40°, la pianta è **più larga** — i rami si estendono più lontano dall'asse centrale, creando un aspetto più cespuglioso.

## Esperimenti

1. **Prova 4 generazioni.** Cambia `range(5)` in `range(4)`. Saprai che ha funzionato quando appare una pianta più piccola e più semplice.

2. **Usa il verde per le foglie.** Dopo aver disegnato ogni `F`, controlla se il carattere successivo è `X` e colora quel segmento verde. Saprai che ha funzionato quando i rami delle foglie sono verdi.

3. **Prova un sistema-L diverso.** Cambia le regole in `{'F': 'F[+F]F[-F][F]'}` con `axiom = 'F'` e `range(4)`. Saprai che ha funzionato quando appare una forma di pianta completamente diversa.

4. **Varia il passo in base alla profondità.** Traccia quante parentesi `[` sono aperte e usa `step / (depth + 1)`. Saprai che ha funzionato quando i rami più profondi sono più corti, come un vero albero.

!!! mascot-celebration "Una Foresta di Regole!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai implementato un sistema di Lindenmayer — uno dei modelli più potenti della crescita biologica!
    I sistemi-L generano anche curve di Koch, triangoli di Sierpiński, e molti altri frattali.
    Prossimo: **Generatore di Labirinti con la Turtle** — labirinto ricorsivo con scavo dei muri.
