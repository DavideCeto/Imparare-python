---
title: Idee di MicroSim per Beginning Python
description: Un elenco con priorità, classificato secondo Bloom, delle MicroSim proposte per il manuale Beginning Python, con un piano di implementazione per ciascuna.
status: draft-for-review
---
# Idee di MicroSim per Beginning Python

**Stato: bozza da rivedere — nessuna sim è stata ancora generata.**

Questo documento è stato prodotto analizzando tutti i 38 capitoli in `docs/chapters/`, i
17 laboratori Python, il grafo di apprendimento e la galleria di grafica turtle. Ogni
capitolo ha già degli ottimi laboratori Skulpt/CodeMirror del tipo "guardalo, eseguilo,
modificalo", quindi queste proposte evitano di proposito di duplicare ciò che un laboratorio
in cui si esegue il codice fa già bene. Ogni MicroSim proposta si concentra invece sui
**meccanismi invisibili**: i modelli mentali (memoria, flusso di controllo, stack delle
chiamate, ricerca per hash, convoluzione) che gli studenti non possono vedere solo
guardando l'output del programma.

## Regole di base per il progetto

Tutte le proposte seguono le convenzioni della skill `microsim-generator`:

- **Cartella:** `docs/sims/<sim-id>/` con `main.html`, `<sim-id>.js`,
  `index.md` e `metadata.json` (struttura creata da `generate-sim-scaffold.py`)
- **La scelta della libreria** segue la tabella di instradamento del generatore (p5.js per
  le simulazioni personalizzate, Chart.js per i grafici, Plotly per i grafici di f(x),
  vis-network per i grafi di nodi e archi, HTML personalizzato per le sim con diagrammi di
  Venn e tabelle)
- **Lo schema di interazione corrisponde al livello di Bloom** (Step 3.2 del generatore):
  le sim di livello Comprendere usano l'**avanzamento passo passo** (pulsanti Next/Previous,
  dati concreti visibili), mai un'animazione continua; le sim di livello Applicare usano
  **cursori dei parametri con riscontro immediato**; le sim di livello Analizzare usano
  **strumenti di confronto ed esplorazione**; le sim di livello Creare usano **strumenti di
  costruzione e canvas**
- Ogni file `.js` dichiara `// CANVAS_HEIGHT: <n>` nelle prime 10 righe;
  altezza dell'iframe = CANVAS_HEIGHT + 2; gli iframe usano percorsi relativi,
  `scrolling="no"` e nessun attributo `style`
- Il pubblico ha 10–14 anni: un concetto per sim, controlli grandi e adatti al tocco,
  niente gergo tecnico nelle etichette

### Promemoria della Tassonomia di Bloom rivista (2001)

| Livello | Processo cognitivo | Verbi tipici |
|-------|-------------------|---------------|
| 1. Ricordare | Recuperare conoscenze | riconoscere, richiamare, elencare, identificare, nominare |
| 2. Comprendere | Costruire significato | spiegare, interpretare, classificare, riassumere, dedurre, confrontare, prevedere, esemplificare |
| 3. Applicare | Eseguire una procedura | eseguire, implementare, usare, dimostrare, risolvere |
| 4. Analizzare | Scomporre in parti e collegarle | differenziare, organizzare, attribuire, contrapporre, fare debug, scomporre |
| 5. Valutare | Giudicare in base a criteri | verificare, criticare, giudicare, motivare, difendere, testare |
| 6. Creare | Assemblare qualcosa di nuovo | generare, pianificare, progettare, produrre, costruire, comporre |

## Riepilogo delle priorità

| Priorità | Ambito | Sim | Motivazione |
|------|-------|------|-----------|
| 1 | Modelli mentali di base (Cap. 1–10) | 11 | Le fondamenta del libro; le idee sbagliate che si formano qui durano per anni |
| 2 | Dati e funzioni (Cap. 11–20) | 9 | Indici, scope e collezioni sono le principali fonti di bug per i principianti |
| 3 | Informatica di livello intermedio (Cap. 21–30) | 10 | Stack delle chiamate, hashing e algoritmi sono classici argomenti "da visualizzare per forza" |
| 4 | Argomenti avanzati (Cap. 31–38) | 6 | Meno lettori arrivano a questi capitoli, ma ogni sim ha comunque molto valore |

---

## Priorità 1 — Modelli mentali di base (Capitoli 1–10)

### 1. Esecutore passo passo (`code-stepper`)

- **Capitolo:** 1–2 (Benvenuto in Python; Struttura del codice Python)
- **Concetto e lacuna:** gli studenti eseguono programmi interi e vedono solo l'output
  finale. Non vedono mai l'interprete percorrere il codice dall'alto verso il basso, una riga
  alla volta: il modello mentale più fondamentale della programmazione.
- **Bloom (2001):** Comprendere — *spiegare, prevedere, seguire l'esecuzione*
- **Obiettivo di apprendimento:** lo studente sarà in grado di prevedere quale riga di un
  breve programma Python verrà eseguita dopo e di spiegare che Python esegue le istruzioni
  in ordine, dall'alto verso il basso.
- **Libreria:** p5.js (simulazione personalizzata passo passo)
- **Schema di interazione:** avanzamento passo passo con i pulsanti Next / Previous / Reset
  (niente animazione continua: è un obiettivo di livello Comprendere)
- **Piano di implementazione:**
    - Pannello sinistro: un programma fisso di 6–8 righe (istruzioni print, una variabile, un
      commento) con la riga corrente evidenziata da una freccia che si sposta
    - Pannello destro: la console di output, che cresce di una riga a ogni passo, più un
      piccolo riquadro "saltata: è un commento" quando la freccia passa su un commento
    - Menu a tendina per scegliere tra 3 programmi predefiniti, via via più insidiosi
    - Pulsanti: Next Step, Previous Step, Reset; contatore dei passi
    - `CANVAS_HEIGHT` stimato: `460` (400 per il disegno + 60 per i controlli)

### 2. Modello della memoria delle variabili (`variable-memory-model`)

- **Capitolo:** 3 (Variabili e numeri)
- **Concetto e lacuna:** `score = 10` è una magia invisibile. La metafora del foglietto
  adesivo è descritta a parole ma non si vede mai in azione. La riassegnazione ("il vecchio
  valore viene sostituito") è un punto in cui nascono spesso idee sbagliate.
- **Bloom (2001):** Comprendere — *spiegare, interpretare, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare che cosa succede in
  memoria quando una variabile viene creata, letta e riassegnata.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo in un breve script di assegnazioni; le
  caselle di memoria con l'etichetta si aggiornano a ogni passo
- **Piano di implementazione:**
    - In alto: uno script di 5 righe (`score = 10`, `lives = 3`, `score = score + 5`, …)
      con la riga corrente evidenziata
    - In basso: caselle di memoria con un nome; alla riassegnazione il vecchio valore salta
      fuori in modo visibile e quello nuovo ci cade dentro; le letture disegnano una freccia
      dalla casella all'espressione
    - Domanda di previsione prima del passo `score = score + 5`: "Che cosa conterrà la
      casella?", con una verifica a 3 scelte da cliccare
    - Pulsanti: Next, Reset; selettore di esempi predefiniti (numeri, stringhe, misti)
    - `CANVAS_HEIGHT` stimato: `480`

### 3. Flusso di una chiamata di funzione (`function-call-flow`)

- **Capitolo:** 4 (Funzioni e oggetti), riutilizzata nel Cap. 11
- **Concetto e lacuna:** gli studenti non vedono il legame tra argomento e parametro, il
  salto nel corpo della funzione o il valore di ritorno che torna indietro. "Perché `def` non
  esegue il mio codice?" è la domanda numero 1 di questo capitolo.
- **Bloom (2001):** Comprendere — *spiegare, seguire l'esecuzione, dedurre*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire una chiamata di
  funzione, spiegando come il valore dell'argomento si lega al parametro e come il valore di
  ritorno prende il posto della chiamata.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo con frecce che mostrano il flusso dei
  dati (secondo le indicazioni del generatore: dati concreti visibili, niente effetti
  particellari)
- **Piano di implementazione:**
    - Pannello del programma con `def double(n): return n * 2` più due chiamate; nella fase
      di definizione la funzione appare come una "macchina" con un'etichetta, che viene
      memorizzata ma non eseguita
    - Nei passi di chiamata, animazione un passo alla volta: l'argomento `5` entra nello
      spazio del parametro `n`, il corpo calcola, `10` torna al punto della chiamata e lo
      sostituisce
    - Mostrare la stessa funzione chiamata due volte con argomenti diversi, per rafforzare
      l'idea di riutilizzo
    - Pulsanti: Next, Previous, Reset
    - `CANVAS_HEIGHT` stimato: `500`

### 4. Ispettore dello stato della turtle (`turtle-state-inspector`)

- **Capitolo:** 5 (Disegnare con la grafica turtle), riutilizzata nel 7 e nel 18
- **Concetto e lacuna:** gli studenti danno comandi alla turtle ma non vedono mai il suo
  stato interno: posizione (x, y), direzione, penna alzata o abbassata. Senza un modello
  della direzione, `t.right(90)` viene imparato a memoria, non capito.
- **Bloom (2001):** da Comprendere ad Applicare — *interpretare, prevedere, dimostrare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di prevedere la posizione e la
  direzione della turtle dopo ogni comando e di dimostrare come i cambi di direzione
  producono le forme.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo in un elenco di comandi, più un pannello
  dello stato aggiornato in tempo reale
- **Piano di implementazione:**
    - Canvas principale: griglia di coordinate con il mirino sull'origine, la turtle
      disegnata come un triangolo con una freccia che indica la direzione
    - Pannello laterale: x, y e direzione in tempo reale (quadrante a bussola), stato della
      penna (icona alzata/abbassata), campione del colore della penna, aggiornati a ogni
      passo
    - Elenco di comandi (per esempio il classico quadrato) da percorrere con Next; il
      comando eseguito si evidenzia e i valori del pannello lampeggiano quando cambiano
    - Selettore di esempi predefiniti: quadrato, triangolo, stella, dimostrazione di
      penup/pendown
    - `CANVAS_HEIGHT` stimato: `520`

### 5. Valutatore di espressioni (`expression-evaluator`)

- **Capitolo:** 6 (Matematica e aritmetica)
- **Concetto e lacuna:** l'ordine delle operazioni è mostrato in una tabella statica. Gli
  studenti hanno bisogno di vedere `2 + 3 * 4` ridursi nell'ordine giusto, passo dopo passo.
- **Bloom (2001):** da Comprendere ad Applicare — *interpretare, eseguire, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di calcolare un'espressione
  aritmetica nello stesso ordine di Python, un'operazione alla volta.
- **Libreria:** p5.js
- **Schema di interazione:** calcolo passo passo, con l'opzione di fare prima una previsione
- **Piano di implementazione:**
    - Un'espressione grande al centro del canvas; ogni clic su Next evidenzia l'operazione
      successiva da eseguire (con un colore diverso per ogni livello di precedenza) e la
      riduce al suo valore
    - Interruttore "Mostra parentesi" che disegna i raggruppamenti impliciti prima di
      procedere
    - Espressioni predefinite che coprono `**`, `//`, `%` e le parentesi, più una casella
      "tocca a te" (solo cifre e operatori) che calcola un'espressione scritta dallo
      studente
    - `CANVAS_HEIGHT` stimato: `420`

### 6. Orologio del modulo (`modulo-clock`)

- **Capitolo:** 6 (Matematica e aritmetica)
- **Concetto e lacuna:** `10 % 3` come "quello che avanza" è un'idea astratta; la vera
  potenza del modulo (i cicli, pari/dispari) ha bisogno di un'immagine che "ricomincia da
  capo".
- **Bloom (2001):** da Comprendere ad Applicare — *spiegare, usare, dimostrare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare il resto come un
  conteggio che ricomincia da capo e di usare `%` per verificare se un numero è pari o
  dispari e per ripetere ciclicamente dei valori.
- **Libreria:** p5.js
- **Schema di interazione:** due cursori con riscontro visivo immediato (livello Applicare:
  la risposta in tempo reale è adatta)
- **Piano di implementazione:**
    - Un quadrante circolare con `divisor` tacche; una pedina fa il giro del quadrante
      `dividend` volte e si ferma sul resto
    - Cursori: dividendo (0–60), divisore (2–12); un'indicazione mostra `17 % 5 = 2`
      aggiornata in tempo reale, più la vista a gruppi (17 puntini raggruppati in righe da 5,
      con 2 che avanzano)
    - Mini-modalità "verifica pari/dispari" con il divisore bloccato a 2
    - `CANVAS_HEIGHT` stimato: `470`

### 7. Ciclo for passo passo (`for-loop-stepper`)

- **Capitolo:** 7 (Cicli for e disegno di forme)
- **Concetto e lacuna:** la tabella delle ripetizioni del ciclo nel testo è statica. Gli
  studenti hanno bisogno di vedere `i` che cambia, il corpo che viene rieseguito e,
  soprattutto per questo libro, la turtle che disegna un lato del quadrato a ogni giro.
- **Bloom (2001):** Comprendere — *seguire l'esecuzione, spiegare, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire un ciclo `for`,
  indicando il valore della variabile del ciclo a ogni giro e prevedendo il numero totale di
  ripetizioni.
- **Estensione di Bloom:** un esempio predefinito con accumulatore (`total += i`) lo porta
  verso il livello Applicare.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo; ogni clic fa avanzare di un'istruzione
  (non di un giro intero), così si vede il salto che torna all'inizio del ciclo
- **Piano di implementazione:**
    - A sinistra: `for i in range(4):` + un corpo di 2 righe con la freccia di esecuzione;
      un'etichetta con il valore attuale di `i`; un contatore dei giri ("Giro 2 di 4")
    - A destra: un piccolo canvas della turtle che disegna un lato a ogni giro, collegato
      direttamente al laboratorio del quadrato del capitolo
    - Selettore di esempi predefiniti: disegnare un quadrato, stampare un conto alla
      rovescia, accumulatore (il totale parziale mostrato come una barra che cresce)
    - Pulsanti: Next, Auto-play (lento, con pausa), Reset
    - `CANVAS_HEIGHT` stimato: `500`

### 8. Esploratore di range (`range-explorer`)

- **Capitolo:** 7 (Cicli for e disegno di forme)
- **Concetto e lacuna:** la confusione sull'errore di uno con `range(start, stop, step)`
  ("perché stop non è incluso?") è la principale fonte di bug nei capitoli sui cicli.
- **Bloom (2001):** Applicare — *usare, eseguire, risolvere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di scegliere i valori di start,
  stop e step che producono la sequenza di numeri desiderata.
- **Libreria:** p5.js
- **Schema di interazione:** tre cursori con riscontro immediato, più una modalità sfida
- **Piano di implementazione:**
    - Retta dei numeri da 0 a 20 con i valori generati accesi come puntini pieni; `stop`
      disegnato come un puntino vuoto "non incluso"
    - Cursori: start (0–10), stop (1–20), step (1–5, più un interruttore per i negativi)
    - Indicazione del codice in tempo reale: `range(2, 12, 3)` → `[2, 5, 8, 11]`
    - Modalità sfida: "accendi 3, 6, 9"; lo studente regola i cursori e controlla la
      risposta
    - `CANVAS_HEIGHT` stimato: `440`

### 9. Esploratore del flusso di controllo (`control-flow-explorer`)

- **Capitolo:** 9 (Prendere decisioni con if/else)
- **Concetto e lacuna:** gli studenti conoscono l'output di ogni ramo, ma non vedono mai che
  si accende esattamente un percorso e gli altri vengono saltati, soprattutto nelle catene
  di `elif`.
- **Bloom (2001):** da Comprendere ad Analizzare — *prevedere, seguire l'esecuzione,
  differenziare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di prevedere quale ramo di una
  catena if/elif/else viene eseguito con un certo input e di spiegare perché i rami
  successivi vengono saltati.
- **Libreria:** p5.js (evidenziazione interattiva del percorso guidata da un cursore; è stato
  considerato Mermaid, secondo la regola di instradamento per i diagrammi di flusso, ma la
  sim deve evidenziare di nuovo il percorso in tempo reale in base all'input, e Mermaid non
  lo permette)
- **Schema di interazione:** input con un cursore + percorso evidenziato nel diagramma di
  flusso; opzione di avanzamento passo passo per i controlli delle condizioni
- **Piano di implementazione:**
    - Diagramma di flusso di un programma che assegna i voti (`if score >= 90 … elif …
      else`) disegnato sul canvas; rombi per le condizioni, rettangoli per le azioni
    - Cursore: punteggio da 0 a 100; il percorso scelto si illumina di verde, i rami
      saltati si attenuano; i rombi delle condizioni mostrano in ordine il verdetto
      True/False
    - Modalità passo passo: si vedono le condizioni controllate una alla volta dall'alto
      verso il basso, a dimostrare che vince la prima condizione True
    - Selettore di esempi predefiniti: if semplice, if/else, catena di elif, if annidati
    - `CANVAS_HEIGHT` stimato: `540`

### 10. Laboratorio di logica booleana (`boolean-logic-lab`)

- **Capitolo:** 9 e 19 (Booleani e condizionali)
- **Concetto e lacuna:** le tavole di verità vengono imparate a memoria, non capite; e la
  valutazione a corto circuito (Cap. 19) è completamente invisibile nel codice.
- **Bloom (2001):** da Comprendere ad Applicare — *classificare, spiegare, dimostrare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di stabilire il risultato delle
  espressioni con `and`, `or` e `not` e di spiegare quando Python salta il calcolo del
  secondo operando.
- **Libreria:** p5.js
- **Schema di interazione:** interruttori con riscontro immediato, più una modalità passo
  passo per il corto circuito
- **Piano di implementazione:**
    - Due grandi interruttori True/False collegati a un blocco operatore (selettore
      `and` / `or` / `not`); la lampadina del risultato si accende subito di verde o di rosso
    - Modalità corto circuito: si avanza passo passo in `a and b`; quando `a` è False,
      l'interruttore di `b` diventa grigio con un'etichetta "Python non ha mai guardato qui"
    - Pannello bonus sui valori "veri" e "falsi": scrivi o scegli un valore (`0`, `""`,
      `[]`, `"hi"`, `42`) e vedi il verdetto di `bool()`; copre la tabella dei valori falsi
      del Cap. 19
    - `CANVAS_HEIGHT` stimato: `480`

### 11. Ciclo while passo passo (`while-loop-stepper`)

- **Capitolo:** 10 (Cicli while e animazione)
- **Concetto e lacuna:** il ritmo "controlla la condizione → esegui il corpo → controlla di
  nuovo" è invisibile, e gli studenti non possono sperimentare in sicurezza un ciclo infinito
  in Skulpt.
- **Bloom (2001):** da Comprendere ad Analizzare — *seguire l'esecuzione, prevedere, fare
  debug*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire i controlli della
  condizione di un ciclo while e di capire perché un ciclo termina, o perché non termina mai.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo con una fase esplicita di controllo
  della condizione; dimostrazione protetta di un ciclo infinito
- **Piano di implementazione:**
    - Programma con un conto alla rovescia (`while count > 0:`) in cui la freccia di
      esecuzione passa sulla riga della condizione prima di ogni giro; a ogni passaggio
      viene mostrato il verdetto della condizione (True/False); la casella di memoria di
      `count` si aggiorna in tempo reale
    - Interruttore "Rompi il ciclo": togli la riga `count -= 1` e procedi; un contagiri
      comincia a girare con un avviso ("questo andrebbe avanti per sempre"),
      fermato a 50 giri per sicurezza
    - Pulsanti: Next, Reset; selettore di esempi predefiniti (conto alla rovescia, attesa
      della password, bug del ciclo infinito)
    - `CANVAS_HEIGHT` stimato: `500`

---

## Priorità 2 — Dati e funzioni (Capitoli 11–20)

### 12. Ispettore dello scope (`scope-inspector`)

- **Capitolo:** 11 (Funzioni con parametri e scope)
- **Concetto e lacuna:** lo scope locale e globale e l'oscuramento delle variabili
  (shadowing) sono le idee più astratte della prima metà del libro: variabili che "vivono"
  in stanze invisibili.
- **Bloom (2001):** Analizzare — *differenziare, attribuire, fare debug*
- **Obiettivo di apprendimento:** lo studente sarà in grado di stabilire a quale variabile si
  riferisce un nome in qualsiasi riga, distinguendo variabili locali, globali e oscurate.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo con riquadri di scope annidati (frame)
- **Piano di implementazione:**
    - Un programma con una variabile globale `score` e una funzione che crea una `score`
      locale; il canvas disegna una grande stanza "Globale" e, durante la chiamata, una
      stanza "Funzione" che compare e poi sparisce insieme alle sue variabili
    - Frecce di ricerca del nome: quando una riga legge `score`, una freccia cerca prima
      nella stanza locale e poi in quella globale; così l'oscuramento diventa letteralmente
      visibile
    - Esempi predefiniti: globale in sola lettura, bug di oscuramento, correzione con la
      parola chiave `global`
    - Pulsanti: Next, Reset
    - `CANVAS_HEIGHT` stimato: `520`

### 13. Miscelatore di colori RGB (`rgb-color-mixer`)

- **Capitolo:** 12 (Colori, riempimento e arte con la turtle)
- **Concetto e lacuna:** le stringhe esadecimali come `"#FF6B35"` sembrano formule magiche;
  il passaggio da RGB a esadecimale va manipolato dal vivo.
- **Bloom (2001):** Applicare — *usare, dimostrare, risolvere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di ottenere un colore
  desiderato regolando i valori di rosso, verde e blu, e di leggerne e scriverne il codice
  esadecimale.
- **Libreria:** p5.js
- **Schema di interazione:** tre cursori con riscontro immediato, più una sfida "trova il
  colore"
- **Piano di implementazione:**
    - Un grande campione di colore; cursori R, G, B (0–255) colorati come il proprio canale;
      valori in tempo reale in decimale ed esadecimale, con la coppia esadecimale che cambia
      evidenziata
    - Modalità sfida "Trova questo colore": compare un campione da raggiungere, lo studente
      mescola i colori e un indicatore di vicinanza gli dà un riscontro
    - Una riga di output pronta da copiare: `t.pencolor("#3FA7D6")`, da incollare in
      qualsiasi laboratorio dei capitoli
    - `CANVAS_HEIGHT` stimato: `460`

### 14. Affettatore di stringhe (`string-slicer`)

- **Capitolo:** 14 (Metodi delle stringhe e formattazione), con le basi nel Cap. 8
- **Concetto e lacuna:** le posizioni degli indici (che partono da 0, gli indici negativi) e
  il limite finale escluso dello slicing causano infiniti errori di uno.
- **Bloom (2001):** Applicare — *usare, eseguire, risolvere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di scrivere espressioni con
  indici e slicing che estraggono la sottostringa desiderata.
- **Libreria:** p5.js
- **Schema di interazione:** manipolazione diretta (trascinare le maniglie della porzione)
  con la notazione mostrata in tempo reale
- **Piano di implementazione:**
    - La stringa `"PYTHON ROCKS"` in grandi tessere, una per lettera, con gli indici positivi
      sopra e quelli negativi sotto ogni tessera
    - Due maniglie a parentesi trascinabili selezionano un intervallo; le tessere
      selezionate si evidenziano; l'indicazione mostra `word[2:7]` → `"THON "` in tempo
      reale; un cursore del passo (1–3) aggiunge il terzo argomento dello slicing
    - Clic su una singola tessera per la modalità indice (`word[3]` → `"H"`)
    - Modalità sfida: "estrai ROCKS"; lo studente trascina le maniglie e controlla la
      risposta
    - Casella di testo per provare una parola propria (massimo 12 caratteri)
    - `CANVAS_HEIGHT` stimato: `450`

### 15. Esploratore degli indici delle liste (`list-index-explorer`)

- **Capitolo:** 15–16 (Liste)
- **Concetto e lacuna:** la stessa trappola dell'errore di uno delle stringhe, più la
  modifica: le liste cambiano direttamente (`append`, `pop`, `insert`) e gli studenti non
  vedono mai le caselle spostarsi.
- **Bloom (2001):** da Applicare ad Analizzare — *usare, dimostrare, differenziare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di selezionare elementi con
  indici positivi e negativi e di dimostrare come append, insert, pop e remove modificano
  direttamente la forma di una lista.
- **Libreria:** p5.js
- **Schema di interazione:** operazioni guidate da pulsanti, con aggiornamenti visivi un
  passo alla volta
- **Piano di implementazione:**
    - Una lista di caselle colorate con doppie etichette di indice (0,1,2… e −1,−2,…); gli
      indici si rinumerano in modo visibile ogni volta che la lista cambia
    - Pulsanti delle operazioni: append, insert-at, pop, remove-by-value; ognuno mostra la
      riga di codice equivalente (`colors.append("purple")`) mentre viene eseguita; le
      caselle scorrono per fare spazio o chiudere un buco
    - Pannello di confronto: prova lo stesso "cambia l'elemento 0" su una stringa →
      bloccato con il vero testo del `TypeError` (copre mutabile e immutabile)
    - `CANVAS_HEIGHT` stimato: `480`

### 16. Simulatore di pila e coda (`stack-queue-simulator`)

- **Capitolo:** 16 (Liste — Metodi e pattern), riutilizzata molto nel 30
- **Concetto e lacuna:** l'ordine LIFO e quello FIFO sono questioni di tempo e di spazio;
  l'output del codice da solo non può mostrare perché l'ordine di estrazione è diverso.
- **Bloom (2001):** da Comprendere ad Applicare — *confrontare, dimostrare, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di prevedere l'ordine in cui gli
  elementi escono da una pila rispetto a una coda e di associare ciascuna alle sue
  operazioni sulle liste.
- **Libreria:** p5.js
- **Schema di interazione:** inserimento ed estrazione guidati da pulsanti, con un confronto
  fianco a fianco
- **Piano di implementazione:**
    - Canvas diviso: una pila di piatti (verticale) e una fila d'attesa (orizzontale),
      alimentate dallo stesso pulsante "Aggiungi elemento", così il confronto è controllato
    - Pulsanti: Aggiungi, Togli (la pila toglie l'elemento in cima, la coda quello davanti),
      con l'equivalente con i metodi delle liste (`stack.pop()` e `queue.pop(0)`)
    - Gettone di previsione prima di ogni Togli: "quale elemento esce?", si clicca per
      indovinare
    - Strisce con la cronologia delle estrazioni sotto ogni struttura, per confrontare gli
      ordini finali
    - `CANVAS_HEIGHT` stimato: `520`

### 17. Istogramma dei lanci di dado (`dice-roll-histogram`)

- **Capitolo:** 17 (Moduli e numeri casuali)
- **Concetto e lacuna:** una singola chiamata a `randint()` sembra puro caos; la
  distribuzione uniforme emerge solo dopo molte prove, ed è impossibile vederla in un
  laboratorio di 10 righe.
- **Bloom (2001):** Analizzare — *organizzare, confrontare, attribuire*
- **Obiettivo di apprendimento:** lo studente sarà in grado di analizzare come la
  distribuzione dei lanci casuali si appiattisce al crescere del numero di prove, e di
  confrontare un dado con la somma di due dadi.
- **Libreria:** Chart.js (instradamento: grafico/barre/statistica) con controlli a pulsanti
- **Schema di interazione:** esecutore di esperimenti: lo studente lancia dei gruppi di prove
  e confronta i risultati
- **Piano di implementazione:**
    - Grafico a barre dei conteggi per le facce da 1 a 6; pulsanti: Lancia 1, Lancia 100,
      Lancia 1000, Reset; totale progressivo ed etichette con la percentuale di ogni faccia
    - Interruttore di modalità: un dado (piatto) contro la somma di due dadi (un triangolo
      attorno al 7), un momento di scoperta davvero sorprendente
    - Casella facoltativa per il seme, che dimostra le sequenze "casuali" riproducibili
      (collegata a `random.seed()` nel capitolo)
    - `CANVAS_HEIGHT` stimato: `505`

### 18. Esploratore dell'onda sinusoidale (`sine-wave-explorer`)

- **Capitolo:** 18 (Modulo math e progetti con la turtle)
- **Concetto e lacuna:** il progetto dell'onda sinusoidale con la turtle del capitolo
  funziona, ma gli studenti devono modificare e rieseguire il codice per percepire ampiezza e
  frequenza; i cursori danno un ciclo di riscontro molto più stretto.
- **Bloom (2001):** Applicare — *dimostrare, usare, risolvere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di dimostrare come ampiezza,
  frequenza e fase cambiano ciascuna la forma di un'onda sinusoidale.
- **Libreria:** Plotly.js (instradamento: funzione matematica f(x))
- **Schema di interazione:** cursori dei parametri con nuovo grafico immediato
- **Piano di implementazione:**
    - Grafico di `y = A * sin(f * x + p)` tra 0 e 4π; cursori per l'ampiezza (0,5–3), la
      frequenza (0,5–4) e la fase (0–2π)
    - Annotazione in tempo reale dell'equazione con i valori attuali sostituiti
    - Casella "Fantasma" che mantiene la curva precedente attenuata per il confronto
    - `CANVAS_HEIGHT` stimato: `475`

### 19. Circonferenza unitaria: gradi e radianti (`unit-circle-radians`)

- **Capitolo:** 18 (Modulo math e progetti con la turtle)
- **Concetto e lacuna:** `math.sin()` vuole i radianti; gli studenti conoscono solo i gradi
  delle rotazioni della turtle. La conversione ha bisogno di un punto di riferimento spaziale.
- **Bloom (2001):** da Comprendere ad Applicare — *interpretare, convertire, usare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di convertire tra gradi e
  radianti e di individuare un angolo sulla circonferenza unitaria.
- **Libreria:** p5.js
- **Schema di interazione:** si trascina il punto dell'angolo; due indicazioni si aggiornano
  in tempo reale
- **Piano di implementazione:**
    - Circonferenza unitaria con un punto trascinabile; l'arco percorso si colora; le
      indicazioni mostrano i gradi, i radianti (sia in decimale sia come multipli di π) e i
      valori di seno e coseno, con le linee di proiezione sugli assi
    - Pulsanti di aggancio per gli angoli di riferimento (0°, 90°, 180°, 270°, 45°)
    - Un'icona della turtle al centro della circonferenza ruota di conseguenza, per collegare
      le direzioni della turtle alla matematica
    - `CANVAS_HEIGHT` stimato: `520`

### 20. Diagramma di Venn delle operazioni sugli insiemi (`set-operations-venn`)

- **Capitolo:** 20 (Tuple e insiemi)
- **Concetto e lacuna:** unione, intersezione e differenza sono per natura spaziali; l'output
  testuale `{...}` nasconde la struttura delle sovrapposizioni.
- **Bloom (2001):** da Comprendere ad Analizzare — *classificare, confrontare, organizzare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di classificare quali elementi
  appartengono ad A | B, A &amp; B, A − B e A ^ B, dati due insiemi.
- **Libreria:** Venn personalizzato (instradamento: insiemi/sovrapposizioni → guida venn)
- **Schema di interazione:** insiemi modificabili + pulsanti delle operazioni che evidenziano
  le regioni
- **Piano di implementazione:**
    - Diagramma di Venn a due cerchi con dei gettoni per gli elementi, collocati nelle
      regioni giuste a partire da due insiemi modificabili (input separati da virgole, per
      esempio gli animali domestici che vogliono Alice e Bob)
    - Pulsanti delle operazioni: `A | B`, `A & B`, `A - B`, `A ^ B`; la regione
      corrispondente si illumina e sotto vengono stampati l'espressione Python e l'insieme
      risultante
    - Dimostrazione dei duplicati: scrivendo un elemento due volte, i due gettoni si fondono
      visibilmente in uno (gli insiemi eliminano i duplicati)
    - `CANVAS_HEIGHT` stimato: `560`

---

## Priorità 3 — Informatica di livello intermedio (Capitoli 21–30)

### 21. Ricerca per chiave nei dizionari (`dictionary-key-lookup`)

- **Capitolo:** 21 (Dizionari)
- **Concetto e lacuna:** perché la ricerca in un dizionario è istantanea, e perché le chiavi
  devono essere esatte? Il meccanismo che associa chiave → valore è invisibile; il `KeyError`
  sembra arbitrario.
- **Bloom (2001):** Comprendere — *spiegare, confrontare, dedurre*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare come un dizionario
  trova un valore a partire da una chiave e perché una chiave mancante solleva un KeyError
  mentre `.get()` no.
- **Libreria:** p5.js
- **Schema di interazione:** ricerca scrivendo una chiave, con avanzamento passo passo della
  ricerca; confronto tra lista e dizionario
- **Piano di implementazione:**
    - Un dizionario-rubrica disegnato come una serie di cassetti chiave/valore; lo studente
      scrive una chiave e il cassetto corrispondente si apre mostrando il valore; una chiave
      sbagliata mostra il banner rosso del `KeyError`, mentre con l'interruttore `.get()` si
      ottiene educatamente `None`
    - Modalità confronto: trovare la stessa voce in una lista (scorrendo gli elementi uno a
      uno e contando i controlli) e nel dizionario (un solo salto); un primo seme dell'idea
      di Big-O, senza i dettagli interni delle tabelle hash (una semplificazione adatta
      all'età)
    - Modalità aggiungi/aggiorna: assegnare un valore a una chiave esistente lo sostituisce;
      assegnarlo a una chiave nuova crea un nuovo cassetto
    - `CANVAS_HEIGHT` stimato: `500`

### 22. Stack delle chiamate nella ricorsione (`recursion-call-stack`)

- **Capitolo:** 24 (Ricorsione e frattali), riutilizzabile nel 23 (traceback)
- **Concetto e lacuna:** lo stack delle chiamate è *la* macchina invisibile per eccellenza.
  Gli studenti vedono `factorial(5) = 120` ma non i frame che si impilano e poi si
  svuotano, che è anche esattamente ciò che stampa un traceback.
- **Bloom (2001):** Analizzare — *scomporre, organizzare, seguire l'esecuzione*
- **Obiettivo di apprendimento:** lo studente sarà in grado di scomporre una chiamata
  ricorsiva in frame dello stack, di identificare il caso base e di seguire i valori che
  tornano indietro lungo lo stack.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo; i frame vengono aggiunti e tolti un
  clic alla volta, con tutti i valori visibili
- **Piano di implementazione:**
    - A sinistra: il codice di `factorial(n)` con la riga corrente evidenziata; a destra: lo
      stack disegnato come frame fisici, ognuno con il proprio `n` e il proprio
      `return n * factorial(n-1)` in sospeso
    - Nella fase di inserimento i frame si impilano verso l'alto finché il caso base non si
      illumina d'oro; nella fase di estrazione ogni moltiplicazione in sospeso viene
      completata mentre i valori scendono
    - Esempi predefiniti: `factorial(4)`, `countdown(3)` e un bug con il caso base mancante
      che sbatte contro un soffitto "RecursionError" (al massimo 8 frame disegnati)
    - Pulsanti: Next, Previous, Reset; contatore dei frame
    - `CANVAS_HEIGHT` stimato: `560`

### 23. Esploratore dell'albero frattale (`fractal-tree-explorer`)

- **Capitolo:** 24 (Ricorsione e frattali)
- **Concetto e lacuna:** il laboratorio sui frattali del capitolo richiede di modificare e
  rieseguire il codice a ogni cambio di parametro; dei cursori in tempo reale rivelano la
  sensibilità ai parametri che rende i frattali così entusiasmanti.
- **Bloom (2001):** da Applicare a Creare — *dimostrare, sperimentare, progettare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di dimostrare come l'angolo dei
  rami, la profondità e il fattore di riduzione danno forma a un albero ricorsivo, e di
  progettare un albero tutto suo.
- **Libreria:** p5.js
- **Schema di interazione:** cursori dei parametri con nuovo disegno immediato (adatto: livello
  Applicare con riscontro in tempo reale)
- **Piano di implementazione:**
    - Un albero ricorsivo che occupa tutto il canvas; cursori: angolo dei rami (10–60°),
      profondità (1–9), fattore di riduzione (0,5–0,8); il cursore della profondità serve
      anche a mostrare dal vivo i livelli di ricorsione (ogni profondità ha il suo colore)
    - Pulsanti "Casuale" e "Istantanea"; l'istantanea sovrappone un'immagine fantasma per il
      confronto
    - Un'indicazione mostra il numero di chiamate ricorsive, collegando la bellezza
      dell'albero alla sim dello stack delle chiamate (#22)
    - `CANVAS_HEIGHT` stimato: `540`

### 24. Ispettore delle istanze di un oggetto (`object-instance-inspector`)

- **Capitolo:** 25 (Programmazione orientata agli oggetti)
- **Concetto e lacuna:** `self` e gli attributi d'istanza: quale `name` appartiene a quale
  cane? Gli studenti confondono la classe (il progetto) con le sue istanze.
- **Bloom (2001):** Comprendere — *spiegare, esemplificare, differenziare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare la differenza tra una
  classe e le sue istanze e di identificare a quale oggetto si riferisce `self` durante la
  chiamata di un metodo.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo nella costruzione degli oggetti e nelle
  chiamate dei metodi, con dei riquadri per le istanze
- **Piano di implementazione:**
    - In alto: la scheda della classe `Dog` (in stile progetto, con il bordo tratteggiato)
      con `__init__` e `bark`; sotto, le istanze compaiono come schede piene con i propri
      valori di `name`/`age` man mano che si avanza in `Dog("Rex", 3)` ecc.
    - Durante `rex.bark()`, una freccia luminosa `self` collega il metodo nel progetto alla
      scheda di rex, e le letture degli attributi prendono i valori solo da quella scheda
    - Dimostrazione delle variabili di classe: un campo condiviso `species` disegnato una
      sola volta sul progetto, con frecce tratteggiate da tutte le istanze
    - `CANVAS_HEIGHT` stimato: `540`

### 25. Esploratore dell'ereditarietà (`inheritance-explorer`)

- **Capitolo:** 25 (Programmazione orientata agli oggetti)
- **Concetto e lacuna:** la ricerca dei metodi risalendo la gerarchia delle classi (e la
  ridefinizione dei metodi più `super()`) è un meccanismo di scelta invisibile.
- **Bloom (2001):** Analizzare — *attribuire, organizzare, differenziare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di stabilire quale metodo di quale
  classe viene eseguito quando si chiama un metodo su un'istanza di una sottoclasse.
- **Libreria:** vis-network (instradamento: gerarchia di nodi e archi) con un pannello delle
  chiamate
- **Schema di interazione:** si clicca su una chiamata di metodo e si guarda la ricerca che
  risale l'albero
- **Piano di implementazione:**
    - Una rete di nodi di classe `Animal` → `Dog` / `Cat`, ognuno con l'elenco dei suoi
      metodi; un nodo istanza è appeso sotto `Dog`
    - Pulsanti per le chiamate (`d.speak()`, `d.eat()`); il percorso di ricerca si anima nodo
      per nodo risalendo la gerarchia finché non si evidenzia una corrispondenza; i metodi
      ridefiniti mostrano la versione del genitore in grigio con un'etichetta "oscurato"
    - L'esempio predefinito con `super()` mostra un metodo figlio che poi risale
      esplicitamente al genitore
    - `CANVAS_HEIGHT` stimato: `600`

### 26. Corrispondenza tra tipi JSON e Python (`json-python-mapper`)

- **Capitolo:** 27 (Libreria standard e JSON)
- **Concetto e lacuna:** JSON somiglia in modo ingannevole a Python; le differenze
  (`true`/`True`, `null`/`None`, le chiavi devono essere stringhe) creano confusione senza
  dare errori.
- **Bloom (2001):** da Comprendere ad Applicare — *interpretare, convertire, classificare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di convertire valori tra testo
  JSON e oggetti Python e di identificare la corrispondenza tra i tipi in entrambe le
  direzioni.
- **Libreria:** HTML personalizzato (editor a due riquadri; instradamento: interazione
  personalizzata in stile matrice/pannello di dettaglio)
- **Schema di interazione:** riquadri modificabili affiancati, con evidenziazione dei tipi
- **Piano di implementazione:**
    - Riquadro sinistro: testo JSON; riquadro destro: il valore Python risultante;
      modificando uno dei due lati si aggiorna l'altro, con un colore per ogni elemento
      (object↔dict, array↔list, true↔True, null↔None)
    - Passando sopra un elemento compare un suggerimento con il nome di entrambi i tipi
    - Esempi predefiniti con errori voluti: apici singoli in JSON, virgola finale, con
      spiegazioni amichevoli degli errori di lettura
    - `CANVAS_HEIGHT` stimato: `520`

### 27. Laboratorio delle corrispondenze regex (`regex-match-lab`)

- **Capitolo:** 29 (Elaborazione del testo ed espressioni regolari)
- **Concetto e lacuna:** le regex sono un linguaggio di regole invisibili; gli studenti hanno
  bisogno di vedere le corrispondenze evidenziate dal vivo per collegare i pezzi dello schema
  ai caratteri trovati.
- **Bloom (2001):** da Applicare ad Analizzare — *usare, testare, scomporre*
- **Obiettivo di apprendimento:** lo studente sarà in grado di provare un'espressione
  regolare su un testo di esempio e di attribuire ogni corrispondenza all'elemento dello
  schema che l'ha prodotta.
- **Libreria:** HTML personalizzato (campi di input + evidenziazione; non serve un canvas)
- **Schema di interazione:** editor dello schema in tempo reale, con una spiegazione pezzo per
  pezzo
- **Piano di implementazione:**
    - Campo per lo schema (precompilato con `\d{3}-\d{4}`) sopra un'area di testo di
      esempio; tutte le corrispondenze si evidenziano in tempo reale; un contatore delle
      corrispondenze rispecchia `re.findall`
    - Striscia di spiegazione dello schema: lo schema mostrato come gettoni (`\d` "una
      cifra", `{3}` "tre volte", `-` "un trattino"); passando sopra un gettone lampeggiano i
      caratteri che ha trovato
    - Schemi predefiniti: numeri di telefono, parole che iniziano con la maiuscola, cifre,
      vocali; testi predefiniti in cui cercare
    - Ambito adatto all'età: solo gli elementi del capitolo (`\d \w \s . * + ?
      {n,m} [] ^ $ |`)
    - `CANVAS_HEIGHT` stimato: `540`

### 28. Confronto tra algoritmi di ordinamento (`sorting-comparer`)

- **Capitolo:** 30 (Algoritmi e strutture dati)
- **Concetto e lacuna:** bubble sort, selection sort e insertion sort differiscono solo nella
  loro coreografia di confronti e scambi: invisibile nel codice, evidente in un'animazione.
- **Bloom (2001):** da Analizzare a Valutare — *confrontare, organizzare, giudicare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di confrontare come bubble sort,
  selection sort e insertion sort riordinano gli stessi dati e di giudicare quale fa meno
  lavoro con un certo input.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo a ogni confronto, con l'opzione di una
  gara automatica per l'obiettivo di livello Valutare
- **Piano di implementazione:**
    - Grafico a barre di 10 valori; selettore dell'algoritmo; il pulsante Step evidenzia la
      coppia che viene confrontata e anima gli scambi; contatori dei confronti e degli
      scambi
    - Modalità gara: due pannelli con algoritmi diversi ordinano gli stessi dati fianco a
      fianco, con contatori delle operazioni in tempo reale
    - Dati predefiniti: casuali, quasi ordinati, invertiti; mostrano perché "dipende dai
      dati"
    - Pulsante Mescola per avere nuovi dati
    - `CANVAS_HEIGHT` stimato: `560`

### 29. Gara di ricerca (`search-race`)

- **Capitolo:** 30 (Algoritmi e strutture dati)
- **Concetto e lacuna:** il Big-O è astratto; vivere sulla propria pelle la ricerca binaria
  che dimezza 100 elementi in 7 controlli rende concreta l'efficienza.
- **Bloom (2001):** da Analizzare a Valutare — *confrontare, testare, motivare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di confrontare il numero di
  controlli che servono alla ricerca lineare e a quella binaria e di motivare perché la
  ricerca binaria richiede dati ordinati.
- **Libreria:** p5.js
- **Schema di interazione:** si sceglie un obiettivo, poi si fanno avanzare le due ricerche
  passo passo o in gara
- **Piano di implementazione:**
    - Uno scaffale ordinato di 31 scatole numerate, ripetuto su due corsie; lo studente
      sceglie un obiettivo; la modalità Step fa avanzare entrambe le ricerche di un controllo
      alla volta: quella lineare arranca da sinistra a destra, quella binaria salta al
      centro e rende grigia la metà scartata
    - Contatori dei controlli per ogni corsia; banner dei risultati ("binaria: 5 controlli,
      lineare: 24")
    - Esempio predefinito "Trappola dei dati non ordinati": eseguire la ricerca binaria su
      dati mescolati e vederla fallire, per rispondere al *perché l'ordine conta*
    - `CANVAS_HEIGHT` stimato: `520`

### 30. Esploratore della visita dei grafi (`graph-traversal-explorer`)

- **Capitolo:** 30 (Algoritmi e strutture dati); rafforza anche i contenuti sui labirinti in
  `docs/intermediate/`
- **Concetto e lacuna:** l'onda livello per livello di BFS e il tuffo in profondità di DFS
  sono questioni di spazio e di tempo; la vera lezione è la coda o la pila nascosta che
  guida ciascuna.
- **Bloom (2001):** Analizzare — *differenziare, organizzare, seguire l'esecuzione*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire l'ordine di visita di
  BFS e DFS sullo stesso grafo e di attribuire la differenza alla coda rispetto alla pila.
- **Libreria:** vis-network (instradamento: nodi/archi) con un pannello laterale
- **Schema di interazione:** avanzamento passo passo, con la struttura dati della frontiera
  mostrata in tempo reale
- **Piano di implementazione:**
    - Un grafo di 10 nodi; interruttore di modalità BFS/DFS; il pulsante Step visita il nodo
      successivo (numerato nell'ordine di visita); il pannello laterale mostra il contenuto
      attuale della coda (BFS) o della pila (DFS) dopo ogni passo
    - Il nodo di partenza si sceglie cliccandolo; Reset dispone di nuovo i nodi a caso
    - La ricompensa del percorso più breve: quando BFS ha finito, si evidenzia il percorso
      più breve verso un nodo di arrivo, il momento del "ecco perché BFS"
    - `CANVAS_HEIGHT` stimato: `620`

---

## Priorità 4 — Argomenti avanzati (Capitoli 31–38)

### 31. Visualizzatore del broadcasting di NumPy (`numpy-broadcasting`)

- **Capitolo:** 33 (NumPy e calcolo scientifico)
- **Concetto e lacuna:** `array + 5` estende in silenzio lo scalare su ogni elemento; niente
  nell'output stampato mostra come vengono accoppiati i valori.
- **Bloom (2001):** Comprendere — *spiegare, dedurre, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare come uno scalare o un
  array più piccolo viene esteso per adattarsi a un array più grande durante le operazioni
  elemento per elemento.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo, un accoppiamento di elementi alla volta
- **Piano di implementazione:**
    - Un array a 1 dimensione disegnato come una riga di celle; lo scalare (o l'array di una
      riga) disegnato una volta sola e poi copiato come fantasma sotto ogni cella man mano che
      si avanza; ogni passo calcola una cella dell'output
    - Esempi predefiniti: array + scalare, array + array (stessa lunghezza), griglia a 2
      dimensioni + riga (il classico caso di broadcasting); l'esempio con lunghezze diverse
      mostra il vero ValueError
    - Selettore dell'operazione: `+`, `*`, `>` (in uscita dei booleani: una bella sorpresa)
    - `CANVAS_HEIGHT` stimato: `500`

### 32. Editor di griglie di pixel (`pixel-grid-editor`)

- **Capitolo:** 34 (Elaborazione delle immagini con Pillow)
- **Concetto e lacuna:** "un'immagine è una griglia di tuple RGB" viene detto ma non
  percepito; modificare i singoli pixel chiude il cerchio.
- **Bloom (2001):** da Applicare a Creare — *dimostrare, produrre, costruire*
- **Obiettivo di apprendimento:** lo studente sarà in grado di costruire un'immagine
  impostando i valori RGB dei pixel e di dimostrare su che cosa lavorano
  `getpixel`/`putpixel`.
- **Libreria:** p5.js
- **Schema di interazione:** canvas a manipolazione diretta (livello Creare: strumento di
  costruzione)
- **Piano di implementazione:**
    - Griglia di 16×16 pixel, molto ingrandita; i cursori RGB impostano il colore della
      "vernice"; si clicca o si trascina per dipingere; passando sopra un pixel se ne vedono
      le coordinate e la tupla `(255, 107, 53)`, cioè la vista di `getpixel`
    - Un riquadro "Dimensioni reali" mostra l'immagine vera da 16×16 accanto a quella
      ingrandita
    - Pulsanti di trasformazione: scala di grigi, inverti, capovolgi in orizzontale; ognuno
      descritto con il calcolo che fa sui pixel (per esempio grigio = media di R, G, B)
    - `CANVAS_HEIGHT` stimato: `560`

### 33. Visualizzatore del ciclo degli eventi (`event-loop-visualizer`)

- **Capitolo:** 35 (Turtle avanzata e programmazione guidata da eventi)
- **Concetto e lacuna:** "registra una callback e aspetta" ribalta tutto ciò che gli
  studenti sanno sull'esecuzione dall'alto verso il basso; il ciclo che smista gli eventi è
  invisibile.
- **Bloom (2001):** Comprendere — *spiegare, interpretare, prevedere*
- **Obiettivo di apprendimento:** lo studente sarà in grado di spiegare come un programma
  registra i gestori di eventi e di prevedere quale gestore viene eseguito per un certo
  evento.
- **Libreria:** p5.js
- **Schema di interazione:** lo studente È la fonte degli eventi: i clic e i tasti premuti
  dentro la sim alimentano un percorso di smistamento visibile
- **Piano di implementazione:**
    - A sinistra: un piccolo schermo della turtle su cui lo studente clicca o preme dei tasti;
      al centro: una coda degli eventi in cui ogni evento compare come un biglietto (CLICK a
      (x, y), KEY "space"); a destra: la tabella dei gestori (`onscreenclick → jump`,
      `onkey space → change color`)
    - Ogni biglietto viaggia in modo visibile fino alla riga del suo gestore, che lampeggia e
      produce il suo effetto sul piccolo schermo; gli eventi senza gestore cadono in un
      cestino "nessun gestore registrato"
    - Interruttore del rallentatore per allungare i passi dello smistamento
    - `CANVAS_HEIGHT` stimato: `540`

### 34. Esploratore dell'overfitting (`overfitting-explorer`)

- **Capitolo:** 37 (Fondamenti di machine learning)
- **Concetto e lacuna:** l'overfitting è invisibile nel codice e compare solo come curve che
  si allontanano; gli studenti devono provocarlo con le proprie mani per crederci.
- **Bloom (2001):** da Analizzare a Valutare — *confrontare, attribuire, giudicare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di analizzare le curve di
  addestramento e di validazione e di giudicare quando un modello ha cominciato a
  memorizzare invece di imparare.
- **Libreria:** Chart.js (grafico a linee) con una riga di controlli senza p5.js
- **Schema di interazione:** cursore della complessità con risposta immediata delle curve
- **Piano di implementazione:**
    - A sinistra: un grafico a dispersione di circa 20 punti in 2 dimensioni con una curva
      adattata, che diventa più ondulata seguendo un cursore della "complessità del
      modello" (1 = linea retta, 10 = passa per ogni punto)
    - A destra: le linee dell'errore di addestramento e di validazione, ridisegnate a ogni
      movimento del cursore; la zona in cui si allontanano si colora di rosso con
      l'etichetta "sta memorizzando!"
    - Il pulsante "Nuovi dati" aggiunge punti di validazione nuovi sulla curva adattata, così
      gli studenti vedono il modello in overfitting sbagliare di molto
    - Dati precalcolati (nessun vero addestramento) che la rendono istantanea e indipendente
      da Skulpt
    - `CANVAS_HEIGHT` stimato: `540`

### 35. Passaggio in avanti di una rete neurale (`nn-forward-pass`)

- **Capitolo:** 37–38 (Machine learning; Reti neurali e MNIST)
- **Concetto e lacuna:** strati, pesi e funzioni di attivazione hanno un nome nel codice
  (`Dense(128, activation="relu")`), ma il flusso dei dati è una scatola nera.
- **Bloom (2001):** da Comprendere ad Analizzare — *spiegare, seguire l'esecuzione,
  attribuire*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire un input attraverso
  una piccolissima rete, spiegando come pesi e funzioni di attivazione determinano l'output
  di ogni strato.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo, uno strato alla volta, con tutti i
  numeri visibili (livello Comprendere: dati concreti, niente effetti particellari)
- **Piano di implementazione:**
    - Una piccolissima rete 2–3–2 disegnata con cerchi e archi pesati (spessore dell'arco =
      grandezza del peso, colore = segno); due cursori per gli input
    - Il pulsante Step fa avanzare di uno strato: i valori in entrata vengono moltiplicati
      lungo gli archi, sommati in ogni neurone e poi passano dalla porta ReLU (i valori sono
      mostrati a ogni fase in piccole indicazioni)
    - Modalità "spingi il peso": si trascina il peso di un arco e si vede l'output cambiare;
      prepara l'idea che "l'addestramento regola i pesi" per il Cap. 38
    - `CANVAS_HEIGHT` stimato: `560`

### 36. Esploratore dei kernel di convoluzione (`convolution-explorer`)

- **Capitolo:** 38 (Reti neurali e MNIST), rafforza i filtri del Cap. 34
- **Concetto e lacuna:** il kernel 3×3 che scorre è il cuore delle CNN e dei filtri di
  Pillow, ed è un'idea puramente spaziale: l'argomento ideale per una MicroSim.
- **Bloom (2001):** da Comprendere ad Analizzare — *spiegare, seguire l'esecuzione,
  confrontare*
- **Obiettivo di apprendimento:** lo studente sarà in grado di seguire il calcolo di
  moltiplicazione e somma per una posizione del kernel e di confrontare che cosa mettono in
  risalto i kernel di rilevamento dei bordi, di sfocatura e di nitidezza.
- **Libreria:** p5.js
- **Schema di interazione:** avanzamento passo passo tra le posizioni del kernel, più un
  selettore del kernel
- **Piano di implementazione:**
    - A sinistra: una griglia di input 8×8 in scala di grigi (esempio predefinito: un "7"
      disegnato a mano); una finestra del kernel 3×3 scorre di un passo a ogni clic; al
      centro: il calcolo ingrandito di moltiplicazione e somma per la posizione attuale; a
      destra: la mappa delle caratteristiche in uscita, che si riempie cella per cella
    - Kernel predefiniti: sfocatura, nitidezza, bordi verticali, bordi orizzontali; celle del
      kernel modificabili per i più avventurosi
    - Il pulsante di completamento automatico riempie velocemente il resto dell'output una
      volta capito il concetto; vista di confronto prima/dopo
    - `CANVAS_HEIGHT` stimato: `580`

---

## Da fare — Idee valide escluse dalla prima ondata

Queste idee sono emerse dall'analisi dei capitoli, ma sono più specifiche, in parte coperte da
una sim della prima ondata, oppure si prestano meglio a un testo più un laboratorio Skulpt. Le
teniamo qui per non perdere nulla.

| Idea | Capitolo | Bloom | Note |
|------|---------|-------|-------|
| Raggruppatore dei blocchi indentati | 2 | Comprendere — *classificare* | Una bolla di scope animata attorno alle righe indentate; in parte coperta dalle #1 e #9 |
| Interprete delle sequenze di escape | 8 | Comprendere — *interpretare* | Lettura carattere per carattere di `\n`, `\t`, `\\`; piccola sim in p5.js |
| Percorso della conversione di tipo | 13 | Comprendere — *seguire l'esecuzione* | Il viaggio `input() → "42" → int() → 42`; si abbina alla #2 |
| Confronto tra HSL e RGB | 12 | Comprendere — *confrontare* | Una modalità aggiuntiva della #13 più che una sim a sé |
| Accoppiamento in parallelo con zip() | 22 | Comprendere — *spiegare* | Due liste percorse in parallelo; piccola sim passo passo |
| Catena di map/filter | 22, 31 | Analizzare — *organizzare* | Gettoni di dati che scorrono attraverso le scatole delle funzioni |
| Annotatore dei traceback | 23 | Analizzare — *scomporre* | L'anatomia di un vero traceback con i colori; la #22 copre la parte sullo stack |
| Modalità e puntatore dei file | 26 | Comprendere — *differenziare* | Le posizioni del puntatore con r/w/a; di nicchia ma economica da costruire |
| Visualizzatore CSV a due riquadri | 26 | Comprendere — *interpretare* | Vista sincronizzata tra testo grezzo e tabella |
| Grafico delle frequenze con Counter | 27 | Applicare — *usare* | Grafico a barre di `Counter.most_common()` in tempo reale; Chart.js |
| Scelta dei metodi dunder | 31 | Analizzare — *attribuire* | Quale `__dunder__` viene chiamato da `obj + other`? |
| Albero della gerarchia delle eccezioni | 31 | Comprendere — *classificare* | Albero in vis-network delle eccezioni built-in |
| Scelta del tipo di grafico | 32 | Valutare — *giudicare* | Gli stessi dati come linee/barre/dispersione/istogramma; "quale grafico dice la verità?" |
| Simulatore del cambio di forma degli array | 33 | Comprendere — *interpretare* | Si guardano gli elementi riorganizzarsi con `reshape()` |
| Animazione del max pooling | 38 | Comprendere — *spiegare* | Da integrare nella #36 come seconda modalità |
| Divisione addestramento/validazione/test | 37 | Comprendere — *classificare* | Si trascinano i punti in tre contenitori; in parte coperta dalla #34 |
| Costruttore dell'albero di scomposizione | 36 | Creare — *pianificare* | Scomporre un problema in sotto-compiti in modo interattivo |
| Cronologia dei commit Git | 36 | Comprendere — *riassumere* | Una vis-timeline di una piccola cronologia con diramazioni |

---

## Ordine di costruzione suggerito

1. **Progetto pilota (per verificare il processo):** #7 Ciclo for passo passo, #13
   Miscelatore di colori RGB, #14 Affettatore di stringhe; una sim passo passo, una con i
   cursori e una a manipolazione diretta: tre schemi di interazione diversi lungo tutto il
   processo del generatore (struttura → js → validazione → altezze degli iframe →
   Playwright → screenshot → revisione dell'impaginazione)
2. **Completamento della priorità 1** nell'ordine dei capitoli: queste servono a tutti i
   lettori
3. **Priorità 2, poi priorità 3**, dando la precedenza alla #22 Stack delle chiamate nella
   ricorsione e alle #28/#29 (ordinamento/ricerca), le visualizzazioni di informatica più
   richieste
4. **Priorità 4** man mano che i capitoli avanzati acquistano lettori

Ogni sim dovrebbe essere generata con il percorso per singola sim di `microsim-generator`
(Step 1B), inserita nel suo capitolo con una domanda di previsione `mascot-thinking`
subito sopra l'iframe, e collegata dalla galleria in `docs/sims/index.md`.
