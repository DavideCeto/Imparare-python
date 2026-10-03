---
title: "Learning Python"
description: "Un libro di testo intelligente e interattivo per imparare Python con esercizi di codice guidati da una mascotte amichevole"
image: img/cover.png
---
# Learning Python
![](./img/cover.png)

!!! mascot-welcome "Benvenuto/a da Monty!"
    ![Monty welcoming you](./img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ciao! Sono Monty, il tuo amichevole serpente-guida Python. Sarò con te a ogni passo
    mentre impari a scrivere vero codice Python — proprio qui nel tuo browser, senza
    bisogno di installare nulla. Andiamo!

**Beginning Python — From Blocks to Code with Monty** è un libro di testo intelligente e
interattivo per studenti dai 10 ai 13 anni pronti a passare dalla programmazione a blocchi
(come Scratch) al vero codice Python testuale. Ogni lezione include finestre di codice dal
vivo basate su **Skulpt** — un motore Python che funziona direttamente nel tuo browser,
così puoi leggere, eseguire e modificare il codice all'istante in ogni pagina.

## Imparare Python con Skulpt

L'ambiente di programmazione principale usato in tutto questo libro è **Skulpt** — una
implementazione JavaScript di Python che funziona interamente nel tuo browser. Nessun
account, nessun download, nessuna installazione. Ogni capitolo include uno o più
laboratori Skulpt incorporati dove puoi:

1. **Leggere** un breve programma Python funzionante
2. **Eseguirlo** immediatamente cliccando sul pulsante Run
3. **Modificarlo** — cambiando un numero, un colore, una direzione — ed eseguirlo di nuovo

Skulpt supporta nativamente le **grafiche turtle**, dando agli studenti un riscontro
visivo immediato mentre disegnano forme, spirali, fiori e frattali. L'area di disegno
appare subito sotto l'editor di codice, così chi impara vede il risultato del proprio
programma nel momento stesso in cui clicca su Run.

Provalo subito tu stesso/a — clicca su **Run** per vedere la tartaruga disegnare un
esagono colorato, poi cambia i colori, il numero di lati o la distanza ed eseguilo di nuovo:

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="js/codemirror-lab.js"></script>

<div class="cm-lab">
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
initCmLab('', `import turtle
t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    t.pencolor(colors[i])
    t.forward(100)
    t.right(60)`);
</script>

Questo programma di sette righe disegna un esagono colorato — e cambiare `6` in `5` o
`100` in `150` richiede un secondo e insegna più di quanto potrebbe mai fare un paragrafo
di spiegazione.

## Imparare Python con i Jupyter Notebook

I [Jupyter Notebook](https://jupyter.org/) sono lo strumento preferito dai professionisti
della data science e un ottimo passo successivo dopo questo libro. Supportano le grafiche
turtle (aprendo una finestra di disegno separata) e danno agli studenti accesso a decine
di migliaia di notebook di esempio scritti dalla community. Jupyter è ideale per gli
studenti che si avvicinano alla visualizzazione dati, a NumPy e al machine learning.

## Imparare Python con Raspberry Pi

La [Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/usage/python/)
ha scelto Python come linguaggio principale per il physical computing sul Pi. Se hai un
Raspberry Pi, Python funziona nativamente e tutte le librerie standard — turtle,
matplotlib e persino Keras — funzionano senza configurazioni aggiuntive. Il Pi è
un'ottima piattaforma per robotica, sensori e progetti maker una volta che gli studenti
hanno acquisito familiarità con il linguaggio di base insegnato in questo libro.

## Struttura del corso

Questo libro copre **38 capitoli** e circa **450 concetti**, procedendo dalla prima
riga di Python di uno studente fino alle reti neurali e al dataset di cifre scritte a
mano MNIST:

| Livello | Capitoli | Argomenti |
|---|---|---|
| **Iniziale** | 1–18 | Grafiche turtle, variabili, cicli, funzioni, stringhe, liste, moduli |
| **Intermedio** | 19–29 | Booleani, dizionari, OOP, I/O su file, ricorsione, espressioni regolari |
| **Avanzato** | 30–38 | Algoritmi, strutture dati, matplotlib, NumPy, elaborazione immagini, ML |

## Concetti chiave

Ecco alcune delle idee di programmazione che imparerai lungo il percorso:

- **Importare librerie** — dire a Python di quali strumenti ha bisogno il tuo programma
- **Grafiche turtle** — disegnare forme, spirali, fiori e frattali con riscontro visivo
- **Variabili** — dare nomi ai valori per rendere i programmi più facili da leggere e modificare
- **Cicli** — ripetere azioni con `for` e `while` senza copiare il codice
- **Condizionali** — prendere decisioni con `if`, `elif` ed `else`
- **Funzioni** — suddividere i programmi in parti nominate e riutilizzabili
- **Parametri e valori di ritorno** — rendere le funzioni flessibili e componibili
- **Numeri casuali** — aggiungere elementi di casualità e varietà a disegni e giochi
- **Liste e dizionari** — memorizzare e organizzare collezioni di dati
- **Ricorsione** — funzioni che richiamano se stesse per costruire frattali e risolvere labirinti
- **Programmazione orientata agli oggetti** — modellare il mondo con classi e oggetti
- **Visualizzazione dati** — rappresentare graficamente i dati con matplotlib
- **Machine learning** — addestrare una rete neurale a riconoscere cifre scritte a mano

## Pubblico di riferimento

Questo libro è ideale per studenti con buone capacità di digitazione che hanno completato
almeno un semestre di programmazione a blocchi (Scratch, Snap! o simili).
Non è richiesta alcuna precedente esperienza di programmazione testuale.

Se uno studente non è ancora a proprio agio con la tastiera, consigliamo di iniziare
prima con [Scratch](https://scratch.mit.edu/) e tornare qui quando sarà pronto.

## Contribuire

Hai un esempio che vorresti condividere con altri studenti e insegnanti?
Consulta la pagina [Contribuire](teachers-guide/contribute.md) per i dettagli su come
inviare il tuo codice.

!!! mascot-celebration "Sei nel posto giusto!"
    ![Monty celebrating](./img/mascot/celebration.png){ class="mascot-admonition-img" }
    Centinaia di studenti hanno usato questo libro per scrivere il loro primo programma
    Python. Scegli un capitolo dalla barra laterale e inizia a programmare — sarò proprio
    lì con te!
