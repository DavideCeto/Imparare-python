---
hide:
    - toc
---
# Quadrati Sovrapposti

Alla fine di questo laboratorio sarai in grado di:

- Spostare forme diagonalmente per creare una sovrapposizione intenzionale
- Capire come l'**ordine di disegno** controlla quale forma appare sopra
- Pianificare una sequenza di colori così le aree sovrapposte sembrino intenzionali

Otto grandi quadrati, ognuno spostato di 25 pixel in diagonale dal precedente, si apre a ventaglio
in una cascata di colore — ogni nuovo quadrato copre parzialmente quello precedente.

!!! mascot-welcome "Benvenuto ai Quadrati Sovrapposti!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio imparerai come posizionare la stessa forma in posizioni leggermente diverse
    e usare il colore di riempimento e l'ordine di disegno per far sembrare belle le sovrapposizioni.
    Programmiamo insieme!

## Come Funziona la Sovrapposizione

Ogni quadrato inizia 25 pixel più a destra e 25 pixel più in basso del precedente.
Poiché i riempimenti di turtle sono **opachi**, ogni nuovo quadrato copre parte del precedente —
l'ultimo quadrato disegnato appare sempre sopra.

Un gradiente di colori (dal scuro al chiaro) rende ogni strato visivamente distinto.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['navy','royalblue','steelblue','cornflowerblue',
          'skyblue','lightskyblue','lightblue','aliceblue']
size = 200
offset = 25

for i in range(8):
    monty.penup()
    monty.goto(-200 + i * offset, 100 - i * offset)
    monty.pendown()
    monty.color(colors[i])
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.right(90)
    monty.end_fill()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    I quadrati sono disegnati da `i=0` (il più scuro, navy) a `i=7` (il più chiaro, aliceblue).
    Quale quadrato apparirà **sopra** — il più scuro o il più chiaro?
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

colors = ['navy','royalblue','steelblue','cornflowerblue',
          'skyblue','lightskyblue','lightblue','aliceblue']
size = 200
offset = 25

for i in range(8):
    monty.penup()
    monty.goto(-200 + i * offset, 100 - i * offset)
    monty.pendown()
    monty.color(colors[i])
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.right(90)
    monty.end_fill()`);
</script>

Il quadrato **più chiaro** (aliceblue, disegnato ultimo) si trova sopra. Avevi indovinato?

## Come Funziona

`monty.goto(-200 + i * offset, 100 - i * offset)` posiziona l'angolo in alto a sinistra di ogni quadrato.
Mentre `i` aumenta, x aumenta (spostandosi a destra) e y diminuisce (spostandosi in basso), creando la cascata diagonale.

La lista `colors` va dal più scuro al più chiaro. Poiché il più chiaro è disegnato ultimo e sopra, gli angoli più scuri sbirciano da sotto — creando una scalinata di colore visibile ai bordi.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `offset = 25` | Ogni quadrato si sposta di 25px a destra e 25px in basso |
| `goto(-200 + i*offset, 100 - i*offset)` | Posizionamento a scalinata diagonale |
| `colors[i]` | Un gradiente di blu dal navy scuro al quasi bianco |
| `for _ in range(4)` | Disegna i quattro lati di un quadrato |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Inverti la Pila"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna i quadrati ma nell'ordine sbagliato — il quadrato più scuro finisce
    sopra, coprendo quelli più chiari. Correggi il ciclo così il quadrato più chiaro sia disegnato ultimo.
    Suggerimento: inverti la lista o l'intervallo.

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

colors = ['navy','royalblue','steelblue','cornflowerblue',
          'skyblue','lightskyblue','lightblue','aliceblue']
size = 200
offset = 25

for i in range(7, -1, -1):
    monty.penup()
    monty.goto(-200 + i * offset, 100 - i * offset)
    monty.pendown()
    monty.color(colors[i])
    monty.begin_fill()
    for _ in range(4):
        monty.forward(size)
        monty.right(90)
    monty.end_fill()`);
</script>

Cambia `range(7, -1, -1)` di nuovo in `range(8)` — il più chiaro (indice 7) dovrebbe essere disegnato ultimo, apparendo sopra.

## Esperimenti

1. **Usa colori caldi.** Sostituisci il gradiente blu con `['darkred','firebrick','red','tomato','coral','lightsalmon','mistyrose','white']`. Saprai che ha funzionato quando la cascata brilla di rosso caldo.

2. **Aumenta l'offset.** Cambia `offset = 25` in `offset = 40`. I quadrati si separano maggiormente. Saprai che ha funzionato quando porzioni più grandi di ogni quadrato sono visibili.

3. **Sovrapponi nella direzione opposta.** Cambia `i * offset` in `-i * offset` nella formula x. La cascata va a sinistra invece che a destra. Saprai che ha funzionato quando il quadrato più chiaro è in basso a sinistra.

4. **Usa quadrati ruotati.** Dentro il ciclo interno, sostituisci `monty.right(90)` con `monty.right(90 + i)` per aggiungere una leggera rotazione ai quadrati successivi. Saprai che ha funzionato quando i quadrati si inclinano progressivamente.

!!! mascot-celebration "Lavoro Eccellente!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai esplorato l'ordine di disegno, i gradienti, e il posizionamento con offset —
    gli stessi principi che ogni gioco e animazione usa per stratificare la grafica sullo schermo!
    Prossimo: **Fiore con Funzione Petalo** per scoprire il potere delle funzioni riutilizzabili.
