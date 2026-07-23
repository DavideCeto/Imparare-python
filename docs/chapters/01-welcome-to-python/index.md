---
title: Benvenuto in Python e Skulpt
description: Conosci Monty, esegui il tuo primo codice Python nel browser e scopri print(), commenti e grafica tartaruga.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:28:14
version: 0.09
---

# Benvenuto in Python e Skulpt

## Riepilogo

In questo primo capitolo conoscerai **Monty** — la tua guida amichevole serpente python —
e scriverai le tue prime righe di codice Python nella finestra di Skulpt nel browser.
Scoprirai cos'è Python, perché è così popolare, e avrai un'anteprima entusiasmante:
eseguirai `import turtle` e guarderai Monty disegnare una forma proprio sulla pagina.
Alla fine conoscerai come stampare messaggi, scrivere commenti e capire
perché Python è un grande passo dopo Scratch.

## Concetti Coperti

Questo capitolo copre i seguenti 9 concetti dal grafico di apprendimento:

1. Panoramica dell'Interprete Python
2. Ambienti Python Basati su Browser
3. Skulpt Browser Python
4. Funzione print()
5. Commenti su Singola Riga
6. Sensibilità alle Maiuscole
7. Righe Vuote e Leggibilità
8. Istruzione import
9. import turtle

## Prerequisiti

Questo capitolo si basa su concetti da:

Questo è il primissimo capitolo — non hai bisogno di prerequisiti se non la familiarità con Scratch!
Questo capitolo presuppone solo i prerequisiti elencati nella [descrizione del corso](../../course-description.md).

---

Al termine di questa lezione sarai in grado di:

- Eseguire codice Python direttamente nel tuo browser senza installare nulla
- Usare `print()` per visualizzare messaggi sullo schermo
- Scrivere commenti su singola riga per spiegare cosa fa il tuo codice
- Importare la libreria turtle e guardarla disegnare una forma sulla pagina

Hai codificato con blocchi colorati — incastrando pezzi in Scratch per far muovere gli sprite, dire cose e reagire ai clic. Ora è tempo della prossima avventura: scrivere **Python**, uno

!!! mascot-welcome "Ciao! Sono Monty."
    ![Monty che saluta](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Benvenuto in **Imparare Python — Dai Blocchi al Codice**! Sono **Monty**, un amichevole serpente python che vive proprio qui nel tuo libro di testo. Apparirò durante ogni lezione, ma mai casualmente.

    Farò sette cose e solo queste sette cose:

    1. **Darti il benvenuto** all'inizio di ogni lezione — esattamente quello che sto facendo proprio ora.
    2. **Aiutarti a pensare e prevedere** prima di eseguire un programma, così costruisci l'abitudine di ragionare attraverso il codice prima di eseguirlo.
    3. **Darti consigli** — le mosse intelligenti che usano i programmatori esperti e che nessuno si prende la briga di scrivere.
    4. **Ponte verso Scratch** — quando un'idea di Python ha un equivalente diretto in Scratch, collegherò i due così puoi usare quello che già conosci.
    5. **Avvertirti** sui punti dove anche i codificatori attenti inciampano — errori comuni, bug subdoli e regole facili da perdere.
    6. **Incoraggiarti** quando un concetto sembra difficile all'inizio — alcune idee richiedono un momento per fare clic, ed è completamente normale.
    7. **Celebrare con te** alla fine di ogni lezione quando l'hai meritato.

    È tutto. Se non sto facendo una di queste sette cose, non sono nella lezione. Codiamo insieme!

## Cos'è Python?

Scratch usa blocchi colorati che si incastrano. Python usa **testo** — parole e simboli che digiti sulla tastiera. Un **linguaggio di programmazione** è un insieme di regole per scrivere istruzioni che un computer

Quando scrivi un programma Python, qualcosa chiamato **interprete Python** legge il tuo codice una riga alla volta dall'alto verso il basso ed esegue ogni istruzione. Pensa all'interprete come a un

Python è stato inventato nel 1991 da un programmatore di nome Guido van Rossum. L'ha chiamato dopo uno spettacolo comico britannico — non dopo il serpente, anche se la mascotte del serpente si adatta perfettamente! Oggi Python alimenta

## Modi di Eseguire Python

Prima di scrivere la tua prima riga di Python, è utile sapere *dove* Python viene eseguito. Ci sono diverse opzioni, e ognuna ha il suo posto in questo corso.

1. **Direttamente in una Pagina Web** — Usiamo una potente libreria chiamata Skulpt che è integrata direttamente in *questo* libro di testo. Skulpt è una versione di Python che viene eseguita direttamente dentro la pagina web che stai leggendo
L'editor CodeMirror viene anche utilizzato per visualizzare e apportare piccole modifiche ai nostri esempi.  Il limite è che alcune funzioni come leggere e scrivere file dal tuo disco locale non funzionano con
2. **Sul tuo computer in un terminale** — Puoi installare Python ed eseguirlo da una finestra terminale. Così lavorano i programmatori professionisti, ma richiede configurazione e non è dove iniziamo.
3. **Usando uno Strumento di Ambiente di Sviluppo Integrato (IDE)** - Questo è uno strumento come Thonny (consigliato per i principianti), Visual Studio Code o diversi altri strumenti.
4. **Usando un Contenitore (Docker)** - Questo processo avvia ed esegue una piccola macchina virtuale per eseguire Python.  I nostri laboratori intermedi e avanzati usano questo approccio.  Otteniamo un comportamento coerente su tutti
5. **Jupyter Labs** - Questo è l'approccio per molti progetti di data science.  Tuttavia
è più complicato da configurare.

!!! Note
  Le prime versioni di questo libro usavano il sito libero `Thonny` per eseguire i nostri programmi Python.
  Sfortunatamente, Thonny non è più supportato e tutti i laboratori Thonny sono stati convertiti
  per usare i nostri strumenti attuali.

In questo corso, **Skulpt** è il tuo strumento principale per i capitoli iniziali. La tabella sottostante riassume tutti e tre gli ambienti:

| Ambiente | Dove viene eseguito | Ha bisogno di installazione? | Migliore per |
|------------|--------------|---------------|----------|
| Il tuo computer | Terminale locale | Sì | Lavoro professionale |
| Skulpt (questo libro) | Questa pagina web | No | Pratica immediata in lezione |

## La Tua Prima Riga Python: print()

La primissima cosa che imparano la maggior parte dei programmatori è come far visualizzare un messaggio a un programma. In Python, il comando si chiama **`print()`**.

Una **funzione** è un'azione nominata che Python sa come eseguire. `print()` è la funzione "visualizza un messaggio" integrata di Python. Qualunque cosa metti dentro le parentesi — circondate da virgolette

!!! mascot-tip "Ponte verso Scratch"
    ![Monty con un consiglio](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Dire [ ] per 2 secondi"** per far mostrare al tuo sprite una bolla di dialogo. In Python, `print("Ciao!")` fa lo stesso lavoro — fa visualizzare un messaggio al tuo programma.

## Codice di Esempio: print()

Qui c'è un breve programma con tre chiamate `print()`. Leggi attentamente ogni riga prima di eseguirla:

```python
print("Ciao, mondo!")
print("Il mio nome è Monty.")
print("Impariamo Python!")
```

**Prima di fare clic su Esegui:** quante linee di testo pensi appariranno nella casella di output? Fai la tua previsione, poi provalo!

## Provalo Ora

Modifica il codice qui sotto e fai clic su **Esegui** per vedere il risultato proprio su questa pagina. Nessun account necessario — tutto viene eseguito nel tuo browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Esegui</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Ripristina</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `print("Ciao, mondo!")
print("Il mio nome è Monty.")
print("Impariamo Python!")`);
</script>

Avevi ragione? Dovresti vedere tre linee di testo apparire, una per ogni chiamata `print()` — Python le esegue in ordine dall'alto verso il basso.

**Se vedi un messaggio di errore rosso:** Controlla l'ortografia con attenzione. Python è sensibile alle maiuscole, quindi `Print("Ciao")` con una P maiuscola non funzionerà — deve essere `print("Ciao")` in minuscolo. Anche

## Come Funziona print()

Ogni riga `print()` viene eseguita una alla volta, dall'alto del programma al basso — esattamente nello stesso ordine in cui Scratch esegue i blocchi dentro uno script. Quando Python vede `print("Ciao, mondo!")` fa

1. Legge il nome della funzione: `print`
2. Legge il testo dentro le parentesi: `"Ciao, mondo!"`
3. Visualizza quel testo, poi passa alla riga successiva

Le virgolette attorno al testo sono importanti. Dicono a Python che `"Ciao, mondo!"` è un pezzo di testo — quello che i programmatori chiamano una **stringa**. Una stringa è qualsiasi sequenza di caratteri (lettere,

| Riga | Cosa fa |
|------|-------------|
| `print("Ciao, mondo!")` | Visualizza il testo: Ciao, mondo! |
| `print("Il mio nome è Monty.")` | Visualizza il testo: Il mio nome è Monty. |
| `print("Impariamo Python!")` | Visualizza il testo: Impariamo Python! |

## Scrivere Commenti con #

Man mano che i tuoi programmi diventano più lunghi, diventa utile lasciare note per te stesso e per chiunque legga il tuo codice. In Python, un **commento** è una nota che l'interprete ignora completamente quando

Inizi un commento digitando un carattere `#` (chiamato hash o pound). Tutto su quella riga dopo il `#` è trattato come una nota, non come codice.

```python
# Questa riga è un commento — Python la ignora completamente
print("Ma Python esegue questa riga!")

# I commenti spiegano il PERCHÉ dietro il tuo codice
print("Rendono i programmi più facili da leggere.")
```

I buoni programmatori usano i commenti costantemente. Un commento non cambia quello che il programma fa — aiuta solo la prossima persona (spesso tu, sei mesi dopo) a capire quello che stavi pensando.

## Vedi: Passo attraverso un Programma

Hai imparato che Python esegue un programma una riga alla volta, dall'alto verso il basso, e che salta i commenti e le righe vuote. Lo Stepper di Codice sotto ti permette di *guardare* accadere. Prima di fare clic

<iframe src="../../sims/code-stepper/main.html" height="452" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Code Stepper](../../sims/code-stepper/index.md){ .md-button }

Prova il programma **Commenti Ovunque** dal menu a discesa — quante linee pensi verranno stampate? Fai un passo attraverso di esso per scoprire se un `print()` nascosto dentro un commento viene mai eseguito.

## Sensibilità alle Maiuscole

Python è **sensibile alle maiuscole**, il che significa che le lettere maiuscole e minuscole sono trattate come cose completamente diverse. Il comando `print` e la parola `Print` non sono la stessa cosa.

!!! mascot-warning "Le Lettere Maiuscole Contano!"
    ![Monty avverte](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Uno degli errori più comuni della prima settimana è digitare `Print("Ciao")` con una P maiuscola. Python risponderà con un messaggio `NameError: name 'Print' is not defined`. La soluzione è semplice: scrivi sempre

## Le Righe Vuote Rendono il Codice Leggibile

Python non si preoccupa delle righe vuote — puoi aggiungere quante righe vuote desideri tra le istruzioni e l'interprete le ignora tutte. Ma i *lettori umani* se ne preoccupano molto.

Le righe vuote dividono il tuo codice in gruppi logici, lo stesso modo in cui le interruzioni di paragrafo dividono una storia in scene. Due righe di codice che fanno lo stesso compito appartengono insieme; due righe che fanno compiti diversi

```python
# --- Introduzione ---
print("Benvenuto nel mio programma!")
print("Iniziamo.")

# --- Messaggio principale ---
print("Python è divertente da imparare.")
print("Stai facendo bene!")
```

Abituati presto: se due blocchi di codice fanno compiti diversi, separali con una riga vuota. I tuoi programmi saranno molto più facili da leggere — e da correggere quando qualcosa va male.

## Importare Librerie con import

Una delle più grandi forze di Python è la sua enorme collezione di strumenti già costruiti. Puoi portare qualsiasi di questi strumenti nel tuo programma con un'**istruzione `import`**.

La parola chiave `import` dice all'interprete Python: "Ho bisogno di questo toolkit extra — per favore caricalo prima di eseguire il resto del mio programma." Di per sé Python sa come fare molte cose (`print`, basis

Un'istruzione import va sempre molto **in alto** nel tuo programma — prima di qualsiasi altro codice — così Python carica la libreria prima di averne bisogno.

```python
import turtle   # Carica la libreria turtle
```

Dopo quella riga, tutto nella libreria turtle è disponibile al tuo programma.

## Disegnare con import turtle

La libreria **turtle** ti permette di disegnare immagini spostando una penna virtuale intorno allo schermo. Immagina una piccola tartaruga che tiene una penna. Quando dici alla tartaruga `forward(100)`, cammina avanti 100 passi e

Ogni programma turtle inizia nello stesso modo:

```python
import turtle
t = turtle.Turtle()
```

La prima riga carica la libreria. La seconda riga crea una tartaruga e le dà il nome `t`. Una volta che hai una tartaruga, la dirigi usando la notazione del punto — `t.forward(100)` significa "dì alla tartaruga `t` di

## Codice di Esempio: Disegno di una Forma

Qui c'è un breve programma turtle. Chiama `forward(100)` e `right(90)` diverse volte di seguito:

```python
import turtle

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
```

!!! mascot-thinking "Quale Forma Disegnerà Monty?"
    ![Monty pensa](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda il programma qui sopra. La tartaruga chiama `forward(100)` quattro volte e `right(90)` tre volte nel mezzo. Il numero 90 è il numero di gradi in ogni curva verso destra. Quanti lati avrà il

## Prova: Grafica Tartaruga

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Esegui</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Ripristina</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `import turtle

t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)`);
</script>

Avevi ragione? La tartaruga disegna un **quadrato** — quattro lati di lunghezza uguale con una curva verso destra di 90 gradi tra ogni lato. Quattro curve di 90 gradi si sommano a 360 gradi, che è una rotazione completa

## Come Funziona il Programma Tartaruga

Tracciamo ogni riga:

| Riga | Cosa fa |
|------|-------------|
| `import turtle` | Carica la libreria di grafica tartaruga |
| `t = turtle.Turtle()` | Crea una nuova tartaruga e le dà il nome `t` |
| `t.forward(100)` | Muove `t` in avanti 100 passi, disegnando una linea |
| `t.right(90)` | Gira `t` in senso orario di 90 gradi |

Il numero dentro `forward()` controlla quanto lontano cammina la tartaruga — numeri più grandi disegnano linee più lunghe. Il numero dentro `right()` controlla quanto bruscamente la tartaruga gira — 90 gradi crea un quadrato

## Controllo di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Completa il Triangolo!"
    ![Monty pensa](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sottostante disegna **due lati** di un triangolo e poi si ferma. Un triangolo ha tre lati uguali, con una curva verso destra di 120 gradi ad ogni angolo. Aggiungi **una riga** — `t.forward(100)` — e

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Esegui</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Ripristina</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `import turtle

t = turtle.Turtle()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
# Aggiungi una riga qui per completare il triangolo!`);
</script>

Quando aggiungi la riga mancante e fai clic su Esegui, la tartaruga dovrebbe disegnare un triangolo chiuso. Se la forma non si chiude, doppio controllo che la tua riga aggiunta scriva `forward` in minuscolo e usi pa

## Esperimenti

Prova questi cambiamenti ai programmi sopra. Per ognuno, **prevedi cosa accadrà prima** — poi eseguilo per controllare!

1. **Cambia un messaggio in `print()`**. Sostituisci `"Ciao, mondo!"` con il tuo nome, come `print("Ciao, sono Alex!")`. **Saprai che ha funzionato quando** il tuo nome appare nella casella di output.

2. **Aggiungi una quarta riga `print()`** con un messaggio di tua scelta. **Saprai che ha funzionato quando** quattro linee di testo appaiono nell'output, non tre.

3. **Cambia `forward(100)` nel quadrato in `forward(200)`**. **Saprai che ha funzionato quando** il quadrato è il doppio della larghezza e dell'altezza.

4. **Disegna una forma diversa**: cambia il programma del quadrato per usare `right(60)` e ripeti `forward(100)` e `right(60)` sei volte. **Saprai che ha funzionato quando** vedi un esagono a sei lati.

5. **Sfida — cambia la velocità**: aggiungi la riga `t.speed(1)` subito dopo `t = turtle.Turtle()` nel programma del quadrato. Eseguilo e osserva cosa accade. Poi prova `t.speed(10)`. **Saprai che ha

!!! mascot-celebration "Fantastici Lavori!"
    ![Monty celebra](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena scritto i tuoi primissimi programmi Python — e hanno davvero funzionato! Hai usato `print()` per visualizzare messaggi, `#` per scrivere commenti, `import` per caricare una libreria, e `import turtle` per disegnare

[Fai il Quiz di Revisione del Capitolo](./quiz.md)

[Vedi Riferimenti Annotati](./references.md)
