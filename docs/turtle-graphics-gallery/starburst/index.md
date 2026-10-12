---
hide:
    - toc
---
# Raggiera a Stella

Alla fine di questo laboratorio sarai in grado di:

- Disegnare linee che si irradiano verso l'esterno da un singolo punto centrale
- Scorrere una lista di colori usando l'operatore modulo
- Calcolare quante linee servono per riempire una rotazione completa di 360°

Trentasei linee esplodono verso l'esterno dal centro, cambiando colore da giallo ad arancione
a rosso — come raggi di sole catturati a metà esplosione.

!!! mascot-welcome "Benvenuto alla Raggiera a Stella!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio disegnerai una linea, torni al centro, girerai, e ripeterai — 36 volte.
    Il trucco è che `forward` e `backward` insieme agiscono come un raggio a due vie.
    Programmiamo insieme!

## Come Funziona la Raggiera

La tartaruga inizia al centro. Ogni iterazione:
1. Disegna una linea di lunghezza 150 verso l'esterno (`forward`)
2. Ritorna al centro (`backward` della stessa distanza)
3. Gira di 10° in senso orario (`right(10)`) prima del raggio successivo

Dopo 36 raggi: 36 × 10° = 360° — esattamente una rotazione completa, riempiendo completamente il cerchio.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['yellow', 'orange', 'red']
length = 150

for i in range(36):
    monty.color(colors[i % 3])
    monty.forward(length)
    monty.backward(length)
    monty.right(10)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ci sono 3 colori e 36 raggi. Quanti raggi **rossi** appariranno nella raggiera finita?
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

colors = ['yellow', 'orange', 'red']
length = 150

for i in range(36):
    monty.color(colors[i % 3])
    monty.forward(length)
    monty.backward(length)
    monty.right(10)`);
</script>

36 ÷ 3 = **12 raggi rossi** (e 12 gialli, 12 arancioni). Avevi indovinato?

## Come Funziona

`forward(length)` muove Monty verso l'esterno dal centro lungo la direzione attuale.
`backward(length)` riporta Monty esattamente allo stesso punto di partenza.
`right(10)` ruota la direzione di 10° in senso orario così il raggio successivo punta in una nuova direzione.

Il colore scorre perché `i % 3` produce 0, 1, 2, 0, 1, 2, … non importa quanto grande diventi `i`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = ['yellow', 'orange', 'red']` | Gradiente a tre colori dal caldo al rovente |
| `length = 150` | Lunghezza di ogni raggio in pixel |
| `monty.color(colors[i % 3])` | Scorre uniformemente tra i tre colori |
| `monty.forward(length)` | Disegna il raggio verso l'esterno |
| `monty.backward(length)` | Ritorna al centro — nessun `penup()` necessario |
| `monty.right(10)` | Rotazione di 10° × 36 iterazioni = cerchio completo di 360° |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna i raggi ma non riempiono il cerchio completo — c'è uno spazio vuoto!
    Trova e correggi l'unico numero sbagliato così tutti i 36 raggi si distribuiscono uniformemente attorno ai 360°.

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

colors = ['yellow', 'orange', 'red']
length = 150

for i in range(36):
    monty.color(colors[i % 3])
    monty.forward(length)
    monty.backward(length)
    monty.right(5)`);
</script>

`right(5)` × 36 = solo 180° — metà cerchio. Cambialo in `right(10)` per un 360° completo.

## Esperimenti

1. **Cambia il numero di raggi.** Sostituisci `range(36)` con `range(72)` e `right(10)` con `right(5)`. Saprai che ha funzionato quando il doppio di raggi più sottili riempiono il cerchio.

2. **Usa più colori.** Cambia `colors` in `['yellow', 'gold', 'orange', 'darkorange', 'red', 'darkred']` e `i % 3` in `i % 6`. Saprai che ha funzionato quando il gradiente ha sei fasce di colore distinte.

3. **Rendi i raggi di lunghezze diverse.** Sostituisci `length = 150` con `length = 50 + i * 3`. I primi raggi sono corti; quelli successivi sono lunghi. Saprai che ha funzionato quando la raggiera sembra una lacrima.

4. **Disegna solo ogni altro raggio.** Aggiungi `if i % 2 == 0:` prima della riga `forward` (e indenta le due righe successive). Saprai che ha funzionato quando appaiono solo 18 raggi con spazi tra loro.

!!! mascot-celebration "Lavoro Brillante!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato avanti + indietro per disegnare raggi, il modulo per il ciclo dei colori, e la matematica
    per dimostrare che 36 × 10° = 360°. Questa è geometria E Python in un unico programma!
    Prossimo: **Griglia a Scacchiera** per esplorare cicli annidati e aritmetica delle coordinate.
