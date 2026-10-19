---
title: Turtle Avanzata e Programmazione Guidata da Eventi
description: Costruisci programmi interattivi con gli eventi onscreenclick, onkey, e timer della turtle — e capisci il modello di programmazione guidata da eventi
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:50:00
version: 0.09
---

# Turtle Avanzata e Programmazione Guidata da Eventi

Alla fine di questa lezione sarai in grado di:

- Spiegare il **modello di programmazione guidata da eventi** e come differisce dai programmi sequenziali
- Usare `turtle.onscreenclick()` per rispondere ai clic del mouse
- Usare `turtle.onkey()` e `turtle.listen()` per rispondere alla pressione dei tasti
- Usare `turtle.ontimer()` per creare cicli di animazione ripetuti
- Costruire un piccolo programma di disegno interattivo usando gli eventi

Ogni gioco, app, e sito web usa la **programmazione guidata da eventi** — codice che aspetta che succeda qualcosa (un clic, una pressione di tasto, un timer) e poi risponde. Questo capitolo ti insegna come costruire programmi che reagiscono in tempo reale.

!!! mascot-welcome "Benvenuto/a al Capitolo 35!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    È qui che i tuoi programmi iniziano a sentirsi vivi — rispondendo al tuo mouse e alla tastiera in tempo reale!
    La programmazione guidata da eventi è la base di ogni gioco e app interattiva.
    Facciamo muovere le cose! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Modello Guidato da Eventi

Nei **programmi sequenziali**, il codice gira dall'alto verso il basso — ogni riga si esegue dopo che la precedente finisce.

Nei **programmi guidati da eventi**, il programma avvia un **ciclo di eventi** (event loop) che aspetta e osserva.
Quando si verifica un **evento** (clic del mouse, pressione di un tasto, scatto di un timer), il ciclo chiama una **funzione di callback** che hai registrato per quell'evento.

```
[Register callbacks]  →  [Start event loop]  →  [Wait]
                                                  ↓
                                           [Event occurs]
                                                  ↓
                                       [Call the callback]
                                                  ↓
                                               [Wait]
```

Non controlli *quando* scattano gli eventi — scrivi solo le funzioni che li gestiscono.

## Tre Concetti Chiave

Prima di scrivere codice turtle interattivo, ecco tre termini che vedrai in tutto questo capitolo:

- **Evento** — qualcosa che succede: un clic del mouse, la pressione di un tasto, o la scadenza di un timer
- **Callback** — la funzione che scrivi per gestire l'evento; la passi come argomento
- **Ciclo di eventi** (event loop) — il ciclo continuo dentro `turtle.mainloop()` che osserva gli eventi e chiama i callback

## Eventi di Clic del Mouse con `onscreenclick()`

`turtle.onscreenclick(callback)` registra una funzione da chiamare ogni volta che l'utente clicca sul canvas della turtle.

Il callback riceve le coordinate x e y del clic come argomenti.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto disegna un punto ovunque l'utente clicchi. Ma prima di eseguirlo — come sa il programma dove è successo il clic?
    Pensa a come il callback riceve le coordinate, poi eseguilo per scoprirlo!

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
screen.setup(400, 400)
screen.title("Clicca per disegnare dei punti")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def on_click(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(20, "steelblue")

screen.onscreenclick(on_click)
screen.mainloop()`);
</script>

`t.dot(size, color)` disegna un cerchio riempito del diametro dato nella posizione attuale della turtle.
Clicca ovunque sul canvas — appare un punto a ogni posizione cliccata!

## Eventi della Tastiera con `onkey()` e `listen()`

`screen.onkey(callback, key)` registra un callback per un tasto specifico.
`screen.listen()` dice allo screen di iniziare a prestare attenzione agli eventi della tastiera — devi chiamarlo prima che gli eventi della tastiera funzionino.

Le stringhe dei nomi dei tasti includono `"Up"`, `"Down"`, `"Left"`, `"Right"`, `"space"`, `"Return"`, e singole lettere come `"a"`.

```python
import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def go_forward():
    t.forward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

screen.onkey(go_forward, "Up")
screen.onkey(turn_left,  "Left")
screen.onkey(turn_right, "Right")
screen.listen()   # bisogna chiamare listen() per attivare gli eventi della tastiera
screen.mainloop()
```

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
screen.setup(400, 400)
screen.title("Usa le frecce per sterzare")

t = turtle.Turtle()
t.shape("arrow")
t.color("steelblue")
t.speed(0)
t.pensize(2)

def go_forward():
    t.forward(20)

def go_backward():
    t.backward(20)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

screen.onkey(go_forward,  "Up")
screen.onkey(go_backward, "Down")
screen.onkey(turn_left,   "Left")
screen.onkey(turn_right,  "Right")
screen.listen()
screen.mainloop()`);
</script>

Usa le freccette per guidare la turtle attorno al canvas!

## Eventi Timer con `ontimer()`

`screen.ontimer(callback, delay_ms)` chiama `callback` una volta dopo `delay_ms` millisecondi.

La tecnica chiave per i cicli di animazione è **ri-registrare il timer dentro il callback** — così scatta ancora e ancora:

```python
def animate():
    t.forward(5)
    t.left(3)
    screen.ontimer(animate, 50)   # si richiama da sola dopo 50 ms

animate()   # avvia il ciclo
screen.mainloop()
```

Questo crea un'animazione fluida che gira a circa 20 fotogrammi al secondo (1000 ÷ 50ms = 20 fps).

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `import turtle

screen = turtle.Screen()
screen.setup(400, 400)
screen.title("Spirale rotante")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]
step = 0

def draw_step():
    global step
    color = colors[step % len(colors)]
    t.pencolor(color)
    t.forward(step * 0.5)
    t.left(31)
    step += 1
    if step < 200:
        screen.ontimer(draw_step, 20)

draw_step()
screen.mainloop()`);
</script>

## Combinare gli Eventi — Arte Interattiva

Il vero potere della programmazione guidata da eventi emerge quando combini più tipi di eventi.
L'esempio sotto ti permette di disegnare con il mouse e pulire con la barra spaziatrice:

```python
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.pencolor("steelblue")

drawing = False

def start_draw(x, y):
    global drawing
    drawing = True
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw(x, y):
    if drawing:
        t.goto(x, y)

def stop_draw(x, y):
    global drawing
    drawing = False

def clear_screen():
    t.clear()

screen.onscreenclick(start_draw, 1)   # pulsante sinistro del mouse premuto
screen.onscreenclick(stop_draw,  3)   # pulsante destro del mouse rilasciato
screen.onkey(clear_screen, "space")
screen.listen()
screen.mainloop()
```

## Il Confronto tra Guidato da Eventi e Sequenziale

| Caratteristica | Sequenziale | Guidato da Eventi |
|---------|-----------|--------------|
| Flusso di esecuzione | Dall'alto verso il basso, prevedibile | Aspetta gli eventi, ordine imprevedibile |
| Interazione con l'utente | Limitata (solo input()) | In tempo reale (mouse, tastiera, timer) |
| Uso tipico | Script, calcoli | Giochi, GUI, app |
| Complessità | Bassa | Media — richiede il pensiero a callback |

!!! mascot-tip "I Callback Sono Solo Funzioni"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    La parte più difficile della programmazione guidata da eventi è fidarsi del pattern del callback.
    Scrivi la funzione. La registri. Il sistema la chiama quando scatta l'evento.
    Non la chiami tu stesso — quello è il compito del ciclo di eventi. Pensalo come impostare una sveglia sul telefono: la imposti una volta, poi suona quando arriva il momento.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Cambia Colore"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto disegna punti al clic, ma tutti i punti sono dello stesso colore.
    Aggiungi un evento tasto così che premere `"c"` scorra tra una lista di colori a ogni pressione!

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `import turtle

screen = turtle.Screen()
screen.setup(400, 400)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

colors = ["red", "orange", "green", "blue", "purple"]
color_index = 0

def on_click(x, y):
    t.penup()
    t.goto(x, y)
    t.dot(24, colors[color_index])

# Aggiungi una funzione "change_color" e registrala con il tasto "c":
# def change_color():
#   ...

screen.onscreenclick(on_click)
screen.listen()
screen.mainloop()`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia il ritardo del timer nel laboratorio della spirale da `20` a `5`. L'animazione diventa più veloce o più lenta?
   **Saprai che ha funzionato quando** vedi la spirale costruirsi a una velocità notevolmente diversa.

2. Aggiungi un collegamento al tasto `"r"` che chiama `t.color("red")` — premere R cambia il colore di disegno della turtle in rosso.
   **Saprai che ha funzionato quando** premere R cambia il colore di disegno.

3. Registra un callback di clic che usa `t.write()` per timbrare le coordinate del clic a ogni posizione cliccata.
   **Saprai che ha funzionato quando** le etichette `"(x, y)"` appaiono a ogni punto cliccato.

4. Modifica la spirale per fermarsi dopo 300 passi (invece di 200) e aggiungi una funzione di reset su `"s"` che pulisce e riparte dal passo 0.
   **Saprai che ha funzionato quando** premere `s` pulisce e riavvia la spirale.

5. Crea una "pallina che rimbalza" — un cerchio che si muove in diagonale usando un timer e inverte direzione quando colpisce i bordi del canvas.
   **Saprai che ha funzionato quando** la pallina rimbalza indefinitamente nel canvas.

!!! mascot-celebration "Programmatore Guidato da Eventi!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito programmi che rispondono al mondo reale — clic, pressioni di tasti, e animazioni temporizzate!
    La programmazione guidata da eventi è la base di ogni gioco, app, e interfaccia utente di siti web.
    Restano due capitoli — e ti portano nell'eccitante mondo dell'IA e del machine learning! Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
