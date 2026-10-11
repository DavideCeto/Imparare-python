# Quiz: Strumenti di Sviluppo Python

Verifica la tua comprensione degli IDE Python, della REPL, di pip, degli ambienti virtuali, e dell'ecosistema Python con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Quale versione di Python dovresti usare per i nuovi progetti?

<div class="upper-alpha" markdown>
1. Python 2, perché è più stabile e largamente usato
2. Python 1, la versione originale
3. Python 3, la versione attuale che tutti usano oggi
4. La versione che è arrivata con il tuo sistema operativo, qualunque sia
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python 3 è lo standard attuale. Python 2 ha raggiunto la fine del suo ciclo di vita nel 2020 e non è più aggiornato o supportato. Se vedi codice Python 2, puoi riconoscerlo da `print "hello"` (senza parentesi). Installa sempre Python 3 ed esegui i tuoi programmi con `python3`.

    **Concept Tested:** Python 2 vs Python 3

---

#### 2. Per cosa è più adatto Thonny?

<div class="upper-alpha" markdown>
1. Lo sviluppo web professionale e il deploy di server
2. Il machine learning con accelerazione GPU
3. I principianti e gli studenti che imparano Python, specialmente per eseguire il codice passo passo con il debugger
4. La data science e il calcolo scientifico con pandas e NumPy
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Thonny (thonny.org) è progettato specificamente per imparare Python. Il suo debugger integrato mostra esattamente come cambiano le variabili mentre ogni riga viene eseguita, rendendolo ideale per principianti dai 10 ai 15 anni che imparano il controllo di flusso e il debug. VS Code e PyCharm sono migliori per i progetti professionali; Spyder è migliore per la data science.

    **Concept Tested:** Thonny IDE

---

#### 3. Cosa significa REPL, e cosa fa?

<div class="upper-alpha" markdown>
1. Run-Execute-Print-Loop — un ciclo che esegue un intero script Python e poi si ripete
2. Read-Eval-Print Loop — una shell interattiva dove scrivi espressioni Python e vedi i risultati immediatamente
3. Recursive-Execution-Protocol-Language — il motore di esecuzione interno di Python
4. Remote-Execution-Python-Layer — un servizio cloud che esegue script Python online
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La REPL (Read-Eval-Print Loop) è la shell interattiva di Python. Avviala scrivendo `python3` nel tuo terminale. Scrivi un'espressione, Python la legge, la valuta, stampa il risultato, e torna indietro per altro. È perfetta per esperimenti rapidi, testare una formula, o esplorare un modulo senza scrivere uno script completo.

    **Concept Tested:** Python REPL

---

#### 4. Per cosa si usa `pip`?

<div class="upper-alpha" markdown>
1. Eseguire script Python dal terminale
2. Installare pacchetti da PyPI (Python Package Index) che non sono nella libreria standard
3. Convertire automaticamente il codice Python 2 in Python 3
4. Creare interfacce grafiche utente in Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `pip` è l'installatore di pacchetti di Python. Esegui `pip install nome_pacchetto` nel tuo terminale per scaricare e installare qualsiasi pacchetto da PyPI (pypi.org), che ospita centinaia di migliaia di pacchetti Python open-source. Per esempio, `pip install matplotlib` installa la libreria matplotlib per creare grafici.

    **Concept Tested:** pip

---

#### 5. Cos'è un ambiente virtuale in Python?

<div class="upper-alpha" markdown>
1. Un computer nel cloud dove Python gira da remoto
2. Un'installazione Python isolata con i propri pacchetti, che impedisce ai diversi progetti di entrare in conflitto tra loro
3. Un'interfaccia grafica che mostra visivamente le variabili Python
4. Una modalità speciale che fa girare Python più velocemente usando la GPU
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un ambiente virtuale è una copia isolata di Python con i propri pacchetti installati. Questo previene i conflitti tra progetti — il Progetto A potrebbe aver bisogno di `requests==2.28` e il Progetto B potrebbe aver bisogno di `requests==2.31`. Con gli ambienti virtuali, ogni progetto usa esattamente i pacchetti di cui ha bisogno senza influenzare gli altri. Creane uno con `python3 -m venv venv` e attivalo con `source venv/bin/activate` (Mac/Linux).

    **Concept Tested:** Virtual Environments

---

#### 6. Per cosa è usato meglio un Jupyter Notebook?

<div class="upper-alpha" markdown>
1. Scrivere grandi programmi orientati agli oggetti con molte classi
2. Costruire server web e API REST
3. L'analisi dei dati e i report che mescolano celle di codice eseguibile con testo esplicativo e output come grafici
4. Sviluppare app mobili per iOS e Android
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un Jupyter Notebook è un formato di documento che combina celle di codice eseguibile, testo Markdown, e output ricco (grafici, tabelle, immagini) in un singolo file. Questo lo rende ideale per l'analisi dei dati, gli esperimenti di machine learning, e i report condivisibili dove vuoi spiegare il codice insieme ai risultati. Google Colab fornisce Jupyter Notebook gratuiti ospitati nel cloud.

    **Concept Tested:** Jupyter Notebooks

---

#### 7. Come esegui uno script Python chiamato `my_script.py` dal terminale?

<div class="upper-alpha" markdown>
1. `open my_script.py`
2. `python3 my_script.py`
3. `run my_script.py`
4. `execute my_script.py`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Per eseguire uno script Python dal terminale (Prompt dei Comandi su Windows, Terminale su Mac/Linux), scrivi `python3 my_script.py`. Su Windows potresti usare `python` invece di `python3`. Assicurati di essere nella stessa directory dello script, oppure fornisci il percorso completo. Lo script gira dall'inizio alla fine e termina quando ha finito.

    **Concept Tested:** Running Scripts

---

#### 8. Per cosa è più conosciuto Google Colab?

<div class="upper-alpha" markdown>
1. Un ambiente Jupyter Notebook gratuito basato sul cloud con librerie di data science pre-installate e accesso GPU gratuito
2. Un IDE adatto ai principianti con un debugger integrato per uso scolastico
3. Un IDE professionale con integrazione Git e autocompletamento per progetti di squadra
4. Un gestore di pacchetti per installare librerie Python offline
</div>

??? question "Mostra risposta"
    La risposta corretta è **A**. Google Colab (colab.research.google.com) è un servizio Jupyter Notebook gratuito ospitato nel cloud. Viene fornito pre-installato con NumPy, pandas, TensorFlow, e altre librerie di data science, e fornisce accesso GPU gratuito per il machine learning. Hai bisogno solo di un account Google — nessuna installazione richiesta.

    **Concept Tested:** Google Colab

---

#### 9. Come puoi riconoscere il codice scritto per Python 2 (invece di Python 3)?

<div class="upper-alpha" markdown>
1. Usa istruzioni `import` invece di istruzioni `from`
2. Usa `print "hello"` senza parentesi, e `5/2` dà `2` invece di `2.5`
3. Richiede `end=""` alla fine di ogni chiamata a `print()`
4. Usa parentesi graffe `{}` per i blocchi di codice invece dell'indentazione
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il codice Python 2 usa `print "hello"` (un'istruzione, non una chiamata di funzione) e la divisione intera dove `5/2 = 2`. Python 3 richiede le parentesi: `print("hello")` e restituisce un float: `5/2 = 2.5`. Python 2 ha raggiunto la fine del suo ciclo di vita nel 2020, quindi evita di usarlo. Se trovi vecchio codice Python 2, usa lo strumento `2to3` per aiutare a convertirlo.

    **Concept Tested:** Python 2 vs Python 3

---

#### 10. Quale comando controlla quale versione di Python è installata?

<div class="upper-alpha" markdown>
1. `pip version`
2. `import python`
3. `python3 --version`
4. `check python`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Eseguire `python3 --version` (oppure `python --version` su Windows) nel terminale stampa la versione di Python installata, come `Python 3.11.4`. Dopo aver installato Python da python.org, questo è il modo standard per verificare che l'installazione sia andata a buon fine. Su alcuni sistemi puoi anche usare `python3 -V` (V maiuscola) come scorciatoia.

    **Concept Tested:** Installing Python

---
