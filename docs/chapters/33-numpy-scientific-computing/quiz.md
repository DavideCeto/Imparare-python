# Quiz: NumPy e Calcolo Scientifico

Verifica la tua comprensione degli array NumPy, della matematica element-wise, del broadcasting, della creazione degli array, dello slicing, e delle funzioni statistiche con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è l'alias standard per importare NumPy?

<div class="upper-alpha" markdown>
1. `import numpy as num`
2. `import numpy as np`
3. `import np from numpy`
4. `from numpy import *`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La convenzione universale è `import numpy as np`. Ogni tutorial, manuale, ed esempio di codice professionale usa `np` come alias. Questo significa che scrivi `np.array()`, `np.zeros()`, ecc. Usare qualsiasi altro alias renderebbe il tuo codice più difficile da leggere per altri programmatori Python.

    **Concept Tested:** Importing NumPy

---

#### 2. Qual è il vantaggio principale di un array NumPy rispetto a una lista Python per i dati numerici?

<div class="upper-alpha" markdown>
1. Gli array NumPy possono contenere più tipi di dati delle liste
2. Gli array NumPy hanno più metodi come `.append()` e `.insert()`
3. Gli array NumPy eseguono operazioni matematiche element-wise 10-100 volte più velocemente, usando codice C ottimizzato
4. Gli array NumPy ordinano automaticamente il loro contenuto
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Gli array NumPy memorizzano tutti i valori in un blocco compatto di memoria (tutti dello stesso tipo) ed eseguono le operazioni in codice C ottimizzato. Questo li rende 10-100 volte più veloci delle liste Python per i calcoli numerici. Il vantaggio di velocità è fondamentale nella data science e nel machine learning, dove gli array possono contenere milioni di valori.

    **Concept Tested:** NumPy Arrays

---

#### 3. Dato `a = np.array([1, 2, 3, 4])`, cosa produce `a * 2`?

<div class="upper-alpha" markdown>
1. `[1, 2, 3, 4, 1, 2, 3, 4]` (l'array ripetuto due volte)
2. `[2, 4, 6, 8]` (ogni elemento moltiplicato per 2)
3. `8` (la somma di tutti gli elementi per 2)
4. Un errore perché non puoi moltiplicare un array per uno scalare
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. NumPy esegue automaticamente le operazioni element-wise. `a * 2` moltiplica ogni elemento nell'array per 2, dando `[2, 4, 6, 8]`. Questo è diverso dalle liste Python, dove `[1, 2, 3, 4] * 2` ripete la lista. La matematica element-wise è una delle caratteristiche più importanti di NumPy — senza bisogno di nessun ciclo.

    **Concept Tested:** Element-Wise Math

---

#### 4. Cos'è il broadcasting in NumPy?

<div class="upper-alpha" markdown>
1. Inviare dati di un array su una rete a più computer
2. Applicare automaticamente uno scalare (singolo numero) o un array più piccolo a ogni elemento di un array più grande
3. Stampare il contenuto di un array in una tabella formattata
4. Convertire un array in un segnale di frequenza radio
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il broadcasting è la capacità di NumPy di espandere automaticamente uno scalare o un array più piccolo per corrispondere alla forma di un array più grande durante le operazioni. Quando scrivi `a + 10`, NumPy "trasmette" il valore `10` attraverso tutti gli elementi — come se avessi creato un array di 10 della stessa dimensione di `a`. Questo elimina il bisogno di cicli espliciti.

    **Concept Tested:** Broadcasting

---

#### 5. Cosa produce `np.linspace(0, 1, 5)`?

<div class="upper-alpha" markdown>
1. Cinque valori casuali tra 0 e 1
2. `[0, 0.2, 0.4, 0.6, 0.8]` (senza includere l'estremo finale 1)
3. `[0.0, 0.25, 0.5, 0.75, 1.0]` (5 valori equispaziati da 0 a 1, inclusi)
4. Un oggetto range come il `range(0, 1, 5)` di Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `np.linspace(start, stop, num)` crea esattamente `num` valori equispaziati da `start` a `stop`, inclusi. `np.linspace(0, 1, 5)` dà `[0.0, 0.25, 0.5, 0.75, 1.0]`. Questo è particolarmente utile per generare valori x per funzioni matematiche e disegnare curve morbide, a differenza di `np.arange()` che usa una dimensione del passo.

    **Concept Tested:** np.linspace()

---

#### 6. Cosa crea `np.zeros(4)`?

<div class="upper-alpha" markdown>
1. Una lista Python di quattro zeri: `[0, 0, 0, 0]`
2. Un array NumPy di quattro zeri a virgola mobile: `array([0., 0., 0., 0.])`
3. Una matrice 4×4 di zeri
4. Un array dei quattro numeri più piccoli possibili
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `np.zeros(n)` crea un array NumPy 1-D di `n` zeri, con dtype `float64` per default. `np.ones(n)` crea un array di uni. Entrambi sono comunemente usati per inizializzare gli array prima di riempirli con valori calcolati. Per una matrice 2-D di zeri, usa `np.zeros((rows, cols))`.

    **Concept Tested:** np.zeros() and np.ones()

---

#### 7. Come trovi l'indice del valore massimo in un array NumPy `a`?

<div class="upper-alpha" markdown>
1. `a.max_index()`
2. `a.index(max(a))`
3. `np.argmax(a)`
4. `a.find_max()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `np.argmax(a)` restituisce l'indice (posizione) del valore più grande nell'array. Per esempio, se `a = np.array([3, 7, 2, 9, 1])`, allora `np.argmax(a)` restituisce `3` (l'indice dove vive `9`). `a.max()` restituisce il valore `9` stesso. `argmax` è utile quando hai bisogno di sapere DOVE si trova il massimo, non solo quale sia.

    **Concept Tested:** argmax

---

#### 8. Cosa calcola `a.mean()` per un array NumPy `a`?

<div class="upper-alpha" markdown>
1. Il valore centrale quando ordinato (la mediana)
2. Il valore che occorre più frequentemente (la moda)
3. La media (media aritmetica) di tutti i valori nell'array
4. La deviazione standard dei valori dell'array
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `a.mean()` restituisce la media aritmetica — la somma di tutti i valori divisa per il conteggio. Per `np.array([2, 4, 6, 8])`, la media è `(2+4+6+8)/4 = 5.0`. Puoi anche usare `np.mean(a)`. Per la deviazione standard (quanto sono sparsi i valori), usa `a.std()` oppure `np.std(a)`.

    **Concept Tested:** mean and std

---

#### 9. Cosa ti dice `.shape` riguardo a un array NumPy?

<div class="upper-alpha" markdown>
1. Il tipo di dato degli elementi memorizzati nell'array
2. Il numero totale di elementi attraverso tutte le dimensioni
3. Una tupla che descrive il numero di righe e colonne (o elementi in ogni dimensione)
4. Se l'array è memorizzato in ordine row-major o column-major
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'attributo `.shape` restituisce una tupla che descrive le dimensioni dell'array. Per un array 1-D di 5 elementi, `a.shape` è `(5,)`. Per un array 2-D con 3 righe e 4 colonne, `a.shape` è `(3, 4)`. Usa `.shape` per verificare che il tuo array abbia la struttura prevista prima di passarlo a una funzione.

    **Concept Tested:** Array Shape

---

#### 10. In che modo lo slicing di un array NumPy differisce dallo slicing di una lista Python?

<div class="upper-alpha" markdown>
1. Gli array NumPy non possono essere tagliati — devi usare `np.select()` invece
2. Gli slice degli array NumPy sono vedute (i cambiamenti allo slice influenzano l'originale); gli slice delle liste sono copie
3. Gli slice NumPy includono l'indice di stop; gli slice delle liste no
4. Gli array NumPy possono essere tagliati solo in una dimensione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Uno slice di un array NumPy è una **veduta** (view) — condivide la stessa memoria dell'array originale. Se modifichi lo slice, cambia anche l'array originale. Uno slice di una lista Python crea una copia indipendente. Questo comportamento a veduta è intenzionale in NumPy per l'efficienza (nessuna copia), ma può causare bug inaspettati se non ne sei consapevole. Usa `.copy()` per ottenere una copia indipendente.

    **Concept Tested:** Array Slicing

---
