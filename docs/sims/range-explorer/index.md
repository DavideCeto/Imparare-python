---
title: Esploratore di Range
description: Regola gli slider di inizio, fine e passo e vedi istantaneamente quali numeri genera range() su una linea dei numeri, con il valore finale mostrato come mai incluso.
image: /sims/range-explorer/range-explorer.png
og:image: /sims/range-explorer/range-explorer.png
twitter:image: /sims/range-explorer/range-explorer.png
social:
   cards: false
quality_score: 93
---

# Esploratore di Range

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore di Range a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli errori di sbaglio-per-uno intorno a `range()` sono il bug da ciclo più
comune che i principianti scrivono. Questo esploratore rende fisica la
regola: i numeri generati appaiono come puntini blu pieni su una linea dei
numeri, mentre il valore finale è un anello arancione vuoto etichettato "non
incluso." Una lettura del codice dal vivo mostra esattamente cosa produce
`range(start, stop, step)`, e la riga dei fatti collega il conteggio dei
numeri a quante volte un ciclo for verrebbe eseguito. La modalità sfida
mostra anelli bersaglio verdi da colpire con gli slider.

**Obiettivo di apprendimento:** Lo studente sarà in grado di scegliere i
valori di inizio, fine e passo che producono una sequenza di numeri
desiderata.

- **Tassonomia di Bloom (2001):** Applicare — *usare, eseguire, risolvere*
- **Pattern di interazione:** slider dei parametri con riscontro immediato e
  verifica automatica delle sfide

## Come Usarlo

1. Prevedi cosa produce `range(2, 12, 3)`, poi controlla la linea dei
   numeri.
2. Scorri **Fine** su e giù e osserva l'anello vuoto — i puntini blu si
   fermano sempre prima di raggiungerlo.
3. Clicca **Nuova Sfida** e regola gli slider finché i tuoi puntini blu non
   atterrano esattamente sugli anelli verdi.
4. Seleziona **conta all'indietro** per provare i passi negativi — e scopri
   quando un range non produce alcun numero.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/range-explorer/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 7 (Cicli for e disegno di forme)

### Durata

10 minuti

### Prerequisiti

- Il ciclo for con range() (sezioni iniziali del Capitolo 7)

### Attività

1. **Prevedi** (3 min): Gli studenti scrivono gli output di `range(4)`,
   `range(2, 6)` e `range(0, 10, 2)` prima di toccare la simulazione.
2. **Verifica** (3 min): Controlla ognuno sulla linea dei numeri. Enfatizza
   ogni volta l'anello vuoto di fine.
3. **Sfide** (4 min): Gli studenti risolvono tre round di Nuova Sfida. Vince
   chi imposta correttamente gli slider più in fretta.

### Verifica

- Lo studente scrive valori corretti per un nuovo range come
  `range(3, 14, 4)`
- Lo studente sa spiegare perché `range(5)` esegue un ciclo 5 volte ma non
  produce mai 5
- Lo studente sa produrre una sequenza bersaglio come 1, 3, 5, 7, 9 al primo
  tentativo

## Riferimenti

1. [Python Documentation — range](https://docs.python.org/3/library/stdtypes.html#range) — documentazione ufficiale di range
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
