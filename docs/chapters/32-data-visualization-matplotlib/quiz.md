# Quiz: Visualizzazione Dati con matplotlib

Verifica la tua comprensione di matplotlib, dei tipi di grafici, delle etichette, dei sottografici, e del salvataggio delle figure con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è il modo standard di importare matplotlib per creare grafici?

<div class="upper-alpha" markdown>
1. `import matplotlib`
2. `from matplotlib import charts as mc`
3. `import matplotlib.pyplot as plt`
4. `import pyplot from matplotlib`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La convenzione standard è `import matplotlib.pyplot as plt`. Il sottomodulo `pyplot` contiene tutte le funzioni per i grafici: `plt.plot()`, `plt.show()`, `plt.title()`, ecc. L'alias `plt` è usato universalmente nella comunità di data science Python — lo vedrai in ogni tutorial, manuale, ed esempio di codice professionale.

    **Concept Tested:** Importing matplotlib

---

#### 2. Cosa fa `plt.show()`?

<div class="upper-alpha" markdown>
1. Salva il grafico attuale in un file chiamato `chart.png`
2. Elimina tutti i dati del grafico precedente e inizia un nuovo grafico
3. Rende e mostra il grafico che è stato costruito con le precedenti chiamate a `plt.plot()`
4. Stampa i valori grezzi dei dati usati nel grafico sulla console
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `plt.show()` rende e mostra la finestra del grafico. Costruisci un grafico chiamando `plt.plot()`, `plt.title()`, `plt.xlabel()`, ecc., poi chiami `plt.show()` per mostrarlo effettivamente. Nei Jupyter Notebook, i grafici potrebbero rendersi automaticamente senza `plt.show()`, ma è sempre buona pratica includerlo.

    **Concept Tested:** plt.show()

---

#### 3. Quale funzione matplotlib crea uno scatter plot?

<div class="upper-alpha" markdown>
1. `plt.dots(x, y)`
2. `plt.points(x, y)`
3. `plt.scatter(x, y)`
4. `plt.spot(x, y)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `plt.scatter(x, y)` crea uno scatter plot — singoli punti disegnati senza collegare linee. Gli scatter plot sono utili per mostrare la relazione (correlazione) tra due variabili. Usa `plt.plot(x, y)` per i grafici a linee (che collegano i punti). Non esistono funzioni `dots()`, `points()`, o `spot()` in matplotlib.

    **Concept Tested:** Scatter Plots

---

#### 4. Cosa fa `plt.xlabel("Time (seconds)")`?

<div class="upper-alpha" markdown>
1. Imposta il titolo del grafico a "Time (seconds)"
2. Aggiunge un'etichetta all'asse x (asse orizzontale)
3. Limita l'intervallo dell'asse x a 0-10 secondi
4. Cambia i segni di graduazione dell'asse x per mostrare i secondi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `plt.xlabel("text")` aggiunge un'etichetta di testo sotto l'asse x (l'asse orizzontale) del grafico. In modo simile, `plt.ylabel("text")` etichetta l'asse y (asse verticale), e `plt.title("text")` imposta il titolo in cima. Etichetta sempre i tuoi assi così i lettori sanno cosa rappresentano i dati e quali unità vengono usate.

    **Concept Tested:** Axis Labels and Titles

---

#### 5. Come aggiungi più linee a un grafico?

<div class="upper-alpha" markdown>
1. Chiama `plt.new_line()` prima di ogni chiamata a `plt.plot()`
2. Passa tutti i dati come una lista annidata a una singola chiamata a `plt.plot()`
3. Chiama `plt.plot()` più volte prima di chiamare `plt.show()`
4. Crea più figure con `plt.figure()` e sovrapponile
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Ogni chiamata a `plt.plot()` aggiunge un'altra linea al grafico attuale. Tutte le linee vengono combinate quando chiami `plt.show()`. Usa il parametro `label=` su ogni chiamata a `plt.plot()` e poi chiama `plt.legend()` per mostrare una legenda che identifica quale linea è quale.

    **Concept Tested:** Multiple Lines

---

#### 6. Quale tipo di grafico è migliore per mostrare come cambia un valore continuo nel tempo?

<div class="upper-alpha" markdown>
1. Un grafico a barre
2. Un istogramma
3. Un grafico a torta
4. Un grafico a linee
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Un grafico a linee (creato con `plt.plot()`) è ideale per mostrare dati continui che cambiano nel tempo — come la temperatura durante una settimana, il prezzo di un'azione nel corso di mesi, o un esperimento di fisica durante i secondi. I grafici a barre confrontano categorie discrete. Gli istogrammi mostrano le distribuzioni di frequenza. I grafici a torta mostrano le proporzioni di un totale.

    **Concept Tested:** Chart Types

---

#### 7. Cosa fa `plt.grid(True)`?

<div class="upper-alpha" markdown>
1. Divide la finestra del grafico in una griglia di sottografici
2. Aggiunge linee della griglia di sfondo al grafico per rendere i valori più facili da leggere
3. Aggancia i punti dei dati all'intersezione della griglia più vicina
4. Mostra le coordinate del grafico di ogni punto di dati
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `plt.grid(True)` aggiunge leggere linee della griglia di sfondo al grafico, rendendo più facile leggere visivamente i valori approssimativi dal grafico. Chiamala dopo le tue chiamate a `plt.plot()` ma prima di `plt.show()`. La griglia non influenza i dati o i calcoli — è puramente un aiuto visivo per il lettore.

    **Concept Tested:** Grid Lines

---

#### 8. Cosa fa `plt.savefig("chart.png")`?

<div class="upper-alpha" markdown>
1. Carica un grafico precedentemente salvato da `chart.png`
2. Fa uno screenshot di tutto lo schermo e lo salva
3. Salva il grafico attuale in un file chiamato `chart.png` invece di mostrarlo in una finestra
4. Converte automaticamente il grafico in formato PDF
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `plt.savefig("filename.png")` salva il grafico in un file immagine. Chiamala prima di `plt.show()` (o invece di essa). Puoi salvare come PNG, PDF, SVG, o altri formati cambiando l'estensione del file. Questo è essenziale per includere grafici in report, siti web, o condividere risultati senza richiedere che il destinatario abbia matplotlib installato.

    **Concept Tested:** Saving Figures

---

#### 9. Cosa mostra un grafico a istogramma?

<div class="upper-alpha" markdown>
1. Il cambiamento di una variabile nel tempo
2. La correlazione tra due variabili disegnate come punti individuali
3. La distribuzione di frequenza di un insieme di dati — quanto spesso i valori rientrano in ogni intervallo
4. Un confronto dei totali tra categorie discrete
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un istogramma (creato con `plt.hist()`) mostra quanto frequentemente i valori rientrano in intervalli (chiamati bin). Per esempio, un istogramma dei punteggi degli studenti mostra quanti studenti hanno ottenuto 60-70, 70-80, 80-90, ecc. Rivela la forma della distribuzione dei dati — se è simmetrica, asimmetrica, o ha valori anomali. I grafici a barre confrontano categorie distinte; gli istogrammi mostrano distribuzioni di valori continui.

    **Concept Tested:** Histograms

---

#### 10. Cosa crea `plt.subplots(1, 2)`?

<div class="upper-alpha" markdown>
1. Un grafico con due assi y per confrontare scale diverse
2. Una figura con 1 riga e 2 colonne di pannelli di grafici fianco a fianco
3. Due finestre di grafico separate mostrate sullo schermo contemporaneamente
4. Un singolo grafico con due temi di colore applicati simultaneamente
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `fig, axes = plt.subplots(rows, cols)` crea una figura con una griglia di pannelli di grafici (sottografici). `plt.subplots(1, 2)` crea una riga e due colonne — due grafici fianco a fianco. Poi disegni su ciascuno con `axes[0].plot(...)` e `axes[1].plot(...)`. Questo è come confronti insiemi di dati correlati in una singola figura.

    **Concept Tested:** Subplots

---
