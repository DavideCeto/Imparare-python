# Albero Frattale con la Ricorsione

Alla fine di questa lezione sarai in grado di:

- Spiegare cosa significa **ricorsione** — una funzione che chiama se stessa
- Tracciare come una funzione ricorsiva si ferma usando un caso base
- Disegnare un albero ramificato dove ogni ramo genera due rami più piccoli

Un **frattale** è un pattern che si ripete a scale sempre più piccole. I frattali più belli in natura — alberi, felci, coste — sono costruiti esattamente così. In questo laboratorio scriverai una funzione che disegna un ramo, poi chiama *se stessa* due volte per disegnare due rami più piccoli alla punta, e così via finché i rami non sono troppo piccoli per essere visti.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La ricorsione è una delle idee più magiche dell'informatica.
    Quando la capisci, la vedrai ovunque — dalla matematica alla natura all'arte.
    Programmiamo insieme!

## Cos'è la Ricorsione?

La **ricorsione** è quando una funzione chiama se stessa. Senza una condizione di arresto, si chiamerebbe per sempre — quindi ogni funzione ricorsiva ha bisogno di un **caso base**: una condizione in cui si ferma e ritorna senza chiamarsi di nuovo.

Ecco il pattern:

```python
def draw_branch(size, level):
    if level == 0:      # base case: stop here
        return
    monty.forward(size)
    draw_branch(size * 0.6, level - 1)   # left branch
    draw_branch(size * 0.6, level - 1)   # right branch
    monty.backward(size)
```

Ogni chiamata passa una `size` *più piccola* e un `level` *più basso*. Quando `level` raggiunge 0, la ricorsione si ferma.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)
monty.left(90)

monty.penup()
monty.goto(0, -160)
monty.pendown()

colors = ['brown', 'sienna', 'green', 'limegreen']

def draw_branch(size, level):
    if level == 0:
        return
    monty.color(colors[min(level, len(colors) - 1)])
    monty.pensize(max(level, 1))
    monty.forward(size)
    monty.right(25)
    draw_branch(size * 0.65, level - 1)
    monty.left(50)
    draw_branch(size * 0.65, level - 1)
    monty.right(25)
    monty.backward(size)

draw_branch(80, 4)
monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione inizia con `level = 4` e chiama se stessa con `level - 1` ogni volta.
    Quanti livelli di ramificazione avrà l'albero? Sembrerà più un albero vero o un pattern geometrico?
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
monty.speed(10)
monty.left(90)

monty.penup()
monty.goto(0, -160)
monty.pendown()

colors = ['brown', 'sienna', 'green', 'limegreen']

def draw_branch(size, level):
    if level == 0:
        return
    monty.color(colors[min(level, len(colors) - 1)])
    monty.pensize(max(level, 1))
    monty.forward(size)
    monty.right(25)
    draw_branch(size * 0.65, level - 1)
    monty.left(50)
    draw_branch(size * 0.65, level - 1)
    monty.right(25)
    monty.backward(size)

draw_branch(80, 4)
monty.hideturtle()`);
</script>

Avevi indovinato? Un albero ramificato con tronco marrone, rami che si assottigliano, e punte verdi alle foglie — tutto da una breve funzione che chiama se stessa!

## Come Funziona

`draw_branch(80, 4)` disegna un tronco di 80 passi, poi chiama se stessa due volte con `size * 0.65` (restringendo ogni ramo del 35%) e `level - 1`. Ognuna di quelle chiamate disegna un ramo più piccolo e chiama *se stessa* di nuovo — finché `level` raggiunge 0, momento in cui la funzione semplicemente ritorna. Poi ogni chiamata di funzione ripercorre il percorso indietro con `backward(size)` per ripristinare la tartaruga dove il ramo era iniziato.

`pensize(max(level, 1))` rende le righe del tronco spesse e quelle delle punte sottili — più spesse ai livelli alti, ma sempre almeno 1 pixel.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `if level == 0: return` | Caso base — ferma la ricorsione quando i rami sono troppo piccoli |
| `monty.forward(size)` | Disegna il ramo attuale |
| `monty.right(25)` | Angola a destra prima di disegnare il sotto-ramo destro |
| `draw_branch(size * 0.65, level - 1)` | Chiamata ricorsiva — disegna un ramo più piccolo |
| `monty.left(50)` | Gira a sinistra per disegnare il sotto-ramo sinistro |
| `monty.backward(size)` | Ripercorre il ramo attuale così la posizione della tartaruga del chiamante viene ripristinata |

!!! mascot-encourage "La Ricorsione Sembra Difficile all'Inizio!"
    ![Monty encouraging](../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    È normale non capire completamente la ricorsione la prima volta che la vedi.
    L'intuizione chiave: ogni chiamata di funzione gestisce *un ramo*, e si fida delle chiamate
    più piccole per gestire il resto. Prova a cambiare `level` da 4 a 2 per vedere una versione più semplice!

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto cerca di disegnare un albero frattale, ma il caso base è sbagliato —
    si ferma troppo presto così appare solo il tronco. Riesci a trovare e correggere la condizione?

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
monty.speed(10)
monty.left(90)

monty.penup()
monty.goto(0, -160)
monty.pendown()

def draw_branch(size, level):
    if level == 4:   # bug: this stops when level IS 4, but we start AT 4!
        return
    monty.color('brown')
    monty.forward(size)
    monty.right(25)
    draw_branch(size * 0.65, level - 1)
    monty.left(50)
    draw_branch(size * 0.65, level - 1)
    monty.right(25)
    monty.backward(size)

draw_branch(80, 4)
monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice dell'albero frattale. Prevedi prima, poi esegui!

1. Cambia `draw_branch(80, 4)` in `draw_branch(80, 3)`.
   **Saprai che ha funzionato quando** l'albero ha meno livelli e sembra più semplice.

2. Cambia l'angolo dei rami: sostituisci entrambi i valori `25` con `35`.
   **Saprai che ha funzionato quando** l'albero è più largo e più piatto.

3. Cambia `size * 0.65` in `size * 0.5` così i rami si restringono della metà ogni volta.
   **Saprai che ha funzionato quando** l'albero è più alto e più simmetrico.

4. Cambia `draw_branch(80, 4)` in `draw_branch(80, 5)`.
   **Saprai che ha funzionato quando** l'albero ha grappoli di foglie più densi e intricati.

5. Sostituisci le voci della lista `colors` con `'darkgreen'` e `'forestgreen'` per i livelli delle foglie.
   **Saprai che ha funzionato quando** le punte esterne dell'albero sono di un verde più profondo.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scritto una funzione ricorsiva — uno dei pattern più potenti in tutta la programmazione!
    Artisti e scienziati veri usano esattamente questa tecnica per generare alberi, fiocchi di neve, e montagne.
    Programmiamo insieme!
