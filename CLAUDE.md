# Introduzione a Python — Istruzioni per il progetto

## Filosofia didattica di base

**Lo strumento principale per l'insegnamento nei Capitoli 1–18 sono le grafiche interattive in formato turtle, supportate da Skulpt.**

Ogni lezione nei primi capitoli deve includere almeno un laboratorio con Skulpt, in cui lo studente può:
1. **Leggere** un breve programma Python funzionante
2. **Eseguirlo** immediatamente nel browser (senza installazione, senza account)
3. **Modificarlo** — cambiando un numero, un colore, una direzione — ed eseguirlo di nuovo

Questo ciclo di “vedere, eseguire, modificare” è il cuore di questo manuale. È ciò che lo distingue da un semplice riferimento e lo rende utilizzabile nei club di programmazione o nelle aule.

### Prevedere prima di eseguire

Prima di ogni laboratorio con Skulpt, chiedete allo studente di **prevedere cosa farà il programma** prima di cliccare su “Eseguire”. Questa abitudine — fermarsi a riflettere sul codice prima di eseguirlo — è una delle competenze più importanti che un programmatore principiante può sviluppare.

Monty organizza le previsioni utilizzando `mascot-thinking`:

```markdown
!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di cliccare su Run, guarda il programma qui sotto.
    Quanti lati pensi che disegnerà la tartaruga?
    Fai la tua ipotesi, poi eseguilo per scoprirlo!
```

**Regole per le domande di previsione:**
- Chiedete una domanda specifica e risolvibile (disegno del modello, numero di linee stampate, colore utilizzato, numero di volte che il ciclo si ripete, ecc.) — non una domanda aperta del tipo “cosa succede?”
- Posizionate la domanda di previsione `mascot-thinking` **immediatamente sopra** il blocco del laboratorio con Skulpt, prima che lo studente possa eseguire il codice
- Dopo il laboratorio, aggiungete una breve frase “Hai indovinato?” in prosa per chiudere il ciclo — non è necessario un secondo avvertimento
- Mantenete la domanda di previsione a un livello di difficoltà tale che circa la metà degli studenti possa indovinare correttamente al primo tentativo — troppo facile non crea abitudine, troppo difficile scoraggia le previsioni

### Verifiche di apprendimento

Per ogni concetto importante, includete almeno una **Verifica di apprendimento** — un laboratorio con Skulpt in cui:
- Il programma è **quasi completo** ma manca una riga chiave che lo studente deve aggiungere, OPPURE
- Il programma contiene un **piccolo bug intenzionale** che lo studente deve trovare e correggere

Le verifiche di apprendimento devono essere chiaramente etichettate e introdotte da Monty, così che gli studenti capiscano che viene chiesto loro di ragionare, non solo di leggere. Usate `mascot-thinking` per le sfide “aggiungi la riga mancante” e `mascot-warning` per le sfide “trova il bug”.

**Formato della Verifica di apprendimento:**
```markdown
!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna tre lati di un quadrato, ma si ferma prima.
    Aggiungi **una riga** per fargli disegnare il quarto lato e completare la figura!
```

Subito dopo deve seguire un laboratorio con Skulpt il cui editor contiene il programma incompleto o con il bug.

## Linee guida per la generazione dei contenuti

**Leggete `CONTENT-GENERATION-GUIDELINES.md` prima di generare qualsiasi contenuto destinato agli studenti.**

Quel file è la fonte di riferimento per:
- L'uso di Monty, la mascotte di Python (tipi di avvertimento, percorsi delle immagini, regole di posizionamento, limiti rigidi)
- La struttura HTML dei blocchi dei laboratori Skulpt e gli ID degli elementi obbligatori
- Lo stile di scrittura generale (pubblico di 10–14 anni, che arriva da Scratch, tono incoraggiante)

Regole chiave da tenere sempre a mente:

- **Al massimo 6 avvertimenti della mascotte per lezione** — mai uno subito dopo l'altro
- **Aprite sempre con `mascot-welcome`** e **chiudete con `mascot-celebration`**
- **La profondità del percorso delle immagini è importante**: i capitoli si trovano due livelli più in basso → usate `../../img/mascot/`
- **Non usate mai i tag `<img>`** — usate sempre `![alt](path){ class="mascot-admonition-img" }`
- **Gli ID dei laboratori CodeMirror sono fissi** — `codemirror-lab.js` dipende da `cm-editor`, `cm-output` e `cm-turtle` (con i suffissi `-2`… per i laboratori successivi); non rinominateli
- I contenuti destinati agli insegnanti (guida per gli insegnanti, descrizione del corso) NON usano la mascotte

## Struttura dei capitoli

38 capitoli che coprono 452 concetti, tutti verificati per 0 violazioni delle regole di dipendenza.
I file dei capitoli si trovano in `docs/chapters/##-slug/index.md`.
L'assegnazione dei concetti ai capitoli è la fonte di verità per stabilire a quale capitolo appartiene ogni concetto.

## MkDocs

- NON aggiungere `- navigation.tabs` al file mkdocs.yml.
- Non avviare né terminare `mkdocs serve` — l'utente lo esegue direttamente nel proprio terminale.
