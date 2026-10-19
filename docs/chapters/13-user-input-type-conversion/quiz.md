# Quiz: Input dell'Utente e Conversione di Tipo

Verifica la tua comprensione della funzione input(), della conversione di tipo, e della validazione dell'input con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale tipo di dato restituisce sempre `input()`?

<div class="upper-alpha" markdown>
1. Un intero, se l'utente scrive un numero
2. Un float, se l'utente scrive un decimale
3. Una stringa, indipendentemente da cosa scrive l'utente
4. Un booleano, se l'utente scrive "yes" o "no"
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `input()` restituisce sempre una stringa — indipendentemente da cosa scrive l'utente. Se l'utente scrive `42`, Python ti dà la stringa `"42"`, non l'intero `42`. Questo significa che devi convertire l'input nel tipo di dato giusto prima di fare calcoli matematici o altre operazioni che richiedono un numero.

    **Concept Tested:** input() Function

---

#### 2. Cosa succede se provi a sommare il risultato di `input()` a un numero senza convertirlo prima?

<div class="upper-alpha" markdown>
1. Python converte automaticamente la stringa in un numero e li somma
2. Python genera un `TypeError` perché non puoi sommare una stringa e un numero
3. Python concatena il numero alla stringa
4. Python stampa una riga vuota e continua
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Python non converte automaticamente i tipi. Se `age` contiene la stringa `"12"` (da `input()`), allora `age + 1` genera un `TypeError: can only concatenate str (not "int") to str`. Devi convertire esplicitamente con `int(age)` o `float(age)` prima di eseguire l'aritmetica.

    **Concept Tested:** Type Conversion

---

#### 3. Cosa restituisce `int("42")`?

<div class="upper-alpha" markdown>
1. La stringa `"42"` invariata
2. Il float `42.0`
3. L'intero `42`
4. Un errore, perché le stringhe non possono essere convertite in interi
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `int()` converte una stringa (o un float) in un numero intero. `int("42")` restituisce l'intero `42`. Nota che `int("3.14")` genererebbe un `ValueError` perché `"3.14"` contiene un punto decimale — avresti bisogno prima di `float("3.14")`, poi di `int()` se vuoi la parte intera.

    **Concept Tested:** int() Conversion

---

#### 4. Perché hai bisogno di `str()` quando costruisci un messaggio come `"Score: " + score`?

<div class="upper-alpha" markdown>
1. `str()` fa stampare il numero in grassetto
2. Python non può concatenare una stringa e un intero con `+` — devi convertire prima il numero in una stringa
3. `str()` converte il numero in un float prima di unirlo
4. Hai bisogno di `str()` solo quando il numero è negativo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'operatore `+` funziona in modo diverso in base ai tipi. Con due stringhe, concatena. Con due numeri, somma. Ma mischiare una stringa e un numero con `+` genera un `TypeError`. Per costruire un messaggio che include un numero, devi convertire prima il numero in una stringa: `"Score: " + str(score)`.

    **Concept Tested:** str() Conversion

---

#### 5. Cosa restituisce `bool(0)`?

<div class="upper-alpha" markdown>
1. `True`
2. `None`
3. `"False"`
4. `False`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `bool()` converte un valore in `True` o `False`. I valori che diventano `False` sono: `0`, `0.0`, `""` (stringa vuota), `None`, e le collezioni vuote. Tutto il resto diventa `True`. Quindi `bool(0)` restituisce `False`, ma `bool(1)` o `bool(-5)` restituisce `True`.

    **Concept Tested:** bool() Conversion

---

#### 6. Cosa restituisce `type(3.14)`?

<div class="upper-alpha" markdown>
1. `<class 'int'>`
2. `3.14`
3. `<class 'str'>`
4. `<class 'float'>`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `type()` restituisce il tipo di dato di un valore come oggetto classe. `3.14` è un numero a virgola mobile, quindi `type(3.14)` restituisce `<class 'float'>`. Questo è molto utile per il debug quando non sei sicuro di che tipo contiene una variabile — specialmente dopo aver ricevuto l'input dall'utente.

    **Concept Tested:** type() Function

---

#### 7. Cosa restituisce `"  hello  ".strip()`?

<div class="upper-alpha" markdown>
1. `"hello"` con gli spazi iniziali e finali rimossi
2. `"HELLO"` in maiuscolo
3. `"  hello  "` invariata
4. Un errore perché `strip()` richiede un argomento
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. `strip()` rimuove gli spazi bianchi iniziali e finali (spazi, tabulazioni, ritorni a capo) da una stringa. `"  hello  ".strip()` restituisce `"hello"`. Questo è importante per pulire l'input dell'utente, che spesso ha spazi extra accidentali. `strip()` non modifica gli spazi in mezzo alla stringa.

    **Concept Tested:** Input Validation

---

#### 8. Cosa restituisce `str.isdigit()` quando chiamato sulla stringa `"123"`?

<div class="upper-alpha" markdown>
1. `123` (l'intero)
2. `True`
3. `False`
4. `"digit"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `isdigit()` restituisce `True` se ogni carattere nella stringa è una cifra (0-9), e `False` altrimenti. `"123".isdigit()` restituisce `True`. `"12.3".isdigit()` restituisce `False` (a causa del punto), e `"abc".isdigit()` restituisce `False`. Questo ti permette di controllare in sicurezza prima di chiamare `int()` per evitare un `ValueError`.

    **Concept Tested:** Input Validation

---

#### 9. Cos'è la validazione dell'input?

<div class="upper-alpha" markdown>
1. Convertire automaticamente tutto l'input in interi
2. Controllare che l'input dell'utente sia sicuro e nel formato previsto prima di usarlo
3. Stampare l'input dell'utente prima che il programma continui
4. Memorizzare l'input dell'utente in una variabile globale per un uso successivo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La validazione dell'input significa controllare che i dati forniti dall'utente siano nella forma prevista dal tuo programma prima di provare a usarli. Per esempio, controllare `raw.isdigit()` prima di chiamare `int(raw)` previene un crash da `ValueError` se l'utente scrive lettere invece di un numero. I buoni programmi non si fidano mai dell'input grezzo dell'utente senza controllarlo prima.

    **Concept Tested:** Input Validation

---

#### 10. Quale riga di codice legge correttamente un numero dall'utente e lo memorizza come intero?

<div class="upper-alpha" markdown>
1. `age = input(int("Quanti anni hai? "))`
2. `age = input("Quanti anni hai? ")`
3. `age = int(input("Quanti anni hai? "))`
4. `age = str(int("Quanti anni hai? "))`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `int(input("Quanti anni hai? "))` funziona chiamando prima `input()` per ottenere la risposta dell'utente come stringa, poi passando immediatamente quella stringa a `int()` per convertirla in un intero. Questo è lo schema standard di Python per leggere un numero dall'utente. L'opzione A tenta erroneamente di convertire il messaggio del prompt stesso.

    **Concept Tested:** Type Conversion

---
