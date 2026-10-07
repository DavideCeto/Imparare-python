# Quiz: Metodi delle Stringhe e Formattazione

Verifica la tua comprensione dell'indicizzazione delle stringhe, dello slicing, dei metodi, e delle f-string con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale indice ha il primo carattere di una stringa Python?

<div class="upper-alpha" markdown>
1. `1`
2. `-1`
3. `0`
4. L'indice dipende dalla lunghezza della stringa
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Le stringhe Python (e la maggior parte delle sequenze Python) usano l'indicizzazione a base zero — il primo carattere è all'indice `0`, il secondo all'`1`, e così via. Quindi per la stringa `"Python"`, `word[0]` dà `"P"`, `word[1]` dà `"y"`, e `word[5]` dà `"n"`.

    **Concept Tested:** String Indexing

---

#### 2. Cosa restituisce `"Python"[-1]`?

<div class="upper-alpha" markdown>
1. `"P"` (il primo carattere)
2. Un errore, perché gli indici negativi non sono permessi
3. `"n"` (l'ultimo carattere)
4. `6` (la lunghezza della stringa)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Gli indici negativi contano all'indietro dalla fine della stringa. L'indice `-1` è l'ultimo carattere, `-2` è il penultimo, e così via. Per `"Python"`, l'indice `-1` è `"n"`. Questo è comodo quando vuoi l'ultimo carattere senza conoscere la lunghezza della stringa.

    **Concept Tested:** String Indexing

---

#### 3. Cosa restituisce `"programming"[0:4]`?

<div class="upper-alpha" markdown>
1. `"prog"`
2. `"rogr"`
3. `"prog "` (con uno spazio)
4. `"rogramming"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. Lo slicing delle stringhe `[start:end]` restituisce i caratteri dall'indice `start` fino a, ma NON includendo, l'indice `end`. `"programming"[0:4]` dà i caratteri agli indici 0, 1, 2, e 3 — che sono `p`, `r`, `o`, `g` — formando `"prog"`. Il carattere all'indice 4 (`a`) non è incluso.

    **Concept Tested:** String Slicing

---

#### 4. Cosa restituisce `"hello world".split()`?

<div class="upper-alpha" markdown>
1. `"hello"` e `"world"` come due istruzioni print separate
2. `["hello", "world"]` — una lista di due stringhe
3. `"hello,world"` con una virgola aggiunta
4. `11` — il numero di caratteri incluso lo spazio
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `split()` senza argomento divide una stringa su ogni spazio bianco e restituisce una lista dei pezzi. `"hello world".split()` restituisce la lista `["hello", "world"]`. Puoi anche dividere su un carattere specifico: `"a,b,c".split(",")` restituisce `["a", "b", "c"]`.

    **Concept Tested:** split() Method

---

#### 5. Cosa restituisce `"-".join(["a", "b", "c"])`?

<div class="upper-alpha" markdown>
1. `"a-b-c"`
2. `["a", "b", "c"]` invariata
3. `"-a-b-c-"`
4. `"abc"` senza separatore
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. `join()` incolla insieme una lista di stringhe usando la stringa su cui viene chiamato come separatore. `"-".join(["a", "b", "c"])` restituisce `"a-b-c"`. Il separatore appare tra gli elementi ma non all'inizio o alla fine. `join()` è l'opposto di `split()`.

    **Concept Tested:** join() Method

---

#### 6. Cosa restituisce `"the fox ran".replace("fox", "dog")`?

<div class="upper-alpha" markdown>
1. `"the fox ran"` invariata
2. `"the dog ran"`
3. `"the dog dog ran"` sostituendo una volta
4. Un errore, perché `replace()` richiede tre argomenti
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `replace(old, new)` restituisce una nuova stringa con ogni occorrenza di `old` sostituita da `new`. `"the fox ran".replace("fox", "dog")` restituisce `"the dog ran"`. Nota che le stringhe sono immutabili — `replace()` non cambia la stringa originale; ne restituisce una nuova.

    **Concept Tested:** replace() Method

---

#### 7. Cosa restituisce `"report.pdf".endswith(".pdf")`?

<div class="upper-alpha" markdown>
1. L'indice dove inizia `".pdf"` nella stringa
2. `True`
3. `False`
4. `".pdf"` (il suffisso corrispondente)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `endswith(suffix)` restituisce `True` se la stringa finisce con il suffisso dato, `False` altrimenti. `"report.pdf".endswith(".pdf")` restituisce `True` perché la stringa finisce davvero con `".pdf"`. Questo è molto utile per controllare le estensioni dei file, le terminazioni degli URL, e altri pattern di suffisso.

    **Concept Tested:** String Search Methods

---

#### 8. Cos'è una f-string in Python?

<div class="upper-alpha" markdown>
1. Una stringa che può contenere solo numeri a virgola mobile
2. Un tipo speciale di stringa "veloce" che gira più velocemente delle stringhe normali
3. Un letterale di stringa formattato che ti permette di incorporare variabili direttamente usando `{variabile}` dentro la stringa
4. Una stringa definita con triple virgolette per più righe
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una f-string (letterale di stringa formattato) si crea mettendo `f` prima della virgoletta di apertura: `f"Hello, {name}!"`. Qualsiasi espressione dentro `{}` viene valutata e inserita nella stringa. Le f-string eliminano il bisogno di convertire i numeri con `str()` prima di unirli e sono molto più leggibili della concatenazione.

    **Concept Tested:** f-Strings

---

#### 9. Cosa produce `f"Score: {95:.1f}%"`?

<div class="upper-alpha" markdown>
1. `"Score: 95%"`
2. `"Score: 95.0%"`
3. `"Score: 95.1%"`
4. Un errore perché gli interi non possono usare il formato `.1f`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La specifica di formato `:.1f` dentro una f-string formatta un numero come un float con esattamente 1 cifra decimale. `95` formattato come `:.1f` diventa `95.0`. Quindi `f"Score: {95:.1f}%"` produce `"Score: 95.0%"`. Specifiche di formato come `.2f` (2 cifre decimali) o `.0f` (nessuna cifra decimale) ti danno un controllo preciso sulla visualizzazione numerica.

    **Concept Tested:** f-Strings

---

#### 10. Cosa restituisce `s.find("xyz")` quando `"xyz"` non viene trovato nella stringa `s`?

<div class="upper-alpha" markdown>
1. `None`
2. `False`
3. Viene generato un errore
4. `-1`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `find()` restituisce l'indice della prima occorrenza della stringa cercata. Se la stringa cercata non viene trovata, `find()` restituisce `-1` invece di generare un errore. Questo ti permette di controllare il risultato: `if s.find("xyz") != -1:` significa "se xyz è stato trovato." L'operatore `in` (`"xyz" in s`) è un altro modo comune per controllare senza preoccuparsi dell'indice.

    **Concept Tested:** String Search Methods

---
