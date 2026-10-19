---
title: Benvenuto in Python e Skulpt
description: Incontra Monty, esegui il tuo primo codice Python nel browser e scopri print(), i commenti e la grafica turtle.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:28:14
version: 0.09
---

# Benvenuto in Python e Skulpt

## Riepilogo

In questo primo capitolo incontrerai **Monty** — la tua amichevole guida python-serpente —
e scriverai le tue primissime righe di codice Python dentro la finestra del browser di Skulpt.
Scoprirai cos'è Python, perché è così popolare, e avrai un'anteprima emozionante:
eseguirai `import turtle` e vedrai Monty disegnare una forma proprio sulla pagina.
Alla fine saprai come stampare messaggi, scrivere commenti, e capirai
perché Python è un ottimo passo successivo dopo Scratch.

## Concetti Trattati

Questo capitolo tratta i seguenti 9 concetti del grafo di apprendimento:

1. Python Interpreter Overview
2. Browser-Based Python Environments
3. Skulpt Browser Python
4. print() Function
5. Single-Line Comments
6. Case Sensitivity
7. Blank Lines and Readability
8. import Statement
9. import turtle

## Prerequisiti

Questo capitolo si basa sui concetti di:

Questo è proprio il primo capitolo — non servono prerequisiti oltre alla familiarità con Scratch!
Questo capitolo presuppone solo i prerequisiti elencati nella [descrizione del corso](../../course-description.md).

---

Alla fine di questa lezione sarai in grado di:

- Eseguire codice Python direttamente nel tuo browser senza installare nulla
- Usare `print()` per mostrare messaggi sullo schermo
- Scrivere commenti su una riga per spiegare cosa fa il tuo codice
- Importare la libreria turtle e vederla disegnare una forma sulla pagina

Finora hai programmato con blocchi colorati — incastrando pezzi in Scratch per far muovere gli sprite, farli parlare e farli reagire ai clic. Ora è il momento della prossima avventura: scrivere **Python**, uno dei linguaggi di programmazione più popolari al mondo. La buona notizia? Tutto quello che già sai da Scratch funziona ancora — solo che in Python ha un aspetto un po' diverso.

!!! mascot-welcome "Ciao! Sono Monty."
    ![Monty waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Benvenuto in **Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty**! Sono **Monty**, un amichevole serpente python che vive proprio qui nel tuo libro di testo. Comparirò in ogni lezione, ma mai a caso — ho esattamente **sette compiti**, e imparerai presto a riconoscermi in base a quale sto svolgendo:

    1. **Darti il benvenuto** all'inizio di ogni lezione — esattamente quello che sto facendo ora.
    2. **Aiutarti a pensare e prevedere** prima di eseguire un programma, così da costruire l'abitudine di ragionare sul codice prima di farlo girare.
    3. **Darti consigli** — le mosse intelligenti che i programmatori esperti usano e che nessuno si prende la briga di scrivere.
    4. **Fare da ponte con Scratch** — ogni volta che un'idea di Python ha un corrispettivo diretto in Scratch, li collegherò così potrai usare quello che già sai.
    5. **Avvisarti** dei punti in cui anche i programmatori attenti inciampano — errori comuni, bug subdoli e regole facili da perdere.
    6. **Incoraggiarti** quando un concetto sembra difficile all'inizio — alcune idee richiedono un momento per essere capite, ed è del tutto normale.
    7. **Festeggiare con te** alla fine di ogni lezione, quando te lo sarai meritato.

    Questo è tutto. Se non sto facendo una di queste sette cose, non sono nella lezione. Programmiamo insieme!

## Cos'è Python?

Scratch usa blocchi colorati che si incastrano tra loro. Python usa il **testo** — parole e simboli che digiti sulla tastiera. Un **linguaggio di programmazione** è un insieme di regole per scrivere istruzioni che un computer può seguire. Python è uno di questi linguaggi, ed è una scelta eccellente perché si legge quasi come l'inglese comune.

Quando scrivi un programma Python, qualcosa chiamato **interprete Python** legge il tuo codice una riga alla volta, dall'alto verso il basso, ed esegue ogni istruzione. Pensa all'interprete come a un lettore velocissimo che trasforma le tue parole in azioni. In Scratch, cliccare sulla bandierina verde avviava il tuo programma. In Python, l'interprete fa lo stesso lavoro — parte dalla primissima riga e prosegue verso il basso.

Python è stato inventato nel 1991 da un programmatore di nome Guido van Rossum. Gli ha dato questo nome in onore di uno show comico britannico — non del serpente, anche se la mascotte-serpente ci sta benissimo! Oggi Python fa funzionare YouTube, Instagram, i robot della NASA e la ricerca sull'intelligenza artificiale. È costantemente considerato il primo linguaggio di programmazione più popolare al mondo, sia per i principianti che per i professionisti.

## Modi per Eseguire Python

Prima di scrivere la tua prima riga di Python, è utile sapere *dove* funziona Python. Ci sono diverse opzioni, e ognuna ha il suo posto in questo corso.

1. **Direttamente in una Pagina Web** — Usiamo una potente libreria chiamata Skulpt, integrata proprio in *questo* libro di testo. Skulpt è una versione di Python che funziona direttamente dentro la pagina web che stai leggendo in questo momento. Ogni finestra di codice interattiva nei Capitoli 1–18 è alimentata da Skulpt. Non serve aprire una nuova scheda, accedere con un account o installare nulla. Clicchi su **Run** e il codice viene eseguito qui, sulla pagina.
L'editor di codice CodeMirror viene usato anche per mostrare e apportare piccole modifiche ai nostri esempi. Il limite è che alcune funzioni, come leggere e scrivere file dal tuo disco locale, non funzionano con l'approccio nel browser.
2. **Sul tuo computer, in un terminale** — Puoi installare Python ed eseguirlo da una finestra di terminale. È così che lavorano i programmatori professionisti, ma richiede una configurazione iniziale e non è da qui che partiamo.
3. **Usando un ambiente di sviluppo integrato (IDE)** - È uno strumento come Thonny (consigliato per i principianti), Visual Studio Code o diversi altri strumenti.
4. **Usando un Container (Docker)** - Questo processo avvia ed esegue una piccola macchina virtuale per far funzionare Python. I nostri laboratori Intermediate e Advanced usano questo approccio. Otteniamo un comportamento coerente su tutti i sistemi, ma devi eseguire il libro di testo sul tuo computer locale oppure avere un runner Docker configurato per la tua scuola. Puoi vedere il programma che lo avvia nei nostri script su GitHub.
5. **Jupyter Labs** - Questo è l'approccio usato in molti progetti di data science. Tuttavia è più complicato da configurare.

!!! Note
  Le prime versioni di questo libro usavano il sito web gratuito `Thonny` per eseguire i nostri programmi Python.
  Purtroppo Thonny non è più supportato e tutti i laboratori Thonny sono stati convertiti
  per usare i nostri strumenti attuali.

In questo corso, **Skulpt** è il tuo strumento principale per i primi capitoli. La tabella seguente riassume tutti e tre gli ambienti:

| Ambiente | Dove funziona | Richiede installazione? | Ideale per |
|------------|--------------|---------------|----------|
| Il tuo computer | Terminale locale | Sì | Lavoro professionale |
| Skulpt (questo libro) | Questa pagina web | No | Pratica immediata durante la lezione |

## La Tua Prima Riga Python: print()

La primissima cosa che la maggior parte dei programmatori impara è come far mostrare un messaggio a un programma. In Python, il comando si chiama **`print()`**.

Una **funzione** è un'azione con un nome che Python sa eseguire. `print()` è la funzione integrata di Python per “mostrare un messaggio”. Qualunque cosa metti dentro le parentesi — circondata da virgolette — appare nell'area di output quando il programma viene eseguito.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch usavi il blocco **“Dì [ ] per 2 secondi”** per far mostrare al tuo sprite un fumetto. In Python, `print("Ciao!")` fa lo stesso lavoro — fa mostrare un messaggio al tuo programma. La differenza è che Python mostra il messaggio come testo semplice sotto il codice, non come un fumetto su un personaggio.

## Codice di Esempio: print()

Ecco un breve programma con tre chiamate a `print()`. Leggi attentamente ogni riga prima di eseguirlo:

```python
print("Ciao, mondo!")
print("Mi chiamo Monty.")
print("Impariamo Python!")
```

**Prima di cliccare su Run:** quante righe di testo pensi appariranno nel riquadro di output? Fai la tua previsione, poi prova!

## Provalo Ora

Modifica il codice qui sotto e clicca su **Run** per vedere il risultato direttamente su questa pagina. Non serve alcun account — tutto funziona nel tuo browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

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
initCmLab('', `print("Ciao, mondo!")
print("Mi chiamo Monty.")
print("Impariamo Python!")`);
</script>

Avevi ragione? Dovresti vedere apparire tre righe di testo, una per ogni chiamata a `print()` — Python le esegue in ordine dall'alto verso il basso.

**Se vedi un messaggio di errore rosso:** controlla attentamente l'ortografia. Python distingue tra maiuscole e minuscole, quindi `Print("Hello")` con la P maiuscola non funziona — deve essere `print("Hello")` tutto minuscolo. Assicurati anche di avere sia una `"` di apertura che una `"` di chiusura intorno al tuo testo.

## Come Funziona print()

Ogni riga `print()` viene eseguita una alla volta, dall'inizio del programma fino alla fine — esattamente lo stesso ordine con cui Scratch esegue i blocchi dentro uno script. Quando Python incontra `print("Ciao, mondo!")`, fa tre cose:

1. Legge il nome della funzione: `print`
2. Legge il testo dentro le parentesi: `"Ciao, mondo!"`
3. Mostra quel testo, poi passa alla riga successiva

Le virgolette intorno al testo sono importanti. Dicono a Python che `"Ciao, mondo!"` è un pezzo di testo — quella che i programmatori chiamano una **stringa**. Una stringa è una qualsiasi sequenza di caratteri (lettere, numeri, spazi, punteggiatura) racchiusa tra virgolette. Senza le virgolette, Python penserebbe che stai scrivendo il nome di una variabile o un comando che non riconosce.

| Riga | Cosa fa |
|------|-------------|
| `print("Ciao, mondo!")` | Mostra il testo: Ciao, mondo! |
| `print("Mi chiamo Monty.")` | Mostra il testo: Mi chiamo Monty. |
| `print("Impariamo Python!")` | Mostra il testo: Impariamo Python! |

## Scrivere Commenti con \#

Man mano che i tuoi programmi crescono, diventa utile lasciare delle note per te stesso e per chiunque altro legga il tuo codice. In Python, un **commento** è una nota che l'interprete ignora completamente quando esegue il programma — esiste solo per i lettori umani.

Un commento si avvia digitando il carattere `#` (chiamato cancelletto). Tutto ciò che si trova su quella riga dopo il `#` viene considerato una nota, non codice.

```python
# Questa riga è un commento — Python la ignora completamente
print("Ma Python esegue questa riga!")

# I commenti spiegano il PERCHÉ del tuo codice
print("Rendono i programmi più facili da leggere.")
```

I bravi programmatori usano i commenti di continuo. Un commento non cambia cosa fa il programma — aiuta semplicemente la prossima persona (spesso tu stesso, sei mesi dopo) a capire cosa stavi pensando.

## Guardalo: Esegui un Programma Passo Passo

Hai imparato che Python esegue un programma una riga alla volta, dall'alto verso il basso, e che salta i commenti e le righe vuote. Il Code Stepper qui sotto ti permette di *osservare* tutto questo. Prima di cliccare su qualsiasi cosa, guarda il programma a sinistra e **prevedi esattamente cosa mostrerà il pannello di output quando il programma avrà finito**. Poi clicca su **Next Step** per verificare la tua previsione una riga alla volta.

<iframe src="../../sims/code-stepper/main.html" height="452" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Code Stepper](../../sims/code-stepper/index.md){ .md-button }

Prova il programma **Comments Everywhere** dal menu a tendina — quante righe pensi verranno stampate? Esegui il programma passo passo per scoprire se un `print()` nascosto dentro un commento viene mai eseguito.

## Distinzione tra Maiuscole e Minuscole

Python è **case-sensitive** (distingue tra maiuscole e minuscole), il che significa che le lettere maiuscole e minuscole vengono trattate come cose completamente diverse. Il comando `print` e la parola `Print` non sono la stessa cosa.

!!! mascot-warning "Le Maiuscole Contano!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Uno degli errori più comuni della prima settimana è digitare `Print("Hello")` con la P maiuscola. Python risponderà con un messaggio `NameError: name 'Print' is not defined`. La soluzione è semplice: usa sempre `print()` minuscolo. Questa regola si applica a ogni comando Python — `Forward` non è la stessa cosa di `forward`, e `Turtle` (T maiuscola) si riferisce a qualcosa di diverso da `turtle` (t minuscola). Quando impari un nuovo comando, controlla sempre bene le maiuscole e le minuscole.

## Le Righe Vuote Rendono il Codice Leggibile

A Python non importa delle righe vuote — puoi aggiungere tutte le righe vuote che vuoi tra le istruzioni e l'interprete le ignora tutte. Ma ai *lettori umani* importa eccome.

Le righe vuote dividono il tuo codice in gruppi logici, proprio come gli a capo dividono una storia in scene. Due righe di codice che svolgono lo stesso compito vanno tenute insieme; due righe che svolgono compiti diversi vanno separate da una riga vuota (ed eventualmente un'etichetta di commento).

```python
# --- Introduzione ---
print("Benvenuto nel mio programma!")
print("Cominciamo.")

# --- Messaggio principale ---
print("Python è divertente da imparare.")
print("Stai andando alla grande!")
```

Prendi l'abitudine fin da subito: se due pezzi di codice svolgono compiti diversi, separali con una riga vuota. I tuoi programmi saranno molto più facili da leggere — e da correggere quando qualcosa va storto.

## Importare Librerie con import

Uno dei più grandi punti di forza di Python è la sua enorme collezione di strumenti già pronti. Puoi portare uno qualsiasi di questi strumenti nel tuo programma con un'**istruzione `import`**.

La parola chiave `import` dice all'interprete Python: “Mi serve questo set di strumenti extra — per favore caricalo prima di eseguire il resto del mio programma.” Da solo Python sa fare molte cose (`print`, matematica di base e altro), ma librerie come `turtle`, `random` e `math` devono essere importate prima di poterle usare.

Un'istruzione import va sempre proprio in **cima** al tuo programma — prima di qualsiasi altro codice — così Python carica la libreria prima che ne abbia bisogno.

```python
import turtle   # Carica la libreria turtle
```

Dopo quella singola riga, tutto ciò che si trova nella libreria turtle è disponibile per il tuo programma.

## Disegnare con import turtle

La libreria **turtle** ti permette di disegnare immagini muovendo una penna virtuale sullo schermo. Immagina una piccola tartaruga che tiene in mano una penna. Quando dici alla tartaruga `forward(100)`, questa cammina in avanti per 100 passi e disegna una linea mentre si muove. Quando le dici `right(90)`, ruota di 90 gradi in senso orario.

Ogni programma turtle inizia allo stesso modo:

```python
import turtle
t = turtle.Turtle()
```

La prima riga carica la libreria. La seconda riga crea una tartaruga e le dà il nome `t`. Una volta che hai una tartaruga, la comandi usando la notazione col punto — `t.forward(100)` significa “dì alla tartaruga `t` di andare avanti di 100 passi”.

## Codice di Esempio: Disegnare una Forma

Ecco un breve programma turtle. Chiama `forward(100)` e `right(90)` diverse volte di seguito:

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

!!! mascot-thinking "Che Forma Disegnerà Monty?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda il programma qui sopra. La tartaruga chiama `forward(100)` quattro volte e `right(90)` tre volte nel mezzo. Il numero 90 è il numero di gradi di ogni giro a destra. Quanti lati avrà la forma finita, e come si chiama quella forma? Fai la tua ipotesi — poi clicca su Run per scoprirlo!

## Provalo: Grafica Turtle

<div class="cm-lab">
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

Avevi ragione? La tartaruga disegna un **quadrato** — quattro lati di uguale lunghezza con una rotazione di 90 gradi a destra tra un lato e l'altro. Quattro rotazioni di 90 gradi fanno 360 gradi in totale, cioè un giro completo, quindi la tartaruga finisce per guardare nella stessa direzione in cui aveva iniziato.

## Come Funziona il Programma Turtle

Analizziamo ogni riga:

| Riga | Cosa fa |
|------|-------------|
| `import turtle` | Carica la libreria di grafica turtle |
| `t = turtle.Turtle()` | Crea una nuova tartaruga e la chiama `t` |
| `t.forward(100)` | Muove `t` in avanti di 100 passi, disegnando una linea |
| `t.right(90)` | Ruota `t` in senso orario di 90 gradi |

Il numero dentro `forward()` controlla quanto lontano cammina la tartaruga — numeri più grandi disegnano linee più lunghe. Il numero dentro `right()` controlla quanto bruscamente gira la tartaruga — 90 gradi crea un angolo quadrato. Cambiare questi due numeri è il modo in cui disegni forme diverse.

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Completa il Triangolo!"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna **due lati** di un triangolo e poi si ferma. Un triangolo ha tre lati uguali, con una rotazione di 120 gradi a destra a ogni angolo. Aggiungi **una riga** — `t.forward(100)` — per disegnare il terzo lato mancante e chiudere il triangolo!

<div class="cm-lab">
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
initCmLab('-3', `import turtle

t = turtle.Turtle()
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
# Aggiungi qui una riga per completare il triangolo!`);
</script>

Quando aggiungi la riga mancante e clicchi su Run, la tartaruga dovrebbe disegnare un triangolo chiuso. Se la forma non si chiude, controlla che la riga che hai aggiunto scriva `forward` tutto minuscolo e usi le parentesi con il numero 100 dentro.

## Esperimenti

Prova queste modifiche ai programmi qui sopra. Per ognuna, **prevedi prima cosa succederà** — poi eseguila per verificare!

1. **Cambia un messaggio in `print()`**. Sostituisci `"Ciao, mondo!"` con il tuo nome, come `print("Ciao, sono Alex!")`. **Saprai che ha funzionato quando** il tuo nome apparirà nel riquadro di output.

2. **Aggiungi una quarta riga `print()`** con un messaggio a tua scelta. **Saprai che ha funzionato quando** appariranno quattro righe di testo nell'output, non tre.

3. **Cambia `forward(100)` nel quadrato in `forward(200)`**. **Saprai che ha funzionato quando** il quadrato sarà due volte più largo e alto.

4. **Disegna una forma diversa**: modifica il programma del quadrato per usare `right(60)` e ripeti `forward(100)` e `right(60)` sei volte. **Saprai che ha funzionato quando** vedrai un esagono a sei lati.

5. **Sfida — cambia la velocità**: aggiungi la riga `t.speed(1)` subito dopo `t = turtle.Turtle()` nel programma del quadrato. Eseguilo e osserva cosa succede. Poi prova `t.speed(10)`. **Saprai che ha funzionato quando** la velocità di disegno cambierà visibilmente tra le due esecuzioni.

!!! mascot-celebration "Lavoro Fantastico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena scritto i tuoi primissimi programmi Python — e hanno davvero funzionato! Hai usato `print()` per mostrare messaggi, `#` per scrivere commenti, `import` per caricare una libreria, e `import turtle` per disegnare una forma sullo schermo. Sono nove concetti completamente nuovi in un solo capitolo, e li hai gestiti tutti quanti. Ce la puoi fare — continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
