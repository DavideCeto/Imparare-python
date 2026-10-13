# Notebook Jupyter di Esempio

!!! Warning
    Questa sezione introduce gli studenti a semplici Notebook Jupyter.
    Questa sezione non è stata testata a fondo e dipende da una libreria
    per Jupyter Notebook che non è ben mantenuta dal 2023.
    Per eseguire le lezioni, gli studenti dovranno scaricare Jupyter Notebook
    sul proprio computer locale o eseguire questi notebook dentro un IDE
    come VS Code.

## Cos'è un Jupyter Notebook

Un **Jupyter Notebook** è un documento che mescola insieme tre cose che normalmente
terresti separate: scrittura, codice, e i risultati dell'esecuzione di quel
codice. Invece di scrivere un intero programma Python in un unico file ed
eseguirlo tutto in una volta, un notebook è diviso in piccole caselle chiamate
**celle**. Puoi scrivere una frase in una cella, qualche riga di Python nella
cella successiva, eseguire solo quella cella, e vedere immediatamente l'output
apparire proprio sotto di essa — un numero, del testo, un grafico, o persino
un'immagine.

Questo stile "esegui un piccolo pezzo alla volta" si chiama **Programmazione
Letterata** — il codice e la spiegazione di quel codice convivono fianco a
fianco, così il notebook si legge quasi come un rapporto di laboratorio che
però è anche vivo ed eseguibile. Poiché puoi rieseguire una singola cella senza
rieseguire l'intero programma, i notebook sono ottimi per sperimentare: cambia
un numero, premi esegui, guarda cosa è cambiato, senza aspettare che accada
nient'altro.

Alcune cose che gli studenti costruiscono comunemente in un primo notebook:

- Un **calcolatore di voti** — digita i punteggi dei test in una cella, calcola
  la media nella successiva
- Un **disegno con la turtle passo-passo** — disegna un lato di una forma per
  cella così puoi vederla crescere
- Un **mini diario scientifico** — registra le misurazioni in una cella, poi
  tracciale come un semplice grafico

## Cos'è Jupyter Lab

**Jupyter Lab** è l'applicazione (viene eseguita nel tuo browser web) che ti
permette di aprire, modificare ed eseguire i notebook. Pensala come una
combinazione tra un editor di testo e un browser di file costruita apposta per
i notebook: un pannello a sinistra mostra i tuoi file e cartelle, e l'area
principale al centro è dove vivono le celle del tuo notebook. Puoi avere
diversi notebook aperti in schede contemporaneamente, proprio come le schede
in un browser web.

Jupyter Lab è il cugino più nuovo e più potente della più vecchia app
**Jupyter Notebook** — entrambi aprono gli stessi file notebook `.ipynb`, ma
Jupyter Lab aggiunge strumenti extra come un gestore di file, un visualizzatore
di immagini, e la capacità di disporre più notebook fianco a fianco sul tuo
schermo.

## Chi Usa Jupyter

I notebook Jupyter sono uno degli strumenti più usati nella programmazione
moderna, specialmente fuori dall'ingegneria del software tradizionale:

- I **data scientist** usano i notebook per esplorare enormi insiemi di dati —
  per esempio, pulire e tracciare in grafico dati meteorologici per cercare
  tendenze climatiche
- Gli **sviluppatori di IA e machine learning** usano i notebook per addestrare
  e testare modelli, poiché possono rieseguire solo la cella di "addestramento"
  più e più volte senza ricostruire tutto il resto
- Gli **scienziati e ricercatori** usano i notebook per registrare insieme
  esperimenti e calcoli, così chiunque legga il notebook può vedere esattamente
  come è stato prodotto un risultato
- Gli **insegnanti e gli studenti** usano i notebook per lezioni interattive,
  poiché un notebook può mescolare spiegazioni, esempi eseguibili, ed esercizi
  pratici sulla stessa pagina

Se hai mai visto un foglio di calcolo usato per analizzare dati, un notebook
fa qualcosa di simile ma con tutta la potenza del linguaggio Python dietro
ogni cella — il che è parte del motivo per cui alcune persone chiamano i
notebook il "nuovo Excel".

## In Cosa Jupyter è Diverso da Python Normale?

Quando scrivi un normale programma Python — il tipo che salvi come file
`.py` — l'intero file viene eseguito dall'inizio alla fine ogni volta, in
un colpo solo. Se c'è un errore alla riga 40, spesso devi aspettare che il
programma raggiunga quella riga prima di scoprirlo, e ogni esecuzione di test
ricomincia da zero.

Un Jupyter Notebook funziona diversamente:

- **Le celle vengono eseguite indipendentemente.** Puoi eseguire la cella 3
  senza rieseguire le celle 1 e 2, purché siano già state eseguite una volta.
  Questo rende veloce testare piccole modifiche.
- **Le variabili restano.** Se crei una variabile come `score = 95` in una
  cella, ogni cella successiva può ancora usare `score` — il notebook se la
  ricorda finché non riavvii.
- **L'output resta attaccato al codice che l'ha prodotto.** Grafici, disegni
  e testo stampato appaiono direttamente sotto la cella che li ha prodotti,
  così il tuo notebook diventa un registro salvato di cosa hai fatto e cosa è
  successo.
- **L'ordine conta — ma non è fisso.** Puoi eseguire le celle fuori ordine
  mentre sperimenti, il che è potente, ma significa anche che un notebook può
  diventare confuso se non lo esegui occasionalmente tutto dall'inizio alla
  fine per assicurarti che funzioni ancora correttamente.

In breve: un file `.py` è un programma finito pensato per essere eseguito
dall'inizio alla fine, mentre un notebook è più simile a un blocco appunti
per esplorare idee un piccolo passo alla volta — il che è esattamente il
motivo per cui è un modo così popolare per imparare Python.
