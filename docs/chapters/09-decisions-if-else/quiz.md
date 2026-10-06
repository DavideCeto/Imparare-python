# Quiz: Prendere Decisioni con If/Else

Verifica la tua comprensione dei valori booleani, degli operatori di confronto, e delle diramazioni if/elif/else con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quali sono gli unici due valori possibili per un booleano in Python?

<div class="upper-alpha" markdown>
1. `yes` e `no`
2. `1` e `0`
3. `True` e `False`
4. `on` e `off`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. In Python, i valori booleani si scrivono esattamente come `True` e `False` — con la prima lettera maiuscola. Appartengono al tipo `bool`. I booleani sono il risultato dei confronti e vengono usati nelle istruzioni `if` per decidere quale ramo di codice eseguire.

    **Concept Tested:** Boolean Type

---

#### 2. Qual è la differenza tra `=` e `==` in Python?

<div class="upper-alpha" markdown>
1. `=` confronta due valori; `==` assegna un valore a una variabile
2. `=` assegna un valore a una variabile; `==` confronta due valori per verificarne l'uguaglianza
3. Entrambi fanno la stessa cosa — sono intercambiabili
4. `=` funziona con i numeri; `==` funziona con le stringhe
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `=` è l'operatore di assegnazione: `x = 5` memorizza il valore 5 nella variabile `x`. `==` è l'operatore di confronto per l'uguaglianza: `x == 5` verifica se `x` contiene attualmente il valore 5 e restituisce `True` o `False`. Usare `=` dentro una condizione `if` causa un `SyntaxError` — questo è uno degli errori più comuni tra i principianti.

    **Concept Tested:** Comparison Operators

---

#### 3. Cosa stamperà questo codice quando `score = 75`?

```python
if score >= 60:
    print("Passing!")
else:
    print("Try again!")
```

<div class="upper-alpha" markdown>
1. `Try again!`
2. Sia `Passing!` sia `Try again!`
3. `Passing!`
4. Niente — il programma salta entrambi i rami
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Quando `score = 75`, la condizione `score >= 60` si valuta come `True` (75 è maggiore o uguale a 60). Quindi Python esegue il blocco `if` e stampa `"Passing!"`. Dato che il blocco `if` è stato eseguito, Python salta completamente il blocco `else`. Un `if/else` esegue sempre esattamente uno dei due rami.

    **Concept Tested:** if...else Block

---

#### 4. Cosa fa la parola chiave `elif` in una catena di condizioni?

<div class="upper-alpha" markdown>
1. Viene eseguita insieme al blocco `if` ogni volta che il programma viene eseguito
2. Crea una nuova variabile per memorizzare il risultato di una condizione
3. Controlla una condizione aggiuntiva solo se tutte le condizioni precedenti erano False
4. Riavvia l'intera catena if/elif/else dall'inizio
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `elif` (abbreviazione di "else if") aggiunge un altro ramo a una catena decisionale. Python controlla le condizioni dall'alto verso il basso ed esegue il corpo del **primo** ramo la cui condizione è `True`, poi salta tutti i rami rimanenti. Se nessun `if` o `elif` è `True`, viene eseguito il ramo `else` (se esiste).

    **Concept Tested:** elif Chains

---

#### 5. Cosa richiede l'operatore logico `and` perché una condizione combinata sia `True`?

<div class="upper-alpha" markdown>
1. Almeno una delle condizioni deve essere `True`
2. Nessuna delle due condizioni può essere `True`
3. Entrambe le condizioni devono essere `True`
4. Le condizioni devono essere esattamente uguali tra loro
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'operatore `and` restituisce `True` solo quando **entrambe** le condizioni alla sua sinistra e destra sono `True`. Se anche solo una è `False`, l'intera espressione è `False`. Questo è diverso da `or`, che restituisce `True` quando **almeno una** condizione è `True`.

    **Concept Tested:** Logical Operators

---

#### 6. Qual è il risultato di `not True`?

<div class="upper-alpha" markdown>
1. `True`
2. `0`
3. `None`
4. `False`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. L'operatore `not` inverte un valore booleano: `not True` diventa `False`, e `not False` diventa `True`. È utile per rendere le condizioni più leggibili — per esempio, `if not is_finished:` si legge naturalmente come "se non abbiamo ancora finito."

    **Concept Tested:** Logical Operators

---

#### 7. Quale voto stamperà Python per `score = 83` in questo codice?

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

<div class="upper-alpha" markdown>
1. `A`
2. `C`
3. `B`
4. Sia `B` sia `C`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python controlla le condizioni dall'alto verso il basso e si ferma alla prima che è `True`. `83 >= 90` è `False`, quindi passa a `83 >= 80`, che è `True`. Python stampa `"B"` e salta tutti i rami rimanenti, incluso `elif score >= 70`. Anche se `83 >= 70` è anch'essa `True`, non viene mai controllata perché un ramo è già stato eseguito.

    **Concept Tested:** elif Chains

---

#### 8. Cosa verifica questo confronto concatenato?

```python
if 0 <= age < 18:
```

<div class="upper-alpha" markdown>
1. Se `age` è uguale a 0 o uguale a 18
2. Se `age` è compresa tra 0 e 18, includendo 0 ma non 18
3. Se `age` è negativa o maggiore di 18
4. Se `age` è esattamente 0 o esattamente 18
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il confronto concatenato `0 <= age < 18` verifica se `age` è almeno 0 E minore di 18. Questo equivale a `age >= 0 and age < 18`. Python permette questa notazione simile alla matematica per i controlli di intervallo. L'età 0 passerebbe il test (0 <= 0 è True) ma l'età 18 no (18 < 18 è False).

    **Concept Tested:** Chained Comparisons

---

#### 9. Cos'è un'istruzione `if` annidata?

<div class="upper-alpha" markdown>
1. Un'istruzione `if` scritta su una sola riga senza i due punti
2. Un'istruzione `if` posizionata dentro il corpo di un'altra istruzione `if`
3. Un'istruzione `if` che controlla più di tre condizioni contemporaneamente
4. Un'istruzione `if` che viene eseguita all'indietro dal basso verso l'alto
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un `if` annidato è un'istruzione `if` scritta dentro il corpo (blocco indentato) di un'altra istruzione `if`. Questo ti permette di controllare una seconda condizione solo quando la prima condizione è già `True`. L'annidamento ti dà un controllo fine, ma troppi livelli di annidamento possono rendere il codice difficile da leggere.

    **Concept Tested:** Nested if Statements

---

#### 10. Quale condizione verifica correttamente se una variabile `n` è sia maggiore di 0 SIA pari?

<div class="upper-alpha" markdown>
1. `if n > 0 or n % 2 == 0:`
2. `if n > 0 and n % 2 == 0:`
3. `if n > 0 and n % 2 != 0:`
4. `if n > 0 not n % 2 == 0:`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Per richiedere entrambe le condizioni, usa `and`. `n > 0` verifica che il numero sia positivo, e `n % 2 == 0` verifica che il resto dopo la divisione per 2 sia zero (cioè che sia pari). Usare `or` renderebbe la condizione `True` se ne fosse soddisfatta anche solo una, il che non è quello che vogliamo.

    **Concept Tested:** Logical Operators

---
