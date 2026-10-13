---
title: Comparatore di Algoritmi di Ordinamento
description: Esegui passo-passo bubble, selection e insertion sort un confronto alla volta, o fai gareggiare bubble contro insertion fianco a fianco con contatori di operazioni dal vivo.
image: /sims/sorting-comparer/sorting-comparer.png
og:image: /sims/sorting-comparer/sorting-comparer.png
twitter:image: /sims/sorting-comparer/sorting-comparer.png
social:
   cards: false
quality_score: 93
---

# Comparatore di Algoritmi di Ordinamento

<iframe src="main.html" height="542" width="100%" scrolling="no"></iframe>

[Esegui il Comparatore di Algoritmi di Ordinamento a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Bubble, selection e insertion sort differiscono solo nella loro
coreografia di confronto-e-scambio — invisibile nel codice, ovvia su un
grafico a barre. Ogni Passo evidenzia la coppia in confronto (ambra) e fa
lampeggiare gli scambi (corallo), con contatori dal vivo di confronti e
scambi. La modalità **Gara** esegue bubble e insertion sort fianco a
fianco sugli *stessi* dati, trasformando "quale ordinamento è migliore?"
in un esperimento: cambia il preset dei dati in quasi ordinato o invertito
e guarda il vincitore cambiare.

**Obiettivo di apprendimento:** Lo studente sarà in grado di confrontare
come bubble, selection e insertion sort riordinano gli stessi dati e di
giudicare quale fa meno lavoro per un dato input.

- **Tassonomia di Bloom (2001):** Analizzare → Valutare — *confrontare,
  organizzare, giudicare*
- **Pattern di interazione:** esecuzione passo-passo per confronto con una
  modalità gara fianco a fianco e preset di dati

## Come Usarlo

1. Esegui passo-passo **Bubble Sort** su dati casuali e narra la sua mossa
   distintiva: i valori grandi risalgono verso destra come bolle.
2. Confronta con **Selection Sort** (cerca il minimo) e **Insertion Sort**
   (inserisce ogni valore al suo posto scorrendo).
3. Scegli **Gara — Bubble contro Insertion**, Auto-play, e nota entrambi i
   totali delle operazioni.
4. Cambia i dati in **quasi ordinati** e fai gareggiare di nuovo —
   insertion sort vince alla grande. Prova **invertiti** per il caso
   peggiore.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/sorting-comparer/main.html"
        height="542px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 30 (Algoritmi e strutture dati)

### Durata

15 minuti

### Prerequisiti

- Liste e cicli (Capitoli 7 e 15-16)
- Il codice del capitolo per bubble/selection/insertion sort

### Attività

1. **Nomina la coreografia** (5 min): Gli studenti eseguono passo-passo
   ogni algoritmo e scrivono una frase che descrive il suo pattern di
   movimento.
2. **Gara di previsione** (5 min): Prima di ogni gara, gli studenti
   scommettono su un vincitore e prevedono i conteggi delle operazioni
   entro il 20%.
3. **I dati contano** (4 min): Gli studenti trovano il preset di dati in
   cui bubble sort fa MENO lavoro e spiegano perché.

### Verifica

- Lo studente abbina ogni algoritmo alla sua firma visiva
- Lo studente sa spiegare perché i dati quasi ordinati favoriscono
  insertion sort
- Lo studente sa indicare cosa misura il contatore dei confronti e perché
  conta

## Riferimenti

1. [Wikipedia — Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm) — panoramica degli algoritmi classici
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
