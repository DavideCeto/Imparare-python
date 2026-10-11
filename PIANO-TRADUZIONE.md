# Piano di traduzione — Imparare Python (IT)

Traduzione italiana di [learning-python](https://github.com/dmccreary/learning-python) di Dan McCreary.
Questo documento è la guida di riferimento per procedere, un passo alla volta, alla
traduzione completa del progetto. Non è un documento "a sola lettura": va aggiornato
man mano che lo stato avanza.

## 0. Stato attuale (2026-10-03)

Già tradotti (modifiche presenti nel working tree, non ancora committate):

- `CLAUDE.md`, `README.md`, `CONTENT-GENERATION-GUIDELINES.md`
- `docs/about.md`, `docs/contact.md`, `docs/course-description.md`, `docs/faq.md`
- `docs/index.md`, `docs/references.md`, `docs/license.md`, `docs/running-python.md`
- `mkdocs.yml` (etichette nav per le sezioni già tradotte: Home, Capitoli 1–38,
  Laboratori Python, Glossario/FAQ/Riferimenti/Licenza/Contatti)
- `docs/chapters/01-welcome-to-python/` (index, references, quiz)
- `docs/chapters/02-python-code-structure/` (index, references, quiz)
- `docs/chapters/03-variables-and-numbers/` (index, references, quiz)
- `docs/chapters/04-functions-and-objects/` (index, references, quiz)
- `docs/chapters/05-drawing-with-turtle/` (index, references, quiz — corretto anche un
  bug pre-esistente nel `quiz.md` inglese: una riga duplicata con un tag
  `<parameter name="content">` incollato per errore prima della domanda 7)
- `docs/chapters/06-math-and-arithmetic/` (index, references, quiz)
- `docs/chapters/07-for-loops-and-shapes/` (index, references, quiz)
- `docs/chapters/08-working-with-strings/` (index, references, quiz)
- `docs/chapters/09-decisions-if-else/` (index, references, quiz)
- `docs/chapters/10-while-loops-and-animation/` (index, references, quiz)
- `docs/chapters/11-functions-parameters-scope/` (index, references, quiz — questo capitolo
  nell'originale inglese non ha le sezioni "Summary"/"Concepts Covered"/"Prerequisites", a
  differenza dei Capitoli 1-10; la traduzione rispecchia questa differenza di struttura)
- `docs/chapters/12-colors-fill-turtle-art/` (index, references, quiz — i nomi dei colori nella
  tabella RGB e nelle risposte del quiz sono stati tradotti perché sono prosa descrittiva, non
  identificatori di codice; i termini Hue/Saturation/Lightness sono stati tradotti con
  l'originale inglese tra parentesi alla prima occorrenza)
- `docs/chapters/13-user-input-type-conversion/` (index, references, quiz)
- `docs/chapters/14-string-methods-formatting/` (index, references, quiz)
- `docs/chapters/15-lists-basics/` (index, references, quiz — titolo allineato alla nav di
  `mkdocs.yml` già tradotta in precedenza: "Liste — Nozioni di Base", non "Le Basi")
- `docs/chapters/16-lists-methods-patterns/` (index, references, quiz — titolo allineato alla
  nav: "Liste — Metodi e Pattern")
- `docs/chapters/17-modules-and-random/` (index, references, quiz — titolo allineato alla
  nav: "Moduli e Numeri Casuali")
- `docs/chapters/18-math-module-turtle-projects/` (index, references, quiz — titolo allineato
  alla nav: "Modulo math e Progetti con la Turtle")
- `docs/chapters/19-booleans-and-conditionals/` (index, references, quiz — titolo allineato
  alla nav: "Altri Booleani e Condizionali"; chiude i Capitoli 1-18 = Fase Skulpt/turtle)
- `docs/chapters/20-tuples-and-sets/` (index, references, quiz — titolo allineato alla nav:
  "Tuple e Insiemi")
- `docs/chapters/21-dictionaries/` (index, references, quiz — titolo allineato alla nav:
  "Dizionari")
- `docs/chapters/22-advanced-collections/` (index, references, quiz — titolo allineato alla
  nav: "Collezioni Avanzate e Funzioni Built-in")
- `docs/chapters/23-error-handling-debugging/` (index, references, quiz — titolo allineato
  alla nav: "Gestione degli Errori e Debugging"; questo `references.md` ha anche un link
  finale "[See Chapter Content](./index.md)" che gli altri capitoli non hanno — tradotto)
- `docs/chapters/24-recursion-and-fractals/` (index, references, quiz — titolo allineato
  alla nav: "Ricorsione e Frattali")
- `docs/chapters/25-object-oriented-programming/` (index, references, quiz — titolo
  allineato alla nav: "Programmazione Orientata agli Oggetti")
- `docs/chapters/26-file-input-output/` (index, references, quiz — titolo allineato alla
  nav: "Input e Output su File")
- `docs/chapters/27-standard-library-json/` (index, references, quiz — titolo allineato
  alla nav: "Libreria Standard e JSON")
- `docs/chapters/28-python-dev-tools/` (index, references, quiz — titolo allineato alla
  nav: "Strumenti di Sviluppo Python"; alt-text dell'immagine XKCD tradotto)
- `docs/chapters/29-text-processing-regex/` (index, references, quiz — titolo allineato
  alla nav: "Elaborazione del Testo ed Espressioni Regolari")
- `docs/chapters/30-algorithms-data-structures/` (index, references, quiz — titolo
  allineato alla nav: "Algoritmi e Strutture Dati")
- `docs/chapters/31-advanced-functions-oop/` (index, references, quiz — titolo allineato
  alla nav: "Funzioni Avanzate e OOP")
- `docs/chapters/32-data-visualization-matplotlib/` (index, references, quiz — titolo
  allineato alla nav: "Visualizzazione Dati con matplotlib")
- `docs/chapters/33-numpy-scientific-computing/` (index, references, quiz — titolo
  allineato alla nav: "NumPy e Calcolo Scientifico")
- `docs/chapters/34-image-processing-pillow/` (index, references, quiz — titolo allineato
  alla nav: "Elaborazione delle Immagini con Pillow")
- `docs/glossary.md` (tutte le 338 voci, intestazioni `####` verificate 338/338 rispetto
  all'originale)

Verificato: i file skill (`skills/python-lab-generator/SKILL.md` e
`skills/python-lab-generator/references/content-rules.md`) risultano intatti
(nessuna modifica rispetto a `main`), quindi il problema dei placeholder rotti
segnalato in una versione precedente di questo piano non è più presente.

## 1. Cosa tradurre e cosa NON tradurre (regole semantiche)

Questa è la parte più delicata: una traduzione "alla lettera" romperebbe il codice e
i meccanismi del sito. Regole fisse per ogni file:

### NON tradurre mai

- **Parole chiave e sintassi Python**: `print`, `import`, `def`, `for`, `while`, `if`,
  `elif`, `else`, `True`, `False`, `None`, `return`, `class`, ecc.
- **Nomi di funzioni/metodi di libreria**: `forward()`, `right()`, `turtle.Turtle()`,
  `begin_fill()`, `range()`, `input()`, `type()`, nomi di variabili nel codice (`t`, `i`, `x`…).
- **Blocchi di codice** (` ```python ... ``` `) e **codice inline** (`` `come questo` ``) —
  contenuto eseguibile, va lasciato intatto carattere per carattere.
- **Percorsi, URL, link relativi, nomi di file/cartelle** (es. `../../img/mascot/welcome.png`,
  `./quiz.md`) — solo il *testo del link* si traduce, mai il target.
- **Nomi propri e di prodotto**: Monty, Skulpt, CodeMirror, Python, Thonny, GitHub, Jupyter,
  Docker, NumPy, Pillow, ecc.
- **Il "tipo" degli admonition** di MkDocs Material: `!!! mascot-welcome`, `!!! mascot-tip`,
  `!!! mascot-warning`, `!!! mascot-thinking`, `!!! mascot-celebration`, `!!! Note` — la parola
  chiave dopo `!!!` è legata al CSS/plugin e deve restare invariata. Il *titolo tra virgolette*
  e il corpo del blocco invece si traducono.
- **Chiavi del front matter YAML** (`title:`, `description:`, `generated_by:`, `date:`,
  `version:`) — le chiavi restano in inglese; il *valore* di `title` e `description` si traduce,
  `generated_by`/`date`/`version` restano invariati (sono metadati di generazione).
- **HTML/JS incorporato** (tag `<script>`, `<div class="cm-lab">`, attributi `onclick`,
  id come `cm-editor-2`) — è infrastruttura della pagina, non prosa.

### Tradurre sempre

- Tutta la prosa: riepiloghi di capitolo, spiegazioni, titoli di sezione, testo dei dialoghi
  di Monty, didascalie, domande di previsione, celebrazioni.
- Il testo delle tabelle (tranne nomi di comandi/funzioni che restano in inglese).
- Domande e risposte dei quiz.
- Le *definizioni* nel glossario (il termine tecnico Python resta in inglese nell'intestazione,
  la spiegazione si traduce — es. `abs() — valore assoluto`).

### Zone grigie da decidere prima di partire (vedi sezione 2)

- I **titoli dei 450 concetti** della learning graph (es. "Python Interpreter Overview")
  compaiono sia nei capitoli (lista "Concepts Covered") sia nei file sorgente
  `docs/learning-graph/concept-list*.md` che fanno da fonte di verità per lo strumento di
  verifica delle dipendenze. Tradurli ovunque rischia di rompere il matching automatico
  tra capitoli e grafo dei concetti.
- Il testo dei **pulsanti dell'interfaccia** (`▶ Run`, `↺ Reset`) è stampato dallo stesso
  template in centinaia di pagine (lab generator / `js/codemirror-lab.js`). Tradurlo pagina
  per pagina sarebbe enormemente ridondante: va deciso se cambiarlo **una sola volta** a
  livello di template/JS condiviso, oppure lasciarlo in inglese come "linguaggio universale
  dei bottoni" (scelta comune nei siti didattici bilingue).
- Il testo nelle **MicroSims** (le app HTML/JS in `docs/sims/*/main.html`) è codice
  applicativo, non Markdown: tradurlo è un progetto a parte, molto più grande (bisogna
  toccare JS), separato dalla traduzione delle pagine `index.md` che le descrivono.
- Le **etichette della sidebar** in `mkdocs.yml` (nav) sono in inglese: senza tradurle,
  un lettore italiano vedrebbe un menu laterale inglese anche a traduzione dei contenuti
  completata.

## 2. Decisioni prese con l'utente (2026-10-03)

1. **Concetti della learning graph**: si traduce il testo visibile nei capitoli, ma gli
   ID/slug usati dai tool di verifica delle dipendenze restano invariati.
2. **Pulsanti Run/Reset** e altra "UI chrome" dei lab: restano in inglese (linguaggio
   universale dei bottoni); non si tocca il template/JS condiviso in questa fase.
3. **MicroSims**: si traducono solo le pagine `index.md` descrittive; il codice JS
   applicativo resta in inglese e fuori scope per ora.
4. **Nav di `mkdocs.yml`**: si traducono le etichette visibili nella sidebar, mantenendo
   invariati i percorsi dei file. Fatto per le sezioni già coperte dalla Fase 1/2/3
   (Home, pagine di ingresso, tutti i 38 capitoli, Laboratori Python, Glossario/FAQ/
   Riferimenti/Licenza/Contatti). Le etichette delle sezioni non ancora tradotte
   (Turtle Graphics Gallery, Jupyter Notebooks, Advanced Python Examples, Trinket Labs,
   Learning Graph, MicroSims, Teacher's Guide) restano in inglese e si traducono insieme
   al contenuto quando si arriva alla rispettiva fase (3–8), per evitare di disallinearle
   dai titoli reali delle pagine.
5. Metodo di traduzione per il grosso del contenuto: traduzione assistita (Claude, paragrafo
   per paragrafo, con revisione terminologica) vs. script locale `traduci_textbook.py`
   (veloce ma — visto il bug sui placeholder — da **non** fidarsi ciecamente senza revisione).
   Si procede con Claude per i capitoli (contenuto pedagogico ad alto valore, Fase 2)
   e si riserva lo script, se non altro corretto, solo a contenuti ripetitivi a bassa priorità
   (es. Turtle Graphics Gallery, Fase 4).

## 3. Fasi di lavoro (ordine consigliato)

| Fase | Contenuto | File | Priorità |
|---|---|---|---|
| 0 | Housekeeping: ripristinare i file skill rotti, fissare le decisioni (sez. 2), creare un mini-glossario di coerenza terminologica | 2 | Bloccante |
| 1 | Pagine di ingresso al sito: `docs/index.md`, `glossary.md`, `references.md`, `license.md`, `running-python.md`, nav di `mkdocs.yml` | ~6 | Alta |
| 2 | **38 capitoli** (`index.md` + `references.md` + `quiz.md` per capitolo) — il cuore didattico del libro | 115 | Alta |
| 3 | Python Labs (`docs/python-labs/`) | 19 | Alta |
| 4 | Turtle Graphics Gallery (`docs/turtle-graphics-gallery/`) — struttura molto ripetitiva, buon candidato per traduzione semi-automatica con QA | 102 | Media |
| 5 | MicroSims — solo le pagine `index.md` descrittive, non il codice JS dell'app | 33 | Media |
| 6 | Teacher's Guide + prompt di esempio | 14 | Bassa |
| 7 | Jupyter notebooks docs, Advanced/Advanced-python | 11 | Bassa |
| 8 | Learning Graph (report tecnici per chi mantiene il libro) | 11 | Bassa |
| 9 | Trinket Labs — segnato come **deprecated** nella nav originale | 23 | Minima / valutare se tradurre affatto |

Totale righe editoriali vere e proprie (fasi 1–8, escluso Trinket deprecato): ~316 file.

## 4. Flusso di lavoro per ogni batch di file

1. Tradurre un gruppo coerente (es. un capitolo completo: `index.md` + `references.md` + `quiz.md`).
2. Verificare a mano: nessun codice toccato, link/percorsi intatti, tipo di admonition invariato.
3. Chiedere all'utente di far girare `mkdocs serve` (non lo avviamo noi, vedi `CLAUDE.md`) per
   un controllo visivo del rendering.
4. Commit per singolo batch con messaggio chiaro (non un unico mega-commit finale) — più
   facile da revisionare e, se serve, da annullare.
5. Aggiornare lo stato di avanzamento (proposta: una tabella di tracking, es. estendendo
   `book-status.json` o un file parallelo `translation-status.json`, capitolo per capitolo).

## 5. Prossimo passo concreto

Fase 0 chiusa: i file skill (`skills/python-lab-generator/SKILL.md` e
`references/content-rules.md`) risultano intatti (nessuna modifica rispetto a `main`),
quindi non serve alcun ripristino. Decisioni della sezione 2 fissate il 2026-10-03.

Fase 1 completata (pagine di ingresso, `docs/glossary.md`, nav di `mkdocs.yml` per le
sezioni coperte). Fase 2 in corso: Capitoli 1-34 tradotti.

Prossimo: continuare la Fase 2 dal Capitolo 35 (`docs/chapters/35-advanced-turtle-event-driven/`),
un capitolo alla volta (`index.md` + `references.md` + `quiz.md`). La nav di `mkdocs.yml`
per tutti i 38 capitoli è già tradotta dalla Fase 1 — controllare sempre l'etichetta nav
esistente e allineare il titolo H1/front matter a quella (vedi nota sui Capitoli 15-34),
invece di tradurre il titolo da zero. Nota di qualità: nel Capitolo 34 un errore di
battitura ha temporaneamente corrotto il percorso di un'immagine mascotte
(`thinking.png` → `thinking.img-admonition`) prima della verifica — controllare sempre
con `grep '!\[.*\]('` che tutti i percorsi immagine restino intatti dopo la traduzione.

Nota di qualità: durante la traduzione del Capitolo 5 è stato trovato e corretto un
bug pre-esistente nell'originale inglese `docs/chapters/05-drawing-with-turtle/quiz.md`
(riga duplicata con un tag placeholder incollato per errore prima della domanda 7).
Il bug esiste ancora nella versione inglese — da segnalare/correggere separatamente
se si vuole tenere i due testi allineati.
