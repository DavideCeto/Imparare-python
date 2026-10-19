---
title: Cicli For e Disegno di Forme
description: Usa il ciclo for di Python e range() per disegnare quadrati, poligoni e pattern a stella con la grafica turtle — poi esplora il posizionamento assoluto e il controllo dello schermo.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 10:25:00
version: 0.09
---

# Cicli For e Disegno di Forme

## Riepilogo

I cicli ti permettono di ripetere passaggi senza copiare e incollare — proprio come un
blocco "repeat" di Scratch. Il ciclo `for` con `range()` è il cavallo di battaglia di Python
per contare. Questo capitolo usa i cicli per disegnare quadrati, triangoli e altri poligoni
con turtle, poi introduce il posizionamento assoluto (`goto()`), la pulizia dello schermo,
le interrogazioni di posizione, e un classico progetto di pattern a stella.

## Concetti Trattati

Questo capitolo tratta i seguenti 11 concetti del grafo di apprendimento:

1. for Loop over Sequence
2. for Loop with range()
3. Range with Start Stop Step
4. Loop Counter Variable
5. Loop Accumulator Pattern
6. Absolute Positioning goto()
7. Drawing circle() and Polygons
8. Clearing and Resetting
9. Position Query xcor() ycor()
10. setheading() Direction
11. Drawing Star Patterns

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 5: Disegnare con la Grafica Turtle](../05-drawing-with-turtle/index.md)
- [Capitolo 6: Matematica e Aritmetica](../06-math-and-arithmetic/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Usare un ciclo `for` con `range()` per ripetere comandi turtle un numero qualsiasi di volte
- Disegnare qualsiasi poligono regolare combinando un ciclo con la formula `360 / lati`
- Usare `goto()`, `setheading()` e `circle()` per controllare con precisione la posizione della turtle
- Disegnare una classica stella a cinque punte usando il contatore del ciclo

Nel Capitolo 5 hai disegnato un quadrato parziale scrivendo quattro comandi `forward()` e `right()` in fila.
In questo capitolo scriverai lo stesso disegno con solo **due righe** dentro un ciclo — e poi userai quella stessa idea per disegnare forme con 100 lati.

!!! mascot-welcome "Benvenuto/a al Capitolo 7!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I cicli sono una delle idee più grandi della programmazione. Una volta che li capisci, non copierai e incollerai mai più codice — dirai semplicemente a Python quante volte ripetere qualcosa e lascerai che faccia il lavoro. Programmiamo insieme!

## Il Ciclo for

Un **ciclo for** ripete un blocco di codice un numero prefissato di volte.
In Python, la forma più comune usa **`range()`** per contare:

```python
for i in range(4):
    print(i)
```

Questo stampa `0`, `1`, `2`, `3` — quattro numeri, a partire da zero.
La riga indentata (`print(i)`) è il **corpo del ciclo** — tutto ciò che Python ripete.
La variabile `i` è il **contatore del ciclo** — cambia valore a ogni giro del ciclo.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, il blocco **Repeat** esegue il suo contenuto un numero fisso di volte. Il `for i in range(n):` di Python fa esattamente la stessa cosa! La grande differenza: Python ti dà anche il contatore `i` come variabile che puoi usare dentro il ciclo — ottimo per creare pattern che cambiano a ogni passo.

Ora mettiamo al lavoro un ciclo `for` con la turtle.
Prima di eseguire il programma qui sotto, pensa a cosa disegneranno `forward(100)` e `right(90)` ripetuti quattro volte.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo gira **4 volte**. Ogni volta, la turtle si muove avanti di 100 pixel e gira a destra di 90°.
    Una svolta di 90° a destra è un angolo perfetto. Quale forma pensi apparirà?
    Fai la tua previsione — poi clicca su Run!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato.

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
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)`);
</script>

Avevi indovinato? Due righe dentro un ciclo disegnano un quadrato completo — la stessa forma che nel Capitolo 5 ha richiesto otto righe!

## Come Funziona il Ciclo

Ecco cosa fa Python a ogni giro del ciclo:

| Giro | Valore di `i` | Cosa fa la turtle |
|------|-----------|----------------------|
| 1° | `0` | avanti 100, gira a destra 90° |
| 2° | `1` | avanti 100, gira a destra 90° |
| 3° | `2` | avanti 100, gira a destra 90° |
| 4° | `3` | avanti 100, gira a destra 90° |

Dopo quattro svolte di 90° la turtle ha ruotato di un giro completo di 360° ed è rivolta nella sua direzione originale — ed è per questo che la forma si chiude perfettamente in un quadrato.

**L'indentazione conta.** Le due righe dentro il ciclo (`t.forward(100)` e `t.right(90)`) devono essere entrambe indentate esattamente di quattro spazi (o un Tab). Python usa l'indentazione per sapere quali righe appartengono al corpo del ciclo e quali vengono *dopo* il ciclo.

```python
for i in range(4):
    t.forward(100)    # ← parte del ciclo (indentata)
    t.right(90)       # ← parte del ciclo (indentata)
t.penup()             # ← NON fa parte del ciclo (nessuna indentazione)
```

### Osservalo: Procedi Passo Passo nel Ciclo

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nello stepper qui sotto, osserva il valore di `i` nel badge in alto.
    Quanto varrà `i` al primissimo giro — 1 o 0? E quante volte la freccia
    salterà indietro verso la riga `for`? Fai le tue previsioni, poi procedi
    passo passo e verifica!

<iframe src="../../sims/for-loop-stepper/main.html" height="502" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim For-Loop Stepper](../../sims/for-loop-stepper/index.md){ .md-button }

Avevi indovinato? Il programma **Countdown** nel menu a tendina mostra lo stesso ritmo con print(), e **Running Total** anticipa il pattern accumulatore che incontrerai più avanti in questo capitolo.

## Capire range()

`range()` può accettare uno, due o tre argomenti:

| Forma | Cosa produce | Output di esempio |
|------|-----------------|----------------|
| `range(n)` | 0, 1, 2, …, n-1 | `range(4)` → 0 1 2 3 |
| `range(start, stop)` | start, start+1, …, stop-1 | `range(2, 6)` → 2 3 4 5 |
| `range(start, stop, step)` | start, start+step, …, < stop | `range(0, 10, 2)` → 0 2 4 6 8 |

L'argomento **step** ti permette di saltare valori o contare all'indietro:

```python
for i in range(0, 360, 45):
    print(i)    # 0, 45, 90, 135, 180, 225, 270, 315
```

Questo è utile per disegnare forme a intervalli angolari regolari — per esempio, disegnare otto linee che si irradiano dal centro come i raggi di una ruota, ciascuna distanziata di 45°.

### Osservalo: Il Range Explorer

La cosa più insidiosa di `range()` è che il **valore di stop non è mai incluso**. Nell'esploratore qui sotto, il valore di stop è disegnato come un anello arancione vuoto — il conteggio si ferma sempre appena prima. Prima di muovere qualsiasi cosa, prevedi: **quali numeri produce `range(2, 12, 3)`?** Poi verifica sulla linea dei numeri.

<iframe src="../../sims/range-explorer/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Range Explorer](../../sims/range-explorer/index.md){ .md-button }

Quando ti senti sicuro/a, clicca su **New Challenge** — il simulatore mostra anelli bersaglio verdi, e il tuo compito è trovare le impostazioni dei cursori che li accendono esattamente.

## La Variabile Contatore del Ciclo

Il contatore `i` è una variabile vera — puoi usarla *dentro* il corpo del ciclo.
Questo ti permette di rendere ogni passo leggermente diverso:

```python
import turtle
t = turtle.Turtle()
for i in range(5):
    t.forward(20 + i * 20)   # 20, 40, 60, 80, 100
    t.right(90)
```

Ogni passo in avanti diventa 20 pixel più lungo perché `i` cresce di 1 a ogni giro.
Il risultato è una forma a scala invece di un quadrato.

## Il Pattern Accumulatore del Ciclo

Un **accumulatore** è una variabile che imposti *prima* del ciclo e aggiorni *dentro* il ciclo a ogni passo.
L'accumulatore più comune semplicemente somma dei valori insieme:

```python
total = 0               # l'accumulatore parte da zero
for i in range(1, 6):   # i takes values 1, 2, 3, 4, 5
    total += i          # aggiunge i a total a ogni giro
print(total)            # 15  (1+2+3+4+5)
```

Userai il pattern accumulatore costantemente — per contare cose, sommare punteggi, e costruire stringhe carattere per carattere.

## Disegnare Qualsiasi Poligono Regolare

Combina il ciclo `for` con la formula `360 / lati` del Capitolo 6 e puoi disegnare qualsiasi poligono regolare:

```python
import turtle
t = turtle.Turtle()
sides = 6
turn_angle = 360 / sides
for i in range(sides):
    t.forward(80)
    t.right(turn_angle)
```

Cambia `sides` in qualsiasi numero e il ciclo si adatta automaticamente.

## Altri Comandi Turtle

Con il ciclo padroneggiato, è tempo di aggiungere comandi turtle di precisione al tuo repertorio.
Prima di guardarli uno per uno, ecco un riferimento rapido:

| Comando | Cosa fa |
|---------|-------------|
| `t.goto(x, y)` | Salta alla posizione (x, y) — il centro della tela è (0, 0) |
| `t.setheading(angle)` | Orienta la turtle verso una direzione esatta della bussola |
| `t.circle(radius)` | Disegna un cerchio con il raggio indicato |
| `t.xcor()` | Restituisce la posizione x attuale della turtle |
| `t.ycor()` | Restituisce la posizione y attuale della turtle |
| `t.clear()` | Cancella tutto ciò che la turtle ha disegnato, ma mantiene la turtle |
| `t.reset()` | Cancella i disegni E riporta la turtle all'inizio |

**Posizionamento assoluto con `goto(x, y)`.** La tela ha un sistema di coordinate dove `(0, 0)` è il centro. La x positiva è a destra, la y positiva è in alto, la x negativa è a sinistra, la y negativa è in basso. `t.goto(100, 0)` sposta la turtle in un punto 100 pixel a destra del centro — disegnando una linea lì a meno che tu non chiami prima `t.penup()`.

**Orientarsi con `setheading(angle)`.** L'orientamento si misura in gradi a partire dall'asse x positivo (Est), in senso antiorario:
- `0` = Est (destra)
- `90` = Nord (su)
- `180` = Ovest (sinistra)
- `270` = Sud (giù)

**Disegnare con `circle(radius)`.** `t.circle(50)` disegna un cerchio con un raggio di 50 pixel, a partire da dove si trova attualmente la turtle.

**Interrogare la posizione.** `t.xcor()` e `t.ycor()` restituiscono le coordinate x e y attuali della turtle come float.
Questo è utile per stampare i progressi o per posizionare del testo nella posizione della turtle.

## Disegnare Pattern a Stella

Una **stella a cinque punte** è una delle forme più soddisfacenti da disegnare con un ciclo.
Il trucco è l'angolo di svolta: `144°` per punta.

Ecco come funziona la matematica:
- Una stella a cinque punte ha 5 punte
- A ogni punta, la turtle gira di `360° × 2 / 5` = `144°`
  (percorre *due* rotazioni complete intorno alla stella invece di una)

Il programma qui sotto disegna quattro delle cinque punte — manca l'angolo di svolta corretto.

!!! mascot-thinking "Tocca a Te — Completa la Stella"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La turtle qui sotto disegna linee ma non chiude mai la stella perché l'angolo di svolta è sbagliato.
    Sostituisci `???` con il numero corretto di gradi così la turtle traccia tutte e cinque le punte
    e torna esattamente al punto di partenza.
    **Suggerimento:** l'angolo di svolta per una stella a 5 punte è `144`.

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
t = turtle.Turtle()
t.speed(3)
for i in range(5):
    t.forward(150)
    t.right(???)    # sostituisci ??? con l'angolo di rotazione corretto`);
</script>

Quando la stella si chiude perfettamente tornando al punto di partenza, sai che l'angolo di svolta è corretto!

## Esperimenti

Prova questi cambiamenti al programma della stella qui sopra. Per ciascuno, prevedi prima cosa succederà, poi eseguilo per verificare!

1. Cambia `range(5)` in `range(7)` e l'angolo di svolta in `154` (circa `360 * 2 / 7`). **Saprai che ha funzionato quando** vedi una stella a sette punte.
2. Cambia `t.forward(150)` in `t.forward(i * 30 + 30)`. **Saprai che ha funzionato quando** ogni braccio della stella diventa più lungo del precedente.
3. Aggiungi `t.pencolor("red")` prima del ciclo. **Saprai che ha funzionato quando** la stella viene disegnata in rosso.
4. Dopo il ciclo della stella, aggiungi `t.penup()`, `t.goto(0, 0)`, `t.pendown()` e `t.circle(80)`. **Saprai che ha funzionato quando** appare un cerchio al centro della stella.
5. Cambia `t.speed(3)` in `t.speed(1)` e guarda Monty disegnare lentamente, oppure `t.speed(10)` per la velocità massima.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato una delle idee più importanti di tutta la programmazione — il ciclo. Con solo due righe dentro un blocco `for` hai disegnato un quadrato, poi un poligono, poi una stella. Hai anche imparato `goto()`, `circle()` e `setheading()` per un controllo preciso della turtle. Questi strumenti saranno il tuo kit di disegno per il resto del corso. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
