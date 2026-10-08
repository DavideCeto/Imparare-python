# Quiz: Altri Booleani e Condizionali

Verifica la tua comprensione della truthiness, della valutazione a corto circuito, delle espressioni ternarie, e delle condizioni composte con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale dei seguenti valori è considerato "falsy" in Python?

<div class="upper-alpha" markdown>
1. `"False"` (la stringa con il testo)
2. `[0]` (una lista contenente zero)
3. `1` (l'intero uno)
4. `[]` (una lista vuota)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. In Python, una lista vuota `[]` è falsy — viene trattata come `False` in un contesto booleano. `"False"` (una stringa non vuota) è truthy, `[0]` (una lista con un elemento) è truthy, e `1` è truthy. La lista completa dei valori falsy include: `False`, `0`, `0.0`, `""`, `[]`, `{}`, e `None`.

    **Concept Tested:** Truthiness and Falsiness

---

#### 2. Come puoi usare la truthiness per controllare se una stringa `name` non è vuota?

<div class="upper-alpha" markdown>
1. `if name == True:`
2. `if name != "":`
3. `if name:`
4. `if len(name) != 0:`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Dato che le stringhe vuote sono falsy e le stringhe non vuote sono truthy, `if name:` è `True` quando `name` contiene testo e `False` quando è vuota. Questo è più Pythonic (stile Python idiomatico) rispetto a confrontare esplicitamente con `!= ""` o controllare `len(name) != 0`. Tutte le tre opzioni B, C, e D producono lo stesso risultato, ma C è lo stile preferito.

    **Concept Tested:** Truthiness and Falsiness

---

#### 3. Cos'è la valutazione a corto circuito con `and`?

<div class="upper-alpha" markdown>
1. Python valuta prima il lato destro per risparmiare tempo
2. Python interrompe la valutazione di un'espressione `and` non appena il lato sinistro è falsy, senza controllare il lato destro
3. Python esegue entrambi i lati di `and` contemporaneamente in parallelo
4. Python memorizza il risultato nella cache così non esegue mai la stessa espressione due volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Con `and`, se l'operando sinistro è falsy, l'espressione complessiva non può mai essere `True`, quindi Python restituisce immediatamente il valore sinistro senza valutare il lato destro. Questo previene potenziali errori — per esempio, `data and data.upper()` non va in crash se `data` è `None`, perché il corto circuito si ferma prima di chiamare `.upper()`.

    **Concept Tested:** Short-Circuit Evaluation

---

#### 4. Cosa restituisce l'espressione `name or "stranger"` quando `name = ""`?

<div class="upper-alpha" markdown>
1. `True`
2. `""` (la stringa vuota)
3. `"stranger"`
4. Un errore, perché non puoi usare `or` con le stringhe
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `or` fa corto circuito su un lato sinistro truthy, ma `""` è falsy, quindi Python continua al lato destro e restituisce `"stranger"`. Questo è un utile pattern di valore predefinito: `value or default` restituisce `value` se è truthy, altrimenti restituisce `default`. Quando `name = "Monty"`, l'espressione restituisce `"Monty"` perché è truthy.

    **Concept Tested:** Short-Circuit Evaluation

---

#### 5. Qual è il modo corretto di controllare se `result` è `None`?

<div class="upper-alpha" markdown>
1. `if result == None:`
2. `if result = None:`
3. `if result is None:`
4. `if result.isNone():`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Per `None`, `True`, e `False`, lo stile Python raccomanda di usare `is` invece di `==`. `is` controlla l'identità (se due nomi si riferiscono esattamente allo stesso oggetto in memoria), mentre `==` controlla l'uguaglianza di valore. Dato che `None` è un singleton in Python (esiste solo un oggetto `None`), `is None` è il modo corretto e Pythonic di controllarlo.

    **Concept Tested:** Checking for None with is

---

#### 6. A cosa si valuta questa espressione ternaria quando `score = 85`?

```python
grade = "pass" if score >= 70 else "fail"
```

<div class="upper-alpha" markdown>
1. `"fail"`
2. `None`
3. `True`
4. `"pass"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Un'espressione ternaria ha la forma `valore_se_vero if condizione else valore_se_falso`. Quando `score = 85`, la condizione `score >= 70` è `True` (85 è almeno 70), quindi l'espressione si valuta a `"pass"`. Se `score` fosse `65`, la condizione sarebbe `False` e il risultato sarebbe `"fail"`.

    **Concept Tested:** Ternary Expression

---

#### 7. Qual è la differenza tra la conversione di tipo implicita ed esplicita?

<div class="upper-alpha" markdown>
1. La conversione implicita è più lenta; la conversione esplicita è più veloce
2. La conversione implicita avviene automaticamente (ad es., int + float → float); la conversione esplicita usa funzioni come `int()` o `str()`
3. La conversione implicita richiede `import`; la conversione esplicita è incorporata
4. La conversione implicita funziona solo con i numeri; la conversione esplicita funziona con qualsiasi tipo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La conversione implicita (chiamata anche coercizione) avviene automaticamente quando Python decide che la conversione è sicura — per esempio, `3 + 2.5` converte `3` in `3.0` automaticamente, dando `5.5`. La conversione esplicita è quando chiami deliberatamente `int()`, `float()`, `str()`, o `bool()` per controllare tu stesso la conversione.

    **Concept Tested:** Implicit vs Explicit Conversion

---

#### 8. Cosa fa `x, y = input("Enter x and y: ").split()`?

<div class="upper-alpha" markdown>
1. Chiede all'utente due input separati con due prompt
2. Ottiene una riga di input dall'utente, la divide sugli spazi, e assegna le due parti a `x` e `y`
3. Crea una lista `[x, y]` dall'input diviso
4. Genera un errore perché `split()` non può essere concatenato direttamente con `input()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `input()` restituisce una stringa con tutto ciò che l'utente ha scritto. `.split()` la divide sugli spazi bianchi, producendo una lista. L'assegnazione multipla poi scompone quella lista nelle variabili. Se l'utente scrive `3 7`, il risultato è `x = "3"` e `y = "7"` (ancora stringhe — hai bisogno di `int()` per convertirle per la matematica).

    **Concept Tested:** Reading Multiple Inputs

---

#### 9. Quale condizione composta controlla che `age` sia tra 13 e 17 (inclusi)?

<div class="upper-alpha" markdown>
1. `if age > 13 or age < 17:`
2. `if age == 13 and age == 17:`
3. `if 13 <= age <= 17:`
4. `if age >= 13 or age <= 17:`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python supporta i confronti concatenati che si leggono come la matematica: `13 <= age <= 17` controlla che age sia almeno 13 E al massimo 17. Questo equivale a `age >= 13 and age <= 17`. Le opzioni A e D che usano `or` sarebbero vere per quasi qualsiasi età, e l'opzione B (usando `==` e `and`) è impossibile — nessun valore può essere uguale sia a 13 sia a 17 contemporaneamente.

    **Concept Tested:** Compound Conditions

---

#### 10. Quale valore NON è falsy in Python?

<div class="upper-alpha" markdown>
1. `None`
2. `0`
3. `"0"` (la stringa contenente zero)
4. `[]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `"0"` è una stringa non vuota contenente un carattere — la cifra zero. Le stringhe non vuote sono truthy in Python, indipendentemente dai caratteri che contengono. Il numero `0` (intero), `None`, e `[]` (lista vuota) sono tutti falsy. Questa distinzione tra il numero zero e la stringa `"0"` è una fonte comune di confusione.

    **Concept Tested:** Truthiness and Falsiness

---
