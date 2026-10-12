---
hide:
    - toc
---
# Scarabocchio a Simmetria Quadrupla

Alla fine di questo laboratorio sarai in grado di:

- Registrare comandi della tartaruga come dati in una lista e riprodurli
- Applicare una rotazione di 90° a una lista di movimenti registrati per creare simmetria quadrupla
- Capire la differenza tra registrare comandi ed eseguirli immediatamente

Un quadrante di uno scarabocchio geometrico è registrato, poi riprodotto altre tre volte con rotazioni di 90°, 180°, e 270° — producendo automaticamente una perfetta simmetria rotazionale quadrupla.

!!! mascot-welcome "Benvenuto allo Scarabocchio a Simmetria Quadrupla!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo laboratorio insegna un'idea di programmazione potente: **registrare le azioni come dati**.
    Disegna una volta, riproduci quattro volte con rotazioni diverse — simmetria istantanea!
    Programmiamo insieme!

## Come Funziona

Memorizziamo i movimenti come una lista di tuple: `('forward', 40)`, `('left', 60)`, ecc. Dopo aver costruito la lista, la riproduciamo quattro volte, ruotando di 90° tra ogni riproduzione. Questo garantisce una perfetta simmetria quadrupla indipendentemente dai movimenti presenti nella lista.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

moves = [
    ('forward', 50), ('left', 60), ('forward', 40), ('right', 90),
    ('forward', 30), ('left', 120), ('forward', 50), ('left', 90),
    ('forward', 40), ('right', 60), ('forward', 60),
]

colors = ['crimson', 'royalblue', 'forestgreen', 'darkorange']

for rotation in range(4):
    monty.pencolor(colors[rotation])
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(rotation * 90)
    monty.pendown()
    for cmd, val in moves:
        if cmd == 'forward':
            monty.forward(val)
        elif cmd == 'left':
            monty.left(val)
        elif cmd == 'right':
            monty.right(val)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ognuna delle 4 riproduzioni inizia rivolta in una direzione diversa: 0°, 90°, 180°, 270°.
    Le quattro riproduzioni colorate sembreranno quattro scarabocchi indipendenti, o formeranno un pattern simmetrico?
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

moves = [
    ('forward', 50), ('left', 60), ('forward', 40), ('right', 90),
    ('forward', 30), ('left', 120), ('forward', 50), ('left', 90),
    ('forward', 40), ('right', 60), ('forward', 60),
]

colors = ['crimson', 'royalblue', 'forestgreen', 'darkorange']

for rotation in range(4):
    monty.pencolor(colors[rotation])
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(rotation * 90)
    monty.pendown()
    for cmd, val in moves:
        if cmd == 'forward':
            monty.forward(val)
        elif cmd == 'left':
            monty.left(val)
        elif cmd == 'right':
            monty.right(val)`);
</script>

Un **pattern simmetrico** — i quattro bracci colorati sono rotazioni l'uno dell'altro, incontrandosi al centro per formare un design coerente. Avevi indovinato?

## Come Funziona

`monty.setheading(rotation * 90)` è la chiave. Prima di ogni riproduzione, la tartaruga viene inviata all'origine rivolta in una nuova direzione. Dal punto di vista della tartaruga, ogni riproduzione sembra identica — ma poiché la direzione di partenza ruota, anche il risultato ruota.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `moves = [...]` | Registra i comandi come una lista di tuple (comando, valore) |
| `monty.setheading(rotation * 90)` | Ruota la direzione iniziale per ogni riproduzione |
| `for cmd, val in moves` | Spacchetta ogni movimento registrato |
| `colors[rotation]` | Colore diverso per ogni rotazione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi Più Movimenti"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi 3 movimenti in più alla lista `moves` — qualsiasi combinazione di avanti/sinistra/destra.
    Prevedi come cambierà la simmetria (resterà quadrupla!), poi eseguila.

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

moves = [
    ('forward', 50), ('left', 60), ('forward', 40), ('right', 90),
    ('forward', 30), ('left', 120), ('forward', 50), ('left', 90),
    ('forward', 40), ('right', 60), ('forward', 60),
    ('left', 45), ('forward', 35), ('right', 90), ('forward', 25),
]

colors = ['crimson', 'royalblue', 'forestgreen', 'darkorange']

for rotation in range(4):
    monty.pencolor(colors[rotation])
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(rotation * 90)
    monty.pendown()
    for cmd, val in moves:
        if cmd == 'forward':
            monty.forward(val)
        elif cmd == 'left':
            monty.left(val)
        elif cmd == 'right':
            monty.right(val)`);
</script>

Non importa cosa metti in `moves`, il risultato è sempre a simmetria quadrupla — il meccanismo di rotazione lo garantisce.

## Esperimenti

1. **Simmetria a sei pieghe.** Cambia `range(4)` in `range(6)` e `rotation * 90` in `rotation * 60`. Saprai che ha funzionato quando appaiono 6 bracci.

2. **Monocromo.** Usa `'black'` per tutti i colori. Saprai che ha funzionato quando tutti i bracci sono dello stesso colore, rendendo la simmetria ancora più evidente.

3. **Disegna con penna alzata a metà.** Aggiungi voci `('penup', 0)` e `('pendown', 0)` e gestiscile nel ciclo di riproduzione. Saprai che ha funzionato quando alcuni movimenti creano trattini.

4. **Movimenti casuali.** Genera movimenti con `random.choice` e `random.randint`. Saprai che ha funzionato quando appare un pattern simmetrico diverso a ogni esecuzione.

!!! mascot-celebration "Comandi come Dati!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato un'idea potente: memorizzare azioni come dati così puoi riprodurle
    con trasformazioni. Questa tecnica è usata nei sistemi di annulla/ripeti e nell'animazione!
    Prossimo: **Mandala a Simmetria Sestupla** — estendendo a simmetria a 6 pieghe.
