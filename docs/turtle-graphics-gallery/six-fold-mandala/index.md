---
hide:
    - toc
---
# Mandala a Simmetria Sestupla

Alla fine di questo laboratorio sarai in grado di:

- Disegnare una sezione di un mandala e stamparla sei volte ruotando di 60° tra ognuna
- Costruire pattern simmetrici complessi da una semplice unità ripetuta
- Capire come la rotazione `360 / 6 = 60°` crea simmetria a sei pieghe

Dodici anelli concentrici di petali, archi, e diamanti — tutti generati disegnando un sesto del design e ruotandolo sei volte. Cambia un dettaglio e tutte le sei sezioni si aggiornano istantaneamente.

!!! mascot-welcome "Benvenuto al Mandala a Simmetria Sestupla!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I mandala sono antiche forme d'arte basate sulla simmetria radiale. In questo laboratorio
    lo programmerai da zero usando una singola funzione ripetuta!
    Programmiamo insieme!

## Come Funziona

`mandala_section()` disegna un sesto del design dal centro verso l'esterno — un petalo, poi un arco, poi una forma a diamante. Il ciclo esterno la chiama sei volte, ruotando di 60° ogni volta.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 60)
    monty.left(120)
    monty.circle(size, 60)
    monty.left(120)
    monty.end_fill()

def mandala_section():
    for i, r in enumerate([30, 50, 70, 90]):
        color = ['crimson', 'darkorange', 'gold', 'royalblue'][i]
        petal(r, color)
        monty.penup()
        monty.goto(0, 0)
        monty.setheading(monty.heading())
        monty.pendown()

for i in range(6):
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(i * 60)
    monty.pendown()
    mandala_section()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Disegniamo 4 petali per sezione e 6 sezioni — quanti petali in totale?
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

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 60)
    monty.left(120)
    monty.circle(size, 60)
    monty.left(120)
    monty.end_fill()

def mandala_section():
    for i, r in enumerate([30, 50, 70, 90]):
        color = ['crimson', 'darkorange', 'gold', 'royalblue'][i]
        petal(r, color)
        monty.penup()
        monty.goto(0, 0)
        monty.setheading(monty.heading())
        monty.pendown()

for i in range(6):
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(i * 60)
    monty.pendown()
    mandala_section()`);
</script>

`4 × 6 = 24` petali — disposti in quattro anelli concentrici di sei, ognuno di un colore diverso. Avevi indovinato?

## Come Funziona

`petal(size, color)` disegna una forma a lente disegnando due archi di 60°. La tartaruga inizia e finisce al centro ogni volta perché `goto(0, 0)` riposiziona dopo ogni petalo. `setheading(i * 60)` prima di ogni rotazione di sezione assicura che tutte le sezioni partano dal medesimo offset angolare.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.circle(size, 60)` | Disegna un arco di 60° — un lato della lente del petalo |
| `monty.left(120)` | Gira di 120° per disegnare l'arco di ritorno |
| `monty.goto(0, 0)` | Ritorna al centro tra i petali |
| `setheading(i * 60)` | Ruota di 60° prima di ogni sezione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia a 8 Pieghe"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `range(6)` in `range(8)` e `i * 60` in `i * 45`.
    La simmetria a 8 pieghe appare nei lavori di piastrelle islamiche e nei fiocchi di neve.
    Prevedi come cambierà il mandala — poi eseguilo!

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

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 45)
    monty.left(135)
    monty.circle(size, 45)
    monty.left(135)
    monty.end_fill()

def mandala_section():
    for i, r in enumerate([30, 50, 70, 90]):
        color = ['crimson', 'darkorange', 'gold', 'royalblue'][i]
        petal(r, color)
        monty.penup()
        monty.goto(0, 0)
        monty.setheading(monty.heading())
        monty.pendown()

for i in range(8):
    monty.penup()
    monty.goto(0, 0)
    monty.setheading(i * 45)
    monty.pendown()
    mandala_section()`);
</script>

La simmetria a 8 pieghe produce `4 × 8 = 32` petali — le sezioni sono più strette e si compattano più strettamente attorno al centro.

## Esperimenti

1. **Cambia i colori dei petali.** Sostituisci la lista dei colori con `['navy', 'royalblue', 'deepskyblue', 'lightcyan']`. Saprai che ha funzionato quando il mandala diventa blu.

2. **Anello esterno più grande.** Cambia `[30, 50, 70, 90]` in `[30, 55, 85, 120]`. Saprai che ha funzionato quando i petali più esterni sono più grandi.

3. **Aggiungi un punto centrale.** Dopo il ciclo, aggiungi `monty.penup(); monty.goto(0, -15); monty.dot(30, 'gold')`. Saprai che ha funzionato quando un cerchio dorato riempie il centro.

4. **Prova la simmetria a 12 pieghe.** Cambia in `range(12)` e `i * 30`. Saprai che ha funzionato quando appaiono 12 sezioni, facendo un mandala molto denso.

!!! mascot-celebration "Mandala Completato!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai creato un mandala da una funzione ripetuta 6 volte!
    Qualsiasi cambiamento a `mandala_section()` aggiorna automaticamente tutte le sei sezioni.
    Prossimo: **Farfalla a Specchio** — simmetria bilaterale tramite negazione delle coordinate.
