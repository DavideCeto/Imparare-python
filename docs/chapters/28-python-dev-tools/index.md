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
- Installare pacchetti con `pip` e capire gli **ambienti virtuali**

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

4. Ricerca: scopri cosa fa `pip show numpy` (in un vero terminale). Scrivi un commento che lo spiega.
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
