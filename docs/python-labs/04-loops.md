# Disegnare Poligoni con i Cicli

Alla fine di questa lezione sarai in grado di:

- Usare `for i in range(n):` per ripetere un blocco di codice `n` volte
- Disegnare qualsiasi poligono regolare cambiando solo due variabili
- Spiegare perché un ciclo è meglio che scrivere le stesse righe ancora e ancora

Disegnare un quadrato nella lezione precedente richiedeva otto righe — quattro chiamate `forward()` e quattro chiamate `right()`. Un ciclo `for` fa questo in due righe. Ancora meglio, cambia una variabile e ottieni istantaneamente un pentagono, un esagono, o qualsiasi poligono tu voglia.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ecco un segreto che ogni programmatore conosce: se stai copiando e incollando la stessa riga,
    c'è un modo migliore. Oggi ti mostrerò il ciclo `for` — è la scorciatoia preferita di Monty.
    Programmiamo insieme!

## Il Ciclo For

Un **ciclo for** è un blocco di codice che gira un numero fissato di volte. Ecco il pattern:

```python
for i in range(4):
    monty.forward(80)
    monty.right(90)
```

`range(4)` conta da 0 a 3, quindi il blocco indentato gira **4 volte**. La variabile `i` traccia a quale ripetizione sei — ma per disegnare poligoni, non hai nemmeno bisogno di usare `i`.

L'**angolo di svolta** per qualsiasi poligono regolare segue una regola: dividi 360 per il numero di lati.
Un ottagono ha 8 lati: 360 ÷ 8 = 45 gradi. Un esagono: 360 ÷ 6 = 60 gradi.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Ripeti 4"** per eseguire comandi un numero fissato di volte.
    In Python, `for i in range(4):` fa esattamente la stessa cosa — e le righe indentate
    sotto di esso sono i comandi che si ripetono!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

sides = 6
angle = 360 / sides

for i in range(sides):
    monty.forward(80)
    monty.right(angle)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `sides = 6` e `angle = 360 / 6`. Quanti lati avrà la forma, e qual è quella forma?
    Fai la tua previsione — poi clicca Esegui per scoprirlo!

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

sides = 6
angle = 360 / sides

for i in range(sides):
    monty.forward(80)
    monty.right(angle)`);
</script>

Avevi indovinato? Sei lati, ognuno a 60 gradi — un esagono perfetto!

**Se vedi un messaggio di errore rosso:** Controlla che le due righe dentro il ciclo siano indentate esattamente di 4 spazi. Python usa l'indentazione per sapere quali righe appartengono dentro il ciclo.

## Come Funziona

`for i in range(sides):` dice a Python di contare da 0 fino a (ma non includendo) `sides`. Ogni conteggio è una ripetizione del blocco indentato. La formula dell'angolo `360 / sides` dà sempre la svolta esterna corretta per un poligono regolare — è un fatto matematico che gli angoli esterni di qualsiasi poligono convesso sommano esattamente a 360 gradi.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `sides = 6` | Numero di lati — cambialo per ottenere un poligono diverso |
| `angle = 360 / sides` | Calcola l'angolo di svolta corretto per questo poligono |
| `for i in range(sides):` | Ripete il blocco indentato una volta per ogni lato |
| `    monty.forward(80)` | Disegna un lato (lungo 80 passi); l'indentazione di 4 spazi lo rende parte del ciclo |
| `    monty.right(angle)` | Gira della quantità corretta a ogni angolo |

!!! mascot-warning "Errore Comune: Dimenticare i Due Punti"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    La riga `for` deve finire con due punti `:` e le righe dentro devono essere indentate.
    Se ne dimentichi uno dei due, Python mostrerà un `SyntaxError`. Controlla entrambi prima di cercare oltre!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Riga Mancante"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto cerca di disegnare un pentagono (5 lati), ma `angle` non viene mai calcolato —
    quindi Python non sa quanto girare. Aggiungi **una riga** per calcolare l'angolo!

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

sides = 5
# Add one line here to calculate the correct angle

for i in range(sides):
    monty.forward(80)
    monty.right(angle)`);
</script>

## Esperimenti

Prova questi cambiamenti al codice dell'esagono. Prevedi prima, poi esegui!

1. Cambia `sides = 6` in `sides = 3`.
   **Saprai che ha funzionato quando** vedi un triangolo.

2. Cambia `sides = 6` in `sides = 8`.
   **Saprai che ha funzionato quando** vedi un ottagono (8 lati uguali).

3. Cambia `sides = 6` in `sides = 36`.
   **Saprai che ha funzionato quando** il poligono sembra quasi un cerchio.

4. Cambia `monty.forward(80)` in `monty.forward(120)`.
   **Saprai che ha funzionato quando** l'esagono è più grande e potrebbe estendersi fino al bordo del canvas.

5. Aggiungi `monty.color('purple')` e `monty.pensize(4)` prima del ciclo.
   **Saprai che ha funzionato quando** appare un poligono viola spesso.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Un ciclo `for`, poligoni infiniti — hai sbloccato un superpotere!
    Nel prossimo laboratorio userai `if/else` dentro un ciclo per rendere ogni lato di un colore diverso.
    Programmiamo insieme!
