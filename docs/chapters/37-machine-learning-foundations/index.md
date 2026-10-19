---
title: Fondamenti di Machine Learning
description: Capisci l'apprendimento supervisionato vs non supervisionato, le divisioni train/val/test, l'overfitting, e costruisci una prima rete neurale con Keras sul dataset MNIST
generated_by: claude skill chapter-content-generator
date: 2026-06-28 16:10:00
version: 0.09
---

# Fondamenti di Machine Learning

Alla fine di questa lezione sarai in grado di:

- Spiegare la differenza tra apprendimento **supervisionato** e **non supervisionato**
- Descrivere le divisioni **training, validation, e test** e perché tutte e tre contano
- Definire l'**overfitting** e spiegare come rilevarlo
- Capire i componenti di base di una **rete neurale**: layer, attivazioni, funzioni di loss, e optimizer
- Leggere e capire un semplice modello Keras per classificare cifre scritte a mano

Il machine learning (ML) è un modo di insegnare ai computer a riconoscere i pattern mostrando loro esempi — invece di scrivere regole a mano. Alimenta il riconoscimento delle immagini, i filtri antispam, i motori di raccomandazione, e i grandi modelli linguistici.

!!! mascot-welcome "Benvenuto/a al Capitolo 37!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il machine learning è una delle aree più eccitanti dell'informatica — e con Python, è sorprendentemente accessibile!
    Questo capitolo ti dà il vocabolario e i concetti di cui hai bisogno per capire e costruire veri sistemi di ML.
    Esploriamo! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Cos'è il Machine Learning?

Programmazione tradizionale: **scrivi tu le regole**.
```
Input: image of a dog
Rules: if has fur AND four legs AND tail → output "dog"
```

Machine learning: **mostri esempi, il computer impara le regole**.
```
Training data: 50,000 labeled images (dog / cat / bird)
ML algorithm: finds patterns in pixels that distinguish each class
Result: model that predicts the class of new, unseen images
```

L'"apprendimento" succede durante il **training** — un processo di aggiustamento ripetuto dei numeri interni del modello (chiamati **parametri** o **pesi**, weights) per ridurre gli errori.

## Apprendimento Supervisionato vs Non Supervisionato

L'**apprendimento supervisionato** si allena su esempi etichettati — ogni input viene con la risposta corretta.

- Input: foto di un "3" scritto a mano
- Etichetta: la cifra 3
- Obiettivo: imparare a predire la cifra corretta per qualsiasi nuova foto

Esempi: classificazione delle immagini, rilevamento dello spam, diagnosi medica, previsione dei prezzi

L'**apprendimento non supervisionato** trova pattern nei dati senza etichette.

- Input: 10.000 registri di acquisto dei clienti (nessuna categoria)
- Obiettivo: scoprire raggruppamenti naturali (cluster) nei dati

Esempi: segmentazione dei clienti, rilevamento di anomalie, modellazione di argomenti, compressione dei dati

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto simula un "classificatore" molto semplice che predice pass/fail da un punteggio del test.
    Prima di eseguirlo — quale soglia pensi che darà la migliore accuratezza sul set di test?
    Fai la tua previsione, poi eseguilo!

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
initCmLab('', `def simple_classifier(score, threshold):
    return "pass" if score >= threshold else "fail"

def evaluate(data, labels, threshold):
    correct = 0
    for score, label in zip(data, labels):
        if simple_classifier(score, threshold) == label:
            correct += 1
    return correct / len(data)

# Dati di addestramento (punteggi ed esiti reali):
scores = [45, 62, 78, 55, 90, 38, 71, 85, 50, 93]
labels = ["fail", "pass", "pass", "fail", "pass",
          "fail", "pass", "pass", "fail", "pass"]

for threshold in [50, 60, 65, 70, 80]:
    acc = evaluate(scores, labels, threshold)
    print(f"Soglia {threshold}: accuratezza = {acc:.0%}")`);
</script>

## Il Dataset MNIST

**MNIST** (Modified National Institute of Standards and Technology) è il "Hello, World!" del machine learning.
Contiene 70.000 immagini in scala di grigi di cifre scritte a mano (0–9), ognuna di 28×28 pixel.

- 60.000 immagini di training
- 10.000 immagini di test

Ogni pixel è un numero da 0 (nero) a 255 (bianco).
Un'immagine 28×28 è una griglia di 784 numeri — questo diventa un vettore di 784 input per una rete neurale.

## Divisioni Train / Validation / Test

Prima di allenare un modello, dividi i tuoi dati in tre insiemi separati:

| Insieme | Scopo | Dimensione tipica |
|-----|---------|-------------|
| **Training** | Il modello impara da questi esempi | 70–80% |
| **Validation** | Controlla le prestazioni durante il training; ottimizza le impostazioni | 10–15% |
| **Test** | Valutazione finale su dati non visti — usata UNA SOLA VOLTA | 10–15% |

**Perché tre insiemi?**

- Il modello non si allena mai sui dati di test — quindi l'accuratezza del test è una misura onesta delle prestazioni nel mondo reale
- Il validation ti aiuta a catturare l'overfitting *prima* che tu tocchi il set di test

**Una regola fondamentale:** Non guardare mai il tuo set di test finché non hai completamente finito con tutta l'ottimizzazione del modello. Sbirciare e riottimizzare in base ai risultati del test è "barare" — il tuo modello sembrerà generalizzare meglio di quanto effettivamente faccia.

## Overfitting

L'**overfitting** succede quando un modello memorizza i dati di training invece di imparare il pattern sottostante.
Si comporta molto bene sui dati di training ma male su nuovi esempi non visti.

Pensa a uno studente che memorizza esattamente ogni domanda dell'esame dell'anno scorso, senza capire la materia. Andrà benissimo sul vecchio test ma fallirà sulle nuove domande.

Segnali di overfitting:
- Accuratezza di training: 99%
- Accuratezza di validation: 65%
- Grande divario tra i due numeri

Correzioni per l'overfitting:
- Più dati di training
- **Dropout** — disabilita casualmente alcuni neuroni durante il training (trattato nel Capitolo 38)
- Modello più semplice (meno layer, layer più piccoli)
- **Regularization** (regolarizzazione) — penalità per pesi grandi

## Reti Neurali — Vocabolario Chiave

Prima di leggere il codice Keras, ecco i termini chiave:

- **Neurone** — una singola unità di calcolo che prende input, li moltiplica per i pesi, aggiunge un bias, e applica una funzione di attivazione
- **Layer** — un gruppo di neuroni che ricevono tutti gli stessi input e producono output insieme
- **Dense layer** — ogni neurone si connette a ogni neurone del layer precedente (chiamato anche "fully connected")
- **Funzione di attivazione** — una funzione non lineare applicata all'output di ogni neurone; senza di essa, impilare i layer non sarebbe più potente di un solo layer
- **Peso / parametro** (weight) — un numero che il modello aggiusta durante il training per ridurre gli errori; un modello tipico ha da migliaia a miliardi di pesi
- **Funzione di loss** — misura quanto sono sbagliate le previsioni del modello; il training cerca di minimizzare questo valore
- **Optimizer** — l'algoritmo che aggiusta i pesi per ridurre la loss
- **Epoch** — un passaggio completo attraverso tutti i dati di training

## Le Attivazioni `relu` e `softmax`

Due attivazioni appaiono in quasi ogni rete di classificazione:

**ReLU** (Rectified Linear Unit): `f(x) = max(0, x)`
- L'output è 0 per gli input negativi, x per gli input positivi
- Usata nei layer nascosti; introduce non-linearità a basso costo

**Softmax**: converte un vettore di numeri in probabilità che sommano a 1.0
- Usata nel layer di output finale per la classificazione multi-classe
- Output: `[0.02, 0.85, 0.01, ..., 0.05]` significa "85% sicuro che sia la cifra 1"

## Costruire un Modello Keras per MNIST

**Keras** è una libreria di reti neurali di alto livello che gira sopra TensorFlow.
Installala con:

```bash
pip install tensorflow
```

Ecco un modello completo per classificare le cifre MNIST:

```python
import tensorflow as tf
from tensorflow import keras

# Carica e prepara i dati:
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalizza i valori dei pixel da 0–255 a 0–1:
x_train = x_train / 255.0
x_test  = x_test  / 255.0

# Costruisci il modello:
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),   # 784 input
    keras.layers.Dense(128, activation="relu"),    # strato nascosto
    keras.layers.Dense(10,  activation="softmax") # 10 classi in uscita
])

# Compila: scegli la funzione di perdita, l'ottimizzatore e la metrica:
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Addestra per 5 epoche:
model.fit(x_train, y_train, epochs=5, validation_split=0.1)

# Valuta sul test set:
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Accuratezza sul test: {test_acc:.2%}")
```

Questo modello raggiunge tipicamente **97–98% di accuratezza** su MNIST — classificando correttamente circa 9.700 delle 10.000 immagini di test.

## Capire il Modello Layer per Layer

Percorriamo l'architettura:

```
Input: 28×28 image (784 pixels)
    ↓
Flatten:      (784,)       — reshape to a flat vector
    ↓
Dense(128, relu):  (128,)  — 128 neurons, each connected to all 784 inputs
    ↓                         weights: 784×128 = 100,352 parameters
Dense(10, softmax): (10,)  — one output per digit class (0–9)
    ↓                         weights: 128×10 = 1,280 parameters
Output: [0.01, 0.02, 0.95, ...] — probabilities for digits 0–9
```

Parametri totali: ~101.632 — piccolo per gli standard moderni, ma abbastanza potente per MNIST.

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
initCmLab('-2', `# Simula i calcoli di un neurone Dense:
import math

def relu(x):
    return max(0, x)

def dense_neuron(inputs, weights, bias):
    total = sum(i * w for i, w in zip(inputs, weights)) + bias
    return relu(total)

def softmax(vector):
    exps = [math.exp(v) for v in vector]
    total = sum(exps)
    return [e / total for e in exps]

# Simula una piccolissima rete con 3 input, 1 neurone nascosto e 3 classi:
inputs  = [0.5, 0.2, 0.8]   # valori dei pixel (normalizzati)
weights = [0.4, -0.3, 0.6]
bias    = 0.1

hidden_output = dense_neuron(inputs, weights, bias)
print(f"Uscita del neurone nascosto: {hidden_output:.4f}")

# Softmax su uno strato di uscita finto:
logits = [2.0, 1.0, 0.1]   # punteggi grezzi per 3 classi
probs  = softmax(logits)
print("Probabilità softmax:", [round(p, 3) for p in probs])
print(f"Somma delle probabilità: {sum(probs):.6f}")
print(f"Classe prevista: {probs.index(max(probs))}")`);
</script>

## Dimensione del Batch ed Epoch

Due impostazioni chiave del training:

**Dimensione del batch (batch size)**: quanti esempi di training il modello elabora prima di aggiornare i suoi pesi.
- Dimensione del batch 32 significa "elabora 32 immagini, calcola l'errore medio, aggiorna i pesi" — poi ripeti
- Batch più piccoli → aggiornamenti più rumorosi ma più veloci; batch più grandi → aggiornamenti più fluidi ma più lenti
- Scelte comuni: 32, 64, 128

**Epoch**: quante volte il modello vede l'intero dataset di training.
- 1 epoch = un passaggio completo attraverso 60.000 immagini (in batch)
- 5 epoch = 5 passaggi completi (300.000 batch in totale per MNIST con dimensione del batch 32)
- Troppi pochi epoch → il modello fa underfitting; troppi epoch → il modello fa overfitting

!!! mascot-tip "L'Optimizer Adam"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    `"adam"` (Adaptive Moment Estimation) è l'optimizer predefinito per la maggior parte dei principianti perché aggiusta automaticamente il learning rate per ogni parametro.
    Altri optimizer includono SGD (stochastic gradient descent) e RMSprop.
    In caso di dubbio, inizia con Adam — funziona bene in un'ampia gamma di compiti.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Implementa l'Accuratezza"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto ha uno stub per una funzione `accuracy()`.
    Implementala: conta quante previsioni corrispondono alle loro etichette vere, e restituisci la frazione corretta!

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
initCmLab('-3', `def accuracy(predictions, true_labels):
    # Restituisci la frazione di previsioni che corrispondono a true_labels
    pass   # sostituiscilo con la tua implementazione

# Prova la tua funzione:
preds  = [0, 1, 2, 1, 0, 2, 1, 0, 2, 1]
labels = [0, 1, 2, 0, 0, 1, 1, 0, 2, 1]

acc = accuracy(preds, labels)
print(f"Accuratezza: {acc:.0%}")   # dovrebbe essere 80% (8 corrette su 10)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Nel classificatore a soglia, prova `threshold = 63`. Migliora l'accuratezza?
   **Saprai che ha funzionato quando** vedi se l'accuratezza cambia.

2. Estendi la funzione `dense_neuron` per gestire correttamente gli input negativi: cosa produce ReLU per -2.0?
   **Saprai che ha funzionato quando** gli input negativi danno 0, non un numero negativo.

3. Calcola il softmax di `[1, 1, 1]`. Tutti gli input sono uguali — a cosa sommano le probabilità, e quanto vale ciascuna?
   **Saprai che ha funzionato quando** tutte e tre le probabilità sono uguali a 0.333.

4. Ricerca: cerca "matrice di confusione" (confusion matrix) e descrivi cosa mostra che la semplice accuratezza non mostra.
   **Saprai che ha funzionato quando** riesci a spiegare cosa rappresentano le righe e le colonne.

5. Pensa a due problemi del mondo reale: uno che ha bisogno dell'apprendimento supervisionato e uno che ha bisogno di quello non supervisionato. Descrivi come sarebbero i dati di training per ciascuno.
   **Saprai che ha funzionato quando** riesci ad articolare cosa significa (o non significa) "etichetta" per ciascun problema.

!!! mascot-celebration "Pioniere del Machine Learning!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora capisci il vocabolario, la matematica, e la struttura del machine learning!
    Supervisionato vs non supervisionato, divisioni train/val/test, overfitting, layer, attivazioni, funzioni di loss — hai il quadro completo.
    Un altro capitolo: le Reti Neurali Convoluzionali — l'architettura che ha rivoluzionato la visione artificiale. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
