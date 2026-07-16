# Questo è un fork in lingua italiana del bellissimo progetto Learning Python di Dan McCreary (https://github.com/dmccreary/learning-python) 

# Introduzione a Python — Dalle istruzioni di programmazione ai codici con Monty

[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/View%20on-GitHub%20Pages-blue?logo=github)](https://dmccreary.github.io/learning-python/)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-DA7857?logo=anthropic)](https://claude.ai/code)
[![Claude Skills](https://img.shields.io/badge/Uses-Claude%20Skills-DA7857?logo=anthropic)](https://github.com/dmccreary/claude-skills)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![p5.js](https://img.shields.io/badge/p5.js-ED225D?logo=p5.js&logoColor=white)](https://p5js.org/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Visualizza il sito web in tempo reale

Leggi il libro su: **[https://dmccreary.github.io/learning-python/](https://dmccreary.github.io/learning-python/)**

## Descrizione

**Introduzione a Python — Dalle istruzioni di programmazione ai codici con Monty** è un libro di testo interattivo e intelligente, creato da AI, per studenti di età compresa tra 10 e 13 anni che desiderano passare da programmazioni basate su blocchi (come Scratch) a programmazioni reali in Python.

Ogni lezione è basata su programmazione interattiva, realizzata con **Skulpt**, una implementazione di Python in JavaScript. Gli studenti possono leggere un breve programma, cliccare su **Run** per vedere come esegue immediatamente (senza bisogno di installazione o account), e poi modificarlo: cambiare il colore, il numero, la direzione… e ripetere l’esecuzione. La grafica astratta fornita da Skulpt offre un feedback visivo immediato: gli studenti vedono immediatamente quali forme, spirali e pattern appaiono non appena il codice viene eseguito. Prima di ogni esercizio, una simpatica mascotte chiamata Monty chiede agli studenti di *prevedere* cosa farà il codice prima di cliccare su “Run”… Questo metodo favorisce lo sviluppo delle capacità di ragionamento, non solo di una semplice abitudine di copiare e eseguire.

Il libro copre 38 capitoli che trattano 450 concetti, verificati attraverso un grafico della dipendenza dei concetti, in modo che ogni idea si basi su quella precedente. Il contenuto, i quiz, le voci del glossario e i MicroSims vengono generati e curati utilizzando le competenze di Claude AI, rendendo questo un libro di testo intelligente di livello 2+ con elementi interattivi e pratici in tutto il libro.

## Stato del sito e metriche

| Metric | Count |
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
git clone https://github.com/dmccreary/learning-python.git
cd learning-python
```

### Installare le dipendenze

Questo progetto utilizza MkDocs con lo stile Material:

```bash
pip install mkdocs
pip install mkdocs-material
```

### Creare e servire localmente

Servire localmente per lo sviluppo (con ricarica in tempo reale):

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

Questo crea il sito e lo spinge sulla branch `gh-pages`.

### Utilizzare il libro

- Utilizzare la barra laterale a sinistra per navigare tra i capitoli, o il pulsante di ricerca per cercare tutto il contenuto.
- Ogni capitolo include uno o più laboratori interattivi — leggere il codice, prevedere cosa farà, cliccare su **Eseguire**, poi modificarlo ed eseguirlo di nuovo.
- Ogni capitolo termina con un quiz e una lista di riferimenti annotati.
- Esplorare la [Galleria grafica a teste](docs/turtle-graphics-gallery) e [MicroSims](docs/sims) per esempi interattivi autonomi.

## Struttura del repository

```
learning-python/
├── docs/                          # MkDocs documentation source
│   ├── chapters/                  # 38 chapters, each with content, quiz, references
│   │   ├── 01-welcome-to-python/
│   │   │   ├── index.md          # Chapter content with Skulpt labs
│   │   │   ├── quiz.md           # Chapter quiz
│   │   │   └── references.md     # Annotated references
│   │   └── ...
│   ├── sims/                      # Interactive p5.js and Skulpt MicroSims
│   ├── turtle-graphics-gallery/   # Turtle graphics example gallery
│   ├── learning-graph/            # Concept dependency graph and book metrics
│   ├── js/                        # Skulpt/CodeMirror lab runtime
│   ├── glossary.md                # ISO 11179-compliant term definitions
│   ├── faq.md                     # Frequently asked questions
│   └── license.md                 # License details
├── mkdocs.yml                     # MkDocs configuration
└── README.md                      # This file
```

## Segnalare problemi

Ha trovato un bug, un errore di battitura, o ha una suggerimento per miglioramenti? Si prega di segnalarlo:

[Issues su GitHub](https://github.com/dmccreary/learning-python/issues)

Quando segnalate problemi, si prega di includere una descrizione del problema, passaggi per riprodurre il problema (per i bug) e screenshot, se disponibili.

## Licenza

Questo lavoro è licenziato sotto la [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**È libero di:**

- **Condividere** — copiare e distribuire il materiale
- **Adattare** — rimixare, trasformare e sviluppare sul materiale

**Sotto i seguenti termini:**

- **Attribuzione** — Dare il dovuto credito con un link all'originale
- **Non Commerciale** — Nessun uso commerciale senza permesso
- **ShareAlike** — Distribuire i contributi sotto la stessa licenza

Per maggiori dettagli, comprese le richieste di licenza commerciale, si veda [docs/license.md](docs/license.md).

## Ringraziamenti

Questo progetto si basa sui contributi dei grandi esperti della comunità open source:

- **[MkDocs](https://www.mkdocs.org/)** — Generatore di siti statici ottimizzato per la documentazione dei progetti
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — Theme bello e reattivo per la documentazione
- **[Skulpt](https://skulpt.org/)** — Implementazione Python in browser che alimenta ogni laboratorio di programmazione
- **[p5.js](https://p5js.org/)** — Biblioteca di programmazione creativa dell'ITP della NYU, utilizzata in diversi progetti MicroSims
- **[Claude AI](https://claude.ai)** di Anthropic — Generazione di contenuti assistita da intelligenza artificiale
- **[GitHub Pages](https://pages.github.com/)** — Hosting gratuito per progetti open source

## Contatti

**Dan McCreary**

- LinkedIn: [linkedin.com/in/danmccreary](https://www.linkedin.com/in/danmccreary/)
- GitHub: [@dmccreary](https://github.com/dmccreary)

Domande, suggerimenti o opportunità di collaborazione? Non esitate a contattarmi su LinkedIn o a creare un issue su GitHub.
