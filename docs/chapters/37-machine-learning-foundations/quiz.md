# Quiz: Fondamenti di Machine Learning

Verifica la tua comprensione dell'apprendimento supervisionato vs non supervisionato, delle divisioni dei dati, dell'overfitting, dei componenti delle reti neurali, e del dataset MNIST con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è la differenza fondamentale tra l'apprendimento supervisionato e non supervisionato?

<div class="upper-alpha" markdown>
1. L'apprendimento supervisionato richiede che un umano osservi il training; quello non supervisionato gira automaticamente
2. L'apprendimento supervisionato si allena su esempi etichettati (input con risposte corrette conosciute); quello non supervisionato trova pattern nei dati non etichettati
3. L'apprendimento supervisionato è più veloce; quello non supervisionato è più accurato
4. L'apprendimento supervisionato usa Python; quello non supervisionato usa un linguaggio diverso
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Nell'apprendimento supervisionato, ogni esempio di training viene con un'etichetta — la risposta corretta. Il modello impara a mappare gli input agli output (ad es., foto → "dog"). Nell'apprendimento non supervisionato, non ci sono etichette — l'algoritmo scopre una struttura nascosta da solo, come raggruppare i clienti per pattern di acquisto (clustering).

    **Concept Tested:** Supervised vs Unsupervised Learning

---

#### 2. Qual è lo scopo del validation set nel machine learning?

<div class="upper-alpha" markdown>
1. Fornire dati di training extra quando il set di training è troppo piccolo
2. Controllare le prestazioni del modello durante il training e rilevare l'overfitting prima del test finale
3. Validare che il codice giri senza errori prima che inizi il training
4. Memorizzare i pesi finali del modello dopo che il training è completo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il validation set viene usato per monitorare le prestazioni durante il training. Dopo ogni epoch, valuti sul validation set (su cui il modello non si è mai allenato) per rilevare l'overfitting: se l'accuratezza di training continua a salire ma quella di validation si stabilizza o scende, il modello sta memorizzando invece di imparare. Il test set viene tenuto da parte fino alla fine.

    **Concept Tested:** Train/Validation/Test Splits

---

#### 3. Cos'è l'overfitting nel machine learning?

<div class="upper-alpha" markdown>
1. Allenare un modello per troppi epoch, facendolo girare lentamente
2. Usare troppi dati per il training, lasciandone troppo pochi per il test
3. Un modello che memorizza i dati di training invece di imparare il pattern sottostante, comportandosi bene sul training ma male su nuovi dati non visti
4. Un modello che è troppo semplice per catturare i pattern nei dati
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'overfitting è come uno studente che memorizza le risposte dell'esame dell'anno scorso ma non capisce la materia — va benissimo sul vecchio test ma fallisce sulle nuove domande. Segnali di overfitting: l'accuratezza di training è molto alta (95%+) ma quella di validation è molto più bassa (65%). Il modello ha imparato il rumore nei dati di training invece del pattern generale.

    **Concept Tested:** Overfitting

---

#### 4. Cos'è il dataset MNIST?

<div class="upper-alpha" markdown>
1. Un dataset di 70.000 immagini in scala di grigi di cifre scritte a mano (0-9), ognuna di 28x28 pixel, usato come benchmark per la classificazione delle immagini
2. Una collezione di 1 milione di frasi in inglese usate per allenare i modelli linguistici
3. Un dataset di immagini medicali per allenare i modelli di rilevamento del cancro
4. Un dataset benchmark di prezzi del mercato azionario per allenare i modelli finanziari
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. MNIST contiene 70.000 immagini di cifre scritte a mano in scala di grigi: 60.000 per il training e 10.000 per il test. Ogni immagine è di 28x28 pixel (784 numeri da 0-255). È il "Hello, World!" del machine learning — un dataset ben compreso e gestibile che è perfetto per imparare e fare benchmark delle nuove tecniche.

    **Concept Tested:** MNIST Dataset

---

#### 5. Cosa significa un epoch nel training di una rete neurale?

<div class="upper-alpha" markdown>
1. Un singolo esempio di training mostrato al modello
2. Un passaggio completo attraverso tutti i dati di training
3. Un singolo aggiustamento dei pesi del modello
4. Un singolo layer di neuroni nella rete
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un epoch è un passaggio completo attraverso l'intero dataset di training. Se hai 60.000 esempi di training e ti alleni per 10 epoch, il modello vede ogni esempio di training 10 volte (in ordini diversi). Più epoch permettono al modello di affinare progressivamente i suoi pesi e migliorare l'accuratezza, anche se troppi epoch possono portare all'overfitting.

    **Concept Tested:** Epoch

---

#### 6. Cosa misura la funzione di loss nel machine learning?

<div class="upper-alpha" markdown>
1. La velocità del processo di training in secondi per epoch
2. Quanto sono sbagliate le previsioni del modello — il valore che il training cerca di minimizzare
3. Il numero di parametri (pesi) nel modello
4. La quantità di memoria che il modello usa durante l'inferenza
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La funzione di loss quantifica quanto sono sbagliate le previsioni del modello rispetto alle etichette corrette. Il training è il processo di aggiustare i pesi del modello per minimizzare la loss. Funzioni di loss comuni includono la cross-entropy (per la classificazione) e l'errore quadratico medio (per la regressione). Una loss più bassa significa previsioni più accurate.

    **Concept Tested:** Loss Function

---

#### 7. Cosa fa la funzione di attivazione ReLU?

<div class="upper-alpha" markdown>
1. Normalizza tutti gli output per essere tra 0 e 1
2. Converte gli output in probabilità che sommano a 1.0
3. Produce 0 per gli input negativi e restituisce l'input invariato per gli input positivi: `max(0, x)`
4. Moltiplica gli input per un peso casuale per introdurre casualità
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. ReLU (Rectified Linear Unit) è definita come `f(x) = max(0, x)`. Per qualsiasi input negativo, ReLU produce 0. Per qualsiasi input positivo, ReLU lo lascia passare invariato. ReLU viene usata nei layer nascosti perché introduce la non-linearità in modo efficiente, permettendo alla rete di imparare pattern complessi. Senza funzioni di attivazione, impilare i layer non sarebbe più potente di un singolo layer.

    **Concept Tested:** ReLU Activation

---

#### 8. Cosa fa la funzione di attivazione softmax?

<div class="upper-alpha" markdown>
1. Filtra il rumore dai dati di input prima del training
2. Converte un vettore di punteggi grezzi in probabilità che sommano a 1.0
3. Disabilita casualmente alcuni neuroni per prevenire l'overfitting
4. Riduce automaticamente il learning rate durante il training
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Softmax converte un vettore di numeri grezzi (chiamati logits) in probabilità che sommano esattamente a 1.0. Per un classificatore di cifre a 10 classi, potrebbe produrre `[0.02, 0.85, 0.01, ..., 0.05]`, che significa "85% sicuro che sia la cifra 1." Softmax viene usata nel layer di output finale delle reti di classificazione multi-classe.

    **Concept Tested:** Softmax Activation

---

#### 9. Qual è una regola fondamentale riguardo al test set?

<div class="upper-alpha" markdown>
1. Il test set dovrebbe essere più grande del set di training per risultati affidabili
2. Il test set non deve mai essere usato durante il training o la selezione del modello — solo per una singola valutazione finale
3. Il test set dovrebbe essere revisionato prima del training per capire il livello di difficoltà previsto
4. Lo stesso test set dovrebbe essere riutilizzato tra più progetti per consistenza
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il test set deve essere trattato come dati completamente non visti. Se usi i risultati del test per aggiustare il tuo modello e riallenarlo, stai "barando" — il modello sembra generalizzare meglio di quanto effettivamente faccia. Il test set dovrebbe essere usato esattamente una volta, alla fine, per riportare le prestazioni reali del tuo modello. Usa il validation set per tutte le decisioni di ottimizzazione.

    **Concept Tested:** Train/Validation/Test Splits

---

#### 10. Cos'è un dense layer in una rete neurale?

<div class="upper-alpha" markdown>
1. Un layer che usa pesi molto piccoli per comprimere le informazioni
2. Un layer specifico per elaborare dati di immagine in un pattern a griglia
3. Un layer completamente connesso dove ogni neurone si connette a ogni neurone del layer precedente
4. Un layer che è attivo solo durante il training e disabilitato durante la previsione
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un dense layer (completamente connesso) connette ogni neurone nel layer attuale a ogni neurone nel layer precedente. Questo è il tipo di layer più comune nelle reti neurali di base. Ogni connessione ha un peso apprendibile. Per un layer con 100 neuroni connesso a un layer precedente di 784 input, ci sono 100 × 784 = 78.400 parametri di peso solo in quel layer.

    **Concept Tested:** Neural Network Layers

---
