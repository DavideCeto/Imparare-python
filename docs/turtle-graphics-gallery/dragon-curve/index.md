---
hide:
    - toc
---
# Curva del Dragone

Alla fine di questo laboratorio sarai in grado di:

- Costruire la Curva del Dragone piegando ripetutamente una lista di rotazioni
- Capire come una sequenza di rotazioni L/R (sinistra/destra) codifica un percorso frattale
- Vedere come la manipolazione di liste può sostituire le chiamate ricorsive per alcuni frattali

La Curva del Dragone — o Dragone di Heighway — sembra una striscia di carta piegata e poi distesa. Dopo 12 piegature, il percorso si avvolge e riempie lo spazio in un bellissimo pattern che non si incrocia mai.

!!! mascot-welcome "Benvenuto alla Curva del Dragone!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La Curva del Dragone appare sulle intestazioni dei capitoli del libro *Jurassic Park*!
    In questo laboratorio la costruirai simulando la piegatura della carta con una lista. Programmiamo insieme!

## Come Funziona

Immagina di piegare a metà ripetutamente una striscia di carta, sempre piegando a destra. Quando la distendi, vedi una sequenza di pieghe a sinistra e a destra. Nel codice le scriviamo con le iniziali inglesi: 'L' (*left*, sinistra) e 'R' (*right*, destra). La Curva del Dragone è ciò che ottieni quando disegni quelle pieghe come rotazioni di 90°.

La regola della piegatura: prendi la sequenza attuale, aggiungi una 'R', poi aggiungi la stessa sequenza letta al contrario e con le svolte scambiate ('L' diventa 'R' e 'R' diventa 'L').

Dopo 12 piegature, hai `2^12 - 1 = 4095` rotazioni.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('darkorchid')
monty.pensize(1)

turns = ['R']
for _ in range(12):
    turns = turns + ['R'] + [('L' if t == 'R' else 'R') for t in reversed(turns)]

monty.penup()
monty.goto(-80, 80)
monty.pendown()

step = 4
for t in turns:
    monty.forward(step)
    if t == 'R':
        monty.right(90)
    else:
        monty.left(90)
monty.forward(step)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Dopo 12 piegature, il percorso si incrocerà, o in qualche modo eviterà l'auto-intersezione?
    La Curva del Dragone ha una proprietà sorprendente — fai la tua previsione poi esegui per scoprirlo!

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
monty.pencolor('darkorchid')
monty.pensize(1)

turns = ['R']
for _ in range(12):
    turns = turns + ['R'] + [('L' if t == 'R' else 'R') for t in reversed(turns)]

monty.penup()
monty.goto(-80, 80)
monty.pendown()

step = 4
for t in turns:
    monty.forward(step)
    if t == 'R':
        monty.right(90)
    else:
        monty.left(90)
monty.forward(step)`);
</script>

La Curva del Dragone **non si incrocia mai** — il percorso riempie lo spazio senza che due segmenti si sovrappongano. Avevi indovinato?

## Come Funziona

La regola della piegatura raddoppia la lista a ogni iterazione. Dopo la piegatura `n`, la lista ha `2^n - 1` voci. Il nuovo elemento centrale è sempre 'R' (la direzione di piegatura più recente). La metà destra è la vecchia lista letta al contrario e con le svolte scambiate (L↔R) — questo è ciò che sembra la metà piegata vista dall'estremità distesa.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `turns = ['R']` | Inizia con una piegatura |
| `turns + ['R'] + [...]` | Aggiunge il marcatore di piegatura e la vecchia sequenza letta al contrario e con le svolte scambiate |
| `('L' if t == 'R' else 'R')` | Scambia ogni rotazione: 'L' (sinistra) diventa 'R' (destra) e viceversa |
| `reversed(turns)` | Legge la vecchia sequenza al contrario (l'altro lato della piegatura) |
| `if t == 'R': right(90)` | Traduce la lista di rotazioni in movimenti della tartaruga |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Riduci a 8 Piegature"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `range(12)` in `range(8)`. Quante rotazioni avrà il percorso?
    (Suggerimento: `2^8 - 1 = ?`). Prevedi, poi esegui per controllare!

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
monty.pencolor('darkorchid')
monty.pensize(1)

turns = ['R']
for _ in range(8):
    turns = turns + ['R'] + [('L' if t == 'R' else 'R') for t in reversed(turns)]

monty.penup()
monty.goto(-80, 80)
monty.pendown()

step = 6
for t in turns:
    monty.forward(step)
    if t == 'R':
        monty.right(90)
    else:
        monty.left(90)
monty.forward(step)`);
</script>

8 piegature → `2^8 - 1 = 255` rotazioni. La forma è riconoscibilmente simile a un dragone ma più semplice di 12 piegature.

## Esperimenti

1. **Usa un passo più grande.** Cambia `step = 4` in `step = 6`. La curva riempie più canvas. Saprai che ha funzionato quando la forma del dragone è più grande.

2. **Colora per posizione.** Aggiungi una lista di colori e `monty.pencolor(colors[i % len(colors)])` dentro il ciclo. Saprai che ha funzionato quando il percorso è multicolore.

3. **Prova 15 piegature.** Cambia in `range(15)` (più lento ma più dettagliato). Saprai che ha funzionato quando vedi una curva molto più densa e che riempie più spazio.

4. **Stampa le prime 10 rotazioni.** Aggiungi `print(turns[:10])` prima del ciclo di disegno. Saprai che ha funzionato quando vedi la sequenza `['R', 'R', 'L', 'R', 'R', 'L', 'L', 'R', 'R', 'R']`.

!!! mascot-celebration "Un Dragone di Carta nel Codice!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un frattale usando la **manipolazione di liste** invece della ricorsione — un approccio
    completamente diverso alla stessa idea! Entrambi codificano la stessa struttura auto-simile.
    Prossimo: **Curva di Hilbert** — una curva che riempie lo spazio usando la ricorsione mutua.
