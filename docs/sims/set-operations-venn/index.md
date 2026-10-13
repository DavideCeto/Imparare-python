---
title: Diagramma di Venn delle Operazioni sugli Insiemi
description: Digita due insiemi, guarda i gettoni dei membri atterrare nelle regioni giuste del diagramma di Venn, e illumina unione, intersezione, differenza e differenza simmetrica.
image: /sims/set-operations-venn/set-operations-venn.png
og:image: /sims/set-operations-venn/set-operations-venn.png
twitter:image: /sims/set-operations-venn/set-operations-venn.png
social:
   cards: false
quality_score: 93
---

# Diagramma di Venn delle Operazioni sugli Insiemi

<iframe src="main.html" height="542" width="100%" scrolling="no"></iframe>

[Esegui il Diagramma di Venn delle Operazioni sugli Insiemi a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Unione, intersezione e differenza sono idee intrinsecamente spaziali che
l'output testuale di `{...}` nasconde completamente. Qui gli studenti
digitano due insiemi e i gettoni dei membri atterrano automaticamente
nelle regioni giuste del diagramma di Venn. Ogni pulsante operazione ombreggia
esattamente la regione che seleziona — `A | B` illumina entrambi i cerchi,
`A & B` solo la lente, `A - B` la mezzaluna sinistra, `A ^ B` tutto tranne
la lente — mentre l'espressione Python e il suo insieme risultato vengono
stampati sotto. Digitare un duplicato lo fa visibilmente collassare, e
un'intersezione vuota stampa `set()`, la notazione Python per l'insieme
vuoto.

**Obiettivo di apprendimento:** Lo studente sarà in grado di classificare
quali elementi appartengono a A | B, A & B, A − B e A ^ B per due insiemi
dati.

- **Tassonomia di Bloom (2001):** Comprendere → Analizzare — *classificare,
  confrontare, organizzare*
- **Pattern di interazione:** insiemi modificabili più pulsanti operazione
  che evidenziano le regioni

## Come Usarlo

1. Prevedi quali animali seleziona `A & B`, poi clicca il pulsante
   intersezione e controlla la regione ombreggiata.
2. Clicca tutte e quattro le operazioni e descrivi ogni regione ombreggiata
   con parole tue.
3. Modifica gli insiemi: digita i tuoi elementi, poi digita un elemento due
   volte nell'insieme A — il duplicato collassa perché gli insiemi non
   contengono mai ripetizioni.
4. Rimuovi tutti gli elementi condivisi e clicca `A & B` — il risultato è
   `set()`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/set-operations-venn/main.html"
        height="542px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 20 (Tuple e insiemi)

### Durata

10-15 minuti

### Prerequisiti

- Creare insiemi con le parentesi graffe (Capitolo 20)

### Attività

1. **Giro delle regioni** (4 min): Per gli insiemi predefiniti, gli
   studenti prevedono su carta tutti e quattro i risultati delle
   operazioni, poi verificano ciascuno con un click.
2. **Costruisci il tuo** (4 min): Gli studenti inseriscono i loro due
   insiemi di cibi preferiti e trovano l'intersezione con quello di un
   compagno.
3. **Casi limite** (4 min): Rendi vuota l'intersezione (cosa stampa?),
   rendi B un sottoinsieme di A (cosa lascia A - B?), e inserisci un
   duplicato.

### Verifica

- Lo studente abbina ogni simbolo di operatore alla sua regione ombreggiata
- Lo studente prevede l'insieme risultato per tutte e quattro le operazioni
  su nuovi insiemi
- Lo studente sa spiegare perché gli insiemi rimuovono automaticamente i
  duplicati

## Riferimenti

1. [Python Documentation — Set Types](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) — documentazione ufficiale delle operazioni sugli insiemi
2. [Wikipedia — Venn diagram](https://en.wikipedia.org/wiki/Venn_diagram) — approfondimento sulla visualizzazione
3. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
