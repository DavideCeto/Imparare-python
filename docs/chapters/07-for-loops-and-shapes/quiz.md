# Quiz: Cicli For e Disegno di Forme

Verifica la tua comprensione dei cicli for, di range(), del posizionamento della turtle e del disegno di pattern con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa produce `range(4)` quando usato in un ciclo for?

<div class="upper-alpha" markdown>
1. I numeri 1, 2, 3, 4
2. I numeri 0, 1, 2, 3
3. Il numero 4 ripetuto quattro volte
4. I numeri 0, 1, 2, 3, 4
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `range(4)` genera la sequenza 0, 1, 2, 3 — quattro numeri a partire da zero e fermandosi prima di 4. In Python, `range(n)` inizia sempre da 0 e arriva fino a, ma non include, `n`. Quindi `range(4)` ti dà quattro valori: 0, 1, 2 e 3.

    **Concept Tested:** for Loop with range()

---

#### 2. Quale forma disegna questo codice?

```python
import turtle
t = turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
```

<div class="upper-alpha" markdown>
1. Un triangolo
2. Un cerchio
3. Un quadrato
4. Una linea retta
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il ciclo gira 4 volte. Ogni volta, la turtle si muove avanti di 100 pixel e gira a destra di 90 gradi. Dopo quattro svolte a destra di 90 gradi, la turtle ha ruotato di un giro completo di 360 gradi e torna alla sua direzione di partenza — creando una forma a quadrato chiusa con lati di 100 pixel.

    **Concept Tested:** for Loop with range()

---

#### 3. Qual è la variabile contatore del ciclo in `for i in range(5)`?

<div class="upper-alpha" markdown>
1. `range`
2. `5`
3. `for`
4. `i`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. La variabile `i` è il contatore del ciclo — assume ogni valore prodotto da `range(5)` (cioè, 0, 1, 2, 3, 4) nei giri successivi del ciclo. Puoi usare `i` dentro il corpo del ciclo per rendere ogni passo leggermente diverso, come disegnare linee che si allungano a ogni iterazione.

    **Concept Tested:** Loop Counter Variable

---

#### 4. Cosa produce `range(2, 8, 2)`?

<div class="upper-alpha" markdown>
1. `2, 3, 4, 5, 6, 7, 8`
2. `2, 4, 6, 8`
3. `2, 4, 6`
4. `0, 2, 4, 6, 8`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `range(start, stop, step)` inizia da 2, si ferma prima di 8, e conta a passi di 2. Questo dà 2, 4, 6 — tre valori. Nota che 8 stesso NON è incluso perché `range` si ferma prima del valore di stop. Se cambiassi lo stop a 9, otterresti 2, 4, 6, 8.

    **Concept Tested:** Range with Start Stop Step

---

#### 5. Cos'è un accumulatore in Python?

<div class="upper-alpha" markdown>
1. Una variabile creata dentro un ciclo che scompare quando il ciclo finisce
2. Una variabile impostata prima di un ciclo e aggiornata dentro il ciclo a ogni passo
3. La funzione `range()` che controlla quante volte gira un ciclo
4. Un tipo speciale di ciclo `for` che conta all'indietro
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un accumulatore è una variabile che inizializzi prima del ciclo (di solito a 0 o a un valore vuoto) e poi aggiorni dentro il ciclo a ogni iterazione. Un esempio classico: `total = 0` prima del ciclo, poi `total += i` dentro. Dopo il ciclo, `total` contiene la somma di tutti i valori elaborati dal ciclo.

    **Concept Tested:** Loop Accumulator Pattern

---

#### 6. Cosa fa `t.goto(0, 0)`?

<div class="upper-alpha" markdown>
1. Imposta la velocità della turtle a zero (la ferma)
2. Sposta la turtle al centro della tela alle coordinate (0, 0)
3. Crea una nuova turtle nell'origine
4. Disegna un cerchio nella posizione (0, 0)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.goto(x, y)` sposta la turtle in una posizione esatta sulla tela usando le coordinate. Il centro della tela della turtle è in `(0, 0)`. La x positiva è a destra, la y positiva è in alto. La turtle disegnerà una linea mentre si muove a meno che tu non chiami prima `t.penup()`.

    **Concept Tested:** Absolute Positioning goto()

---

#### 7. Cosa farà `t.setheading(90)` alla turtle?

<div class="upper-alpha" markdown>
1. Fa ruotare la turtle di 90 gradi in senso orario dalla sua direzione attuale
2. Orienta la turtle direttamente verso Nord (in alto), indipendentemente dalla sua direzione attuale
3. Muove la turtle di 90 pixel nella direzione attuale
4. Imposta la velocità della turtle a 90 pixel al secondo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.setheading(angle)` imposta la direzione della turtle a un orientamento esatto della bussola, non una svolta relativa. Orientamento 90 significa Nord (su), 0 significa Est (destra), 180 significa Ovest (sinistra), e 270 significa Sud (giù). Questo è diverso da `t.right()` e `t.left()`, che girano relativamente alla direzione attuale verso cui è rivolta la turtle.

    **Concept Tested:** setheading() Direction

---

#### 8. Quante volte viene eseguito il corpo di `for i in range(6)`?

<div class="upper-alpha" markdown>
1. 5 volte
2. 7 volte
3. 0 volte
4. 6 volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `range(6)` genera 6 valori: 0, 1, 2, 3, 4, 5. Il corpo del ciclo viene eseguito una volta per ogni valore, quindi gira esattamente 6 volte. Un errore comune tra i principianti è pensare che giri 7 volte (includendo 6) o 5 volte (fermandosi a 5). Ricorda sempre: `range(n)` produce esattamente `n` valori.

    **Concept Tested:** for Loop with range()

---

#### 9. Quale comando disegna un cerchio con un raggio di 50 pixel?

<div class="upper-alpha" markdown>
1. `t.square(50)`
2. `t.oval(50)`
3. `t.circle(50)`
4. `t.round(50)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.circle(radius)` dice alla turtle di disegnare un cerchio con il raggio indicato. La turtle inizia a disegnare dalla sua posizione attuale. Puoi usare valori positivi o negativi per il raggio — un raggio negativo disegna il cerchio sul lato opposto della turtle.

    **Concept Tested:** Drawing circle() and Polygons

---

#### 10. Per disegnare un pentagono regolare, quante volte dovrebbe girare il ciclo e qual è l'angolo di svolta?

<div class="upper-alpha" markdown>
1. Ciclo 5 volte, svolta di 60 gradi ogni volta
2. Ciclo 5 volte, svolta di 72 gradi ogni volta
3. Ciclo 6 volte, svolta di 60 gradi ogni volta
4. Ciclo 4 volte, svolta di 90 gradi ogni volta
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un pentagono ha 5 lati, quindi il ciclo gira 5 volte. L'angolo di svolta a ogni angolo è `360 / 5 = 72` gradi. Puoi usare questa formula per qualsiasi poligono regolare: `angolo_svolta = 360 / numero_di_lati`. Il ciclo si ripete quel numero di volte, muovendosi in avanti e girando di quell'angolo ogni volta.

    **Concept Tested:** Drawing circle() and Polygons

---
