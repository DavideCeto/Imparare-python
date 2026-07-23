---
title: Struttura del Codice Python
description: Scopri come Python usa l'indentazione per raggruppare il codice, scopri le parole chiave Python e aggiungi colori denominati ai tuoi disegni tartaruga.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:35:09
version: 0.09
---

# Struttura del Codice Python

## Riepilogo

Python ha un aspetto molto pulito: invece di parentesi graffe o parole chiave `begin/end`,
usa l'**indentazione** (spazi) per raggruppare le righe di codice insieme.
Questo capitolo esplora queste regole — indentazione, blocchi di codice, istruzioni,
spazi bianchi — più le parole chiave Python e i colori denominati che userai con tartaruga.

## Concetti Coperti

Questo capitolo copre i seguenti 7 concetti dal grafico di apprendimento:

1. Stringhe Multi-Riga
2. Indentazione come Sintassi
3. Parole Chiave Python
4. Struttura del Blocco di Codice
5. Istruzione vs Espressione
6. Regole di Spazio Bianco
7. Colori Denominati

## Prerequisiti

Questo capitolo si basa su concetti da:

- [Capitolo 1: Benvenuto in Python e Skulpt](../01-welcome-to-python/index.md)

---

Al termine di questa lezione sarai in grado di:

- Scrivere testo multi-riga usando virgolette triple
- Spiegare perché Python usa l'indentazione per raggruppare le righe di codice insieme
- Riconoscere le parole chiave Python e capire perché non possono essere usate come nomi di variabili
- Usare colori denominati come `"rosso"` e `"verde forestale"` nei programmi di grafica tartaruga

Nel Capitolo 1 hai scritto le tue prime righe Python: `print()`, commenti e un disegno tartaruga. Ora sei pronto a guardare come Python è *strutturato* — le regole che governano come il codice è disposto su

!!! mascot-welcome "Bentornato, Codificatore!"
    ![Monty saluta il benvenuto](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto ad andare più a fondo? Questo capitolo riguarda come il codice Python è organizzato — e le regole sono più semplici di quanto potresti pensare. Alla fine renderai anche i tuoi disegni tartaruga molto più color

## Stringhe Multi-Riga

Nel Capitolo 1 hai usato `print()` per visualizzare il testo circondato da virgolette doppie, come `"Ciao, mondo!"`. Funziona bene per messaggi brevi su una riga. Ma cosa succede se vuoi scrivere diverse righe di

Python risolve questo con una **stringa multi-riga** — una stringa che si estende su più righe, creata racchiudendo il testo in **virgolette triple**: tre virgolette doppie (`"""`) o tre virgolette singole

```python
haiku = """Un vecchio stagno silenzioso.
Una rana salta nello stagno.
Spruzz! Silenzio di nuovo."""
print(haiku)
```

**Prima di fare clic su Esegui:** quante linee pensi appariranno nell'output? Conta le interruzioni di riga dentro le virgolette triple per fare la tua previsione!

## Provalo: Stringhe Multi-Riga

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
initCmLab('', `haiku = """Un vecchio stagno silenzioso.
Una rana salta nello stagno.
Spruzz! Silenzio di nuovo."""
print(haiku)`);
</script>

Avevi ragione? Tre righe appaiono — una per ogni riga dentro le virgolette triple. La variabile `haiku` contiene tutte e tre le righe come una singola stringa, e `print()` le visualizza tutte in una volta con il l

## Come Funzionano le Stringhe Multi-Riga

Una stringa regolare usa un paio di virgolette: `"Ciao"`. Una stringa multi-riga usa tre paia: `"""Ciao"""`. Le virgolette triple dicono a Python: "continua a leggere finché non vedi altre tre virgolette — non importa

| Sintassi | Può estendersi su più righe? | Esempio |
|--------|-------------------------|----------|
| `"testo"` | No — una riga sola | `"Ciao, mondo!"` |
| `'testo'` | No — una riga sola | `'Ciao, mondo!'` |
| `"""testo"""` | Sì | `"""Riga uno\nRiga due"""` |
| `'''testo'''` | Sì | `'''Riga uno\nRiga due'''` |

Le stringhe multi-riga sono utili per scrivere poesie, paragrafi o qualsiasi blocco di testo che vuoi mantenere insieme in una variabile.

## Indentazione come Sintassi

La maggior parte dei linguaggi di programmazione usa **parentesi graffe** `{ }` o le parole `inizio` e `fine` per mostrare che le righe di codice appartengono insieme. Python fa qualcosa di diverso — usa l'**indentazione**: il n

**Indentazione** significa premere la barra spaziatrice (o il tasto Tab) prima di una riga di codice per spingerla a destra. In Python, l'indentazione non è solo per aspetto — è parte della grammatica del linguaggio

!!! mascot-tip "Ponte verso Scratch"
    ![Monty con un consiglio](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, metti i blocchi *dentro* un altro blocco (come un blocco Repeat) trascinandoli in modo che si incastrino insieme dentro. In Python, metti le righe *dentro* un gruppo **indentandole** — a

Ecco un'anteprima di come appare l'indentazione in azione. Non hai ancora imparato i cicli `for` — questo è il Capitolo 7 — ma guarda il modello di spaziatura adesso:

```python
# ANTEPRIMA — imparerai i cicli for nel Capitolo 7
# Per ora, nota solo il modello di indentazione

for i in range(4):   # Questa riga inizia al margine sinistro
    t.forward(100)   # Queste due righe sono indentate 4 spazi
    t.right(90)      # Appartengono DENTRO il ciclo for
```

Le due righe con 4 spazi prima sono *dentro* il ciclo. La riga `for` stessa è al margine sinistro. Quella differenza nella spaziatura è quello che Python usa per sapere quali righe fanno parte del ciclo

!!! mascot-warning "IndentationError — L'Errore Python Più Comune"
    ![Monty avverte](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se accidentalmente metti troppi spazi, troppi pochi spazi, o mescoli tabulazioni con spazi, Python si fermerà e ti mostrerà un `IndentationError`. Questo è uno degli errori più comuni che vedono i principianti. Il

## Struttura del Blocco di Codice

Un **blocco di codice** è un gruppo di righe che appartengono insieme perché sono tutte indentate allo stesso livello. Ogni blocco inizia dopo una riga che termina con i due punti `:`, e ogni riga nel blocco

Vedrai questo modello costantemente in Python:

```python
some_statement:        # due punti aprono un blocco
    first line         # 4 spazi — dentro il blocco
    second line        # 4 spazi — ancora dentro il blocco
    third line         # 4 spazi — ancora dentro il blocco
back_to_normal         # 0 spazi — il blocco è finito
```

Al momento tutti i tuoi programmi sono una lista piatta di righe senza blocchi. Questo cambia quando raggiungi i cicli (Capitolo 7) e i condizionali (Capitolo 9). Quando arribi lì, avrai già capito come

## Regole di Spazio Bianco

Lo spazio bianco è il nome per qualsiasi carattere invisibile nel tuo codice: spazi, tabulazioni e righe vuote. Python ha regole chiare su come viene usato lo spazio bianco:

- **Dentro una riga:** aggiungi uno spazio singolo attorno agli operatori (`2 + 3`, non `2+3`) per rendere le espressioni più facili da leggere. Python ignora spazi extra dentro una riga, ma uno spazio è la convenzione.
- **All'inizio di una riga:** questi spazi sono *indentazione* e contano per Python (vedi sopra).
- **Righe vuote:** Python ignora completamente le righe vuote. Usale per separare le sezioni logiche del tuo programma.

Ecco lo stesso programma tartaruga scritto in due modi:

```python
# Difficile da leggere — nessuno spazio bianco
import turtle
t=turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
```

```python
# Facile da leggere — buono spazio bianco
import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
```

Entrambi i programmi fanno esattamente la stessa cosa. Il secondo è molto più facile da leggere a colpo d'occhio. I buoni programmatori scelgono sempre il secondo stile.

## Parole Chiave Python

Python riserva certe parole per il suo uso proprio. Queste si chiamano **parole chiave** — parole che già significano qualcosa di specifico nel linguaggio Python e non possono essere usate come nomi per le tue variabili o

Per esempio, `for` è una parola chiave Python. Non puoi nominare una variabile `for` perché Python sarebbe confuso — non saprebbe se intendevi il comando del ciclo o una variabile. Lo stesso è vero per

Ecco l'elenco completo delle parole chiave Python:

| Parole Chiave | | | | |
|---|---|---|---|---|
| `False` | `None` | `True` | `and` | `as` |
| `assert` | `async` | `await` | `break` | `class` |
| `continue` | `def` | `del` | `elif` | `else` |
| `except` | `finally` | `for` | `from` | `global` |
| `if` | `import` | `in` | `is` | `lambda` |
| `nonlocal` | `not` | `or` | `pass` | `raise` |
| `return` | `try` | `while` | `with` | `yield` |

Non hai bisogno di memorizzare questo elenco. Man mano che scrivi più programmi Python, naturalmente riconoscerai le parole chiave — la maggior parte degli editor di codice le evidenzia in un colore diverso per aiutarti a s

## Istruzione vs Espressione

Due parole escono costantemente quando si parla di codice Python: **istruzione** e **espressione**. Suonano simili ma fanno compiti diversi.

Un'**istruzione** è un'istruzione che *fa* qualcosa. Esegue un'azione. Le istruzioni non producono un valore che puoi immagazzinare o passare in giro — agiscono semplicemente.

Un'**espressione** è un pezzo di codice che *produce un valore*. Puoi usare un'espressione ovunque sia previsto un valore — immagazzinarlo in una variabile, passarlo a una funzione, o stamparlo.

La tabella sottostante mostra esempi uno accanto all'altro:

| Tipo | Esempio | Cosa fa |
|------|---------|----------|
| Istruzione | `print("Ciao")` | Visualizza il testo — non produce un valore |
| Istruzione | `import turtle` | Carica una libreria — non produce un valore |
| Espressione | `2 + 3` | Produce il valore `5` |
| Espressione | `"Ciao"` | Produce la stringa `"Ciao"` |
| Espressione | `100 * 2` | Produce il valore `200` |

Nella pratica, molte righe di Python combinano entrambe: `print(2 + 3)` è un'*istruzione* (il print) che contiene un'*espressione* (l'addizione). Conoscere la differenza aiuta a capire i messaggi di errore

## Colori Denominati

La libreria tartaruga conosce i nomi di centinaia di colori. Invece di descrivere un colore matematicamente, puoi usare il nome in inglese di un colore — un **colore denominato** — come stringa. Basta passarlo a

Alcuni colori denominati che puoi usare subito:

- Comuni: `"rosso"`, `"blu"`, `"verde"`, `"giallo"`, `"arancione"`, `"viola"`, `"nero"`, `"bianco"`
- Sfumature: `"verde forestale"`, `"blu cielo"`, `"salmone"`, `"corallo"`, `"oro"`, `"cremisi"`
- Divertenti: `"rosa caldo"`, `"blu cielo profondo"`, `"verde lime"`, `"pomodoro"`, `"orchidea"`

L'elenco completo dei colori denominati viene da uno standard chiamato **colori X11**, che include 140 nomi. Puoi sperimentare liberamente — se un nome non funziona, vedrai un errore nell'output

Ecco un programma tartaruga che disegna un quadrato con un colore diverso su ogni lato:

```python
import turtle

t = turtle.Turtle()

t.pencolor("rosso")
t.forward(100)
t.right(90)

t.pencolor("blu")
t.forward(100)
t.right(90)

t.pencolor("verde forestale")
t.forward(100)
t.right(90)

t.pencolor("arancione")
t.forward(100)
```

!!! mascot-thinking "Cosa Vedrai?"
    ![Monty pensa](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda il programma qui sopra. La tartaruga chiama `pencolor()` quattro volte — una volta prima di ogni lato. Quanti colori diversi vedrai nel disegno? Quale colore avrà l'ultimo lato? Ma

## Provalo: Disegno Tartaruga Colorato

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

t.pencolor("red")
t.forward(100)
t.right(90)

t.pencolor("blue")
t.forward(100)
t.right(90)

t.pencolor("forestgreen")
t.forward(100)
t.right(90)

t.pencolor("orange")
t.forward(100)`);
</script>

Avevi ragione? Ogni lato del quadrato è un colore diverso — rosso, blu, verde forestale e arancione. Nota le righe vuote nel codice che separano ogni gruppo di cambio colore: non influiscono su come

## Come Funziona pencolor()

`t.pencolor("nome del colore")` cambia il colore della penna della tartaruga per tutte le linee disegnate dopo quella chiamata. Non influisce sulle linee già disegnate. Pensa a esso come cambiare il colore di un marcatore prima di

| Riga | Cosa fa |
|------|----------|
| `t.pencolor("rosso")` | Cambia la penna al rosso |
| `t.forward(100)` | Disegna una linea rossa lunga 100 passi |
| `t.pencolor("blu")` | Cambia la penna al blu |
| `t.forward(100)` | Disegna una linea blu lunga 100 passi |

Il colore rimane impostato finché non chiami `pencolor()` di nuovo con un colore diverso. Se non chiami mai `pencolor()`, la tartaruga disegna in nero per impostazione predefinita.

## Controllo di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi il Colore Mancante"
    ![Monty pensa](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sottostante disegna una forma a tre lati, ma il secondo lato è senza il suo cambio di colore — disegnerà in qualunque colore venisse prima. Aggiungi **una riga** — una chiamata `t.pencolor()` con

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

t.pencolor("red")
t.forward(100)
t.right(120)

# Aggiungi una riga qui per cambiare il colore in viola

t.forward(100)
t.right(120)

t.pencolor("gold")
t.forward(100)`);
</script>

Quando aggiungi la riga giusta e fai clic su Esegui, dovresti vedere un triangolo con i lati in rosso, viola e oro. Se il secondo lato è ancora rosso, verifica di aver scritto `pencolor` in minuscolo e di aver usato pa

## Esperimenti

Prova questi cambiamenti ai programmi sopra. Per ognuno, prevedi cosa accadrà prima — poi eseguilo per controllare!

1. **Scrivi la tua stringa multi-riga.** Cambia l'haiku nel primo programma in una poesia a tre righe che hai inventato tu. **Saprai che ha funzionato quando** la tua poesia appare nell'output, una riga

2. **Cambia i colori nel programma del quadrato.** Sostituisci `"rosso"` con `"rosa caldo"`, `"blu"` con `"blu cielo profondo"`, `"verde forestale"` con `"verde lime"` e `"arancione"` con `"oro"`. **Saprai che

3. **Aggiungi un quinto lato.** Nel programma del quadrato, aggiungi `t.pencolor("viola")` e `t.right(90)` e `t.forward(100)` alla fine. Il risultato sembra un quadrato con una linea extra? **Saprai che

4. **Prova un colore che potrebbe non esistere.** Cambia un argomento `pencolor()` in `"blu neon"` ed esegui il programma. Leggi il messaggio di errore con attenzione — ti dice cosa è andato male. Poi cambialo ba

5. **Sfida — disegna un triangolo arcobaleno.** Usa tre colori denominati di tua scelta per disegnare un triangolo equilatero (tre lati uguali, `right(120)` ad ogni angolo). Aggiungi righe vuote e commenti

!!! mascot-celebration "Lavoro Brillante!"
    ![Monty celebra](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena imparato come Python organizza il codice — stringhe multi-riga, indentazione, parole chiave, blocchi di codice, istruzioni, espressioni e regole di spazio bianco — e hai reso i tuoi disegni tartaruga colorati

[Fai il Quiz di Revisione del Capitolo](./quiz.md)

[Vedi Riferimenti Annotati](./references.md)
