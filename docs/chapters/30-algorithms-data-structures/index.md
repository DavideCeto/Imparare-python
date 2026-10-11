---
title: Algoritmi e Strutture Dati
description: Esplora le pile, le code, i grafi, BFS, DFS, gli algoritmi di ordinamento, la ricerca binaria, e l'analisi della complessità Big-O
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:00:00
version: 0.09
---

# Algoritmi e Strutture Dati

Alla fine di questa lezione sarai in grado di:

- Spiegare e implementare una **pila** (LIFO) e una **coda** (FIFO)
- Rappresentare un **grafo** come una lista di adiacenza e attraversarlo con **BFS** e **DFS**
- Implementare il **bubble sort**, il **selection sort**, e la **ricerca binaria**
- Descrivere la notazione Big-O e spiegare la complessità temporale delle operazioni comuni

Questo capitolo introduce le basi dell'informatica che alimentano tutto, dai motori di ricerca all'IA dei giochi.

!!! mascot-welcome "Benvenuto/a al Capitolo 30!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le strutture dati e gli algoritmi sono il cuore dell'informatica.
    Ogni ricerca, ogni raccomandazione, ogni app di pianificazione del percorso usa le idee di questo capitolo.
    Sblocchiamole! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Tipi di Dati Abstract

Un **Tipo di Dato Abstract (ADT)** descrive *cosa* fa una struttura di dati, non *come* lo fa internamente.
Una pila, una coda, e un grafo sono ADT — ognuno definisce operazioni come push, pop, enqueue, e dequeue.

## Pile — LIFO

Una **pila** (stack) è una collezione Last In, First Out (LIFO) — ultimo entrato, primo uscito.
Pensa a una pila di piatti — puoi solo aggiungere o rimuovere dalla cima.

Due operazioni:
- **Push** — aggiungi in cima
- **Pop** — rimuovi dalla cima

Le liste Python funzionano perfettamente come pile:

```python
stack = []
stack.append("first")    # push
stack.append("second")   # push
stack.append("third")    # push
print(stack.pop())       # "third" — last in, first out
print(stack.pop())       # "second"
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto usa una pila per invertire una stringa.
    Dopo aver spinto tutti i caratteri e averli tolti, in quale ordine appariranno?
    Fai la tua previsione — poi eseguilo!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)   # push each character
    result = ""
    while stack:
        result += stack.pop()   # pop in reverse order
    return result

print(reverse_string("Hello"))
print(reverse_string("Python"))`);
</script>

## Code — FIFO

Una **coda** (queue) è una collezione First In, First Out (FIFO) — primo entrato, primo uscito.
Pensa a una fila alla mensa — la prima persona in fila è la prima a essere servita.

Due operazioni:
- **Enqueue** — aggiungi in fondo
- **Dequeue** — rimuovi dal fronte

`collections.deque` di Python è più efficiente di una lista per le code:

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `from collections import deque

queue = deque()
queue.append("Alice")    # enqueue
queue.append("Bob")
queue.append("Carol")

print("Queue:", list(queue))
print("Served:", queue.popleft())   # dequeue — FIFO
print("Served:", queue.popleft())
print("Remaining:", list(queue))`);
</script>

## Grafi — Nodi e Archi

Un **grafo** è un insieme di **nodi** (chiamati anche vertici) collegati da **archi**.
I grafi modellano le reti sociali, le mappe stradali, internet, e molti altri sistemi del mondo reale.

Una **lista di adiacenza** rappresenta un grafo come un dizionario dove ogni chiave è un nodo e il valore è una lista dei suoi vicini.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}
```

## Ricerca in Ampiezza (BFS)

**BFS** (Breadth-First Search) esplora un grafo livello per livello — prima tutti i nodi a distanza 1, poi distanza 2, e così via.
Usa una **coda** per tenere traccia di quale nodo visitare dopo.

BFS trova il **percorso più corto** in un grafo non pesato.

Prima del codice, i passi chiave sono:
1. Inizia dal nodo sorgente; segnalo come visitato; metti in coda
2. Mentre la coda non è vuota: togli dalla coda un nodo, elaboralo, metti in coda tutti i vicini non visitati

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def bfs(graph, start):
    visited = set()
    queue   = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

print("BFS from A:", bfs(graph, "A"))`);
</script>

## Ricerca in Profondità (DFS)

**DFS** (Depth-First Search) esplora quanto più lontano possibile lungo ogni ramo prima di tornare indietro.
Usa una **pila** (o la ricorsione) per tenere traccia del percorso.

DFS non garantisce il percorso più corto, ma usa meno memoria di BFS per grafi profondi.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result += dfs(graph, neighbor, visited)
    return result

print("DFS from A:", dfs(graph, "A"))
print("BFS is level-by-level; DFS goes deep before backtracking.")`);
</script>

| | BFS | DFS |
|--|-----|-----|
| Struttura di dati | Coda | Pila / ricorsione |
| Percorso più corto? | Sì (non pesato) | Non garantito |
| Memoria | Più (memorizza l'intero fronte) | Meno (memorizza un percorso) |
| Migliore per | Percorso più corto, reti sociali | Esplorare tutti i percorsi, cicli |

### Guardalo: La Coda e la Pila Guidano Tutto

L'unica differenza tra BFS e DFS è la riga nella prima linea di quella tabella — quale nodo in attesa viene visitato dopo. L'esploratore sotto mostra la coda o la pila **dal vivo** accanto al grafo mentre procedi passo passo. Prima di cliccare, prevedi: **partendo da A, quale nodo visita BFS come terzo? DFS è d'accordo?**

<iframe src="../../sims/graph-traversal-explorer/main.html" height="537" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Graph Traversal Explorer](../../sims/graph-traversal-explorer/index.md){ .md-button }

Procedi passo passo attraverso BFS fino alla fine e guarda l'onda muoversi livello per livello — poi l'ultimo passo rivela il premio: seguire i genitori all'indietro dà il **percorso più corto** da A all'obiettivo. Passa a DFS e procedi di nuovo: stesso grafo, stesso inizio, ordine completamente diverso, perché la pila prende sempre la scoperta *più recente*.

## Applicare BFS: Trovare un Percorso Attraverso un Labirinto

Un labirinto è solo un grafo — gli incroci e le stanze sono nodi, i corridoi sono archi. La coda di BFS esplora già livello per livello, il che significa che può trovare il **percorso più corto**, non solo rispondere "posso arrivare lì?" Il trucco è ricordare **da dove sei venuto** a ogni passo, così puoi ripercorrere la tua strada una volta raggiunto l'obiettivo.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il labirinto sotto ha due possibili percorsi da "Start" a "Goal".
    Attraverso quali stanze pensi che passerà il percorso — "A"/"C" oppure "B"/"D"? Fai la tua previsione — poi eseguilo!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-7"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-7')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-7')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-7"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-7"></div>
  </div>
</div>
<script>
initCmLab('-7', `from collections import deque

maze = {
    "Start": ["A", "B"],
    "A": ["Start", "C"],
    "B": ["Start", "D"],
    "C": ["A", "Goal"],
    "D": ["B", "Goal"],
    "Goal": ["C", "D"]
}

def find_path(maze, start, goal):
    came_from = {start: None}   # remembers which room led to each room
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for neighbor in maze[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    # Walk backwards from the goal to the start using came_from
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

print("Path found:", find_path(maze, "Start", "Goal"))`);
</script>

Avevi indovinato? BFS scopre "A" e "B" nello stesso momento, ma "A" è elencato per primo in `maze["Start"]`, quindi viene scoperto per primo — il percorso passa attraverso "A" e "C".

DFS potrebbe risolvere lo stesso labirinto seguendo un corridoio fino alla fine prima di tornare indietro, ma come mostra la tabella sopra, non garantirebbe il percorso più corto.

## Algoritmi di Ordinamento

### Bubble Sort

Il **bubble sort** confronta gli elementi adiacenti e li scambia se sono nell'ordine sbagliato.
Ogni passaggio "fa risalire a bolla" l'elemento più grande non ordinato alla sua posizione corretta.
Complessità temporale: O(n²) — lento per liste grandi.

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
```

### Selection Sort

Il **selection sort** trova l'elemento più piccolo e lo sposta in avanti, poi ripete per gli elementi rimanenti.
Anche questo è O(n²) ma fa meno scambi del bubble sort.

### Insertion Sort

L'**insertion sort** costruisce la lista ordinata un elemento alla volta — come ordinare le carte da gioco in mano.
Caso peggiore O(n²) ma O(n) per liste quasi ordinate, rendendolo veloce in pratica per input piccoli o quasi ordinati.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-5"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-5')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-5')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-5"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-5"></div>
  </div>
</div>
<script>
initCmLab('-5', `def bubble_sort(lst):
    lst = lst[:]   # work on a copy
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

data = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted:", data)
print("Bubble:  ", bubble_sort(data))
print("Insertion:", insertion_sort(data))
print("Built-in:", sorted(data))`);
</script>

### Guardalo: Ordinamento al Rallentatore

Il codice sopra mostra *cosa* calcola ogni ordinamento; il comparatore sotto mostra *come si muovono*. Ogni ordinamento è solo confronti e scambi in una coreografia diversa. Prima di cliccare Step, prevedi: **per 10 valori invertiti, approssimativamente quanti confronti avrà bisogno il bubble sort?**

<iframe src="../../sims/sorting-comparer/main.html" height="542" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Sorting Algorithm Comparer](../../sims/sorting-comparer/index.md){ .md-button }

Procedi passo passo attraverso ogni algoritmo e guarda la sua mossa caratteristica: i valori grandi del bubble sort fluttuano a destra, il selection sort cerca il minimo, l'insertion sort fa scorrere ogni nuovo valore al suo posto. Poi scegli **Race — Bubble vs Insertion**, cambia i dati in **nearly sorted**, e Auto-play: l'insertion sort demolisce il bubble sort — la risposta a "quale ordinamento è il migliore?" è sempre *dipende dai dati*.

## Ricerca Binaria

La **ricerca binaria** trova un elemento in una lista *ordinata* in tempo O(log n) — molto più veloce della ricerca lineare.

L'idea: taglia ripetutamente a metà l'intervallo di ricerca.
1. Guarda l'elemento centrale
2. Se corrisponde — fatto!
3. Se l'obiettivo è più piccolo — cerca nella metà sinistra
4. Se l'obiettivo è più grande — cerca nella metà destra

```python
def binary_search(sorted_list, target):
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1   # not found
```

### Guardalo: Lineare vs Binaria, Testa a Testa

La gara sotto esegue entrambe le ricerche sullo stesso scaffale di 31 scatole. Prima di cliccare Step, prevedi: **quanti controlli avrà bisogno ciascuna ricerca per trovare 24?** (La lineare parte da sinistra; la binaria parte dal centro.)

<iframe src="../../sims/search-race/main.html" height="522" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Search Race](../../sims/search-race/index.md){ .md-button }

Guarda la ricerca binaria scartare metà dello scaffale a ogni controllo: 31 → 15 → 7 → 3 → 1. Poi passa allo **shuffled shelf (trap!)** e cerca di nuovo — la ricerca binaria può segnalare NOT FOUND anche quando l'obiettivo è proprio lì. Tagliare il problema a metà funziona solo quando lo scaffale è ordinato, che è esattamente il motivo per cui la funzione sopra si chiama `binary_search(sorted_list, ...)`.

## Notazione Big-O — Complessità Temporale e Spaziale

La **notazione Big-O** descrive come cresce il tempo di esecuzione di un algoritmo con la dimensione dell'input.

| Big-O | Nome | Esempio |
|-------|------|---------|
| O(1) | Costante | Ricerca in un dizionario |
| O(log n) | Logaritmica | Ricerca binaria |
| O(n) | Lineare | Ricerca lineare, ciclo singolo |
| O(n log n) | Log-lineare | `sorted()` built-in di Python |
| O(n²) | Quadratica | Bubble sort, cicli annidati |
| O(2ⁿ) | Esponenziale | Enumerazione di sottoinsiemi a forza bruta |

La **complessità spaziale** descrive quanta memoria usa un algoritmo.
BFS usa O(n) memoria perché la coda può crescere fino a contenere tutti i nodi.
DFS usa O(profondità) memoria — solo il percorso attuale.

!!! mascot-tip "Perché Big-O È Importante"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Con 1.000 elementi: O(n²) = 1.000.000 operazioni; O(n log n) = ~10.000.
    Questo è 100× più veloce! Per 1.000.000 di elementi, il divario diventa 1.000.000× più veloce.
    Scegliere l'algoritmo giusto è spesso più importante che comprare hardware più veloce.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Implementa la Ricerca Binaria"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto chiama `binary_search` ma il corpo della funzione manca!
    Implementalo usando l'algoritmo descritto sopra — taglia a metà ripetutamente l'intervallo di ricerca.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-6"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-6')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-6')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-6"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-6"></div>
  </div>
</div>
<script>
initCmLab('-6', `def binary_search(sorted_list, target):
    lo, hi = 0, len(sorted_list) - 1
    # Implement: while lo <= hi, check middle, adjust lo or hi
    # Return the index if found, -1 if not found
    return -1   # placeholder — replace with your implementation

data = sorted([34, 7, 23, 32, 5, 62, 12, 77])
print("Sorted data:", data)
print("Find 23:", binary_search(data, 23))
print("Find 99:", binary_search(data, 99))`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Modifica la funzione BFS per restituire anche la **distanza** (numero di salti) dall'inizio a ogni nodo.
   **Saprai che ha funzionato quando** ogni nodo è accoppiato con la sua distanza da "A".

2. Aggiungi un nuovo nodo "G" al grafo collegato a "D". Esegui di nuovo BFS e controlla che G appaia.
   **Saprai che ha funzionato quando** "G" è incluso nell'output di BFS.

3. Confronta BFS e DFS partendo da "C" invece di "A". Nota come differiscono gli ordini di visita.
   **Saprai che ha funzionato quando** entrambi partono da "C" ed esplorano con pattern chiaramente diversi.

4. Implementa il selection sort: trova il minimo nella porzione non ordinata e scambialo in avanti.
   **Saprai che ha funzionato quando** `selection_sort([5, 3, 8, 1])` restituisce `[1, 3, 5, 8]`.

5. Testa la ricerca binaria su una lista di 1.000.000 di elementi. Di quanti confronti ha bisogno?
   Aggiungi un contatore dentro il ciclo e stampalo.
   **Saprai che ha funzionato quando** vedi che richiede al massimo 20 confronti — O(log 1.000.000) ≈ 20!

!!! mascot-celebration "Informatico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato le strutture dati e gli algoritmi — le basi di tutto il software efficiente!
    Pile, code, grafi, BFS, DFS, ordinamento, e Big-O sono gli strumenti a cui pensano ogni giorno gli sviluppatori professionisti.
    Ora stai pensando come un informatico. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
