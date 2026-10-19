# Grafo di Apprendimento

[Apri il Visualizzatore del Grafo di Apprendimento a Schermo Intero](../sims/graph-viewer/main.html){ .md-button .md-button--primary }

<iframe src="../sims/graph-viewer/main.html" width="100%" height="600px" frameborder="0"></iframe>

Questa sezione contiene il grafo di apprendimento per *Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty*.
Un grafo di apprendimento è un grafo di concetti usati in questo corso. Ogni concetto è rappresentato da un
nodo in un grafo di rete. I concetti sono collegati da archi diretti che indicano
da quali concetti dipende ogni nodo prima che quel concetto venga compreso dallo studente.

Un grafo di apprendimento è la struttura dati fondamentale per i manuali intelligenti che possono raccomandare percorsi di apprendimento.
Un grafo di apprendimento è come una mappa di concetti per aiutare gli studenti a raggiungere i loro obiettivi di apprendimento.

A sinistra del grafo di apprendimento ci sono i concetti prerequisiti o fondamentali. Non
hanno archi in uscita. Hanno solo archi in entrata da altri concetti che dipendono dalla
comprensione di questi concetti prerequisiti fondamentali. All'estrema destra
ci sono i concetti più avanzati del corso. Per padroneggiare questi concetti
devi comprendere tutti i concetti a cui puntano.

Questo grafo contiene **450 concetti** organizzati in **14 categorie tassonomiche** con **838 archi di dipendenza**,
che spaziano dall'interprete Python e le basi della riga di comando fino alle
reti neurali Keras e ai fondamenti del pensiero computazionale.

Ecco altri file usati dal grafo di apprendimento.

## Descrizione del Corso

Usiamo la [Descrizione del Corso](../course-description.md) come
documento sorgente per i concetti inclusi in questo corso.
La descrizione del corso usa la tassonomia di Bloom del 2001 per ordinare gli obiettivi di apprendimento.

## Elenco dei Concetti

Usiamo l'IA generativa per convertire la descrizione del corso in un [Elenco dei Concetti](./concept-list.md).
Ogni concetto è nella forma di una breve etichetta con la Maiuscola a Ogni Parola, con la maggior parte delle etichette sotto i 32 caratteri di lunghezza.

## Elenco delle Dipendenze tra Concetti

Usiamo poi l'IA generativa per creare un Grafo Aciclico Diretto (DAG). I DAG non hanno cicli dove
i concetti dipendono da se stessi. Forniamo il DAG in due formati. Uno è un [file CSV](learning-graph.csv) e l'altro
formato è un [file JSON](learning-graph.json) che usa il formato della libreria JavaScript vis-network. Il formato vis-network usa elementi `nodes`, `edges` e `metadata`
con gli archi che contengono le proprietà `from` e `to`. Questo rende facile visualizzare e modificare il grafo
di apprendimento usando un editor costruito con gli strumenti vis-network.

## Analisi e Documentazione

### Valutazione della Qualità della Descrizione del Corso

Questo report valuta la qualità complessiva della descrizione del corso allo scopo di generare un grafo di apprendimento.

- Analisi dei campi della descrizione del corso e della profondità dei contenuti
- Verifica che la descrizione del corso abbia profondità sufficiente per generare 200 concetti
- Confronta la descrizione del corso con corsi simili
- Identifica lacune e punti di forza dei contenuti
- Suggerisce aree di miglioramento

[Visualizza la Valutazione della Qualità della Descrizione del Corso](course-description-assessment.md)

### Validazione della Qualità del Grafo di Apprendimento

Questo report fornisce una valutazione complessiva della qualità del grafo di apprendimento.
Usa algoritmi sui grafi per cercare pattern di qualità specifici nel grafo.

- Validazione della struttura del grafo — tutti i concetti sono collegati
- Validazione DAG — nessun ciclo rilevato ✅
- Concetti fondamentali: 2 punti di ingresso (Python Interpreter Overview, Command Line Basics)
- Analisi della distribuzione del grado entrante
- Catena di dipendenza più lunga: 13 passaggi
- Connettività: tutti i 450 nodi in un'unica componente connessa

[Visualizza la Validazione della Qualità del Grafo di Apprendimento](quality-metrics.md)

### Tassonomia dei Concetti

Per vedere i pattern nel grafo di apprendimento, è utile assegnare colori
a ogni concetto in base al tipo di concetto. Usiamo l'IA generativa per
creare circa una dozzina di categorie per i nostri concetti e poi collocare ogni concetto
in un singolo classificatore primario.

- Una tassonomia classificatrice di concetti con 14 categorie
- Organizzazione delle categorie — prima l'ambiente, poi ML/IA avanzato per ultimo
- Categorie bilanciate (2.2% – 15.1% ciascuna)
- Tutte le categorie sotto la soglia del 30%
- Abbreviazioni chiare di 3 lettere per l'uso nel file CSV

[Visualizza la Tassonomia dei Concetti](concept-taxonomy.md)

### Distribuzione della Tassonomia

Questo report mostra quanti concetti rientrano in ogni categoria della tassonomia.
Il nostro obiettivo è una tassonomia abbastanza bilanciata dove ogni categoria contenga
un numero uguale di concetti. Non vogliamo nemmeno che nessuna categoria contenga
oltre il 30% dei nostri concetti.

- Riepilogo statistico
- Elenco dettagliato dei concetti per categoria
- Tabella visiva della distribuzione
- Verifica del bilanciamento

[Visualizza il Report sulla Distribuzione della Tassonomia](./taxonomy-distribution.md)
