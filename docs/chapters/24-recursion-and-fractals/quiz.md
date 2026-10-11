# Quiz: Ricorsione e Frattali

Verifica la tua comprensione della ricorsione, dei casi base, delle funzioni lambda, e dello stack delle chiamate con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è la ricorsione in Python?

<div class="upper-alpha" markdown>
1. Un ciclo che si ripete un numero fisso di volte
2. Una funzione che chiama sé stessa per risolvere una versione più piccola dello stesso problema
3. Un metodo che inverte una lista o una stringa
4. Un modo di importare funzioni da un altro file
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La ricorsione è quando una funzione chiama sé stessa. Ogni chiamata lavora su una versione più piccola o più semplice del problema, finché non raggiunge un punto di arresto (il caso base) e inizia a restituire valori lungo la catena. Pensa alle bambole russe matrioska — ognuna contiene una versione più piccola di sé stessa, fino a quella minuscola e solida al centro.

    **Concept Tested:** Recursion Concept

---

#### 2. Cos'è un caso base in una funzione ricorsiva?

<div class="upper-alpha" markdown>
1. La prima volta che la funzione viene chiamata dal programma principale
2. Una variabile che conta quante volte la funzione ha chiamato sé stessa
3. La condizione che ferma la ricorsione e restituisce un valore senza chiamare di nuovo la funzione
4. Il livello di indentazione più profondo dentro la funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il caso base è ciò che impedisce a una funzione ricorsiva di chiamare sé stessa per sempre. È una condizione che, quando vera, restituisce un valore direttamente invece di fare un'altra chiamata ricorsiva. Senza un caso base, Python chiamerebbe la funzione indefinitamente finché non genera un `RecursionError` (profondità massima di ricorsione superata).

    **Concept Tested:** Base Case

---

#### 3. Cosa restituisce `factorial(5)` se `factorial(n)` restituisce `n * factorial(n-1)` con un caso base di `factorial(1) = 1`?

<div class="upper-alpha" markdown>
1. `15` (5 + 4 + 3 + 2 + 1)
2. `120` (5 × 4 × 3 × 2 × 1)
3. `25` (5 al quadrato)
4. `5` (solo l'input)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `factorial(5)` si espande come: `5 * factorial(4)` → `5 * 4 * factorial(3)` → `5 * 4 * 3 * factorial(2)` → `5 * 4 * 3 * 2 * factorial(1)` → `5 * 4 * 3 * 2 * 1 = 120`. Il fattoriale (n!) moltiplica tutti gli interi positivi fino a n.

    **Concept Tested:** Recursive Factorial

---

#### 4. Cosa succede se una funzione ricorsiva non ha un caso base?

<div class="upper-alpha" markdown>
1. Python aggiunge automaticamente un caso base quando n raggiunge 0
2. La funzione gira esattamente 1.000 volte e poi si ferma
3. Python genera un `RecursionError` quando lo stack delle chiamate diventa troppo profondo
4. La funzione restituisce `None` dopo la prima chiamata
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Senza un caso base, la funzione continua a chiamare sé stessa indefinitamente. Python limita lo stack delle chiamate a circa 1.000 chiamate annidate per default. Quando quel limite viene superato, Python genera `RecursionError: maximum recursion depth exceeded`. Assicurati sempre che la tua funzione ricorsiva abbia un caso base che verrà raggiunto alla fine.

    **Concept Tested:** Base Case

---

#### 5. Cos'è lo stack delle chiamate nel contesto della ricorsione?

<div class="upper-alpha" markdown>
1. Una lista di tutti i nomi delle funzioni definite nel programma
2. La memoria che Python usa per salvare lo stato attuale di ogni chiamata di funzione mentre aspetta che le chiamate interne tornino
3. L'output stampato da ogni chiamata ricorsiva in ordine
4. Una struttura built-in di Python che limita i cicli a 1.000 iterazioni
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Ogni volta che una funzione chiama sé stessa ricorsivamente, Python salva lo stato attuale (variabili locali, dove si è interrotta) sullo stack delle chiamate. Quando viene raggiunto il caso base, Python risale lo stack, riprendendo ogni stato salvato in ordine inverso. Lo stack delle chiamate cresce con ogni chiamata ricorsiva e si riduce quando le chiamate tornano.

    **Concept Tested:** Call Stack

---

#### 6. Cos'è una funzione lambda in Python?

<div class="upper-alpha" markdown>
1. Una funzione che prende una lista come unico argomento
2. Una funzione definita dentro un'altra funzione
3. Una piccola funzione anonima su una riga scritta con la parola chiave `lambda`
4. Una funzione che fa automaticamente ricorsione finché non trova un caso base
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una lambda è una funzione anonima compatta: `lambda parametri: espressione`. Per esempio, `square = lambda x: x * x` crea una funzione su una riga che eleva al quadrato il suo input. Le lambda sono particolarmente utili quando hai bisogno di una funzione breve da passare come argomento a un'altra funzione (come `sorted()` con un argomento `key=`).

    **Concept Tested:** Lambda Functions

---

#### 7. Cosa fa `lambda a, b: a + b`?

<div class="upper-alpha" markdown>
1. Crea una funzione che restituisce il più grande tra `a` e `b`
2. Crea una funzione anonima che prende due argomenti e restituisce la loro somma
3. Crea una lista con gli elementi `a` e `b` sommati insieme
4. Genera un errore perché le funzioni lambda possono prendere solo un argomento
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `lambda a, b: a + b` crea una funzione anonima con due parametri `a` e `b` che restituisce la loro somma. Le funzioni lambda possono prendere qualsiasi numero di parametri. Questa lambda equivale a `def add(a, b): return a + b`, solo scritta più compattamente su una riga.

    **Concept Tested:** Lambda Functions

---

#### 8. Perché la ricorsione è particolarmente adatta a disegnare i frattali?

<div class="upper-alpha" markdown>
1. I frattali sono troppo grandi per entrare in un ciclo for
2. I frattali hanno una struttura autosimile — ogni parte sembra una versione più piccola del tutto — che corrisponde naturalmente alle chiamate di funzione ricorsive
3. La libreria turtle funziona solo con le funzioni ricorsive
4. I frattali richiedono esattamente 1.000 iterazioni, che è il limite di ricorsione di Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. I frattali sono autosimili — un ramo su un albero frattale sembra una versione più piccola dell'intero albero, che sembra una versione più piccola, e così via. Questo rispecchia perfettamente la struttura della ricorsione: disegna un ramo, poi chiama la stessa funzione per disegnare rami più piccoli alla punta, finché i rami non diventano troppo piccoli da vedere (il caso base).

    **Concept Tested:** Fractal Tree

---

#### 9. Cosa fa diversamente la funzione ricorsiva `countdown(n)` rispetto a un conto alla rovescia con ciclo `for`?

<div class="upper-alpha" markdown>
1. Un conto alla rovescia ricorsivo è sempre più veloce di un ciclo for
2. Un conto alla rovescia ricorsivo può gestire numeri negativi ma un ciclo for no
3. Un conto alla rovescia ricorsivo chiama sé stesso con un valore più piccolo a ogni passo, usando lo stack delle chiamate invece di un contatore di ciclo
4. Sono identici — la ricorsione e i cicli producono sempre lo stesso codice
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un conto alla rovescia ricorsivo chiama sé stesso con `n - 1` a ogni chiamata, affidandosi allo stack delle chiamate per tenere traccia di dove si trova. Un ciclo for usa una variabile contatore gestita dalla struttura del ciclo. Entrambi ottengono lo stesso risultato, ma usano meccanismi diversi. I cicli for sono spesso più efficienti e chiari per il conteggio semplice; la ricorsione risplende quando il problema ha una struttura naturalmente ricorsiva.

    **Concept Tested:** Recursion Concept

---

#### 10. Quale delle seguenti definisce correttamente una lambda che raddoppia il suo input?

<div class="upper-alpha" markdown>
1. `lambda: x * 2`
2. `def double = lambda x: x * 2`
3. `lambda x: x * 2`
4. `lambda x => x * 2`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La sintassi corretta della lambda è `lambda parametri: espressione`. `lambda x: x * 2` crea una funzione che prende un argomento `x` e restituisce `x * 2`. L'opzione A manca del parametro `x`. L'opzione B mescola la sintassi di `def` e `lambda` in modo scorretto. L'opzione D usa `=>` che non è Python valido (si usa in JavaScript).

    **Concept Tested:** Lambda Functions

---
