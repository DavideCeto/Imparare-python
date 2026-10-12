---
hide:
    - toc
---
# Griglia a Scacchiera

Alla fine di questo laboratorio sarai in grado di:

- Usare **cicli `for` annidati** per iterare su righe e colonne
- Calcolare la posizione (x, y) di ogni quadrato dal suo indice di riga e colonna
- Scegliere un colore in base a se `row + col` è pari o dispari

Una griglia 8×8 di quadrati neri e bianchi riempie il canvas — proprio come una scacchiera —
costruita interamente con cicli e aritmetica, non coordinate scritte a mano.

!!! mascot-welcome "Benvenuto alla Scacchiera!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio imparerai come due cicli — uno per le righe, uno per le colonne — possono
    posizionare 64 quadrati sullo schermo con solo poche righe di codice.
    Programmiamo insieme!

## Come Funziona la Griglia

Il ciclo esterno conta le **righe** (0–7, dall'alto al basso). Il ciclo interno conta le **colonne** (0–7, da sinistra a destra).
Per ogni combinazione, la posizione è:

- `x = -160 + col * 40` — inizia a sinistra, si sposta a destra di 40px per colonna
- `y = 160 - row * 40` — inizia in alto, si sposta in basso di 40px per riga

Il colore alterna perché `(row + col) % 2` è `0` sui quadrati pari e `1` sui quadrati dispari —
esattamente come il pattern nero e bianco di una scacchiera.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

size = 40

for row in range(8):
    for col in range(8):
        x = -160 + col * size
        y = 160 - row * size
        color = 'black' if (row + col) % 2 == 0 else 'white'
        monty.penup()
        monty.goto(x, y)
        monty.pendown()
        monty.color(color)
        monty.begin_fill()
        for _ in range(4):
            monty.forward(size)
            monty.right(90)
        monty.end_fill()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il quadrato in alto a sinistra è a row=0, col=0. `(0 + 0) % 2 = 0` → nero.
    Di che colore è il quadrato a row=2, col=3?
    Calcolalo, poi clicca Esegui per controllare!

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

size = 40

for row in range(8):
    for col in range(8):
        x = -160 + col * size
        y = 160 - row * size
        color = 'black' if (row + col) % 2 == 0 else 'white'
        monty.penup()
        monty.goto(x, y)
        monty.pendown()
        monty.color(color)
        monty.begin_fill()
        for _ in range(4):
            monty.forward(size)
            monty.right(90)
        monty.end_fill()`);
</script>

`(2 + 3) % 2 = 1` → **bianco**. Avevi indovinato?

## Come Funziona

Il `for _ in range(4)` più interno disegna un quadrato: avanti 40, gira a destra 90°, quattro volte.
(Il `_` è un nome di variabile usa-e-getta usato quando non hai bisogno del contatore del ciclo.)

Prima di ogni quadrato, `monty.goto(x, y)` salta alla posizione corretta con la penna alzata — senza
questo, Monty tirerebbe linee attraverso il canvas tra i quadrati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `for row in range(8)` | Ciclo esterno — 8 righe dall'alto al basso |
| `for col in range(8)` | Ciclo interno — 8 colonne da sinistra a destra |
| `x = -160 + col * size` | La colonna 0 inizia a x = -160; ogni colonna è 40px a destra |
| `y = 160 - row * size` | La riga 0 inizia a y = 160; ogni riga è 40px più in basso |
| `(row + col) % 2` | 0 su somma pari → nero; 1 su somma dispari → bianco |
| `for _ in range(4)` | Disegna i quattro lati di un quadrato |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna tutti i 64 quadrati **neri** — nessun pattern alternato!
    Correggi l'unica riga che decide il colore così appaia il pattern a scacchiera.

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

size = 40

for row in range(8):
    for col in range(8):
        x = -160 + col * size
        y = 160 - row * size
        color = 'black'
        monty.penup()
        monty.goto(x, y)
        monty.pendown()
        monty.color(color)
        monty.begin_fill()
        for _ in range(4):
            monty.forward(size)
            monty.right(90)
        monty.end_fill()`);
</script>

Sostituisci `color = 'black'` con `color = 'black' if (row + col) % 2 == 0 else 'white'`.

## Esperimenti

1. **Rendilo colorato.** Sostituisci `'black'` e `'white'` con `'navy'` e `'gold'`. Saprai che ha funzionato quando la scacchiera mostra due colori vivaci invece della scala di grigi.

2. **Ridimensiona i quadrati.** Cambia `size = 40` in `size = 30`. La scacchiera resta 8×8 ma è più piccola. Prova ad adattare le formule x/y per mantenerla centrata. Saprai che ha funzionato quando tutti i 64 quadrati appaiono ancora.

3. **Diventa più grande.** Cambia `range(8)` in `range(10)` in entrambi i cicli e adatta le posizioni di partenza. Saprai che ha funzionato quando hai una griglia 10×10 (100 quadrati).

4. **Usa colori casuali.** Aggiungi `import random` e sostituisci la riga del colore con `color = random.choice(['red','blue','green','purple','orange'])`. Saprai che ha funzionato quando ogni quadrato è di un colore casuale diverso.

!!! mascot-celebration "Lavoro Eccellente!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato cicli annidati, aritmetica delle coordinate, e scelta del colore basata sul modulo —
    tre dei più potenti strumenti in tutta la programmazione!
    Prossimo: **Campo di Strisce Diagonali** per esplorare il disegno di linee con `setheading()`.
