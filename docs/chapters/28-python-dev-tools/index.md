---
title: Strumenti di Sviluppo Python
description: Esplora i veri ambienti Python — Thonny, VS Code, Jupyter, pip, gli ambienti virtuali, la REPL, e il Raspberry Pi
generated_by: claude skill chapter-content-generator
date: 2026-06-28 14:40:00
version: 0.09
---

# Strumenti di Sviluppo Python

Alla fine di questa lezione sarai in grado di:

- Descrivere i principali ambienti di sviluppo Python e quando usare ciascuno
- Installare Python localmente ed eseguire script dal terminale
- Usare la **REPL di Python** (shell interattiva) per esperimenti rapidi
- Installare pacchetti con `pip` o `uv` e capire gli **ambienti virtuali**
- Spiegare quando un'attività Python lenta potrebbe essere una buona candidata per Rust

Skulpt è ottimo per imparare — non devi installare nulla.
Ma i veri progetti Python usano strumenti più ricchi. Questo capitolo è la tua mappa dell'ecosistema Python.

!!! mascot-welcome "Benvenuto/a al Capitolo 28!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sei pronto a togliere le rotelle di Skulpt ed entrare nel vero mondo Python!
    Ci sono molti ottimi strumenti tra cui scegliere — troviamo quello giusto per te.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Python 2 vs Python 3

Potresti occasionalmente vedere codice Python scritto per **Python 2** — una versione più vecchia che ha raggiunto la fine del suo ciclo di vita nel 2020.
Python 3 è quello che tutti usano oggi.

Differenze chiave che potresti incontrare nel vecchio codice Python 2:

| Caratteristica | Python 2 | Python 3 |
|---------|----------|----------|
| Print | `print "hello"` | `print("hello")` |
| Divisione intera | `5/2 = 2` | `5/2 = 2.5` |
| Tipo stringa | ASCII per default | Unicode per default |

Se vedi del codice che usa `print` senza parentesi, è stato scritto per Python 2.
Evitalo — installa Python 3.

## Ambienti di Sviluppo

Un **ambiente di sviluppo** (chiamato anche IDE — Integrated Development Environment) è dove scrivi, esegui, e fai debug del codice Python.
Ecco un confronto delle opzioni più popolari per i principianti e oltre.

### Thonny — Il Migliore per i Principianti

**Thonny** (thonny.org) è progettato specificamente per imparare Python.
Ha un'interfaccia semplice e un debugger integrato che ti mostra esattamente come cambiano le variabili mentre ogni riga viene eseguita.

**Migliore per:** principianti assoluti, dai 10 ai 15 anni, che imparano il controllo di flusso e il debug

### Repl.it — Collaborazione Basata su Browser

**Repl.it** (replit.com) ti permette di scrivere ed eseguire Python in un browser senza alcuna installazione.
Supporta più file e l'editing collaborativo.

**Migliore per:** condividere progetti, lavorare da qualsiasi computer, uso in club di programmazione

### VS Code — Scelta Professionale

**VS Code** (Visual Studio Code) è uno degli editor di codice più popolari al mondo.
Con l'estensione Python installata, fornisce autocompletamento, debug, un terminale integrato, integrazione Git, e centinaia di estensioni.

**Migliore per:** progetti seri, linguaggi multipli, flussi di lavoro professionali

### Spyder — Python Scientifico

**Spyder** è progettato per la data science e il calcolo scientifico.
Ha un esploratore di variabili che mostra visivamente i tuoi array NumPy e DataFrame.

**Migliore per:** analisi dei dati, calcolo scientifico, utenti che arrivano da MATLAB

### Jupyter Notebook — Data Science Interattiva

Un **Jupyter Notebook** è un documento che mescola testo (Markdown), celle di codice che puoi eseguire individualmente, e output (grafici, tabelle, risultati) tutto in un singolo file.

```python
# In a Jupyter Notebook, each "cell" is a runnable block:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.title("Squares")
plt.show()
```

**Migliore per:** analisi dei dati, machine learning, report che mescolano codice e spiegazione

### Google Colab — Jupyter Gratuito nel Cloud

**Google Colab** (colab.research.google.com) è un ambiente Jupyter Notebook gratuito ospitato nel cloud.
Viene fornito con NumPy, pandas, TensorFlow, e accesso GPU pre-installati — nessuna configurazione necessaria.

**Migliore per:** machine learning, accesso GPU gratuito, condivisione di notebook

### JupyterLab

**JupyterLab** è l'interfaccia Jupyter di nuova generazione — un IDE completo basato su browser con browser dei file, terminali, notebook, ed editor di testo tutto in uno.

## Installare Python Localmente

Per eseguire Python sul tuo computer:

1. Visita [python.org](https://python.org) e scarica l'ultimo installer di Python 3 per il tuo sistema operativo.
2. Esegui l'installer — su Windows, seleziona **"Add Python to PATH"** prima di cliccare Install.
3. Apri un terminale (Prompt dei Comandi su Windows, Terminale su Mac/Linux).
4. Scrivi `python3 --version` per verificare l'installazione.

## Eseguire Script dal Terminale

Una volta installato Python, puoi eseguire qualsiasi file `.py` dal terminale:

```bash
python3 my_script.py
```

Su Windows, potresti usare `python` invece di `python3`.

## La Shell REPL di Python

La **REPL** (Read-Eval-Print Loop) è la shell interattiva di Python.
Scrivi `python3` (o semplicemente `python`) nel terminale per avviarla.
Poi scrivi qualsiasi espressione Python e premi Invio — Python la valuta immediatamente.

```
>>> 2 + 2
4
>>> name = "Monty"
>>> print(f"Hello, {name}")
Hello, Monty
>>> [x**2 for x in range(5)]
[0, 1, 4, 9, 16]
```

La REPL è perfetta per esperimenti rapidi: testare una funzione, controllare una formula, esplorare un modulo.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `# This Skulpt window works like a mini-REPL!
# Try typing expressions and running them.

import math

# Quick experiments:
print(math.factorial(10))
print(math.gcd(48, 36))
print(2 ** 32)`);
</script>

## `pip` — L'Installatore di Pacchetti

La libreria standard di Python è grande, ma migliaia di pacchetti in più sono disponibili su PyPI (Python Package Index).
`pip` è lo strumento che li installa.

Per installare un pacchetto, esegui questo nel tuo terminale:

```bash
pip install requests
pip install matplotlib
pip install pillow
```

Per vedere cosa è installato: `pip list`

Per installare una versione specifica: `pip install requests==2.31.0`

## `uv` — Uno strumento Python veloce e tutto-in-uno

Man mano che i progetti crescono, potresti aver bisogno di diversi strumenti per installare Python,
creare un ambiente virtuale, aggiungere pacchetti, registrare le versioni esatte dei pacchetti,
eseguire script, costruire un pacchetto e pubblicarlo. **uv** riunisce molti di questi compiti in
un solo strumento. È un gestore di pacchetti e di progetti Python scritto in Rust, e include
un'interfaccia familiare, compatibile con `pip`.

Il team di uv riporta che nei suoi benchmark può essere da 10 a 100 volte più veloce di `pip`.
Il guadagno esatto dipende dal progetto, dal computer, dalla rete e dal fatto che i pacchetti siano
già nella cache di uv. Una **cache** conserva i file scaricati, così lo strumento può riutilizzarli
invece di scaricare di nuovo gli stessi file.

Una volta installato uv, questi comandi creano un progetto, aggiungono il pacchetto `requests`,
eseguono il suo programma Python e costruiscono i file che potrebbero essere pubblicati come pacchetto:

```bash
uv init weather-app
cd weather-app
uv add requests
uv run main.py
uv build
```

Per un progetto esistente che usa già `pip`, uv offre anche comandi simili:

```bash
uv venv
uv pip install requests
uv pip list
```

uv può prendere il posto di diversi strumenti separati, ma i suoi comandi non sono identici a quelli
di ogni strumento che sostituisce. Inizia con `uv pip` quando vuoi un modo di lavorare familiare.
Prova i comandi di livello più alto `uv add`, `uv lock`, `uv sync` e `uv run` quando vuoi che sia uv
a gestire l'intero progetto. Consulta la [documentazione ufficiale di uv](https://docs.astral.sh/uv/)
per le istruzioni di installazione per il tuo sistema operativo.

## Python vs. Rust

Di solito Python esegue il tuo codice sorgente tramite un interprete Python. Questo rende Python
veloce da imparare, modificare e provare. Rust è un **linguaggio compilato**: un compilatore controlla
il codice sorgente Rust e lo trasforma in un programma in codice macchina prima che tu lo esegua.
I programmi Rust compilati possono essere molto più veloci per alcuni tipi di lavoro, ma di solito
Rust richiede più tempo per essere imparato e scritto.

I computer moderni hanno diversi **core** del processore, come diversi lavoratori che possono
svolgere compiti separati nello stesso momento. Rust ha i thread, i canali per lo scambio di
messaggi, strumenti per lo stato condiviso e un sistema di tipi che individua molti errori di
concorrenza non sicuri già durante la compilazione. Queste caratteristiche possono aiutare un
programma progettato con cura a distribuire il lavoro pesante per la CPU su più core. Rust non
rende automaticamente parallelo ogni programma: il problema deve contenere lavoro che si possa
dividere in sicurezza in parti indipendenti.

Il confronto qui sotto riassume quando ciascun linguaggio è spesso la scelta migliore.

| Scegli Python quando... | Valuta Rust quando... |
|-------------------------|-----------------------|
| Stai imparando, sperimentando o costruendo una prima versione | Una parte lenta, misurata, esegue un'enorme quantità di calcoli ripetuti |
| Contano soprattutto un codice chiaro e uno sviluppo rapido | La velocità di esecuzione o il basso uso di memoria sono un requisito importante |
| Le librerie Python risolvono già le parti difficili | Il lavoro si può dividere in sicurezza su più core della CPU |
| Il programma passa la maggior parte del tempo ad aspettare file o la rete | Il codice deve diventare uno strumento a riga di comando veloce o un'estensione Python riutilizzabile |

Uno strumento di programmazione con l'IA può aiutarti a creare una prima versione in Rust di una
funzione Python piccola e ben testata. Può valere la pena provarci per filtri di immagini,
simulazioni, conversione di dati, compressione o altri cicli pesanti per la CPU che vengono eseguiti
milioni di volte. Prima, però, fai il **profiling** del programma Python, cioè misura dove passa
davvero il suo tempo. Convertire codice che non è un vero collo di bottiglia aggiunge complessità
senza rendere il programma sensibilmente più veloce.

La conversione fatta dall'IA è una bozza, non una prova che il nuovo programma sia corretto. Python
e Rust gestiscono in modo diverso i tipi, la memoria, gli errori e il lavoro in parallelo, quindi una
traduzione riga per riga potrebbe essere sbagliata o più lenta del previsto. Tieni dei test con
risposte note, confronta i risultati di Python e di Rust, misura entrambe le versioni e fai
controllare il codice Rust a una persona. Spesso la soluzione migliore mantiene la maggior parte del
progetto nel Python, amichevole e flessibile, e sposta in Rust un solo collo di bottiglia dimostrato.

## Ambienti Virtuali

Un **ambiente virtuale** è un'installazione Python isolata per un progetto specifico.
Permette a ogni progetto di avere il proprio insieme di pacchetti senza interferire con altri progetti.

Per creare e usare un ambiente virtuale:

```bash
# Create:
python3 -m venv myenv

# Activate (Mac/Linux):
source myenv/bin/activate

# Activate (Windows):
myenv\Scripts\activate

# Install packages (only inside this environment):
pip install flask

# Deactivate when done:
deactivate
```

**Perché preoccuparsene?** Immagina due progetti — uno ha bisogno di `requests 2.28`, un altro ha bisogno di `requests 2.31`.
Senza gli ambienti virtuali, installarne uno rompe l'altro. Con essi, ogni progetto è isolato.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto stampa informazioni sull'ambiente Python.
    Quale versione di Python pensi che stia girando in questo ambiente Skulpt?
    Fai la tua previsione — poi eseguilo!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `import sys

print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Default encoding:", sys.getdefaultencoding())`);
</script>

## Il Percorso di Ricerca dei Moduli di Python

Quando fai `import` di un modulo, Python deve sapere dove cercarlo. Controlla una lista di cartelle chiamata il **percorso di ricerca dei moduli**, memorizzata in `sys.path`.

```python
import sys

for i, folder in enumerate(sys.path, 1):
    print(i, folder)
```

Python controlla queste cartelle **in ordine** e usa il primo modulo corrispondente che trova. È per questo che due moduli diversi con lo stesso nome, che stanno in due cartelle diverse, possono causare bug confusi — Python vede sempre solo il primo.

## Affrontare gli Ambienti Python

Se hai lottato con installazioni, versioni di pacchetti in conflitto, o bug del tipo "funziona sul mio computer", sei in buona compagnia — anche gli sviluppatori professionisti trovano confusa la configurazione degli ambienti Python. Il webcomic XKCD ha colto perfettamente la sensazione:

![Gli ambienti Python, visti da XKCD](../../img/python_environment.png)

La comunità Python è enorme e si muove velocemente. Ognuno aggiorna le proprie librerie secondo il proprio programma, e i progetti più vecchi possono dipendere da versioni che entrano in conflitto con quelle più nuove. Alcune abitudini mantengono il caos gestibile:

1. Sapere sempre quale versione di Python stai eseguendo (`python3 --version`).
2. Usare un ambiente virtuale separato (o un ambiente `conda`) per ogni progetto.
3. Sapere come controllare `sys.path` quando un import non si comporta come ti aspetti.
4. Essere cauti con l'ambiente Python predefinito/globale del tuo computer — è spesso obsoleto.

!!! mascot-tip "Non Devi Padroneggiare Questo Oggi"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    I mal di testa da ambiente succedono a tutti — anche gli sviluppatori senior ci scherzano sopra.
    Attieniti alle abitudini sopra ed evitarai la maggior parte del dolore.

## Il Gestore di Pacchetti Conda

**Conda** (da Anaconda) è un gestore di pacchetti alternativo popolare nella data science.
Gestisce sia i pacchetti Python sia le dipendenze non-Python (come le librerie C di cui ha bisogno NumPy).

```bash
conda create -n myenv python=3.11
conda activate myenv
conda install numpy pandas matplotlib
```

Anaconda (la distribuzione completa) include Python, conda, Jupyter, e più di 200 pacchetti di data science pre-installati.

## La Piattaforma Python per Raspberry Pi

Il **Raspberry Pi** è un piccolo computer economico (circa delle dimensioni di una carta di credito) che esegue Python completo.
È popolare per i progetti hardware — controllare LED, leggere sensori, costruire robot.

Python viene pre-installato su Raspberry Pi OS.
Librerie come `RPi.GPIO` permettono ai programmi Python di controllare i pin fisici.

```python
import RPi.GPIO as GPIO
GPIO.setup(17, GPIO.OUT)   # set pin 17 as output
GPIO.output(17, True)      # turn on an LED
```

## Scegliere lo Strumento Giusto

| Situazione | Strumento raccomandato |
|-----------|-----------------|
| Sto solo imparando Python | Skulpt (questo corso) o Thonny |
| Condividere codice online | Repl.it o Google Colab |
| Progetti professionali | VS Code |
| Gestione veloce di pacchetti e progetti | uv |
| Data science / ML | Jupyter Notebook o JupyterLab |
| Progetti hardware | Raspberry Pi + Thonny |
| Calcolo scientifico | Spyder + Anaconda |

!!! mascot-tip "Inizia Semplice"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Non devi scegliere subito lo strumento "perfetto".
    Thonny è un ottimo primo passo dopo Skulpt — è gratuito, gira offline, e ti mostra esattamente cosa fa Python.
    Una volta che superi Thonny, VS Code è il naturale passo successivo per la maggior parte dei programmatori.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Abbina lo Strumento"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Leggi ogni scenario sotto e decidi quale strumento si adatta meglio.
    Scrivi le tue risposte — non c'è codice da eseguire, solo ragionamento da fare!

Usa questa finestra Skulpt per registrare le tue risposte:

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `# Scenario → Best tool
# 1. A student wants to learn Python without installing anything on the school computer.
#    Answer:

# 2. A data scientist needs to share analysis with charts and explanation in one document.
#    Answer:

# 3. A developer is building a Flask web app with multiple Python files and a database.
#    Answer:

# 4. A maker wants to control LEDs and sensors with Python on cheap hardware.
#    Answer:

# 5. A team wants one fast tool to create environments, add packages, and lock versions.
#    Answer:

# 6. Profiling shows that one image-processing loop uses nearly all the running time.
#    Should the team keep all the code in Python, or test a Rust version of that loop?
#    Answer:

print("Scenarios answered above!")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Nel laboratorio di informazioni di sys, stampa anche `sys.executable` per vedere il percorso completo dell'interprete Python.
   **Saprai che ha funzionato quando** vedi un percorso che finisce con `python` o `python3`.

2. Usa `sys.getsizeof([])` e `sys.getsizeof([1,2,3])` per confrontare le dimensioni di memoria delle liste.
   **Saprai che ha funzionato quando** vedi che la lista con 3 elementi occupa più byte.

3. Prova `sys.maxsize` — l'intero massimo che Python può memorizzare in modo efficiente.
   **Saprai che ha funzionato quando** vedi un numero molto grande (9.223.372.036.854.775.807 su sistemi a 64 bit).

4. Confronta `pip show numpy` con `uv pip show numpy` in un vero terminale. Scrivi un commento
   che spiega cosa mostrano entrambi i comandi.
   **Saprai che ha funzionato quando** il tuo commento descrive la versione del pacchetto, l'autore, e la posizione di installazione.

5. Scrivi un blocco di commenti elencando tre pacchetti da PyPI che vorresti esplorare in seguito e perché.
   **Saprai che ha funzionato quando** hai una mini "lista dei desideri" per il tuo percorso di apprendimento Python.

!!! mascot-celebration "Esploratore del Mondo Python!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora hai una mappa dell'intero ecosistema Python — dagli strumenti per principianti agli ambienti professionali!
    Scegliere lo strumento giusto per il lavoro è una vera competenza da sviluppatore.
    Quando sei pronto, scegli un ambiente e inizia a costruire qualcosa di vero. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
