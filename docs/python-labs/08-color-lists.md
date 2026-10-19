# Liste di Colori

Alla fine di questa lezione sarai in grado di:

- Creare una lista di stringhe di colore e accedere agli elementi per numero di indice
- Scorrere ogni elemento di una lista usando `for color in my_list:`
- Disegnare una riga di forme colorate iterando su una lista di colori

Una **lista** è una collezione ordinata di valori. In Python la scrivi con le parentesi quadre. Le liste sono perfette per memorizzare una tavolozza di colori e poi dipingere forme una per una attraverso l'intera tavolozza.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Cosa succederebbe se potessi dire a Monty: "ecco dieci colori — dipingi un cerchio per ciascuno"?
    Questo è esattamente ciò che ti permettono di fare le liste! Programmiamo insieme!

## Creare e Usare una Lista

Una **lista** memorizza più valori in una variabile, separati da virgole dentro parentesi quadre:

```python
colors = ['red', 'orange', 'yellow', 'green', 'blue']
```

Accedi a qualsiasi elemento tramite il suo **indice** — la sua posizione nella lista, contando da 0:

```python
colors[0]   # 'red'
colors[2]   # 'yellow'
colors[4]   # 'blue'
```

Per fare qualcosa con *ogni* elemento, usa un ciclo `for` direttamente sulla lista:

```python
for color in colors:
    # 'color' è, a turno, ciascun elemento
```

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **Lista** con slot numerati (elemento 1, elemento 2, …).
    In Python, le liste usano la stessa idea — ma il conteggio inizia a **0**, non a 1.
    Quindi `colors[0]` è ciò che Scratch chiama "elemento 1 di colors".

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

monty.penup()
monty.goto(-150, 0)

for color in colors:
    monty.color(color)
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    monty.forward(45)

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La lista ha 7 colori e il ciclo gira una volta per colore.
    Quanti cerchi appariranno, e in quale ordine andranno i colori?
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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

monty.penup()
monty.goto(-150, 0)

for color in colors:
    monty.color(color)
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    monty.forward(45)

monty.hideturtle()`);
</script>

Avevi indovinato? Sette cerchi riempiti distribuiti in riga, ognuno dipinto di un colore diverso dalla lista — una tavolozza arcobaleno!

## Come Funziona

`for color in colors:` è un **ciclo for-each** — a ogni ripetizione, `color` viene automaticamente impostato all'elemento successivo nella lista. La prima volta è `'red'`, poi `'orange'`, e così via finché la lista non si esaurisce.

`forward(45)` muove la tartaruga di 45 passi a destra dopo ogni cerchio così il successivo appare affianco senza sovrapporsi.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = ['red', …]` | Crea una lista di stringhe di colore |
| `colors[0]` | Accede al primo elemento (`'red'`); gli indici iniziano da 0 |
| `for color in colors:` | Gira una volta per ogni elemento; `color` contiene l'elemento attuale |
| `monty.goto(-150, 0)` | Si muove sul lato sinistro del canvas come punto di partenza |
| `monty.forward(45)` | Si sposta a destra di 45 passi prima di disegnare il cerchio successivo |

!!! mascot-warning "Indice Fuori Intervallo"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se la tua lista ha 7 elementi, gli indici validi sono 0–6. Provare `colors[7]` causa un
    `IndexError` — Python non può trovare l'elemento 7 perché non esiste.
    Usa `len(colors)` per scoprire quanti elementi ci sono in una lista.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Disegna Quadrati Invece"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe disegnare una riga di piccoli quadrati riempiti (non cerchi),
    ma il corpo del ciclo è incompleto. Aggiungi **due righe** dentro il ciclo — un ciclo `for`
    che disegna quattro lati — così ogni colore diventa un quadrato riempito invece di un cerchio.

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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

monty.penup()
monty.goto(-140, 0)

for color in colors:
    monty.color(color)
    monty.pendown()
    monty.begin_fill()
    # Aggiungi qui un ciclo for per disegnare 4 lati di un quadrato (forward 30, right 90)
    monty.end_fill()
    monty.penup()
    monty.forward(40)

monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice dei cerchi colorati. Prevedi prima, poi esegui!

1. Aggiungi `'gold'` e `'brown'` alla fine della lista `colors`.
   **Saprai che ha funzionato quando** due cerchi extra appaiono a destra dei sette originali.

2. Cambia `monty.circle(20)` in `monty.circle(15)` e `monty.forward(45)` in `monty.forward(35)`.
   **Saprai che ha funzionato quando** i cerchi sono più piccoli e più vicini tra loro.

3. Stampa la lunghezza della lista: aggiungi `print(len(colors))` dopo la definizione della lista e prima del ciclo.
   **Saprai che ha funzionato quando** `7` (o il tuo nuovo conteggio) appare nella casella di output sotto l'editor.

4. Accedi a un singolo colore per indice: aggiungi `print(colors[3])` dopo la definizione della lista.
   **Saprai che ha funzionato quando** `green` appare nell'output (è all'indice 3).

5. Prova un ciclo `for` usando un indice: sostituisci `for color in colors:` con `for i in range(len(colors)):` e poi usa `colors[i]` invece di `color`.
   **Saprai che ha funzionato quando** l'output sembra lo stesso — questo è un modo alternativo di iterare.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Le liste ti permettono di memorizzare intere collezioni di dati e scorrerle automaticamente!
    Nel prossimo laboratorio combinerai le liste con i numeri casuali e le funzioni per disegnare stelle casuali.
    Programmiamo insieme!
