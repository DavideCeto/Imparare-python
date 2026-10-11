# Quiz: Libreria Standard e JSON

Verifica la tua comprensione dei moduli Python, dei dati JSON, dei moduli sys e os, e del modulo collections con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è un modulo Python?

<div class="upper-alpha" markdown>
1. Una funzione built-in come `print()` o `len()`
2. Un file `.py` contenente funzioni, variabili, e classi che possono essere importate e riutilizzate
3. Un commento speciale che dice a Python di caricare funzionalità extra
4. Una cartella contenente più programmi Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un modulo è semplicemente un file `.py`. Qualsiasi file Python può essere un modulo — ci scrivi funzioni e variabili, poi usi `import nome_modulo` in un altro file per accedervi. Python viene anche fornito con molti moduli pre-costruiti (la libreria standard) come `math`, `random`, `os`, `sys`, e `json`.

    **Concept Tested:** Custom Modules

---

#### 2. Cosa fa il guardiano `if __name__ == "__main__":`?

<div class="upper-alpha" markdown>
1. Fa girare il programma più velocemente saltando gli import
2. Controlla se il modulo è già stato importato prima
3. Assicura che il blocco indentato giri solo quando il file viene eseguito direttamente, non quando viene importato
4. Definisce il punto di ingresso per un server web
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Quando Python esegue un file direttamente, `__name__` è uguale a `"__main__"`. Quando un file viene importato come modulo, `__name__` è uguale al nome del file del modulo. Il guardiano `if __name__ == "__main__":` si usa per mettere il codice di test o la logica dello script che dovrebbe girare solo quando esegui il file direttamente — non quando un altro programma lo importa.

    **Concept Tested:** __name__ Guard

---

#### 3. Cosa contiene `sys.argv`?

<div class="upper-alpha" markdown>
1. La lista di tutti i moduli attualmente importati nel programma
2. Gli argomenti della riga di comando passati allo script Python quando è stato eseguito
3. Una lista di tutte le funzioni definite nel programma
4. La versione dell'interprete Python e le informazioni sulla piattaforma
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `sys.argv` è una lista di stringhe che rappresentano gli argomenti della riga di comando. `sys.argv[0]` è sempre il nome dello script stesso. Se esegui `python my_script.py hello 42`, allora `sys.argv` è uguale a `["my_script.py", "hello", "42"]`. Questo permette ai programmi di accettare configurazioni dalla riga di comando senza usare `input()`.

    **Concept Tested:** sys Module

---

#### 4. Cosa restituisce `os.path.exists("data.txt")`?

<div class="upper-alpha" markdown>
1. Il percorso completo a `data.txt` sul tuo computer
2. `True` se il file o la cartella esiste, `False` se non esiste
3. La dimensione del file in byte
4. La data e l'ora dell'ultima modifica del file
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `os.path.exists(path)` controlla se un file o una directory esiste al percorso dato e restituisce `True` o `False`. Questo è utile prima di provare ad aprire un file — puoi controllare prima per evitare un `FileNotFoundError`. Il sottomodulo `os.path` ha molte altre funzioni utili come `os.path.join()` e `os.path.basename()`.

    **Concept Tested:** os Module

---

#### 5. Cos'è JSON?

<div class="upper-alpha" markdown>
1. Un formato binario specifico di Python per salvare i dati del programma
2. Un formato di testo per memorizzare dati strutturati che assomiglia ai dizionari e alle liste di Python
3. Un tipo di file cifrato usato per memorizzare le password in sicurezza
4. Un linguaggio di database simile a SQL
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. JSON (JavaScript Object Notation) è un formato di testo leggero per i dati strutturati. Usa le parentesi graffe `{}` per gli oggetti (come i dizionari Python), le parentesi quadre `[]` per gli array (come le liste Python), e `true`/`false`/`null` per i booleani e None. JSON è il formato più comune per le API web e i file di configurazione, e il modulo `json` di Python lo rende facile da leggere e scrivere.

    **Concept Tested:** JSON Format

---

#### 6. Cosa restituisce `json.loads('{"x": 1}')`?

<div class="upper-alpha" markdown>
1. La stringa `'{"x": 1}'` invariata
2. Un dizionario Python `{"x": 1}`
3. Una lista Python `[{"x": 1}]`
4. Un errore perché JSON richiede le virgolette doppie attorno alle chiavi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `json.loads(text)` analizza una stringa JSON e restituisce l'oggetto Python equivalente. `{"x": 1}` in JSON diventa un `dict` Python. Il nome della funzione "loads" sta per "load string". JSON usa le virgolette doppie per le stringhe, il che è Python valido quando la stringa è dentro virgolette singole. Il risultato è un dizionario Python nativo che puoi usare come qualsiasi altro.

    **Concept Tested:** json.loads()

---

#### 7. Cosa fa `json.dumps({"name": "Alice", "age": 14})`?

<div class="upper-alpha" markdown>
1. Salva il dizionario direttamente in un file chiamato `Alice.json`
2. Stampa il dizionario sulla console in formato JSON
3. Converte il dizionario Python in una stringa in formato JSON
4. Carica il dizionario da un file JSON
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `json.dumps(obj)` converte un oggetto Python (dict, list, numero, stringa, bool, o None) in una stringa in formato JSON. Il nome "dumps" sta per "dump string". Per salvare JSON in un file, usa invece `json.dump(obj, file_object)`. `json.dumps()` è utile quando hai bisogno di una stringa JSON in memoria, per esempio per inviarla su una rete.

    **Concept Tested:** json.dumps()

---

#### 8. A quale tipo Python corrisponde `true` di JSON?

<div class="upper-alpha" markdown>
1. La stringa `"true"`
2. L'intero `1`
3. Il booleano Python `True`
4. Il valore Python `None`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. JSON usa `true` e `false` minuscoli per i booleani; Python usa `True` e `False` con la maiuscola. Quando `json.loads()` incontra `true` in JSON, lo converte nel `True` di Python. In modo simile, `false` di JSON diventa `False` di Python, e `null` di JSON diventa `None` di Python.

    **Concept Tested:** JSON Type Mapping

---

#### 9. Cosa produce `os.path.join("folder", "file.txt")`?

<div class="upper-alpha" markdown>
1. `"folder file.txt"` (con uno spazio)
2. `"folder/file.txt"` su Mac/Linux oppure `"folder\file.txt"` su Windows, usando il separatore corretto per il sistema operativo
3. Sempre `"folder/file.txt"` indipendentemente dal sistema operativo
4. Un errore perché non puoi unire i percorsi senza una barra iniziale
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `os.path.join()` costruisce un percorso di file usando il separatore corretto per il sistema operativo attuale — barra `/` su Mac e Linux, backslash `\` su Windows. Non concatenare mai manualmente le stringhe dei percorsi con `"/"` perché il tuo codice si romperebbe su Windows. Usa sempre `os.path.join()` per costruire percorsi portabili e multipiattaforma.

    **Concept Tested:** os.path

---

#### 10. Qual è la differenza tra `json.loads()`/`json.dumps()` e `json.load()`/`json.dump()`?

<div class="upper-alpha" markdown>
1. `loads`/`dumps` sono più veloci; `load`/`dump` producono un output meglio formattato
2. `loads`/`dumps` funzionano con le stringhe; `load`/`dump` funzionano con gli oggetti file
3. `loads` legge una riga; `load` legge l'intero file
4. Sono identici — la `s` extra è solo un alias
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `json.loads(text)` analizza da una stringa; `json.dumps(obj)` serializza in una stringa. `json.load(file)` legge JSON direttamente da un oggetto file aperto; `json.dump(obj, file)` scrive JSON direttamente su un oggetto file aperto. Usa le versioni con la `s` (loads/dumps) per le stringhe in memoria; usa le versioni senza `s` (load/dump) quando lavori con i file.

    **Concept Tested:** json Module Functions

---
