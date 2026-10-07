# Quiz: Liste — Nozioni di Base

Verifica la tua comprensione delle liste Python, dell'indicizzazione, dello slicing, e della mutabilità con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Come crei in Python una lista che contiene tre colori?

<div class="upper-alpha" markdown>
1. `colors = {"red", "green", "blue"}`
2. `colors = ("red", "green", "blue")`
3. `colors = ["red", "green", "blue"]`
4. `colors = "red, green, blue"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Le liste in Python si creano usando le parentesi quadre `[]` con gli elementi separati da virgole. L'opzione A crea un set (parentesi graffe), l'opzione B crea una tupla (parentesi), e l'opzione D è solo una singola stringa — non una collezione di elementi separati.

    **Concept Tested:** List Type

---

#### 2. Data `scores = [95, 87, 100, 73]`, cosa restituisce `scores[2]`?

<div class="upper-alpha" markdown>
1. `87`
2. `73`
3. `95`
4. `100`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Python usa l'indicizzazione a base zero: l'indice 0 è `95`, l'indice 1 è `87`, l'indice 2 è `100`, e l'indice 3 è `73`. Un errore molto comune è assumere che l'indice 2 sia il secondo elemento, ma in realtà è il terzo elemento (contando da zero).

    **Concept Tested:** List Indexing

---

#### 3. Data `colors = ["red", "green", "blue", "yellow"]`, cosa restituisce `colors[-1]`?

<div class="upper-alpha" markdown>
1. `"red"` (il primo elemento)
2. Un errore, perché gli indici negativi non sono validi per le liste
3. `"green"` (il secondo elemento)
4. `"yellow"` (l'ultimo elemento)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Gli indici negativi contano dalla fine della lista. L'indice `-1` è l'ultimo elemento, `-2` è il penultimo, e così via. Per `["red", "green", "blue", "yellow"]`, `colors[-1]` è `"yellow"`. Questo è utile quando vuoi l'ultimo elemento senza conoscere la lunghezza della lista.

    **Concept Tested:** Negative Indexing

---

#### 4. Cosa restituisce `scores[1:3]` per `scores = [95, 87, 100, 73]`?

<div class="upper-alpha" markdown>
1. `[87, 100, 73]`
2. `[87, 100]`
3. `[95, 87, 100]`
4. `[100, 73]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Lo slicing delle liste `[start:end]` restituisce gli elementi dall'indice `start` fino a ma NON includendo l'indice `end`. `scores[1:3]` dà gli elementi agli indici 1 e 2: `[87, 100]`. L'elemento all'indice 3 (`73`) non è incluso. Questa è la stessa regola dello slicing delle stringhe.

    **Concept Tested:** List Slicing

---

#### 5. Cosa restituisce `len(["apple", "banana", "kiwi"])`?

<div class="upper-alpha" markdown>
1. `15` (il numero totale di caratteri in tutte le parole)
2. `2`
3. `3`
4. `0`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `len()` conta il numero di **elementi** in una lista, non il numero di caratteri negli elementi. La lista `["apple", "banana", "kiwi"]` ha 3 elementi, quindi `len()` restituisce `3`. `len()` funziona allo stesso modo sulle stringhe (contando i caratteri) e su altre collezioni.

    **Concept Tested:** List Length with len()

---

#### 6. Come controlli se `"mango"` è nella lista `fruits = ["apple", "banana", "mango"]`?

<div class="upper-alpha" markdown>
1. `fruits.contains("mango")`
2. `fruits.find("mango")`
3. `"mango" in fruits`
4. `fruits["mango"]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'operatore `in` controlla l'appartenenza e restituisce `True` o `False`. `"mango" in fruits` restituisce `True` perché `"mango"` è nella lista. Puoi anche usare `not in` per controllare che qualcosa sia assente. Questo funziona allo stesso modo per le stringhe: `"py" in "python"` restituisce `True`.

    **Concept Tested:** Membership with in

---

#### 7. Qual è la differenza fondamentale tra i tipi mutabili e immutabili?

<div class="upper-alpha" markdown>
1. I tipi mutabili sono più veloci; i tipi immutabili sono più lenti
2. I tipi mutabili possono essere cambiati dopo la creazione; i tipi immutabili no
3. I tipi mutabili contengono numeri; i tipi immutabili contengono stringhe
4. I tipi mutabili si creano con `[]`; i tipi immutabili usano `()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un oggetto mutabile può essere cambiato dopo essere stato creato — puoi aggiornare, aggiungere, o rimuovere elementi. Una lista è mutabile: `colors[0] = "purple"` funziona. Un oggetto immutabile non può essere cambiato — devi crearne uno nuovo invece. Le stringhe sono immutabili: `word[0] = "H"` genera un `TypeError`.

    **Concept Tested:** Mutable vs Immutable

---

#### 8. Cosa fa `colors[1] = "purple"` alla lista `colors = ["red", "green", "blue"]`?

<div class="upper-alpha" markdown>
1. Aggiunge `"purple"` alla fine della lista
2. Crea una lista completamente nuova con `"purple"` inserito
3. Sostituisce `"green"` (all'indice 1) con `"purple"` nella lista esistente
4. Genera un `TypeError` perché le liste non possono essere cambiate
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Le liste sono mutabili, quindi puoi assegnare un nuovo valore a qualsiasi indice esistente. `colors[1] = "purple"` cambia l'elemento all'indice 1 da `"green"` a `"purple"`. Dopo questa riga, `colors` è `["red", "purple", "blue"]`. Questa modifica sul posto è una delle caratteristiche chiave che distingue le liste dai tipi immutabili come le stringhe.

    **Concept Tested:** List Indexing

---

#### 9. Quale delle seguenti crea correttamente una lista vuota?

<div class="upper-alpha" markdown>
1. `my_list = {}`
2. `my_list = None`
3. `my_list = ()`
4. `my_list = []`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Una lista vuota si crea con `[]` — parentesi quadre senza nulla dentro. `{}` crea un dizionario vuoto (o un set), `()` crea una tupla vuota, e `None` è un valore speciale che significa "niente qui." Puoi poi aggiungere elementi alla lista vuota usando metodi come `append()`.

    **Concept Tested:** List Type

---

#### 10. Cosa succede quando provi ad accedere a `colors[10]` su una lista che ha solo 4 elementi?

<div class="upper-alpha" markdown>
1. Python restituisce `None` per qualsiasi indice fuori intervallo
2. Python restituisce l'ultimo elemento della lista
3. Python genera un `IndexError` perché l'indice è fuori intervallo
4. Python estende automaticamente la lista con elementi vuoti fino all'indice 10
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Accedere a un indice che non esiste in una lista genera un `IndexError: list index out of range`. Per una lista con 4 elementi, gli indici positivi validi sono 0, 1, 2, e 3. Provare ad accedere all'indice 10 (o all'indice 4 o superiore) causa un errore. Assicurati sempre che il tuo indice sia nell'intervallo valido.

    **Concept Tested:** List Indexing

---
