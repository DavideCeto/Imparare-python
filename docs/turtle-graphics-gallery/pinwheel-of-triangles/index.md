---
hide:
    - toc
---
# Girandola di Triangoli

Alla fine di questo laboratorio sarai in grado di:

- Disegnare qualsiasi poligono regolare usando un ciclo e la formula dell'angolo `360 / sides`
- Ripetere una forma attorno a un punto centrale per costruire simmetria radiale
- Usare `begin_fill()` e `end_fill()` per riempire forme con il colore

Disegna 12 triangoli equilateri, ognuno ruotato di 30° dal precedente.
Pale oro e rosso scuro si aprono a ventaglio dal centro come i raggi di una ruota che gira.

!!! mascot-welcome "Benvenuto alla Girandola di Triangoli!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio disegnerai un triangolo alla volta, ruotando di 30° tra ognuno.
    Dodici triangoli × 30° = un cerchio completo di 360° — e una girandola straordinaria!
    Programmiamo insieme!

## Come Funziona la Girandola

Ogni triangolo equilatero ha tre angoli uguali di 60°.
Per disegnarne uno con la grafica turtle giri di **120°** a ogni angolo (l'angolo *esterno* — il supplemento di 60°).
Dopo tre lati la tartaruga è tornata esattamente dove ha iniziato, rivolta nella stessa direzione.

Poi `monty.right(30)` fa girare Monty di 30° in senso orario prima del triangolo successivo.
Dopo 12 triangoli, 12 × 30° = 360° — una rotazione completa — così ogni pala si apre a ventaglio uniformemente.

!!! mascot-tip "La Formula Magica"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Per distribuire **n** copie di qualsiasi forma uniformemente attorno a un punto centrale, ruota di `360 / n` gradi tra le copie.
    Qui n = 12, quindi `360 / 12 = 30`. Prova a cambiare 12 in 6 o 8 e vedi cosa succede!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)

colors = ['gold', 'darkred']
size = 120

for i in range(12):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for j in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()
    monty.right(30)

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ci sono 2 colori nella lista e 12 triangoli da disegnare.
    Quanti triangoli oro appariranno nella girandola finita?
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

colors = ['gold', 'darkred']
size = 120

for i in range(12):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for j in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()
    monty.right(30)

monty.hideturtle()`);
</script>

Esattamente **6 oro** e 6 rosso scuro — perché `i % 2` alterna 0 e 1 per ciascuna delle 12 iterazioni. Avevi indovinato?

## Come Funziona

Il programma ha due cicli annidati. Il **ciclo esterno** (`for i in range(12)`) si ripete 12 volte — una per ogni pala del triangolo. Il **ciclo interno** (`for j in range(3)`) disegna i tre lati di ogni triangolo.

Dentro il ciclo esterno:
- `monty.color(colors[i % 2])` sceglie oro quando `i` è pari, rosso scuro quando `i` è dispari
- `monty.begin_fill()` / `monty.end_fill()` racchiudono il ciclo interno per riempire il triangolo in modo solido
- `monty.right(30)` ruota Monty di 30° in senso orario *dopo* ogni triangolo completo così la pala successiva si apre verso l'esterno

L'intuizione chiave è che dopo tre passi `forward` + `left(120)`, la tartaruga atterra *esattamente* al centro rivolta nella direzione originale. La rotazione avviene *tra* i triangoli, non al loro interno.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = ['gold', 'darkred']` | Lista di due colori per alternare i colori delle pale |
| `size = 120` | Lunghezza del lato di ogni triangolo in pixel |
| `for i in range(12)` | Disegna 12 pale — una per iterazione del ciclo |
| `colors[i % 2]` | `i % 2` è 0 o 1, alternando i due colori |
| `monty.begin_fill()` | Inizia a registrare la forma da riempire |
| `for j in range(3)` | Disegna 3 lati — un triangolo equilatero |
| `monty.left(120)` | Gira a ogni angolo (angolo esterno del triangolo equilatero) |
| `monty.end_fill()` | Riempie il triangolo completato con il colore attuale |
| `monty.right(30)` | Ruota di 30° (= 360° ÷ 12) prima della pala successiva |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Rotazione Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 12 triangoli ma si sovrappongono tutti — nessuna girandola!
    Aggiungi **una riga** alla fine del ciclo esterno per distribuire le pale uniformemente attorno al centro.

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

colors = ['gold', 'darkred']
size = 120

for i in range(12):
    monty.color(colors[i % 2])
    monty.begin_fill()
    for j in range(3):
        monty.forward(size)
        monty.left(120)
    monty.end_fill()
    # AGGIUNGI QUI UNA RIGA per ruotare prima del triangolo successivo

monty.hideturtle()`);
</script>

La riga mancante è `monty.right(30)` — 360° diviso 12 pale = 30° per passo.

## Esperimenti

Prova questi cambiamenti nell'editor **Provalo Ora** sopra:

1. **Cambia il numero di pale.** Sostituisci `range(12)` con `range(6)` e `monty.right(30)` con `monty.right(60)`. Saprai che ha funzionato quando vedi una girandola a 6 pale con spazi più larghi tra le pale.

2. **Prova tre colori.** Cambia `colors` in `['gold', 'darkred', 'navy']`. Con 3 colori e 12 pale, il pattern si ripete ogni 3 pale. Saprai che ha funzionato quando vedi quattro gruppi di tre triangoli di colore diverso.

3. **Rendi le pale più grandi o più piccole.** Cambia `size = 120` in `size = 80` o `size = 160`. Saprai che ha funzionato quando i triangoli sono notevolmente più corti o più lunghi.

4. **Gira a sinistra invece di destra tra le pale.** Sostituisci `monty.right(30)` con `monty.left(30)`. Saprai che ha funzionato quando la girandola sembra identica — riesci a capire perché?

5. **Disegna pentagoni invece di triangoli.** Cambia il ciclo interno in `range(5)` e `monty.left(120)` in `monty.left(72)`. Saprai che ha funzionato quando ogni pala è un poligono a cinque lati invece di un triangolo.

!!! mascot-celebration "Lavoro Eccellente!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato la formula `360 / n`, cicli annidati, e forme riempite per costruire una girandola che gira!
    Lo stesso trucco di rotazione funziona per qualsiasi forma — provalo con quadrati, pentagoni, o esagoni.
    Prossimo: **Cerchi Annidati** per esplorare un tipo di ripetizione completamente diverso.
