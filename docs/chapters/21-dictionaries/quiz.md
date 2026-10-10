# Quiz: Dizionari

Verifica la tua comprensione dei dizionari Python, dell'accesso chiave-valore, dell'iterazione, e delle dictionary comprehension con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Come crei un dizionario in Python con due voci?

<div class="upper-alpha" markdown>
1. `d = ["name": "Alice", "age": 12]`
2. `d = ("name": "Alice", "age": 12)`
3. `d = {"name": "Alice", "age": 12}`
4. `d = dict[name="Alice", age=12]`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. I dizionari si creano con le parentesi graffe `{}`, con ogni voce scritta come `chiave: valore` e le voci separate da virgole. Le chiavi devono essere univoche all'interno di un dizionario. I valori possono essere di qualsiasi tipo — stringhe, numeri, liste, o persino altri dizionari.

    **Concept Tested:** Creating Dictionaries

---

#### 2. Dati `grades = {"Alice": 95, "Bob": 87}`, cosa restituisce `grades["Alice"]`?

<div class="upper-alpha" markdown>
1. `"Alice"`
2. `0` (l'indice di "Alice")
3. `87`
4. `95`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. La ricerca nel dizionario con le parentesi quadre usa la chiave per recuperare il suo valore associato. `grades["Alice"]` restituisce `95`. A differenza delle liste (che usano indici interi a partire da 0), i dizionari usano le chiavi che hai definito — in questo caso, la stringa `"Alice"` mappa all'intero `95`.

    **Concept Tested:** Accessing Values by Key

---

#### 3. Cosa succede quando accedi a una chiave di dizionario che non esiste usando le parentesi quadre?

<div class="upper-alpha" markdown>
1. Python restituisce automaticamente `None`
2. Python crea la chiave con un valore predefinito di `0`
3. Python genera un `KeyError`
4. Python salta la riga e continua
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Se usi `d[key]` con una chiave che non è nel dizionario, Python genera un `KeyError`. Questo fa andare in crash il tuo programma a meno che tu non catturi l'errore. Per accedere in sicurezza a una chiave che potrebbe non esistere, usa `d.get(key)` che restituisce `None` (o un valore predefinito che specifichi) invece di andare in crash.

    **Concept Tested:** KeyError

---

#### 4. Cosa restituisce `grades.get("Dave", 0)` se `"Dave"` non è nel dizionario?

<div class="upper-alpha" markdown>
1. Un'eccezione `KeyError`
2. `None`
3. `"Dave"`
4. `0`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `dict.get(key, default)` restituisce il valore per `key` se esiste, altrimenti restituisce il valore `default`. Con `grades.get("Dave", 0)`, se `"Dave"` non è una chiave, il metodo restituisce `0`. Senza un valore predefinito, `get()` restituisce `None`. Questo è molto più sicuro che usare `d[key]` quando non sei sicuro se la chiave esiste.

    **Concept Tested:** Safe Access with get()

---

#### 5. Come aggiungi una nuova chiave `"Eve"` con valore `88` al dizionario `grades`?

<div class="upper-alpha" markdown>
1. `grades.add("Eve", 88)`
2. `grades.append({"Eve": 88})`
3. `grades["Eve"] = 88`
4. `grades.insert("Eve", 88)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Aggiungere una nuova voce a un dizionario usa la stessa sintassi di aggiornamento di una esistente: `d[key] = value`. Se la chiave esiste già, questo aggiorna il suo valore. Se la chiave è nuova, questo crea una nuova voce. I dizionari non hanno metodi `add()`, `append()`, o `insert()`.

    **Concept Tested:** Adding and Updating Entries

---

#### 6. Quale metodo restituisce tutte le coppie chiave-valore come tuple per l'iterazione?

<div class="upper-alpha" markdown>
1. `d.keys()`
2. `d.values()`
3. `d.pairs()`
4. `d.items()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `d.items()` restituisce una vista di tutte le coppie `(chiave, valore)` come tuple. Puoi iterarci sopra con `for key, value in d.items():`. `d.keys()` dà solo le chiavi, `d.values()` dà solo i valori, e `d.pairs()` non è un metodo valido del dizionario.

    **Concept Tested:** Keys, Values, and Items

---

#### 7. Come controlli se la chiave `"Bob"` è in un dizionario senza rischiare un `KeyError`?

<div class="upper-alpha" markdown>
1. `grades.contains("Bob")`
2. `"Bob" in grades`
3. `grades.find("Bob")`
4. `grades.has_key("Bob")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'operatore `in` controlla l'appartenenza di una chiave in un dizionario e restituisce `True` o `False`. `"Bob" in grades` è il modo Pythonic standard per verificare se una chiave esiste. `has_key()` è stato rimosso in Python 3, `contains()` non è un metodo del dizionario, e `find()` è un metodo delle stringhe.

    **Concept Tested:** Key Membership with in

---

#### 8. Cosa ti permette di rappresentare un dizionario annidato?

<div class="upper-alpha" markdown>
1. Un dizionario dove tutti i valori devono essere dello stesso tipo
2. Dati strutturati dove un valore è esso stesso un dizionario, permettendo ricerche a più livelli
3. Un dizionario che ordina automaticamente le sue chiavi in ordine alfabetico
4. Un dizionario che può essere solo letto, non modificato
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un dizionario annidato è uno dove i valori sono essi stessi dizionari. Questo ti permette di rappresentare dati strutturati con più livelli — per esempio, una lista di contatti dove ogni contatto ha un telefono e un'email. L'accesso è concatenato: `contacts["Alice"]["phone"]` prima ottiene il sotto-dizionario di Alice, poi cerca "phone" al suo interno.

    **Concept Tested:** Nested Dictionaries

---

#### 9. Cosa produce questa dictionary comprehension?

```python
squares = {n: n * n for n in range(1, 4)}
```

<div class="upper-alpha" markdown>
1. `[1, 4, 9]`
2. `{1, 4, 9}` (un insieme)
3. `{1: 1, 2: 4, 3: 9}`
4. `{0: 0, 1: 1, 2: 4}`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una dictionary comprehension usa la forma `{espressione_chiave: espressione_valore for elemento in iterabile}`. Qui, `n` diventa la chiave e `n * n` diventa il valore. `range(1, 4)` produce 1, 2, 3 — quindi il risultato è `{1: 1, 2: 4, 3: 9}`. Le parentesi graffe con il pattern dei due punti la distinguono da una set comprehension.

    **Concept Tested:** Dictionary Comprehensions

---

#### 10. Cosa fa `d.pop("Bob")` se `"Bob"` esiste nel dizionario?

<div class="upper-alpha" markdown>
1. Rimuove "Bob" dal dizionario e restituisce il suo valore
2. Rimuove "Bob" dal dizionario e restituisce `None`
3. Rimuove l'ultimo elemento aggiunto al dizionario
4. Restituisce il valore di "Bob" ma lo lascia nel dizionario
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. `d.pop(key)` rimuove la voce con la chiave data dal dizionario e restituisce il suo valore. Se `grades = {"Bob": 87}`, allora `grades.pop("Bob")` restituisce `87` e `grades` diventa `{}`. Se la chiave non esiste, `pop()` genera un `KeyError` a meno che tu non fornisca un valore predefinito: `d.pop("Bob", None)`.

    **Concept Tested:** Removing Entries

---
