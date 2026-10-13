---
title: Esecutore Passo-Passo del Ciclo For
description: Percorri passo-passo un ciclo for Python una istruzione alla volta - guarda la variabile del ciclo cambiare, la freccia saltare indietro in cima, e una turtle disegnare un lato di quadrato per ogni giro.
image: /sims/for-loop-stepper/for-loop-stepper.png
og:image: /sims/for-loop-stepper/for-loop-stepper.png
twitter:image: /sims/for-loop-stepper/for-loop-stepper.png
social:
   cards: false
quality_score: 93
---

# Esecutore Passo-Passo del Ciclo For

<iframe src="main.html" height="502" width="100%" scrolling="no"></iframe>

[Esegui l'Esecutore Passo-Passo del Ciclo For a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

La statica "tabella dei giri del ciclo" diventa una macchina che puoi far
girare a mano. Ogni click su Passo Successivo avanza di una *istruzione*,
così gli studenti vedono la freccia di esecuzione saltare indietro alla
riga `for` all'inizio di ogni giro — l'esatto momento in cui `i` prende il
suo valore successivo. Nel preset Disegna Quadrato una mini turtle disegna
un lato per ogni giro, collegando la meccanica del ciclo direttamente al
programma del quadrato del capitolo.

**Obiettivo di apprendimento:** Lo studente sarà in grado di tracciare un
ciclo for, indicando il valore della variabile del ciclo a ogni giro e
prevedendo il numero totale di ripetizioni.

- **Tassonomia di Bloom (2001):** Comprendere — *tracciare, spiegare,
  prevedere* (il preset Totale Progressivo si estende verso Applicare)
- **Pattern di interazione:** esecuzione passo-passo a livello di
  istruzione; auto-play lento opzionale che parte in pausa

## Come Usarlo

1. Prevedi: quanto sarà `i` al primo giro? Quanti giri ci saranno?
2. Clicca **Passo Successivo** ripetutamente. Osserva il badge di `i` e il
   contatore dei giri, e nota la freccia che salta indietro in cima.
3. Usa **Auto-play** per guardare un'esecuzione completa a velocità di
   lettura; clicca **Pausa** in qualsiasi momento.
4. Prova **Conto alla Rovescia** (perché non stampa mai 3?) e **Totale
   Progressivo** (guarda la scatola dell'accumulatore crescere di `i` a
   ogni giro).

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/for-loop-stepper/main.html"
        height="502px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 7 (Cicli for e disegno di forme)

### Durata

10-15 minuti

### Prerequisiti

- Comandi base della turtle (Capitolo 5)
- Variabili (Capitolo 3)

### Attività

1. **Prevedi** (3 min): "Quanto vale `i` al primo giro? E all'ultimo?
   Quanti lati vengono disegnati?"
2. **Fai girare la macchina** (5 min): Esegui passo-passo Disegna Quadrato.
   Ogni volta che la freccia atterra sulla riga `for`, gli studenti dicono
   ad alta voce il nuovo valore di `i`.
3. **Trasferimento** (5 min): Passa a Conto alla Rovescia. Chiedi:
   "range(3) — perché il 3 non viene mai stampato?" Poi Totale Progressivo:
   "Perché il totale cresce di una quantità diversa a ogni giro?"

### Verifica

- Lo studente indica i valori che `i` assume per `range(4)` senza eseguirlo
- Lo studente sa indicare l'esatto passo in cui il ciclo decide di fermarsi
- Lo studente prevede il totale finale per l'accumulo con `range(5)` (10)

## Riferimenti

1. [Python Tutorial — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
