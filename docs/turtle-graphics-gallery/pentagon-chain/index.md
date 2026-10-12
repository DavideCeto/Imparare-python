---
hide:
    - toc
---
# Catena di Pentagoni

Alla fine di questo laboratorio sarai in grado di:

- Calcolare l'angolo esterno di qualsiasi poligono regolare con `360 / sides`
- Posizionare forme in una riga orizzontale facendo avanzare la tartaruga tra di esse
- Usare `begin_fill()` e `end_fill()` con due colori alternati

Dieci pentagoni marciano in riga, alternando viola e oro —
un braccialetto di tessere a cinque lati che si estende attraverso il canvas.

!!! mascot-welcome "Benvenuto alla Catena di Pentagoni!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio imparerai l'unica formula che disegna qualsiasi poligono regolare,
    poi ne concatenerai 10 in fila. Programmiamo insieme!

## Come Funziona la Catena

Un **poligono regolare** con `n` lati ha bisogno di un angolo esterno di `360 / n` gradi a ogni angolo.
Per un pentagono (5 lati): `360 / 5 = 72°`.

Dopo aver disegnato ogni pentagono, la tartaruga è tornata all'angolo di partenza.
Muovendosi avanti di `size` passi si posiziona la tartaruga all'angolo di partenza del pentagono successivo.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['purple', 'gold']
sides = 5
size = 60
angle = 360 / sides

monty.penup()
monty.goto(-270, 0)
monty.pendown()

for i in range(10):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for _ in range(sides):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()
    monty.forward(size)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    L'angolo esterno di un pentagono è 72°. Dopo aver disegnato tutti i 5 lati, quanti gradi totali
    ha girato Monty? (Suggerimento: 5 × 72° = ?)
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

colors = ['purple', 'gold']
sides = 5
size = 60
angle = 360 / sides

monty.penup()
monty.goto(-270, 0)
monty.pendown()

for i in range(10):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for _ in range(sides):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()
    monty.forward(size)`);
</script>

5 × 72° = **360°** — una rotazione completa. Questo è il motivo per cui la tartaruga finisce sempre rivolta nella stessa direzione dopo qualsiasi poligono regolare. Avevi indovinato?

## Come Funziona

Il ciclo interno `for _ in range(sides)` disegna un pentagono. Dopo ogni lato, `right(angle)` ruota dell'angolo esterno. Dopo tutti i 5 lati, la tartaruga è tornata all'inizio rivolta nella direzione originale.

`monty.forward(size)` dopo `end_fill()` fa avanzare la tartaruga esattamente di una lunghezza di lato, posizionandola al primo angolo del pentagono successivo — così la catena si collega angolo per angolo.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `angle = 360 / sides` | Formula dell'angolo esterno — funziona per qualsiasi poligono regolare |
| `monty.goto(-270, 0)` | Inizia vicino al bordo sinistro |
| `for _ in range(sides)` | Disegna un lato + una rotazione, ripetuta `sides` volte |
| `monty.end_fill()` | Riempie il pentagono completato |
| `monty.forward(size)` | Avanza verso l'angolo di partenza del pentagono successivo |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Crea una Catena di Esagoni"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia il codice sotto per disegnare una catena di **esagoni** (6 lati) invece di pentagoni.
    Dovrai aggiornare `sides` e potresti voler ridurre leggermente `size` per far entrare 8 esagoni.

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

colors = ['purple', 'gold']
sides = 5
size = 60
angle = 360 / sides

monty.penup()
monty.goto(-270, 0)
monty.pendown()

for i in range(10):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for _ in range(sides):
        monty.forward(size)
        monty.right(angle)
    monty.end_fill()
    monty.forward(size)`);
</script>

Cambia `sides = 5` in `sides = 6`. L'angolo si aggiorna automaticamente a `360 / 6 = 60°`.

## Esperimenti

1. **Prova i quadrati.** Cambia `sides = 4` e `size = 50`. Otto quadrati si concateneranno attraverso il canvas. Saprai che ha funzionato quando vedi una riga di quadrati colorati.

2. **Usa tre colori.** Cambia `colors` in `['purple', 'gold', 'crimson']` e `i % 2` in `i % 3`. Saprai che ha funzionato quando tre colori scorrono attraverso la catena.

3. **Crea una catena verticale.** Dopo `monty.goto(-270, 0)`, aggiungi `monty.setheading(90)`. La catena marcerà verso l'alto. Saprai che ha funzionato quando i pentagoni si impilano verticalmente.

4. **Cambia il numero di pentagoni.** Sostituisci `range(10)` con `range(6)`. Adatta la posizione x di partenza così la catena più corta sia ancora centrata. Saprai che ha funzionato quando 6 pentagoni appaiono centrati sul canvas.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato la formula dell'angolo esterno `360 / sides` — la chiave per disegnare
    qualsiasi poligono regolare in Python. Cambia un numero, cambia tutta la forma!
    Prossimo: **Quadrati Sovrapposti** per esplorare l'ordine di disegno e gli effetti di trasparenza.
