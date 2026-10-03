# Quiz: Matematica e Aritmetica

Verifica la tua comprensione degli operatori aritmetici di Python, dell'ordine delle operazioni e dell'assegnazione aumentata con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è il risultato di `10 // 3` in Python?

<div class="upper-alpha" markdown>
1. `3.3333`
2. `1`
3. `3`
4. `0.3`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'operatore `//` è la divisione intera — divide e mantiene solo la parte di numero intero, scartando ogni decimale. 10 diviso 3 fa 3 con un resto di 1, quindi `10 // 3` dà `3`. Se vuoi il risultato decimale, usa invece `/`: `10 / 3` dà `3.3333...`.

    **Concept Tested:** Integer Division Operator

---

#### 2. Cosa calcola l'operatore modulo `%`?

<div class="upper-alpha" markdown>
1. La percentuale di un numero rispetto a un altro
2. Il resto che rimane dopo aver diviso due interi
3. La media di due numeri
4. Il maggiore tra due numeri
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'operatore `%` (modulo) ti dà il resto dopo la divisione. Per esempio, `10 % 3` è `1` perché il 3 entra in 10 tre volte (cioè 9), e 10 − 9 = 1 di resto. Il modulo è molto utile per verificare se un numero è pari (`n % 2 == 0`) e per creare pattern ripetuti nei programmi.

    **Concept Tested:** Modulo Operator

---

#### 3. A cosa equivale `2 ** 8` in Python?

<div class="upper-alpha" markdown>
1. `16`
2. `256`
3. `28`
4. `10`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'operatore `**` è l'elevamento a potenza — "elevato alla potenza di." `2 ** 8` significa 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2, che equivale a 256. È lo stesso di 2 elevato all'ottava potenza in matematica. L'elevamento a potenza è uno dei tre operatori aritmetici extra di Python non presenti in Scratch.

    **Concept Tested:** Exponentiation Operator

---

#### 4. Qual è il risultato di `2 + 3 * 4` in Python?

<div class="upper-alpha" markdown>
1. `20`
2. `24`
3. `14`
4. `9`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python segue l'ordine standard delle operazioni (PEMDAS): la moltiplicazione viene prima dell'addizione. Quindi Python calcola prima `3 * 4 = 12`, poi somma `2 + 12 = 14`. Se volessi sommare prima e poi moltiplicare, scriveresti `(2 + 3) * 4`, che equivale a `20`.

    **Concept Tested:** Order of Operations

---

#### 5. Quale operatore abbreviato aggiunge 5 alla variabile `score`?

<div class="upper-alpha" markdown>
1. `score =+ 5`
2. `score += 5`
3. `score + 5`
4. `score == score + 5`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `score += 5` è un operatore di assegnazione aumentata — è l'abbreviazione di `score = score + 5`. Legge il valore attuale di `score`, aggiunge 5, e memorizza il risultato di nuovo in `score`. Questo schema si usa costantemente nei cicli: `count += 1` aggiunge 1 a un contatore ogni volta che il ciclo si ripete.

    **Concept Tested:** Augmented Assignment Operators

---

#### 6. Qual è il valore di `x` dopo l'esecuzione di questo codice?

```python
x = 10
x -= 3
x *= 2
print(x)
```

<div class="upper-alpha" markdown>
1. `7`
2. `14`
3. `20`
4. `4`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Python esegue ogni riga in ordine. Prima `x = 10` imposta x a 10. Poi `x -= 3` significa `x = x - 3` = `10 - 3` = 7, quindi x ora è 7. Poi `x *= 2` significa `x = x * 2` = `7 * 2` = 14. Il valore finale stampato è 14.

    **Concept Tested:** Augmented Assignment Operators

---

#### 7. Cosa fa `a, b = 5, 10` in Python?

<div class="upper-alpha" markdown>
1. Crea una lista con due elementi: 5 e 10
2. Assegna 5 ad `a` e 10 a `b` contemporaneamente
3. Scambia i valori di `a` e `b`
4. Moltiplica `a` per `b` e memorizza il risultato
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'assegnazione multipla ti permette di assegnare valori a due o più variabili in una riga. Python legge i valori a destra (`5` e `10`) e li assegna da sinistra a destra alle variabili a sinistra (`a` e `b`). Dopo questa riga, `a` contiene `5` e `b` contiene `10`.

    **Concept Tested:** Multiple Assignment

---

#### 8. Perché `10 / 2` restituisce `5.0` invece di `5` in Python?

<div class="upper-alpha" markdown>
1. Python arrotonda automaticamente per eccesso tutti i risultati delle divisioni
2. L'operatore `/` restituisce sempre un float, anche quando la risposta è un numero intero
3. `5.0` e `5` sono esattamente la stessa cosa in Python
4. Devi usare le parentesi per ottenere un intero dalla divisione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In Python 3, l'operatore di divisione `/` restituisce sempre un float (un numero con una virgola decimale), anche quando i numeri si dividono esattamente. Quindi `10 / 2` dà `5.0`, non `5`. Se vuoi il risultato intero, usa l'operatore `//`: `10 // 2` dà `5`.

    **Concept Tested:** Division Returns Float

---

#### 9. Cos'è `3e8` in Python?

<div class="upper-alpha" markdown>
1. Il numero 38
2. 3 elevato alla potenza di 8 (= 6561)
3. 3 moltiplicato per 10 elevato alla potenza di 8 (= 300.000.000)
4. Un errore, perché `e` non è un carattere numerico valido
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python usa la lettera `e` (o `E`) per la notazione scientifica. `3e8` significa 3 × 10^8, che equivale a 300.000.000 (la velocità approssimativa della luce in metri al secondo). La notazione scientifica è utile quando si lavora con numeri molto grandi o molto piccoli per evitare di scrivere molti zeri.

    **Concept Tested:** Scientific Notation Floats

---

#### 10. Per disegnare un esagono regolare con una turtle, quale angolo di svolta dovresti usare a ogni angolo?

<div class="upper-alpha" markdown>
1. 45 gradi
2. 72 gradi
3. 60 gradi
4. 120 gradi
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Per qualsiasi poligono regolare, l'angolo di svolta a ogni angolo è `360 / numero_di_lati`. Un esagono ha 6 lati, quindi l'angolo di svolta è `360 / 6 = 60` gradi. Dovresti ripetere `t.forward(lunghezza)` e `t.right(60)` sei volte. Per un pentagono (5 lati), la svolta è `360 / 5 = 72` gradi.

    **Concept Tested:** Arithmetic Operators

---
