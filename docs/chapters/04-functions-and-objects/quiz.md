# Quiz: Funzioni e Oggetti

Verifica la tua comprensione sulla definizione di funzioni, i parametri, i valori di ritorno e la Standard Library con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale parola chiave Python usi per definire una nuova funzione?

<div class="upper-alpha" markdown>
1. `function`
2. `make`
3. `def`
4. `create`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La parola chiave `def` (abbreviazione di "define", definisci) inizia una definizione di funzione in Python. Scrivi `def`, poi il nome della funzione, poi le parentesi, poi i due punti. Tutto ciò che è indentato sotto quella riga diventa il corpo della funzione — i passaggi che vengono eseguiti quando chiami la funzione.

    **Concept Tested:** def Keyword

---

#### 2. Qual è la differenza tra definire una funzione e chiamare una funzione?

<div class="upper-alpha" markdown>
1. Definire esegue la funzione; chiamare ne scrive la ricetta
2. Definire scrive i passaggi sotto un nome; chiamare dice "esegui quei passaggi adesso"
3. Sono la stessa cosa — definire e chiamare avvengono nello stesso momento
4. Definire rimuove la funzione dalla memoria; chiamare la crea
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Definire una funzione (con `def`) scrive la ricetta e la memorizza sotto un nome — Python la legge ma non la esegue ancora. Chiamare una funzione (scrivendo il suo nome con le parentesi) dice a Python di eseguire subito i passaggi memorizzati. Puoi definire una volta e chiamare molte volte.

    **Concept Tested:** Function Calls

---

#### 3. Quante righe di output produrrà questo programma?

```python
def say_hi():
    print("Hi!")
    print("Welcome!")

say_hi()
say_hi()
```

<div class="upper-alpha" markdown>
1. 2 righe
2. 4 righe
3. 1 riga
4. 6 righe
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La funzione `say_hi()` contiene due chiamate a `print()`, quindi ogni chiamata alla funzione produce 2 righe di output. Il programma chiama `say_hi()` due volte, per un totale di 2 × 2 = 4 righe. Questo mostra il potere delle funzioni — scrivi i passaggi una volta, eseguili tutte le volte che ti servono.

    **Concept Tested:** Function Calls

---

#### 4. Cos'è un parametro in una funzione Python?

<div class="upper-alpha" markdown>
1. I due punti alla fine della riga `def`
2. Una variabile dichiarata dentro le parentesi che riceve un valore quando la funzione viene chiamata
3. Il nome del modulo in cui è memorizzata la funzione
4. Un commento che spiega cosa fa la funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un parametro è una variabile elencata dentro le parentesi di un'istruzione `def`. Quando chiami la funzione e fornisci un valore, Python copia quel valore nel parametro. Dentro il corpo della funzione, il parametro funziona esattamente come qualsiasi altra variabile. Il valore che fornisci al momento della chiamata si chiama argomento.

    **Concept Tested:** Positional Parameters

---

#### 5. Cosa stamperà questo codice?

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Monty")
```

<div class="upper-alpha" markdown>
1. `Hello, name!`
2. `Hello, Monty!`
3. `greet("Monty")`
4. Un errore, perché `name` non è definita fuori dalla funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Quando viene chiamata `greet("Monty")`, la stringa `"Monty"` viene copiata nel parametro `name`. Dentro la funzione, `"Hello, " + name + "!"` diventa `"Hello, Monty!"`, che viene stampato. Il parametro `name` è definito solo dentro la funzione, quindi otterresti un errore provando a usare `name` fuori da essa — ma la chiamata in sé funziona perfettamente.

    **Concept Tested:** Positional Parameters

---

#### 6. Cosa fa l'istruzione `return` in una funzione?

<div class="upper-alpha" markdown>
1. Stampa il risultato sullo schermo
2. Restituisce un valore al codice che ha chiamato la funzione
3. Ripete il corpo della funzione dall'inizio
4. Termina immediatamente l'intero programma
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'istruzione `return` restituisce un valore a qualsiasi codice abbia chiamato la funzione. Chi ha effettuato la chiamata può poi memorizzare quel valore in una variabile o usarlo direttamente. `return` è diverso da `print()` — `print` mostra qualcosa sullo schermo, mentre `return` passa indietro un valore in modo invisibile così il tuo programma può usarlo ulteriormente.

    **Concept Tested:** Return Values

---

#### 7. Quale valore restituisce Python da una funzione che non ha un'istruzione `return`?

<div class="upper-alpha" markdown>
1. `0`
2. `False`
3. `None`
4. Una stringa vuota `""`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Se una funzione termina l'esecuzione senza incontrare un'istruzione `return`, Python restituisce automaticamente `None`. Questo si chiama "funzioni che restituiscono None." Un bug molto comune tra i principianti è dimenticare di scrivere `return` in una funzione che calcola qualcosa — la funzione viene eseguita ma il risultato sparisce, e chi l'ha chiamata riceve `None` invece del valore atteso.

    **Concept Tested:** Functions Returning None

---

#### 8. Dove dovrebbe essere posizionata una docstring dentro una funzione?

<div class="upper-alpha" markdown>
1. Dopo l'ultima riga del corpo della funzione
2. Prima della parola chiave `def`, su una riga separata
3. Come prima riga dentro il corpo della funzione, tra triple virgolette
4. In un commento con `#` in un punto qualsiasi dentro la funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una docstring è una stringa racchiusa tra triple virgolette (`"""`) posizionata come primissima riga dentro il corpo della funzione. Gli strumenti Python possono leggere le docstring automaticamente e mostrarle come testo di aiuto. Le docstring spiegano cosa fa la funzione, i suoi parametri, e cosa restituisce — aiutando il prossimo lettore (spesso il te stesso del futuro) a capire rapidamente il codice.

    **Concept Tested:** Docstrings

---

#### 9. Cos'è la Standard Library di Python?

<div class="upper-alpha" markdown>
1. Un sito web da cui scaricare pacchetti Python aggiuntivi
2. Una collezione di moduli già scritti che arriva con ogni installazione di Python
3. L'insieme delle parole chiave di Python riservate per il linguaggio
4. Un file speciale che crei per memorizzare tutte le tue funzioni
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La Standard Library è una grande collezione di moduli già scritti (come `math`, `random`, `time` e `turtle`) che viene fornita insieme a ogni installazione di Python, gratuitamente. Importi un modulo nel tuo programma usando `import`, poi accedi alle sue funzioni con la notazione a punto: `math.sqrt(25)`.

    **Concept Tested:** Standard Library

---

#### 10. Cosa significa il punto in `math.sqrt(16)`?

<div class="upper-alpha" markdown>
1. Moltiplica `math` per `sqrt`
2. Accede alla funzione `sqrt` che si trova dentro il modulo `math`
3. Separa un numero intero da un decimale
4. Segna la fine della chiamata di funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il punto in `math.sqrt(16)` è la notazione a punto — collega il nome del modulo (`math`) a una funzione che si trova al suo interno (`sqrt`). Dopo aver scritto `import math`, accedi a tutto ciò che è dentro il modulo in questo modo: nome del modulo, punto, poi la funzione o il valore che vuoi. Userai questo schema per tutto il corso.

    **Concept Tested:** Standard Library

---
