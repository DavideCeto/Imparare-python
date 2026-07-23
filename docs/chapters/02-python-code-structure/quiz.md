# Quiz: Struttura del Codice Python

Prova la tua comprensione della struttura del codice Python, dell'indentazione, delle parole chiave e altro con queste domande. Fai clic su "Mostra Risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Come crei una stringa multi-riga in Python?

<div class="upper-alpha" markdown>
1. Racchiudi il testo in virgolette singole come `'testo'`
2. Racchiudi il testo in virgolette triple come `"""testo"""`
3. Usa la funzione `multiline()`
4. Aggiungi un `#` prima di ogni riga di testo
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. Le virgolette triple (`"""` o `'''`) creano una stringa multi-riga in Python. Tutto tra le virgolette triple di apertura e chiusura — incluse le interruzioni di riga — diventa

    **Concetto Testato:** Stringhe Multi-Riga

---

#### 2. In Python, cosa significa indentazione?

<div class="upper-alpha" markdown>
1. Usare parentesi graffe `{ }` per raggruppare le righe di codice insieme
2. Aggiungere righe vuote extra tra sezioni del tuo programma
3. Aggiungere spazi all'inizio delle righe per mostrare quali righe appartengono insieme
4. Scrivere commenti alla fine di ogni riga di codice
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. L'indentazione significa aggiungere spazi all'inizio di una riga per spingerla a destra. In Python, l'indentazione non è solo per aspetto — è parte della grammatica del linguaggio

    **Concetto Testato:** Indentazione come Sintassi

---

#### 3. Quale errore mostra Python quando la tua indentazione è sbagliata?

<div class="upper-alpha" markdown>
1. `NameError`
2. `TypeError`
3. `SyntaxError`
4. `IndentationError`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **D**. Quando hai troppi spazi, troppo pochi spazi, o mescoli tabulazioni e spazi, Python si ferma e mostra un `IndentationError`. La soluzione è sempre usare esattamente 4 spazi per

    **Concetto Testato:** Indentazione come Sintassi

---

#### 4. Cos'è una parola chiave Python?

<div class="upper-alpha" markdown>
1. Una parola speciale che Python riserva per il suo uso proprio e non può essere usata come nome di variabile
2. Qualsiasi parola che digiti dentro un'istruzione `print()`
3. Il nome che dai a un oggetto tartaruga
4. Una parola che appare in un commento dopo il simbolo `#`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **A**. Le parole chiave Python sono parole che hanno già un significato specifico nel linguaggio — parole come `for`, `if`, `while`, `def` e `import`. Non puoi usarle come nom

    **Concetto Testato:** Parole Chiave Python

---

#### 5. Quale dei seguenti è una parola chiave Python?

<div class="upper-alpha" markdown>
1. `tartaruga`
2. `print`
3. `for`
4. `avanti`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. `for` è una parola chiave Python riservata usata per scrivere cicli. Non puoi usare `for` come nome di variabile. Gli altri — `tartaruga`, `print` e `avanti` — non sono parole chiave

    **Concetto Testato:** Parole Chiave Python

---

#### 6. Cosa segnala l'inizio di un blocco di codice in Python?

<div class="upper-alpha" markdown>
1. Una riga che inizia con `#`
2. Una riga che termina con i due punti `:`
3. Una riga vuota prima del codice indentato
4. La parola `begin` all'inizio della riga
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. In Python, i due punti `:` alla fine di una riga aprono un nuovo blocco di codice. Le righe che seguono, indentate da 4 spazi, appartengono a quel blocco. Questo modello appare con `f

    **Concetto Testato:** Struttura del Blocco di Codice

---

#### 7. Qual è la differenza tra un'istruzione e un'espressione in Python?

<div class="upper-alpha" markdown>
1. Un'istruzione produce un valore; un'espressione esegue un'azione
2. Un'istruzione esegue un'azione; un'espressione produce un valore
3. Le istruzioni usano virgolette; le espressioni usano numeri
4. Le istruzioni e le espressioni sono due nomi per la stessa cosa
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. Un'istruzione è un'istruzione che *fa* qualcosa (come `print("Ciao")` o `import turtle`) ma non produce un valore che puoi immagazzinare. Un'espressione è un pez

    **Concetto Testato:** Istruzione vs Espressione

---

#### 8. Quale regola di spazio bianco Python in realtà applica (causa un errore se rotta)?

<div class="upper-alpha" markdown>
1. Devi aggiungere una riga vuota tra ogni due istruzioni
2. Devi mettere esattamente uno spazio dopo ogni virgola
3. Devi usare un'indentazione coerente per mostrare quali righe appartengono dentro un blocco
4. Devi aggiungere spazi attorno al segno `=` in ogni assegnazione
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Python applica le regole di indentazione — l'indentazione incoerente o errata causa un `IndentationError`. Le altre regole (spazi dopo le virgole, spazi attorno a `=`,

    **Concetto Testato:** Regole di Spazio Bianco

---

#### 9. Come imposti il colore della penna della tartaruga in arancione in Python?

<div class="upper-alpha" markdown>
1. `t.colore = "arancione"`
2. `t.setcolore("arancione")`
3. `t.pencolor("arancione")`
4. `colore("arancione", t)`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Il metodo tartaruga `pencolor()` imposta il colore della penna di disegno della tartaruga. Lo chiami con una stringa di colore denominato come `t.pencolor("arancione")`. Le altre opzioni us

    **Concetto Testato:** Colori Denominati

---

#### 10. Quale dei seguenti NON è un colore denominato valido che puoi usare con tartaruga?

<div class="upper-alpha" markdown>
1. `"blu cielo"`
2. `"verde forestale"`
3. `"ultravioletto"`
4. `"cremisi"`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. `"ultravioletto"` non è uno dei 140 colori X11 denominati che la libreria tartaruga riconosce — causerebbe un errore di colore. Le altre opzioni — `"blu cielo"`, `"verde forestale"`

    **Concetto Testato:** Colori Denominati

---
