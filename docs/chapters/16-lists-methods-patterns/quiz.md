# Quiz: Liste — Metodi e Pattern

Verifica la tua comprensione dei metodi delle liste, dell'ordinamento, delle list comprehension, e dei pattern pila/coda con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa fa `fruits.append("mango")`?

<div class="upper-alpha" markdown>
1. Inserisce `"mango"` all'inizio della lista
2. Aggiunge `"mango"` alla fine della lista
3. Sostituisce il primo elemento con `"mango"`
4. Crea una nuova lista con `"mango"` come unico elemento
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `append(x)` aggiunge un singolo elemento alla **fine** di una lista esistente, modificandola sul posto. Se `fruits = ["apple", "banana"]`, dopo `fruits.append("mango")` la lista diventa `["apple", "banana", "mango"]`. Usa invece `insert(i, x)` se vuoi aggiungere l'elemento in una posizione specifica.

    **Concept Tested:** append() Method

---

#### 2. Cosa fa `items.insert(1, "kiwi")` a `items = ["apple", "banana"]`?

<div class="upper-alpha" markdown>
1. Sostituisce `"banana"` con `"kiwi"`
2. Aggiunge `"kiwi"` alla fine della lista
3. Inserisce `"kiwi"` prima dell'elemento all'indice 1, rendendo la lista `["apple", "kiwi", "banana"]`
4. Genera un errore perché `"banana"` è già all'indice 1
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `insert(i, x)` inserisce l'elemento `x` **prima** dell'elemento attualmente all'indice `i`. Con `items = ["apple", "banana"]`, chiamare `items.insert(1, "kiwi")` posiziona `"kiwi"` all'indice 1 e spinge `"banana"` all'indice 2: `["apple", "kiwi", "banana"]`. La lista cresce di un elemento.

    **Concept Tested:** insert() Method

---

#### 3. Cosa fa `items.pop()`?

<div class="upper-alpha" markdown>
1. Rimuove il primo elemento dalla lista e lo restituisce
2. Rimuove e restituisce l'ultimo elemento dalla lista
3. Rimuove tutti gli elementi dalla lista
4. Restituisce l'ultimo elemento senza rimuoverlo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `pop()` senza argomento rimuove e restituisce l'**ultimo** elemento nella lista. Puoi anche usare `pop(i)` per rimuovere e restituire l'elemento a un indice specifico. Questo rende `pop()` molto utile per implementare le pile (ultimo entrato, primo uscito), dove lavori sempre con l'elemento in cima (l'ultimo).

    **Concept Tested:** pop() Method

---

#### 4. Cosa fa `scores.sort()` a `scores = [73, 100, 87, 55]`?

<div class="upper-alpha" markdown>
1. Restituisce una nuova lista ordinata senza cambiare l'originale
2. Ordina la lista in ordine decrescente (il più grande prima)
3. Ordina la lista in ordine crescente (il più piccolo prima) e la modifica sul posto
4. Crea una copia ordinata e la memorizza in una nuova variabile chiamata `sorted_scores`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `sort()` riorganizza gli elementi della lista **sul posto** in ordine crescente (dal più piccolo per i numeri, alfabetico per le stringhe). Dopo `scores.sort()`, `scores` stesso diventa `[55, 73, 87, 100]`. NON restituisce una nuova lista — se scrivi `result = scores.sort()`, `result` sarà `None`.

    **Concept Tested:** sort() Method

---

#### 5. Qual è il risultato di `[s * 2 for s in [1, 2, 3]]`?

<div class="upper-alpha" markdown>
1. `[1, 2, 3, 1, 2, 3]`
2. `12`
3. `[2, 4, 6]`
4. `[[2], [4], [6]]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Questa è una list comprehension — costruisce una nuova lista applicando un'espressione (`s * 2`) a ogni elemento della lista sorgente `[1, 2, 3]`. Il risultato è `[2, 4, 6]`. Le list comprehension sono un modo conciso e leggibile per trasformare le liste senza scrivere un ciclo completo.

    **Concept Tested:** List Comprehensions

---

#### 6. Cosa produce la seguente list comprehension?

```python
[s for s in [60, 80, 45, 90] if s >= 70]
```

<div class="upper-alpha" markdown>
1. `[60, 80, 45, 90]` — la lista originale invariata
2. `[80, 90]` — solo i punteggi 70 e superiori
3. `[60, 45]` — solo i punteggi sotto 70
4. `[True, True, False, True]` — una lista di booleani
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La clausola `if` in una list comprehension agisce come un filtro — solo gli elementi per cui la condizione è `True` vengono inclusi nel risultato. `s >= 70` è `True` per `80` e `90`, quindi solo questi due valori appaiono nella lista di output. Questo è un pattern molto comune per filtrare i dati.

    **Concept Tested:** List Comprehensions

---

#### 7. Cosa fa `colors.remove("red")` se `colors = ["red", "blue", "red"]`?

<div class="upper-alpha" markdown>
1. Rimuove tutte le occorrenze di `"red"` dalla lista
2. Rimuove l'elemento all'indice chiamato `"red"`
3. Rimuove solo la prima occorrenza di `"red"` dalla lista
4. Genera un `ValueError` perché `"red"` appare più di una volta
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `remove(x)` cerca e rimuove la **prima** occorrenza del valore `x`. Dopo `colors.remove("red")`, la lista diventa `["blue", "red"]` — il secondo `"red"` resta. Se `x` non è affatto nella lista, `remove()` genera un `ValueError`.

    **Concept Tested:** remove() Method

---

#### 8. In una struttura di dati a pila, quale elemento viene rimosso per primo?

<div class="upper-alpha" markdown>
1. L'elemento all'indice 0 (aggiunto per primo)
2. L'elemento nel mezzo della pila
3. Un elemento scelto a caso
4. L'elemento aggiunto più di recente (ultimo entrato, primo uscito)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Una pila segue il principio LIFO (Last In, First Out) — l'elemento aggiunto più di recente è il primo a essere rimosso. Implementi una pila in Python con una lista: `append()` per impilare gli elementi in cima e `pop()` per rimuovere gli elementi dalla cima. Pensa a una pila di piatti — prendi sempre quello in cima per primo.

    **Concept Tested:** Stack Pattern

---

#### 9. Come trovi quante volte appare il valore `5` in `numbers = [5, 3, 5, 8, 5]`?

<div class="upper-alpha" markdown>
1. `numbers.find(5)`
2. `numbers.index(5)`
3. `numbers.count(5)`
4. `len(numbers, 5)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `count(x)` restituisce il numero di volte che il valore `x` appare nella lista. `numbers.count(5)` restituirebbe `3` perché ci sono tre `5` nella lista. `index(x)` restituisce la posizione della prima occorrenza (non il conteggio). `find()` è un metodo delle stringhe, non delle liste.

    **Concept Tested:** count() and index() Methods

---

#### 10. Cosa fa `my_list.extend(["x", "y"])` che `my_list.append(["x", "y"])` NON fa?

<div class="upper-alpha" markdown>
1. `extend()` aggiunge ogni elemento individualmente; `append()` aggiungerebbe l'intera lista come un singolo elemento annidato
2. `extend()` crea una nuova lista; `append()` modifica l'originale
3. `extend()` funziona solo con le stringhe; `append()` funziona con qualsiasi tipo
4. Fanno la stessa cosa — `extend()` e `append()` sono intercambiabili
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. `extend(other_list)` scompone `other_list` e aggiunge ogni elemento individualmente alla fine. `append(other_list)` aggiunge l'intera lista come un singolo elemento (creando una lista annidata). Se `my_list = [1, 2]`, allora `extend([3, 4])` dà `[1, 2, 3, 4]`, mentre `append([3, 4])` dà `[1, 2, [3, 4]]`.

    **Concept Tested:** extend() Method

---
