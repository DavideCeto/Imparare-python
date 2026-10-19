---
title: Cicli While e Animazione
description: Usa i cicli while, break, continue e il modulo time per costruire programmi di conto alla rovescia e disegni animati con la tartaruga che si muovono da soli.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 11:10:00
version: 0.09
---

# Cicli While e Animazione

## Riepilogo

I cicli `while` continuano a girare finché una condizione è vera — perfetti per giochi
e animazioni. Questo capitolo tratta `while`, come fermare i cicli con `break`,
saltare le iterazioni con `continue`, la clausola `else` sui cicli, i pericoli dei
cicli infiniti, i cicli di conto alla rovescia e il modulo `time`. Finirai con un
vero disegno animato con la tartaruga che si muove da solo.

## Concetti Trattati

Questo capitolo tratta i seguenti 10 concetti del grafo di apprendimento:

1. while Loop
2. break Statement
3. continue Statement
4. else Clause on Loops
5. Nested Loops
6. Infinite Loops to Avoid
7. Countdown Loop
8. time Module Overview
9. time.sleep()
10. Animation with Turtle Loops

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 5: Disegnare con la Grafica Turtle](../05-drawing-with-turtle/index.md)
- [Capitolo 7: Cicli For e Disegno di Forme](../07-for-loops-and-shapes/index.md)
- [Capitolo 9: Prendere Decisioni con If/Else](../09-decisions-if-else/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Scrivere un ciclo `while` che gira finché una condizione è `True`
- Usare `break` per uscire da un ciclo in anticipo e `continue` per saltare un'iterazione
- Spiegare perché si verificano i cicli infiniti e come evitarli
- Costruire una spirale animata con la tartaruga che cresce passo dopo passo usando un ciclo `while`

Il ciclo `for` che hai imparato nel Capitolo 7 è perfetto quando sai esattamente quante volte ripetere — `for i in range(10)` si ripete esattamente dieci volte.
Ma cosa succede se non sai in anticipo quando fermarti?
Cosa succede se vuoi continuare a contare alla rovescia finché un razzo non viene lanciato, o continuare a disegnare finché la tartaruga non raggiunge il bordo dello schermo?
È allora che hai bisogno di un **ciclo `while`**.

!!! mascot-welcome "Benvenuto/a al Capitolo 10!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il ciclo `while` è dove i programmi prendono vita — è il motore dietro ai giochi, alle animazioni e a tutto ciò che gira finché qualcosa non cambia. Alla fine di questo capitolo, Monty la tartaruga disegnerà tutto da solo! Programmiamo insieme!

## Il Ciclo while

Un **ciclo `while`** ripete il suo corpo finché una condizione è `True`.
La struttura assomiglia a un'istruzione `if`, ma invece di girare una sola volta, continua a girare:

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Decollo!")
```

Ecco cosa succede passo dopo passo:

| Passo | Valore di `count` | Condizione `count > 0` | Azione |
|------|--------------|----------------------|--------|
| 1 | 5 | True | stampa 5, count diventa 4 |
| 2 | 4 | True | stampa 4, count diventa 3 |
| 3 | 3 | True | stampa 3, count diventa 2 |
| 4 | 2 | True | stampa 2, count diventa 1 |
| 5 | 1 | True | stampa 1, count diventa 0 |
| 6 | 0 | **False** | il ciclo finisce, stampa "Decollo!" |

Il ciclo gira esattamente finché la condizione resta `True`.
Nel momento in cui diventa `False`, Python esce dal ciclo e continua con la riga successiva.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, il blocco **Ripeti finché** continua a eseguire il suo contenuto finché una condizione non diventa vera. Il ciclo `while` di Python è la stessa idea — tranne che la condizione viene controllata **all'inizio** di ogni giro: il ciclo continua mentre la condizione è `True` e si ferma nel momento in cui diventa `False`.

Prima di eseguire il programma di conto alla rovescia, pensa a cosa stamperà.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La variabile `count` parte da `5`. Il ciclo stampa `count` e poi sottrae 1 a ogni giro.
    Quante righe pensi che il programma stamperà prima che appaia "Decollo!"?
    Stamperà il numero `0`? Fai la tua previsione — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

<div class="cm-lab cm-text-only">
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
initCmLab('', `count = 5
while count > 0:
    print(count)
    count -= 1
print("Decollo!")`);
</script>

Avevi indovinato? Il ciclo stampa `5`, `4`, `3`, `2`, `1` — cinque righe — e poi `"Decollo!"`.
Il numero `0` **non** viene stampato perché la condizione `count > 0` viene controllata *prima* di ogni giro.
Quando `count` è `0`, la condizione è `False`, quindi il ciclo finisce immediatamente.

## Cicli Infiniti da Evitare

Un **ciclo infinito** è un ciclo `while` la cui condizione non diventa mai `False`.
Il programma gira per sempre (finché non lo chiudi forzatamente):

```python
# ATTENZIONE: questo gira all'infinito — non eseguirlo!
while True:
    print("Help, I can't stop!")
```

I cicli infiniti si verificano quando dimentichi di cambiare la variabile da cui dipende la condizione.
La causa più comune: dimenticare `count -= 1` dentro il ciclo.

```python
count = 5
while count > 0:
    print(count)
    # MANCA: count -= 1  ← senza questa riga, count resta 5 per sempre!
```

**Come risolverlo:** Ogni ciclo `while` ha bisogno di almeno una riga al suo interno che alla fine rende la condizione `False`.
Controlla sempre: "Cosa cambia dentro questo ciclo per fermarlo alla fine?"

### Guardalo: Controlla, Esegui, Controlla di Nuovo

Un ciclo while ha un ritmo: **controlla** la condizione, **esegui** il corpo, torna indietro, **controlla** di nuovo. Il simulatore sotto stampa un verdetto True o False ogni volta che la condizione viene controllata. Prima di cliccare, prevedi: **per un conto alla rovescia che parte da 3, quante volte gira il corpo — e quante volte viene controllata la condizione?** (Non sono lo stesso numero!)

<iframe src="../../sims/while-loop-stepper/main.html" height="502" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim While-Loop Stepper](../../sims/while-loop-stepper/index.md){ .md-button }

Poi scegli il programma **Infinite Bug** — è esattamente il bug del decremento mancante visto sopra, in esecuzione in una gabbia sicura. Guarda il contachilometri dei giri girare e la condizione segnare True, True, True... per sempre. Skulpt ti protegge da questo nei laboratori, ma il vero Python non lo farà!

## L'Istruzione break

`break` esce immediatamente da un ciclo, anche se la condizione è ancora `True`.
È utile quando vuoi fermarti in base a qualcosa che succede *dentro* il ciclo:

```python
count = 10
while count > 0:
    print(count)
    if count == 7:
        print("Mi fermo prima, al 7!")
        break
    count -= 1
```

Questo conto alla rovescia si ferma a `7` e non raggiunge mai `6` o valori inferiori — il `break` salta fuori dal ciclo completamente.

## L'Istruzione continue

`continue` salta il resto del giro attuale del ciclo e va direttamente al controllo successivo della condizione.
Usalo per saltare certi valori senza fermare l'intero ciclo:

```python
count = 10
while count > 0:
    count -= 1
    if count % 2 == 0:   # salta i numeri pari
        continue
    print(count)         # stampa solo i numeri dispari: 9, 7, 5, 3, 1
```

Pensa a `break` come "esci dal ciclo completamente" e a `continue` come "salta questo giro e riprova."

## La Clausola else sui Cicli

Python ha una caratteristica inusuale: puoi aggiungere una clausola `else` a un ciclo `while`.
Il blocco `else` gira solo se il ciclo è terminato *naturalmente* (la condizione è diventata `False`) — non se è terminato tramite `break`:

```python
count = 3
while count > 0:
    print(count)
    count -= 1
else:
    print("Conto alla rovescia terminato normalmente!")   # viene eseguito perché non è stato usato break
```

```python
count = 3
while count > 0:
    if count == 2:
        break
    print(count)
    count -= 1
else:
    print("Questo non verrà stampato — il ciclo è stato interrotto!")  # saltato perché è stato usato break
```

L'`else` su un ciclo è raro in pratica, ma è un modo elegante di gestire lo schema "ricerca riuscita / ricerca fallita."

## Cicli Annidati

Un **ciclo annidato** è un ciclo dentro un altro ciclo.
Il ciclo interno gira completamente per ogni singolo giro del ciclo esterno:

```python
for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()    # va alla riga successiva dopo ogni fila
```

Questo stampa una griglia di stelle di 3 righe per 4 colonne.
Il `for col in range(4)` interno completa quattro giri per ogni singolo giro di `for row in range(3)`.

I cicli annidati sono potenti per disegnare griglie, tabelle e pattern 2D — e li userai ancora di più nei capitoli successivi.

## Il Modulo time

Il **modulo `time`** incorporato di Python permette al tuo programma di interagire con l'orologio.
Prima di usarlo, lo importi come qualsiasi altro modulo:

```python
import time
```

La funzione più utile per l'animazione è **`time.sleep(seconds)`** — pausa il programma per il numero di secondi indicato (i decimali sono permessi):

```python
import time
print("Inizio...")
time.sleep(2)          # pausa di 2 secondi
print("Ho finito di aspettare!")
```

`time.sleep()` è come controlli la velocità delle animazioni: pausa di 0.05 secondi tra ogni fotogramma per ottenere circa 20 fotogrammi al secondo.

!!! mascot-warning "time.sleep() nel Browser"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    In un vero programma Python sul tuo computer, `time.sleep()` pausa il programma in modo fluido. Nei laboratori Skulpt nel browser, tempi di pausa molto lunghi potrebbero causare un momento di blocco della pagina. Mantieni i valori di `time.sleep()` piccoli (0.05–0.2 secondi) nei laboratori, e usa valori più grandi solo quando esegui Python sul tuo computer.

## Animazione con Cicli Turtle

Combina un ciclo `while` con la tartaruga e `time.sleep()` per creare una semplice animazione.
L'idea chiave: disegna un piccolo passo, pausa brevemente, disegna il passo successivo, pausa di nuovo — e ripeti.

Il programma sotto disegna una spirale che cresce.
Ogni volta che il ciclo gira, la lunghezza del passo aumenta, quindi la spirale diventa più grande a ogni giro.

!!! mascot-thinking "Il Tuo Turno — Correggi la Spirale che Cresce"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto ha un bug: la spirale non cresce mai perché `step` non cambia mai dentro il ciclo.
    Aggiungi **una riga** dentro il corpo del ciclo per aumentare `step` di `5` a ogni giro.
    **Suggerimento:** usa `step += 5`. Guarda la spirale crescere mentre la esegui!

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
t.speed(0)

step = 5
while step < 150:
    t.forward(step)
    t.right(45)
    # Aggiungi qui una riga per aumentare step di 5 a ogni giro`);
</script>

Una volta che la spirale appare, nota come la condizione `while step < 150` fermi automaticamente il ciclo quando la spirale è abbastanza grande — senza bisogno di contare manualmente!

## Esperimenti

Prova questi cambiamenti ai programmi sopra. Per ognuno, prevedi cosa succederà prima, poi eseguilo per verificare!

1. Nel laboratorio del conto alla rovescia, cambia `count = 5` in `count = 10`. **Saprai che ha funzionato quando** il conto alla rovescia stampa 10 numeri prima di "Decollo!".
2. Cambia `while count > 0` in `while count > 3`. **Saprai che ha funzionato quando** il conto alla rovescia si ferma a 4, non a 1.
3. Nel laboratorio della spirale, cambia `t.right(45)` in `t.right(90)`. **Saprai che ha funzionato quando** vedi una spirale quadrata invece di una diagonale.
4. Cambia `t.right(45)` in `t.right(91)`. **Saprai che ha funzionato quando** vedi una spirale che ruota lentamente con degli spazi tra le linee.
5. Aggiungi `t.pencolor("blue")` prima del ciclo `while`, poi dentro il ciclo aggiungi `if step > 80: t.pencolor("red")`. **Saprai che ha funzionato quando** la parte interna della spirale si disegna blu e la parte esterna si disegna rossa.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato il ciclo `while` — il motore di Python per la ripetizione a durata indefinita! Sai come fermare i cicli con `break`, saltare passi con `continue`, usare il modulo `time` e costruire animazioni che crescono passo dopo passo. Giochi, simulazioni e programmi interattivi girano tutti esattamente su questo tipo di ciclo. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
