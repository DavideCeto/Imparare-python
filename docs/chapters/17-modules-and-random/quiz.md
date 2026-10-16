# Quiz: Moduli e Numeri Casuali

Verifica la tua comprensione dei moduli Python, della sintassi di import, e del modulo random con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa fa l'istruzione `import` in cima a un programma Python?

<div class="upper-alpha" markdown>
1. Salva il tuo programma in un file
2. Carica un modulo così che il tuo programma possa usare le sue funzioni e valori
3. Esegue un altro file Python dentro il tuo programma attuale
4. Crea una nuova variabile con il nome del modulo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `import module_name` carica un modulo dalla Libreria Standard di Python (o un pacchetto installato) e rende disponibili le sue funzioni. Dopo `import random`, accedi alle sue funzioni con `random.function_name()`. Il modulo viene caricato solo una volta, anche se lo importi più volte.

    **Concept Tested:** import Statement

---

#### 2. Qual è la differenza tra `import random` e `from random import randint`?

<div class="upper-alpha" markdown>
1. `import random` carica solo `randint`; `from random import randint` carica tutto
2. `import random` richiede `random.randint()`; `from random import randint` ti permette di chiamare `randint()` direttamente senza il prefisso
3. `from random import randint` è più lento di `import random`
4. Sono identici — entrambi ti permettono di chiamare `random.randint()` nello stesso modo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `import random` importa l'intero modulo, e accedi alle funzioni con `random.randint()`. `from random import randint` importa solo la funzione `randint` per nome, così puoi chiamarla direttamente come `randint()` senza il prefisso `random.`. Entrambi gli approcci funzionano; il secondo è più conciso quando hai bisogno solo di una o due funzioni.

    **Concept Tested:** from...import Syntax

---

#### 3. Cosa fa `import random as rnd`?

<div class="upper-alpha" markdown>
1. Crea una copia del modulo `random` chiamata `rnd`
2. Importa solo la funzione `rnd` da `random`
3. Importa il modulo `random` e gli dà l'alias `rnd`, così usi `rnd.randint()` invece di `random.randint()`
4. Rinomina tutte le funzioni in `random` perché iniziano con `rnd_`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `import ... as alias` importa un modulo e gli dà un soprannome più corto. Dopo `import random as rnd`, chiami `rnd.randint(1, 6)` invece di `random.randint(1, 6)`. Questo è comunemente usato per moduli con nomi lunghi (come `numpy as np` o `matplotlib.pyplot as plt`) per risparmiare digitazione.

    **Concept Tested:** import...as Alias

---

#### 4. Cosa restituisce `random.randint(1, 6)`?

<div class="upper-alpha" markdown>
1. Un float casuale tra 1.0 e 6.0
2. Un intero casuale da 1 a 5, senza includere 6
3. Un intero casuale da 1 a 6, includendo sia 1 sia 6
4. Sempre il numero 3 (il punto medio)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `randint(a, b)` restituisce un intero casuale dove entrambi gli estremi sono inclusi: `a <= result <= b`. Quindi `randint(1, 6)` può restituire 1, 2, 3, 4, 5, o 6 — simulando un dado a sei facce onesto. Questo è diverso da `range(1, 6)` che si ferma prima di 6.

    **Concept Tested:** random.randint()

---

#### 5. Cosa restituisce `random.random()`?

<div class="upper-alpha" markdown>
1. Un intero casuale tra 0 e 100
2. Un float casuale tra 0.0 e 1.0 (escluso 1.0)
3. Una scelta casuale da una lista che fornisci
4. Un booleano casuale — `True` oppure `False`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `random.random()` restituisce un numero a virgola mobile casuale nell'intervallo `[0.0, 1.0)` — cioè, 0.0 è possibile ma 1.0 no. Questo è utile per le probabilità: `if random.random() < 0.3:` si attiva circa il 30% delle volte. Moltiplica per un intervallo per ottenere float in altri range: `random.random() * 10` dà un float da 0 a 10.

    **Concept Tested:** random.random()

---

#### 6. Cosa fa `random.choice(["rock", "paper", "scissors"])`?

<div class="upper-alpha" markdown>
1. Restituisce tutti e tre gli elementi come una lista
2. Restituisce `None` dopo aver stampato una scelta casuale
3. Sceglie e restituisce un elemento casuale dalla lista
4. Mescola la lista sul posto e la restituisce
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `random.choice(sequence)` sceglie un elemento casuale dalla sequenza e lo restituisce. Ogni elemento ha una probabilità uguale di essere scelto. Questo è perfetto per simulare lanci di moneta, scelte casuali di colori, direzioni casuali in un gioco, e compiti simili.

    **Concept Tested:** random.choice()

---

#### 7. Cosa fa `random.shuffle(cards)`?

<div class="upper-alpha" markdown>
1. Restituisce una nuova copia mescolata di `cards`, lasciando l'originale invariata
2. Mescola la lista `cards` sul posto e restituisce `None`
3. Rimuove elementi casuali da `cards` finché non è vuota
4. Ordina `cards` casualmente (come `sort()` ma con ordine casuale)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `random.shuffle(lst)` mescola la lista **sul posto**, riorganizzando i suoi elementi casualmente, e restituisce `None`. Questo significa che la lista originale viene cambiata direttamente — una nuova lista NON viene creata. Quindi `shuffled = random.shuffle(cards)` farebbe diventare `shuffled` uguale a `None`, non una lista mescolata.

    **Concept Tested:** random.shuffle()

---

#### 8. Qual è lo scopo di `random.seed(42)`?

<div class="upper-alpha" markdown>
1. Rende il modulo random 42 volte più veloce
2. Limita i numeri casuali a valori inferiori a 42
3. Imposta un punto di partenza così che la sequenza casuale sia la stessa ogni volta che esegui il programma con quel seme
4. Genera esattamente 42 numeri casuali e poi si ferma
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `random.seed(n)` imposta il punto di partenza per il generatore di numeri casuali. Con lo stesso seme, ottieni sempre la stessa sequenza di numeri "casuali". Questo è molto utile per i test e il debug — puoi riprodurre gli stessi risultati casuali a ogni esecuzione. Senza un seme, Python usa l'ora attuale come seme, dando risultati diversi a ogni esecuzione.

    **Concept Tested:** random.seed()

---

#### 9. Quale riga `from...import` ti permette di chiamare `randint()` senza il prefisso `random.`?

<div class="upper-alpha" markdown>
1. `import randint from random`
2. `import random.randint`
3. `from random import randint`
4. `from randint import random`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La sintassi corretta per importare una funzione specifica è `from module import function`. Dopo `from random import randint`, puoi chiamare `randint(1, 6)` direttamente senza il prefisso `random.`. Le opzioni A e D hanno le parole nell'ordine sbagliato, e l'opzione B richiederebbe comunque di chiamare `random.randint()`.

    **Concept Tested:** from...import Syntax

---

#### 10. Cosa restituisce `random.sample(range(1, 50), 6)`?

<div class="upper-alpha" markdown>
1. 6 numeri casuali da 1 a 50, con duplicati possibili
2. I numeri da 1 a 6 in ordine casuale
3. Una lista di 6 numeri casuali unici scelti da 1 a 49
4. Il numero 6 ripetuto 50 volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `random.sample(population, k)` restituisce una lista di `k` elementi unici scelti dalla popolazione senza ripetizione (nessun duplicato). `sample(range(1, 50), 6)` sceglie 6 numeri unici da 1 a 49 — come scegliere i numeri della lotteria. Nota che `range(1, 50)` va da 1 a 49, non a 50.

    **Concept Tested:** random.sample()

---
