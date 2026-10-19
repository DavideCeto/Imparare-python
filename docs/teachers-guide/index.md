# Guida per gli Insegnanti alla Programmazione Python

Benvenuto alla guida per gli insegnanti di *Introduzione a Python: Risorse per insegnare Python a studenti di quinta elementare e oltre, dai programmatori principianti agli sviluppatori esperti.* Questa guida spiega ogni caratteristica del manuale, come usarlo nella tua classe, e come personalizzarlo per i tuoi studenti. Non si presuppone nessuna conoscenza tecnica preliminare — ogni termine tecnico viene definito prima di essere usato.

## Informazioni su Questo Manuale Intelligente Interattivo

### Cos'è un Manuale Intelligente?

Un **manuale intelligente** è un manuale digitale che va oltre il testo e le immagini statiche. Include simulazioni interattive, quiz auto-valutanti, un glossario ricercabile, e una mappa strutturata di come i concetti si collegano tra loro. L'obiettivo è dare agli studenti un'esperienza di apprendimento più ricca e coinvolgente rispetto a un manuale stampato tradizionale.

### I Cinque Livelli dei Manuali Intelligenti

Non tutti i manuali digitali sono uguali. Classifichiamo i manuali intelligenti in cinque livelli in base a quanto siano interattivi e adattivi:

<iframe src="https://dmccreary.github.io/intelligent-textbooks/sims/book-levels/main.html" height="500px" scrolling="no"
  style="overflow: hidden;"></iframe>

| Livello | Nome | Descrizione | Esempi di Funzionalità |
|-------|------|-------------|-----------------|
| **Livello 1** | Digitale Statico | Un PDF o una versione web di base di un manuale stampato | Solo testo e immagini, nessuna interattività |
| **Livello 2** | Interattivo | Aggiunge elementi interattivi come simulazioni, quiz e glossari ricercabili | Laboratori Skulpt, quiz di autoverifica, ricerca dei concetti |
| **Livello 3** | Adattivo | Regola i contenuti in base alle prestazioni dello studente | Percorsi di apprendimento personalizzati, regolazione della difficoltà |
| **Livello 4** | Assistito dall'IA | Include un tutor IA che può rispondere alle domande degli studenti | Integrazione chatbot, riscontro automatizzato |
| **Livello 5** | IA Pienamente Adattiva | Impara continuamente dalle interazioni degli studenti e ottimizza l'esperienza | Generazione di contenuti in tempo reale, analisi predittiva |

**Questo manuale è un Manuale Intelligente di Livello 2.** Gli studenti possono eseguire e modificare codice Python direttamente nel loro browser — senza installazione, senza account — usando laboratori interattivi basati su Skulpt incorporati in ogni capitolo.

### Cosa Rende Diverso Questo Manuale

- **Laboratori interattivi Skulpt** permettono agli studenti di scrivere ed eseguire codice Python istantaneamente nel browser — nessuna installazione di software richiesta
- **La grafica turtle** rende la programmazione visiva e immediatamente gratificante — gli studenti vedono il loro codice disegnare forme, pattern e animazioni in tempo reale
- **L'inquadratura "vedi, esegui, modifica"** — ogni lezione è costruita intorno a questo ciclo invece che su una lettura passiva
- **Prevedi prima di eseguire** — gli studenti formulano un'ipotesi prima di eseguire il codice, costruendo l'abitudine di ragionare sui programmi
- **Il grafo di apprendimento** — una mappa visiva che mostra come tutti i 450 concetti si collegano e si costruiscono l'uno sull'altro
- **Monty the Python** — un personaggio mascotte amichevole che guida gli studenti attraverso ogni capitolo con consigli, incoraggiamento e intuizioni chiave
- **Completamente gratuito e open source** — concesso in licenza Creative Commons per uso non commerciale

## Aggiungere Laboratori Python Personalizzati

Gli insegnanti possono aggiungere nuovi laboratori Python interattivi al manuale usando diversi ambienti di esecuzione — dall'esecutore browser Skulpt a installazione zero fino a container Docker completi.

**[Leggi la guida completa: Aggiungere Laboratori Python Personalizzati](adding-custom-python-labs.md)**

Quella guida copre:

- **La skill del Laboratorio Skulpt** — per laboratori Python nel browser con grafica turtle (raccomandata per i capitoli 1–18)
- **La skill del Laboratorio Python Docker** — per eseguire vero Python in un container isolato
- **Nove ambienti di esecuzione** — una tabella di confronto da Skulpt a Thonny a VS Code a Jupyter, con indicazioni su quando usare ciascuno
- **Una guida alla decisione** — un diagramma di flusso per scegliere il tipo di laboratorio giusto per il tuo contesto didattico

## Usare i Capitoli

### Struttura dei Capitoli

Il manuale contiene **38 capitoli** organizzati in una sequenza deliberata. Ogni capitolo si basa sui concetti dei capitoli precedenti, quindi gli studenti dovrebbero percorrerli in ordine:

| Capitoli | Area Tematica |
|----------|-----------|
| 1–2 | Fondamenta (Benvenuto in Python, struttura del codice, l'ambiente Skulpt) |
| 3–5 | Concetti Fondamentali (variabili, funzioni, grafica turtle) |
| 6–9 | Elementi Costitutivi (matematica, cicli for, stringhe, decisioni if/else) |
| 10–12 | Flusso di Controllo e Arte (cicli while, parametri delle funzioni, colori e arte con la turtle) |
| 13–18 | Dati e Moduli (input dell'utente, metodi delle stringhe, liste, moduli, numeri casuali, modulo math) |
| 19–25 | Python Intermedio (booleani, tuple, insiemi, dizionari, collezioni avanzate, gestione degli errori, ricorsione, OOP) |
| 26–31 | Python in Pratica (I/O su file, libreria standard, JSON, strumenti di sviluppo, elaborazione del testo, algoritmi) |
| 32–35 | Python Applicato (visualizzazione dati, NumPy, elaborazione delle immagini, turtle avanzata ed eventi) |
| 36–38 | Argomenti Avanzati (pensiero computazionale, fondamenti di machine learning, reti neurali e MNIST) |

### Cosa Contiene Ogni Capitolo

Ogni capitolo segue una struttura coerente:

1. **Front matter YAML** — Metadati all'inizio di ogni file di capitolo (titolo, descrizione, livello di lettura, versione). Gli studenti non lo vedono; viene usato dai motori di ricerca e dal generatore del sito web.
2. **Riepilogo** — Una breve panoramica di cosa copre il capitolo e cosa impareranno gli studenti.
3. **Concetti trattati** — Un elenco numerato dei concetti specifici affrontati nel capitolo, tratti dal grafo di apprendimento.
4. **Prerequisiti** — Link ai capitoli precedenti che dovrebbero essere completati prima.
5. **Benvenuto da Monty** — Un'ammonizione della mascotte che introduce l'argomento del capitolo con la voce amichevole di Monty.
6. **Contenuto principale** — Il materiale didattico centrale, scritto a un livello di lettura di quinta-ottava elementare. Include tabelle, esempi del mondo reale, e laboratori Skulpt incorporati.
7. **Prevedi prima di eseguire** — Prima di ogni laboratorio Skulpt, Monty chiede agli studenti di prevedere cosa farà il codice. Questo è posizionato immediatamente sopra il laboratorio così gli studenti formano prima un'ipotesi.
8. **Laboratori Skulpt** — Programmi Python interattivi incorporati direttamente nella pagina. Gli studenti leggono il codice, prevedono il suo output, lo eseguono, e poi lo modificano.
9. **Verifiche di apprendimento** — Laboratori dove a un programma manca una riga chiave (lo studente la aggiunge) o contiene un piccolo bug deliberato (lo studente lo trova e lo corregge).
10. **Ammonizioni di Monty** — Durante tutto il capitolo, Monty appare 5-6 volte per evidenziare intuizioni chiave, offrire consigli, e avvertire su errori comuni.
11. **Punti chiave da ricordare** — Un riepilogo numerato dei concetti più importanti, preceduto da una celebrazione di Monty.

### Uso Suggerito in Classe

- **Prima della lezione**: Assegna il capitolo come lettura per casa. I laboratori Skulpt mantengono gli studenti coinvolti durante la lettura indipendente — possono eseguire ogni esempio senza alcuna configurazione.
- **Durante la lezione**: Apri il capitolo su un proiettore. Leggi ad alta voce lo spunto "prevedi prima di eseguire", lascia che gli studenti discutano le loro previsioni, poi esegui il codice insieme.
- **Dopo la lezione**: Assegna le domande di pratica e le verifiche di apprendimento. Usa il quiz (pagina separata) per una rapida valutazione formativa.
- **Ritmo**: Ogni capitolo è progettato per circa 2-3 periodi di lezione (90-135 minuti di istruzione). I capitoli con più laboratori Skulpt o argomenti complessi (ricorsione, OOP, machine learning) potrebbero richiedere più tempo.

## Usare i Laboratori Interattivi Skulpt

### Cos'è un Laboratorio Skulpt?

**Skulpt** è un interprete Python compilato in JavaScript — il che significa che viene eseguito interamente dentro il browser web dello studente senza server, senza installazione, e senza account richiesto. Gli studenti possono leggere un programma Python funzionante, eseguirlo istantaneamente, cambiare un numero o un colore, ed eseguirlo di nuovo.

Questo ciclo "vedi, esegui, modifica" è lo strumento didattico principale nei capitoli 1–18.

### Come Funzionano i Laboratori Skulpt

Ogni laboratorio Skulpt appare nel testo del capitolo come un'area interattiva con:

- Un **editor di codice** (un'area di testo dove gli studenti possono modificare il programma)
- Un **pulsante Run** che esegue il codice immediatamente
- Un **canvas** dove la grafica turtle si rende in linea accanto al codice
- Un **pulsante Reset** che ripristina il programma originale

Gli studenti non devono installare Python, aprire un terminale, o creare alcun account. Possono essere a scrivere ed eseguire Python entro 30 secondi dall'apertura della pagina.

### L'Abitudine di Prevedere Prima di Eseguire

Prima di ogni laboratorio Skulpt, Monty fa agli studenti una domanda specifica e risolvibile — "Quanti lati disegnerà la turtle?" o "Di che colore pensi che sarà l'output?" — prima che clicchino Esegui.

Questa abitudine di fermarsi a ragionare sul codice prima di eseguirlo è una delle competenze più preziose che un programmatore principiante può costruire. Incoraggia gli studenti a scrivere la loro previsione, non solo a pensarla.

### Verifiche di Apprendimento

Alcuni laboratori sono **verifiche di apprendimento** dove:

- Il programma è quasi completo ma manca di una riga chiave che lo studente deve aggiungere, OPPURE
- Il programma contiene un piccolo bug deliberato che lo studente deve trovare e correggere

Le verifiche di apprendimento etichettate con l'icona "pensante" di Monty chiedono agli studenti di aggiungere una riga mancante. Quelle etichettate con l'icona "avviso" di Monty chiedono agli studenti di trovare e correggere un bug.

### Consigli per Usare i Laboratori Skulpt in Classe

1. **Proiettali su uno schermo** — Il canvas si rende su qualsiasi proiettore. Chiedi agli studenti di prevedere quale forma verrà disegnata prima di eseguirlo.
2. **Lascia che gli studenti sperimentino** — Dopo aver visto l'output atteso, incoraggia gli studenti a cambiare un numero o un colore e a prevedere il nuovo risultato.
3. **Usa il pulsante Reset** — Se le modifiche di uno studente rompono il programma, Reset ripristina l'originale con un click.
4. **Nessuna risoluzione di problemi necessaria** — Poiché Skulpt viene eseguito nel browser, non c'è alcuna installazione di Python da debuggare, nessun PATH da correggere, e nessuna incompatibilità di versione tra gli studenti.

### Aggiungere Nuovi Laboratori Skulpt

Qualsiasi insegnante può aggiungere nuovi laboratori Skulpt al manuale. Vedi la guida [Aggiungere Laboratori Python Personalizzati](adding-custom-python-labs.md) per le istruzioni, incluso il formato esatto del blocco HTML e gli ambienti di esecuzione disponibili.

## Usare il Glossario

### Cos'è il Glossario?

Il **glossario** è un elenco alfabetico di tutti i termini chiave usati nel manuale, ciascuno con una definizione precisa e concisa. Serve come dizionario di riferimento rapido per gli studenti che incontrano un vocabolario non familiare.

### Come Accedere al Glossario

- Clicca **"Glossario"** nella barra di navigazione laterale sinistra da qualsiasi pagina
- Usa la ricerca integrata del browser (Ctrl+F su Windows/Linux, Cmd+F su Mac) per trovare un termine specifico nella pagina del glossario
- Usa la **barra di ricerca** a livello di sito in cima a qualsiasi pagina per cercare un termine in tutto il manuale

### Consigli per Usare il Glossario in Classe

- **Anteprima del vocabolario** — Prima di iniziare un nuovo capitolo, fai cercare agli studenti i termini chiave nel glossario per costruire familiarità.
- **Abbinamento delle definizioni** — Crea un'attività di riscaldamento dove gli studenti abbinano le definizioni del glossario ai termini del capitolo corrente.
- **Definizioni generate dagli studenti** — Dopo aver letto un capitolo, fai scrivere agli studenti le proprie definizioni, poi confronta con il glossario.
- **Quiz sul glossario** — Usa i termini del glossario per rapide valutazioni formative (flash card, giochi di quiz, ecc.).

## Usare le FAQ

### Cosa Sono le FAQ?

Le **FAQ** (Domande Frequenti) sono un elenco curato di domande comuni che gli studenti fanno sulla programmazione Python, organizzate per argomento. Ogni domanda include una risposta chiara e concisa scritta allo stesso livello di lettura dei capitoli.

### Come Sono Organizzate le FAQ

Le FAQ coprono domande attraverso tutti i 38 capitoli. Le domande sono raggruppate per area tematica per rendere facile la navigazione.

### Consigli per Usare le FAQ in Classe

- **Spunti di discussione** — Scegli 2-3 domande dalle FAQ all'inizio della lezione e fai discutere gli studenti prima di rivelare la risposta.
- **Supporto per i compiti** — Indirizza gli studenti alle FAQ quando hanno domande fuori dall'orario di lezione.
- **Lettura di approfondimento** — Le FAQ spesso coprono angolazioni non affrontate nel testo principale del capitolo, rendendole un buon materiale supplementare.
- **Ripasso per i test** — Gli studenti possono usare le FAQ come guida di studio prima delle valutazioni.

## Usare i Quiz

### Cosa Sono i Quiz?

Ogni capitolo ha una **pagina quiz** associata con domande a scelta multipla progettate per l'autovalutazione. I quiz verificano la comprensione dei concetti trattati in quel capitolo e sono allineati a elementi specifici del grafo di apprendimento.

### Come Funzionano i Quiz

- Si accede ai quiz cliccando il link **"Quiz"** sotto ogni capitolo nella navigazione a sinistra
- Ogni quiz contiene domande a scelta multipla a vari livelli della Tassonomia di Bloom
- Le domande sono presentate come sezioni espandibili — gli studenti possono cliccare per rivelare la risposta e la spiegazione dopo aver tentato la domanda
- I quiz **non sono valutati automaticamente** — sono progettati come strumenti formativi di autoverifica, non come valutazioni sommative

### Consigli per Usare i Quiz in Classe

- **Biglietti d'uscita** — Fai completare il quiz agli studenti alla fine di un periodo di lezione come rapido controllo della comprensione.
- **Controllo pre-lettura** — Assegna il quiz prima del capitolo per vedere cosa già sanno gli studenti (valutazione diagnostica).
- **Ripasso post-lettura** — Usa il quiz dopo la lettura per identificare i concetti che necessitano di essere reinsegnati.
- **Quiz collaborativo** — Fai lavorare gli studenti in coppia per discutere ogni domanda prima di rivelare la risposta.
- **Valutazioni personalizzate** — Usa le domande del quiz come banca per creare i tuoi test. Le domande sono concesse in licenza aperta (vedi "Comprendere la Licenza" qui sotto).

### Livelli della Tassonomia di Bloom

Ogni domanda del quiz è etichettata con un livello della **Tassonomia di Bloom**. La Tassonomia di Bloom è un quadro che classifica le abilità di pensiero dal semplice al complesso:

| Livello | Nome | Cosa Significa | Verbo di Esempio |
|-------|------|--------------|-------------|
| L1 | Ricordare | Richiamare fatti e definizioni | Definire, elencare, nominare |
| L2 | Comprendere | Spiegare concetti con parole proprie | Spiegare, descrivere, confrontare |
| L3 | Applicare | Usare concetti per risolvere problemi | Scrivere, dimostrare, tracciare |
| L4 | Analizzare | Scomporre ed esaminare le relazioni | Differenziare, organizzare, prevedere |
| L5 | Valutare | Esprimere giudizi basati su criteri | Valutare, argomentare, giustificare |
| L6 | Creare | Produrre lavoro o soluzioni originali | Progettare, costruire, scrivere un programma |

Una valutazione ben bilanciata include domande attraverso più livelli. I quiz in questo manuale puntano principalmente ai livelli L1–L4, con le verifiche di apprendimento e i progetti di grafica turtle che puntano a L5–L6.

## Usare i Riferimenti

### Cosa Sono i Riferimenti?

Ogni capitolo ha una **pagina dei riferimenti** associata con un elenco curato di circa 10 fonti di alta qualità che gli studenti possono usare per approfondire. I riferimenti danno priorità agli articoli di Wikipedia per accessibilità e affidabilità, integrati da documentazione Python autorevole e libri.

### Come Sono Organizzati i Riferimenti

Ogni riferimento include:

- **Titolo** — Il nome della fonte
- **URL** — Un link cliccabile alla fonte
- **Rilevanza** — Una breve descrizione del perché questa fonte è utile e come si collega al contenuto del capitolo

### Una Nota sui Link Non Più Funzionanti

Il **decadimento dei link** si verifica quando un link web (URL) smette di funzionare perché la pagina è stata spostata, rinominata, o eliminata. Se tu o i tuoi studenti incontrate un link rotto:

1. Prova a cercare il titolo dell'articolo sul sito web della fonte
2. Usa la [Wayback Machine](https://web.archive.org/) per trovare versioni archiviate della pagina
3. Segnala il link rotto usando GitHub Issues (vedi "Riscontro" qui sotto)

## Riscontro

### Segnalare Problemi e Suggerimenti

Questo manuale è un progetto open source ospitato su **GitHub**, un sito web dove i progetti di software e contenuti vengono sviluppati collaborativamente. Non è necessario capire la programmazione per segnalare un problema o suggerire un miglioramento.

### Cos'è una GitHub Issue?

Una **GitHub Issue** è come un ticket di supporto — è un modo per segnalare un bug, suggerire un miglioramento, o fare una domanda. Ogni issue riceve un numero unico e può essere discussa dal team del progetto e dalla community.

### Come Inviare un Riscontro

1. Vai al repository GitHub del manuale: [dmccreary/learning-python](https://github.com/dmccreary/learning-python)
2. Clicca la scheda **"Issues"** in cima alla pagina
3. Clicca il pulsante verde **"New issue"**
4. Dai alla tua issue un titolo chiaro (es. "Link rotto nei riferimenti del Capitolo 5" o "Suggerimento: Aggiungere un laboratorio per l'argomento X")
5. Nella descrizione, fornisci quanti più dettagli possibile:
    - Quale pagina o capitolo ha il problema
    - Cosa ti aspettavi di vedere rispetto a cosa vedi effettivamente
    - Il tuo browser e dispositivo (se rilevante)
6. Clicca **"Submit new issue"**

Avrai bisogno di un account GitHub gratuito per inviare issue. Se preferisci non creare un account, puoi inviare un riscontro via email all'autore usando la pagina dei contatti.

### Tipi di Riscontro Benvenuti

- **Refusi ed errori** — errori fattuali, errori di ortografia, formattazione rotta
- **Link rotti** — URL che non funzionano più
- **Bug nei laboratori Skulpt** — programmi che non si eseguono o producono output inaspettato
- **Suggerimenti di contenuto** — argomenti che dovrebbero essere trattati, esempi che potrebbero essere migliorati
- **Problemi di accessibilità** — contenuto difficile da leggere o navigare per studenti con disabilità

## Comprendere la Licenza

### Cos'è una Licenza Creative Commons?

Una **licenza** è un documento legale che spiega cosa è permesso fare agli altri con un'opera. Una **licenza Creative Commons (CC)** è una licenza standardizzata e facile da comprendere usata per contenuti educativi e creativi. Ti dice esattamente quali permessi hai senza bisogno di un avvocato.

### La Licenza di Questo Manuale

Questo manuale usa la licenza **CC BY-NC-SA 4.0**. Ecco cosa significa ogni parte:

| Codice | Nome Completo | Cosa Significa |
|------|-----------|---------------|
| **CC** | Creative Commons | Una licenza aperta standard |
| **BY** | Attribuzione | Devi dare credito all'autore originale |
| **NC** | Non-Commerciale | Non puoi usare il materiale per fare soldi |
| **SA** | Condividi Allo Stesso Modo | Se modifichi il materiale, devi condividerlo con la stessa licenza |
| **4.0** | Versione 4.0 | La versione della licenza (lo standard attuale) |

### Cosa PUOI Fare

- **Copiare** l'intero manuale o singoli capitoli per i tuoi studenti
- **Condividere** il link del manuale con altri insegnanti, studenti, o genitori
- **Stampare** i capitoli per uso in classe
- **Modificare** il contenuto — aggiungere i tuoi esempi, rimuovere sezioni, cambiare l'ordine
- **Tradurre** il contenuto in altre lingue
- **Creare opere derivate** — costruire la tua versione del manuale basata su questo
- **Aggiungere i tuoi laboratori Skulpt** — e inviarli indietro tramite una pull request

### Cosa NON PUOI Fare

- **Vendere** il manuale o far pagare gli studenti per l'accesso
- **Rimuovere l'attribuzione** — devi accreditare l'autore originale (Dan McCreary)
- **Usare una licenza diversa** — se modifichi e condividi, deve rimanere CC BY-NC-SA 4.0
- **Rivendicarlo come opera tua** — il requisito di attribuzione significa che devi riconoscere la fonte originale

Per il testo legale completo, vedi la pagina [Licenza Creative Commons](../license.md).

## Personalizzare il Tuo Manuale

Una delle caratteristiche più potenti di questo manuale è che puoi creare la tua versione personalizzata. Questa sezione spiega come, passo dopo passo.

### Termini Tecnici Chiave

Prima di iniziare, ecco alcuni termini che dovrai capire:

- **Repository (repo)** — Una cartella su GitHub che contiene tutti i file di un progetto. Pensala come la directory principale del progetto.
- **Git** — Uno strumento di controllo versione che traccia le modifiche ai file. Ti permette di vedere cosa è cambiato, quando, e da chi.
- **Clone** — Fare una copia completa di un repository sul tuo computer.
- **Fork** — Fare una copia completa di un repository nel tuo account GitHub (resta su GitHub, non sul tuo computer).
- **MkDocs** — Il software che converte i file markdown del manuale in un sito web. Non devi imparare MkDocs in profondità — solo abbastanza per fare modifiche di base.
- **Markdown** — Un semplice linguaggio di formattazione del testo. Se sai scrivere un'email, sai scrivere Markdown. `**grassetto**` crea il **grassetto**, `# Titolo` crea un titolo, e `-` crea un punto elenco.
- **mkdocs.yml** — Il file di configurazione principale per il sito web del manuale. Controlla il titolo del sito, la struttura di navigazione, i colori, e quali funzionalità sono abilitate.

### Passo 1: Crea un Account GitHub

Se non ne hai già uno, vai su [github.com](https://github.com) e crea un account gratuito.

### Passo 2: Fai il Fork o Clona il Repository

**Opzione A: Fork (più facile, resta su GitHub)**

1. Vai su [dmccreary/learning-python](https://github.com/dmccreary/learning-python)
2. Clicca il pulsante **"Fork"** nell'angolo in alto a destra
3. Questo crea una copia nel tuo account GitHub che puoi modificare

**Opzione B: Clone (più controllo, funziona sul tuo computer)**

1. Installa Git sul tuo computer ([git-scm.com](https://git-scm.com/))
2. Apri un terminale (Prompt dei comandi su Windows, Terminale su Mac)
3. Esegui questo comando:

```bash
git clone https://github.com/dmccreary/learning-python.git
```

Questo scarica l'intero manuale sul tuo computer.

### Passo 3: Fai le Modifiche

Tutti i file di contenuto sono nella cartella `docs/`. Sono scritti in **Markdown** (file `.md`) — file di testo semplice con formattazione semplice. Puoi modificarli con qualsiasi editor di testo.

#### Cambiare il Titolo e la Descrizione

Apri `mkdocs.yml` e modifica queste righe:

```yaml
site_name: "Your Custom Textbook Title"
site_description: "Your description here"
site_author: "Your Name"
```

#### Cambiare i Colori

In `mkdocs.yml`, trova la sezione `palette`:

```yaml
theme:
  palette:
    primary: '#642580'    # Change to a hex color or named color
    accent: '#41BAC1'     # Change the accent color
```

MkDocs Material supporta colori con nome (blue, red, green, purple, teal, ecc.) o qualsiasi codice colore esadecimale CSS.

#### Aggiungere i Tuoi Laboratori

Vedi la guida [Aggiungere Laboratori Python Personalizzati](adding-custom-python-labs.md) per il flusso di lavoro completo, inclusi i laboratori Skulpt (installazione zero, nel browser) e i laboratori Docker (per argomenti più avanzati).

### Passo 4: Visualizza in Anteprima le Tue Modifiche Localmente

1. Installa Python (versione 3.8 o più recente) da [python.org](https://python.org)
2. Installa MkDocs e il tema Material:

```bash
pip install mkdocs mkdocs-material
```

3. Naviga nella cartella del progetto e avvia il server di anteprima:

```bash
cd learning-python
mkdocs serve
```

4. Apri il tuo browser su `http://127.0.0.1:8000/learning-python/` per vedere la tua versione personalizzata

Il server di anteprima tiene sotto controllo le modifiche ai file. Quando modifichi e salvi un file Markdown, la pagina si aggiorna automaticamente nel tuo browser.

### Passo 5: Pubblica la Tua Versione

Per pubblicare il tuo manuale personalizzato come sito web gratuito usando GitHub Pages:

```bash
mkdocs gh-deploy
```

Questo comando costruisce il sito web e lo pubblica su `https://YOUR-USERNAME.github.io/learning-python/`. Il processo richiede circa 1-2 minuti.

## Personalizzare le Tue Analitiche

### Cos'è l'Analisi Web?

L'**analisi web** è il processo di misurare come i visitatori usano un sito web — quali pagine visitano, quanto tempo rimangono, e da dove provengono. Per un manuale educativo, l'analisi può aiutarti a capire quali capitoli leggono di più gli studenti e con quali laboratori Skulpt interagiscono.

### Google Analytics

Questo manuale include **Google Analytics** — un servizio gratuito di Google che traccia le visite al sito web. La proprietà di analisi dell'autore è già configurata, ma se crei il tuo fork, vorrai configurarne una tua.

#### Configurare il Tuo Google Analytics

1. Vai su [analytics.google.com](https://analytics.google.com/) e accedi con un account Google
2. Crea una nuova **proprietà** (il termine di Google per un sito web tracciato)
3. Google ti darà un **ID di Misurazione** — un codice che assomiglia a `G-XXXXXXXXXX`
4. Nel tuo `mkdocs.yml`, aggiorna questa sezione:

```yaml
extra:
  analytics:
    provider: google
    property: G-YOUR-MEASUREMENT-ID
```

5. Ricostruisci e pubblica il tuo sito. I dati di analisi inizieranno ad apparire entro 24-48 ore.

#### Cosa Puoi Imparare dall'Analisi

- **Quali capitoli sono più/meno visitati** — ti aiuta a identificare dove gli studenti potrebbero saltare i contenuti
- **Tempo medio sulla pagina** — tempi più lunghi possono indicare coinvolgimento o difficoltà
- **Ripartizione per dispositivo** — quale percentuale di studenti usa telefoni rispetto a computer
- **Distribuzione geografica** — da dove accedono i tuoi studenti

### Monitoraggio xAPI (Avanzato)

**xAPI** (Experience API, chiamata anche "Tin Can API") è uno standard avanzato per tracciare attività di apprendimento dettagliate — non solo visualizzazioni di pagina, ma interazioni specifiche come "lo studente ha eseguito il laboratorio di grafica turtle nel Capitolo 5" o "lo studente ha risposto correttamente alla domanda 3 del quiz".

#### Cos'è un LRS?

Un **LRS** (Learning Record Store) è un database che memorizza i record di apprendimento xAPI. Pensalo come un sistema di analisi specializzato progettato specificamente per l'educazione. Se usi un LRS, puoi tracciare dati di apprendimento granulari degli studenti, come quali laboratori Skulpt uno studente ha eseguito, quante volte ha cliccato Esegui prima di ottenere l'output atteso, e quali verifiche di apprendimento ha completato con successo.

#### Importante: Considerazioni Normative

Prima di raccogliere dati specifici degli studenti, sii consapevole di queste normative:

- **FERPA** (Family Educational Rights and Privacy Act) — legge federale USA che protegge i registri scolastici degli studenti. Se raccogli dati che possono identificare singoli studenti, devi rispettare il FERPA.
- **COPPA** (Children's Online Privacy Protection Act) — legge federale USA che si applica ai bambini sotto i 13 anni. Poiché questo manuale si rivolge a studenti di 10-14 anni, il COPPA potrebbe applicarsi ai tuoi studenti.
- **Leggi statali** — Molti stati USA hanno leggi aggiuntive sulla privacy degli studenti.
- **GDPR** (General Data Protection Regulation) — legge dell'Unione Europea che si applica se qualcuno dei tuoi studenti si trova nell'UE.

**Raccomandazione**: La configurazione di Google Analytics descritta sopra è anonima per impostazione predefinita — traccia visualizzazioni aggregate di pagina, non singoli studenti. Questo è l'approccio più sicuro per l'uso K-12. Se vuoi il tracciamento individuale degli studenti tramite xAPI, consulta il responsabile della privacy dei dati del tuo distretto scolastico prima di procedere.

### Costruire una Dashboard dei Progressi degli Studenti con l'IA

Man mano che gli strumenti IA diventano più accessibili, sta diventando possibile costruire dashboard personalizzate che visualizzano i progressi degli studenti attraverso il manuale. Per esempio:

- Quali capitoli ogni studente ha completato
- I punteggi dei quiz nel tempo
- Il coinvolgimento nei laboratori Skulpt — quanti laboratori uno studente ha eseguito e modificato
- Concetti che necessitano di essere reinsegnati in base alle prestazioni nei quiz

Costruire una dashboard del genere richiede conoscenze di programmazione (Python, JavaScript) e attenzione scrupolosa alla privacy dei dati degli studenti. Questo è un argomento avanzato che va oltre lo scopo di questa guida, ma la natura open source di questo manuale significa che tutte le strutture dati sono disponibili perché gli sviluppatori ci costruiscano sopra.

## Il Grafo di Apprendimento

### Cos'è un Grafo di Apprendimento?

Un **grafo di apprendimento** è una mappa visiva che mostra come i concetti nel manuale dipendono l'uno dall'altro. È strutturato come un **DAG** (Directed Acyclic Graph, grafo aciclico diretto) — un diagramma dove le frecce mostrano quali concetti devono essere compresi prima di altri.

Per esempio, comprendere la ricorsione richiede prima di comprendere le funzioni e i valori di ritorno. Il grafo di apprendimento rende visibili queste catene di dipendenza. Il grafo di apprendimento di questo manuale copre tutti i **450 concetti** attraverso i 38 capitoli, con zero violazioni di dipendenza.

### Come gli Insegnanti Possono Usare il Grafo di Apprendimento

- **Verifica dei prerequisiti** — Prima di insegnare un concetto, verifica che gli studenti abbiano coperto i suoi prerequisiti
- **Recupero** — Se uno studente fatica con un concetto, risali ai suoi prerequisiti per trovare la lacuna
- **Mappatura del curriculum** — Confronta il grafo di apprendimento con il tuo programma esistente per identificare lacune di copertura
- **Arricchimento** — Gli studenti avanzati possono esplorare concetti in anticipo rispetto al capitolo corrente seguendo il grafo in avanti

Il Visualizzatore interattivo del Grafo di Apprendimento è disponibile nella sezione "Grafo di Apprendimento" della navigazione a sinistra.

## Monty the Python: Il Tuo Agente Pedagogico

### Cos'è un Agente Pedagogico?

Un **agente pedagogico** è un personaggio che appare in tutto un manuale per guidare gli studenti. La ricerca mostra che gli agenti pedagogici migliorano il coinvolgimento degli studenti e la percezione dell'apprendimento — un fenomeno chiamato **effetto persona**.

### Come Appare Monty

Monty the Python appare come riquadri colorati (chiamati **ammonizioni**) in tutto ogni capitolo. Ce ne sono sette tipi:

| Tipo | Colore | Scopo | Frequenza |
|------|-------|---------|-----------|
| Welcome | Verde | Introduce il capitolo | Ogni apertura di capitolo |
| Thinking | Arancione | Evidenzia intuizioni chiave, pone domande di previsione | 1-2 per capitolo |
| Tip | Verde | Condivide consigli pratici | Secondo necessità |
| Warning | Rosso | Avverte su errori comuni e bug | Secondo necessità |
| Encourage | Blu | Supporta gli studenti sui concetti più difficili | Dove gli studenti potrebbero avere difficoltà |
| Celebration | Viola | Celebra i progressi | Ogni chiusura di capitolo |
| Neutral | Grigio | Note generali | Secondo necessità |

Monty appare non più di 5-6 volte per capitolo per evitare l'eccesso. Le ammonizioni della mascotte non vengono mai messe una dopo l'altra.

### Consigli per gli Insegnanti

- **Leggi ad alta voce i consigli di Monty** — Sono scritti in un tono colloquiale che funziona bene se letto ad alta voce
- **Usali come spunti di discussione** — Le ammonizioni "pensanti" di Monty evidenziano l'intuizione più importante della sezione
- **Indica le ammonizioni "encourage"** per gli studenti frustrati con un concetto — il tono di Monty è specificamente calibrato per quel momento
- **Gli spunti di previsione sono interattivi** — Chiedi a tutta la classe di votare prima di eseguire il codice; la rivelazione diventa una mini-lezione
