---
title: "Informazioni su questo libro"
description: "Informazioni su Beginning Python: la sua storia, lo scopo, il pubblico, il progetto e le persone che lo hanno realizzato."
---

# Informazioni su questo libro

## Il benvenuto di Monty

!!! mascot-welcome "Benvenuto!"
    ![Monty waving welcome](./img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ciao, sono Monty! Vivo in queste pagine fin dall'inizio e accompagno gli studenti
    dal loro primo `print("Hello!")` fino alle reti neurali e agli algoritmi che
    risolvono i labirinti. Questo libro è la mia casa, e sono felicissimo che tu sia qui.
    Che tu sia alle prime armi con Python o che tu stia cercando un posto per salire di livello,
    sarò al tuo fianco a ogni passo. Programmiamo insieme qualcosa di fantastico!

---

## Una nota sulla storia della piattaforma

Questo manuale ha una storia, ed è una storia importante per capire perché oggi è costruito così.

**Beginning Python** è stato creato nel 2020 da Dan McCreary come risorsa didattica, realizzata
da volontario, per [CoderDojo Twin Cities](https://www.coderdojotc.org/), un club di
programmazione gratuito per ragazzi gestito dalla comunità. Le prime lezioni usavano
**Trinket.io**, un popolare ambiente Python nel browser che permetteva agli studenti di
scrivere ed eseguire programmi Python senza installare nulla sul proprio computer. Dal 2020 al
2025 Trinket ha fatto funzionare centinaia di esempi di codice interattivi di questo libro, ed è
stato molto utile alla comunità di CoderDojo.

Nel 2026 Trinket ha annunciato che avrebbe
**[chiuso definitivamente all'inizio di agosto 2026](https://trinket.io/announcement)**:

> *"Trinket chiuderà all'inizio di agosto 2026. Dopo questa data trinket.io non sarà più
> disponibile e non potrai più accedere ai tuoi trinket, ai corsi o a qualsiasi contenuto di
> questo sito."*

È stato un duro colpo. Tutti i laboratori Trinket incorporati nel libro sono diventati link non
funzionanti. Sono seguite settimane di ricerca di un sostituto. **Pickcode.io** era
l'alternativa più promettente, ma si è rivelata inadeguata: aveva problemi di visualizzazione,
un supporto limitato alla grafica turtle e, per gli utenti del piano gratuito, un limite di
appena cinque programmi turtle: troppo pochi per un corso costruito attorno a esercizi di
disegno visivi e pratici.

Dopo aver valutato le alternative, si è deciso di riscrivere il libro da zero attorno a
**[Skulpt](https://skulpt.org/)**, un'implementazione di Python open source, ospitata
direttamente insieme al sito, che funziona interamente nel browser. Skulpt non ha dipendenze
esterne, non richiede account, non ha limiti da piano gratuito e supporta completamente il
modulo `turtle` di Python. Ogni laboratorio di questo libro è incorporato direttamente nella
pagina (il motore Skulpt abbinato all'editor CodeMirror, che aggiunge i numeri di riga e
l'evidenziazione della sintassi), quindi l'ambiente di programmazione interattivo continuerà a
funzionare finché la pagina stessa si carica.

In quell'occasione il libro ha anche cambiato ufficialmente nome: dalla sua identità legata a
CoderDojo è diventato **Beginning Python**, a riflettere la sua missione più ampia di risorsa
educativa aperta per qualsiasi studente, classe o club di programmazione che voglia
un'introduzione a Python gratuita e completa.

---

## Perché questo manuale intelligente

Python è il linguaggio di programmazione più popolare al mondo, e lo è da anni. È alla base di
scoperte nella data science, nell'intelligenza artificiale, nel calcolo scientifico, nello
sviluppo web e nella comunità di Raspberry Pi e dei Maker. Eppure la maggior parte delle risorse
per imparare Python presuppone che gli studenti sappiano già installare un software, oppure che
siano adulti a proprio agio con la documentazione tecnica. I programmatori alle prime armi tra i
10 e i 13 anni meritano di meglio.

**Negli Stati Uniti (2025–2026):**

- Python è il **linguaggio più insegnato** nelle scuole K–12 (dalla primaria alla secondaria)
  degli Stati Uniti, secondo l'indagine più recente della Computer Science Teachers Association
  sullo stato dell'informatica nella scuola[^1]
- Lo U.S. Bureau of Labor Statistics prevede una **crescita del 25%** dei posti di lavoro per
  sviluppatori software e per il controllo qualità del software (quality assurance) fino al
  2032; la maggior parte di questi lavori usa Python come linguaggio principale[^2]
- Solo il **57% delle scuole superiori statunitensi** offre almeno un corso di informatica,
  lasciando milioni di studenti senza alcun contatto con la programmazione in classe prima
  dell'università[^3]
- Il Developer Survey 2024 di Stack Overflow ha rilevato che **Python è il linguaggio più usato**
  dagli sviluppatori per il quinto anno consecutivo, usato dal **51% di tutti gli intervistati**[^4]

**Nel mondo:**

- L'indice dei pacchetti di Python (PyPI) ospita più di **550.000 pacchetti**, ed è quindi il
  più grande ecosistema di codice riutilizzabile di qualsiasi linguaggio di programmazione[^5]
- Il mercato mondiale degli strumenti per sviluppatori e della formazione legati a Python vale
  oltre **8 miliardi di dollari** e cresce del 25% all'anno[^6]

Questi numeri rappresentano milioni di giovani che hanno bisogno di una rampa di accesso davvero
alla loro portata: che parta da dove sono già (la programmazione a blocchi), che usi strumenti
che funzionano senza installazioni né account e che insegni attraverso progetti visivi e pratici
invece che con aridi esercizi di sintassi.

Questo libro segue un approccio radicalmente diverso. È costruito su un **grafo di
apprendimento di 450 concetti collegati tra loro**, verificato su 38 capitoli, in cui ogni
concetto viene introdotto solo dopo i suoi prerequisiti. Ogni capitolo iniziale include dei
**laboratori Skulpt**: editor Python completamente interattivi incorporati direttamente nel
browser, senza account né installazioni. Gli studenti eseguono il codice, lo modificano e vedono
subito i risultati. Monty, la mascotte, offre incoraggiamenti, suggerimenti e domande di
previsione a ogni passo. L'intero manuale è **open source e gratuito**: niente paywall, niente
codici di accesso, niente nuove edizioni da comprare ogni anno.

---

## Come usare questo libro

Questo manuale è pensato per lo studio al proprio ritmo: parte da zero e arriva a una vera
padronanza di Python. Ogni capitolo si basa sul materiale precedente, quindi è consigliato
leggerlo in ordine, soprattutto per i capitoli 1–18, dove la grafica turtle fornisce la base
visiva.

Il libro comprende:

- **[38 capitoli](./chapters/index.md)** che trattano la sintassi di base di Python, la grafica turtle, il controllo del flusso, le funzioni,
  le collezioni, la programmazione orientata agli oggetti, gli algoritmi, la visualizzazione dei dati, NumPy,
  l'elaborazione delle immagini e un'introduzione al machine learning
- **[Laboratori Skulpt](./python-labs/index.md)** incorporati nei capitoli: editor Python completamente interattivi che funzionano nel
  tuo browser, senza installazioni né account
- **Quiz** alla fine di ogni capitolo per verificare la comprensione e la memorizzazione
- **Riferimenti commentati** con link a Wikipedia, alla documentazione di Python e ad altre fonti autorevoli
- **[Glossario](./glossary.md)** con le definizioni di tutti i concetti chiave, scritte in un linguaggio accessibile
- **[Domande frequenti](./faq.md)** che rispondono ai dubbi più comuni di chi passa dalla programmazione a blocchi
- **[Grafo di apprendimento](./learning-graph/index.md)** che mostra tutte le 450 dipendenze tra i concetti del corso
- **[Guida per gli insegnanti](./teachers-guide/index.md)** con indicazioni sui tempi, domande di discussione e allineamento agli standard CSTA
- **Ricerca** disponibile da ogni pagina tramite la barra di ricerca in alto

Il [grafo di apprendimento](learning-graph/index.md) è particolarmente utile se vuoi esplorare
il corso senza seguire l'ordine o controllare i prerequisiti di un concetto specifico: mostra
esattamente come sono collegate le idee e in quali capitoli vengono introdotte.

!!! mascot-tip "Da dove cominciare"
    ![Monty offering a tip](./img/mascot/tip.png){ class="mascot-admonition-img" }
    Se non hai mai scritto codice Python, comincia dal Capitolo 1 e vai avanti in ordine.
    Se hai già usato un po' Python ma vuoi rafforzare le basi, guarda il
    [grafo di apprendimento](learning-graph/index.md) per trovare esattamente da dove partire.
    In ogni caso, io sarò lì a guidarti!

---

## L'autore

![Dan McCreary headshot](./img/dan-headshot-small.png){ width="150px" align="right"}

Dan McCreary è un ricercatore nel campo dell'intelligenza artificiale, solution architect ed
educatore, oggi in semi-pensione, che per oltre trent'anni ha aiutato aziende della Fortune 100
a ragionare su enormi quantità di dati. In Optum ha fondato il Generative AI Center of
Excellence e ha guidato il team che ha costruito uno dei più grandi grafi di conoscenza
sanitari al mondo (oltre 25 miliardi di vertici), per unificare le informazioni su iscritti,
fornitori di servizi e pazienti. La sua profonda esperienza nella rappresentazione della
conoscenza e nel pensiero sistemico è alla base dei grafi di apprendimento precisi e dei
processi di creazione dei manuali intelligenti usati in tutto questo corso.

È coautore di *Making Sense of NoSQL* (Manning Publications), è stato il primo presidente della
conferenza NoSQL Now! ed è spesso relatore principale su ricerca semantica, strategia delle
ontologie e hardware per l'intelligenza artificiale. Al di fuori del lavoro, dal 2014 Dan fa da
mentore agli studenti come volontario STEM con CoderDojo Twin Cities, e oggi applica lo stesso
rigore usato su scala aziendale alla creazione di risorse educative aperte per i più giovani.
Puoi visitare gli
[Intelligent Textbooks Case Studies](https://dmccreary.github.io/intelligent-textbooks/case-studies/)
per vedere gli oltre 87 manuali che Dan ha creato da solo o insieme ad altri autori.

**Titoli e riconoscimenti principali**

- Laurea (B.A.) in Fisica e Informatica al Carleton College
- Laurea magistrale in Ingegneria Elettrica (M.S.E.E.) all'Università del Minnesota
- Corsi di MBA all'University of St. Thomas
- Titolare di brevetti su tecniche di ricerca semantica e di gestione delle ontologie
- Sostenitore dell'adozione su larga scala degli Enterprise Knowledge Graph nella sanità e nell'istruzione
- Da tempo promotore di esperienze di apprendimento basate sull'intelligenza artificiale, accessibili e a basso costo, per gli studenti K–12

---

## Come citare questo libro

Se citi questo manuale in lavori accademici, proposte di curricolo, piani di lezione o altre
pubblicazioni, usa uno dei seguenti formati di citazione.

**APA (7ª edizione)**

McCreary, D. (2026). *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/

**Chicago (17ª edizione)**

McCreary, Dan. 2026. *Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/.

**MLA (9ª edizione)**

McCreary, Dan. *Beginning Python: From Blocks to Code with Monty*. 2026, dmccreary.github.io/python/.

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

Per citare un capitolo specifico, aggiungi il numero e il titolo del capitolo, per esempio:

McCreary, D. (2026). Chapter 1: Welcome to Python and Skulpt. In
*Beginning Python: From Blocks to Code with Monty*. https://dmccreary.github.io/python/chapters/01-welcome-to-python/

---

## Licenza

Quest'opera è distribuita con licenza
[Creative Commons Attribuzione - Non commerciale - Condividi allo stesso modo 4.0
Internazionale (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Sei libero di condividere e adattare il materiale per scopi non commerciali, a condizione di
citare adeguatamente la fonte e di condividere i tuoi adattamenti con la stessa licenza.

---

## Riferimenti

[^1]: Computer Science Teachers Association. (2023). *State of K-12 Computer Science Education*. https://advocacy.code.org/stateofcs

[^2]: U.S. Bureau of Labor Statistics. (2024). *Occupational Outlook Handbook: Software Developers, Quality Assurance Analysts, and Testers*. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm

[^3]: Code.org. (2024). *2024 State of Computer Science Education: Laying the Groundwork*. https://advocacy.code.org/2024_state_of_cs.pdf

[^4]: Stack Overflow. (2024). *2024 Developer Survey*. https://survey.stackoverflow.co/2024/

[^5]: Python Package Index. (2026). *PyPI Statistics*. https://pypi.org/

[^6]: Grand View Research. (2024). *Python Web Frameworks Market Size, Share & Trends Analysis Report*. https://www.grandviewresearch.com/industry-analysis/python-web-framework-market-report
