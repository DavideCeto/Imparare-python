# Rispondere ai Click del Mouse

Alla fine di questa lezione sarai in grado di:

- Registrare una funzione come gestore di click usando `screen.onscreenclick()`
- Usare gli argomenti `x` e `y` che il tuo gestore riceve per disegnare nella posizione del click
- Costruire un programma che risponde all'utente in tempo reale

Ogni programma fin qui gira dall'inizio alla fine e poi si ferma. I **programmi guidati da eventi** sono diversi — impostano una funzione gestore e poi *aspettano*. Quando l'utente clicca sul canvas, il gestore viene chiamato con le coordinate esatte del click. Il tuo codice poi decide cosa disegnare lì.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Clicca ovunque sul canvas e appare una forma — questo è un programma guidato da eventi!
    Oggi farai rispondere Monty a dove clicchi. Programmiamo insieme!

## Gestori di Eventi

Un **gestore di eventi** è una funzione che scrivi e poi *registri* con lo schermo. Python la chiama automaticamente ogni volta che l'evento accade — non la chiami tu stesso:

```python
def on_click(x, y):
    # x e y sono il punto in cui l'utente ha cliccato
    monty.goto(x, y)
    monty.circle(15)

screen = turtle.Screen()
screen.onscreenclick(on_click)
```

`screen.onscreenclick(on_click)` dice a Python: "quando qualcuno clicca sul canvas, chiama `on_click` con le coordinate del click." La tua funzione riceve `x` e `y` automaticamente.

## Codice di Esempio

```python
import turtle

screen = turtle.Screen()
screen.bgcolor('lightyellow')
screen.title("Clicca per disegnare!")

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)
monty.penup()

colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink']
click_count = [0]

def on_click(x, y):
    color = colors[click_count[0] % len(colors)]
    monty.color(color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    click_count[0] += 1

screen.onscreenclick(on_click)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Dopo aver cliccato Esegui, il canvas aspetta i tuoi click.
    Ogni click disegna un cerchio in quella posizione. Cosa pensi succeda al colore ogni volta che clicchi?
    Fai la tua previsione — poi clicca Esegui e prova a cliccare sul canvas!

## Provalo Ora

Clicca **Esegui**, poi clicca ovunque sul canvas di disegno per posizionare un cerchio lì.
Nessun account necessario — tutto gira nel tuo browser.

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

screen = turtle.Screen()
screen.bgcolor('lightyellow')

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)
monty.penup()

colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink']
click_count = [0]

def on_click(x, y):
    color = colors[click_count[0] % len(colors)]
    monty.color(color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    click_count[0] += 1

screen.onscreenclick(on_click)`);
</script>

Avevi indovinato? Ogni click disegna un cerchio riempito esattamente in quel punto, scorrendo attraverso rosso, arancione, verde, blu, viola, e rosa — il colore avanza con ogni click.

## Come Funziona

`screen.onscreenclick(on_click)` registra la tua funzione. Ogni volta che il canvas viene cliccato, Python chiama `on_click(x, y)` con le coordinate in pixel del click. La tua funzione poi va a quella posizione e disegna.

`click_count` è memorizzato come una **lista con un elemento** (`[0]`) invece che una variabile semplice. Questo è un trucco di scoping di Python: le variabili semplici dentro una funzione annidata non possono essere aggiornate direttamente — ma gli elementi di una lista sì. `click_count[0] += 1` incrementa il contatore in modo sicuro.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `screen = turtle.Screen()` | Ottiene un riferimento alla finestra di disegno |
| `screen.onscreenclick(on_click)` | Registra `on_click` come la funzione da chiamare a ogni click sul canvas |
| `def on_click(x, y):` | Il gestore — `x` e `y` sono forniti automaticamente dallo schermo |
| `click_count = [0]` | Un contatore memorizzato in una lista così può essere aggiornato dentro il gestore |
| `click_count[0] % len(colors)` | Scorre la lista dei colori a ogni click |

!!! mascot-tip "La x, y Arrivano Gratis"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Non chiami mai `on_click()` tu stesso — lo schermo la chiama per te e compila `x` e `y`
    automaticamente. Il tuo compito è solo decidere cosa disegnare in quelle coordinate!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Disegna Stelle Invece di Cerchi"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna un cerchio a ogni click. Cambia il codice di disegno dentro `on_click`
    così disegna una **stella a cinque punte** nella posizione del click invece.
    Suggerimento: una stella usa `for i in range(5): forward(30); right(144)`.

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

screen = turtle.Screen()
screen.bgcolor('navy')

monty = turtle.Turtle()
monty.speed(10)
monty.penup()

colors = ['yellow', 'gold', 'white', 'orange', 'cyan']
click_count = [0]

def on_click(x, y):
    color = colors[click_count[0] % len(colors)]
    monty.color(color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    # Trasforma questo cerchio in una stella a 5 punte
    # (for i in range(5): forward(30); right(144))
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    click_count[0] += 1

screen.onscreenclick(on_click)`);
</script>

## Esperimenti

Prova questi cambiamenti al codice del click-per-disegnare. Prevedi prima, poi prova!

1. Cambia `monty.circle(20)` in `monty.circle(random.randint(10, 40))` (aggiungi `import random` in cima).
   **Saprai che ha funzionato quando** ogni click produce un cerchio di dimensione casuale.

2. Cambia `screen.bgcolor('lightyellow')` in `screen.bgcolor('black')` e aggiungi colori brillanti alla lista.
   **Saprai che ha funzionato quando** i cerchi sembrano bolle colorate su uno sfondo scuro.

3. Dopo che `on_click` gira, aggiungi `monty.write(str(click_count[0]), font=("Arial", 12, "normal"))` per numerare ogni cerchio.
   **Saprai che ha funzionato quando** un numero appare vicino a ogni cerchio mostrando l'ordine in cui è stato cliccato.

4. Cambia `monty.circle(20)` in un piccolo poligono: `for i in range(6): monty.forward(20); monty.right(60)`.
   **Saprai che ha funzionato quando** cliccare posiziona esagoni invece di cerchi.

5. Aggiungi `if click_count[0] >= 5: return` all'inizio di `on_click` per limitare i click a 5.
   **Saprai che ha funzionato quando** i click dopo il quinto non hanno nessun effetto.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scritto un programma guidato da eventi — lo stesso pattern usato in ogni bottone, menu, e
    gioco nel mondo. Ogni click, tap, e pressione di tasto funziona esattamente così sotto il cofano!
    Programmiamo insieme!
