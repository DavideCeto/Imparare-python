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
- `docs/chapters/35-advanced-turtle-event-driven/` (index, references, quiz — titolo
  allineato alla nav: "Turtle Avanzata e Programmazione Guidata da Eventi"; percorsi
  immagine verificati dopo l'incidente del Capitolo 34)
- `docs/chapters/36-computational-thinking-best-practices/` (index, references, quiz —
  titolo allineato alla nav: "Pensiero Computazionale e Buone Pratiche"; corretta
  un'inconsistenza dove "Abstraction" era rimasto non tradotto mentre gli altri tre
  pilastri del pensiero computazionale erano già in italiano)
- `docs/chapters/37-machine-learning-foundations/` (index, references, quiz — titolo
  allineato alla nav: "Fondamenti di Machine Learning"; corretti due refusi di
  coniugazione verbale introdotti durante la traduzione — "imparo"/"convertí" invece
  di "impara"/"converte" alla terza persona)
- `docs/chapters/38-neural-networks-and-mnist/` (index, references, quiz — titolo
  allineato alla nav: "Reti Neurali e MNIST"; ULTIMO capitolo — Fase 2 completa, tutti
  i 38 capitoli tradotti; "Beginning Python" lasciato non tradotto perché è il titolo
  proprio del libro originale, come già stabilito in `docs/about.md`/`docs/index.md`;
  corretti altri due refusi di coniugazione alla terza persona prima del commit)
- `docs/glossary.md` (tutte le 338 voci, intestazioni `####` verificate 338/338 rispetto
  all'originale)

**Fase 3 — Python Labs** (`docs/python-labs/`), in corso:

- `docs/python-labs/index.md` (griglia di card con titoli/descrizioni dei 17 laboratori)
- `01-turtle-commands.md`, `02-square.md`, `03-variables.md`, `04-loops.md`,
  `04a-stop-sign.md` (primo batch)
- `05-conditionals.md`, `06-functions-and-flowers.md`, `07-function-parameters.md`
  (secondo batch)
- `08-random-circles.md`, `08-color-lists.md`, `08b-random-stars.md` (terzo batch —
  corretto un refuso di coniugazione "scegle" → "sceglie" in `08b-random-stars.md`
  prima del commit)
- `10-debugging.md`, `11-user-input.md`, `12-fractal-tree.md` (quarto batch — titoli
  allineati alla nav: "Leggere gli errori", "Input dell'utente", "Albero frattale")
- `14-hex-colors.md`, `15-sine-wave.md`, `17-mouse-clicks.md` (quinto batch — titoli
  allineati alla nav: "Colori esadecimali", "Onda sinusoidale", "Click del mouse")
- `text-only-example.md` (sesto batch — pagina tecnica di riferimento per autori di
  contenuti, non è nella nav di `mkdocs.yml`; front matter `title`/`description`
  tradotti). **FASE 3 COMPLETA — tutti i 19 file di Python Labs tradotti.**

**Fase 4 — Turtle Graphics Gallery** (`docs/turtle-graphics-gallery/`, ~102 file), in corso:

- Etichette di navigazione in `mkdocs.yml` tradotte per l'intera sezione (header +
  Galleria + Idee per i Pattern + 100 titoli dei singoli pattern), in un unico passaggio,
  così i titoli dei file successivi si allineano alla nav come già fatto nelle Fasi 2-3
- `pattern-ideas.md` (catalogo delle 100 idee di pattern in 11 categorie — solo prosa,
  nessun blocco di codice; corretto un refuso "abstract" → "astratta" prima del commit)
- `index.md` (griglia di card della galleria con tutti i 100 pattern — titoli riusati
  identici a quelli già stabiliti nella nav di `mkdocs.yml` per coerenza)
- `rainbow-square-spiral/`, `pinwheel-of-triangles/`, `nested-circles/`, `starburst/`
  (primo batch di singoli laboratori — stesso schema delle Fasi 2-3: front matter con
  `hide: toc`, obiettivi di apprendimento, mascot-welcome, codice di esempio, domanda di
  previsione, laboratorio Skulpt, spiegazione, tabella, verifica di apprendimento,
  esperimenti, mascot-celebration con rimando "Prossimo" al laboratorio successivo —
  i rimandi "Up next" tradotti come "Prossimo" e mantenuti coerenti con l'ordine della nav)
- `checkerboard-grid/`, `diagonal-stripe-field/`, `dotted-grid/`, `color-wheel-wedges/`,
  `pentagon-chain/` (secondo batch di singoli laboratori)
- `overlapping-squares/`, `flower-petal-function/`, `honeycomb-grid/`, `city-skyline/`,
  `snowflake-arms/` (terzo batch — trovato un bug pre-esistente nell'originale inglese
  `honeycomb-grid/index.md`: dopo la sezione "Learning Check" c'è un blocco di
  contenuto corrotto/duplicato — un secondo esempio di codice non coerente con lo
  stile della lezione, frasi concatenate senza spazi tipo "How the Math WorksThe
  Offset:", e una sezione "Alternative Package Options" fuori tema che consiglia
  librerie esterne. Escluso dalla traduzione italiana, come già fatto per il bug
  del Capitolo 5; il bug resta nell'originale inglese, da segnalare separatamente)
- `polka-dot-canvas/`, `brick-wall/`, `stars-different-sizes/`, `traffic-light/`,
  `fish-school/` (quarto batch — corretto un refuso "metter" → "mettere" in
  `traffic-light/index.md` prima del commit)
- `mountain-range/`, `archimedean-spiral/`, `rainbow-line-spiral/`, `hexagonal-spiral/`,
  `triangular-spiral/` (quinto batch — corretto un refuso "alignate" → "allineate" in
  `rainbow-line-spiral/index.md` prima del commit)
- `inward-spiral/`, `logarithmic-spiral/`, `double-helix-spiral/`, `fibonacci-spiral/`,
  `spiral-of-spirals/` (sesto batch — chiude la categoria 3 "Spirali" della galleria)
- `pentagon-spiral/`, `koch-snowflake/`, `sierpinski-triangle/`, `fractal-tree/`,
  `l-system-plant/` (settimo batch — `pentagon-spiral/` chiude la categoria 3,
  gli altri quattro iniziano la categoria 4 "Frattali e Ricorsione"; il laboratorio
  della galleria `fractal-tree/` è un file diverso e più articolato rispetto a
  `docs/python-labs/12-fractal-tree.md` già tradotto in Fase 3, non un duplicato)
- `turtle-maze/`, `parametric-surface/`, `linden-snowflakes/`, `generative-art/`,
  `bouncing-ball/` (ottavo batch — nota: la pagina inglese `generative-art/index.md`
  dichiara nel celebration finale "you made it through all 100 patterns", ma
  nell'ordine reale della nav ci sono ancora decine di laboratori dopo questo
  (animazione, tipografia, illusioni ottiche, ecc.) — è un'incongruenza editoriale
  pre-esistente nell'originale inglese, non una corruzione testuale; tradotta
  fedelmente senza correggerla, a differenza del blocco duplicato illeggibile
  trovato in `honeycomb-grid/index.md`)
- `clock-face/`, `spirograph-drawer/`, `spiral-text/`, `seven-segment/`,
  `circular-badge/` (nono batch — nota: `spirograph-drawer/index.md` ha un
  altro rimando finale pre-esistente inconsistente, "Up next: Category 11",
  mentre il file successivo reale nella nav è `spiral-text/`; tradotto
  fedelmente senza correggerlo, stessa logica del batch precedente)
- `block-letters/`, `rotating-squares/`, `cafe-wall/`, `moire-pattern/`,
  `riley-waves/` (decimo batch — corretto un refuso "stretate" → "strette" in
  `moire-pattern/index.md` prima del commit; apre la categoria "Illusioni
  Ottiche e Op Art")
- `expanding-hexagons/`, `lissajous-figure/`, `rose-curve/`, `spirograph/`,
  `butterfly-curve/` (undicesimo batch — corretto un refuso "Divide" →
  "Dividi" in `butterfly-curve/index.md` prima del commit; chiude le
  Illusioni Ottiche e apre la categoria "Curve Matematiche")
- `epicycloid-star/`, `sunflower-spiral/`, `spider-web/`, `lightning-bolt/`,
  `galaxy-spiral/` (dodicesimo batch — corretti due refusi: "scegle" →
  "sceglie" in `lightning-bolt/index.md` e "disperso" → "dispersi" in
  `galaxy-spiral/index.md`, prima dei rispettivi commit; `epicycloid-star/`
  chiude le Curve Matematiche, gli altri quattro aprono la categoria "Natura
  e Scienza")
- `ripple-waves/`, `four-fold-doodle/`, `six-fold-mandala/`, `mirror-butterfly/`,
  `truchet-tiles/` (tredicesimo batch — corretto un refuso "stretate" →
  "strette" in `six-fold-mandala/index.md` prima del commit; `ripple-waves/`
  chiude Natura e Scienza, gli altri quattro aprono la categoria "Simmetria e
  Tassellatura")
- `islamic-star/`, `mandelbrot-pixel-art/`, `julia-set/`, `sierpinski-carpet/`,
  `barnsley-fern/` (quattordicesimo batch — `barnsley-fern/index.md` tradotto
  dal contenuto inglese già letto all'inizio della Fase 4 come file campione,
  senza bisogno di rileggerlo; `islamic-star/` chiude Simmetria e Tassellatura,
  gli altri quattro aprono la categoria "Frattali" nel raggruppamento reale
  della nav — diverso dall'ordine di `pattern-ideas.md`)
- `anti-koch/`, `pythagorean-tree/`, `t-square-fractal/`, `levy-c-curve/`,
  `gosper-curve/` (quindicesimo batch — `anti-koch/index.md` tradotto dal
  contenuto inglese letto a inizio Fase 4 come secondo file campione, senza
  rileggerlo; nota: `gosper-curve/index.md` ha un altro rimando finale
  pre-esistente inconsistente, "Up next: Category 5 — Symmetry and Tiling,
  starting with the Sunflower Seed Spiral", mentre il file reale successivo
  nella nav è `dragon-curve/` — tradotto fedelmente senza correggerlo, stessa
  logica delle incongruenze precedenti)
- `dragon-curve/`, `hilbert-curve/`, `cantor-dust/`, `kaleidoscope-slice/`,
  `pinwheel-tiling/` (sedicesimo batch — nessun problema trovato)
- `escher-fish/`, `voronoi-regions/`, `penrose-rhombus/`, `river-delta/`
  (diciassettesimo batch — trovati già tradotti e non committati in una
  sessione precedente; verificato codice/percorsi immagine intatti con
  `git diff` prima del commit)
- `coral-branch/`, `leaf-venation/`, `dna-helix/`, `topographic-map/`,
  `epitrochoid/` (diciottesimo batch — nota: il celebration finale di
  `topographic-map/index.md` non ha un rimando "Up next" al laboratorio
  successivo ma un generico "Browse the Turtle Graphics Gallery", a
  differenza degli altri file; tradotto fedelmente senza correggerlo,
  stessa logica delle incongruenze editoriali già documentate sopra)
- `superellipse/`, `cassini-oval/`, `fermat-spiral/`, `astroid/`,
  `mach-bands/` (diciannovesimo batch — stessa incongruenza già vista in
  `topographic-map/`: anche `astroid/index.md` chiude con un generico
  "Browse the Turtle Graphics Gallery" invece di un rimando "Up next";
  nota di metodo: le liste `labels = [[...]]` dentro i blocchi di codice
  Python che scrivono testo sul canvas con `monty.write()` (es. 'b = 120
  (one oval)' in `cassini-oval/`) sono state lasciate intatte in inglese
  perché sono stringhe letterali dentro codice eseguibile — la regola
  "codice mai tradotto, carattere per carattere" vale anche per le
  stringhe visibili sul canvas, non solo per identificatori/sintassi)
- `vasarely-sphere/`, `scintillating-grid/`, `impossible-triangle/`,
  `ring-pulsation/`, `binary-tree-name/`, `turtle-chase/`,
  `reaction-diffusion/` (ventesimo e ultimo batch della Fase 4 — nessun
  problema trovato; conferma della nota di metodo sui commenti `#` dentro
  i blocchi di codice Python, es. `# ... create prey (green) and hunter
  (red) turtles ...` in `turtle-chase/`: restano in inglese, stessa
  regola delle stringhe letterali)

**FASE 4 COMPLETA — tutti i 102 file/unità della Turtle Graphics Gallery
tradotti** (nav di `mkdocs.yml`, `pattern-ideas.md`, `index.md` root, e
tutti i singoli laboratori).

**FASE 5 COMPLETA — tutte le 31 pagine lato lettore dei MicroSims
tradotte** (nav di `mkdocs.yml`, `docs/sims/index.md` — la griglia di
card della galleria —, `docs/sims/graph-viewer/index.md`, e tutti i 30
singoli MicroSim). Decisioni prese durante questa fase:

- I **nomi dei MicroSim** (es. "Code Stepper" → "Esecutore di Codice
  Passo-Passo") sono stati tradotti in italiano, per coerenza con la
  convenzione già stabilita per titoli di capitoli, laboratori Python e
  pattern della Turtle Graphics Gallery — non sono nomi di prodotto fissi
  come "Skulpt" o "CodeMirror", ma titoli descrittivi come "Rainbow
  Square Spiral". Tradotti ovunque: nav di `mkdocs.yml`, titoli H1 e
  `title:` nel front matter di ogni pagina, titoli delle card nella
  galleria `sims/index.md`.
- Un titolo con `:` al suo interno (`Unit Circle Degrees and Radians`)
  è stato reso con una lineetta — `Cerchio Unitario — Gradi e Radianti`
  — invece dei due punti, perché un `:` in un valore di nav YAML lo fa
  interpretare come una mappatura annidata e rompe `mkdocs.yml` (validato
  con `python3 -c "import yaml; yaml.safe_load(...)"` prima e dopo la
  correzione).
- Front matter YAML di ogni pagina: solo `title`/`description` tradotti;
  `image`, `og:image`, `twitter:image`, `social.cards`, `quality_score`
  lasciati invariati (metadati di generazione/social, non prosa).
- **`docs/sims/microsim-ideas.md` (904 righe) escluso dalla Fase 5.** È un
  documento di pianificazione interno per chi genera nuovi MicroSim (non
  è nella nav, stato "draft-for-review", e il suo testo introduttivo è
  disallineato con lo stato reale del repo — dice "no sims have been
  generated yet" mentre tutti i 30 MicroSim esistono già). Trattato come
  i log di `logs/` o `CONTENT-GENERATION-GUIDELINES.md`: materiale per
  chi mantiene il libro, non contenuto per il lettore. Da rivalutare se
  l'utente lo richiede esplicitamente.

**FASE 6 COMPLETA — tutti i 13 file della Guida per gli Insegnanti
tradotti** (nav di `mkdocs.yml`, `index.md` panoramica, `contribute.md`,
`adding-custom-python-labs.md`, `run-pause-buttons.md`,
`code-mirror-example.md`, `order-of-concepts.md`,
`comparing-textbooks.md`, e tutte le 7 pagine di Prompt di Esempio).
Decisioni prese durante questa fase:

- Le **etichette dei pulsanti dell'interfaccia** (Run, Pause, Resume, Run
  New Code, Reset) restano in inglese ovunque compaiano — nel testo
  prosa, nelle tabelle di comportamento, e nel codice HTML/JS incorporato
  — coerente con la decisione 2 già presa (UI chrome resta in inglese
  come "linguaggio universale dei bottoni").
- I **blocchi di codice incorporati HTML/CSS/JS** in `code-mirror-example.md`
  (inclusi i commenti Python dentro la stringa `_cmLines` che Skulpt
  esegue) sono stati lasciati completamente intatti, anche se non sono
  racchiusi in un fence ```` ```html ```` ma scritti direttamente nel
  Markdown — è comunque infrastruttura di pagina/codice eseguibile, non
  prosa.
- I **blocchi ``` generici senza tag di linguaggio** che contengono testo
  in inglese semplice (i prompt dati all'IA in `order-of-concepts.md`, e
  il diagramma di flusso ASCII "Decision Guide" in
  `adding-custom-python-labs.md`) sono stati trattati come prosa e
  tradotti — a differenza dei blocchi ```python/```sh/```bash/```yaml
  che restano sempre intatti perché contengono sintassi eseguibile vera.
  Il criterio: un fence senza tag linguaggio il cui contenuto sono frasi
  in inglese naturale è prosa formattata come citazione, non codice.
- Le pagine di **Prompt di Esempio** (`teachers-guide/prompts/*.md`) sono
  i prompt letterali dati all'IA durante la creazione di questo stesso
  libro. Tradotta la prosa, ma lasciati intatti i riferimenti `@percorso/file`
  e gli slash-command (`/ibook`, `/course-description-analyzer`,
  `/learning-graph-generator`, `/book-chapter-generator`,
  `/microsim-generator`) perché funzionano come identificatori di
  strumenti, non prosa. Il file `06-microsim-ideas-given-to-fable-5.md`
  non è nella nav di `mkdocs.yml` ma è stato tradotto comunque per
  completezza della collezione di prompt (è molto breve).
- `order-of-concepts.md` contiene un bug pre-esistente nell'originale
  inglese: un blocco ``` di apertura senza chiusura corrispondente in
  fondo al file (5 marcatori ``` totali, numero dispari). Preservato
  fedelmente senza correggerlo, stessa logica delle incongruenze
  editoriali già documentate per la Fase 4.

**FASE 7 COMPLETA — Jupyter Notebooks docs e Advanced Python Examples
tradotti.** File tradotti: nav di `mkdocs.yml` (sezioni "Notebook Jupyter"
ed "Esempi di Python Avanzato"), `docs/jupyter/index.md`,
`docs/jupyter/01-setup.md`, `docs/jupyter/02-draw-figure.md`,
`docs/jupyter/02-setup-canvas.md`, `docs/jupyter/20-canvas-color-bars.md`,
`docs/advanced/stocks.md`, `docs/advanced/mnist.md`. Inoltre tradotte le
due pagine orfane ma legittime `docs/advanced-python/01-intro.md` e
`02-roll-the-dice.md` (non nella nav, ma contenuto reale per il lettore,
stessa logica di `text-only-example.md` in Fase 3) — il file sorgente
`roll-dice.py` resta codice, non toccato.

Decisioni di questa fase:

- **Un solo notebook Jupyter tradotto**: `docs/jupyter/draw-figure.ipynb`,
  l'unico `.ipynb` effettivamente collegato da una pagina raggiungibile
  dalla nav (`02-draw-figure.md`). Tradotte solo le 4 celle markdown di
  spiegazione con lo strumento `NotebookEdit`; le celle codice (inclusi i
  commenti Python come `# this will be true for alternate edges`) sono
  rimaste intatte. Verificato con un confronto cella per cella che il
  codice non fosse stato toccato.
- **Notebook orfani esclusi dallo scope**: `02-draw-box.ipynb`,
  `canvas-test.ipynb`, `Python_Introduction.ipynb`,
  `variables-and-strings.ipynb` non sono collegati da nessuna pagina
  `.md` né dalla nav — trattati come i file sotto `microsim-ideas.md`,
  priorità minima, da rivalutare se richiesti esplicitamente.
  `docs/jupyter/.ipynb_checkpoints/` è una cartella di backup automatico
  di Jupyter (non contenuto editoriale) ed è esclusa a priori.
- **Typo pre-esistenti "Jypyter"/"juypter"**: nel testo prosa inglese
  originale (titoli, link) sono stati corretti silenziosamente in
  "Jupyter" durante la traduzione italiana (sono refusi di battitura, non
  bug di contenuto pedagogico). Dentro i blocchi di codice/shell (es. il
  comando `juypter notebook` nei passaggi di setup conda) sono stati
  lasciati intatti carattere per carattere, perché sono codice eseguibile
  — stessa regola generale, anche se qui il comando così com'è non
  funzionerebbe davvero se digitato alla lettera.

**FASE 8 COMPLETA — tutti i 9 file nav-collegati di `docs/learning-graph/`
tradotti**, più la nav di `mkdocs.yml` (sezione "Grafo di Apprendimento"):
`index.md`, `course-description-assessment.md`, `concept-list-v1.md`,
`concept-list.md`, `quality-metrics.md`, `concept-taxonomy.md`,
`taxonomy-distribution.md`, `mascot-test.md`, `faq-quality-report.md`.

**Decisione di metodo cruciale per questa fase** (verificata prima di
tradurre, non assunta): i titoli dei 450/350 concetti e i nomi delle 14
categorie di tassonomia (ENV, SYN, DAT, CTL, FUN, COL, MOD, TXT, FIO,
ERR, OOP, VIZ, ALG, ADV e i rispettivi nomi estesi come "Environment &
Tools") **restano sempre in inglese**, in ogni file di questa sezione —
non solo in `concept-list.md`/`concept-list-v1.md` ma anche nelle liste
di esempio dentro `quality-metrics.md`, `taxonomy-distribution.md` e
`faq-quality-report.md`. Verificato con
`python3 -c "import json; ..."` che questi titoli/nomi corrispondono
esattamente (stessa stringa carattere per carattere) alle label dei nodi
in `learning-graph.json`/`learning-graph.csv` e alle chiavi di
`taxonomy-names.json` — gli stessi file dati che alimentano il
Visualizzatore del Grafo di Apprendimento (MicroSim, Fase 5) e il tool
di verifica delle dipendenze citato in CLAUDE.md ("L'assegnazione dei
concetti è la fonte di verità"). Tradurli romperebbe quella
corrispondenza automatica. Tradotti invece: titoli di pagina, prosa
introduttiva/esplicativa, intestazioni di sezione, etichette di campo
generiche (es. "Conteggio", "Percentuale"), raccomandazioni — ma non le
etichette di schema CSV/dati come `TaxonomyID`/`ConceptID` che sono
nomi di colonna letterali in `learning-graph.csv`.

File esclusi dallo scope (stessa logica di `microsim-ideas.md`):
`book-metrics.md` e `chapter-metrics.md` — non collegati alla nav né da
nessuna pagina `.md`, report auto-generati per chi mantiene il libro con
un timestamp di generazione (2026-07-02) già disallineato con lo stato
attuale (i conteggi parole riflettono la versione inglese pre-traduzione,
non quella italiana). I file `.py`, `.json` e `.csv` in
`docs/learning-graph/` (script e dati) non sono mai stati toccati, per
definizione.

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

**FASE 2 COMPLETA — tutti i 38 capitoli tradotti (Capitoli 1-38).** Questo chiude il
cuore didattico del libro.

**FASE 3 COMPLETA — tutti i 19 file di Python Labs tradotti** (`index.md` +
17 lezioni numerate + `text-only-example.md`).

**FASE 4 IN CORSO — Turtle Graphics Gallery.** Tradotti finora: nav di `mkdocs.yml`,
`pattern-ideas.md`, `index.md` (root), `rainbow-square-spiral/`, `pinwheel-of-triangles/`,
`nested-circles/`, `starburst/`, `checkerboard-grid/`, `diagonal-stripe-field/`,
`dotted-grid/`, `color-wheel-wedges/`, `pentagon-chain/`, `overlapping-squares/`,
`flower-petal-function/`, `honeycomb-grid/`, `city-skyline/`, `snowflake-arms/`,
`polka-dot-canvas/`, `brick-wall/`, `stars-different-sizes/`, `traffic-light/`,
`fish-school/`, `mountain-range/`, `archimedean-spiral/`, `rainbow-line-spiral/`,
`hexagonal-spiral/`, `triangular-spiral/`, `inward-spiral/`, `logarithmic-spiral/`,
`double-helix-spiral/`, `fibonacci-spiral/`, `spiral-of-spirals/`, `pentagon-spiral/`,
`koch-snowflake/`, `sierpinski-triangle/`, `fractal-tree/`, `l-system-plant/`,
`turtle-maze/`, `parametric-surface/`, `linden-snowflakes/`, `generative-art/`,
`bouncing-ball/`, `clock-face/`, `spirograph-drawer/`, `spiral-text/`,
`seven-segment/`, `circular-badge/`, `block-letters/`, `rotating-squares/`,
`cafe-wall/`, `moire-pattern/`, `riley-waves/`, `expanding-hexagons/`,
`lissajous-figure/`, `rose-curve/`, `spirograph/`, `butterfly-curve/`,
`epicycloid-star/`, `sunflower-spiral/`, `spider-web/`, `lightning-bolt/`,
`galaxy-spiral/`, `ripple-waves/`, `four-fold-doodle/`, `six-fold-mandala/`,
`mirror-butterfly/`, `truchet-tiles/`, `islamic-star/`, `mandelbrot-pixel-art/`,
`julia-set/`, `sierpinski-carpet/`, `barnsley-fern/`, `anti-koch/`,
`pythagorean-tree/`, `t-square-fractal/`, `levy-c-curve/`, `gosper-curve/`,
`dragon-curve/`, `hilbert-curve/`, `cantor-dust/`, `kaleidoscope-slice/`,
`pinwheel-tiling/`, `escher-fish/`, `voronoi-regions/`, `penrose-rhombus/`,
`river-delta/`, `coral-branch/`, `leaf-venation/`, `dna-helix/`,
`topographic-map/`, `epitrochoid/`, `superellipse/`, `cassini-oval/`,
`fermat-spiral/`, `astroid/`, `mach-bands/`, `vasarely-sphere/`,
`scintillating-grid/`, `impossible-triangle/`, `ring-pulsation/`,
`binary-tree-name/`, `turtle-chase/`, `reaction-diffusion/`
(102 di 102 file/unità — **FASE 4 COMPLETA**).

**FASE 5 COMPLETA.** Tradotte 31 pagine: nav di `mkdocs.yml` (sezione
MicroSims), `docs/sims/index.md`, `docs/sims/graph-viewer/index.md`, e
tutti i 30 singoli MicroSim (`boolean-logic-lab`, `code-stepper`,
`control-flow-explorer`, `dice-roll-histogram`, `dictionary-key-lookup`,
`expression-evaluator`, `for-loop-stepper`, `fractal-tree-explorer`,
`function-call-flow`, `graph-traversal-explorer`, `inheritance-explorer`,
`json-python-mapper`, `list-index-explorer`, `modulo-clock`,
`object-instance-inspector`, `range-explorer`, `recursion-call-stack`,
`regex-match-lab`, `rgb-color-mixer`, `scope-inspector`, `search-race`,
`set-operations-venn`, `sine-wave-explorer`, `sorting-comparer`,
`stack-queue-simulator`, `string-slicer`, `turtle-state-inspector`,
`unit-circle-radians`, `variable-memory-model`, `while-loop-stepper`).
`docs/sims/microsim-ideas.md` escluso dallo scope (vedi nota sopra).

**FASE 6 COMPLETA.** Tradotti tutti i 13 file di `docs/teachers-guide/`:
nav di `mkdocs.yml` (sezione "Guida per gli Insegnanti"), `index.md`
(panoramica, 508 righe), `adding-custom-python-labs.md`,
`code-mirror-example.md`, `comparing-textbooks.md`, `contribute.md`,
`order-of-concepts.md`, `run-pause-buttons.md`, e tutte le 7 pagine in
`teachers-guide/prompts/` (`index.md`, `01-list-old-concepts.md`,
`02-course-description.md`, `03-learning-graph.md`,
`04-book-chapter-generator.md`, `05-content-generation-strategy.md`,
`06-microsim-ideas-given-to-fable-5.md`).

**FASE 7 COMPLETA.** Tradotti: nav di `mkdocs.yml` (Notebook Jupyter,
Esempi di Python Avanzato), i 5 file di `docs/jupyter/*.md` collegati
alla nav, i 2 file di `docs/advanced/*.md`, i 2 file orfani di
`docs/advanced-python/*.md`, e le celle markdown di
`docs/jupyter/draw-figure.ipynb` (unico notebook collegato alla nav).
Notebook orfani non collegati (`02-draw-box.ipynb`, `canvas-test.ipynb`,
`Python_Introduction.ipynb`, `variables-and-strings.ipynb`) esclusi
dallo scope, vedi nota sopra.

**FASE 8 COMPLETA.** Tradotti tutti i 9 file nav-collegati di
`docs/learning-graph/` più la nav di `mkdocs.yml`. Titoli dei concetti e
nomi delle categorie di tassonomia lasciati in inglese ovunque (vedi nota
sopra); `book-metrics.md`/`chapter-metrics.md` esclusi (orfani, stale).

Con questo si chiudono tutte le fasi di priorità Alta/Media.

**FASE 9 (Trinket Labs, 23 file) SALTATA DELIBERATAMENTE — decisione
dell'utente (2026-10-13).** La sezione era già segnata a priorità minima
e la sua stessa nav originale la marca "(deprecated)"; l'utente ha
confermato esplicitamente di non volerla tradurre e considera il manuale
completo così com'è.

## 6. Stato finale del progetto (2026-10-13)

**Il piano di traduzione è considerato completo.** Tradotte le Fasi 1–8
(pagine di ingresso, 38 capitoli, Python Labs, Turtle Graphics Gallery,
MicroSims, Teacher's Guide, Jupyter/Advanced Python, Learning Graph).
Fase 9 (Trinket Labs) saltata su decisione esplicita dell'utente.

File/sezioni rimasti volutamente in inglese o esclusi dallo scope, con
motivazione già documentata sopra:
- `docs/trinket/` (Trinket Labs, deprecato) — intera sezione, Fase 9
- `docs/sims/microsim-ideas.md` — documento di pianificazione interno
- `docs/learning-graph/book-metrics.md`, `chapter-metrics.md` — report
  auto-generati orfani e già obsoleti
- Notebook Jupyter orfani non collegati alla nav (`02-draw-box.ipynb`,
  `canvas-test.ipynb`, `Python_Introduction.ipynb`,
  `variables-and-strings.ipynb`)
- Nomi dei 450 concetti e delle 14 categorie di tassonomia in
  `docs/learning-graph/` — restano in inglese ovunque perché sono le
  chiavi esatte usate da `learning-graph.json`/`.csv` e dal
  Visualizzatore del Grafo
- Tutti i file `.py`, `.json`, `.csv` di dati/script in tutto il
  progetto — mai toccati, per definizione
- UI chrome dei laboratori (pulsanti Run/Pause/Resume/Reset) — in
  inglese ovunque, per decisione 2

Se in futuro si vorrà riprendere la Fase 9 o rivalutare uno dei punti
sopra, questo documento resta la guida di riferimento: le regole
semantiche in sezione 1 e le decisioni in sezione 2 restano valide.

Note di qualità accumulate durante la Fase 2, da continuare ad applicare nelle fasi
successive: (1) controllare sempre con `grep '!\[.*\]('` (o pattern equivalente per il
formato del file) che tutti i percorsi immagine restino intatti dopo la traduzione (vedi
incidente Capitolo 34); (2) quando un file elenca più termini paralleli (pilastri,
categorie) in una tabella o lista, controllare con `grep -ni` che tutte le occorrenze del
termine inglese siano state tradotte in modo consistente, non solo la prima (vedi
Capitolo 36); (3) rileggere le frasi con verbi alla terza persona singolare per refusi di
coniugazione (es. "imparo"/"convertí" invece di "impara"/"converte" — capitato più volte
nei Capitoli 32-38); (4) per contenuti che hanno un `references.md` con formattazione
leggermente diversa dal pattern standard (es. link finale extra, riga `---` finale),
preservare quella particolarità invece di normalizzarla (vedi Capitoli 23 e 38); (5) nomi
propri/titoli di libri come "Beginning Python" restano non tradotti, per coerenza con le
pagine di ingresso già tradotte in Fase 1.

Nota di qualità: durante la traduzione del Capitolo 5 è stato trovato e corretto un
bug pre-esistente nell'originale inglese `docs/chapters/05-drawing-with-turtle/quiz.md`
(riga duplicata con un tag placeholder incollato per errore prima della domanda 7).
Il bug esiste ancora nella versione inglese — da segnalare/correggere separatamente
se si vuole tenere i due testi allineati.
