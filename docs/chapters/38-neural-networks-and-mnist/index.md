---
title: Reti Neurali e MNIST
description: Costruisci una Rete Neurale Convoluzionale (CNN) per classificare le cifre MNIST — e ottieni una panoramica di RNN, LSTM, e autoencoder
generated_by: claude skill chapter-content-generator
date: 2026-06-28 16:20:00
version: 0.09
---

# Reti Neurali e MNIST

Alla fine di questa lezione sarai in grado di:

- Spiegare cosa rende una **Rete Neurale Convoluzionale (CNN)** diversa da una rete densa
- Capire i layer **Conv2D**, **MaxPooling2D**, **Flatten**, e **Dropout**
- Leggere e scrivere un modello CNN Keras completo
- Usare `model.compile()`, `model.fit()`, `model.evaluate()`, e `model.predict()`
- Descrivere ad alto livello: **RNN**, **LSTM**, e **autoencoder**

Le reti dense del Capitolo 37 trattano un'immagine come un vettore piatto — perdendo tutte le informazioni spaziali.
Le reti convoluzionali mantengono la struttura 2-D delle immagini e cercano **pattern locali** come bordi, angoli, e forme. Questo è il motivo per cui le CNN sono l'architettura dominante per il riconoscimento delle immagini.

!!! mascot-welcome "Benvenuto/a al Capitolo 38!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Benvenuto/a all'ultimo capitolo di *Introduzione a Python*!
    Sei arrivato da stampare "Hello, World!" fino a costruire un'IA che legge cifre scritte a mano.
    Finiamo alla grande! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Perché le Convoluzioni?

Una rete densa che prende un'immagine 28×28 la appiattisce in 784 numeri — scarta completamente il fatto che il pixel (3, 5) è vicino al pixel (3, 6).

Un layer **convoluzionale** fa scorrere un piccolo filtro (chiamato **kernel**) attraverso l'immagine.
Il kernel rileva pattern locali — un kernel 3×3 può rilevare un bordo orizzontale, una diagonale, o un angolo.
Più kernel nello stesso layer rilevano caratteristiche diverse simultaneamente.

Questo dà alle CNN due enormi vantaggi:
- **Efficienza dei parametri** — un kernel è condiviso attraverso tutta l'immagine (contro il denso dove ogni pixel ha il proprio peso per ogni neurone)
- **Invarianza alla traslazione** — un kernel che rileva la forma di un "7" in alto a sinistra lo riconosce anche in basso a destra, perché lo stesso kernel scansiona ovunque

## Tipi Chiave di Layer CNN

Prima di leggere il codice Keras, ecco i quattro nuovi tipi di layer di questo capitolo:

| Layer | Scopo |
|-------|---------|
| `Conv2D(filters, kernel_size, activation)` | Fa scorrere `filters` kernel di dimensione `kernel_size×kernel_size` attraverso l'immagine |
| `MaxPooling2D(pool_size)` | Riduce le dimensioni spaziali prendendo il massimo in ogni regione |
| `Dropout(rate)` | Imposta casualmente a zero una frazione `rate` di neuroni durante il training — combatte l'overfitting |
| `Flatten()` | Converte le mappe di caratteristiche 2-D in un vettore 1-D prima dei layer densi |

Un **filtro** (o mappa di caratteristiche, feature map) è l'output di un kernel applicato all'intera immagine.
`Conv2D(32, (3,3))` crea 32 kernel 3×3 diversi — producendo 32 mappe di caratteristiche.

`MaxPooling2D((2,2))` divide l'immagine in blocchi 2×2 e mantiene solo il valore massimo in ogni blocco — dimezzando larghezza e altezza.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto simula un passo di Max Pooling su una piccola griglia 4×4.
    Se la dimensione del pool è 2×2, quanti valori di output ti aspetti?
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
initCmLab('', `def max_pool_2d(grid, pool_size=2):
    rows = len(grid)
    cols = len(grid[0])
    out_rows = rows // pool_size
    out_cols = cols // pool_size
    result = []
    for r in range(out_rows):
        row = []
        for c in range(out_cols):
            block = [
                grid[r*pool_size + dr][c*pool_size + dc]
                for dr in range(pool_size)
                for dc in range(pool_size)
            ]
            row.append(max(block))
        result.append(row)
    return result

# 4x4 feature map (imagine after a convolution):
feature_map = [
    [1, 3, 2, 4],
    [5, 6, 1, 2],
    [3, 1, 7, 2],
    [2, 4, 1, 8],
]

print("Input (4x4):")
for row in feature_map:
    print(" ", row)

pooled = max_pool_2d(feature_map, pool_size=2)
print("\\nAfter MaxPooling 2x2:")
for row in pooled:
    print(" ", row)
print(f"Output size: {len(pooled)}x{len(pooled[0])}")`);
</script>

## Dropout — Combattere l'Overfitting

**Dropout** è una tecnica di regolarizzazione semplice ma potente.

Durante ogni passo di training, Dropout imposta casualmente a zero l'output di una frazione di neuroni.
Con `Dropout(0.5)`, metà dei neuroni viene silenziata casualmente ogni volta — così la rete non può fare affidamento su nessun singolo neurone.

Questo forza la rete a imparare **rappresentazioni ridondanti** — più modi per rilevare la stessa caratteristica.
Al momento dell'inferenza (previsione), Dropout viene automaticamente disabilitato e tutti i neuroni partecipano.

```python
keras.layers.Dropout(0.5)   # randomly zero out 50% of inputs during training
keras.layers.Dropout(0.25)  # gentler — zero out 25%
```

## Una CNN Completa per MNIST

Ecco una CNN completa che raggiunge **~99% di accuratezza** su MNIST:

```python
import tensorflow as tf
from tensorflow import keras

# Load and prepare data:
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Add channel dimension: (samples, 28, 28) → (samples, 28, 28, 1)
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test  = x_test.reshape(-1, 28, 28, 1) / 255.0

# Build CNN:
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation="relu",
                        input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation="relu"),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()   # print layer-by-layer shape info
```

## Capire `model.compile()`

`model.compile()` imposta tre scelte chiave per il training:

- **optimizer** — come vengono aggiornati i pesi (ad es., `"adam"`, `"sgd"`)
- **loss** — cosa minimizzare durante il training
  - `"sparse_categorical_crossentropy"` — per etichette di classe intere (ad es., 0, 1, 2, …, 9)
  - `"categorical_crossentropy"` — per etichette codificate one-hot
  - `"binary_crossentropy"` — per problemi a due classi (sì/no)
- **metrics** — cosa tracciare ma non ottimizzare (ad es., `"accuracy"`)

## Allenare con `model.fit()`

```python
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.1
)
```

`model.fit()` restituisce un oggetto `history`.
`history.history` è un dict con le chiavi `"accuracy"`, `"val_accuracy"`, `"loss"`, `"val_loss"`.

Puoi disegnare le curve di training per visualizzare l'overfitting:

```python
import matplotlib.pyplot as plt

plt.plot(history.history["accuracy"],     label="train accuracy")
plt.plot(history.history["val_accuracy"], label="val accuracy")
plt.legend()
plt.title("Training Curves")
plt.show()
```

## Valutare con `model.evaluate()`

```python
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.2%}")   # e.g., "99.15%"
```

Chiamalo **una sola volta**, alla fine, su dati che il modello non ha mai visto.

## Fare Previsioni con `model.predict()`

```python
predictions = model.predict(x_test[:10])   # probabilities for first 10 images
predicted_classes = predictions.argmax(axis=1)
print("Predicted:", predicted_classes)
print("True labels:", y_test[:10])
```

`predictions` è un array di forma `(10, 10)` — 10 immagini, ognuna con 10 probabilità di classe.
`.argmax(axis=1)` sceglie l'indice della probabilità più alta per ogni immagine.

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
initCmLab('-2', `import math

def softmax(vec):
    exps = [math.exp(v) for v in vec]
    s = sum(exps)
    return [e/s for e in exps]

def argmax(lst):
    return lst.index(max(lst))

# Simulate predictions for 5 "images":
raw_outputs = [
    [10.2, 0.1, 0.3, 0.0, 0.5, 0.1, 0.2, 0.0, 0.1, 0.1],  # very sure: class 0
    [0.1, 0.0, 0.2, 0.1, 0.1, 0.0, 0.1, 9.8, 0.2, 0.1],   # very sure: class 7
    [0.5, 0.3, 9.1, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1, 0.1],   # very sure: class 2
    [0.1, 9.5, 0.1, 0.0, 0.2, 0.1, 0.1, 0.0, 0.1, 0.0],   # very sure: class 1
    [2.0, 0.5, 1.5, 1.0, 2.5, 0.8, 1.2, 0.9, 1.8, 2.1],   # uncertain!
]
true_labels = [0, 7, 2, 1, 5]

for i, (logits, true) in enumerate(zip(raw_outputs, true_labels)):
    probs = softmax(logits)
    pred  = argmax(probs)
    conf  = max(probs)
    status = "✓" if pred == true else "✗"
    print(f"  {status} True={true}, Pred={pred}, Confidence={conf:.1%}")`);
</script>

## Estrazione delle Caratteristiche

Una CNN allenata non è solo un classificatore di cifre — i suoi **layer intermedi** hanno imparato caratteristiche visive significative:

- I primi layer Conv2D: rilevano bordi e angoli
- I layer Conv2D intermedi: rilevano curve e forme semplici
- I layer successivi: rilevano caratteristiche specifiche delle cifre

Il **transfer learning** sfrutta questo: prendi una CNN pre-allenata su milioni di immagini, tagli via gli ultimi layer, e attacchi nuovi layer allenati sul tuo dataset più piccolo. Le caratteristiche pre-allenate si trasferiscono al nuovo compito.

Questo è il motivo per cui un modello allenato su ImageNet (1,3M di foto) può essere adattato rapidamente per classificare radiografie medicali, immagini satellitari, o stili artistici — con solo centinaia di nuovi esempi etichettati.

## Altre Architetture di Reti Neurali

### Reti Neurali Ricorrenti (RNN)

Le **RNN** elaborano sequenze — testo, audio, serie temporali — un passo alla volta.
Ogni passo produce uno **stato nascosto** (hidden state) che viene passato al passo successivo, dando alla rete una memoria del passato.

```python
keras.layers.SimpleRNN(64)
```

Le RNN hanno difficoltà con le sequenze lunghe perché il segnale del gradiente si debilita attraverso molti passi temporali (il problema del "vanishing gradient").

### Long Short-Term Memory (LSTM)

Le **LSTM** sono un tipo speciale di RNN con meccanismi di gating che le permettono di ricordare o dimenticare informazioni su sequenze lunghe.
Sono la scelta standard per la modellazione del linguaggio, il riconoscimento vocale, e la previsione delle serie temporali.

```python
keras.layers.LSTM(128)
```

### Autoencoder

Un **autoencoder** impara a comprimere i dati in una piccola rappresentazione (il **bottleneck**) e poi a ricostruire l'originale.

```
Input (784 pixels) → Encoder → Bottleneck (32 values) → Decoder → Reconstructed image
```

Applicazioni: rilevamento di anomalie, denoising, arte generativa, compressione dei dati.

## Mettere Tutto Insieme — Il Viaggio della Forma nella CNN

La tabella sotto traccia la forma dei dati attraverso la CNN per una singola immagine MNIST 28×28:

| Layer | Forma dell'Output | Parametri |
|-------|-------------|------------|
| Input | (28, 28, 1) | 0 |
| Conv2D(32, 3×3) | (26, 26, 32) | 320 |
| MaxPooling2D | (13, 13, 32) | 0 |
| Conv2D(64, 3×3) | (11, 11, 64) | 18.496 |
| MaxPooling2D | (5, 5, 64) | 0 |
| Flatten | (1.600,) | 0 |
| Dense(128) | (128,) | 204.928 |
| Dropout(0.5) | (128,) | 0 |
| Dense(10) | (10,) | 1.290 |

Parametri totali: **225.034** — molto più efficiente di un modello solo-denso di profondità simile.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Conta i Parametri"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Un layer `Dense(64)` che segue un layer `Flatten()` con 1.600 input ha 1.600 × 64 pesi più 64 valori di bias.
    Scrivi una funzione che calcola il conteggio dei parametri per un layer Dense dalla sua dimensione di input e numero di neuroni!

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
initCmLab('-3', `def dense_params(input_size, neurons):
    weights = input_size * neurons
    biases  = neurons
    return weights + biases

# CNN architecture:
layers = [
    ("Conv2D(32, 3x3)",  (3 * 3 * 1) * 32 + 32),   # kernel * in_channels * filters + bias
    ("MaxPooling2D",     0),
    ("Conv2D(64, 3x3)",  (3 * 3 * 32) * 64 + 64),  # 32 input channels
    ("MaxPooling2D",     0),
    ("Flatten",          0),
    ("Dense(128)",       dense_params(1600, 128)),
    ("Dropout(0.5)",     0),
    ("Dense(10)",        dense_params(128, 10)),
]

total = 0
print(f"{'Layer':<22} {'Parameters':>12}")
print("-" * 36)
for name, params in layers:
    print(f"{name:<22} {params:>12,}")
    total += params
print("-" * 36)
print(f"{'Total':<22} {total:>12,}")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Modifica la simulazione del max pooling per usare una dimensione del pool 3×3 su una griglia 6×6. Qual è la dimensione dell'output?
   **Saprai che ha funzionato quando** vedi un output 2×2.

2. Nel simulatore di previsioni, cambia i logit dell'ultima riga così che favoriscano più fortemente la classe 5.
   **Saprai che ha funzionato quando** la confidenza per la classe 5 supera il 70%.

3. Implementa `min_pool_2d` (come `max_pool_2d` ma usando `min` invece di `max`). Come differiscono gli output dal max pooling sullo stesso input?
   **Saprai che ha funzionato quando** vedi che il min pooling mantiene i valori più scuri (più piccoli).

4. Calcola il conteggio dei parametri per un layer `Dense(256)` che segue un layer `Dense(128)`.
   **Saprai che ha funzionato quando** ottieni 128 × 256 + 256 = 33.024.

5. Ricerca: cerca "GPT" o "BERT" e descrivi in 2-3 frasi come differiscono dalla CNN descritta in questo capitolo.
   **Saprai che ha funzionato quando** riesci a spiegare: che tipo di dati elaborano e quale architettura usano.

!!! mascot-celebration "Ce l'Hai Fatta — Diplomato in Python!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai completato tutti i 38 capitoli di *Introduzione a Python*!
    Hai iniziato stampando un quadrato con la tartaruga e hai finito costruendo un'IA che legge cifre scritte a mano con il 99% di accuratezza.
    Non sei più un principiante — sei un programmatore Python. Vai a costruire qualcosa di straordinario!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
