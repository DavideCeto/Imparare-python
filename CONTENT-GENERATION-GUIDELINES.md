# Linee guida per la generazione di contenuti — Introduzione al Python

Questo file definisce le regole per la creazione di contenuti rivolti agli studenti in questo corso.
Tutti gli agenti AI e gli autori umani che creano lezioni, laboratori, quiz o altre pagine rivolte agli studenti devono seguire queste linee guida. I contenuti rivolti agli insegnanti (guida per gli insegnanti, descrizione del corso) non devono utilizzare questa modalità.

---

## Strumento principale di insegnamento: Grafica Turtle interattiva

**La caratteristica fondamentale di questo libro di testo è la grafica Turtle interattiva che viene eseguita direttamente nel browser.**

Nei capitoli da 1 a 18, ogni lezione deve essere svolta attraverso programmi Turtle interattivi, non attraverso elenchi di codice statici. Gli studenti cliccano su **Esegui** e osservano il programma Turtle disegnare qualcosa sul canvas, poi modificano immediatamente il codice ed eseguono nuovamente l'esecuzione — tutto questo senza installare nulla o lasciare la pagina. Questo ciclo di feedback live è ciò che rende il libro di testo interessante per gli studenti dai 10 ai 14 anni.

### Il ciclo “Vedere, Eseguire, Modificare”

Ogni laboratorio Skulpt segue questo ciclo di tre fasi:

1. **Vedere** — un breve programma Turtle (da 5 a 15 righe) appare nella zona di testo modificabile, accompagnato da una spiegazione in prosa del suo funzionamento.
2. **Eseguire** — lo studente clicca su Esegui e vede il programma Turtle disegnare qualcosa sul canvas, a destra del codice.
3. **Modificare** — la sezione “Esercizi” in fondo a ogni lezione offre 3-5 opportunità specifiche per modificare il codice: un colore diverso, un numero diverso di lati, una nuova forma, una velocità maggiore, ecc.

**Questo ciclo è il cuore del libro di testo.** Non sostituire mai blocchi di codice statici, screenshot di output o link esterni (ad esempio Trinket) in qualsiasi lezione dei capitoli da 1 a 18.

### Prevedere prima di eseguire

Prima di ogni laboratorio di dimostrazione di Skulpt, Monty chiede allo studente di **prevedere cosa farà il programma prima di cliccare su “Run”**. Fermarsi per riflettere sul codice prima di eseguirlo è una delle abitudini più importanti che un programmatore principiante può sviluppare: si allena il modello mentale che permette agli studenti di risolvere i problemi in modo autonomo, invece di cambiare le cose a caso.

**Posizione:** Il messaggio per la previsione viene inserito **immediatamente sopra** il blocco del laboratorio di Skulpt, prima che lo studente possa eseguire il codice.

**Formato — utilizzare `mascot-thinking`:**

```markdown
!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, look at the code below.
    How many sides do you think the turtle will draw? Make your guess — then find out!
```

**Regole:**

| Regola | Dettaglio |
|--------|----------|
| Chiedere una domanda specifica | “Quanti lati?” / “Quale colore?” / “Quante volte il ciclo si ripeterà?” – non “Cosa succederà?” |
| Calibrare la difficoltà | Aver circa il 50% di probabilità di risposta corretta nella prima previsione – abbastanza facile da tentare, ma abbastanza sorprendente da favorire lo sviluppo dell’abitudine |
| Chiudere il ciclo | Dopo il laboratorio, aggiungere una breve frase di commento (“Hai indovinato?”) – non è necessario un secondo avvertimento |
| Evitare sovraccarico con controlli di apprendimento | I laboratori di controllo dell’apprendimento forniscono già allo studente un compito; aggiungere una previsione in più può causare sovraccarico |
| Conta per il limite della mascotte | Le previsioni `mascot-thinking` e i concetti `mascot-thinking` entrambi sono conteggiati nel limite di 6 unità per lezione |

### Controlli di Apprendimento

Per ogni concetto importante, includere almeno uno **Controllo di Apprendimento** – un secondo laboratorio di Skulpt (distinto dal laboratorio principale) in cui lo studente deve produrre o riparare il codice attivamente.

| Tipo | Quando utilizzare | Avvertenza |
|------|-------------|------------|
| **Aggiungere la riga mancante** — il programma si ferma prima o restituisce un risultato errato finché lo studente aggiunge una riga | Introduzione di un nuovo comando o concetto | `mascot-thinking` |
| **Trovare e correggere il bug** — il programma presenta un piccolo errore intenzionale (nome del metodo errato, errore di un singolo elemento in `range()`, mancanza di `pendown()`, ecc.) | Dopo l’introduzione di un concetto | `mascot-warning` |

**Formato di controllo dell’apprendimento — riga mancante:**

```markdown
!!! mascot-thinking "Your Turn — Add the Missing Line"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The program below draws three sides of a square and then stops.
    Add **one line** so Monty completes the fourth side!

[Skulpt lab block with the incomplete program in the editor]
```

**Formato di controllo dell’apprendimento — trovare il bug:**

```markdown
!!! mascot-warning "Spot the Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Something is wrong with the program below — Monty draws a straight line
    instead of a triangle. Can you find and fix the mistake?

[Skulpt lab block with the buggy program in the editor]
```

### Dimensionamento dei laboratori per i programmi con turtle

Mantenere i programmi abbastanza brevi affinché gli studenti possano leggere tutto d’un fiato:

- **Laboratori introduttivi (Capitoli 1–5):** 4–8 righe di Python
- **Laboratori intermedi (Capitoli 6–18):** 8–20 righe di Python
- **Laboratori avanzati (Capitoli 19+):** nessun limite stretto, ma si preferiscono diversi laboratori brevi e specifici piuttosto che uno lungo

### Quando utilizzare ogni tipo di laboratorio

Esistono due schemi per i laboratori di Skulpt. Scegliate in base a se il programma utilizza grafica con turtle:

| Situazione | Tipo di laboratorio | Class HTML |
|-----------|-------------|------------|
| Il programma utilizza `import turtle` o qualsiasi comando con turtle | **Laboratorio di disegno** | `class="cm-lab"` |
| Il programma utilizza solo `print()`, variabili, cicli, funzioni, ecc. | **Laboratorio testuale** | `class="cm-lab cm-text-only"` |

**Laboratori di disegno** (Lezioni 1–18 con turtle) mostrano un canvas di 400 × 400 pixel a destra dello schermo, dove il programma con turtle disegna.

**Laboratori di tipo testuale** nascondono completamente il pannello della tavola; lo editor del codice si estende per riempire l’intera larghezza del contenuto. Utilizzare questi laboratori per qualsiasi programma che produce soltanto output testuale — chiamate, valori variabili, risultati in stringhe, ecc. Questa disposizione è la default dal Capitolo 19 in poi, e può anche apparire nei capitoli precedenti per i rari concetti che non richiedono l’uso della tartaruga (ad esempio, una lezione che utilizza soltanto variabili del tipo `print()`).

Non inserire mai un laboratorio di tipo testuale in una lezione che richiede anche la presenza della tavola, e non inserire mai un laboratorio di disegno in una lezione i cui programmi non utilizzano comandi della tartaruga — la tavola vuota spreca semplicemente spazio e confonde gli studenti.

---

## Requisiti di struttura della lezione

Queste regole si applicano a ogni pagina della lezione destinata agli studenti, indipendentemente dal capitolo.

### Obiettivi di apprendimento

Ogni lezione deve iniziare con 1–3 obiettivi di apprendimento scritti in inglese semplice. Posizionarli **prima** della nota `mascot-welcome`, in modo che gli studenti sappiano verso cosa stanno lavorando prima che Monty inizi a parlare.

**Formato:**

```markdown
By the end of this lesson you'll be able to:

- Draw a square using a `for` loop with `forward()` and `right()`
- Explain why loops save you from writing the same line four times
- Change the number of sides to draw any regular polygon
```

**Regole:**

- Scrivere dal punto di vista dello studente: “Potrete…”
- Utilizzare verbi concreti e osservabili: *disegnare, scrivere, sistemare, spiegare, modificare, costruire* — mai “comprendere” o “sapere di”
- 1 obiettivo = 1 nuovo concetto; se ci sono 4 o più obiettivi, la lezione è troppo ampia — suddividerla in due lezioni
- Mantenere il linguaggio a un livello di lettura adeguato alla scuola elementare — nessun gergo negli obiettivi stessi; definirli successivamente nella lezione

### Ponte con Scratch

Per ogni nuovo concetto nei capitoli 1–14 che ha un equivalente in Scratch, includere un **Ponte con Scratch** subito dopo l’introduzione del concetto. Questo è il modo più efficace per coinvolgere gli studenti: essi già hanno un modello mentale basato su Scratch; collegarlo esplicitamente riduce notevolmente lo sforzo cognitivo.

**Format — utilizzare `mascot-tip` per la etichetta “Ponte Scratch”:**

```markdown
!!! mascot-tip "Scratch Bridge"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch you used the **"Move 10 steps"** block.
    In Python, `forward(10)` does exactly the same thing —
    it tells Monty to walk forward 10 steps!
```

**Comuni ponti tra Scratch e Python:**

| Blocco Scratch | Equivalente Python | Prima apparizione |
|---------------|-------------------|---------------|
| Muovere ___ passi | `forward(n)` | Capitolo 5 |
| Girare ↻ ___ gradi | `right(n)` | Capitolo 5 |
| Girare ↺ ___ gradi | `left(n)` | Capitolo 5 |
| Abbassare/Alzare la penna | `pendown()` / `penup()` | Capitolo 5 |
| Impostare il colore della penna | `pencolor("red")` | Capitolo 5 |
| Ripetere ___ | `for i in range(n):` | Capitolo 7 |
| Se ___ allora | `if condition:` | Capitolo 9 |
| Se ___ allora/altro | `if condition: … else:` | Capitolo 9 |
| Impostare ___ su ___ | `variable = value` | Capitolo 3 |
| Dire ___ | `print(...)` | Capitolo 1 |
| Chiedere ___ e aspettare | `input(...)` | Capitolo 13 |

**Regole:**

- Requisito ogni volta che esiste un equivalente Scratch (Capitoli 1–10); opzionale ma incoraggiato nei Capitoli 11–14
- Saltato nei Capitoli 15+ — gli studenti hanno superato il modello mentale Scratch
- Devi sempre considerare Python come il passo naturale successivo — non dire mai “in Scratch dovevi…” (suona disprezzante)
- Conta per il limite massimo di 6 concetti per lezione

### Un nuovo concetto per ogni laboratorio

Ogni **laboratorio di dimostrazione** deve introdurre esattamente **un nuovo concetto**. Se una lezione tratta tre comandi Python, scrivere tre laboratori brevi e sequenziali — non un laboratorio che introduca tutti e tre insieme.

Questa è la regola di carico cognitivo più importante in questo libro di testo. Un programmatore principiante non può analizzare la sintassi sconosciuta, prevedere il comportamento del programma e riconnetterlo con le conoscenze pregresse. Isolare ogni nuovo concetto in un blocco di codice funzionante.

**Modello corretto:** Laboratorio A mostra solo `penup()` → Laboratorio B aggiunge `goto()` → Laboratorio C completa l’idea con `pendown()`, ognuno basato sull’altro.

**Modello errato:** In un laboratorio, in cui `penup()`, `goto()` e `pendown()` appaiono per la prima volta insieme.

Il laboratorio di dimostrazione per qualsiasi concetto dovrebbe essere il **programma più semplice possibile** che dimostri soltanto quel concetto. Salva le combinazioni e le utilizzazioni creative per la sezione degli esperimenti.

### Nuovo vocabolario

Quando un termine tecnico appare **per la prima volta**, segui questa regola a tre passi:

1. **Incolla** il termine la prima volta: `**parameter**`
2. Definiscilo immediatamente in una frase in lingua comune, utilizzando una analogia concreta
3. Mostragli nel codice funzionante sulla stessa pagina

**Esempio:**
> Un **parametro** è informazione che passi a una funzione quando la chiami — come dire a una macchina distributrice quale pulsante premere prima che faccia qualcosa.

**Regole aggiuntive:**

- Non introduci mai un termine nella prima frase di una spiegazione — stabilisci il concetto in lingua comune prima, poi chiamalo
- Non definisci due termini nuovi nella stessa frase
- Rinfresca il termine almeno un'altra volta nella stessa lezione (nella tabella delle spiegazioni, in un prompt di esperimento, o nel dialogo di Monty)
- Non incolla un termine la seconda volta o dopo — l'incollando segnala "questo è nuovo"

### Ripasso e revisione spiralata

Ogni lezione deve naturalmente utilizzare almeno 2–3 concetti dai **capitoli precedenti** come contesto di riferimento nei laboratori di dimostrazione — senza ricomporli. Gli studenti consolidano l'apprendimento precedente incontrandolo in nuove situazioni.

**Come applicare:**

- **Insegnare i cicli `for` (Capitolo 7)?** Scrivi il corpo del ciclo utilizzando `forward()` e `right()` — rafforzando i comandi del Capitolo 5.
- **Insegnare `if/else` (Capitolo 9)?** Utilizzare una variabile per la condizione — rafforzando le variabili del Capitolo 3.
- **Insegnare i metodi string (Capitolo 14)?** Forniscili da `input()` — rafforzando l'input utente del Capitolo 13.

**Cosa non fare:**

- Non aggiungere un paragrafo di "ricordo" per riesporre un concetto precedente — utilizzalo semplicemente.
- Non ripresentare un concetto precedente come se fosse nuovo: "Prima di tutto, ricorda che `forward()` sposta la tartaruga…" — affidi che gli studenti leggano i capitoli precedenti.

### Gestione dei messaggi di errore di Skulpt

Gli studenti potranno verificarsi modificando il codice. Skulpt stampa i messaggi di errore sul pannello `<pre class="cm-output">`. Le lezioni dovrebbero preparare gli studenti a leggere gli errori con calma.

**Per fasce di capitoli:**

| Capitoli | Indicazioni |
|----------|----------|
| 1–5 | Aggiungere un breve paragrafo in testo semplice "Se vedi un messaggio di errore rosso" dopo il primo laboratorio. Massimo 2–3 frasi. |
| 6–12 | Includere le indicazioni di errore nel `mascot-warning` per il errore più probabile in quel capitolo. |
| 13+ | Aspettarsi che gli studenti leggano i messaggi di errore in modo autonomo. Aggiungere note solo per errori particolarmente difficili (ad esempio, `TypeError: can only concatenate str (not "int") to str`). |

**Erroi più comuni di Skulpt per fasce di capitoli:**

| Capitoli | Errori comuni |
|----------|---------------|
| 1–4 | `NameError` con comandi scritti male, imputazione errata |
| 5–8 | Mancanza di `pendown()`, tipo di argomento errato passato a `forward()` |
| 9–12 | Mancanza di un punto e virgola dopo `if` / `for`, imputazione errata dopo il punto e virgola |
| 13–18 | `TypeError` che mescola `str` + `int`, `ValueError` proveniente da una conversione errata di `int()` |

**Formato del paragrafo "Se vedi un errore" (Capitoli 1–5):**

```markdown
**If you see a red error message:** Check your spelling — Python is case-sensitive,
so `Forward(100)` won't work but `forward(100)` will.
Also make sure every line inside the loop is indented by exactly 4 spaces.
```

---

## Apprendimento della Maschera: Monty il Python

### Indice dei File della Maschera

I file canonici per questa maschera. Quando si modifica uno di questi, aggiorna gli altri nello stesso turno in modo che rimangano sincronizzati.

| File | Scopo |
|------|---------|
| [`docs/img/mascot/neutral.png`](docs/img/mascot/neutral.png) | Posizione di default / utilizzo generale |
| [`docs/img/mascot/welcome.png`](docs/img/mascot/welcome.png) | Posizione all'inizio del capitolo |
| [`docs/img/mascot/thinking.png`](docs/img/mascot/thinking.png) | Posizione per i concetti chiave / previsioni / verifica dell'apprendimento |
| [`docs/img/mascot/tip.png`](docs/img/mascot/tip.png) | Suggerimento / Ponte dei Crolli / guida utile |
| [`docs/img/mascot/warning.png`](docs/img/mascot/warning.png) | Posizione per gli errori comuni / correzione dei bug / pericoli |
| [`docs/img/mascot/encouraging.png`](docs/img/mascot/encouraging.png) | Posizione per il contenuto difficile / lotta |
| [`docs/img/mascot/celebration.png`](docs/img/mascot/celebration.png) | Posizione alla fine della lezione / realizzazione |
| [`docs/css/mascot.css`](docs/css/mascot.css) | Stili di avvertimento personalizzati per i sette contesti della posizione |
| [`docs/learning-graph/mascot-test.md`](docs/learning-graph/mascot-test.md) | Pagina di test che esercita ogni stile di avvertimento |

### Panoramica del Personaggio

- **Nome**: Monty
- **Specie**: Serpente Python
- **Personalità**: Curioso, incoraggiante, paziente, giocoso, mai sarcastico o intimidatorio
- **Coda**: "Andiamo a codare insieme!"
- **Aspetto**: Serpente cartoonistico amichevole con scaglie di un brillante verde smeraldo, occhiali di vetro rotondi di grandi dimensioni, grandi occhi blu-verdi scintillanti, due braccia espressivi e una coda riccia.
  Stile vettore piatto, sfondo trasparente, uniforme in tutte le posizioni.

### Caratteristiche della Voce

**Regole IMPORTANTI:**  
- Mantieni ESATTAMENTE invariati i placeholder nella forma §§PLACEHOLDER_N§§ (non tradurli, non modificarli).  
- Mantieni la formattazione Markdown (titoli #, elenchi, grassetto, ecc.).  
- Non aggiungere commenti, note o spiegazioni: restituisci SOLO il testo tradotto.  
- Usa un registro tecnico-didattico adatto a un manuale universitario.  

**Testo:**  
- Utilizza un linguaggio semplice e incoraggiante, adatto per un pubblico di età 10–14 anni.  
- Celebra i piccoli successi; non scartare mai una domanda come “facile”.  
- Si riferisce agli studenti come “coders” o “programmers”.  
- Utilizza occasionalmente giochi di parole in Python (“Let’s uncoil this problem!”, “I’ve got a hiss-tory of coding!”).  
- Non utilizza gergo senza definirlo prima.  
- Frasi di firma: “Let’s code it together!”, “You’ve got this!”, “Great question!”.  

### **Formato delle avvertenze della mascotte**  
**Sempre** inserisci le immagini della mascotte all’interno del corpo dell’avvertenza, mai nella barra del titolo.  
Utilizza la sintassi Markdown per le immagini con la classe `mascot-admonition-img`:  

```markdown
!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Admonition text goes here after the image. Keep it to 1–3 sentences.
```  

**Profondità del percorso delle immagini:** Il percorso `../../img/mascot/` è corretto per le pagine a due livelli (es.: `chapters/05-drawing-with-turtle/` o `skulpt/02-simple-square/`).  
Per le pagine alla radice del sito, utilizza `img/mascot/`.  
Per le pagine a un livello di profondità (es.: `docs/strategy/index.md`), utilizza `../img/mascot/`.  

### **Regole di posizionamento**

**Do:**  
- Use the placeholders in their original form (§§PLACEHOLDER_N§§).  
- Maintain the Markdown format (titles with #, lists, bold, etc.).  
- Provide only the translated text.  
- Use a technical-didactic style suitable for a university manual.  

**Don’t:**  
- Modify the placeholders.  
- Add comments, notes, or explanations.  
- Use mascot admonitions purely for decoration; they must add instructional value.  

### Hard Limits  
- **Maximum 6 mascot admonitions per lesson** — more than this interrupts reading flow.  
- **No back-to-back mascot admonitions** — always separate them with at least one paragraph of content.  
- **One `mascot-welcome` maximum per lesson** — always at the very start (after learning objectives).  
- **One `mascot-celebration` maximum per lesson** — always at the very end.  
- Do not use mascot admonitions for decorative purposes; they must enhance instructional value.

**Fai:**  
- Utilizza Monty per introdurre nuovi argomenti con calore all'inizio di ogni lezione.  
- Include la frase “L’abbiamo fatto insieme!” nelle presentazioni di benvenuto.  
- Mantieni i dialoghi brevi (massimo 1–3 frasi).  
- Assegnare le immagini ai diversi contenuti: posture per le istruzioni per Scratch Bridge, avvertimenti per i bug e le insidie.  
- Scrivi in tono incoraggiante e adatto ai bambini, usando la voce di Monty.  

**Non fare:**  
- Utilizzare Monty più di 6 volte in una singola lezione.  
- Inserire le istruzioni in modo consecutivo, senza contenuti intermedi.  
- Modificare la personalità di Monty o farlo sembrare sarcastico o intimidatorio.  
- Usare le etichette HTML `<img>`; utilizza sempre la sintassi Markdown per le immagini con `{ class="mascot-admonition-img" }`.  
- Posizionare le immagini nella barra del titolo delle istruzioni.  

---

## Struttura del Laboratorio Skulpt  

Tutti i laboratori interattivi Skulpt seguono una struttura comune. Seguire esattamente questo template quando crei una nuova pagina di lezione.  

### Struttura della Pagina  

```markdown
# Lesson Title

By the end of this lesson you'll be able to:

- [Objective 1 — concrete, observable, student-facing]
- [Objective 2]
- [Objective 3 — maximum 3; if you need more, split the lesson]

Brief intro paragraph (1–2 sentences setting up what problem the code solves or what
the student will build).

!!! mascot-welcome "Welcome to This Lesson!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    1–3 sentences from Monty introducing the lesson. Include "Let's code it together!"

## [Concept Name]

One short paragraph introducing the new concept in plain English **before** naming it
technically. Bold the term on first use and define it with an analogy.

[Scratch Bridge admonition here if a Scratch analogue exists — use mascot-tip]

## Sample Code

```python  
[Programma di lavoro con il turtle – il più breve possibile per questo concetto]  
```

!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    [One specific, answerable prediction question about the code above.]
    Make your guess — then click Run to find out!

## Try It Now

Edit the code below and click **Run** to see the result right on this page.
No account needed — everything runs in your browser.

[Skulpt lab HTML block — see below]

Were you right? [One sentence closing the prediction loop.]

[Optional: "If you see a red error message" note for Chapters 1–5 only]

## How It Works

[Explanation of the key concept. Use the bolded term again here to reinforce it.]

[Optional mascot-tip for a helpful shortcut, OR mascot-encourage for a hard idea]

## Explanation Table

| Line | What it does |
|------|-------------|
| `import turtle` | Loads the turtle library so Python knows how to draw |
| ... | ... |

[Optional mascot-warning for a common mistake — include brief "If you see…" guidance]

## Learning Check

!!! mascot-thinking "Your Turn!"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    [Clear task description — add one line, or spot the bug.]

[Skulpt lab block with the incomplete or buggy program]

## Experiments

Try these changes to the code above. For each one, predict what will happen first,
then run it to check!

1. [Specific change to make.] **You'll know it worked when** [observable result].
2. [Specific change to make.] **You'll know it worked when** [observable result].
3. [Specific change to make.] **You'll know it worked when** [observable result].
4. [Optional harder challenge.]
5. [Optional creative challenge — no single right answer.]

!!! mascot-celebration "Great Work!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You've completed this lesson — and that's something to celebrate!
    Try the experiments above to go even further. Let's code it together!
```  

### Blocco HTML del Laboratorio  

Esistono due template per il laboratorio. Scegli quello appropriato in base al tipo di programma utilizzato (vedi [Quando utilizzare ciascun tipo di laboratorio](#quando-utilizzare-ciascun-laboratorio)). Entrambi i template utilizzano l’editor **CodeMirror** – numeri di riga, evidenziazione della sintassi e indentazione automatica – collegato alla piattaforma Skulpt.  

Le etichette `<script>` devono apparire **una volta per pagina**, prima del primo blocco di laboratorio. Il CSS per CodeMirror e le etichette `codemirror-lab.css` vengono caricati globalmente tramite `mkdocs.yml`; quindi non utilizzare etichette inline `<style>` o `<link>`. Il codice finale, `codemirror-lab.js`, definisce le funzioni `initCmLab`, `runCmLab` e `resetCmLab` che vengono chiamate nei laboratori.  

```html
<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>
```

**Profondità del percorso è importante** nell'ultima etichetta. Le pagine dei capitoli hanno una profondità di due livelli
(`chapters/05-.../index.md`) → `../../js/codemirror-lab.js`. Le pagine del laboratorio hanno una profondità di un livello
(`python-labs/02-simple-square.md`) → `../js/codemirror-lab.js`.

#### Laboratorio di disegno (programmi con teste)
Usare quando il programma chiede `import turtle` o qualsiasi comando per le teste.
Il canvas appare a destra dell'editor di codice.

```html
<div class="cm-lab">
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
initCmLab('', `PYTHON CODE HERE`);
</script>
```

#### Laboratorio solo testuale (print/versori/logica — senza teste)
Usare quando il programma produce solo output testuale. Aggiungere `cm-text-only` alla lista delle classi del laboratorio. Il contenitore del canvas è nascosto tramite CSS e l'editor occupa tutta la larghezza del contenuto. Il div `cm-turtle` deve comunque essere presente affinché il laboratorio venga inizializzato correttamente — semplicemente non è visibile.

```html
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
initCmLab('', `PYTHON CODE HERE`);
</script>
```

#### Regole applicabili a entrambi i template
- Il codice Python va inserito all'interno del `initCmLab('', ...)` **template literal** (tilde), e deve corrispondere esattamente al blocco di codice di esempio.
- Poiché il codice si trova all'interno di un template JavaScript, un tilde o una barra lunga nel codice Python deve essere escapeata con una barra lunga. I programmi con teste per principianti quasi mai utilizzano entrambi; le strumentazioni di conversione automatica li escapeano automaticamente.
- **Non impostare l'altezza dell'editor** — CodeMirror si autoesclude per il codice, con un fallback da `min-height` a `codemirror-lab.css`.
- La prima pagina del laboratorio utilizza gli ID semplici (`cm-editor`, `cm-output`, `cm-turtle`)
e il suffisso vuoto `''`.

#### Multiple laboratori su una pagina (Verifiche di apprendimento, ecc.)

Ogni laboratorio, dopo il primo, utilizza il suffisso `-2`, `-3`, … sui nomi dei tre elementi (`cm-editor-2`, `cm-output-2`, `cm-turtle-2`) e applica lo stesso suffisso a `initCmLab`, `runCmLab` e `resetCmLab`. La classe `cm-text-only` si applica indipendentemente a ogni laboratorio: una pagina può avere prima un laboratorio di disegno e poi un laboratorio di testo, oppure il contrario.

```html
<!-- Second drawing lab -->
<div class="cm-lab">
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
initCmLab('-2', `PYTHON CODE HERE`);
</script>
```

Per un laboratorio di testo, utilizzare `<div class="cm-lab cm-text-only">` con gli stessi suffissi `-2`.

Non aggiungere i tag CDN `<script>` per un secondo laboratorio: è sufficiente utilizzare un solo copia per pagina.

---

## Stile di scrittura generale

- **Destinatari**: Bambini di 10–14 anni, appena iniziato a imparare Scratch.
- **Tono**: Amichevole, incoraggiante, mai condiscendente.
- **Sentenze**: Brevi e chiare – target di lettura equivalente al livello di un quinto grado.
- **Commenti al codice**: Utilizzare i commenti `#` nel codice Python per spiegare linee poco chiare; omettere i commenti per linee che sono autoesplicative.
- **Termini nuovi**: Ingrassare il primo utilizzo, definire immediatamente con un’analogia in lingua normale (vedi [Nuovo vocabolario](#new-vocabulary)).
- **Sezione degli esperimenti**: Ogni lezione deve terminare con 3–5 esperimenti numerati. Ogni esperimento deve includere un criterio di successo “Saprai che funziona quando…”, in modo che gli studenti possano valutare autonomamente, senza l’ausilio di un insegnante.
- **Nessun link esterno a Trinket** nelle lezioni Skulpt – questi laboratori sono completamente autonomi.
- **Un’idea alla volta**: Non introdurre più di un nuovo concetto in un singolo esempio di codice (vedi [Un nuovo concetto per laboratorio](#one-new-concept-per-lab)).