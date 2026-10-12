# Quiz: Pensiero Computazionale e Buone Pratiche

Verifica la tua comprensione del pensiero computazionale, dei principi DRY, dell'abstraction, dei nomi significativi, delle strategie di debug, e del controllo di versione con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa significa scomposizione nel pensiero computazionale?

<div class="upper-alpha" markdown>
1. Scomporre un programma nelle sue singole righe di codice per l'analisi
2. Scomporre un problema grande e complesso in sotto-problemi più piccoli e gestibili che possono essere risolti ciascuno indipendentemente
3. Convertire un linguaggio di programmazione di alto livello in codice macchina
4. Rimuovere il codice non necessario da un programma per renderlo più corto
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La scomposizione è uno dei quattro pilastri del pensiero computazionale. Invece di provare a risolvere un intero problema complesso in una volta, lo scomponi in pezzi più piccoli. Per esempio, "costruisci un'app di quiz" si scompone in "memorizza le domande," "chiedi all'utente," "controlla la risposta," e "traccia il punteggio." Ogni pezzo è abbastanza piccolo da essere programmato e testato indipendentemente.

    **Concept Tested:** Decomposition

---

#### 2. Cos'è l'abstraction nel pensiero computazionale?

<div class="upper-alpha" markdown>
1. Scrivere codice in una lingua straniera per nascondere cosa fa
2. Concentrarsi sui dettagli essenziali di un problema e nascondere o ignorare la complessità non necessaria
3. Sostituire i numeri concreti con variabili in una formula
4. Usare l'arte astratta come ispirazione per il design dell'interfaccia utente
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'abstraction significa concentrarsi su ciò che conta per risolvere il problema attuale e nascondere i dettagli che non contano. Una funzione `ask_question(q)` nasconde i dettagli di input/output — chi chiama ha bisogno solo di sapere che fa una domanda e restituisce la risposta. Una buona abstraction rende il codice riutilizzabile e più facile da ragionare.

    **Concept Tested:** Abstraction

---

#### 3. Cosa significa il principio DRY, e quale problema risolve?

<div class="upper-alpha" markdown>
1. "Develop Rapidly, Yes" — incoraggia a scrivere codice il più velocemente possibile
2. "Don't Repeat Yourself" — previene la logica duplicata, così i bug e i cambiamenti devono essere affrontati solo in un punto
3. "Delete Redundant Yield" — rimuove le espressioni generatore non necessarie
4. "Define, Run, Yield" — i tre passi del ciclo di vita di una funzione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. DRY significa "Don't Repeat Yourself" (non ripeterti). Se la stessa logica appare in più punti, una correzione di bug o un cambiamento deve essere fatto in ogni copia — ed è facile perderne una. DRY dice: estrai la logica ripetuta in una singola funzione o variabile. L'opposto di DRY è "WET" (Write Everything Twice), che crea codice fragile e difficile da mantenere.

    **Concept Tested:** DRY Principle

---

#### 4. Cos'è il riconoscimento dei pattern nel pensiero computazionale?

<div class="upper-alpha" markdown>
1. Usare le espressioni regolari per trovare pattern nel testo
2. Progettare pattern visivi ripetuti nella grafica turtle
3. Individuare somiglianze, ripetizioni, e struttura condivisa tra diverse parti di un problema
4. Confrontare il codice dello studente con soluzioni corrette conosciute
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il riconoscimento dei pattern significa notare quando diverse parti di un problema hanno la stessa struttura. Per esempio, notare che ogni domanda del quiz ha un testo, quattro scelte, e una risposta corretta — quel pattern suggerisce una lista di dizionari o una classe `Question`. Riconoscere i pattern ti permette di riutilizzare le soluzioni invece di risolvere lo stesso problema ripetutamente.

    **Concept Tested:** Pattern Recognition

---

#### 5. Cosa rende "significativo" il nome di una variabile?

<div class="upper-alpha" markdown>
1. È quanto più corto possibile per risparmiare digitazione
2. Inizia con una lettera maiuscola per risaltare
3. Descrive chiaramente quale valore contiene la variabile, rendendo il codice leggibile senza commenti extra
4. Non contiene vocali, seguendo le tradizionali convenzioni di denominazione Unix
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un nome significativo comunica lo scopo della variabile a colpo d'occhio. `student_score` è molto più chiaro di `x` o `s`. I nomi autodocumentanti riducono il bisogno di commenti e rendono i bug più facili da trovare. PEP 8 (la guida di stile di Python) raccomanda `snake_case` per le variabili — minuscolo con underscore tra le parole.

    **Concept Tested:** Meaningful Names

---

#### 6. Cos'è il refactoring?

<div class="upper-alpha" markdown>
1. Convertire il codice Python 2 nella sintassi Python 3
2. Migliorare la struttura e la leggibilità del codice esistente senza cambiare cosa fa
3. Riscrivere un programma da zero usando un linguaggio diverso
4. Aggiungere nuove funzionalità a un programma per migliorare cosa fa
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il refactoring significa ristrutturare il codice esistente per renderlo più pulito, più leggibile, o meglio organizzato — senza cambiare il suo comportamento esterno. Esempi: rinominare le variabili per chiarezza, estrarre la logica ripetuta in una funzione, semplificare un condizionale complesso. I buoni programmatori fanno il refactor regolarmente per mantenere il loro codice manutenibile.

    **Concept Tested:** Refactoring

---

#### 7. Cos'è il pensiero test-driven?

<div class="upper-alpha" markdown>
1. Scrivere i test solo dopo che il programma è completo e funziona
2. Usare un framework di test come pytest per eseguire test automatizzati
3. Pensare a quale dovrebbe essere l'output corretto prima di scrivere il codice, e verificare che ogni funzione funzioni come previsto
4. Testare un programma facendo provare agli utenti a romperlo
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il pensiero test-driven significa decidere cosa dovrebbe fare una funzione e quale dovrebbe essere il suo output prima (o mentre) la scrivi. Per i principianti, questo significa: pensare agli input e output previsti, testare con valori conosciuti, e verificare i casi limite (lista vuota, zero, negativo). Il Test-Driven Development (TDD) formale scrive prima i test automatizzati; il pensiero test-driven applica la stessa mentalità informalmente.

    **Concept Tested:** Test-Driven Thinking

---

#### 8. Cos'è il controllo di versione, e perché i programmatori lo usano?

<div class="upper-alpha" markdown>
1. Un modo per controllare quale versione di Python sta girando nel tuo programma
2. Un sistema che traccia i cambiamenti al codice nel tempo, permettendoti di vedere la storia, annullare i cambiamenti, e collaborare con altri
3. Una funzionalità che aggiorna automaticamente i tuoi pacchetti Python all'ultima versione
4. Un tipo di sistema di commenti che registra chi ha scritto ogni riga di codice
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il controllo di versione (più comunemente Git) registra ogni cambiamento che fai al tuo codice come una serie di commit. Questo ti permette di vedere la storia completa del tuo progetto, tornare a qualsiasi stato precedente se rompi qualcosa, lavorare su funzionalità sperimentali senza rischiare il codice funzionante, e collaborare con altri senza sovrascrivere i cambiamenti a vicenda. GitHub ospita i repository Git online.

    **Concept Tested:** Version Control

---

#### 9. Cos'è il pair programming?

<div class="upper-alpha" markdown>
1. Scrivere codice che gira in parallelo su due core della CPU simultaneamente
2. Due programmatori che lavorano insieme su un computer — uno scrive mentre l'altro rivede, e scambiano i ruoli regolarmente
3. Scrivere lo stesso programma due volte per verificare che entrambe le versioni producano lo stesso output
4. Programmare in coppie di file — uno per il codice e uno per i suoi test
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il pair programming è una pratica dove due sviluppatori lavorano insieme su una postazione di lavoro. Uno è il "driver" che scrive il codice; l'altro è il "navigator" che rivede, suggerisce, e individua i problemi. Scambiano i ruoli regolarmente. La ricerca mostra che il pair programming produce meno bug e aiuta entrambi i programmatori a imparare l'uno dall'altro, anche se richiede più tempo totale.

    **Concept Tested:** Pair Programming

---

#### 10. Cosa significa che il codice è "modulare"?

<div class="upper-alpha" markdown>
1. Il codice usa frequentemente l'operatore `mod` (`%`) per i calcoli
2. Il codice è organizzato in funzioni o moduli separati e autonomi, ognuno con una singola responsabilità chiara
3. Il codice è distribuito su più computer che girano simultaneamente
4. Il codice usa solo funzionalità della libreria standard di Python senza nessun pacchetto esterno
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il codice modulare è organizzato in unità piccole e indipendenti (funzioni, classi, o moduli) dove ogni unità ha un compito chiaro. Il codice modulare è più facile da testare (testare ogni pezzo in isolamento), fare debug (isolare il pezzo rotto), e riutilizzare (copiare una funzione in un nuovo progetto). L'opposto è il codice monolitico — uno script lungo senza funzioni, dove tutto è intrecciato insieme.

    **Concept Tested:** Modularity

---
