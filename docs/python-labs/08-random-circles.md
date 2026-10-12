# Cerchi Casuali

Alla fine di questa lezione sarai in grado di:

- Importare la libreria `random` e generare interi casuali con `randint()`
- Usare numeri casuali per posizionare una tartaruga in una posizione imprevedibile
- Disegnare un canvas pieno di cerchi colorati che sembrano diversi ogni volta che esegui il programma

Finora ogni programma che hai scritto produce esattamente lo stesso disegno ogni volta. La libreria `random` cambia questo — genera numeri imprevedibili, così ogni esecuzione del tuo programma è una sorpresa.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Cosa succederebbe se potessi fare un programma che disegna qualcosa di diverso ogni singola volta che lo esegui?
    Questa è la magia della casualità — e oggi ti mostrerò come fare!
    Programmiamo insieme!

## Generare Numeri Casuali

Per usare i numeri casuali, devi prima **importare** la libreria `random` — proprio come importi `turtle`. Poi usa `randint(min, max)` per ottenere un numero intero casuale tra `min` e `max` (entrambi inclusi):

```python
import random
x = random.randint(-150, 150)
```

Ogni volta che questa riga gira, `x` ottiene un valore diverso tra -150 e 150.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Scegli numero a caso da 1 a 10"**.
    In Python, `random.randint(1, 10)` fa esattamente la stessa cosa — scegli un numero intero casuale
    in quell'intervallo ogni volta che gira!

## Codice di Esempio

```python
import turtle
import random

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

colors = ['red', 'orange', 'blue', 'green', 'purple', 'pink']

for i in range(10):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    color = colors[random.randint(0, 5)]
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    monty.circle(10)
    monty.end_fill()

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo gira 10 volte, scegliendo una nuova posizione e colore casuali ogni volta.
    Quanti cerchi appariranno? Saranno sempre negli stessi posti?
    Fai la tua previsione — poi clicca Esegui due volte per vedere cosa cambia!

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

colors = ['red', 'orange', 'blue', 'green', 'purple', 'pink']

for i in range(10):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    color = colors[random.randint(0, 5)]
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    monty.circle(10)
    monty.end_fill()

monty.hideturtle()`);
</script>

Avevi indovinato? Dieci cerchi colorati si disperdono attraverso il canvas in posizioni casuali — e cliccando di nuovo Esegui si produce una disposizione completamente diversa!

## Come Funziona

`random.randint(-150, 150)` restituisce un intero diverso ogni volta — Python usa un algoritmo pseudocasuale che produce numeri che sembrano imprevedibili. `goto(x, y)` fa saltare la tartaruga a quella posizione, e `circle(10)` disegna un cerchio con un raggio di 10 passi attorno alla posizione attuale.

`speed(10)` imposta la tartaruga alla velocità massima di disegno così i cerchi appaiono velocemente invece di muoversi lentamente in posizione.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `import random` | Carica la libreria dei numeri casuali |
| `random.randint(-150, 150)` | Restituisce un intero casuale tra -150 e 150 (inclusi) |
| `monty.speed(10)` | Imposta la velocità di disegno al massimo (10 = più veloce) |
| `colors[random.randint(0, 5)]` | Sceglie un indice casuale da 0 a 5 per selezionare un colore dalla lista |
| `monty.circle(10)` | Disegna un cerchio con raggio 10 nella posizione attuale |

!!! mascot-warning "Indice Fuori Intervallo"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se la tua lista `colors` ha 6 elementi (indici 0–5), allora `randint(0, 6)` può produrre l'indice 6 — che non esiste!
    Usa sempre `randint(0, len(colors) - 1)` oppure `randint(0, 5)` quando la lista ha 6 elementi.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Rendi i Cerchi Più Grandi"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 10 cerchi casuali ma sono tutti della stessa dimensione minuscola.
    Aggiungi **una riga** dentro il ciclo per scegliere un raggio casuale tra `5` e `25`,
    memorizzalo in una variabile chiamata `radius`, e usalo in `monty.circle(radius)`.

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

colors = ['red', 'orange', 'blue', 'green', 'purple', 'pink']

for i in range(10):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    color = colors[random.randint(0, 5)]
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    # Add one line: radius = random.randint(5, 25)
    monty.circle(10)  # change 10 to radius after adding the line above
    monty.end_fill()

monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi prima, poi esegui e confronta!

1. Cambia `range(10)` in `range(30)`.
   **Saprai che ha funzionato quando** 30 cerchi riempiono il canvas invece di 10.

2. Cambia `randint(-150, 150)` in `randint(-50, 50)` sia per `x` sia per `y`.
   **Saprai che ha funzionato quando** tutti i cerchi si raggruppano vicino al centro del canvas.

3. Aggiungi `'gold'`, `'cyan'`, e `'brown'` alla lista `colors`, e aggiorna `randint(0, 5)` per corrispondere alla nuova lunghezza della lista.
   **Saprai che ha funzionato quando** vedi occasionalmente cerchi dorati, ciano, o marroni.

4. Cambia `monty.circle(10)` in `monty.circle(random.randint(5, 25))`.
   **Saprai che ha funzionato quando** i cerchi variano in dimensione, alcuni minuscoli e alcuni grandi.

5. Cambia il numero di cerchi disegnati memorizzando il conteggio in una variabile `num_circles = 20` in cima e usandola in `range(num_circles)`.
   **Saprai che ha funzionato quando** cambiare `num_circles` in un solo posto controlla quanti ne appaiono.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ogni esecuzione è un'opera d'arte unica — questo è il potere della casualità!
    Nel prossimo laboratorio imparerai di più sulle liste e come scorrerle direttamente.
    Programmiamo insieme!
