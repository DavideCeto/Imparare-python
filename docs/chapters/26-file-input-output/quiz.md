# Quiz: Input e Output su File

Verifica la tua comprensione delle modalità dei file, dell'istruzione with, della lettura e scrittura dei file, e della gestione dei CSV con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa fa l'istruzione `with` quando usata con `open()`?

<div class="upper-alpha" markdown>
1. Rende il file di sola lettura così non può essere cambiato accidentalmente
2. Apre il file, esegue il blocco indentato, e chiude automaticamente il file quando ha finito
3. Crea una copia di backup del file prima di aprirlo
4. Scarica il file da internet sul tuo computer
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'istruzione `with` è un context manager. Quando scrivi `with open("file.txt") as f:`, Python apre il file, esegue il blocco indentato, e chiude il file automaticamente quando il blocco finisce — anche se si verifica un errore dentro il blocco. Questo previene il bug comune di dimenticare di chiudere il file.

    **Concept Tested:** with Statement

---

#### 2. Quale modalità di file dovresti usare per aggiungere contenuto alla fine di un file esistente senza eliminare ciò che c'è già?

<div class="upper-alpha" markdown>
1. `"r"` (modalità lettura)
2. `"w"` (modalità scrittura)
3. `"a"` (modalità aggiunta)
4. `"e"` (modalità estensione)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Aprire un file con `"a"` (modalità aggiunta/append) aggiunge nuovo contenuto alla fine del file esistente. La modalità `"w"` (scrittura) crea un nuovo file o sovrascrive l'intero contenuto esistente. La modalità `"r"` (lettura) permette solo di leggere — non puoi scriverci. Non esiste una modalità `"e"` in Python.

    **Concept Tested:** File Modes

---

#### 3. Cosa fa `open("data.txt", "w")` se `data.txt` esiste già?

<div class="upper-alpha" markdown>
1. Genera un `FileExistsError` perché il file esiste già
2. Apre il file per la lettura senza cambiare nulla
3. Crea un nuovo file con un nome diverso come `data(1).txt`
4. Crea un nuovo file vuoto, sovrascrivendo ed eliminando tutto il contenuto esistente
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. La modalità scrittura (`"w"`) sovrascrive completamente il file. Se il file esiste già, il suo contenuto precedente viene eliminato e sostituito. Se il file non esiste, Python lo crea. Questo è il motivo per cui è importante usare `"a"` (modalità aggiunta) se vuoi preservare il contenuto esistente.

    **Concept Tested:** File Modes

---

#### 4. Perché devi aggiungere `"\n"` quando scrivi righe in un file con `f.write()`?

<div class="upper-alpha" markdown>
1. Perché `write()` rimuove automaticamente tutte le terminazioni di riga dal testo
2. Perché `write()` non aggiunge automaticamente un carattere di ritorno a capo — devi aggiungerlo tu stesso
3. Perché `"\n"` dice a Python di scrivere immediatamente il file sul disco
4. Perché i file su Windows richiedono doppi ritorni a capo (`"\n\n"`) tra le righe
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. A differenza di `print()`, che aggiunge automaticamente un ritorno a capo alla fine di ogni chiamata, `f.write()` scrive esattamente ciò che gli dai — niente di più. Se vuoi che ogni pezzo di testo sia sulla sua propria riga nel file, devi includere `"\n"` alla fine: `f.write("Hello\n")`. Senza di esso, tutto il tuo testo finisce insieme su una riga.

    **Concept Tested:** Writing to a File

---

#### 5. Cosa restituisce `f.read()`?

<div class="upper-alpha" markdown>
1. Una lista dove ogni elemento è una riga del file
2. L'intero contenuto del file come una singola stringa
3. Solo la prima riga del file
4. Il numero di caratteri nel file
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `f.read()` legge l'intero file e restituisce tutto il suo contenuto come una grande stringa, inclusi tutti i caratteri di ritorno a capo `"\n"`. Per ottenere una lista con ogni riga come elemento separato, usa `f.readlines()`. Per elaborare una riga alla volta in modo efficiente (specialmente per file grandi), itera direttamente sull'oggetto file con `for line in f:`.

    **Concept Tested:** Reading Files

---

#### 6. Qual è la differenza tra `f.read()` e `f.readlines()`?

<div class="upper-alpha" markdown>
1. `read()` legge file di testo; `readlines()` legge file binari
2. `read()` restituisce una singola stringa con tutto il contenuto; `readlines()` restituisce una lista dove ogni elemento è una riga
3. `read()` è più veloce; `readlines()` è più accurato
4. `read()` richiede la modalità `"r"`; `readlines()` funziona con qualsiasi modalità
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `f.read()` restituisce l'intero file come una stringa. `f.readlines()` legge il file e restituisce una lista dove ogni elemento è una riga del file (con il carattere `"\n"` ancora attaccato). Entrambi richiedono un file aperto in modalità lettura. Usa `readlines()` quando vuoi elaborare ogni riga separatamente senza dividerla manualmente.

    **Concept Tested:** readlines()

---

#### 7. Cosa fa `"r"` (modalità lettura) se il file non esiste?

<div class="upper-alpha" markdown>
1. Python crea un nuovo file vuoto con quel nome
2. Python restituisce una stringa vuota da `f.read()`
3. Python genera un `FileNotFoundError`
4. Python chiede all'utente di scrivere il contenuto del file dalla tastiera
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La modalità lettura (`"r"`) richiede che il file esista già. Se il file non viene trovato, Python genera `FileNotFoundError`. Puoi gestirlo con eleganza con un blocco `try/except FileNotFoundError:`. La modalità scrittura (`"w"`) e la modalità aggiunta (`"a"`) creano entrambe il file se non esiste.

    **Concept Tested:** File Modes

---

#### 8. Quale modulo Python importi per leggere e scrivere file CSV?

<div class="upper-alpha" markdown>
1. `import files`
2. `import csv`
3. `import spreadsheet`
4. `import tabular`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La libreria standard di Python include il modulo `csv` per leggere e scrivere file CSV (Comma-Separated Values). Gestisce automaticamente casi difficili come le virgole dentro campi tra virgolette. Usa `csv.reader(f)` per leggere le righe e `csv.writer(f)` per scriverle. Non esiste un modulo `files`, `spreadsheet`, o `tabular` nella libreria standard.

    **Concept Tested:** CSV Module

---

#### 9. Cosa ti dà ogni iterazione quando fai un ciclo su un oggetto file con `for line in f:`?

<div class="upper-alpha" markdown>
1. Un carattere alla volta dal file
2. Una parola alla volta separata da spazi
3. Una riga alla volta come stringa, incluso il `"\n"` finale
4. Una tupla di `(numero_riga, testo_riga)` per ogni riga
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Iterare direttamente su un oggetto file con `for line in f:` ti dà una riga per iterazione come stringa. La riga include il carattere di ritorno a capo finale `"\n"` (eccetto forse l'ultima riga). Usa `line.strip()` per rimuovere gli spazi bianchi iniziali/finali incluso `"\n"`. Questo è efficiente in termini di memoria per i file grandi perché Python legge una riga alla volta invece di caricare tutto in una volta.

    **Concept Tested:** Line Iteration

---

#### 10. Cos'è la cartella di lavoro attuale (current working directory)?

<div class="upper-alpha" markdown>
1. La cartella dove Python è installato sul tuo computer
2. La cartella attualmente attiva — la cartella in cui Python cerca quando specifichi un nome di file senza un percorso completo
3. L'ultima cartella che hai visitato prima di eseguire Python
4. La cartella dove sono memorizzati tutti i file della libreria standard di Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La cartella di lavoro attuale (CWD) è la cartella che Python usa come punto di partenza quando dai un nome di file senza un percorso completo. Se il tuo script è in `~/projects/` e scrivi `open("data.txt")`, Python cerca `data.txt` in `~/projects/`. Puoi controllare la CWD con `import os; print(os.getcwd())` e navigare nel terminale con `cd`.

    **Concept Tested:** Current Working Directory

---
