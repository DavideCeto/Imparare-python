---
title: Esploratore degli Indici di Lista
description: Clicca su append, insert e pop e guarda una lista di scatole colorate riformarsi sul posto - gli indici si rinumerano dal vivo, e un Test Stringa mostra il TypeError che le stringhe danno invece.
image: /sims/list-index-explorer/list-index-explorer.png
og:image: /sims/list-index-explorer/list-index-explorer.png
twitter:image: /sims/list-index-explorer/list-index-explorer.png
social:
   cards: false
quality_score: 93
---

# Esploratore degli Indici di Lista

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore degli Indici di Lista a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli studenti leggono che le liste "cambiano sul posto" ma non vedono mai le
scatole spostarsi. Qui ogni operazione è un click: `append()` allunga la
fine, `insert(1, ...)` si incunea dentro e fa scorrere tutto verso destra,
`pop()` accorcia la coda — ed entrambe le righe di indici, positivi e
negativi, si rinumerano davanti ai loro occhi, con la riga Python esatta
mostrata per ogni cambiamento. Il pannello **Test Stringa** mostra il vero
`TypeError` che una stringa solleva per lo stesso cambiamento sul posto,
rendendo concreta la divisione tra mutabile e immutabile.

**Obiettivo di apprendimento:** Lo studente sarà in grado di selezionare
elementi tramite indice positivo e negativo e di dimostrare come append,
insert e pop riformino una lista sul posto.

- **Tassonomia di Bloom (2001):** Applicare → Analizzare — *usare,
  dimostrare, differenziare*
- **Pattern di interazione:** operazioni guidate da pulsanti con un
  cambiamento di stato visibile per click

## Come Usarlo

1. Prevedi: dopo `insert(1, ...)`, quale indice avrà `"gold"`? Clicca e
   verifica.
2. Osserva la riga degli indici **negativi**: quale elemento ha sempre
   indice −1?
3. Riempi la lista con `append()`, poi fai `pop()` all'indietro — la lista
   si ristampa sotto le scatole dopo ogni cambiamento.
4. Clicca **Test Stringa** per vedere perché `word[0] = "X"` fallisce su
   una stringa.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/list-index-explorer/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitoli 15-16 (Liste)

### Durata

10 minuti

### Prerequisiti

- Indicizzazione delle stringhe (Capitoli 8 e 14)

### Attività

1. **Caccia allo scorrimento** (4 min): Gli studenti cliccano insert e
   registrano quali elementi hanno ottenuto nuovi indici e quali hanno
   mantenuto il proprio. Poi lo stesso per pop.
2. **Ancora negativa** (3 min): "Qualunque cosa tu faccia, cosa c'è
   all'indice −1?" Gli studenti verificano con diverse operazioni.
3. **Mutabile contro immutabile** (3 min): Confronta l'errore del Test
   Stringa con il comportamento della lista; gli studenti scrivono una
   frase per ciascuno.

### Verifica

- Lo studente prevede la rinumerazione completa degli indici dopo un
  insert
- Lo studente sa indicare da quale estremità rimuove pop()
- Lo studente sa spiegare il TypeError nel pannello Test Stringa

## Riferimenti

1. [Python Tutorial — More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) — documentazione ufficiale dei metodi delle liste
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
