---
hide:
    - toc
---
# Griglia di Punti

Alla fine di questo laboratorio sarai in grado di:

- Posizionare punti a ogni intersezione di una griglia usando cicli annidati
- Usare `dot()` per disegnare un cerchio riempito in una riga
- Mappare una variabile di ciclo a una proprietà visiva (dimensione del punto) per aggiungere profondità

Cento punti blu acciaio riempiono una griglia 10×10. Ogni riga di punti cresce un po'
più grande, così il fondo sembra più pesante e vicino — un semplice trucco per creare profondità.

!!! mascot-welcome "Benvenuto alla Griglia di Punti!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio scoprirai `dot()` — il comando cerchio in una riga di turtle —
    e vedrai come mappare una variabile di ciclo alla dimensione aggiunge un senso di prospettiva a una griglia.
    Programmiamo insieme!

## Come Funziona la Griglia

Due cicli annidati scorrono attraverso ogni coppia (row, col) da (0,0) a (9,9).
La posizione di ogni punto è:

- `x = -180 + col * 40` — 10 colonne, 40 pixel di distanza, centrate sul canvas
- `y = 180 - row * 40` — 10 righe, 40 pixel di distanza, dall'alto al basso

La dimensione del punto è `4 + row * 2`: riga 0 → dimensione 4, riga 9 → dimensione 22.
Punti più grandi verso il basso danno l'illusione di una superficie piatta che si allontana verso l'alto.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

for row in range(10):
    for col in range(10):
        x = -180 + col * 40
        y = 180 - row * 40
        dot_size = 4 + row * 2
        monty.penup()
        monty.goto(x, y)
        monty.dot(dot_size, 'steelblue')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La griglia è 10 colonne × 10 righe. Quanti punti verranno disegnati in totale?
    Fai la tua previsione — poi clicca Esegui per scoprirlo!

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

for row in range(10):
    for col in range(10):
        x = -180 + col * 40
        y = 180 - row * 40
        dot_size = 4 + row * 2
        monty.penup()
        monty.goto(x, y)
        monty.dot(dot_size, 'steelblue')`);
</script>

10 × 10 = **100 punti**. Avevi indovinato?

## Come Funziona

`monty.dot(size, color)` disegna un cerchio riempito centrato sulla posizione attuale della tartaruga — nessun `begin_fill()` necessario.

`monty.penup()` prima di `goto()` è essenziale qui. Senza, Monty tirerebbe una linea da punto a punto attraverso ogni riga.

La formula della dimensione `4 + row * 2` è una **mappatura lineare** — convertono l'indice di riga (0–9) in una dimensione in pixel (4–22). Questo pattern di conversione di un intervallo di numeri in un altro appare costantemente nella visualizzazione dei dati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `for row in range(10)` | Ciclo esterno — 10 righe |
| `for col in range(10)` | Ciclo interno — 10 colonne |
| `x = -180 + col * 40` | Posizione x: da sinistra a destra, distanti 40px |
| `y = 180 - row * 40` | Posizione y: dall'alto al basso, distanti 40px |
| `dot_size = 4 + row * 2` | I punti crescono di 2px a ogni riga |
| `monty.dot(dot_size, 'steelblue')` | Disegna un cerchio riempito in una riga |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi Variazione di Dimensione"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 100 punti ma sono tutti della stessa piccola dimensione — nessun effetto di profondità!
    Correggi la riga `dot_size` così i punti crescano più grandi verso il fondo della griglia.

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

for row in range(10):
    for col in range(10):
        x = -180 + col * 40
        y = 180 - row * 40
        dot_size = 4
        monty.penup()
        monty.goto(x, y)
        monty.dot(dot_size, 'steelblue')`);
</script>

Cambia `dot_size = 4` in `dot_size = 4 + row * 2` per rendere ogni riga 2 pixel più grande della riga sopra.

## Esperimenti

1. **Mappa la dimensione alla colonna invece che alla riga.** Cambia `dot_size = 4 + row * 2` in `dot_size = 4 + col * 2`. Saprai che ha funzionato quando i punti crescono più grandi da sinistra a destra invece che dall'alto al basso.

2. **Cambia il colore.** Sostituisci `'steelblue'` con `'tomato'` o `'mediumseagreen'`. Saprai che ha funzionato quando il colore del punto cambia attraverso la griglia.

3. **Colora per riga.** Crea `colors = ['navy', 'royalblue', 'steelblue', 'cornflowerblue', 'skyblue', 'lightblue', 'lightyellow', 'yellow', 'orange', 'red']` e usa `colors[row]` come colore. Saprai che ha funzionato quando ogni riga ha un colore distinto.

4. **Riduci lo spazio.** Cambia `col * 40` e `row * 40` in `col * 20` e `row * 20` — e aumenta l'intervallo a 20. Saprai che ha funzionato quando 400 piccolissimi punti riempiono il canvas.

!!! mascot-celebration "Lavoro Fantastico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato `dot()`, cicli annidati, e una formula sulla dimensione per creare una griglia con profondità visiva —
    la stessa tecnica usata nelle visualizzazioni di dati per codificare una terza variabile come dimensione del punto!
    Prossimo: **Spicchi della Ruota dei Colori** — dividere il cerchio in 12 fette di tonalità pura.
