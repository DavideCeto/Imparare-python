---
title: "Informazioni su questo libro"
description: "Informazioni su *Beginning Python* — la sua storia, scopo, pubblico, design e il team che lo ha creato."
---

# Informazioni su questo libro

## Benvenuto da Monty

!!! mascot-welcome "Benvenuto!"
    ![Monty waving welcome](./img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ciao, sono Monty! Sono stato tra le pagine di questo libro fin dall'inizio, guidando gli studenti
    dalle prime nozioni fino a concetti avanzati come reti neurali e algoritmi per la risoluzione
    dei labirinti. Questo libro è il mio ambiente di lavoro, e sono felice che tu sia qui.
    Che tu sia completamente nuovo al linguaggio Python o che tu stia cercando un modo per migliorare le
    tue competenze, sarò al tuo fianco in ogni fase del percorso. Cominciamo insieme a creare
    qualcosa di fantastico!

---

## Una nota sulla storia della piattaforma

Questo libro ha una storia, e questa storia è importante per capire perché è stato creato
nella forma in cui lo abbiamo oggi.

***Beginning Python** è stato creato nel 2020 da Dan McCreary come risorsa didattica volontaria per
[CoderDojo Twin Cities](https://www.coderdojotc.org/), un club di programmazione gratuito gestito
da comunità. Le lezioni iniziali utilizzavano **Trinket.io** — una popolare sandbox basata sul browser
che permetteva agli studenti di scrivere e eseguire programmi Python senza dover installare
nulla sul loro computer. Dal 2020 al 2025, Trinket ha fornito centinaia di esempi di codice
interattivi in questo libro, contribuendo molto alla comunità di CoderDojo.

Nel 2026, Trinket ha annunciato che avrebbe **chiuso permanentemente all’inizio di agosto 2026**:

> *"Trinket si conterà all’inizio di agosto 2026. Dopo questa data, trinket.io non sarà più
> disponibile, e non potrete accedere ai vostri trinket, ai corsi o a qualsiasi altro contenuto
> presente su questo sito."*

Questa è stata una significativa interruzione. Ogni laboratorio incorporato in questo libro è diventato un link morto.  
Sono passate settimane di ricerca per trovare un sostituto. **Pickcode.io** era l’alternativa più promettente, ma si è rivelata insufficiente: presentava errori di rendering, supporto limitato per le grafiche con il programma “turtle”, e limitava l’accesso ai utenti gratuiti a soli cinque programmi, numero decisamente insufficiente per un corso incentrato su esercizi di disegno visivi e pratici.  
Dopo aver valutato le alternative, si è deciso di riscrivere il libro da zero utilizzando **[Skulpt](https://skulpt.org/)** – una implementazione Python open-source autoinstallata che funziona interamente nel browser. Skulpt non ha dipendenze esterne, non richiede account specifici, non ha limitazioni per gli utenti gratuiti, e offre un supporto completo per il modulo `turtle` di Python. Ogni laboratorio presente in questo libro è incorporato direttamente nella pagina web; il ambiente di programmazione interattiva funzionerà comunque finché la pagina stessa viene caricata.  
Inoltre, il libro è stato ufficialmente rinominato, passando da “CoderDojo” a “Beginning Python”, in linea con la sua missione di diventare una risorsa educativa aperta per qualsiasi studente, aula o club di programmazione che desidera un’introduzione gratuita e completa a Python.  
  
## Perché questo manuale di programmazione intelligente  
Python è il linguaggio di programmazione più popolare al mondo – e lo è da anni. È alla base di importanti progressi nel campo della data science, dell’intelligenza artificiale, della computational science, dello sviluppo web, e della comunità dei Raspberry Pi e dei Maker. Tuttavia, la maggior parte delle risorse disponibili per i principianti di Python presuppone che gli studenti sappiano già come installare software, o che siano studenti adulti disposti a leggere documentazioni tecniche. I programmatori principianti tra i 10 e i 13 anni meritano di meglio.

**Negli Stati Uniti (2025–2026):**

- Il Python è la **lingua più utilizzata** nelle scuole K–12 negli Stati Uniti, secondo l’ultima indagine della Computer Science Teachers Association[^1].
- Il U.S. Bureau of Labor Statistics prevede un **incremento del 25%** nel numero di posti di lavoro legati allo sviluppo software e alla qualità dei testi entro il 2032; la maggior parte di questi posti utilizza il Python come linguaggio principale[^2].
- Solo **il 57% delle scuole superiori negli Stati Uniti** offre almeno un corso di informatica, lasciando milioni di studenti senza alcuna esperienza pratica con la programmazione prima dell’università[^3].
- Secondo l’indagine di Stack Overflow del 2024, il Python è la lingua più utilizzata dai sviluppatori per il quinto anno consecutivo, utilizzata da **51% dei rispondenti**[^4].

**A livello mondiale:**

- L’indice dei pacchetti di Python (PyPI) ospita più di **550.000 pacchetti**, rendendolo il più grande ecosistema di codice riutilizzabile in qualsiasi linguaggio di programmazione[^5].
- Il mercato globale degli strumenti e dell’educazione legati al Python è valutato in oltre **8 miliardi di dollari** e cresce con un tasso annuo del 25%[^6].

Questi numeri rappresentano milioni di giovani apprendenti che hanno bisogno di un percorso di apprendimento accessibile e pratico: un percorso che si adatti alle loro esigenze, utilizzi strumenti che non richiedono installazioni o account personali, e che insegna attraverso progetti visivi e pratici, piuttosto che attraverso esercizi di sintassi noiosa.

Questo libro adotta un approccio fondamentalmente diverso. È basato su una **grafica di apprendimento** composta da 450 concetti interconnessi, verificati attraverso 38 capitoli. Ogni concetto viene presentato soltanto dopo che i prerequisiti necessari sono stati affrontati. Ogni capitolo iniziale include **Skulpt labs** – editori di Python completamente interattivi, integrati direttamente nel browser, senza bisogno di account o installazioni. Gli studenti eseguono il codice, lo modificano e vedono i risultati immediatamente. Monty, la mascotte del libro, fornisce incoraggiamenti, indicazioni e previsioni a ogni passo. L’intero libro è **open source e gratuito** – senza barriere di pagamento, senza codici di accesso, senza aggiornamenti annuali.

---

## Come utilizzare questo libro

Questo libro è progettato per un apprendimento a ritmo personale, partendo da zero e sviluppando una vera e propria padronanza del Python. Ogni capitolo si basa sul materiale precedente, quindi si consiglia di leggere in ordine, soprattutto per i capitoli 1–18, dove i grafici visivi forniscono la base per l’apprendimento.

Il libro include:

- **[38 Capitoli](./chapters/index.md)** che trattano della sintassi di base di Python, grafica con turtle, flusso di controllo, funzioni, collezioni, programmazione orientata agli oggetti, algoritmi, visualizzazione dei dati, NumPy, elaborazione delle immagini e un’introduzione al machine learning.
- **[Skulpt Labs](./python-labs/index.md)** integrati nei capitoli: editor di Python completamente interattivi che si eseguono nel browser, senza bisogno di installazione o account.
- **Quiz** alla fine di ogni capitolo per testare la comprensione e la memorizzazione.
- **Riferimenti annotati** che linkano a Wikipedia, documentazione di Python e fonti autorevoli.
- **[Glossario](./glossary.md)** con definizioni per ogni concetto chiave, scritto a un livello di lettura accessibile.
- **[FAQ](./faq.md)** che rispondono alle domande comuni degli studenti che passano da una programmazione basata su blocchi a una programmazione orientata agli oggetti.
- **[Grapha di Apprendimento](./learning-graph/index.md)** che visualizza le 450 dipendenze tra i concetti nel corso.
- **[Guida per Insegnanti](./teachers-guide/index.md)** con raccomandazioni sul ritmo di apprendimento, domande per la discussione e in linea con gli standard del CSTA.
- **Cerca** disponibile da qualsiasi pagina utilizzando la barra di ricerca in alto.

La [Grapha di Apprendimento](learning-graph/index.md) è particolarmente utile se si desidera esplorare in modo non lineare o verificare i prerequisiti per un concetto specifico: mostra esattamente come le idee sono collegate e quali capitoli le introducono.

!!! Consiglio della mascotte "Dove iniziare"
    ![Monty offering a tip](./img/mascot/tip.png){ class="mascot-admonition-img" }
    Se non hai mai scritto in Python, inizia dal Capitolo 1 e procedi avanti.
    Se hai già esercitato in Python ma desideri rafforzare le tue basi, consulta la [Grapha di Apprendimento](learning-graph/index.md) per scoprire esattamente dove iniziare.
    Io sarò lì per guidarti, in qualsiasi momento!

---

## Informazioni sull'autore

![Dan McCreary headshot](./img/dan-headshot-small.png){ width="150px" align="right"}

Dan McCreary è un ricercatore di intelligenza artificiale, architetto di soluzioni e educatore semi-retroattivo, che ha trascorso più di tre decenni aiutando le organizzazioni del Fortune 100 a ragionare su grandi dataset. All’Optum ha fondato il Generative AI Center of Excellence e ha guidato il team che ha costruito uno dei più grandi grafi di conoscenza nel settore sanitario al mondo, che comprende oltre 25 miliardi di vertici, al fine di unificare le informazioni riguardanti membri, fornitori e pazienti. La profonda conoscenza di Dan nella rappresentazione della conoscenza e nel pensiero sistemico costituisce la base per i grafi di apprendimento precisi e le procedure intelligenti per la creazione di libri di testo.

È coautore del libro *Making Sense of NoSQL* (Manning Publications), presidente fondatore della conferenza NoSQL Now!, e un oratore frequente su temi come ricerca semantica, strategie di ontologia e hardware per l’intelligenza artificiale. Oltre che nel settore industriale, Dan ha fornito consulenza agli studenti come volontario STEM dal 2014 attraverso CoderDojo Twin Cities, e ora applica lo stesso rigoroso approccio utilizzato a livello aziendale nella creazione di risorse educative aperte per giovani apprendenti. È possibile visitare la [sezione Case Studies dei Intelligent Textbooks](https://dmccreary.github.io/intelligent-textbooks/case-studies/) per vedere oltre 87 libri di testo creati da Dan o co-creati con altri autori.

**Credenziali**
- Laurea in Fisica e Informatica presso il Carleton College
- Master in Scienze dell’Educazione presso l’Università del Minnesota
- Corso di MBA presso l’Università di St. Thomas
- Detentore di brevetti per tecniche di ricerca semantica e gestione di ontologie
- Promotore dell’adozione di grafi di conoscenza su larga scala nel settore sanitario e educativo
- Fondatore di iniziative volte a creare esperienze di apprendimento accessibili e a basso costo per gli studenti delle scuole primarie e secondarie

---

## Come citare questo libro

Seguendo questo libro di testo, se lo si cita in opere accademiche, proposte di curriculum, piani di lezione o altre pubblicazioni, si deve utilizzare uno dei seguenti formati di citazione.

**APA (7ª edizione)**  
McCreary, D. (2026). *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/

**Chicago (17ª edizione)**  
McCreary, Dan. 2026. *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/

**MLA (9ª edizione)**  
McCreary, Dan. *Beginning Python: From Blocks to Code with Monty*. 2026, dmccreary.github.io/python/

**BibTeX**  
```bibtex
@book{mccreary2026python,
  title     = {Beginning Python: From Blocks to Code with Monty},
  author    = {McCreary, Dan},
  year      = {2026},
  url       = {https://dmccreary.github.io/python/},
  note      = {Interactive intelligent textbook with Skulpt inline Python labs}
}
```

Per citare un capitolo specifico, si deve aggiungere il numero del capitolo e il titolo — ad esempio:  
McCreary, D. (2026). Capitolo 1: Benvenuto in Python e Skulpt. In *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/chapters/01-welcome-to-python/

---

## Licenza  
Questo lavoro è rilasciato sotto la  
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).  
È libero di condividere e adattare il materiale per scopi non commerciali, purché si fornisca il dovuto credito e si adattino le modifiche sotto la stessa licenza.

---

## Riferimenti  
[^1]: Computer Science Teachers Association. (2023). *State of K-12 Computer Science Education*. https://advocacy.code.org/stateofcs  
[^2]: U.S. Bureau of Labor Statistics. (2024). *Occupational Outlook Handbook: Software Developers, Quality Assurance Analysts, and Testers*. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm  
[^3]: Code.org. (2024). *2024 State of Computer Science Education: Laying the Groundwork*. https://advocacy.code.org/2024_state_of_cs.pdf

[^4]: Stack Overflow. (2024). *2024 Developer Survey*. https://survey.stackoverflow.co/2024/

[^5]: Python Package Index. (2026). *PyPI Statistics*. https://pypi.org/

[^6]: Grand View Research. (2024). *Python Web Frameworks Market Size, Share & Trends Analysis Report*. https://www.grandviewresearch.com/industry-analysis/python-web-framework-market-report