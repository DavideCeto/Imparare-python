---
title: Flusso di Chiamata delle Funzioni
description: Traccia passo-passo una chiamata di funzione Python - l'argomento si lega al parametro, il corpo calcola, e il valore di ritorno fluisce indietro al punto di chiamata.
image: /sims/function-call-flow/function-call-flow.png
og:image: /sims/function-call-flow/function-call-flow.png
twitter:image: /sims/function-call-flow/function-call-flow.png
social:
   cards: false
quality_score: 93
---

# Flusso di Chiamata delle Funzioni

<iframe src="main.html" height="502" width="100%" scrolling="no"></iframe>

[Esegui il Flusso di Chiamata delle Funzioni a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

"Perché `def` non esegue il mio codice?" e "dove va a finire l'argomento?"
sono le due domande più comuni nel capitolo sulle funzioni. Questo MicroSim
risponde a entrambe visivamente. Il passo `def` memorizza la funzione come
una "macchina" verde senza eseguirla. Ogni passo di chiamata mostra
l'argomento che vola nello slot del parametro, il corpo che calcola, e il
valore di ritorno che vola indietro per sostituire il punto di chiamata. La
stessa funzione viene eseguita due volte con argomenti diversi, così gli
studenti vedono perché le funzioni sono riutilizzabili.

**Obiettivo di apprendimento:** Lo studente sarà in grado di tracciare una
chiamata di funzione, spiegando come il valore dell'argomento si lega al
parametro e come il valore di ritorno sostituisce il punto di chiamata.

- **Tassonomia di Bloom (2001):** Comprendere — *spiegare, tracciare, dedurre*
- **Pattern di interazione:** passo-passo con frecce di flusso dati e valori
  concreti visibili a ogni passo (nessuna animazione)

## Come Usarlo

1. Leggi il programma e **prevedi i due numeri che stamperà**.
2. Clicca **Passo Successivo**. Il primo passo è `def` — nota che non viene
   eseguito nulla; Python memorizza solo la ricetta.
3. Osserva la freccia blu portare l'argomento `5` nello slot del parametro
   `n`, e la freccia arancione portare il valore restituito `10` indietro.
4. Continua a procedere passo-passo per vedere la stessa macchina eseguirsi
   di nuovo con `7`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/function-call-flow/main.html"
        height="502px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 4 (Funzioni e oggetti)

### Durata

10 minuti

### Prerequisiti

- Variabili e assegnazione (Capitolo 3)
- L'idea che i programmi vengono eseguiti dall'alto verso il basso (Capitoli 1-2)

### Attività

1. **Prevedi** (3 min): Gli studenti scrivono i due numeri che il programma
   stamperà, prima di toccare la simulazione.
2. **Traccia** (5 min): Procedi attraverso tutti i 9 passi. Fermati al passo
   1 e chiedi: "Perché l'output è ancora vuoto dopo che Python ha letto il
   blocco def?"
3. **Riuso** (2 min): Chiedi agli studenti cosa stamperebbe una terza riga
   che chiama `double(100)` — dovrebbero essere in grado di tracciarlo
   mentalmente ora.

### Verifica

- Lo studente sa spiegare perché il corpo della funzione non viene eseguito
  alla riga `def`
- Lo studente sa indicare dove va il valore dell'argomento e dove finisce il
  valore di ritorno
- Lo studente traccia correttamente una nuova chiamata come `double(12)`
  senza la simulazione

## Riferimenti

1. [Python Tutorial — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
