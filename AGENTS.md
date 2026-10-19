# Introduzione a Python — Istruzioni per il progetto

## Filosofia didattica di base

**Lo strumento principale per l'insegnamento nei Capitoli 1–18 sono le grafiche interattive in formato turtle, supportate da Skulpt.**

Ogni lezione nei primi capitoli deve includere almeno un laboratorio con Skulpt, in cui lo studente può:
1. **Leggere** un breve programma Python funzionante
2. **Esecutarlo** immediatamente nel browser (senza installazione, senza account)
3. **Modificarlo** — cambiando un numero, un colore, una direzione — e eseguirlo di nuovo

Questo ciclo di “vedere, eseguire, modificare” è il cuore di questo manuale. È ciò che lo distingue da una semplice riferimento e lo rende utilizzabile nei club di programmazione o nelle aule.

### Prevedere prima di eseguire

Prima di ogni laboratorio con Skulpt, chiedete allo studente di **prevedere cosa farà il programma** prima di cliccare su “Eseguire”. Questa abitudine — fermarsi a riflettere sul codice prima di eseguirlo — è una delle competenze più importanti che un programmatore principiante può sviluppare.

Monty organizza le previsioni utilizzando `mascot-thinking`:

```markdown
!!! mascot-thinking "What Do You Think Will Happen?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you click Run, look at the program below.
    How many sides do you think the turtle will draw?
    Make your guess, then run it to find out!
```

**Regole per le domande di previsione:**
- Chiedete una domanda specifica e risolvibile (disegno del modello, numero di linee stampate, colore utilizzato, numero di volte che il ciclo si ripete, ecc.) — non una domanda aperta del tipo “cosa succede?”
- Posizionate la domanda di previsione `mascot-thinking` **immediatamente sopra** il blocco del laboratorio con Skulpt, prima che lo studente possa eseguire il codice
- Dopo il laboratorio, aggiungete una breve frase “Hai indovinato?” in prosa per chiudere il ciclo — non è necessario un secondo avvertimento
- Mantenete la domanda di previsione a un livello di difficoltà tale che circa la metà degli studenti possa indovinare correttamente al primo tentativo — troppo facile non crea abitudine, troppo difficile scoraggia le previsioni

### Verifiche di apprendimento

**Struttura del Capitolo**

38 capitoli che coprono 452 concetti, tutti verificati per 0 violazioni delle regole di dipendenza.  
I file dei capitoli si trovano in `docs/chapters/##-slug/index.md`.  
L’assegnazione dei concetti è la fonte di verità per cui i concetti appartengono a determinati luoghi.  

## MkDocs  

- NON aggiungere `- navigation.tabs` al file mkdocs.yml.  
- Non iniziare né terminare il processo relativo a `mkdocs serve` – l’utente lo esegue direttamente nel proprio terminale.