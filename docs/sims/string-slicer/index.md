---
title: Affettatore di Stringhe
description: Trascina le maniglie di affettamento sopra le tessere delle lettere per costruire espressioni Python di indice e slice con notazione word[2:7] dal vivo, indici negativi e sfide.
image: /sims/string-slicer/string-slicer.png
og:image: /sims/string-slicer/string-slicer.png
twitter:image: /sims/string-slicer/string-slicer.png
social:
   cards: false
quality_score: 93
---

# Affettatore di Stringhe

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui l'Affettatore di Stringhe a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

La notazione slice causa infiniti bug di sbaglio-per-uno perché gli
studenti non riescono a vedere i confini. Questo affettatore li rende
fisici: le tessere delle lettere portano indici positivi sopra e indici
negativi sotto, e due maniglie trascinabili — inizio verde, fine rossa —
selezionano la slice. La maniglia rossa si trova visibilmente una posizione
dopo l'ultima lettera selezionata, rendendo "la fine non è mai inclusa" una
cosa che puoi vedere invece di memorizzare. Un selettore di passo aggiunge
il terzo argomento della slice, i click su singole tessere mostrano
l'indicizzazione semplice, e la modalità sfida chiede sottostringhe
bersaglio come `"ROCKS"`.

**Obiettivo di apprendimento:** Lo studente sarà in grado di scrivere
espressioni di indice e slice che estraggono una sottostringa desiderata.

- **Tassonomia di Bloom (2001):** Applicare — *usare, eseguire, risolvere*
- **Pattern di interazione:** manipolazione diretta con lettura della
  notazione dal vivo

## Come Usarlo

1. Trascina le maniglie verde **inizio** e rossa **fine** e osserva
   `word[start:end]` aggiornarsi con il suo risultato.
2. Nota dove si trova la maniglia rossa quando la slice legge `"THON "` —
   una posizione dopo l'ultima lettera.
3. Imposta **passo** a 2 e vedi slice a lettere alternate come
   `word[0:6:2]`.
4. Clicca una singola tessera per la modalità indice, controlla gli indici
   negativi sotto le tessere, e prova **Nuova Sfida**.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/string-slicer/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 14 (Metodi delle stringhe e formattazione); fondamenti dal Capitolo 8

### Durata

10-15 minuti

### Prerequisiti

- Stringhe e len() (Capitolo 8)

### Attività

1. **Prevedi e trascina** (4 min): Per `"PYTHON ROCKS"`, gli studenti
   scrivono su carta la slice per `"ROCKS"`, poi verificano trascinando.
2. **Esercizio fine-esclusiva** (3 min): "Crea una slice che selezioni
   esattamente una lettera." Cosa notano gli studenti su inizio e fine?
   (fine = inizio + 1)
3. **Sfide** (5 min): Risolvi tutti e quattro i round di Nuova Sfida,
   incluso quello con passo 2.

### Verifica

- Lo studente scrive una slice corretta per una sottostringa indicata al
  primo tentativo
- Lo studente sa spiegare perché `word[2:7]` seleziona cinque caratteri, non
  sei
- Lo studente sa usare un indice negativo per prendere l'ultimo carattere

## Riferimenti

1. [Python Tutorial — Strings (indexing and slicing)](https://docs.python.org/3/tutorial/introduction.html#strings) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
