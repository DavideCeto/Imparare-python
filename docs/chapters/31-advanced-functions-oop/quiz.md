# Quiz: Funzioni Avanzate e OOP

Verifica la tua comprensione di map(), filter(), any(), all(), delle eccezioni personalizzate, delle proprietà, dei metodi dunder, e della composizione di oggetti con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa fa `map(square, [1, 2, 3, 4])`?

<div class="upper-alpha" markdown>
1. Restituisce la somma di tutti i quadrati
2. Restituisce una lista ordinata di quadrati
3. Applica la funzione `square` a ogni elemento e restituisce un iteratore dei risultati
4. Filtra la lista per includere solo numeri che sono quadrati perfetti
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `map(function, iterable)` applica la funzione a ogni elemento e restituisce un oggetto map (iteratore). Racchiudilo con `list()` per ottenere una lista: `list(map(square, [1, 2, 3, 4]))` dà `[1, 4, 9, 16]`. `map()` è uno strumento di programmazione funzionale — spesso sostituito dalle list comprehension nel Python moderno, ma ancora utile e conciso.

    **Concept Tested:** map()

---

#### 2. Cosa restituisce `filter(is_even, [1, 2, 3, 4, 5, 6])`?

<div class="upper-alpha" markdown>
1. Il conteggio dei numeri pari: `3`
2. Un oggetto filter (iteratore) che produce solo gli elementi dove `is_even` restituisce `True`
3. Il primo numero pari trovato: `2`
4. Una lista di numeri dispari: `[1, 3, 5]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `filter(function, iterable)` restituisce un oggetto filter (iteratore) che produce solo gli elementi per cui la funzione restituisce `True`. Racchiudi con `list()` per ottenere una lista: `list(filter(is_even, [1,2,3,4,5,6]))` dà `[2, 4, 6]`. Come `map()`, `filter()` è lazy — elabora gli elementi uno alla volta secondo necessità.

    **Concept Tested:** filter()

---

#### 3. Cosa restituisce `any([False, False, True, False])`?

<div class="upper-alpha" markdown>
1. `False` (non tutti gli elementi sono True)
2. `1` (il conteggio degli elementi True)
3. `True` (almeno un elemento è truthy)
4. `[True]` (una lista di solo gli elementi truthy)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `any(iterable)` restituisce `True` se almeno un elemento nell'iterabile è truthy. Fa corto circuito — non appena trova un elemento truthy, si ferma e restituisce `True` senza controllare il resto. `all(iterable)` restituisce `True` solo se ogni elemento è truthy, e fa corto circuito al primo elemento falsy.

    **Concept Tested:** any() and all()

---

#### 4. Cosa restituisce `ord("A")`?

<div class="upper-alpha" markdown>
1. La stringa `"a"` (versione minuscola)
2. `1` (A è la 1ª lettera dell'alfabeto)
3. `"A1"` (lettera e la sua posizione combinate)
4. `65` (il codice intero ASCII/Unicode per A maiuscola)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `ord(character)` restituisce il codice intero Unicode (ASCII) per un carattere. `ord("A")` è `65`, `ord("B")` è `66`, e così via. La funzione inversa è `chr(integer)`: `chr(65)` restituisce `"A"`. Sono utili per implementare cifrari, matematica sui caratteri, o generare sequenze di caratteri in un ciclo.

    **Concept Tested:** chr() and ord()

---

#### 5. Cosa ti mostra `dir(math)`?

<div class="upper-alpha" markdown>
1. Il codice sorgente del modulo math
2. Una lista di tutti gli attributi e i metodi disponibili sul modulo math
3. La documentazione per ogni funzione math
4. La posizione del file del modulo math sul disco
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `dir(obj)` restituisce una lista di tutti gli attributi e i metodi disponibili su un oggetto o modulo. `dir(math)` mostra tutte le funzioni disponibili nel modulo `math` (come `sqrt`, `sin`, `pi`, `factorial`, ecc.). Per la documentazione dettagliata su una funzione, usa `help(math.sqrt)`. Insieme, `dir()` e `help()` sono strumenti essenziali per esplorare moduli non familiari.

    **Concept Tested:** dir() and help()

---

#### 6. Come crei una classe di eccezione personalizzata in Python?

<div class="upper-alpha" markdown>
1. `def CustomError(): raise Exception`
2. `class CustomError(Exception): pass`
3. `error CustomError = new Exception()`
4. `CustomError = Exception("custom message")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Le classi di eccezione personalizzate si creano facendo una sottoclasse di `Exception` (o un'eccezione built-in più specifica come `ValueError`). La forma più semplice è `class MyError(Exception): pass`. Puoi anche sovrascrivere `__init__()` per aggiungere attributi o messaggi personalizzati. Chi chiama può catturare la tua eccezione personalizzata specificamente con `except MyError:`, rendendo la gestione degli errori molto più precisa.

    **Concept Tested:** Custom Exception Classes

---

#### 7. Per cosa si usa il decorator `@property`?

<div class="upper-alpha" markdown>
1. Per far girare automaticamente un metodo quando la classe viene importata
2. Per trasformare un metodo in un attributo che può essere letto senza chiamarlo con le parentesi, permettendoti di aggiungere logica di validazione
3. Per impedire che il metodo venga ereditato dalle sottoclassi
4. Per segnare un metodo come variabile di classe invece che come metodo di istanza
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il decorator `@property` ti permette di definire un metodo che viene accesso come un attributo — `obj.temperature` invece di `obj.temperature()`. Puoi aggiungere un corrispondente `@temperature.setter` per eseguire codice di validazione quando il valore viene assegnato. Questo ti dà una sintassi degli attributi pulita mantenendo il controllo su come i valori vengono letti e impostati.

    **Concept Tested:** @property Decorator

---

#### 8. Cos'è un metodo dunder (chiamato anche metodo magico) in Python?

<div class="upper-alpha" markdown>
1. Un metodo che può essere chiamato solo una volta per esecuzione del programma
2. Un metodo che inizia e finisce con doppio underscore che Python chiama automaticamente in risposta a operazioni specifiche come la stampa o l'aritmetica
3. Un metodo nascosto da `dir()` e inaccessibile al programmatore
4. Un metodo che gira in un thread separato per migliori prestazioni
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. I metodi dunder (metodi con doppio underscore) come `__init__`, `__str__`, `__add__`, e `__len__` vengono chiamati automaticamente da Python in risposta a operazioni. `__str__` viene chiamato da `print()`, `__add__` viene chiamato dall'operatore `+`, e `__len__` viene chiamato da `len()`. Definirli sulla tua classe personalizza come funzionano le operazioni built-in di Python con i tuoi oggetti.

    **Concept Tested:** Dunder Methods

---

#### 9. Cos'è la composizione di oggetti?

<div class="upper-alpha" markdown>
1. Usare l'eredità multipla per combinare caratteristiche da diverse classi genitore
2. Costruire oggetti complessi contenendo oggetti più semplici come attributi, invece di usare l'eredità
3. Combinare due liste di oggetti in una
4. Comprimere i dati di un oggetto per risparmiare memoria
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La composizione è la relazione "ha-un" (has-a): un oggetto `Car` *ha* un oggetto `Engine` e un oggetto `Wheel` come attributi. Questo è diverso dall'eredità (la relazione "è-un", is-a). La composizione è spesso preferita alle profonde gerarchie di eredità perché è più flessibile e più facile da cambiare — puoi sostituire il componente motore senza cambiare l'interfaccia dell'auto.

    **Concept Tested:** Object Composition

---

#### 10. Cosa restituisce `all([True, True, True, False])`?

<div class="upper-alpha" markdown>
1. `True` (la maggior parte degli elementi sono True)
2. `False` (non ogni elemento è True)
3. `3` (il conteggio degli elementi True)
4. `[True, True, True]` (gli elementi truthy)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `all(iterable)` restituisce `True` solo se ogni elemento nell'iterabile è truthy. Dato che la lista `[True, True, True, False]` contiene un `False`, `all()` restituisce `False`. Fa corto circuito — nel momento in cui trova il primo elemento falsy, si ferma e restituisce `False` senza controllare gli elementi rimanenti.

    **Concept Tested:** any() and all()

---
