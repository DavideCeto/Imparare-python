# Quiz: Collezioni Avanzate e Funzioni Built-in

Verifica la tua comprensione di enumerate(), zip(), *args, **kwargs, e delle funzioni built-in di Python con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa ti dà `enumerate(["a", "b", "c"])` in un ciclo?

<div class="upper-alpha" markdown>
1. Solo gli elementi: `"a"`, `"b"`, `"c"`
2. Solo gli indici: `0`, `1`, `2`
3. Sia l'indice sia l'elemento come coppie: `(0, "a")`, `(1, "b")`, `(2, "c")`
4. Gli elementi in ordine inverso: `"c"`, `"b"`, `"a"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `enumerate(iterable)` incapsula una sequenza e ti dà sia l'indice sia l'elemento a ogni iterazione del ciclo. Usare `for i, item in enumerate(my_list):` è più pulito che mantenere una variabile contatore separata. Per default il conteggio inizia da 0; passa un secondo argomento per iniziare da un numero diverso: `enumerate(items, 1)` inizia da 1.

    **Concept Tested:** enumerate()

---

#### 2. Cosa produce `zip(["A", "B", "C"], [1, 2])`?

<div class="upper-alpha" markdown>
1. `[("A", 1), ("B", 2), ("C", None)]`
2. `[("A", 1), ("B", 2)]`
3. `["A", "B", "C", 1, 2]`
4. Un errore perché le liste hanno lunghezze diverse
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `zip()` accoppia gli elementi di due o più iterabili e si ferma quando il più corto finisce. Dato che la seconda lista ha solo 2 elementi, `zip()` produce solo 2 coppie: `("A", 1)` e `("B", 2)`. Il terzo elemento `"C"` viene ignorato perché non c'è un elemento corrispondente nella seconda lista.

    **Concept Tested:** zip()

---

#### 3. Come costruisci un dizionario da due liste `keys` e `values` usando `zip()`?

<div class="upper-alpha" markdown>
1. `{keys: values}`
2. `dict(keys, values)`
3. `dict(zip(keys, values))`
4. `zip(dict(keys), dict(values))`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `zip(keys, values)` accoppia ogni chiave con il suo valore corrispondente. Racchiudere con `dict()` converte quelle coppie in un dizionario. Per esempio, `dict(zip(["a", "b"], [1, 2]))` dà `{"a": 1, "b": 2}`. Questo è un pattern molto comune e pulito per costruire dizionari da liste parallele.

    **Concept Tested:** Dictionary from zip()

---

#### 4. Cosa fa `*args` in una definizione di funzione?

<div class="upper-alpha" markdown>
1. Crea un argomento obbligatorio che deve sempre essere fornito
2. Raccoglie tutti gli argomenti posizionali extra in una tupla
3. Scompone una lista in argomenti separati
4. Segna un parametro come opzionale con un valore predefinito di `None`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `*args` in una definizione di funzione raccoglie qualsiasi numero di argomenti posizionali che chi chiama passa in una singola tupla. Per esempio, `def total(*args): return sum(args)` può essere chiamata come `total(1, 2, 3)` o `total(10)` — gli argomenti posizionali extra finiscono tutti in `args`.

    **Concept Tested:** *args

---

#### 5. Cosa raccoglie `**kwargs` in una definizione di funzione?

<div class="upper-alpha" markdown>
1. Argomenti posizionali extra come una lista
2. Argomenti keyword extra come un dizionario
3. Un insieme fisso di argomenti keyword con tipi obbligatori
4. Tutti gli argomenti di qualsiasi tipo in una singola tupla
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `**kwargs` raccoglie gli argomenti keyword extra (quelli passati come `name=value`) in un dizionario. Chiamare `describe(color="red", size=5)` darebbe `kwargs = {"color": "red", "size": 5}` dentro la funzione. Poi ci iteri sopra con `kwargs.items()`. `*args` gestisce gli argomenti posizionali; `**kwargs` gestisce gli argomenti keyword.

    **Concept Tested:** **kwargs

---

#### 6. Cosa restituisce `max([73, 100, 87, 55])`?

<div class="upper-alpha" markdown>
1. `55`
2. `73`
3. `415` (la somma)
4. `100`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `max(iterable)` restituisce il valore più grande nella collezione. Per `[73, 100, 87, 55]`, il valore più grande è `100`. In modo simile, `min()` restituisce il valore più piccolo (`55` qui), e `sum()` restituisce il totale (`415`). Tutte e tre funzionano su qualsiasi iterabile di valori comparabili.

    **Concept Tested:** max(), min(), sum()

---

#### 7. Qual è la differenza tra `list.sort()` e `sorted(list)`?

<div class="upper-alpha" markdown>
1. `sort()` funziona sulle stringhe; `sorted()` funziona sui numeri
2. `sort()` modifica la lista sul posto e restituisce `None`; `sorted()` restituisce una nuova lista ordinata senza cambiare l'originale
3. `sort()` è crescente; `sorted()` è sempre decrescente
4. Producono risultati identici in ogni modo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `list.sort()` riorganizza la lista **sul posto** e restituisce `None`. `sorted(iterable)` crea e restituisce una **nuova** lista ordinata, lasciando l'originale invariata. Usa `sort()` quando vuoi cambiare la lista direttamente. Usa `sorted()` quando hai bisogno di mantenere l'ordine originale avendo anche una versione ordinata.

    **Concept Tested:** sorted() and reversed()

---

#### 8. Cosa restituisce `isinstance(42, int)`?

<div class="upper-alpha" markdown>
1. `"int"`
2. `False`
3. `42`
4. `True`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `isinstance(value, type)` restituisce `True` se il valore è un'istanza del tipo dato, `False` altrimenti. `42` è un intero, quindi `isinstance(42, int)` restituisce `True`. Questo è il modo preferito di controllare i tipi in Python perché gestisce anche l'eredità, a differenza di `type(x) == int` che non lo fa.

    **Concept Tested:** isinstance()

---

#### 9. Cosa restituisce `sorted([5, 2, 8, 1], reverse=True)`?

<div class="upper-alpha" markdown>
1. `[1, 2, 5, 8]`
2. `[8, 5, 2, 1]`
3. `[5, 2, 8, 1]` (invariata)
4. `[8, 5, 1, 2]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `sorted(iterable, reverse=True)` restituisce una nuova lista ordinata in ordine decrescente (il più grande prima). Per `[5, 2, 8, 1]`, il risultato è `[8, 5, 2, 1]`. La lista originale non viene modificata. Per ordinare in modo crescente (il default), usa semplicemente `sorted(iterable)` senza l'argomento `reverse`.

    **Concept Tested:** sorted() and reversed()

---

#### 10. Cosa produce `enumerate(["x", "y", "z"], 1)` come primo valore in un ciclo?

<div class="upper-alpha" markdown>
1. `(0, "x")`
2. `(1, "y")`
3. `("x", 1)`
4. `(1, "x")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `enumerate(iterable, start)` inizia a contare dal valore `start` invece che da 0. Con `enumerate(["x", "y", "z"], 1)`, la prima coppia è `(1, "x")`, la seconda è `(2, "y")`, e così via. Questo è utile quando vuoi mostrare liste numerate a partire da 1 invece che da 0.

    **Concept Tested:** enumerate()

---
