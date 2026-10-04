# Quiz: Lavorare con le Stringhe

Verifica la tua comprensione delle stringhe Python, della concatenazione, dei caratteri di escape e altro con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è una stringa in Python?

<div class="upper-alpha" markdown>
1. Una lista di numeri memorizzata in una variabile
2. Qualsiasi sequenza di caratteri racchiusa tra virgolette
3. Un tipo speciale di ciclo che ripete del testo
4. Una parola chiave Python usata per stampare testo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una stringa (`str`) è qualsiasi sequenza di caratteri — lettere, cifre, spazi, punteggiatura, persino emoji — racchiusa tra virgolette. Puoi usare sia virgolette singole (`'...'`) sia virgolette doppie (`"..."`). Le stringhe sono diverse dai numeri: `"42"` (con le virgolette) è una stringa, non l'intero 42.

    **Concept Tested:** String Type

---

#### 2. Perché potresti scegliere le virgolette singole per una stringa invece di quelle doppie?

<div class="upper-alpha" markdown>
1. Le virgolette singole rendono la stringa più veloce
2. Le virgolette singole sono obbligatorie per le stringhe memorizzate in variabili
3. Quando la stringa contiene virgolette doppie al suo interno
4. Python riconosce le virgolette singole solo per stringhe di più parole
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Entrambi i tipi di virgolette funzionano in modo identico in Python. Il motivo principale per cambiare è quando la tua stringa contiene al suo interno un tipo di virgolette. Per esempio, `'She said "wow!"'` usa le virgolette singole all'esterno perché la stringa contiene virgolette doppie. Se usassi lo stesso tipo di virgolette sia dentro che fuori, Python si confonderebbe e genererebbe un `SyntaxError`.

    **Concept Tested:** Single vs Double Quotes

---

#### 3. Cosa fa l'operatore `+` quando usato con due stringhe?

<div class="upper-alpha" markdown>
1. Somma le lunghezze delle due stringhe
2. Unisce le due stringhe una dopo l'altra (concatenazione)
3. Converte entrambe le stringhe in numeri e le somma
4. Confronta se le due stringhe sono uguali
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Quando `+` viene usato tra due stringhe, le concatena — le unisce una dopo l'altra in un'unica stringa più lunga. Per esempio, `"Hello, " + "Monty"` produce `"Hello, Monty"`. Python non aggiunge spazi automaticamente, quindi devi includere tu stesso ogni spazio che vuoi nella tua concatenazione.

    **Concept Tested:** String Concatenation

---

#### 4. Cosa produce `"Ha" * 3`?

<div class="upper-alpha" markdown>
1. `"Ha Ha Ha"` con spazi
2. `"HaHaHa"` senza spazi
3. `6` (la lunghezza della stringa ripetuta)
4. Un errore, perché non puoi moltiplicare una stringa
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'operatore `*` ripete una stringa un numero indicato di volte senza alcun separatore. `"Ha" * 3` produce `"HaHaHa"`. Se vuoi spazi tra le ripetizioni, devi includerli tu stesso nella stringa: `"Ha " * 3` darebbe `"Ha Ha Ha "`. Il numero a destra deve essere un intero.

    **Concept Tested:** String Repetition

---

#### 5. Cosa fa il carattere di escape `\n` dentro una stringa?

<div class="upper-alpha" markdown>
1. Stampa una barra rovesciata seguita dalla lettera n
2. Inizia una nuova riga nell'output
3. Aggiunge uno spazio della dimensione di un tab all'output
4. Segnala la fine della stringa
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `\n` è il carattere di escape per la nuova riga. Quando Python incontra `\n` dentro una stringa, sposta il cursore all'inizio della riga successiva nell'output. Questo permette a una singola chiamata `print()` di produrre più righe: `print("Line one\nLine two")` mostra due righe di testo.

    **Concept Tested:** Escape Characters

---

#### 6. Cosa restituisce `len("Hello!")`?

<div class="upper-alpha" markdown>
1. `5`
2. `7`
3. `6`
4. `1`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `len()` conta ogni carattere nella stringa, inclusa la punteggiatura. `"Hello!"` ha sei caratteri: H, e, l, l, o, e !. La funzione `len()` è integrata in Python — non devi importare nulla per usarla. Funziona su stringhe, liste e molti altri tipi di dati.

    **Concept Tested:** String Length with len()

---

#### 7. Cosa significa che le stringhe Python sono immutabili?

<div class="upper-alpha" markdown>
1. Le stringhe non possono mai essere memorizzate in variabili
2. Non puoi cambiare i singoli caratteri dentro una stringa una volta creata
3. Le stringhe non possono essere stampate con la funzione `print()`
4. Le variabili stringa non possono essere riassegnate a nuovi valori
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'immutabilità significa che una volta creata una stringa, non puoi modificare i suoi singoli caratteri. Provare `name[0] = "B"` genera un `TypeError`. Per "cambiare" una stringa, crei una nuova stringa a partire da quella vecchia e riassegni la variabile. L'immutabilità rende le stringhe più veloci e sicure da usare in Python.

    **Concept Tested:** String Immutability

---

#### 8. Quale delle seguenti gestisce correttamente una stringa che contiene un apostrofo?

<div class="upper-alpha" markdown>
1. `"It's raining"`
2. `'It's raining'`
3. `"It\'s raining"`
4. Sia A che C sono corrette
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Puoi gestire un apostrofo dentro una stringa in due modi: usare le virgolette doppie all'esterno (`"It's raining"`) così l'apostrofo è solo un carattere normale, oppure usare una sequenza di escape dentro le virgolette singole (`'It\'s raining'`). L'opzione B causerebbe un `SyntaxError` perché l'apostrofo termina la stringa troppo presto.

    **Concept Tested:** Single vs Double Quotes

---

#### 9. Cos'è una stringa raw in Python, e come se ne crea una?

<div class="upper-alpha" markdown>
1. Una stringa che rimuove tutti gli spazi — creata con `space("")`
2. Una stringa in cui le sequenze di escape con barra rovesciata sono trattate come caratteri letterali — creata con `r"..."`
3. Una stringa che può contenere solo numeri — creata con `num("...")`
4. Una stringa stampata senza virgolette — creata con `bare("...")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una stringa raw dice a Python di ignorare le sequenze di escape con barra rovesciata e trattare ogni carattere letteralmente. Se ne crea una mettendo `r` prima della virgoletta di apertura: `r"C:\new_folder"` viene stampata come `C:\new_folder` invece di iniziare una nuova riga a `\n`. Le stringhe raw sono particolarmente utili per i percorsi di file Windows e le espressioni regolari.

    **Concept Tested:** Raw Strings

---

#### 10. Cosa fa `t.write("Score: 10")` in un programma turtle?

<div class="upper-alpha" markdown>
1. Salva il programma turtle in un file chiamato "Score: 10"
2. Disegna il testo "Score: 10" sulla tela turtle nella posizione attuale della turtle
3. Stampa "Score: 10" nell'area di output del testo sotto la tela
4. Imposta la velocità della turtle a 10 e la etichetta
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.write(testo)` disegna un'etichetta di testo direttamente sulla tela turtle nella posizione attuale della turtle. Questo ti permette di aggiungere punteggi, titoli ed etichette ai tuoi disegni turtle. Il testo appare sulla tela stessa — non nell'area di output sottostante — rendendolo perfetto per etichettare forme o mostrare informazioni dentro un disegno.

    **Concept Tested:** Writing Text with turtle.write()

---
