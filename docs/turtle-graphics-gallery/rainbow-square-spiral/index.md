---
hide:
    - toc
---
# Spirale di Quadrati Arcobaleno

Alla fine di questo laboratorio sarai in grado di:

- Usare un ciclo `for` per ripetere un passo di disegno molte volte
- Scorrere una lista di colori usando l'operatore `%` (modulo)
- Vedere come aggiungere una piccola rotazione ogni volta crea un effetto spirale drammatico

Disegna un quadrato, gira un po', disegna un quadrato un po' più grande — e ripeti.
Dopo 36 quadrati ottieni un tunnel di colore luminoso che gira fuori dallo schermo.

!!! mascot-welcome "Benvenuto alla Spirale di Quadrati Arcobaleno!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio userai un ciclo per disegnare 36 quadrati, ruotando un po' ogni volta.
    Piccoli cambiamenti — solo 10 gradi e 8 pixel — si accumulano in qualcosa di spettacolare.
    Programmiamo insieme!

## Come Funziona la Spirale

Ogni volta che il ciclo gira, Monty disegna un quadrato e poi:

1. **Ruota** di 10 gradi a destra (così il quadrato successivo è leggermente girato)
2. **Cresce** la lunghezza del lato di 8 pixel (così il quadrato successivo è leggermente più grande)

Dopo 36 ripetizioni, quei piccoli cambiamenti si accumulano in una rotazione completa di 360 gradi e un quadrato che è largo quasi 300 pixel — partendo da appena 20.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
side = 20

for i in range(36):
    monty.color(colors[i % len(colors)])
    for j in range(4):
        monty.forward(side)
        monty.right(90)
    monty.right(10)
    side += 8

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo esterno gira 36 volte e ci sono 6 colori nella lista.
    Quante volte apparirà ogni colore nella spirale finita?
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
monty.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
side = 20

for i in range(36):
    monty.color(colors[i % len(colors)])
    for j in range(4):
        monty.forward(side)
        monty.right(90)
    monty.right(10)
    side += 8

monty.hideturtle()`);
</script>

Ogni colore appare esattamente **6 volte** — perché 36 ÷ 6 = 6, e `i % 6` scorre tra 0 → 1 → 2 → 3 → 4 → 5 → 0 → 1 → … Avevi indovinato?

## Come Funziona

Il programma usa **due cicli annidati**. Il ciclo esterno (`for i in range(36)`) gira una volta per ogni quadrato. Il ciclo interno (`for j in range(4)`) disegna i quattro lati di ogni quadrato: avanti, gira 90°, avanti, gira 90°, e così via.

Dopo che il ciclo interno finisce un quadrato, il ciclo esterno fa altre due cose prima di iniziare il quadrato successivo:

- `monty.right(10)` — ruota Monty di 10 gradi, così il quadrato successivo è leggermente ruotato
- `side += 8` — rende il quadrato successivo 8 pixel più largo su ogni lato

Il colore è scelto con `colors[i % len(colors)]`. L'operatore `%` dà il **resto** dopo la divisione, così `i % 6` produce sempre un numero da 0 a 5, scorrendo la lista non importa quanto grande diventi `i`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.speed(0)` | Velocità massima — nessun ritardo di animazione |
| `colors = [...]` | Una lista di 6 nomi di colore da scorrere |
| `side = 20` | Lunghezza del lato iniziale del primo (più piccolo) quadrato |
| `for i in range(36)` | Ripete il blocco di disegno del quadrato 36 volte |
| `colors[i % len(colors)]` | Sceglie il colore alla posizione `i mod 6`, scorrendo la lista |
| `for j in range(4)` | Disegna 4 lati per fare un quadrato |
| `monty.right(90)` | Gira a ogni angolo del quadrato |
| `monty.right(10)` | Ruota di 10° prima del quadrato successivo — crea la spirale |
| `side += 8` | Fa crescere il quadrato di 8 pixel a ogni iterazione |

!!! mascot-tip "Cos'è il Modulo?"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    L'operatore `%` ti dà il **resto** della divisione.
    `7 % 3` è `1` (7 ÷ 3 = 2 resto 1).
    È lo strumento perfetto per scorrere una lista — l'indice rimane sempre nei limiti!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Completa la Spirale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna i quadrati ma tutti dello stesso colore — che noia!
    Aggiungi **una riga** dentro il ciclo esterno per far usare a ogni quadrato il colore successivo nella lista.
    Suggerimento: guarda come sono usati `colors` e `i` nell'esempio sopra.

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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
side = 20

for i in range(36):
    # ADD ONE LINE HERE to set the color
    for j in range(4):
        monty.forward(side)
        monty.right(90)
    monty.right(10)
    side += 8

monty.hideturtle()`);
</script>

La riga mancante è `monty.color(colors[i % len(colors)])` — posizionala subito dopo la riga `for i`.

## Esperimenti

Prova questi cambiamenti nell'editor **Provalo Ora** sopra:

1. **Cambia il numero di quadrati.** Sostituisci `range(36)` con `range(72)`. Come cambia la spirale? Saprai che ha funzionato quando la spirale si avvolge due volte più lontano.

2. **Cambia l'angolo di rotazione.** Sostituisci `monty.right(10)` con `monty.right(5)`. Ora 36 quadrati coprono solo 180 gradi. Cosa succede alla forma? Saprai che ha funzionato quando la spirale si apre a ventaglio invece di un tunnel chiuso.

3. **Cambia la velocità di crescita.** Sostituisci `side += 8` con `side += 4`. La spirale diventa più stretta. Cosa fa `side += 16`? Saprai che ha funzionato quando i quadrati si espandono molto più rapidamente ai bordi del canvas.

4. **Inverti la direzione della spirale.** Cambia `monty.right(10)` in `monty.left(10)`. Saprai che ha funzionato quando la spirale si avvolge nella direzione opposta.

5. **Aggiungi più colori.** Aggiungi `'pink'` e `'brown'` alla lista dei colori. Con 8 colori e 36 quadrati, ogni colore appare solo 4–5 volte. La spirale sembra diversa con più strisce? Saprai che ha funzionato quando puoi contare più di 6 fasce di colore distinte.

!!! mascot-celebration "Lavoro Spettacolare!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena usato cicli annidati, una lista di colori, l'operatore modulo, e una variabile crescente
    per produrre un tunnel arcobaleno sbalorditivo — tutto in meno di 20 righe di codice!
    Prossimo: prova la **Girandola di Triangoli** per vedere come la stessa idea
    di rotazione funziona con una forma completamente diversa.
