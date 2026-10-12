# Funzioni e Fiori

Alla fine di questa lezione sarai in grado di:

- Definire la tua propria funzione con `def` e chiamarla per nome
- Chiamare una funzione più volte da dentro un ciclo
- Costruire un disegno di fiore ripetendo una funzione `petal()`

Cosa succede se potessi dare un nome a un pezzo di codice ed eseguirlo quando vuoi — semplicemente dicendo il nome? Questo è cos'è una **funzione**. In questo laboratorio definirai una funzione `petal()` e la chiamerai in un ciclo per far crescere un fiore completo sul canvas.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le funzioni sono il segreto per scrivere codice che è corto, chiaro, e facile da riutilizzare.
    Oggi faremo crescere un fiore insieme — un petalo alla volta!
    Programmiamo insieme!

## Definire una Funzione

Una **funzione** è un blocco di codice che scrivi una volta e puoi eseguire quante volte vuoi chiamando il suo nome. La crei con `def`:

```python
def petal():
    monty.forward(100)
    monty.right(120)
    monty.forward(100)
    monty.right(120)
    monty.forward(100)
    monty.right(120)
```

Questa funzione disegna un triangolo — un petalo. Per usarla, chiama `petal()`. Per disegnare quattro petali, chiamala quattro volte (o metti la chiamata in un ciclo).

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato **"I Miei Blocchi"** per definire un blocco personalizzato e poi trascinarlo dove ne avevi bisogno.
    In Python, `def petal():` definisce il blocco, e `petal()` è come lo usi — ogni volta che lo chiami, l'intera funzione gira!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 80
angle = 120

def petal():
    monty.begin_fill()
    monty.color('pink')
    for i in range(3):
        monty.forward(distance)
        monty.right(angle)
    monty.end_fill()
    monty.right(90)

for i in range(4):
    petal()

monty.pensize(6)
monty.color('green')
monty.right(45)
monty.forward(120)
monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `petal()` viene chiamata 4 volte, e ogni petalo ruota di 90 gradi dall'ultimo.
    Come pensi che apparirà il disegno completo — un fiore, una girandola, qualcos'altro?
    Fai la tua previsione — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato direttamente su questa pagina.
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
monty = turtle.Turtle()
monty.shape('turtle')

distance = 80
angle = 120

def petal():
    monty.begin_fill()
    monty.color('pink')
    for i in range(3):
        monty.forward(distance)
        monty.right(angle)
    monty.end_fill()
    monty.right(90)

for i in range(4):
    petal()

monty.pensize(6)
monty.color('green')
monty.right(45)
monty.forward(120)
monty.hideturtle()`);
</script>

Avevi indovinato? Quattro triangoli rosa riempiti disposti attorno a un centro con uno stelo verde — un fiore!

## Come Funziona

`def petal():` crea la funzione ma non la esegue ancora. Il codice dentro di essa resta inattivo finché non chiami `petal()`. Quando gira il ciclo `for i in range(4):`, chiama `petal()` quattro volte. Ogni chiamata disegna un triangolo e poi ruota la tartaruga di 90 gradi così il petalo successivo punta in una nuova direzione.

`begin_fill()` ed `end_fill()` colorano l'interno di qualsiasi forma la tartaruga tracci tra quelle due chiamate. `hideturtle()` rimuove il cursore della tartaruga alla fine per un risultato più pulito.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def petal():` | Definisce una funzione chiamata `petal` — il codice qui gira quando `petal()` viene chiamata |
| `monty.begin_fill()` | Inizia a registrare il percorso per il riempimento |
| `monty.color('pink')` | Imposta il colore di riempimento e del contorno su rosa |
| `for i in range(3):` | Si ripete 3 volte dentro la funzione per disegnare ogni lato del triangolo |
| `monty.end_fill()` | Riempie l'area racchiusa con il colore attuale |
| `monty.right(90)` | Ruota di 90° così il petalo successivo guarda in una nuova direzione |
| `for i in range(4): petal()` | Chiama la funzione 4 volte per disegnare 4 petali |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto cerca di disegnare 4 petali, ma solo uno appare prima che il programma si fermi.
    La funzione non viene mai chiamata dentro il ciclo. Riesci a trovare e correggere il problema?

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
monty.shape('turtle')

distance = 80
angle = 120

def petal():
    monty.begin_fill()
    monty.color('pink')
    for i in range(3):
        monty.forward(distance)
        monty.right(angle)
    monty.end_fill()
    monty.right(90)

for i in range(4):
    pass  # bug: petal() is never called here!`);
</script>

## Esperimenti

Prova questi cambiamenti al codice del fiore. Prevedi prima, poi esegui!

1. Cambia `monty.color('pink')` in `monty.color('yellow')`.
   **Saprai che ha funzionato quando** i petali sono gialli invece di rosa.

2. Cambia `for i in range(4): petal()` in `for i in range(6): petal()` e la rotazione dentro `petal` in `monty.right(60)`.
   **Saprai che ha funzionato quando** vedi 6 petali invece di 4.

3. Cambia `distance = 80` in `distance = 120`.
   **Saprai che ha funzionato quando** i petali sono notevolmente più grandi.

4. Aggiungi un `if/else` dentro `petal()` così che alterni tra `'pink'` e `'purple'` usando `i % 2`.
   **Saprai che ha funzionato quando** i petali alternano i colori. (Suggerimento: dovrai passare `i` alla funzione.)

5. Cambia la direzione dello stelo: sostituisci `monty.right(45)` con `monty.left(45)`.
   **Saprai che ha funzionato quando** lo stelo cresce verso l'alto-sinistra invece che verso il basso-destra.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai definito la tua prima funzione e l'hai usata per costruire qualcosa di bellissimo!
    Nel prossimo laboratorio darai alle tue funzioni dei *parametri* così la stessa funzione può disegnare
    cose diverse in base a cosa le passi. Programmiamo insieme!
