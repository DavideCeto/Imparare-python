---
title: Ispettore delle Istanze degli Oggetti
description: Percorri passo-passo le costruzioni di Dog e le chiamate ai metodi, guardando le card delle istanze ottenere i propri attributi mentre una freccia luminosa self mostra su quale card lavora ogni metodo.
image: /sims/object-instance-inspector/object-instance-inspector.png
og:image: /sims/object-instance-inspector/object-instance-inspector.png
twitter:image: /sims/object-instance-inspector/object-instance-inspector.png
social:
   cards: false
quality_score: 93
---

# Ispettore delle Istanze degli Oggetti

<iframe src="main.html" height="572" width="100%" scrolling="no"></iframe>

[Esegui l'Ispettore delle Istanze degli Oggetti a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli studenti confondono abitualmente la classe con i suoi oggetti e non
sanno dire a cosa si riferisce `self`. Questo ispettore separa i due
visivamente: la classe è una card **progetto** tratteggiata che da sola
non crea nulla; ogni chiamata `Dog(...)` genera una card istanza solida
con le proprie scatole `name` e `age`. Durante `rex.bark()`, una freccia
arancione luminosa collega il metodo del progetto a esattamente una card —
`self` è l'oggetto a sinistra del punto. Il passo finale legge
`rex.species` e mostra la ricerca scendere fino alla variabile di classe
condivisa sul progetto.

**Obiettivo di apprendimento:** Lo studente sarà in grado di spiegare la
differenza tra una classe e le sue istanze e di identificare a quale
oggetto si riferisce `self` durante una chiamata di metodo.

- **Tassonomia di Bloom (2001):** Comprendere — *spiegare, esemplificare,
  differenziare*
- **Pattern di interazione:** esecuzione passo-passo di costruzione e
  chiamate di metodo con card delle istanze e una freccia self

## Come Usarlo

1. Passo 1: nota che `class Dog:` NON crea nessun cane — solo il progetto
   tratteggiato.
2. Passi 2-3: ogni chiamata `Dog(...)` costruisce una card separata con le
   proprie scatole.
3. Passo 4: prima di cliccare, prevedi il nome di chi stampa `rex.bark()`,
   poi segui la freccia `self`.
4. Passo 5: `rex.species` non è sulla card di rex — osserva la ricerca
   tratteggiata risalire fino al progetto.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/object-instance-inspector/main.html"
        height="572px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 25 (Programmazione orientata agli oggetti)

### Durata

10-15 minuti

### Prerequisiti

- Funzioni e parametri (Capitoli 4 e 11)
- Oggetti e notazione col punto (Capitolo 4)

### Attività

1. **Verifica del progetto** (3 min): Dopo il passo 1, chiedi: "Quanti
   cani esistono in questo momento?" (Zero — un equivoco comune.)
2. **Il nome di chi?** (4 min): Gli studenti prevedono l'output di
   `rex.bark()` e `bella.bark()`, poi verificano con la freccia self.
3. **Condiviso contro posseduto** (4 min): Gli studenti classificano
   `name`, `age` e `species` in "ogni cane ne possiede uno" contro "tutti i
   cani ne condividono uno."

### Verifica

- Lo studente sa indicare a cosa si riferisce self in qualsiasi chiamata
  di metodo
- Lo studente sa spiegare perché due istanze hanno valori di attributo
  indipendenti
- Lo studente prevede dove Python trova rex.species

## Riferimenti

1. [Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
