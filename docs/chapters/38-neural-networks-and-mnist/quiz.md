# Quiz: Reti Neurali e MNIST

Verifica la tua comprensione delle Reti Neurali Convoluzionali, di Conv2D, MaxPooling, Dropout, Flatten, e del training dei modelli Keras con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è il vantaggio principale di una Rete Neurale Convoluzionale (CNN) rispetto a una rete densa per i dati immagine?

<div class="upper-alpha" markdown>
1. Le CNN si allenano più velocemente perché hanno meno parametri totali da aggiornare
2. Le CNN preservano la struttura spaziale 2-D delle immagini e rilevano pattern locali come bordi e angoli, indipendentemente da dove appaiono
3. Le CNN possono elaborare immagini a colori; le reti dense possono gestire solo la scala di grigi
4. Le CNN non richiedono dati di training etichettati, a differenza delle reti dense
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Le reti dense appiattiscono un'immagine in un vettore 1-D, perdendo tutte le relazioni spaziali tra i pixel. Le CNN fanno scorrere i kernel dei filtri attraverso l'immagine 2-D per rilevare pattern locali (bordi, angoli, forme). Lo stesso kernel rileva un pattern ovunque appaia — un "7" in alto a sinistra e in basso a destra vengono riconosciuti dallo stesso kernel. Questo si chiama invarianza alla traslazione.

    **Concept Tested:** CNN vs Dense Networks

---

#### 2. Cosa fa un layer `Conv2D(32, (3,3))`?

<div class="upper-alpha" markdown>
1. Crea un layer denso con 32 neuroni e 3×3 connessioni
2. Divide l'immagine in 32 blocchi ognuno di dimensione 3×3
3. Fa scorrere 32 diversi filtri kernel 3×3 attraverso l'immagine, producendo 32 mappe di caratteristiche
4. Comprime l'immagine a una risoluzione di 32×32 pixel
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `Conv2D(filters, kernel_size)` crea `filters` kernel apprendibili, ognuno di dimensione `kernel_size × kernel_size`. Ogni kernel scorre attraverso l'intero input e produce una mappa di caratteristiche. `Conv2D(32, (3,3))` produce 32 mappe di caratteristiche — ognuna rilevando un pattern visivo diverso (bordi orizzontali, curve, angoli, ecc.).

    **Concept Tested:** Conv2D Layer

---

#### 3. Cosa fa `MaxPooling2D((2,2))` a una mappa di caratteristiche?

<div class="upper-alpha" markdown>
1. Applica un filtro di convoluzione 2×2 per trovare i bordi
2. Raddoppia la larghezza e l'altezza della mappa di caratteristiche per una risoluzione più alta
3. Divide la mappa di caratteristiche in blocchi 2×2 e mantiene solo il valore massimo in ogni blocco, dimezzando larghezza e altezza
4. Fa la media dei valori in ogni blocco 2×2 invece di prendere il massimo
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. MaxPooling divide la mappa di caratteristiche in blocchi non sovrapposti della dimensione data e mantiene il valore massimo di ogni blocco. `MaxPooling2D((2,2))` su una mappa di caratteristiche 24×24 produce una mappa di caratteristiche 12×12. Questo riduce il costo computazionale e crea un certo grado di invarianza di posizione — piccoli spostamenti nell'input producono lo stesso output di pooling.

    **Concept Tested:** MaxPooling2D

---

#### 4. Cosa fa il layer `Flatten()` in una CNN?

<div class="upper-alpha" markdown>
1. Normalizza tutti i valori dei pixel per essere tra 0 e 1
2. Converte le mappe di caratteristiche 2-D dai layer convoluzionali in un singolo vettore 1-D per i layer densi
3. Appiattisce il learning rate a un valore costante durante il training
4. Rimuove tutti i valori zero dalle mappe di caratteristiche per ridurre la memoria
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Dopo i layer convoluzionali e di pooling, i dati sono ancora 2-D (o a dimensionalità più alta). I layer densi richiedono input 1-D. `Flatten()` riforma il tensore multidimensionale in un vettore 1-D senza cambiare nessun valore. Per esempio, un output 5×5×64 diventa un vettore di lunghezza 5×5×64 = 1.600 valori.

    **Concept Tested:** Flatten Layer

---

#### 5. Cosa fa `Dropout(0.5)` durante il training?

<div class="upper-alpha" markdown>
1. Scarta il 50% degli esempi di training ogni epoch per velocizzare il training
2. Imposta casualmente a zero il 50% degli output dei neuroni durante ogni passo di training, forzando la rete a imparare rappresentazioni ridondanti e riducendo l'overfitting
3. Riduce il learning rate del 50% dopo ogni epoch
4. Mantiene solo il 50% superiore dei neuroni per grandezza del peso
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Dropout silenzia casualmente (imposta a zero) una frazione di neuroni durante ogni passo di training. Con `Dropout(0.5)`, il 50% dei neuroni viene disabilitato casualmente ogni volta. Questo impedisce alla rete di fare troppo affidamento su un singolo neurone, forzandola a sviluppare più percorsi indipendenti per rilevare ogni caratteristica. Al momento della previsione, Dropout viene automaticamente disabilitato e tutti i neuroni sono attivi.

    **Concept Tested:** Dropout

---

#### 6. Cosa configura `model.compile()`?

<div class="upper-alpha" markdown>
1. Il numero di layer e neuroni nel modello
2. L'optimizer (come si aggiornano i pesi), la funzione di loss (cosa minimizzare), e le metriche da tracciare
3. L'hardware (CPU vs GPU) che verrà usato per il training
4. La forma di input e output che il modello si aspetta
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `model.compile()` imposta tre scelte chiave di training prima che tu possa chiamare `model.fit()`: (1) l'optimizer — come il modello aggiorna i pesi (ad es., `"adam"`, `"sgd"`); (2) la funzione di loss — quale misura di errore minimizzare; e (3) le metriche da monitorare ma non ottimizzare (ad es., `"accuracy"`). Devi compilare prima di allenare.

    **Concept Tested:** model.compile()

---

#### 7. Cosa fa `model.fit()`?

<div class="upper-alpha" markdown>
1. Controlla se l'architettura del modello corrisponde alla forma dei dati di input
2. Predice le etichette per dati nuovi e non visti
3. Allena il modello eseguendo l'optimizer per minimizzare la loss sui dati di training per un dato numero di epoch
4. Salva i pesi del modello allenato in un file
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `model.fit(x_train, y_train, epochs=10)` esegue il ciclo di training: per ogni epoch, passa tutti gli esempi di training attraverso il modello, calcola la loss, ed esegue l'optimizer per aggiornare i pesi. Restituisce un oggetto history contenente la loss e le metriche per ogni epoch. Usa `validation_split=0.1` per monitorare l'accuratezza di validation durante il training.

    **Concept Tested:** model.fit()

---

#### 8. Cosa controlla il parametro batch_size in `model.fit()`?

<div class="upper-alpha" markdown>
1. Il numero totale di esempi di training da usare per il training
2. Il numero di esempi di training elaborati insieme prima che il modello aggiorni i suoi pesi
3. Il numero di layer da allenare in parallelo
4. La dimensione in pixel delle immagini che il modello può accettare
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `batch_size` determina quanti esempi di training vengono raggruppati insieme per ogni aggiornamento dei pesi. Una dimensione del batch di 64 significa che il modello elabora 64 esempi, calcola la loss media, poi aggiorna i pesi una volta. Batch più piccoli danno aggiornamenti più rumorosi ma più frequenti; batch più grandi danno aggiornamenti più fluidi ma meno frequenti. Valori comuni sono 32, 64, e 128.

    **Concept Tested:** Training with model.fit()

---

#### 9. Cos'è l'invarianza alla traslazione nelle CNN?

<div class="upper-alpha" markdown>
1. La capacità di tradurre (spostare) le previsioni di output in lingue diverse
2. Un kernel imparato nel set di training che non funziona sul set di test
3. La proprietà per cui lo stesso rilevatore di caratteristiche (kernel) può riconoscere un pattern indipendentemente da dove appare nell'immagine
4. Convertire le coordinate dei pixel da un sistema di coordinate a un altro
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'invarianza alla traslazione significa che una CNN può riconoscere una caratteristica — come la curva in cima a un "6" — che appaia in alto a sinistra o in basso a destra dell'immagine. Questo perché lo stesso kernel imparato viene condiviso e scansionato attraverso l'intera immagine. Le reti dense non hanno questa proprietà: ogni posizione nell'immagine ha pesi indipendenti, quindi la rete deve imparare separatamente ogni posizione.

    **Concept Tested:** CNN Properties

---

#### 10. Per cosa si usano le RNN (Reti Neurali Ricorrenti)?

<div class="upper-alpha" markdown>
1. Elaborare dati strutturati a griglia come le immagini con filtri locali
2. Dati sequenziali dove l'ordine conta — come testo, voce, serie temporali, e prezzi delle azioni
3. Generare immagini da descrizioni testuali
4. Raggruppare automaticamente dati non etichettati in gruppi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Le Reti Neurali Ricorrenti (RNN) elaborano sequenze dove l'ordine conta. A differenza dei layer densi o CNN, le RNN mantengono uno stato nascosto — una "memoria" che porta informazioni dall'inizio della sequenza ai passi successivi. Questo le rende adatte all'elaborazione del linguaggio naturale, al riconoscimento vocale, alla previsione delle serie temporali, e alla generazione musicale. Le LSTM (Long Short-Term Memory) sono una versione migliorata delle RNN che gestiscono sequenze più lunghe.

    **Concept Tested:** RNNs and LSTMs

---
