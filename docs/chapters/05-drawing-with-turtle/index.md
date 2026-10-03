---
title: Disegnare con la Grafica Turtle
description: Crea i tuoi primi disegni turtle usando gli oggetti Turtle e Screen, i comandi di movimento, il controllo della penna, i colori, le forme e le impostazioni di velocità.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 09:48:25
version: 0.09
---

# Disegnare con la Grafica Turtle

Alla fine di questa lezione sarai in grado di:

- Creare un oggetto `turtle.Screen()` e un oggetto `turtle.Turtle()` per impostare una finestra di disegno
- Muovere la turtle avanti, indietro, a sinistra e a destra per disegnare linee
- Alzare e abbassare la penna per saltare spazi nel tuo disegno
- Cambiare il colore, lo spessore, la forma e la velocità di disegno della turtle

Immagina un piccolo robot con un pennarello legato alla pancia.
Dici al robot dove camminare, e il pennarello disegna una traccia ovunque vada.
Questo è esattamente ciò che fa la **grafica turtle** — e in questo capitolo scriverai i comandi che danno vita a quel robot.

!!! mascot-welcome "Benvenuto/a al Capitolo 5!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo è il capitolo in cui Python diventa davvero visivo! Ogni comando che digiti fa muovere e disegnare la tua turtle — all'istante, proprio qui nel browser. Non c'è modo migliore per sviluppare il tuo istinto Python che digitare un comando, cliccare Run, e guardare la turtle obbedire. Programmiamo insieme!

## Preparare il Palcoscenico del Disegno

Prima che possa avvenire qualsiasi disegno, Python ha bisogno di due cose: uno **schermo** su cui disegnare, e una **turtle** che disegni.

### L'Oggetto turtle.Screen()

Un **`turtle.Screen()`** crea la finestra di disegno — la tela vuota dove appariranno tutte le tue forme.
Pensalo come il palcoscenico di uno spettacolo teatrale: devi allestire il palco prima che gli attori possano esibirsi.

Memorizzi lo schermo in una variabile così da potergli dare istruzioni più tardi:

```python
import turtle
wn = turtle.Screen()
```

Il nome `wn` sta per "window" (finestra) — è il soprannome più comune usato dai programmatori per questa variabile, ma puoi chiamarla come vuoi.

Una volta che hai lo schermo, puoi cambiarne il colore di sfondo usando **`bgcolor()`** (abbreviazione di "background color", colore di sfondo):

```python
wn.bgcolor("lightblue")
```

Metti qualsiasi nome di colore tra virgolette — `"lightyellow"`, `"pink"`, `"white"`, `"black"`, o uno qualsiasi dei 140 colori web con nome che Python conosce.
`bgcolor()` cambia lo sfondo della finestra nel momento in cui Python esegue quella riga.

### L'Oggetto turtle.Turtle()

Un **`turtle.Turtle()`** crea il tuo agente di disegno — la piccola freccia (o forma a tartaruga!) che si muove sulla tela, lasciando una linea colorata ovunque vada.

Nel Capitolo 4 hai imparato che gli **oggetti** hanno propri **metodi** che chiami con un punto.
Una turtle è un esempio perfetto di questa idea in azione.
Crei un oggetto e poi chiami metodi su di esso per farlo muovere, girare e disegnare.

```python
t = turtle.Turtle()
```

La variabile `t` ora contiene la tua turtle.
Ogni volta che vuoi che la turtle faccia qualcosa, scrivi `t.` seguito da un nome di comando e parentesi.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, lo **Stage** era lo sfondo bianco dove vivevano i tuoi sprite, e uno **Sprite** era il personaggio che programmavi per muoversi. Nella turtle di Python, `turtle.Screen()` è il tuo Stage e `turtle.Turtle()` è il tuo Sprite. La grande differenza? Invece di trascinare uno sprite con il mouse, scrivi comandi Python per controllarlo — e questo ti dà molto più potere di quanto potrebbe mai darti il trascina-e-rilascia!

## Muovere la Turtle

La turtle inizia sempre al centro dello schermo, rivolta verso destra (Est).
Hai quattro comandi di movimento con cui lavorare:

| Comando | Cosa fa |
|---------|-------------|
| `t.forward(n)` | Si muove `n` pixel in avanti nella direzione verso cui è rivolta la turtle |
| `t.backward(n)` | Si muove `n` pixel all'indietro (prima la coda) |
| `t.right(n)` | Ruota la turtle di `n` gradi in senso orario |
| `t.left(n)` | Ruota la turtle di `n` gradi in senso antiorario |

L'`n` in `forward()` e `backward()` si misura in **pixel** — minuscoli puntini sul tuo schermo.
Cento pixel sono circa la lunghezza del tuo pollice tenuto accanto a un monitor tipico.

L'`n` in `right()` e `left()` si misura in **gradi**, proprio come nella tua lezione di geometria.
Un cerchio completo è 360°.
Un angolo retto — come l'angolo di un foglio di carta — è esattamente 90°.

Questi quattro comandi corrispondono direttamente a blocchi che già conosci da Scratch.
Il blocco **Move N steps** è `forward(n)` in Python.
Il blocco **Turn ↻ N degrees** è `right(n)`, e il blocco **Turn ↺ N degrees** è `left(n)` — stesse idee, solo scritte come testo.

Prima di eseguire il primo laboratorio, prenditi un momento per leggere attentamente il codice.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda il programma qui sotto prima di cliccare su Run.
    La turtle si muove avanti di 100, gira a destra di 90°, si muove avanti di 100, gira a destra di 90°, poi si muove avanti un'altra volta.
    Quanti lati di un quadrato pensi vedrai?
    Fai la tua previsione — poi clicca su Run per scoprirlo!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato proprio su questa pagina.
Non serve alcun account — tutto viene eseguito nel tuo browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

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
wn = turtle.Screen()
wn.bgcolor("lightyellow")
t = turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)`);
</script>

Avevi indovinato? La turtle ha disegnato esattamente tre lati di un quadrato — una svolta di 90° a destra per ogni angolo!

**Se vedi un messaggio di errore rosso:** controlla attentamente l'ortografia.
Python distingue tra maiuscole e minuscole, quindi `Forward(100)` non funzionerà ma `forward(100)` sì.
Assicurati anche che ogni riga termini con una parentesi di chiusura `)`.

## Come Funziona

Ecco cosa fa ogni riga del programma:

| Riga | Cosa fa |
|------|-------------|
| `import turtle` | Carica la libreria turtle così Python conosce tutti i comandi di disegno |
| `wn = turtle.Screen()` | Crea la finestra di disegno e la memorizza in `wn` |
| `wn.bgcolor("lightyellow")` | Imposta lo sfondo della finestra su giallo chiaro |
| `t = turtle.Turtle()` | Crea un oggetto turtle e lo memorizza in `t` |
| `t.forward(100)` | Muove la turtle di 100 pixel in avanti nella direzione verso cui è attualmente rivolta |
| `t.right(90)` | Ruota la turtle di 90° in senso orario — un angolo retto perfetto |

Nota lo schema: ogni comando usa l'oggetto (`wn` o `t`), poi un punto, poi il nome del metodo con un numero dentro le parentesi.
Questo è esattamente lo schema oggetto-metodo del Capitolo 4.

## Osservalo: Cosa Sa la Turtle

La turtle tiene segretamente traccia di quattro cose in ogni momento: la sua **posizione x**, la sua **posizione y**, il suo **orientamento** (la direzione verso cui è rivolta), e se la sua **penna** è alzata o abbassata. L'ispettore qui sotto le mostra tutte mentre procedi passo passo attraverso un programma, un comando alla volta. Prima di cliccare, **prevedi dove si troverà la turtle e verso quale direzione sarà rivolta dopo i primi due comandi**.

<iframe src="../../sims/turtle-state-inspector/main.html" height="512" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Turtle State Inspector](../../sims/turtle-state-inspector/index.md){ .md-button }

Osserva il valore dell'orientamento mentre procedi passo passo nel programma Square: `t.right(90)` sottrae 90 dall'orientamento ogni volta. Poi prova il programma **Pen Demo** per vedere lo spazio vuoto che lascia `penup()`.

## Controllo della Penna: penup() e pendown()

In questo momento la turtle disegna una linea ovunque si muova.
Ma cosa succede se vuoi due forme separate con uno spazio tra loro?

Pensa a disegnare con una penna vera: solleveresti la penna dal foglio, la faresti scorrere nel nuovo punto, poi la premeresti di nuovo giù.
La grafica turtle funziona allo stesso modo.

- **`t.penup()`** solleva la penna dalla tela. La turtle può muoversi senza disegnare nulla.
- **`t.pendown()`** riappoggia la penna sulla tela. Ogni passo dopo questo lascia una linea.

La turtle inizia sempre con la penna abbassata, ed è per questo che la primissima chiamata a `forward()` disegna una linea.

In Scratch potresti aver usato i blocchi **Pen Up** e **Pen Down** dall'estensione pen — `penup()` e `pendown()` funzionano esattamente allo stesso modo.

Ecco un programma che disegna due linee separate con uno spazio nel mezzo:

```python
import turtle
t = turtle.Turtle()
t.forward(80)      # draw a line
t.penup()          # lift the pen
t.forward(40)      # move 40 pixels — nothing drawn here
t.pendown()        # lower the pen
t.forward(80)      # draw another line
```

Provalo nel laboratorio qui sotto — presta molta attenzione allo spazio vuoto nel mezzo del disegno.

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
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
t.forward(80)`);
</script>

Lo spazio vuoto è dove la turtle ha viaggiato con la penna in aria.
Prova a cambiare il `40` nel `t.forward(40)` centrale in `80` — lo spazio vuoto raddoppia di larghezza.

!!! mascot-warning "Non Dimenticare pendown()!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    L'errore più comune con `penup()` è dimenticare di chiamare `pendown()` dopo. Se la tua turtle si muove ma la tela resta completamente vuota, cerca un `pendown()` mancante. La turtle si muove esattamente come la comandi — semplicemente non lascia traccia perché la penna è ancora sollevata. Aggiungi `t.pendown()` prima della riga che vuoi disegnare e sei di nuovo a posto!

## Spessore e Colore della Penna

Una linea nera su uno sfondo bianco è solo l'inizio.
Puoi scegliere qualsiasi colore e qualsiasi spessore per la penna della tua turtle.

Due comandi controllano l'aspetto della linea:

- **`t.pensize(n)`** imposta lo spessore della linea in pixel. Il valore predefinito è `1`. Prova `3`, `5` o `10` per disegnare linee più marcate.
- **`t.pencolor("colore")`** imposta il colore della linea disegnata dalla turtle. Usa un nome di colore tra virgolette: `"red"`, `"blue"`, `"green"`, `"orange"`, `"purple"`, o qualsiasi colore web con nome.

Proprio come il blocco **Set pen color** in Scratch, `pencolor()` cambia il colore per ogni linea disegnata dopo quella chiamata.
Puoi cambiare colore a metà di un programma — ogni chiamata a `pencolor()` influisce solo sulle linee che vengono dopo.

## Aspetto della Turtle: shape(), hideturtle() e showturtle()

La turtle predefinita somiglia a una piccola punta di freccia.
Il comando **`t.shape()`** la sostituisce con un aspetto diverso.
Ecco tutte e sei le forme integrate:

| Nome forma | Che aspetto ha |
|------------|-------------------|
| `"arrow"` | Una piccola punta di freccia (quella predefinita) |
| `"turtle"` | Una tartaruga a fumetti vista dall'alto |
| `"circle"` | Un cerchio pieno |
| `"square"` | Un piccolo quadrato pieno |
| `"triangle"` | Un piccolo triangolo |
| `"classic"` | Una forma di freccia leggermente diversa |

A volte vuoi che il cursore della turtle scompaia da un disegno finito, così non distrae dalla tua opera.
Due comandi gestiscono questo:

- **`t.hideturtle()`** rende invisibile il cursore della turtle. Il tuo disegno resta comunque visibile — la turtle si fa semplicemente da parte.
- **`t.showturtle()`** riporta in vista una turtle nascosta.

## Controllo della Velocità: speed()

Ogni turtle inizia con una velocità di disegno media.
Il comando **`t.speed(n)`** controlla quanto velocemente si muove, usando un numero da `0` a `10`:

| Valore | Velocità |
|-------|-------|
| `1` | La più lenta — buona per osservare ogni passo |
| `5` | Media — il valore predefinito |
| `10` | Veloce |
| `0` | Istantanea — salta completamente l'animazione |

Usa `speed(0)` quando il tuo programma disegna molte linee e non vuoi aspettare.
Usa `speed(1)` quando stai imparando o facendo debug e vuoi vedere la turtle muoversi un passo alla volta.

Ora prova un laboratorio che combina colore, aspetto e velocità — tutto in un unico programma:

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
t.shape("turtle")
t.speed(5)
t.pensize(4)
t.pencolor("blue")
t.forward(100)
t.right(90)
t.pencolor("red")
t.forward(100)
t.hideturtle()`);
</script>

Nota che la prima linea è blu e la seconda è rossa — cambiare `pencolor()` a metà di un disegno influisce solo sulle linee che vengono dopo quella chiamata.
Quando il programma termina, il cursore della turtle stesso scompare a causa di `hideturtle()`.

## Verifica di Apprendimento

Hai ora visto tutti e dieci i comandi di questo capitolo.
Ora mettili alla prova!
Il programma qui sotto disegna due lati di un quadrato e poi si ferma.

!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna due lati di un quadrato e poi si ferma a metà.
    Dopo il secondo `t.right(90)`, la turtle è già rivolta nella direzione giusta per il terzo lato.
    Aggiungi **una riga** per farle disegnare quel terzo lato — lungo 100 pixel.
    Suggerimento: quale comando muove la turtle in avanti?

<div class="cm-lab">
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
initCmLab('-4', `import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pencolor("green")
t.pensize(3)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
# Add ONE line below to draw the third side of the square`);
</script>

Se hai risposto correttamente, vedrai tre lati di un quadrato disegnati in verde.
La riga mancante è `t.forward(100)` — la turtle era già rivolta nella direzione giusta dopo due svolte a destra, quindi le serviva solo un'altra spinta in avanti!

## Esperimenti

Prova questi cambiamenti ai programmi qui sopra.
Per ciascuno, prevedi prima cosa succederà — poi eseguilo per verificare!

1. Nel Laboratorio 1, cambia entrambe le chiamate `t.right(90)` in `t.right(120)`. **Saprai che ha funzionato quando** la turtle disegna l'angolo di un triangolo invece dell'angolo di un quadrato.
2. Nel Laboratorio 1, cambia `wn.bgcolor("lightyellow")` in `wn.bgcolor("lightblue")`. **Saprai che ha funzionato quando** lo sfondo diventa un delicato azzurro cielo.
3. Nel Laboratorio 2, cambia il `40` in `t.forward(40)` (quello di mezzo, tra penup e pendown) in `100`. **Saprai che ha funzionato quando** lo spazio tra le due linee è molto più largo delle linee stesse.
4. Nel Laboratorio 3, prova ciascuno dei sei nomi di forma in `t.shape()`: `"arrow"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"`, `"classic"`. **Saprai che ha funzionato quando** il cursore della turtle cambia forma prima di iniziare a disegnare.
5. **Sfida:** Nel Laboratorio 3, cambia `t.speed(5)` in `t.speed(1)` e guarda la turtle disegnare lentamente. Poi cambialo in `t.speed(0)` ed esegui di nuovo. Cosa cambia? Quando sarebbe utile ciascuna impostazione di velocità?

!!! mascot-celebration "Sai Comandare una Turtle!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena imparato dieci comandi turtle di Python e li hai usati per disegnare forme vere sullo schermo — non è poco! Nei capitoli che seguono combinerai questi comandi con cicli e funzioni per disegnare pattern che nessun essere umano potrebbe creare a mano. Te lo sei meritato. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
