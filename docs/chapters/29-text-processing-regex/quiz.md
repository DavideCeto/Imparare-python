# Quiz: Elaborazione del Testo ed Espressioni Regolari

Verifica la tua comprensione delle espressioni regolari, del modulo re, degli elementi del pattern, dei quantificatori, e della sostituzione del testo con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale modulo Python fornisce le funzioni per le espressioni regolari?

<div class="upper-alpha" markdown>
1. `import regex`
2. `import pattern`
3. `import re`
4. `import text`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La libreria standard di Python include il modulo `re` per le espressioni regolari. Importalo con `import re`. Le funzioni principali sono `re.search()`, `re.findall()`, `re.split()`, e `re.sub()`. Le espressioni regolari sono pattern che scrivi per cercare, far corrispondere, dividere, o sostituire il testo in modi potenti che richiederebbero molte righe di metodi delle stringhe per essere replicati.

    **Concept Tested:** re Module

---

#### 2. Perché dovresti usare le stringhe raw (`r"..."`) per i pattern regex?

<div class="upper-alpha" markdown>
1. Le stringhe raw girano più velocemente perché Python salta l'analizzatore di stringhe
2. Le stringhe raw impediscono a Python di interpretare le barre inverse come sequenze di escape, così caratteri regex come `\d` vengono passati letteralmente al motore regex
3. Le stringhe raw sono richieste perché i pattern multilinea funzionino correttamente
4. Le stringhe raw rendono automaticamente il pattern senza distinzione tra maiuscole e minuscole
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. I pattern regex usano molte sequenze con barra inversa: `\d` per cifra, `\w` per carattere di parola, `\s` per spazio bianco. In una normale stringa Python, la barra inversa inizia sequenze di escape (`\n` = ritorno a capo). Una stringa raw (`r"..."`) dice a Python di non elaborare le barre inverse, così `r"\d"` passa `\d` letteralmente al motore regex. Usa sempre `r"..."` per i pattern regex.

    **Concept Tested:** Raw Strings for Regex

---

#### 3. A cosa corrisponde il pattern regex `\d`?

<div class="upper-alpha" markdown>
1. Qualsiasi lettera (a-z o A-Z)
2. Qualsiasi carattere di spazio bianco (spazio, tab, ritorno a capo)
3. Qualsiasi singola cifra (0-9)
4. Qualsiasi carattere di parola (lettera, cifra, o underscore)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `\d` corrisponde a qualsiasi singolo carattere cifra da 0 a 9. Per far corrispondere un carattere di parola (lettere, cifre, underscore), usa `\w`. Per far corrispondere uno spazio bianco, usa `\s`. Le versioni maiuscole (`\D`, `\W`, `\S`) corrispondono all'opposto — qualsiasi cosa che NON sia rispettivamente una cifra, un carattere di parola, o uno spazio bianco.

    **Concept Tested:** Pattern Elements

---

#### 4. Cosa restituisce `re.search(r"\d{3}-\d{4}", "Call 555-1234!")`?

<div class="upper-alpha" markdown>
1. `True`
2. La stringa `"555-1234"`
3. Un oggetto match (perché il pattern è stato trovato nel testo)
4. `None` (perché il testo non è interamente un numero di telefono)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `re.search()` restituisce un **oggetto match** se il pattern viene trovato ovunque nel testo, oppure `None` se non trovato. Non restituisce un semplice booleano o il testo trovato direttamente. Per ottenere la stringa effettivamente trovata, chiama `.group()` sull'oggetto match: `match.group()` restituirebbe `"555-1234"`.

    **Concept Tested:** re.search()

---

#### 5. Cosa significa il quantificatore `+` in un pattern regex?

<div class="upper-alpha" markdown>
1. Fa corrispondere l'elemento precedente esattamente una volta
2. Fa corrispondere l'elemento precedente una o più volte
3. Fa corrispondere l'elemento precedente zero o una volta (rendendolo opzionale)
4. Fa corrispondere l'elemento precedente zero o più volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il quantificatore `+` significa "una o più volte" — l'elemento precedente deve apparire almeno una volta. Per esempio, `\d+` corrisponde a una o più cifre: corrisponde a `"5"`, `"42"`, `"1000"` ma NON a una stringa vuota. Confronta: `*` significa zero o più (può essere assente), `?` significa zero o una (opzionale), `{n}` significa esattamente n volte.

    **Concept Tested:** Quantifiers

---

#### 6. Cosa restituisce `re.findall(r"\d+", "I have 3 cats and 12 fish")`?

<div class="upper-alpha" markdown>
1. `"3"` (solo il primo numero trovato)
2. `None`
3. `["3", "12"]` (una lista di tutte le corrispondenze)
4. `2` (il conteggio delle corrispondenze)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `re.findall()` restituisce una lista di tutte le corrispondenze non sovrapposte come stringhe. Per `\d+` (una o più cifre) applicato a `"I have 3 cats and 12 fish"`, trova `"3"` e `"12"` e le restituisce come `["3", "12"]`. A differenza di `re.search()` che si ferma alla prima corrispondenza, `findall()` raccoglie tutte le occorrenze.

    **Concept Tested:** re.findall()

---

#### 7. Cosa produce `re.sub(r"\s+", "-", "hello world  foo")`?

<div class="upper-alpha" markdown>
1. `"hello world  foo"` (invariata, perché sub funziona solo con corrispondenze esatte)
2. `"hello-world-foo"`
3. `["hello", "world", "foo"]`
4. `"hello-world  foo"` (viene sostituita solo la prima corrispondenza)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `re.sub(pattern, replacement, text)` sostituisce tutte le corrispondenze del pattern con la stringa di sostituzione. `\s+` corrisponde a uno o più caratteri di spazio bianco. Lo spazio singolo tra "hello" e "world" e il doppio spazio tra "world" e "foo" vengono entrambi sostituiti con `"-"`, dando `"hello-world-foo"`. Per default, `re.sub()` sostituisce tutte le occorrenze.

    **Concept Tested:** re.sub()

---

#### 8. Cosa fa l'ancora `^` in un pattern regex?

<div class="upper-alpha" markdown>
1. Corrisponde a qualsiasi carattere eccetto il ritorno a capo
2. Segna la fine del pattern da far corrispondere
3. Rende il pattern senza distinzione tra maiuscole e minuscole
4. Richiede che il pattern corrisponda all'inizio della stringa
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. L'ancora `^` afferma che la corrispondenza deve verificarsi all'inizio della stringa. Per esempio, `r"^\d"` corrisponde a stringhe che iniziano con una cifra. Senza `^`, `re.search(r"\d", text)` trova una cifra ovunque nel testo. L'ancora `$` richiede in modo simile che la corrispondenza sia alla fine della stringa. Insieme, `^...$` corrisponde all'intera stringa.

    **Concept Tested:** Anchors

---

#### 9. Cosa restituisce `re.split(r",\s*", "apples, oranges,bananas,  grapes")`?

<div class="upper-alpha" markdown>
1. `"apples oranges bananas grapes"` (tutte le virgole rimosse)
2. `["apples", "oranges", "bananas", "grapes"]`
3. `["apples, oranges", "bananas,  grapes"]`
4. `4` (il numero di elementi)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `re.split(pattern, text)` divide il testo a ogni corrispondenza del pattern, restituendo una lista dei pezzi. Il pattern `r",\s*"` corrisponde a una virgola seguita da zero o più caratteri di spazio bianco, gestendo tutti i diversi stili di spaziatura attorno alle virgole. Il risultato è una lista pulita: `["apples", "oranges", "bananas", "grapes"]`.

    **Concept Tested:** re.split()

---

#### 10. A cosa corrisponde il carattere `.` in un'espressione regolare?

<div class="upper-alpha" markdown>
1. Solo a un carattere punto letterale
2. A qualsiasi singolo carattere eccetto un ritorno a capo
3. A qualsiasi cifra o lettera (ma non alla punteggiatura)
4. A zero o più del carattere precedente
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In una regex, `.` è un carattere jolly che corrisponde a qualsiasi singolo carattere eccetto un ritorno a capo (`\n`). Per esempio, `r"c.t"` corrisponderebbe a `"cat"`, `"cut"`, `"c4t"`, e `"c!t"`. Per far corrispondere un punto letterale, fai l'escape: `r"\."`. I quantificatori `*` e `+` controllano la ripetizione — non corrispondono a `.`.

    **Concept Tested:** Pattern Elements

---
