# Quiz: Algoritmi e Strutture Dati

Verifica la tua comprensione delle pile, delle code, dei grafi, di BFS, DFS, dell'ordinamento, della ricerca binaria, e della notazione Big-O con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa significa LIFO, e quale struttura di dati lo usa?

<div class="upper-alpha" markdown>
1. Last In, First Out — usato da una coda
2. List In, Front Out — usato da un array ordinato
3. Last In, First Out — usato da una pila
4. Least-Item-First-Out — usato da una coda con priorità
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. LIFO sta per "Last In, First Out" (ultimo entrato, primo uscito). In una pila, l'elemento aggiunto più di recente è il primo a essere rimosso — come una pila di piatti dove prendi sempre dalla cima. Le liste Python funzionano come pile usando `.append()` per fare push e `.pop()` per fare pop. Le code usano FIFO (First In, First Out).

    **Concept Tested:** Stack (LIFO)

---

#### 2. Cosa significa FIFO, e quale struttura di dati lo usa?

<div class="upper-alpha" markdown>
1. First In, First Out — usato da una coda
2. First In, First Out — usato da una pila
3. Files-In, Files-Out — usato dalle operazioni sui file
4. Fastest Item First Out — usato da una coda con priorità
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. FIFO sta per "First In, First Out" (primo entrato, primo uscito). In una coda, il primo elemento aggiunto è il primo elemento rimosso — come una fila alla mensa dove la prima persona in fila viene servita per prima. `collections.deque` di Python è il modo efficiente di implementare una coda, usando `.append()` per fare enqueue e `.popleft()` per fare dequeue.

    **Concept Tested:** Queue (FIFO)

---

#### 3. Quale struttura di dati usa BFS per decidere quale nodo visitare dopo?

<div class="upper-alpha" markdown>
1. Una pila (LIFO)
2. Una lista ordinata
3. Un insieme (per prevenire i duplicati)
4. Una coda (FIFO)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. La Ricerca in Ampiezza (BFS) usa una coda per tracciare quali nodi visitare dopo. I nodi vengono messi in coda quando vengono scoperti e tolti dalla coda in ordine FIFO — quindi BFS esplora tutti i nodi a distanza 1 prima di qualsiasi a distanza 2, garantendo il percorso più corto nei grafi non pesati. DFS, al contrario, usa una pila o la ricorsione.

    **Concept Tested:** BFS

---

#### 4. Per cosa si usa una lista di adiacenza?

<div class="upper-alpha" markdown>
1. Memorizzare efficientemente una lista ordinata di numeri
2. Rappresentare un grafo come un dizionario dove ogni chiave è un nodo e il valore è una lista dei suoi vicini
3. Tracciare quali elementi sono stati visitati in un insieme
4. Organizzare le chiavi di un dizionario in ordine alfabetico
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una lista di adiacenza rappresenta un grafo usando un dizionario: ogni chiave è un nodo (vertice) e il suo valore è una lista di nodi vicini (collegati da archi). Per esempio, `{"A": ["B", "C"], "B": ["A", "D"]}` significa che A si collega a B e C, e B si collega ad A e D. Questo è efficiente in termini di memoria per i grafi sparsi.

    **Concept Tested:** Graph and Adjacency List

---

#### 5. Qual è la differenza fondamentale tra BFS e DFS?

<div class="upper-alpha" markdown>
1. BFS usa la ricorsione; DFS usa un ciclo
2. BFS esplora livello per livello (percorso più corto prima) usando una coda; DFS esplora quanto più profondamente possibile lungo ogni ramo usando una pila o la ricorsione
3. BFS funziona solo sugli alberi; DFS funziona su qualsiasi grafo
4. BFS è sempre più veloce di DFS
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. BFS (Ricerca in Ampiezza) esplora i vicini livello per livello — prima tutti i nodi a distanza 1, poi distanza 2, garantendo il percorso più corto in un grafo non pesato. Usa una coda. DFS (Ricerca in Profondità) va quanto più lontano possibile lungo un percorso prima di tornare indietro, usando una pila o la ricorsione. DFS usa meno memoria per i grafi profondi ma non garantisce il percorso più corto.

    **Concept Tested:** BFS and DFS

---

#### 6. Cosa descrive la notazione Big-O?

<div class="upper-alpha" markdown>
1. Il numero esatto di secondi che un algoritmo impiegherà per girare
2. La quantità di memoria che un algoritmo usa in byte
3. Come crescono i requisiti di tempo o spazio di un algoritmo all'aumentare della dimensione dell'input
4. Il numero di righe di codice in un algoritmo
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La notazione Big-O descrive il tasso di crescita dei requisiti di tempo o memoria di un algoritmo all'aumentare della dimensione dell'input. Per esempio, O(n) significa che il tempo cresce linearmente — raddoppiare l'input raddoppia il tempo. O(n²) significa che il tempo cresce quadraticamente. Si concentra sul termine di crescita dominante e ignora le costanti, aiutandoti a confrontare gli algoritmi indipendentemente dalla velocità dell'hardware.

    **Concept Tested:** Big-O Notation

---

#### 7. Qual è la complessità temporale della ricerca binaria su una lista ordinata di n elementi?

<div class="upper-alpha" markdown>
1. O(n) — controlla ogni elemento
2. O(n²) — confronta ogni coppia
3. O(1) — richiede sempre lo stesso tempo
4. O(log n) — dimezza lo spazio di ricerca a ogni passo
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. La ricerca binaria funziona dimezzando ripetutamente lo spazio di ricerca. A ogni passo, controlla l'elemento centrale: se è troppo alto, elimina la metà superiore; se troppo basso, elimina la metà inferiore. Questo dà un tempo O(log n) — cercare in un milione di elementi richiede circa 20 passi (log₂(1.000.000) ≈ 20). La ricerca binaria richiede che la lista sia ordinata.

    **Concept Tested:** Binary Search

---

#### 8. Come funziona il bubble sort?

<div class="upper-alpha" markdown>
1. Scegli ripetutamente l'elemento più piccolo rimanente e lo posiziona nella sua posizione corretta
2. Divide la lista a metà, ordina ogni metà, e le fonde di nuovo insieme
3. Scorre ripetutamente la lista, confrontando gli elementi adiacenti e scambiandoli se sono nell'ordine sbagliato
4. Usa una tabella hash per contare le frequenze degli elementi e ricostruire l'ordine ordinato
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il bubble sort fa passaggi ripetuti attraverso la lista, confrontando coppie adiacenti e scambiandole se quella a sinistra è più grande di quella a destra. Dopo ogni passaggio, l'elemento non ordinato più grande è "risalito a bolla" alla sua posizione corretta. Il bubble sort è O(n²) — facile da capire ma lento per liste grandi. `sorted()` e `.sort()` built-in di Python sono molto più veloci per l'uso reale.

    **Concept Tested:** Bubble Sort

---

#### 9. Cosa deve essere vero riguardo a una lista perché la ricerca binaria funzioni?

<div class="upper-alpha" markdown>
1. La lista deve contenere solo interi
2. La lista deve avere un numero pari di elementi
3. La lista deve già essere ordinata
4. La lista non deve avere valori duplicati
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La ricerca binaria si basa sul fatto che la lista sia ordinata. Confronta l'obiettivo con l'elemento centrale e decide quale metà cercare dopo. Se la lista fosse non ordinata, eliminare metà degli elementi non sarebbe valido — l'obiettivo potrebbe essere in entrambe le metà. La ricerca binaria su una lista non ordinata produce risultati scorretti.

    **Concept Tested:** Binary Search

---

#### 10. Quale struttura di dati è più appropriata per tracciare la cronologia del browser dove il pulsante indietro ti porta alla pagina visitata più di recente?

<div class="upper-alpha" markdown>
1. Una coda (FIFO)
2. Una pila (LIFO)
3. Una lista ordinata
4. Un grafo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La cronologia del browser è un classico caso d'uso di una pila. Quando visiti una nuova pagina, viene spinta sulla pila. Quando clicchi Indietro, la pagina più recente viene tolta — Last In, First Out (LIFO). Una coda ti darebbe la pagina più vecchia prima (direzione sbagliata). Un grafo potrebbe modellare la navigazione tra le pagine, ma una pila è specificamente ciò che modella il pulsante Indietro.

    **Concept Tested:** Stack (LIFO)

---
