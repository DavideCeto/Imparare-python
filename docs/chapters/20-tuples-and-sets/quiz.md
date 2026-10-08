# Quiz: Tuple e Insiemi

Verifica la tua comprensione dei tipi tuple e set di Python, della scomposizione delle tuple, e delle operazioni sugli insiemi con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è la differenza fondamentale tra una tupla e una lista?

<div class="upper-alpha" markdown>
1. Le tuple usano le parentesi; le liste usano le parentesi quadre, ma per il resto sono identiche
2. Le tuple sono immutabili (non possono essere cambiate dopo la creazione); le liste sono mutabili (possono essere cambiate)
3. Le tuple possono contenere solo numeri; le liste possono contenere qualsiasi tipo
4. Le tuple sono più veloci da creare; le liste sono più veloci da accedere
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La differenza più importante è la mutabilità. Alle liste si possono aggiungere, rimuovere, o cambiare elementi. Le tuple no — una volta create, il loro contenuto è fisso. Entrambe supportano l'indicizzazione, lo slicing, e l'iterazione. Usa una tupla quando i dati rappresentano qualcosa di fisso (come una coordinata) e una lista quando la collezione deve cambiare.

    **Concept Tested:** Tuple Type

---

#### 2. Come crei una tupla a un solo elemento contenente il numero 42?

<div class="upper-alpha" markdown>
1. `(42)`
2. `[42]`
3. `{42}`
4. `(42,)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. È richiesta una virgola finale per dire a Python che intendi una tupla. `(42)` è solo l'intero 42 tra parentesi — non una tupla. `(42,)` ha la virgola finale che segnala "questa è una tupla a un elemento." Per le tuple con due o più elementi, non è necessaria nessuna virgola finale: `(1, 2)` è già chiaramente una tupla.

    **Concept Tested:** Single-Element Tuple Syntax

---

#### 3. Cosa fa la scomposizione delle tuple (tuple unpacking)?

<div class="upper-alpha" markdown>
1. Rimuove tutti gli elementi da una tupla uno alla volta
2. Converte una tupla in una lista così i suoi elementi possono essere cambiati
3. Assegna ogni elemento di una tupla a una variabile separata in un solo passo
4. Stampa tutti gli elementi di una tupla su righe separate
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La scomposizione delle tuple (chiamata anche destructuring) ti permette di scrivere `x, y = (10, 20)` per assegnare `10` a `x` e `20` a `y` in una singola riga. Il numero di variabili a sinistra deve corrispondere al numero di elementi nella tupla. Questo è lo stesso meccanismo che fa funzionare lo scambio di variabili in una riga di Python (`a, b = b, a`).

    **Concept Tested:** Tuple Unpacking

---

#### 4. Qual è un caso d'uso comune per restituire una tupla da una funzione?

<div class="upper-alpha" markdown>
1. Per far girare la funzione più velocemente
2. Per restituire valori multipli da una funzione in una volta
3. Per impedire a chi chiama di cambiare il valore restituito
4. Per assicurarsi che la funzione possa essere chiamata solo una volta
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una funzione può avere solo un'istruzione `return`, ma puoi impacchettare valori multipli in una tupla e restituirli tutti in una volta. Per esempio, `return min_val, max_val` restituisce una tupla. Chi chiama può poi scomporla: `lo, hi = find_range(data)`. Questo è più pulito che restituire una lista o usare variabili globali.

    **Concept Tested:** Tuples as Return Values

---

#### 5. Cosa succede quando aggiungi un elemento duplicato a un insieme?

<div class="upper-alpha" markdown>
1. L'insieme genera un `ValueError`
2. L'elemento viene aggiunto una seconda volta, creando un duplicato
3. Il duplicato viene ignorato silenziosamente — l'insieme resta invariato
4. L'elemento originale viene sostituito dalla nuova copia
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Gli insiemi impongono automaticamente l'unicità — nessun duplicato è permesso. Se fai `add()` di un elemento già nell'insieme, o crei un insieme con valori ripetuti come `{1, 2, 2, 3}`, Python ignora silenziosamente i duplicati. L'insieme `{1, 2, 2, 3}` diventa `{1, 2, 3}`.

    **Concept Tested:** Set Type

---

#### 6. Dati `A = {1, 2, 3, 4}` e `B = {3, 4, 5, 6}`, cos'è `A & B`?

<div class="upper-alpha" markdown>
1. `{1, 2, 3, 4, 5, 6}` (tutti gli elementi di entrambi)
2. `{1, 2}` (elementi solo in A)
3. `{3, 4}` (elementi in sia A sia B)
4. `{5, 6}` (elementi solo in B)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'operatore `&` esegue l'intersezione tra insiemi — restituisce un nuovo insieme contenente solo gli elementi che appaiono in **entrambi** gli insiemi. Sia `3` sia `4` sono in A e in B, quindi `A & B = {3, 4}`. L'operatore `|` è l'unione (tutti gli elementi), e `-` è la differenza (nel primo ma non nel secondo).

    **Concept Tested:** Set Intersection

---

#### 7. Cosa produce `A | B` per `A = {1, 2, 3}` e `B = {3, 4, 5}`?

<div class="upper-alpha" markdown>
1. `{3}` (solo l'elemento condiviso)
2. `{1, 2, 4, 5}` (elementi non in entrambi)
3. `{1, 2}` (elementi solo in A)
4. `{1, 2, 3, 4, 5}` (tutti gli elementi unici di entrambi)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. L'operatore `|` esegue l'unione tra insiemi — restituisce un nuovo insieme contenente tutti gli elementi di entrambi gli insiemi, senza duplicati. `{1, 2, 3} | {3, 4, 5}` dà `{1, 2, 3, 4, 5}`. L'elemento condiviso `3` appare solo una volta nel risultato perché gli insiemi non permettono duplicati.

    **Concept Tested:** Set Union

---

#### 8. Qual è la differenza tra `s.remove(x)` e `s.discard(x)` su un insieme?

<div class="upper-alpha" markdown>
1. `remove()` rimuove per indice; `discard()` rimuove per valore
2. `remove()` genera un `KeyError` se `x` non viene trovato; `discard()` non fa nulla silenziosamente se `x` non viene trovato
3. `remove()` funziona sulle liste; `discard()` funziona solo sugli insiemi
4. Sono identici — solo due nomi per la stessa operazione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Entrambi i metodi rimuovono un elemento da un insieme per valore, ma differiscono nella gestione degli errori. `remove(x)` genera un `KeyError` se `x` non è nell'insieme. `discard(x)` non fa nulla e non genera errori se `x` è assente. Usa `discard()` quando non sei sicuro se l'elemento esiste e non vuoi controllare prima.

    **Concept Tested:** Set Methods

---

#### 9. Qual è il modo più rapido di rimuovere i duplicati da una lista in Python?

<div class="upper-alpha" markdown>
1. Ordinare la lista e rimuovere i duplicati adiacenti con un ciclo
2. Convertire la lista in un insieme con `set()`, che rimuove automaticamente i duplicati
3. Usare `list.remove_duplicates()` (un metodo built-in)
4. Iterare sulla lista e controllare ogni elemento con `in` prima di aggiungerlo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `set(my_list)` converte una lista in un insieme, scartando automaticamente tutti i valori duplicati. Se hai bisogno del risultato di nuovo come lista, racchiudilo: `list(set(my_list))`. L'unico avvertimento è che gli insiemi non sono ordinati, quindi l'ordine originale non viene preservato. Non esiste un metodo built-in `remove_duplicates()` in Python.

    **Concept Tested:** Set Type

---

#### 10. Cosa produce `A - B` per `A = {1, 2, 3, 4}` e `B = {3, 4, 5}`?

<div class="upper-alpha" markdown>
1. `{5}` (elementi solo in B)
2. `{-2, -2, -2, -1}` (sottraendo ogni elemento)
3. `{1, 2}` (elementi in A che non sono in B)
4. `{1, 2, 5}` (tutti gli elementi unici non condivisi)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'operatore `-` esegue la differenza tra insiemi — restituisce gli elementi che sono nel primo insieme ma NON nel secondo. `{1, 2, 3, 4} - {3, 4, 5}` dà `{1, 2}` perché `3` e `4` vengono rimossi (sono in B) e `5` non viene incluso (era solo in B). Nota che `A - B` e `B - A` danno risultati diversi.

    **Concept Tested:** Set Difference

---
