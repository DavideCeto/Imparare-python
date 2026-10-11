---
title: NumPy e Calcolo Scientifico
description: Impara gli array NumPy, il broadcasting, il reshaping, lo slicing, la matematica element-wise, e funzioni chiave come zeros, ones, linspace, argmax, mean, e std
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:30:00
version: 0.09
---

# NumPy e Calcolo Scientifico

Alla fine di questa lezione sarai in grado di:

- Creare array NumPy con `np.array()`, `np.zeros()`, `np.ones()`, e `np.linspace()`
- Eseguire **matematica element-wise** e capire il **broadcasting**
- Fare slice e indicizzare gli array NumPy, inclusi gli array 2-D
- Calcolare **media**, **deviazione standard**, **massimo**, e **argmax** sugli array
- Combinare NumPy con matplotlib per disegnare un'onda sinusoidale

Le liste Python sono flessibili, ma lente per grandi insiemi di dati numerici. **NumPy** (Numerical Python) fornisce un tipo di array che è 10–100× più veloce perché memorizza i valori in modo compatto ed esegue le operazioni in codice C ottimizzato.

!!! mascot-welcome "Benvenuto/a al Capitolo 33!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    NumPy è il motore sotto quasi ogni libreria di data science e machine learning in Python.
    Imparalo una volta e lo userai in ogni progetto scientifico per il resto della tua carriera di programmatore.
    Immergiamoci! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Importare NumPy

Importa NumPy con l'alias standard `np`:

```python
import numpy as np
```

## Creare Array con `np.array()`

Un **array NumPy** (`ndarray`) è come una lista Python, ma:
- Tutti gli elementi devono essere dello stesso tipo (di solito `float64` o `int64`)
- Le operazioni matematiche funzionano automaticamente elemento per elemento
- Può essere multidimensionale (2-D, 3-D, ecc.)

Converti una lista Python in un array:

```python
a = np.array([1, 2, 3, 4, 5])
print(a)          # [1 2 3 4 5]
print(a.dtype)    # int64
print(a.shape)    # (5,) — one dimension with 5 elements
```

## Matematica Element-Wise e Broadcasting

La grande differenza tra le liste e gli array: **gli operatori matematici funzionano elemento per elemento**.

```python
a = np.array([1, 2, 3, 4])
print(a + 10)      # [11 12 13 14]  — adds 10 to every element
print(a * 2)       # [2  4  6  8]
print(a ** 2)      # [1  4  9 16]
```

Aggiungere un singolo numero a ogni elemento si chiama **broadcasting** — NumPy "trasmette" il valore scalare attraverso l'intero array automaticamente, senza bisogno di nessun ciclo.

Due array della stessa forma possono essere combinati elemento per elemento:

```python
b = np.array([10, 20, 30, 40])
print(a + b)   # [11 22 33 44]
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto applica matematica element-wise a un array.
    Prima di eseguirlo, prevedi: come apparirà `temps_f` dopo la formula?
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
initCmLab('', `import numpy as np

temps_c = np.array([0, 20, 37, 100])
temps_f = (temps_c * 9/5) + 32

print("Celsius:   ", temps_c)
print("Fahrenheit:", temps_f)

# Also works: min, max, mean
print("Min F:", temps_f.min())
print("Max F:", temps_f.max())
print("Mean F:", temps_f.mean())`);
</script>

## Creare Array Automaticamente

NumPy fornisce funzioni per i pattern comuni di creazione di array:

| Funzione | Crea |
|----------|---------|
| `np.zeros(n)` | Array di n zeri |
| `np.ones(n)` | Array di n uni |
| `np.arange(start, stop, step)` | Come `range()` ma restituisce un array |
| `np.linspace(start, stop, num)` | Valori equispaziati tra start e stop |
| `np.random.rand(n)` | n valori casuali tra 0 e 1 |

`np.linspace()` è particolarmente utile per la matematica e il disegno di grafici — genera esattamente `num` punti equispaziati:

```python
x = np.linspace(0, 1, 5)
print(x)   # [0.   0.25 0.5  0.75 1.  ]
```

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
initCmLab('-2', `import numpy as np

print("zeros:", np.zeros(5))
print("ones:", np.ones(4))
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 6))

# Use linspace to simulate a sine wave (without plotting):
import math
x = np.linspace(0, 2 * math.pi, 8)
y = np.array([math.sin(v) for v in x])
print("\\nSine wave sample (x, sin(x)):")
for xi, yi in zip(x, y):
    print(f"  x={xi:.2f}  sin(x)={yi:.3f}")`);
</script>

## Slicing e Indicizzazione

Gli array NumPy usano la stessa sintassi di slicing `[start:stop:step]` delle liste Python:

```python
a = np.array([10, 20, 30, 40, 50])
print(a[1:4])    # [20 30 40]
print(a[::2])    # [10 30 50]   — every other element
print(a[-1])     # 50            — last element
```

## Array 2-D — Righe e Colonne

Un array 2-D è come una tabella di un foglio di calcolo — ha righe e colonne.
Creane uno passando una lista di liste:

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.shape)     # (3, 3) — 3 rows, 3 columns
print(matrix[1, 2])     # 6 — row 1, column 2
print(matrix[0, :])     # [1 2 3] — entire first row
print(matrix[:, 1])     # [2 5 8] — entire second column
```

L'indice `matrix[row, col]` seleziona una cella specifica.
`matrix[row, :]` seleziona un'intera riga; `matrix[:, col]` seleziona un'intera colonna.

## Rimodellare gli Array

`array.reshape(rows, cols)` riorganizza un array in una forma diversa senza cambiare i dati.
Il numero totale di elementi deve rimanere lo stesso.

```python
flat = np.arange(12)           # [0 1 2 3 4 5 6 7 8 9 10 11]
grid = flat.reshape(3, 4)      # 3 rows, 4 columns
print(grid)
```

## Funzioni Statistiche

NumPy ha statistiche built-in veloci:

| Funzione | Restituisce |
|----------|---------|
| `a.mean()` | Media |
| `a.std()` | Deviazione standard |
| `a.min()` / `a.max()` | Valore minimo / massimo |
| `a.sum()` | Somma di tutti gli elementi |
| `a.argmax()` | **Indice** del valore massimo |
| `a.argmin()` | **Indice** del valore minimo |

`argmax()` e `argmin()` sono particolarmente utili quando vuoi sapere *dove* in un array si trova il massimo o il minimo — non solo quale sia il valore.

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
initCmLab('-3', `import numpy as np

scores = np.array([78, 95, 88, 62, 91, 74, 99, 83])

print("Scores:", scores)
print("Mean:", scores.mean())
print("Std dev:", round(scores.std(), 2))
print("Min:", scores.min(), "at index", scores.argmin())
print("Max:", scores.max(), "at index", scores.argmax())

names = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Hank"]
winner = names[scores.argmax()]
print(f"Top scorer: {winner} with {scores.max()}")`);
</script>

## Disegnare un'Onda Sinusoidale con NumPy e matplotlib

Qui NumPy e matplotlib si combinano: usa `np.linspace()` per generare valori x equispaziati, applica `np.sin()` per ottenere i valori y, poi disegna.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4 * np.pi, 200)   # 200 points across 2 full cycles
y = np.sin(x)

plt.plot(x, y, color="steelblue")
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.axhline(0, color="gray", linewidth=0.8)   # horizontal line at y=0
plt.grid(True)
plt.show()
```

`np.sin()`, `np.cos()`, `np.exp()`, e `np.sqrt()` funzionano tutti su interi array — senza bisogno di nessun ciclo.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Trova il Giorno Più Caldo"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto ha i dati della temperatura per una settimana, ma la riga che trova il giorno più caldo manca!
    Aggiungi una riga usando `argmax()` per trovare e stampare quale giorno della settimana ha avuto la temperatura più alta.

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
initCmLab('-4', `import numpy as np

days  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = np.array([22, 25, 28, 31, 26, 24, 20])

print("Week temperatures:", temps)
print("Average:", temps.mean(), "°C")

# Add one line here: use argmax() to find and print the hottest day`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Crea una matrice identità 4×4 usando `np.eye(4)` — una matrice quadrata con degli 1 sulla diagonale.
   **Saprai che ha funzionato quando** vedi degli 1 lungo la diagonale e degli 0 ovunque altro.

2. Calcola il prodotto scalare di due array usando `np.dot([1,2,3], [4,5,6])`.
   **Saprai che ha funzionato quando** ottieni `32` (1×4 + 2×5 + 3×6 = 32).

3. Genera 5 interi casuali tra 1 e 100 usando `np.random.randint(1, 101, 5)`. Trova la media.
   **Saprai che ha funzionato quando** ottieni un insieme diverso di numeri a ogni esecuzione con una media tra 1 e 100.

4. Usa `np.where(temps > 25, "Hot", "Cool")` sull'array delle temperature per etichettare ogni giorno.
   **Saprai che ha funzionato quando** vedi un array di stringhe come `["Cool", "Cool", "Hot", ...]`.

5. Crea una matrice 3×3 e usa `matrix.T` per trasporla (le righe diventano colonne).
   **Saprai che ha funzionato quando** le righe e le colonne sono scambiate.

!!! mascot-celebration "Pioniere del Python Scientifico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    NumPy è la base dell'intero ecosistema Python scientifico — pandas, scikit-learn, TensorFlow, e PyTorch usano tutti gli array NumPy sotto il cofano.
    Padroneggiarlo ti mette alla linea di partenza della data science e dell'IA. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
