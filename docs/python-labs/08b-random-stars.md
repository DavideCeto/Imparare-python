# Stelle Casuali

Alla fine di questa lezione sarai in grado di:

- Scrivere una funzione che disegna una stella a cinque punte usando `forward()` e `right(144)`
- Chiamare quella funzione con posizioni, dimensioni e colori casuali da una lista
- Combinare funzioni, liste e casualità in un unico programma

Le stelle a cinque punte hanno un segreto: la tartaruga gira sempre di **144 gradi** e disegna 5 raggi. In questo laboratorio scriverai una funzione `star()`, la disperderai in posizioni casuali, e lascerai che Python scelga i colori — così ogni esecuzione produce una nuova opera d'arte stellare.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Stelle, colori, e casualità — tutto in un unico programma! Questo laboratorio metterà insieme tutto ciò che
    hai imparato finora: funzioni, liste, cicli, e `random`. Programmiamo insieme!

## Disegnare una Stella

Una stella a cinque punte usa un angolo speciale: la tartaruga disegna un raggio, gira **144 gradi** a destra, disegna un altro raggio — e ripetere questo 5 volte chiude la stella perfettamente. La lunghezza del raggio controlla la dimensione della stella.

```python
def star(x, y, size):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    for i in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()
```

## Codice di Esempio

```python
import turtle
import random

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink', 'gold']

def star(x, y, size):
    monty.penup()
    monty.goto(x, y)
    monty.color(colors[random.randint(0, len(colors) - 1)])
    monty.pendown()
    monty.begin_fill()
    for i in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()

for i in range(8):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(20, 50)
    star(x, y, size)

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo gira 8 volte e ogni chiamata sceglie una posizione, dimensione, e colore casuali.
    Quante stelle appariranno? Saranno della stessa dimensione? Clicca Esegui due volte — ottieni la stessa immagine?
    Fai la tua previsione — poi scoprilo!

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
import random

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink', 'gold']

def star(x, y, size):
    monty.penup()
    monty.goto(x, y)
    monty.color(colors[random.randint(0, len(colors) - 1)])
    monty.pendown()
    monty.begin_fill()
    for i in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()

for i in range(8):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(20, 50)
    star(x, y, size)

monty.hideturtle()`);
</script>

Avevi indovinato? Otto stelle riempite — ognuna di un colore e una dimensione casuali diversi, disperse attraverso il canvas. Clicca Reset e poi Esegui di nuovo e otterrai una disposizione completamente nuova ogni volta!

## Come Funziona

La chiave della forma della stella è `right(144)`. Poiché 144 × 5 = 720 = 2 × 360, la tartaruga fa esattamente due rotazioni complete mentre traccia i cinque raggi, finendo dove ha iniziato. Qualsiasi altro angolo e la forma non si chiuderà in una stella.

`len(colors) - 1` calcola l'ultimo indice valido della lista dinamicamente, così aggiungere o rimuovere colori dalla lista aggiorna automaticamente l'intervallo casuale — senza bisogno di aggiornare il numero a mano.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `for i in range(5): forward(size); right(144)` | Disegna i 5 raggi della stella |
| `right(144)` | L'angolo magico della stella — 5 × 144 = 720° = due rotazioni complete |
| `random.randint(0, len(colors) - 1)` | Sceglie un indice valido casuale nella lista dei colori |
| `size = random.randint(20, 50)` | Sceglie una dimensione casuale della stella tra 20 e 50 passi |

!!! mascot-warning "Stelle Che Non Si Chiudono"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se cambi `right(144)` in qualsiasi altro angolo, il ciclo a 5 raggi non riporterà la tartaruga
    al suo punto di partenza — e la stella non si chiuderà. Prova `right(150)` e vedi cosa succede!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Colore di Sfondo"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna stelle casuali ma lo sfondo è bianco semplice.
    Aggiungi **una riga** subito dopo aver creato `monty` per impostare il colore di sfondo dello schermo su `'navy'`.
    Suggerimento: usa `turtle.Screen().bgcolor('navy')`.

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
monty.speed(10)
# Add one line here to set the background to 'navy'

colors = ['white', 'yellow', 'orange', 'cyan', 'gold']

def star(x, y, size):
    monty.penup()
    monty.goto(x, y)
    monty.color(colors[random.randint(0, len(colors) - 1)])
    monty.pendown()
    monty.begin_fill()
    for i in range(5):
        monty.forward(size)
        monty.right(144)
    monty.end_fill()

for i in range(10):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    size = random.randint(15, 40)
    star(x, y, size)

monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice delle stelle casuali. Prevedi prima, poi esegui!

1. Cambia `range(8)` in `range(20)`.
   **Saprai che ha funzionato quando** 20 stelle affollano il canvas.

2. Cambia `random.randint(20, 50)` per `size` in `random.randint(10, 80)`.
   **Saprai che ha funzionato quando** le stelle variano da minuscole a molto grandi.

3. Cambia `range(5)` in `range(6)` e `right(144)` in `right(120)` dentro la funzione.
   **Saprai che ha funzionato quando** vedi Stelle di David a 6 punte invece di stelle a 5 punte.

4. Aggiungi `monty.pensize(2)` dentro la funzione `star` per dare a ogni stella un contorno visibile.
   **Saprai che ha funzionato quando** ogni stella ha un bordo fine.

5. Rimuovi `begin_fill()` ed `end_fill()` dalla funzione.
   **Saprai che ha funzionato quando** vedi stelle solo di contorno invece che riempite.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai combinato funzioni, liste, cicli, e casualità in un unico programma creativo —
    questa è vera programmazione Python! Nel prossimo laboratorio imparerai come ottenere input dall'utente.
    Programmiamo insieme!
