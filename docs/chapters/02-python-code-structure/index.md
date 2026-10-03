---
title: Struttura del Codice Python
description: Scopri come Python usa l'indentazione per raggruppare il codice, conosci le parole chiave di Python e aggiungi colori con nome ai tuoi disegni turtle.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:35:09
version: 0.09
---

# Struttura del Codice Python

## Riepilogo

Python ha un aspetto molto ordinato: invece delle parentesi graffe o delle parole chiave `begin/end`,
usa l'**indentazione** (gli spazi) per raggruppare le righe di codice.
Questo capitolo esplora queste regole — indentazione, blocchi di codice, istruzioni,
spazi bianchi — più le parole chiave di Python e i colori con nome che userai con turtle.

## Concetti Trattati

Questo capitolo tratta i seguenti 7 concetti del grafo di apprendimento:

1. Multi-Line Strings
2. Indentation as Syntax
3. Python Keywords
4. Code Block Structure
5. Statement vs Expression
6. Whitespace Rules
7. Named Colors

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 1: Benvenuto in Python e Skulpt](../01-welcome-to-python/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Scrivere testo multi-riga usando le triple virgolette
- Spiegare perché Python usa l'indentazione per raggruppare le righe di codice
- Riconoscere le parole chiave di Python e capire perché non possono essere usate come nomi di variabili
- Usare colori con nome come `"red"` e `"forestgreen"` nei programmi di grafica turtle

Nel Capitolo 1 hai scritto le tue prime righe Python: `print()`, i commenti e un disegno turtle. Ora sei pronto a guardare come Python è *strutturato* — le regole che governano come il codice è disposto sulla pagina e cosa rende un programma Python leggibile e corretto.

!!! mascot-welcome "Bentornato, Programmatore!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto ad andare più a fondo? Questo capitolo parla di come è organizzato il codice Python — e le regole sono più semplici di quanto pensi. Alla fine renderai anche i tuoi disegni turtle molto più colorati. Programmiamo insieme!

## Stringhe Multi-Riga

Nel Capitolo 1 hai usato `print()` per mostrare testo racchiuso tra virgolette doppie, come `"Hello, world!"`. Funziona benissimo per messaggi brevi su una riga. Ma cosa succede se vuoi scrivere diverse righe di testo memorizzate in un'unica variabile?

Python risolve questo problema con una **stringa multi-riga** — una stringa che si estende su più righe, creata racchiudendo il testo tra **triple virgolette**: tre virgolette doppie (`"""`) o tre virgolette singole (`'''`). Tutto ciò che si trova tra le triple virgolette di apertura e quelle di chiusura — incluse le righe a capo — diventa parte della stringa.

```python
haiku = """An old silent pond.
A frog jumps into the pond.
Splash! Silence again."""
print(haiku)
```

**Prima di cliccare su Run:** quante righe pensi appariranno nell'output? Conta gli a capo dentro le triple virgolette per fare la tua previsione!

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
initCmLab('', `haiku = """An old silent pond.
A frog jumps into the pond.
Splash! Silence again."""
print(haiku)`);
</script>

Avevi ragione? Appaiono tre righe — una per ogni riga dentro le triple virgolette. La variabile `haiku` contiene tutte e tre le righe come un'unica stringa, e `print()` le mostra tutte insieme, con gli a capo preservati.

## Come Funzionano le Stringhe Multi-Riga

Una stringa normale usa una coppia di virgolette: `"Hello"`. Una stringa multi-riga usa tre coppie: `"""Hello"""`. Le triple virgolette dicono a Python: “continua a leggere finché non vedi altre tre virgolette — non importa quanti a capo ci siano nel mezzo.”

| Sintassi | Può estendersi su più righe? | Esempio |
|--------|-------------------------|---------|
| `"text"` | No — solo una riga | `"Hello, world!"` |
| `'text'` | No — solo una riga | `'Hello, world!'` |
| `"""text"""` | Sì | `"""Line one\nLine two"""` |
| `'''text'''` | Sì | `'''Line one\nLine two'''` |

Le stringhe multi-riga sono utili per scrivere poesie, paragrafi, o qualsiasi blocco di testo che vuoi mantenere insieme in un'unica variabile.

## L'Indentazione come Sintassi

La maggior parte dei linguaggi di programmazione usa le **parentesi graffe** `{ }` o le parole `begin` ed `end` per mostrare che certe righe di codice vanno insieme. Python fa qualcosa di diverso — usa l'**indentazione**: il numero di spazi all'inizio di ogni riga.

**Indentazione** significa premere la barra spaziatrice (o il tasto Tab) prima di una riga di codice per spostarla verso destra. In Python, l'indentazione non è solo estetica — fa parte della grammatica del linguaggio. Python legge gli spazi all'inizio di una riga per decidere quali righe vanno insieme.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, metti blocchi *dentro* un altro blocco (come un blocco Repeat) trascinandoli così si incastrano al suo interno. In Python, metti righe *dentro* un gruppo **indentandole** — aggiungendo 4 spazi all'inizio. L'annidamento visivo che vedevi in Scratch adesso vive in quei 4 spazi bianchi.

Ecco un'anteprima di come appare l'indentazione in azione. Non hai ancora imparato i cicli `for` — arriveranno nel Capitolo 7 — ma osserva subito lo schema degli spazi:

```python
# PREVIEW — you will learn for loops in Chapter 7
# For now, just notice the indentation pattern

for i in range(4):   # This line starts at the left edge
    t.forward(100)   # These two lines are indented 4 spaces
    t.right(90)      # They belong INSIDE the for loop
```

Le due righe con 4 spazi davanti sono *dentro* il ciclo. La riga `for` stessa è al margine sinistro. Quella differenza di spaziatura è ciò che Python usa per sapere quali righe fanno parte del ciclo — non le parentesi, non le parole chiave, solo gli spazi.

!!! mascot-warning "IndentationError — L'Errore Più Comune in Python"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se per sbaglio metti troppi spazi, troppo pochi, o mescoli tab e spazi, Python si fermerà e mostrerà un `IndentationError`. È uno degli errori più comuni che i principianti incontrano. La soluzione è sempre la stessa: usa esattamente **4 spazi** per ogni livello di indentazione, e non mescolare mai tab e spazi. La maggior parte degli editor di codice (incluso Skulpt) inserisce automaticamente 4 spazi quando premi Tab.

## Struttura dei Blocchi di Codice

Un **blocco di codice** è un gruppo di righe che vanno insieme perché sono tutte indentate allo stesso livello. Ogni blocco inizia dopo una riga che termina con i due punti `:`, e ogni riga nel blocco è indentata di esattamente 4 spazi in più rispetto alla riga che lo ha aperto.

Vedrai questo schema costantemente in Python:

```python
some_statement:        # colon opens a block
    first line         # 4 spaces — inside the block
    second line        # 4 spaces — still inside the block
    third line         # 4 spaces — still inside the block
back_to_normal         # 0 spaces — block is over
```

Per ora tutti i tuoi programmi sono un elenco piatto di righe senza blocchi. Questo cambierà quando arriverai ai cicli (Capitolo 7) e alle condizioni (Capitolo 9). Quando ci arriverai, capirai già come funzionano i blocchi — perché lo stai imparando adesso.

## Regole sugli Spazi Bianchi

Spazio bianco è il nome per qualsiasi carattere invisibile nel tuo codice: spazi, tab e righe vuote. Python ha regole chiare su come viene usato lo spazio bianco:

- **All'interno di una riga:** aggiungi un singolo spazio intorno agli operatori (`2 + 3`, non `2+3`) per rendere le espressioni più facili da leggere. Python ignora gli spazi extra dentro una riga, ma uno spazio è la convenzione.
- **All'inizio di una riga:** questi spazi sono *indentazione* e sono importanti per Python (vedi sopra).
- **Righe vuote:** Python ignora completamente le righe vuote. Usale per separare le sezioni logiche del tuo programma.

Ecco lo stesso programma turtle scritto in due modi:

```python
# Hard to read — no whitespace
import turtle
t=turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
```

```python
# Easy to read — good whitespace
import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)
```

Entrambi i programmi fanno esattamente la stessa cosa. Il secondo è molto più facile da leggere a prima vista. I bravi programmatori scelgono sempre il secondo stile.

## Parole Chiave di Python

Python riserva certe parole per il proprio uso. Si chiamano **parole chiave** — parole che hanno già un significato specifico nel linguaggio Python e non possono essere usate come nomi per le tue variabili o funzioni.

Per esempio, `for` è una parola chiave di Python. Non puoi chiamare una variabile `for` perché Python si confonderebbe — non saprebbe se intendevi il comando del ciclo o una variabile. Lo stesso vale per `if`, `while`, `def`, `class`, e tutte le altre nella tabella qui sotto.

Ecco l'elenco completo delle parole chiave di Python:

| Parole chiave | | | | |
|---|---|---|---|---|
| `False` | `None` | `True` | `and` | `as` |
| `assert` | `async` | `await` | `break` | `class` |
| `continue` | `def` | `del` | `elif` | `else` |
| `except` | `finally` | `for` | `from` | `global` |
| `if` | `import` | `in` | `is` | `lambda` |
| `nonlocal` | `not` | `or` | `pass` | `raise` |
| `return` | `try` | `while` | `with` | `yield` |

Non devi memorizzare questo elenco. Mentre scrivi più programmi Python, imparerai naturalmente a riconoscere le parole chiave — la maggior parte degli editor di codice le evidenzia con un colore diverso per aiutarti a individuarle a colpo d'occhio.

## Istruzione vs Espressione

Due parole ricorrono costantemente quando si parla di codice Python: **statement** (istruzione) e **expression** (espressione). Sembrano simili ma svolgono compiti diversi.

Uno **statement** (istruzione) è un comando che *fa* qualcosa. Compie un'azione. Gli statement non producono un valore che puoi memorizzare o passare in giro — agiscono, semplicemente.

Un'**expression** (espressione) è un pezzo di codice che *produce un valore*. Puoi usare un'espressione ovunque sia previsto un valore — memorizzarla in una variabile, passarla a una funzione, o stamparla.

La tabella qui sotto mostra esempi affiancati:

| Tipo | Esempio | Cosa fa |
|------|---------|-------------|
| Statement | `print("Hello")` | Mostra testo — non produce un valore |
| Statement | `import turtle` | Carica una libreria — non produce un valore |
| Expression | `2 + 3` | Produce il valore `5` |
| Expression | `"Hello"` | Produce la stringa `"Hello"` |
| Expression | `100 * 2` | Produce il valore `200` |

In pratica, molte righe di Python combinano entrambi: `print(2 + 3)` è uno *statement* (il print) che contiene un'*expression* (l'addizione). Conoscere la differenza ti aiuta a capire i messaggi di errore — Python ti dirà quando si aspettava un'espressione e ha ricevuto uno statement, o viceversa.

## Colori con Nome

La libreria turtle conosce i nomi di centinaia di colori. Invece di descrivere un colore matematicamente, puoi usare il nome inglese di un colore — un **colore con nome** — come stringa. Passalo semplicemente a `t.pencolor()` prima di disegnare una linea e la tartaruga passerà a quel colore.

Alcuni colori con nome che puoi usare subito:

- Comuni: `"red"`, `"blue"`, `"green"`, `"yellow"`, `"orange"`, `"purple"`, `"black"`, `"white"`
- Sfumature: `"forestgreen"`, `"skyblue"`, `"salmon"`, `"coral"`, `"gold"`, `"crimson"`
- Divertenti: `"hotpink"`, `"deepskyblue"`, `"limegreen"`, `"tomato"`, `"orchid"`

L'elenco completo dei colori con nome deriva da uno standard chiamato **X11 colors**, che include 140 nomi. Puoi sperimentare liberamente — se un nome non funziona, vedrai un errore nel riquadro di output e potrai provare un'altra grafia.

Ecco un programma turtle che disegna un quadrato con un colore diverso su ogni lato:

```python
import turtle

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
t.forward(100)
```

!!! mascot-thinking "Cosa Vedrai?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda il programma qui sopra. La tartaruga chiama `pencolor()` quattro volte — una prima di ogni lato. Quanti colori diversi vedrai nel disegno? Di che colore sarà l'ultimissimo lato? Fai le tue previsioni, poi clicca su Run!

## Provalo: Disegno Turtle Colorato

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

Avevi ragione? Ogni lato del quadrato ha un colore diverso — rosso, blu, verde foresta e arancione. Nota le righe vuote nel codice che separano ogni gruppo di cambio colore: non influenzano come viene eseguito il programma, ma rendono la struttura immediatamente chiara a chi legge.

## Come Funziona pencolor()

`t.pencolor("color name")` cambia il colore della penna della tartaruga per tutte le linee disegnate dopo quella chiamata. Non influenza le linee già disegnate. Pensalo come cambiare il colore di un pennarello prima di disegnare il prossimo tratto.

| Riga | Cosa fa |
|------|-------------|
| `t.pencolor("red")` | Passa la penna al rosso |
| `t.forward(100)` | Disegna una linea rossa di 100 passi |
| `t.pencolor("blue")` | Passa la penna al blu |
| `t.forward(100)` | Disegna una linea blu di 100 passi |

Il colore resta impostato finché non chiami di nuovo `pencolor()` con un colore diverso. Se non chiami mai `pencolor()`, la tartaruga disegna in nero per impostazione predefinita.

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Aggiungi il Colore Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna una forma a tre lati, ma al secondo lato manca il cambio di colore — verrà disegnato con qualunque colore fosse impostato prima. Aggiungi **una riga** — una chiamata a `t.pencolor()` con il colore `"purple"` — tra il primo `t.right(90)` e il secondo `t.forward(100)` per rendere il secondo lato viola.

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

t.pencolor("red")
t.forward(100)
t.right(120)

# Add one line here to change the color to purple

t.forward(100)
t.right(120)

t.pencolor("gold")
t.forward(100)`);
</script>

Quando aggiungi la riga giusta e clicchi su Run, dovresti vedere un triangolo con i lati in rosso, viola e oro. Se il secondo lato è ancora rosso, controlla di aver scritto `pencolor` tutto minuscolo e di aver passato `"purple"` tra virgolette.

## Esperimenti

Prova queste modifiche ai programmi qui sopra. Per ognuna, prevedi prima cosa succederà — poi eseguila per verificare!

1. **Scrivi la tua stringa multi-riga.** Cambia l'haiku nel primo programma con una poesia di tre righe inventata da te. **Saprai che ha funzionato quando** la tua poesia apparirà nell'output, una riga alla volta.

2. **Cambia i colori nel programma del quadrato.** Sostituisci `"red"` con `"hotpink"`, `"blue"` con `"deepskyblue"`, `"forestgreen"` con `"limegreen"`, e `"orange"` con `"gold"`. **Saprai che ha funzionato quando** il quadrato verrà disegnato con i tuoi quattro nuovi colori.

3. **Aggiungi un quinto lato.** Nel programma del quadrato, aggiungi alla fine `t.pencolor("purple")`, `t.right(90)` e `t.forward(100)`. Il risultato sembra un quadrato con una linea in più? **Saprai che ha funzionato quando** vedrai una quinta linea disegnata in viola.

4. **Prova un colore che potrebbe non esistere.** Cambia un argomento di `pencolor()` in `"neonblue"` ed esegui il programma. Leggi attentamente il messaggio di errore — ti dice cosa è andato storto. Poi rimettilo su un colore valido come `"cornflowerblue"`.

5. **Sfida — disegna un triangolo arcobaleno.** Usa tre colori con nome a tua scelta per disegnare un triangolo equilatero (tre lati uguali, `right(120)` a ogni angolo). Aggiungi righe vuote e commenti nel codice per etichettare ogni lato. **Saprai che ha funzionato quando** vedrai un triangolo chiuso con tre colori distinti e un codice ordinato e leggibile.

!!! mascot-celebration "Lavoro Brillante!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena imparato come Python organizza il codice — stringhe multi-riga, indentazione, parole chiave, blocchi di codice, statement, espressioni e regole sugli spazi bianchi — e nel frattempo hai reso i tuoi disegni turtle più colorati. Sette concetti in un solo capitolo, e li hai gestiti tutti magnificamente. Continua così — stai costruendo competenze di programmazione reali! Programmiamo insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
