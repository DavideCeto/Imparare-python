---
title: Istogramma dei Lanci di Dadi
description: Lancia un dado 1, 100 o 1000 volte e guarda l'istogramma appiattirsi verso l'uniformità - poi passa a due dadi e scopri il triangolo intorno al 7.
image: /sims/dice-roll-histogram/dice-roll-histogram.png
og:image: /sims/dice-roll-histogram/dice-roll-histogram.png
twitter:image: /sims/dice-roll-histogram/dice-roll-histogram.png
social:
   cards: false
quality_score: 95
---

# Istogramma dei Lanci di Dadi

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui l'Istogramma dei Lanci di Dadi a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

Una singola chiamata a `random.randint(1, 6)` sembra puro caos; il pattern
emerge solo su molte prove. Questo esecutore di esperimenti permette agli
studenti di lanciare in lotti di 1, 100 o 1000 e guardare l'istogramma
assestarsi verso uno skyline piatto e uniforme. Passando alla **somma di
due dadi** si produce il triangolo genuinamente sorprendente con il picco
a 7 — il momento in cui gli studenti scoprono che la casualità ha una
forma.

**Obiettivo di apprendimento:** Lo studente sarà in grado di analizzare
come la distribuzione dei lanci casuali si appiattisce man mano che il
numero di prove cresce, e di confrontare un dado con la somma di due dadi.

- **Tassonomia di Bloom (2001):** Analizzare — *organizzare, confrontare,
  attribuire*
- **Pattern di interazione:** esecutore di esperimenti con lotti avviati
  dallo studente
- **Libreria:** Chart.js (grafico a barre con aggiornamenti dal vivo e
  tooltip di percentuale)

## Come Usarlo

1. Prevedi: dopo 1000 lanci, le sei barre saranno uguali o diseguali?
2. Clicca **Lancia 1** diverse volte (caos), poi **Lancia 100** (uno
   skyline approssimativo), poi **Lancia 1000** (quasi piatto). Passa il
   mouse su una barra per la sua percentuale.
3. Passa a **Somma di due dadi**, lancia 1000 volte, e spiega la montagna:
   perché ci sono più modi per fare 7 che per fare 2?
4. **Reimposta** e ripeti — le barre esatte differiscono ogni volta, ma la
   forma ritorna.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/dice-roll-histogram/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 17 (Moduli e numeri casuali)

### Durata

10-15 minuti

### Prerequisiti

- random.randint() (Capitolo 17)

### Attività

1. **Prevedi e lancia** (4 min): Gli studenti votano se l'istogramma a
   1000 lanci sarà uniforme. Lancia e discuti le piccole oscillazioni.
2. **Mistero dei due dadi** (6 min): Cambia modalità, lancia 1000 volte, e
   sfida gli studenti a elencare tutti i modi per fare 7 (sei modi) contro
   2 (un modo).
3. **Controllo delle percentuali** (3 min): Passa il mouse sulle barre —
   ogni faccia dovrebbe stare intorno al 16,7%. Perché quel numero? (1 su
   6.)

### Verifica

- Lo studente sa spiegare perché più lanci rendono le barre di un dado
  più uniformi
- Lo studente sa spiegare perché 7 è la somma più comune con due dadi
- Lo studente sa indicare la percentuale attesa per ogni faccia di un dado

## Riferimenti

1. [Python Documentation — random module](https://docs.python.org/3/library/random.html) — documentazione ufficiale
2. [Chart.js Documentation](https://www.chartjs.org/docs/latest/) — la libreria di grafici usata
