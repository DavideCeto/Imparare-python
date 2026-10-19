---
title: Descrizione del corso Introduzione a Python
description: Una descrizione dettagliata del corso Introduzione a Python con panoramica, argomenti trattati e obiettivi di apprendimento secondo la Tassonomia di Bloom rivista nel 2001
quality_score: 96
---

# Introduzione a Python

**Titolo:** Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty

**Destinatari:** studenti della scuola primaria e secondaria di primo grado, di circa 10–14 anni,
che hanno completato almeno un semestre di programmazione a blocchi (per esempio Scratch, Snap!
o MIT App Inventor) e sono pronti a passare alla programmazione testuale.

**Prerequisiti:** familiarità con i concetti della programmazione a blocchi come sequenze,
cicli, condizioni e variabili (per esempio Scratch o un ambiente equivalente). Non serve alcuna
esperienza di programmazione testuale. Capacità di lettura e di aritmetica di base, al livello
di una classe quarta della scuola primaria. Saper usare la tastiera aiuta. Gli studenti devono
saper usare le funzioni di copia e incolla, oppure avere l'aiuto di un adulto o di un tutor.

---

## Panoramica del corso

Introduzione a Python è un corso divertente e basato su progetti che accompagna i giovani
programmatori nel percorso dalla programmazione a blocchi alla scrittura di vero codice Python.
Per tutto il corso gli studenti sono affiancati da **Monty**, un pitone mascotte simpatico e
curioso che presenta i nuovi concetti, offre suggerimenti, festeggia i successi e aiuta a
rendere concrete le idee astratte. Monty vive direttamente nelle pagine del corso: gli studenti
leggono i suoi consigli accanto alle finestre di codice interattive basate su **Skulpt**, un
motore Python che funziona nel browser e permette di eseguire codice Python senza installare
nulla.

Il corso parte da dove gli studenti si trovano già, usando la grafica turtle per disegnare
forme come forse hanno fatto in Scratch, e poi costruisce un po' alla volta il modo di
ragionare tipico della programmazione testuale: variabili, cicli, funzioni e strutture dati.
Lungo il percorso gli studenti incontrano progetti colorati come disegni animati, generatori di
arte casuale, selettori di colori interattivi, frattali ricorsivi e algoritmi che risolvono
labirinti. Ogni concetto viene presentato con una breve storia di Monty, un esempio interattivo
che gli studenti possono eseguire e modificare subito e un breve quiz per fissare ciò che hanno
imparato.

Oltre il livello base, il corso si estende al **Python intermedio** (tipi di dati, dizionari,
input/output su file, espressioni regolari, basi della programmazione orientata agli oggetti,
debugging e algoritmi sui grafi) e al **Python avanzato** (visualizzazione dei dati con
matplotlib, calcolo numerico con NumPy, elaborazione delle immagini e un'introduzione al machine
learning con il dataset MNIST di cifre scritte a mano). Un **[glossario](./glossary.md)**
completo, una sezione di **[domande frequenti](./faq.md)**, i **quiz di ogni lezione** e una
**[guida per gli insegnanti](./teachers-guide/index.md) dettagliata** rendono il corso
ugualmente utile per chi studia da solo e per chi insegna in classe.

Questo corso è importante perché Python è costantemente indicato come il linguaggio più popolare
al mondo per iniziare a programmare, è alla base di scoperte nella scienza, nell'analisi dei
dati e nell'intelligenza artificiale, ed è il linguaggio preferito per i progetti con Raspberry
Pi e per la comunità dei Maker. Partendo dalla grafica turtle, che offre un riscontro visivo e
immediato, e accompagnando gli studenti con gradualità verso le strutture dati e il machine
learning, questo corso offre ai giovani una vera rampa di accesso alle competenze di
programmazione moderne e professionali, mantenendo l'esperienza gioiosa e motivante.

---

## Argomenti principali

1. **Ambienti e strumenti Python**: Skulpt (integrato nelle pagine), Repl.it, Thonny,
   VS Code, Jupyter Notebook, Raspberry Pi e l'installazione di Python sul proprio computer
2. **Sintassi di base di Python**: print, commenti, indentazione, parole chiave, variabili,
   assegnazione, convenzioni per i nomi e aritmetica di base
3. **Tipi di dati**: numeri interi, numeri decimali (float), booleani, stringhe, None e
   conversione di tipo
4. **Controllo del flusso**: condizioni if/elif/else, cicli for, cicli while, break, continue,
   cicli annidati e range()
5. **Funzioni**: definire e chiamare funzioni, parametri, valori di ritorno, scope,
   ricorsione, docstring e funzioni lambda
6. **Collezioni**: liste, tuple, dizionari e insiemi con tutte le operazioni più comuni
7. **Grafica turtle**: disegno, movimento, colore, riempimento, animazione, gestione degli
   eventi, frattali e l'onda sinusoidale
8. **Input dell'utente e gestione delle stringhe**: input(), metodi delle stringhe, f-string,
   formattazione, espressioni regolari e input/output su file di testo
9. **Moduli e libreria standard**: random, math, time, sys, os, string, re e la creazione di
   moduli personalizzati
10. **Gestione degli errori e debugging**: errori di sintassi, errori di runtime ed errori
    logici, try/except, lettura dei traceback, assert e strategie di debugging
11. **Programmazione orientata agli oggetti (introduzione)**: classi, oggetti, attributi,
    metodi, `__init__`, `self` e basi dell'ereditarietà
12. **Strutture dati e algoritmi**: pile, code, grafi, liste di adiacenza, ricerca in
    ampiezza (BFS), ricerca in profondità (DFS), risoluzione di labirinti, ordinamento e
    ricerca binaria
13. **Visualizzazione dei dati**: grafici a linee con matplotlib, etichette, griglie e grafici
    di funzioni matematiche
14. **Calcolo numerico**: array NumPy, operazioni sugli array, cambio di forma (reshape)
15. **Elaborazione delle immagini**: Pillow/PIL, aprire e mostrare immagini, array di pixel
16. **Introduzione al machine learning**: modelli sequenziali di Keras, strati densi e
    convoluzionali, riconoscimento delle cifre MNIST, addestramento, valutazione e previsione
17. **Programmazione a eventi e interattiva**: clic del mouse, eventi della tastiera,
    callback e cicli di animazione
18. **Buone pratiche di programmazione**: modularità, principio DRY, nomi significativi,
    basi del controllo di versione, lettura della documentazione
19. **Materiali di supporto al corso**: termini di glossario per ogni lezione, domande
    frequenti, quiz e una guida dettagliata per gli insegnanti con tempi, domande di
    discussione e attività di approfondimento

---

## Argomenti non trattati

I seguenti argomenti sono volutamente esclusi da questo corso, per restare concentrati sulla
padronanza di base della programmazione per un pubblico di principianti:

- Sviluppo web (HTML, CSS, framework JavaScript, Flask, Django)
- Progettazione di database e SQL
- Reti e programmazione con i socket
- Concorrenza, thread e async/await
- Amministrazione di sistema e script di shell oltre l'uso di base del terminale
- Tecniche avanzate di ingegneria del software (design pattern, pipeline CI/CD)
- Distribuzione nel cloud e containerizzazione (Docker, Kubernetes)
- Sicurezza informatica e penetration testing
- Pipeline complete di addestramento per il deep learning oltre l'esempio introduttivo MNIST
- Sviluppo di app per dispositivi mobili

---

## Risultati di apprendimento

Al termine di questo corso, gli studenti saranno in grado di:

### Ricordare
*Recuperare, riconoscere e richiamare conoscenze rilevanti dalla memoria a lungo termine.*

- **Ricordare** che Python usa l'indentazione (gli spazi bianchi) per definire i blocchi di codice
- **Nominare** i sei tipi di dati fondamentali di Python: int, float, str, bool, list e dict
- **Elencare** gli operatori aritmetici disponibili in Python: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Identificare** le parole chiave usate per il controllo del flusso: `if`, `elif`, `else`, `for`, `while`, `break`, `continue`
- **Enunciare** la differenza tra un errore di sintassi, un errore di runtime e un errore logico
- **Ricordare** i comandi della grafica turtle per il movimento, il controllo della penna, il colore e il riempimento
- **Nominare** almeno cinque moduli della libreria standard di Python e una funzione per ciascuno
- **Riconoscere** lo scopo delle parole chiave `import`, `def`, `return`, `class`, `try` ed `except`
- **Elencare** le principali operazioni disponibili per le liste (append, insert, remove, pop, sort, reverse)
- **Ricordare** la differenza tra tipi mutabili (liste, dizionari) e tipi immutabili (stringhe, tuple)
- **Enunciare** che cosa significano le sigle BFS e DFS e identificare quale usa una coda e quale una pila
- **Nominare** in ordine i sei livelli della Tassonomia di Bloom
- **Identificare** il ruolo di Monty nel corso come guida all'apprendimento e fonte di suggerimenti


### Comprendere
*Costruire significato a partire da messaggi didattici, inclusa la comunicazione orale, scritta e grafica.*

- **Spiegare** perché la struttura a blocchi basata sull'indentazione di Python riduce la necessità di parentesi graffe o di parole chiave `begin/end`
- **Descrivere** come un ciclo `for` con `range()` corrisponde a un blocco "ripeti" di Scratch
- **Spiegare** la differenza tra passare un valore a una funzione (parametro) e restituire un valore da essa
- **Interpretare** un traceback di Python e spiegare quali informazioni fornisce ogni riga
- **Descrivere** come un dizionario memorizza coppie chiave-valore e perché le chiavi devono essere uniche
- **Spiegare** che cosa significa ricorsione e identificare il caso base e il caso ricorsivo in una funzione data
- **Riassumere** come le coordinate della grafica turtle corrispondono a un piano x-y con l'origine al centro
- **Descrivere** che cosa significa che una variabile ha scope locale o scope globale
- **Spiegare** lo scopo dei blocchi try/except e quando è opportuno usarli
- **Interpretare** uno schema di espressione regolare e descrivere quali stringhe riconoscerebbe
- **Descrivere** la differenza tra machine learning supervisionato e non supervisionato
- **Spiegare** come si usa il dataset MNIST per addestrare un modello che riconosce le cifre
- **Riassumere** la differenza tra una lista (ordinata, mutabile), una tupla (ordinata, immutabile) e un insieme (non ordinato, elementi unici)
- **Spiegare** come BFS garantisce il percorso più breve in un grafo non pesato

### Applicare
*Eseguire o usare una procedura in una situazione data.*

- **Scrivere** programmi Python che usano print(), variabili, aritmetica e input() per creare una semplice calcolatrice
- **Usare** le istruzioni `if/elif/else` per controllare il flusso del programma in base all'input dell'utente o a valori calcolati
- **Applicare** i cicli `for` e `while` per disegnare forme geometriche con la grafica turtle
- **Definire** e **chiamare** funzioni con parametri e valori di ritorno per organizzare e riutilizzare il codice
- **Usare** i metodi delle liste (append, pop, sort, ecc.) per costruire, modificare ed esplorare collezioni di dati
- **Applicare** le operazioni sui dizionari per memorizzare e recuperare dati con un nome (per esempio un registro dei voti)
- **Scrivere** una funzione ricorsiva per disegnare un albero frattale o una spirale con la grafica turtle
- **Usare** il modulo `random` per generare colori, posizioni e valori casuali in un programma di disegno
- **Applicare** il modulo `math` per calcolare seno e coseno e disegnare un'onda con la turtle
- **Usare** `open()` e l'istruzione `with` per leggere il testo da un file ed elaborarne ogni riga
- **Applicare** `try/except` per gestire un input non valido dell'utente senza che il programma si blocchi
- **Usare** `re.search()` e `re.findall()` per estrarre degli schemi dal testo
- **Applicare** le list comprehension e le dictionary comprehension per trasformare i dati in modo conciso
- **Usare** `matplotlib.pyplot` per creare un grafico a linee con etichette a partire da dati matematici
- **Applicare** gli array NumPy per eseguire operazioni matematiche elemento per elemento su dati numerici
- **Usare** Keras per caricare il dataset MNIST, costruire un modello sequenziale, compilarlo e addestrarlo
- **Applicare** BFS o DFS per trovare un percorso in un labirinto a griglia


### Analizzare
*Scomporre il materiale nelle sue parti e determinare come le parti si collegano tra loro e a una struttura o a uno scopo complessivo.*

- **Confrontare** la sintassi testuale di Python con i blocchi equivalenti di Scratch e spiegare che cosa sostituisce ogni costrutto Python
- **Distinguere** tra la definizione di una funzione e la sua chiamata, e spiegare perché sono necessarie entrambe
- **Analizzare** un programma Python dato e identificarne gli input, i passi di elaborazione e gli output
- **Seguire passo per passo** l'esecuzione di una chiamata ricorsiva attraverso il caso base e i casi ricorsivi
- **Distinguere** quando usare una lista, una tupla, un dizionario o un insieme per un problema dato
- **Identificare** lo scope delle variabili in un programma con più funzioni e prevedere se si verificherà un `NameError`
- **Analizzare** una visita BFS di un grafo e identificare l'ordine in cui vengono visitati i nodi
- **Esaminare** la struttura a strati di una rete neurale (input, nascosto, output) e spiegare il ruolo di ogni strato
- **Scomporre** un programma di grafica turtle nelle sue parti (preparazione, funzioni di disegno, gestori di eventi) e descrivere come interagiscono
- **Distinguere** tra un errore in fase di compilazione (di sintassi) e un errore di runtime in base al momento in cui ciascuno viene rilevato
- **Analizzare** uno schema di espressione regolare identificando ogni classe di caratteri, quantificatore e ancora
- **Confrontare** le caratteristiche di BFS e DFS (uso della memoria, ottimalità del percorso, casi d'uso)
- **Esaminare** l'uso delle variabili globali e locali in un programma e identificare possibili bug dovuti a interazioni di scope non volute

### Valutare
*Formulare giudizi basati su criteri e standard, attraverso la verifica e la critica.*

- **Giudicare** se il nome di una variabile segue le convenzioni di Python e suggerire dei miglioramenti
- **Stabilire** se una funzione è modulare al punto giusto o se andrebbe divisa in funzioni più piccole
- **Valutare** due approcci per risolvere un problema (per esempio iterazione e ricorsione) e motivare quale è più adatto in un certo contesto
- **Criticare** un pezzo di codice di uno studente cercando gli errori più comuni: l'errore di uno (off-by-one) in range(), il return mancante, l'argomento predefinito mutabile, la variabile oscurata (shadowing)
- **Scegliere** la struttura dati adatta (list, dict, set, tuple) per uno scenario reale e difendere la scelta
- **Stabilire** se un blocco try/except intercetta le eccezioni giuste e se la clausola except è troppo ampia o troppo ristretta
- **Valutare** la chiarezza e la completezza di un grafico matplotlib (titolo, etichette degli assi, scala leggibile)
- **Giudicare** la qualità di un modello MNIST addestrato in base alla sua accuratezza e alla curva della loss
- **Valutare** la leggibilità di un programma Python e suggerire miglioramenti a nomi, struttura e commenti
- **Valutare** se BFS o DFS è l'algoritmo migliore per un labirinto o un problema su grafi specifico
- **Verificare** la completezza e la correttezza di un'espressione regolare rispetto a un insieme di stringhe di prova
- **Giudicare** se una funzione ricorsiva ha un caso base corretto e raggiungibile

### Creare
*Mettere insieme elementi per formare un tutto coerente o funzionante; riorganizzare elementi in un nuovo schema o in una nuova struttura.*

- **Progettare** e **costruire** un programma originale di arte con la grafica turtle che usa funzioni, cicli, colore ed elementi casuali
- **Costruire** un programma Python che legge un file di testo, elabora i dati con i metodi delle stringhe e le espressioni regolari e scrive un rapporto riassuntivo
- **Sviluppare** un modulo Python personalizzato con almeno tre funzioni riutilizzabili e importarlo in un programma separato
- **Creare** un'applicazione interattiva completa per scegliere i colori usando la gestione degli eventi della turtle
- **Costruire** un disegno frattale ricorsivo (albero, fiocco di neve o spirale) e regolarne i parametri di profondità e ramificazione
- **Progettare** un'applicazione basata sui dizionari (per esempio un semplice inventario, un contatore della frequenza delle parole o un registro dei voti) che usa cicli, condizioni e input/output su file
- **Implementare** un risolutore di labirinti con BFS o DFS che legge il labirinto da una struttura dati, trova il percorso più breve e mostra la soluzione con la grafica turtle
- **Costruire** una dashboard di visualizzazione dei dati con matplotlib che rappresenti almeno due serie di dati, con assi etichettati e una legenda
- **Creare** una semplice classe con `__init__`, attributi e metodi, e usarla per rappresentare un'entità del mondo reale (per esempio un concorrente di una gara tra turtle, una domanda di un quiz, una carta da gioco)
- **Costruire** e **addestrare** una rete neurale Keras per classificare le cifre scritte a mano del dataset MNIST e riportarne l'accuratezza sul test
- **Progettare** un progetto Python originale completo che integri concetti di almeno tre sezioni del corso (per esempio grafica turtle + input/output su file + casualità, oppure visualizzazione dei dati + NumPy + matplotlib)
- **Produrre** un piano di lezione completo, della qualità di una guida per insegnanti, su un argomento del corso, con obiettivi di apprendimento, codice di esempio, domande di discussione e un quiz

## Materiali del corso inclusi

- **Glossario:** un glossario completo di oltre 200 termini di Python e di informatica, con
  definizioni in linguaggio semplice, scritte per un livello di lettura da quinta primaria e
  accompagnate da esempi
- **Domande frequenti:** una sezione di domande frequenti che affronta i dubbi più comuni degli
  studenti che passano dalla programmazione a blocchi a quella testuale
- **Quiz:** brevi quiz a correzione automatica (5–10 domande) alla fine di ogni lezione, che
  verificano la memorizzazione, la comprensione e l'applicazione dei concetti chiave della lezione
- **Guida per gli insegnanti:** una guida dettagliata per i docenti con indicazioni sui tempi,
  mappe dei concetti prerequisiti, spunti di discussione, idee sbagliate più comuni, attività di
  approfondimento, rubriche di valutazione e l'allineamento agli standard di informatica
  (CSTA K-12)
- **Monty la mascotte:** consigli, suggerimenti e incoraggiamenti di Monty in ogni lezione,
  mostrati come riquadri evidenziati accanto alle finestre di codice interattive di Skulpt
