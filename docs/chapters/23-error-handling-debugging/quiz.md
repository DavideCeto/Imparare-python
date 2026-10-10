# Quiz: Gestione degli Errori e Debugging

Verifica la tua comprensione dei tipi di errore Python, dei traceback, di try/except, e delle tecniche di debug con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale tipo di errore si verifica quando Python non riesce a interpretare il tuo codice prima ancora che venga eseguito?

<div class="upper-alpha" markdown>
1. Errore logico
2. Errore di runtime
3. Errore sintattico
4. Errore di import
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un errore sintattico viene rilevato prima che il programma venga eseguito perché Python non riesce nemmeno a capire il codice. Esempi includono un `:` mancante dopo `if`, parentesi non corrispondenti, o un'indentazione sbagliata. Gli errori di runtime (eccezioni) si verificano mentre il programma è in esecuzione. Gli errori logici sono quando il programma gira ma produce la risposta sbagliata.

    **Concept Tested:** Types of Errors

---

#### 2. Quale tipo di errore produce `int("hello")`?

<div class="upper-alpha" markdown>
1. `SyntaxError`
2. `NameError`
3. `ValueError`
4. `TypeError`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un `ValueError` si verifica quando una funzione riceve un valore del tipo corretto ma un valore inappropriato per il contesto. `int()` si aspetta una stringa che sembra un numero, ma `"hello"` non può essere convertita in un intero. Un `TypeError` si verificherebbe se passassi un tipo completamente sbagliato (come `int([1, 2, 3])`).

    **Concept Tested:** Common Exception Types

---

#### 3. Cosa ti dice un traceback di Python?

<div class="upper-alpha" markdown>
1. Quanto velocemente è girato il programma prima dell'errore
2. Il file, il numero di riga, il codice esatto che è andato in crash, e il tipo di eccezione con il messaggio
3. Un suggerimento su come correggere automaticamente l'errore
4. La memoria totale usata dal programma prima del crash
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un traceback mostra la sequenza di chiamate che ha portato al crash, e soprattutto: il nome del file, il numero di riga, la riga esatta di codice che ha fallito, e il tipo di eccezione con una descrizione. Leggilo dal basso verso l'alto — l'ultima riga dà il tipo di errore e il messaggio, le righe sopra mostrano dove nel codice è successo.

    **Concept Tested:** Reading Tracebacks

---

#### 4. Qual è lo scopo di un blocco `try/except`?

<div class="upper-alpha" markdown>
1. Far girare il codice più velocemente saltando i controlli di errore
2. Catturare gli errori di runtime e gestirli con eleganza così che il programma non vada in crash
3. Testare se il tuo codice ha errori sintattici prima di eseguirlo
4. Ripetere il codice finché non gira senza errori
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un blocco `try/except` ti permette di eseguire codice rischioso dentro `try:` e specificare cosa fare in `except:` se si verifica un errore. Invece di andare in crash, il programma continua con il codice di gestione dell'errore. Questo è essenziale per scrivere programmi che gestiscono input dell'utente, operazioni su file, o connessioni di rete dove gli errori sono previsti e dovrebbero essere gestiti.

    **Concept Tested:** try/except Blocks

---

#### 5. Quale eccezione viene generata quando provi a dividere per zero?

<div class="upper-alpha" markdown>
1. `ValueError`
2. `MathError`
3. `ZeroDivisionError`
4. `ArithmeticException`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python genera `ZeroDivisionError` quando provi a dividere qualsiasi numero per zero (`10 / 0`). La catturi specificamente con `except ZeroDivisionError:`. Controlla sempre un denominatore pari a zero prima di dividere se il denominatore proviene dall'input dell'utente o da un calcolo che potrebbe produrre zero.

    **Concept Tested:** Common Exception Types

---

#### 6. Cosa fa la clausola `else` in un blocco `try/except/else`?

<div class="upper-alpha" markdown>
1. Gira se un'eccezione è stata catturata
2. Gira solo se il blocco `try` si è completato senza generare nessuna eccezione
3. Gira sempre, che si sia verificata o no un'eccezione
4. Rigenera l'eccezione catturata dopo averla gestita
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La clausola `else` in un blocco `try/except` gira solo quando il blocco `try` si è completato con successo — senza nessuna eccezione generata. Questo è un modo pulito di scrivere il codice del "percorso di successo" separatamente dal blocco `try` stesso. La clausola `finally`, al contrario, gira sempre indipendentemente dal fatto che si sia verificata un'eccezione.

    **Concept Tested:** else and finally Clauses

---

#### 7. Quando viene eseguito il blocco `finally`?

<div class="upper-alpha" markdown>
1. Solo quando il blocco `try` genera un'eccezione
2. Solo quando non viene generata nessuna eccezione
3. Sempre — che si sia verificata o no un'eccezione
4. Solo quando lo chiami esplicitamente con `finally()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La clausola `finally` viene sempre eseguita, indipendentemente da cosa succede nei blocchi `try` ed `except`. Gira anche se un'eccezione viene catturata, anche se non viene catturata, e anche se c'è un'istruzione `return` nel blocco `try`. Questo rende `finally` perfetta per operazioni di pulizia come chiudere file o connessioni di rete.

    **Concept Tested:** else and finally Clauses

---

#### 8. Cosa fa `raise ValueError("Speed cannot be negative.")`?

<div class="upper-alpha" markdown>
1. Stampa un messaggio di errore e continua a eseguire il programma
2. Innesca un'eccezione `ValueError` con il messaggio dato, che farà andare in crash il programma a meno che non venga catturata
3. Crea un nuovo tipo di errore chiamato "Speed cannot be negative"
4. Memorizza il messaggio in una variabile chiamata `ValueError`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'istruzione `raise` innesca deliberatamente un'eccezione. `raise ValueError("message")` crea un `ValueError` con il tuo messaggio personalizzato. Questo è utile per imporre regole nel tuo codice — se viene rilevato un input sbagliato, generi un'eccezione così chi chiama sa che qualcosa non va. Chi chiama può catturarla con `try/except ValueError`.

    **Concept Tested:** raise Statement

---

#### 9. Qual è la differenza tra un errore di runtime e un errore logico?

<div class="upper-alpha" markdown>
1. Gli errori di runtime si verificano solo nei cicli; gli errori logici si verificano solo nelle funzioni
2. Gli errori di runtime fanno andare in crash il programma mentre è in esecuzione; gli errori logici permettono al programma di girare ma producono risultati sbagliati
3. Gli errori di runtime possono essere corretti; gli errori logici sono permanenti
4. Gli errori di runtime succedono solo con l'input dell'utente; gli errori logici succedono solo con la matematica
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un errore di runtime (eccezione) fa andare in crash il programma a metà esecuzione con un messaggio di errore — Python ha rilevato qualcosa di sbagliato. Un errore logico è quando il programma gira fino al completamento senza andare in crash ma produce risultati scorretti. Gli errori logici sono spesso i più difficili da trovare perché Python non dà nessun messaggio di errore — devi capire da solo perché l'output è sbagliato.

    **Concept Tested:** Types of Errors

---

#### 10. Per cosa si usa l'istruzione `assert`?

<div class="upper-alpha" markdown>
1. Per stampare un messaggio nell'area di output
2. Per catturare le eccezioni generate da altro codice
3. Per controllare che una condizione sia True e generare un `AssertionError` se non lo è
4. Per dichiarare che una variabile non cambierà mai
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `assert condizione, "messaggio"` controlla che `condizione` sia `True`. Se è `False`, Python genera un `AssertionError` con il tuo messaggio. Viene comunemente usato nel testing e nel debug per verificare che le assunzioni del tuo codice siano corrette in punti specifici. Per esempio, `assert len(items) > 0, "List must not be empty"` conferma che la lista ha elementi prima di elaborarla.

    **Concept Tested:** assert Statement

---
