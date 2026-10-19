# Ottenere Input dall'Utente

Alla fine di questa lezione sarai in grado di:

- Usare `input()` per sospendere un programma e fare una domanda all'utente
- Convertire l'input di testo in un intero con `int()` così puoi usarlo come numero
- Disegnare una forma la cui dimensione o conteggio cambia in base a ciò che l'utente digita

Ogni programma che hai scritto finora gira allo stesso modo ogni volta. `input()` cambia questo — sospende il programma, mostra un prompt, e aspetta che l'utente digiti qualcosa prima di continuare. Qualsiasi cosa l'utente digiti diventa un valore che il tuo programma può usare.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Cosa succederebbe se *tu* potessi dire a Monty quante forme disegnare — mentre il programma gira?
    Questo è ciò che fa l'input dell'utente! Programmiamo insieme!

## La Funzione `input()`

`input("testo del prompt")` mostra un messaggio nella casella di output e aspetta. Quando l'utente digita qualcosa e preme Invio, `input()` restituisce ciò che ha digitato — sempre come **stringa** (testo).

Se hai bisogno di un numero, racchiudi `input()` con `int()` per convertire la stringa:

```python
answer = input("Quanti cerchi? ")
count = int(answer)
```

Oppure combinali su una riga:

```python
count = int(input("Quanti cerchi? "))
```

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Chiedi ___ e aspetta"**, che memorizzava la risposta nella variabile `answer`.
    In Python, `input("domanda")` fa la stessa cosa — chiede, aspetta, e restituisce la risposta!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

count = int(input("Quanti cerchi vuoi disegnare? (prova da 3 a 10) "))
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

monty.penup()
monty.goto(-150, 0)

for i in range(count):
    monty.color(colors[i % len(colors)])
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    monty.forward(50)

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Quando clicchi Esegui, apparirà un prompt che chiede quanti cerchi disegnare.
    Se digiti `5`, quanti cerchi appariranno? E se digiti `0`?
    Fai la tua previsione — poi clicca Esegui e scoprilo!

## Provalo Ora

Clicca **Esegui**, digita un numero nella casella di output quando richiesto, poi premi Invio.
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

count = int(input("Quanti cerchi vuoi disegnare? (prova da 3 a 10) "))
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

monty.penup()
monty.goto(-150, 0)

for i in range(count):
    monty.color(colors[i % len(colors)])
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)
    monty.end_fill()
    monty.penup()
    monty.forward(50)

monty.hideturtle()`);
</script>

Avevi indovinato? Il programma ha disegnato esattamente tanti cerchi quanti ne hai digitati — il ciclo gira `count` volte, usando `i % len(colors)` per scorrere la lista di colori senza uscire dall'intervallo.

## Come Funziona

`input()` restituisce sempre una **stringa** — anche se l'utente digita `5`, Python memorizza `"5"` (testo), non `5` (numero). Chiamare `int()` su di essa converte `"5"` nell'intero `5`. Solo dopo puoi usarlo in `range(count)`.

`i % len(colors)` è il resto quando `i` viene diviso per il numero di colori. Questo fa ripartire l'indice da 0 quando `i` raggiunge la fine della lista — così puoi disegnare più cerchi di quanti colori ci siano senza un `IndexError`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `input("prompt")` | Mostra il prompt e aspetta che l'utente digiti e prema Invio |
| `int(...)` | Converte la stringa restituita in un intero |
| `count = int(input(...))` | Combina entrambi i passi in una riga |
| `i % len(colors)` | Scorre gli indici dei colori senza uscire dall'intervallo |

!!! mascot-warning "Converti Sempre in int"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se ti dimentichi `int()` e provi a usare l'input direttamente in `range(count)`, otterrai un
    `TypeError: 'str' object cannot be interpreted as an integer`.
    `input()` restituisce sempre una stringa — devi convertirla se hai bisogno di un numero.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Chiedi Anche il Raggio"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto chiede il numero di cerchi ma li disegna sempre con raggio 20.
    Aggiungi **una riga** per chiedere anche il raggio all'utente, memorizzalo in `radius`, e usalo
    in `monty.circle(radius)` invece di `monty.circle(20)`.

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

count = int(input("Quanti cerchi? (1-7) "))
# Aggiungi qui una riga: radius = int(input("Quanto grandi? (10-40) "))

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

monty.penup()
monty.goto(-150, 0)

for i in range(count):
    monty.color(colors[i % len(colors)])
    monty.pendown()
    monty.begin_fill()
    monty.circle(20)  # sostituisci 20 con radius dopo aver aggiunto la riga sopra
    monty.end_fill()
    monty.penup()
    monty.forward(50)

monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti. Ricordati di digitare un valore nel prompt quando clicchi Esegui!

1. Chiedi all'utente il raggio invece di contare i cerchi — usa `radius = int(input("Circle radius? "))` e disegna un cerchio con quel raggio.
   **Saprai che ha funzionato quando** digitare numeri diversi produce cerchi di dimensioni diverse.

2. Chiedi un nome di colore: `my_color = input("Pen color? ")` e usa `monty.color(my_color)` prima del ciclo.
   **Saprai che ha funzionato quando** digitare `'blue'` dà cerchi blu e `'green'` dà cerchi verdi.

3. Prova a digitare un decimale come `3.5` al prompt con `int()`. Nota il `ValueError`.
   Ora cambia `int()` in `float()` così i decimali sono accettati.
   **Saprai che ha funzionato quando** digitare `3.5` non blocca più il programma.

4. Aggiungi una `print()` alla fine che dice quanti cerchi sono stati disegnati: `print("Drew", count, "circles!")`.
   **Saprai che ha funzionato quando** quel messaggio appare nella casella di output dopo che il disegno è finito.

5. Chiedi il numero di lati per forma. Usa la risposta per disegnare poligoni invece di cerchi.
   **Saprai che ha funzionato quando** digitare `3` disegna triangoli, `4` disegna quadrati, ecc.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    I tuoi programmi possono ora parlare con l'utente e cambiare il loro comportamento al volo —
    è questo che fa sembrare il software *vivo*! Programmiamo insieme!
