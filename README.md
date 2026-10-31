# Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty

> Versione italiana del bellissimo progetto [Learning Python](https://github.com/dmccreary/learning-python) di Dan McCreary.

[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/View%20on-GitHub%20Pages-blue?logo=github)](https://davideceto.github.io/Imparare-python/)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-DA7857?logo=anthropic)](https://claude.ai/code)
[![Claude Skills](https://img.shields.io/badge/Uses-Claude%20Skills-DA7857?logo=anthropic)](https://github.com/dmccreary/ibook-skills)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![p5.js](https://img.shields.io/badge/p5.js-ED225D?logo=p5.js&logoColor=white)](https://p5js.org/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Visualizza il sito web in tempo reale

Leggi il libro in italiano su: **[https://davideceto.github.io/Imparare-python/](https://davideceto.github.io/Imparare-python/)**

La versione originale in inglese è su [dmccreary.github.io/learning-python](https://dmccreary.github.io/learning-python/).

## Descrizione

**Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty** è un libro di testo interattivo e intelligente, creato grazie all'intelligenza artificiale, per studenti di età compresa tra 10 e 14 anni che desiderano passare dalla programmazione a blocchi (come Scratch) alla vera programmazione in Python.

Ogni lezione si basa su una programmazione interattiva, realizzata con **Skulpt**, una implementazione di Python in JavaScript. Gli studenti possono leggere un breve programma, cliccare su **Run** per vedere come viene eseguito immediatamente (senza bisogno di installazione o account), e poi modificarlo: cambiare il colore, il numero, la direzione… e ripetere l’esecuzione. La grafica astratta fornita da Skulpt offre un feedback visivo immediato: gli studenti vedono immediatamente quali forme, spirali e pattern appaiono non appena il codice viene eseguito. Prima di ogni esercizio, una simpatica mascotte chiamata Monty chiede agli studenti di *prevedere* cosa farà il codice prima di cliccare su “Run”… Questo metodo favorisce lo sviluppo delle capacità di ragionamento, senza limitarsi ad un semplice copia e incolla.

Il libro copre 38 capitoli che trattano 450 concetti, verificati attraverso un grafico della dipendenza dei concetti, in modo che ogni idea si basi su quella precedente. Il contenuto, i quiz, le voci del glossario e i MicroSims vengono generati e curati utilizzando le competenze di Claude AI, rendendo questo un libro di testo intelligente di livello 2+ con elementi interattivi e pratici in tutto il libro.

## Stato del sito e metriche

| Metrica | Valore |
|--------|-------|
| Concetti nel grafico della dipendenza | 450 |
| Capitoli | 38 |
| MicroSims | 31 |
| Termini del glossario | 338 |
| Domande frequenti | 83 |
| Domande dei quiz | 380 |
| Riferimenti | 380 |
| Parole totali | 260.425 |
| Pagine equivalenti | 1.057 |

## Come iniziare

### Clonare il repository

```bash
git clone https://github.com/DavideCeto/Imparare-python.git
cd Imparare-python
```

### Installare le dipendenze

Questo progetto utilizza MkDocs con lo stile Material:

```bash
pip install mkdocs
pip install mkdocs-material
```

### Esecuzione in locale

**Esecuzione in locale (con aggiornamento in tempo reale):**

```bash
mkdocs serve
```

Poi aprire il browser su `http://localhost:8000`.

Creare il sito statico:

```bash
mkdocs build
```

### Distribuire su GitHub Pages

```bash
mkdocs gh-deploy
```

Questo crea il sito e lo pubblica sul branch `gh-pages`.

### Utilizzare il libro

- Utilizzare la barra laterale a sinistra per navigare tra i capitoli, o il pulsante di ricerca per cercare tutto il contenuto.
- Ogni capitolo include uno o più laboratori interattivi — leggere il codice, prevedere cosa farà, cliccare su **Run**, poi modificarlo ed eseguirlo di nuovo.
- Ogni capitolo termina con un quiz e una lista di riferimenti annotati.
- Esplorare la [Galleria di grafica turtle](docs/turtle-graphics-gallery) e i [MicroSims](docs/sims) per esempi interattivi autonomi.

## Struttura del repository

```
Imparare-python/
├── docs/                          # Sorgenti della documentazione MkDocs
│   ├── chapters/                  # 38 capitoli, ognuno con contenuti, quiz e riferimenti
│   │   ├── 01-welcome-to-python/
│   │   │   ├── index.md          # Contenuti del capitolo con i laboratori Skulpt
│   │   │   ├── quiz.md           # Quiz del capitolo
│   │   │   └── references.md     # Riferimenti commentati
│   │   └── ...
│   ├── sims/                      # MicroSims interattivi con p5.js e Skulpt
│   ├── turtle-graphics-gallery/   # Galleria di esempi di grafica turtle
│   ├── learning-graph/            # Grafo delle dipendenze dei concetti e metriche del libro
│   ├── js/                        # Runtime dei laboratori Skulpt/CodeMirror
│   ├── glossary.md                # Definizioni dei termini conformi a ISO 11179
│   ├── faq.md                     # Domande frequenti
│   └── license.md                 # Dettagli sulla licenza
├── mkdocs.yml                     # Configurazione di MkDocs
└── README.md                      # Questo file
```

## Segnalare problemi

Hai trovato un bug, un errore di battitura o un passaggio tradotto male, oppure hai un suggerimento? Segnalalo qui:

[Issue su GitHub](https://github.com/DavideCeto/Imparare-python/issues)

Nella segnalazione includi una descrizione del problema, i passaggi per riprodurlo (per i bug) e, se puoi, uno screenshot.

I problemi che riguardano i contenuti originali in inglese si possono segnalare anche al [progetto originale](https://github.com/dmccreary/learning-python/issues).

## Licenza

Questo lavoro è licenziato sotto la [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**Sei libero di:**

- **Condividere** — copiare e distribuire il materiale
- **Adattare** — rimixare, trasformare e sviluppare sul materiale

**Sotto i seguenti termini:**

- **Attribuzione** — Dare il dovuto credito con un link all'originale
- **Non Commerciale** — Nessun uso commerciale senza permesso
- **ShareAlike** — Distribuire i contributi sotto la stessa licenza

Per maggiori dettagli, comprese le richieste di licenza commerciale, consulta [docs/license.md](docs/license.md).

## Ringraziamenti

Questo progetto si basa sui contributi dei grandi esperti della comunità open source:

- **[MkDocs](https://www.mkdocs.org/)** — Generatore di siti statici ottimizzato per la documentazione dei progetti
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — Tema elegante e reattivo per la documentazione
- **[Skulpt](https://skulpt.org/)** — Implementazione Python in browser che alimenta ogni laboratorio di programmazione
- **[p5.js](https://p5js.org/)** — Libreria di programmazione creativa dell'ITP della NYU, utilizzata in diversi progetti MicroSims
- **[Claude AI](https://claude.ai)** di Anthropic — Generazione di contenuti assistita da intelligenza artificiale
- **[GitHub Pages](https://pages.github.com/)** — Hosting gratuito per progetti open source

## Contatti

### Progetto originale (inglese)

**Dan McCreary** — autore di [Learning Python](https://github.com/dmccreary/learning-python)

- LinkedIn: [linkedin.com/in/danmccreary](https://www.linkedin.com/in/danmccreary/)
- GitHub: [@dmccreary](https://github.com/dmccreary)

### Versione italiana

Traduzione e adattamento in italiano.

- GitHub: [@DavideCeto](https://github.com/DavideCeto)
- Segnalazioni sulla traduzione: [issue su GitHub](https://github.com/DavideCeto/Imparare-python/issues)
