# Aggiungere Laboratori Python Personalizzati al Manuale

Questa guida spiega come aggiungere nuovi laboratori Python interattivi al
manuale, quali strumenti sono disponibili per generarli, e come scegliere
l'ambiente di esecuzione giusto per i tuoi studenti.

---

## Due Skill per Generare Laboratori

Questo manuale usa le skill di Claude Code per generare pagine di
laboratorio coerenti e ben strutturate. Sono disponibili due skill:

### La Skill del Laboratorio Skulpt

La skill `chapter-content-generator` (e la più ampia pipeline di contenuti
del manuale) genera laboratori usando **Skulpt** — un interprete Python
compilato in JavaScript che viene eseguito interamente dentro il browser
web dello studente.

- Nessuna installazione richiesta sulle macchine degli studenti
- Funziona su Chromebook, tablet e computer scolastici bloccati
- I laboratori fanno parte del manuale pubblicato e possono essere
  condivisi con qualsiasi insegnante che abbia l'URL
- La grafica turtle si rende in linea accanto all'editor di codice
- Completamente offline una volta caricata la pagina (nessun server,
  nessun account)

### La Skill del Laboratorio Python Docker

La skill `docker-python-lab` genera laboratori che eseguono vero codice
Python dentro un container Docker isolato sulla macchina locale
dell'insegnante o dello studente.

Per richiamarla, digita:

```
/docker-python-lab
```

Claude genererà il blocco HTML del laboratorio, verificherà che i file CSS
e JavaScript condivisi esistano, e verificherà che `mkdocs.yml` sia
collegato correttamente. Lo studente clicca **Run** nel browser, il codice
viaggia verso un servizio locale sulla porta 5001, viene eseguito in un
container nuovo, e l'output torna in circa 300 millisecondi (dopo la prima
esecuzione a freddo).

---

## Fortemente Raccomandato: Mantieni le Cose Semplici con Skulpt

Prima di ricorrere a Docker o a un'installazione Python locale, considera i
vantaggi di restare con Skulpt per i capitoli 1–18:

**I laboratori Skulpt viaggiano con il manuale.**
Un laboratorio Skulpt è solo una `<textarea>` e un po' di HTML in un file
Markdown. Vive nel repository GitHub insieme al testo della lezione.
Quando condividi un link a una pagina, il laboratorio viene con essa —
nessuna configurazione, nessun numero di porta, nessun "assicurati che il
servizio sia in esecuzione".

**Ogni studente ha lo stesso ambiente.**
Non c'è incompatibilità di versione, nessuna libreria mancante, nessun
momento "funziona sulla mia macchina". Skulpt esegue sempre Python 3 con il
modulo turtle standard, in modo identico su ogni dispositivo.

**Skulpt rimuove la barriera d'ingresso più grande.**
Per studenti di 10-14 anni che provano Python per la prima volta, il
carico cognitivo di installare software, gestire ambienti e risolvere
problemi di PATH è enorme. Skulpt permette loro di scrivere ed eseguire
codice nella stessa sessione in cui imparano cos'è una variabile.

**I laboratori Skulpt possono essere contribuiti indietro.**
Poiché sono semplici file Markdown, qualsiasi insegnante può inviare una
pull request per aggiungere un nuovo laboratorio Skulpt al repository
condiviso del manuale. Un laboratorio Docker richiede che anche
l'insegnante ricevente esegua il servizio locale, il che rompe il flusso
di lavoro "apri il link e insegna".

**Quando Skulpt non basta**, le nove opzioni qui sotto descrivono
alternative progressivamente più potenti (e più complesse).

---

## Nove Opzioni per Eseguire Python

Usa questa tabella per abbinare l'ambiente di esecuzione giusto al tuo
contesto didattico:

| # | Opzione | Ideale per | Complessità |
|---|--------|----------|------------|
| 1 | **Skulpt (nel browser)** | Tutti i principianti, laboratori condivisi del manuale | Nessuna |
| 2 | **Installazione Python locale** | Studenti con il proprio computer | Bassa |
| 3 | **Ambiente virtuale Python (venv)** | Progetti intermedi con dipendenze | Media |
| 4 | **Ambiente virtuale Conda** | Data science, ML, calcolo scientifico | Media |
| 5 | **Container Docker** | Ambienti riproducibili, codice lato server | Alta |
| 6 | **IDE Thonny** | Nuovi studenti che passano allo sviluppo locale | Bassa |
| 7 | **VS Code** | Studenti pronti per strumenti professionali | Media |
| 8 | **Jupyter Notebook / Lab** | Data science, visualizzazione, codice narrativo | Media |
| 9 | **Un altro IDE** | Qualsiasi altro editor o ambiente | Variabile |

---

### Opzione 1 — Skulpt (Python nel Browser)

**Cos'è:** Python compilato in JavaScript, eseguito interamente nel browser
senza server né installazione.

**Quando usarla:** Per insegnare i capitoli 1–18 di questo manuale, per
gestire un coding club su Chromebook o dispositivi gestiti dalla scuola,
per condividere laboratori con altri insegnanti, o per dimostrare Python a
un gruppo dove non puoi controllare ogni macchina.

**Come aggiungere un laboratorio:** Usa la skill `chapter-content-generator`
o scrivi direttamente il blocco HTML di Skulpt. Vedi i laboratori esistenti
in `docs/chapters/` per il formato esatto.

**Limitazioni:** Nessun I/O su file, nessun pacchetto di terze parti
(`numpy`, `pandas`, `requests`, ecc.), nessun `input()` da terminale. La
grafica turtle e le operazioni di base su matematica/stringhe/liste
funzionano perfettamente.

---

### Opzione 2 — Installazione Python Locale (Python di Sistema)

**Cos'è:** Python installato direttamente sul sistema operativo dello
studente, eseguito da un terminale con `python3 script.py`.

**Quando usarla:** Quando gli studenti hanno laptop personali e sono pronti
ad andare oltre Skulpt. Vedi `docs/chapters/28-python-dev-tools/index.md`
per la guida all'installazione e all'ambiente già presente in questo
manuale.

**Come aggiungere un laboratorio:** Scrivi un blocco di codice statico
(```` ```python ````) nella pagina Markdown. Gli studenti copiano il codice
in un file locale e lo eseguono nel loro terminale.

**Limitazioni:** La versione di Python, la configurazione del PATH e i
pacchetti installati variano da macchina a macchina. Aspettati di passare
10–20 minuti a risolvere problemi per studente nel giorno della
configurazione. Il fumetto [XKCD "Python environments"](https://www.explainxkcd.com/wiki/index.php/1987:_Python_Environment)
nella pagina sull'installazione di Python non è del tutto uno scherzo.

---

### Opzione 3 — Ambiente Virtuale Python (`venv`)

**Cos'è:** Un ambiente Python leggero e isolato creato con
`python3 -m venv` che mantiene separati i pacchetti di ogni progetto.

**Quando usarla:** Quando un progetto richiede versioni specifiche di
pacchetti (es. `matplotlib 3.8`) senza influenzare il Python di sistema o
altri progetti.

**Avvio rapido:**
```sh
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
pip install matplotlib pandas
```

**Quando usarla:** Studenti intermedi che iniziano a installare librerie di
terze parti. Insegna `venv` prima di `pip install` così gli studenti
sviluppano fin dall'inizio l'abitudine di isolare le dipendenze.

**Limitazioni:** Gli studenti devono ricordarsi di attivare l'ambiente in
ogni nuova sessione del terminale. Dimenticarlo è la causa numero 1 dei bug
"funzionava ieri".

---

### Opzione 4 — Ambiente Virtuale Conda (Preferito per la Data Science)

**Cos'è:** Il gestore di ambienti di Anaconda o Miniconda, che gestisce sia
le versioni di Python che i pacchetti binari compilati (NumPy, SciPy,
PyTorch, ecc.) in un unico strumento.

**Quando usarlo:** Per insegnare data science, machine learning,
elaborazione delle immagini, o qualsiasi argomento che richieda librerie di
calcolo scientifico. Conda risolve dipendenze binarie che `pip` a volte non
riesce a risolvere.

**Avvio rapido:**
```sh
conda create -n coderdojo python=3.11
conda activate coderdojo
conda install numpy matplotlib scikit-learn
```

**Perché è preferito per la data science:** `pip install numpy` può
fallire su Windows o Apple Silicon se manca la toolchain del compilatore
C. `conda install numpy` fornisce sempre un binario pre-compilato che
funziona e basta.

**Limitazioni:** Miniconda è un download di ~60 MB. Il comando `conda` è
più lento di `pip`. Gli studenti a volte confondono `conda activate` con
il Python di sistema.

---

### Opzione 5 — Container Docker

**Cos'è:** Python eseguito dentro un container isolato tramite
`scripts/run-python-docker.sh`. Gli studenti modificano il codice nel
browser e cliccano **Run**; il codice viene eseguito in un container nuovo
e l'output torna in ~300 ms (dopo la prima esecuzione a freddo di ~5
secondi).

**Quando usarlo:** Quando vuoi un ambiente riproducibile e isolato per
studenti intermedi o avanzati senza chiedere loro di installare Python o
gestire ambienti. Utile anche per argomenti dove vuoi dimostrare che lo
stesso codice viene eseguito in modo identico per ogni studente
indipendentemente dal loro sistema operativo.

**Come aggiungere un laboratorio:** Usa la skill `/docker-python-lab`. La
skill genera il blocco HTML del laboratorio, crea i file CSS e JavaScript
condivisi se non esistono, e controlla `mkdocs.yml`.

**Limitazioni:** Richiede Docker Desktop installato e in esecuzione sulla
macchina locale (o sulla macchina dell'insegnante se in proiezione). Il
servizio (`run-python-docker.sh`) deve essere in esecuzione in un
terminale separato mentre gli studenti usano la pagina. Nessuna grafica
turtle. Nessun `input()`. I pacchetti oltre la libreria standard di Python
richiedono un'immagine Docker personalizzata.

**Condivisibilità:** I laboratori Docker nel manuale pubblicato
funzionano solo per i lettori che hanno il servizio in esecuzione
localmente — altrimenti vedranno "Cannot connect to the Python Docker
service". Questa è la ragione principale per cui Skulpt è preferito per i
contenuti condivisi del manuale.

---

### Opzione 6 — IDE Thonny (Preferito per i Nuovi Studenti che Passano a Python Locale)

**Cos'è:** Un IDE Python gratuito e adatto ai principianti, progettato
specificamente per l'apprendimento. Ha un interprete Python integrato, un
debugger passo-passo che evidenzia ogni riga mentre viene eseguita, e un
ispettore di variabili che mostra il valore attuale di ogni variabile.

**Download:** [thonny.org](https://thonny.org) — funziona su Windows,
macOS e Linux, incluso Raspberry Pi OS (pre-installato).

**Quando usarlo:** Quando gli studenti sono pronti a lasciare Skulpt e a
scrivere Python sul proprio computer per la prima volta. Il debugger di
Thonny è impareggiabile per costruire modelli mentali di come funzionano
cicli e funzioni.

**Perché è preferito a VS Code per i principianti:** Thonny installa
Python automaticamente insieme all'IDE — nessun download separato di
Python, nessuna configurazione del PATH, nessun terminale. Uno studente
può passare da zero all'esecuzione del suo primo script in meno di cinque
minuti.

**Limitazioni:** Thonny è volutamente semplice. Non ha integrazione con
Git, estensioni, o le funzionalità di language-server su cui fanno
affidamento gli sviluppatori professionisti. Gli studenti che lo superano
migreranno naturalmente verso VS Code.

---

### Opzione 7 — VS Code

**Cos'è:** L'editor di codice gratuito e di livello professionale di
Microsoft, con una ricca estensione Python, terminale integrato, supporto
Git e integrazione con Copilot.

**Download:** [code.visualstudio.com](https://code.visualstudio.com)

**Quando usarlo:** Quando gli studenti hanno completato il curriculum
Python per principianti e sono pronti a lavorare su progetti multi-file, a
usare Git, o a prepararsi per uno stage di programmazione o una
competizione.

**Lista di controllo per la configurazione:**
1. Installa VS Code
2. Installa l'estensione **Python** (Microsoft)
3. Seleziona l'interprete Python corretto (`Ctrl+Shift+P` → "Python:
   Select Interpreter")
4. Apri il terminale integrato ed esegui `python --version` per
   verificare

**Limitazioni:** Più configurazione iniziale rispetto a Thonny. Gli
studenti che non conoscono il terminale potrebbero avere difficoltà con la
selezione dell'interprete e l'attivazione dell'ambiente virtuale dentro
VS Code.

---

### Opzione 8 — Jupyter Notebook / Lab

**Cos'è:** Un ambiente di calcolo interattivo basato sul browser dove
codice, output, visualizzazioni e testo esplicativo convivono in un unico
file *notebook* (`.ipynb`). Jupyter Notebook è l'interfaccia classica a
documento singolo; Jupyter Lab è il successore moderno multi-pannello.

**Installazione:**
```sh
pip install jupyterlab        # or: conda install jupyterlab
jupyter lab                   # opens in your default browser
```

**Quando usarlo:**
- Per insegnare data science, statistica o machine learning — i grafici
  in linea e l'esecuzione cella per cella rendono facile esplorare i dati
  passo dopo passo.
- Gli studenti devono consegnare lavori che includano sia codice *che*
  spiegazioni scritte dei risultati (comune nelle classi di scienze).
- Per dimostrare NumPy, Pandas, Matplotlib o Scikit-learn, dove vedere
  l'output subito sotto ogni cella accelera la comprensione.
- Per eseguire i capitoli avanzati di questo manuale (previsione delle
  cifre MNIST, analisi di titoli azionari) — vedi `docs/jupyter/` per i
  laboratori specifici per Jupyter già inclusi.

**Perché merita una sua opzione:** Jupyter è fondamentalmente diverso da
un IDE tradizionale. Il codice viene eseguito in *celle*, non come un
singolo script dall'inizio alla fine. Gli studenti possono rieseguire
celle singole, mantenere risultati intermedi in memoria, e mescolare
l'output di `print()` con grafici `matplotlib` in un'unica vista. Quella
interattività è un superpotere per l'esplorazione dei dati ma può
confondere gli studenti che stanno ancora imparando che i programmi
vengono eseguiti riga per riga.

**Variante Google Colab:** Se gli studenti non vogliono installare nulla,
Google Colab (`colab.research.google.com`) fornisce un ambiente Jupyter
ospitato nel cloud con accesso gratuito alla GPU — ideale per i capitoli
di ML. Richiede un account Google e una connessione internet.

**Limitazioni:** I notebook non sono ottimi per insegnare la struttura dei
programmi — gli studenti possono eseguire le celle fuori ordine e finire
con bug di stato nascosto difficili da riprodurre. Non adatto alla
grafica turtle. Non è un buon primo ambiente per principianti assoluti.

---

### Opzione 9 — Un Altro IDE

**Cos'è:** Qualsiasi altro editor — PyCharm, Spyder, Mu Editor, Replit,
ecc.

**Quando usarlo:** Quando uno strumento specifico è già in uso nella tua
scuola, o uno studente ha una forte preferenza. Il codice Python in questo
manuale è standard e viene eseguito in qualsiasi ambiente.

**Note per strumenti specifici:**

- **PyCharm** — potente IDE professionale con eccellente debugger e
  strumenti di refactoring; la Community Edition è gratuita. Più adatto a
  studenti esperti che a principianti.
- **Spyder** — un IDE Python scientifico incluso con Anaconda; layout
  simile a MATLAB con un pannello esploratore di variabili. Buono per
  studenti di data science che già usano Conda.
- **Mu Editor** — semplicità simile a Thonny; progettato per progetti
  MicroPython e Raspberry Pi. Buono per materie opzionali di
  hardware/elettronica.
- **Replit** — basato sul browser come Skulpt ma richiede un account e
  una connessione internet. Utile quando gli studenti hanno bisogno di un
  file system persistente o più pacchetti di quelli che Skulpt supporta,
  ma non hanno diritti da amministratore sulle macchine scolastiche.

---

## Guida alla Decisione

```
Il laboratorio ha bisogno della grafica turtle o viene eseguito nel manuale condiviso?
  └─ SÌ → Usa Skulpt (Opzione 1)

Il laboratorio ha bisogno di pacchetti di terze parti (numpy, matplotlib, requests)?
  ├─ Data science / ML / visualizzazione → Usa Jupyter + Conda (Opzioni 8 + 4)
  └─ Solo pacchetti generali                → Usa venv (Opzione 3)

È la prima volta che lo studente esegue Python localmente?
  └─ SÌ → Usa Thonny (Opzione 6)

Hai bisogno di una sandbox pienamente riproducibile senza configurazione per lo studente?
  └─ SÌ → Usa Docker (Opzione 5)

Lo studente sta scrivendo codice narrativo (codice + spiegazione + grafici)?
  └─ SÌ → Usa Jupyter (Opzione 8)

Lo studente è pronto per strumenti professionali / progetti multi-file?
  └─ SÌ → Usa VS Code (Opzione 7)
```

---

## Riepilogo

Per la grande maggioranza delle lezioni in questo manuale — specialmente i
capitoli 1–18 — **Skulpt è la scelta giusta**. Non richiede nulla dagli
studenti, viaggia con ogni link che condividi, e mantiene il focus
sull'imparare Python invece che sul configurare strumenti.

Riserva le opzioni più potenti alle sezioni intermedie e avanzate, dove
l'argomento stesso (I/O su file, data science, API) richiede genuinamente
un ambiente Python locale.
