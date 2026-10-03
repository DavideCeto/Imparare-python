# Quiz: Struttura del Codice Python

Verifica la tua comprensione della struttura del codice Python, dell'indentazione, delle parole chiave e altro ancora con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Come si crea una stringa multi-riga in Python?

<div class="upper-alpha" markdown>
1. Racchiudendo il testo tra virgolette singole come `'text'`
2. Racchiudendo il testo tra triple virgolette come `"""text"""`
3. Usando la funzione `multiline()`
4. Aggiungendo un `#` prima di ogni riga di testo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Le triple virgolette (`"""` o `'''`) creano una stringa multi-riga in Python. Tutto ciò che si trova tra le triple virgolette di apertura e quelle di chiusura — incluse le righe a capo — diventa parte della stringa. Le virgolette singole o doppie normali funzionano solo per testo che resta su una riga.

    **Concept Tested:** Multi-Line Strings

---

#### 2. In Python, cosa significa indentazione?

<div class="upper-alpha" markdown>
1. Usare le parentesi graffe `{ }` per raggruppare righe di codice
2. Aggiungere righe vuote extra tra le sezioni del tuo programma
3. Aggiungere spazi all'inizio delle righe per mostrare quali righe vanno insieme
4. Scrivere commenti alla fine di ogni riga di codice
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Indentazione significa aggiungere spazi all'inizio di una riga per spostarla verso destra. In Python, l'indentazione non è solo estetica — fa parte della grammatica del linguaggio. Python usa il numero di spazi all'inizio di ogni riga per decidere quali righe vanno insieme in un blocco.

    **Concept Tested:** Indentation as Syntax

---

#### 3. Quale errore mostra Python quando la tua indentazione è sbagliata?

<div class="upper-alpha" markdown>
1. `NameError`
2. `TypeError`
3. `SyntaxError`
4. `IndentationError`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Quando hai troppi spazi, troppo pochi, o mescoli tab e spazi, Python si ferma e mostra un `IndentationError`. La soluzione è sempre usare esattamente 4 spazi per ogni livello di indentazione e non mescolare mai tab e spazi nello stesso file.

    **Concept Tested:** Indentation as Syntax

---

#### 4. Cos'è una parola chiave di Python?

<div class="upper-alpha" markdown>
1. Una parola speciale che Python riserva per il proprio uso e non può essere usata come nome di variabile
2. Qualsiasi parola che digiti dentro un'istruzione `print()`
3. Il nome che dai a un oggetto tartaruga
4. Una parola che appare in un commento dopo il simbolo `#`
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. Le parole chiave di Python sono parole che hanno già un significato specifico nel linguaggio — parole come `for`, `if`, `while`, `def` e `import`. Non puoi usarle come nomi per le tue variabili o funzioni perché Python si confonderebbe su se intendevi il comando o la tua variabile.

    **Concept Tested:** Python Keywords

---

#### 5. Quale delle seguenti è una parola chiave di Python?

<div class="upper-alpha" markdown>
1. `turtle`
2. `print`
3. `for`
4. `forward`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `for` è una parola chiave riservata di Python usata per scrivere i cicli. Non puoi usare `for` come nome di variabile. Le altre — `turtle`, `print` e `forward` — non sono parole chiave; sono nomi integrati o nomi di libreria che potrebbero tecnicamente essere riutilizzati (anche se farlo è una pessima idea).

    **Concept Tested:** Python Keywords

---

#### 6. Cosa segnala l'inizio di un blocco di codice in Python?

<div class="upper-alpha" markdown>
1. Una riga che inizia con `#`
2. Una riga che termina con i due punti `:`
3. Una riga vuota prima del codice indentato
4. La parola `begin` all'inizio della riga
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In Python, i due punti `:` alla fine di una riga aprono un nuovo blocco di codice. Le righe successive, indentate di 4 spazi, appartengono a quel blocco. Questo schema compare con i cicli `for`, le istruzioni `if`, le definizioni di funzione e altro ancora. Python non usa parole chiave `begin`/`end` come alcuni altri linguaggi.

    **Concept Tested:** Code Block Structure

---

#### 7. Qual è la differenza tra uno statement e un'espressione in Python?

<div class="upper-alpha" markdown>
1. Uno statement produce un valore; un'espressione compie un'azione
2. Uno statement compie un'azione; un'espressione produce un valore
3. Gli statement usano le virgolette; le espressioni usano i numeri
4. Statement ed espressioni sono due nomi per la stessa identica cosa
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Uno statement è un'istruzione che *fa* qualcosa (come `print("Hello")` o `import turtle`) ma non produce un valore che puoi memorizzare. Un'espressione è un pezzo di codice che *produce un valore* (come `2 + 3`, che produce `5`). Molte righe Python combinano entrambi — per esempio `print(2 + 3)` è uno statement che contiene un'espressione.

    **Concept Tested:** Statement vs Expression

---

#### 8. Quale regola sugli spazi bianchi Python impone davvero (causando un errore se violata)?

<div class="upper-alpha" markdown>
1. Devi aggiungere una riga vuota tra ogni due statement
2. Devi mettere esattamente uno spazio dopo ogni virgola
3. Devi usare un'indentazione coerente per mostrare quali righe vanno dentro un blocco
4. Devi aggiungere spazi intorno al segno `=` in ogni assegnazione
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python impone le regole di indentazione — un'indentazione incoerente o scorretta causa un `IndentationError`. Le altre regole (spazi dopo le virgole, spazi intorno a `=`, righe vuote tra statement) sono convenzioni di stile che rendono il codice più leggibile ma non causano errori se le violi.

    **Concept Tested:** Whitespace Rules

---

#### 9. Come si imposta il colore della penna della tartaruga su arancione in Python?

<div class="upper-alpha" markdown>
1. `t.color = "orange"`
2. `t.setcolor("orange")`
3. `t.pencolor("orange")`
4. `color("orange", t)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il metodo turtle `pencolor()` imposta il colore della penna di disegno della tartaruga. Lo chiami con una stringa di colore con nome come `t.pencolor("orange")`. Le altre opzioni usano una sintassi scorretta — Python solleverebbe un `AttributeError` oppure non produrrebbe alcun cambiamento visibile.

    **Concept Tested:** Named Colors

---

#### 10. Quale delle seguenti NON è un colore con nome valido che puoi usare con turtle?

<div class="upper-alpha" markdown>
1. `"skyblue"`
2. `"forestgreen"`
3. `"ultraviolet"`
4. `"crimson"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `"ultraviolet"` non è uno dei 140 colori con nome X11 riconosciuti dalla libreria turtle — causerebbe un errore di colore. Le altre opzioni — `"skyblue"`, `"forestgreen"` e `"crimson"` — sono tutti colori con nome X11 validi che puoi usare con `t.pencolor()`.

    **Concept Tested:** Named Colors

---
