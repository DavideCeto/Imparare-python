# Quiz: Modulo math e Progetti con la Turtle

Verifica la tua comprensione delle funzioni matematiche built-in di Python, del modulo math, e di radianti vs gradi con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa restituisce `abs(-15)`?

<div class="upper-alpha" markdown>
1. `-15`
2. `15`
3. `0`
4. Un errore, perché non puoi usare `abs()` sui numeri negativi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `abs(x)` restituisce il valore assoluto di un numero — la distanza da zero, che è sempre non negativa. `abs(-15)` restituisce `15`. Anche `abs(15)` restituisce `15`. La funzione `abs()` è incorporata in Python e non richiede alcun import.

    **Concept Tested:** abs() Function

---

#### 2. Cosa restituisce `round(3.74, 1)`?

<div class="upper-alpha" markdown>
1. `3`
2. `4.0`
3. `3.7`
4. `3.74`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `round(x, n)` arrotonda `x` a `n` cifre decimali. `round(3.74, 1)` arrotonda a 1 cifra decimale, dando `3.7` (dato che la cifra dopo la prima decimale è 4, che arrotonda in giù). Senza secondo argomento, `round(x)` arrotonda all'intero più vicino: `round(3.74)` dà `4`.

    **Concept Tested:** round() Function

---

#### 3. Cosa restituisce `math.sqrt(144)`?

<div class="upper-alpha" markdown>
1. `12` (un intero)
2. `12.0` (un float)
3. `72.0`
4. `20736.0`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `math.sqrt(x)` restituisce sempre un float, anche quando il risultato è un numero intero. La radice quadrata di 144 è 12, ma `math.sqrt(144)` restituisce `12.0`. Se hai bisogno di un intero, puoi racchiuderlo: `int(math.sqrt(144))` dà `12`.

    **Concept Tested:** math.sqrt()

---

#### 4. Qual è la differenza tra `math.floor(3.9)` e `math.ceil(3.1)`?

<div class="upper-alpha" markdown>
1. Entrambi restituiscono `3`
2. `floor` restituisce `4` e `ceil` restituisce `3`
3. `floor` restituisce `3` (arrotonda in giù) e `ceil` restituisce `4` (arrotonda in su)
4. Entrambi restituiscono `4`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `math.floor(x)` arrotonda **in giù** all'intero più vicino (3.9 → 3), e `math.ceil(x)` arrotonda **in su** all'intero più vicino (3.1 → 4). Questo è diverso da `round()`, che arrotonda all'intero più vicino (in su o in giù in base alla cifra decimale). Floor va sempre in giù, ceil va sempre in su.

    **Concept Tested:** math.floor() and math.ceil()

---

#### 5. Qual è il valore approssimativo di `math.pi`?

<div class="upper-alpha" markdown>
1. `2.71828`
2. `1.41421`
3. `3.14159`
4. `6.28318`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `math.pi` è la costante matematica π (pi), approssimativamente `3.14159265358979`. Rappresenta il rapporto tra la circonferenza di un cerchio e il suo diametro. La costante `math.e` (approssimativamente 2.71828) è il numero di Euler, e `6.28318` è 2π (due pi), chiamato anche tau.

    **Concept Tested:** math.pi

---

#### 6. In quale unità si aspettano il loro input `math.sin()` e `math.cos()` di Python?

<div class="upper-alpha" markdown>
1. Gradi (come in una lezione di geometria)
2. Radianti
3. Gradianti (1/400 di un cerchio)
4. Pixel
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `math.sin()` e `math.cos()` prendono i loro argomenti in **radianti**, non in gradi. Se vuoi il seno di 90 gradi, devi prima convertire: `math.sin(math.radians(90))`. Un cerchio completo è 360 gradi = 2π radianti. Un mezzo cerchio è 180 gradi = π radianti.

    **Concept Tested:** Radians vs Degrees

---

#### 7. Cosa restituisce `math.radians(180)`?

<div class="upper-alpha" markdown>
1. `180.0`
2. `90.0`
3. `math.pi` (approssimativamente 3.14159)
4. `2 * math.pi` (approssimativamente 6.28318)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `math.radians(degrees)` converte un angolo da gradi a radianti. 180 gradi equivalgono a π radianti (un mezzo cerchio). Quindi `math.radians(180)` restituisce approssimativamente `3.14159`. In modo simile, `math.radians(360)` restituisce `2 * math.pi` (un cerchio completo).

    **Concept Tested:** math.radians()

---

#### 8. Cosa restituisce `math.factorial(5)`?

<div class="upper-alpha" markdown>
1. `5` (solo il numero stesso)
2. `25` (5 al quadrato)
3. `10` (5 + 4 + 3 + 2 + 1)
4. `120` (5 × 4 × 3 × 2 × 1)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `math.factorial(n)` calcola n! — il prodotto di tutti gli interi positivi fino a n. `5! = 5 × 4 × 3 × 2 × 1 = 120`. I fattoriali crescono molto velocemente: `10! = 3.628.800`. I fattoriali si usano in probabilità, combinazioni, e molte formule matematiche.

    **Concept Tested:** math.factorial()

---

#### 9. Perché l'onda sinusoidale è un pattern così utile per l'arte con la turtle e l'animazione?

<div class="upper-alpha" markdown>
1. Perché `math.sin()` restituisce sempre interi facili da usare con la tartaruga
2. Perché la funzione seno produce valori morbidi e ripetuti che oscillano su e giù tra -1 e 1, perfetti per creare forme d'onda
3. Perché i valori del seno sono sempre tra 0 e 100, corrispondendo alla scala in pixel del canvas della tartaruga
4. Perché `math.sin()` è l'unica funzione che funziona dentro un ciclo `for`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `math.sin()` restituisce valori che oscillano in modo fluido tra -1.0 e 1.0 all'aumentare dell'angolo di input. Moltiplicando l'output per un'ampiezza (come 100 pixel) e scorrendo gli angoli con un ciclo, puoi far tracciare alla tartaruga un pattern d'onda morbido. Questo stesso principio è usato nei giochi, nella musica, e nelle simulazioni di fisica.

    **Concept Tested:** math.sin() and Turtle Projects

---

#### 10. Qual è il risultato di `math.degrees(math.pi)`?

<div class="upper-alpha" markdown>
1. `90.0`
2. `360.0`
3. `3.14159`
4. `180.0`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `math.degrees(radians)` converte dai radianti ai gradi. π radianti equivale a 180 gradi (un mezzo cerchio). Quindi `math.degrees(math.pi)` restituisce `180.0`. Questo è l'opposto di `math.radians(180)`. Usa `math.degrees()` quando hai un valore in radianti (magari da un calcolo) e hai bisogno di mostrarlo in gradi.

    **Concept Tested:** math.degrees()

---
