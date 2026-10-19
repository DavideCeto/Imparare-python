---
title: Visualizzazione Dati con matplotlib
description: Crea grafici a linee, scatter plot, grafici a barre, istogrammi, e figure multi-pannello usando matplotlib — la libreria di grafici più popolare di Python
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:20:00
version: 0.09
---

# Visualizzazione Dati con matplotlib

Alla fine di questa lezione sarai in grado di:

- Importare e usare **matplotlib.pyplot** per creare grafici in Python
- Aggiungere titoli, etichette degli assi, legende, e griglie a qualsiasi grafico
- Creare **grafici a linee**, **scatter plot**, **grafici a barre**, e **istogrammi**
- Disegnare **linee multiple** su un grafico e disporre **sottografici** uno affianco all'altro
- Salvare un grafico in un file immagine con `savefig()`

Un grafico può comunicare in un secondo quello che una tabella di numeri richiede minuti per essere capita. `matplotlib` è lo strumento a cui i programmatori Python ricorrono per primo.

!!! mascot-welcome "Benvenuto/a al Capitolo 32!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La visualizzazione dei dati trasforma numeri grezzi in storie che puoi vedere.
    Scienziati, giornalisti, analisti di business, e sviluppatori di giochi usano tutti grafici costruiti con matplotlib.
    Iniziamo a disegnare! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Importare matplotlib

matplotlib è una libreria grande — tipicamente importi solo il suo sottomodulo `pyplot`, con alias `plt`:

```python
import matplotlib.pyplot as plt
```

Tutto ciò di cui hai bisogno — `plt.plot()`, `plt.show()`, `plt.title()` — vive in `pyplot`.

!!! mascot-tip "matplotlib in Skulpt"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    I laboratori Skulpt sotto usano una simulazione basata su testo per mostrare i dati che matplotlib disegnerebbe.
    In un vero ambiente Python (Thonny, VS Code, Jupyter), `plt.show()` apre una finestra interattiva.
    I pattern che imparerai qui si trasferiscono direttamente — stessi nomi di funzione, stessi parametri.

## Il Tuo Primo Grafico a Linee

`plt.plot(x_values, y_values)` disegna una linea che collega i punti di dati dati.
`plt.show()` rende il grafico.

Il pattern più semplice è:

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Quadrati")
plt.xlabel("Numero")
plt.ylabel("Quadrato")
plt.show()
```

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
initCmLab('', `import matplotlib
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Quadrati")
plt.xlabel("Numero")
plt.ylabel("Quadrato")
plt.show()

print("Dati del grafico:")
for i, j in zip(x, y):
    print(f"  x={i}, y={j}")`);
</script>

## Aggiungere Etichette, Titoli, e una Griglia

Queste funzioni rifiniscono qualsiasi grafico:

| Funzione | Effetto |
|----------|--------|
| `plt.title("text")` | Titolo del grafico |
| `plt.xlabel("text")` | Etichetta l'asse x |
| `plt.ylabel("text")` | Etichetta l'asse y |
| `plt.legend()` | Mostra una legenda per le serie etichettate |
| `plt.grid(True)` | Aggiungi una griglia di sfondo |
| `plt.xlim(lo, hi)` | Imposta l'intervallo dell'asse x |
| `plt.ylim(lo, hi)` | Imposta l'intervallo dell'asse y |

Chiamale dopo `plt.plot()` ma prima di `plt.show()`.

## Disegnare Linee Multiple

Chiamare `plt.plot()` più volte prima di `plt.show()` mette tutte le linee sullo stesso grafico.
Usa il parametro `label=` e poi chiama `plt.legend()` così i lettori sanno quale linea è quale.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto disegna tre diverse serie matematiche su un grafico.
    Quale pensi che crescerà più velocemente: x, x al quadrato, o x al cubo (ridotto in scala)?
    Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]

y_linear = [v for v in x]
y_square = [v**2 for v in x]
y_cube   = [v**3 / 10 for v in x]   # in scala, così entrano tutti in un grafico

plt.plot(x, y_linear, label="x (lineare)")
plt.plot(x, y_square, label="x² (quadratica)")
plt.plot(x, y_cube,   label="x³/10 (cubica)")

plt.title("Confronto della crescita")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

print("Valori per x=5:")
print(f"  lineare   : {y_linear[-1]}")
print(f"  quadratica: {y_square[-1]}")
print(f"  cubica/10 : {y_cube[-1]:.1f}")`);
</script>

## Scatter Plot

Un **scatter plot** mostra singoli punti di dati senza collegarli con linee.
Usa `plt.scatter(x, y)` invece di `plt.plot()`.

Gli scatter plot sono ideali per mostrare le relazioni tra due variabili — per esempio, altezza vs peso, o ore di studio vs punteggio al test.

```python
import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [45, 55, 60, 70, 75, 80, 88, 95]

plt.scatter(study_hours, test_scores, color="blue", s=80)
plt.title("Ore di studio e voto nella verifica")
plt.xlabel("Ore di studio")
plt.ylabel("Punteggio")
plt.grid(True)
plt.show()
```

Il parametro `s=` controlla la dimensione dei punti (il default è 20).
Il parametro `color=` accetta nomi di colore (`"red"`, `"blue"`, `"green"`) o codici esadecimali (`"#FF6600"`).

## Grafici a Barre

`plt.bar(x_labels, heights)` crea un **grafico a barre verticale**.
I grafici a barre sono i migliori per confrontare categorie discrete — punteggi per studente, entrate per mese, ecc.

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
initCmLab('-3', `import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Art"]
scores   = [88, 92, 76, 85, 95]
colors   = ["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"]

plt.bar(subjects, scores, color=colors)
plt.title("Punteggi degli studenti per materia")
plt.xlabel("Materia")
plt.ylabel("Punteggio")
plt.ylim(0, 100)
plt.grid(axis="y")
plt.show()

print("Punteggi:")
for subj, score in zip(subjects, scores):
    print(f"  {subj}: {score}")
print(f"Media: {sum(scores)/len(scores):.1f}")`);
</script>

`plt.grid(axis="y")` aggiunge le linee della griglia solo sull'asse y — uno stile comune per i grafici a barre.

## Istogrammi

Un **istogramma** mostra la distribuzione di un insieme di numeri — quanti valori rientrano in ogni intervallo (chiamato "bin").

`plt.hist(data, bins=10)` divide automaticamente i dati in `bins` gruppi di uguale larghezza e disegna barre che mostrano il conteggio in ogni gruppo.

```python
import matplotlib.pyplot as plt

# 50 altezze più o meno casuali (cm):
heights = [162, 170, 168, 175, 180, 165, 172, 178, 160, 185,
           163, 171, 177, 182, 169, 174, 179, 166, 173, 188,
           160, 171, 164, 176, 183, 168, 175, 180, 162, 170,
           165, 172, 178, 184, 167, 174, 179, 163, 171, 187,
           161, 170, 166, 175, 181, 169, 173, 178, 164, 172]

plt.hist(heights, bins=8, color="steelblue", edgecolor="white")
plt.title("Distribuzione delle altezze")
plt.xlabel("Altezza (cm)")
plt.ylabel("Numero di persone")
plt.show()
```

## Salvare le Figure con `savefig()`

Invece di `plt.show()`, chiama `plt.savefig("filename.png")` per salvare il grafico in un file.

```python
plt.plot(x, y)
plt.title("Il mio grafico")
plt.savefig("chart.png", dpi=150)   # 150 punti per pollice, buono per lo schermo
```

I formati supportati includono `.png`, `.jpg`, `.pdf`, e `.svg`.
Chiama `savefig()` prima di `plt.show()` — `show()` resetta la figura.

## Sottografici — Più Grafici Fianco a Fianco

`plt.subplots(rows, cols)` crea una griglia di grafici (chiamati **assi**, axes).
Restituisce il `fig` (l'intero canvas) e un array di oggetti `ax` — uno per posizione del grafico.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y_square)
axes[0].set_title("Quadratica")

axes[1].bar(subjects, scores)
axes[1].set_title("Punteggi")

plt.tight_layout()   # evita che i grafici si sovrappongano
plt.show()
```

Nota: quando usi i sottografici, usa `ax.set_title()` (non `plt.title()`) e `ax.set_xlabel()` (non `plt.xlabel()`).

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Correggi il Grafico a Barre"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto cerca di fare un grafico a barre ma mancano le etichette degli assi e il titolo.
    Aggiungi `plt.title()`, `plt.xlabel()`, e `plt.ylabel()` per completarlo!

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
initCmLab('-4', `import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [120, 145, 130, 165, 182, 200]

plt.bar(months, sales, color="coral")
# Aggiungi qui title, xlabel e ylabel:

plt.show()

print("Dati delle vendite:")
for month, amount in zip(months, sales):
    print(f"  {month}: {amount} unità")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia i colori del grafico a linee aggiungendo il parametro `color=`: `plt.plot(x, y, color="red")`.
   **Saprai che ha funzionato quando** la linea appare nel colore che hai scelto.

2. Aggiungi un parametro `marker="o"` a `plt.plot()` per mostrare dei punti a ogni coordinata dei dati.
   **Saprai che ha funzionato quando** appaiono cerchi a ogni coordinata x, y.

3. Crea un grafico a barre orizzontale usando `plt.barh(subjects, scores)` invece di `plt.bar()`.
   **Saprai che ha funzionato quando** le barre crescono orizzontalmente invece che verticalmente.

4. Genera una lista di 100 numeri usando una list comprehension con `(i % 10)` e disegna un istogramma con `bins=10`.
   **Saprai che ha funzionato quando** vedi una distribuzione piatta — ogni bin ha circa la stessa altezza.

5. Usa `plt.subplots(2, 1)` per impilare due grafici verticalmente: un grafico a linee in alto e un grafico a barre sotto.
   **Saprai che ha funzionato quando** entrambi i grafici appaiono nella stessa figura, impilati.

!!! mascot-celebration "Visualizzatore di Dati!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai trasformato numeri grezzi in grafici che raccontano storie!
    Grafici a linee, scatter plot, grafici a barre, istogrammi, e sottografici — questi sono il pane quotidiano di ogni data scientist.
    Il prossimo capitolo ti porta in NumPy, dove imparerai a elaborare grandi quantità di dati numerici a velocità fulminea. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
