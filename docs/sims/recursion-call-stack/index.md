---
title: Pila delle Chiamate Ricorsive
description: Esegui passo-passo factorial(4) e guarda i frame della pila accumularsi fino al caso base dorato, poi srotolarsi mentre ogni moltiplicazione in sospeso si riempie.
image: /sims/recursion-call-stack/recursion-call-stack.png
og:image: /sims/recursion-call-stack/recursion-call-stack.png
twitter:image: /sims/recursion-call-stack/recursion-call-stack.png
social:
   cards: false
quality_score: 93
---

# Pila delle Chiamate Ricorsive

<iframe src="main.html" height="562" width="100%" scrolling="no"></iframe>

[Esegui la Pila delle Chiamate Ricorsive a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

La pila delle chiamate è la macchina invisibile per eccellenza: gli
studenti vedono `factorial(4) = 24` ma mai i frame che si accumulano e si
srotolano. Questa simulazione disegna ogni frame come una scatola fisica
che ricorda il proprio `n` e il proprio lavoro in sospeso (`4 × ?`). I
frame si accumulano verso l'alto finché il caso base non si illumina
**dorato**, poi vengono rimossi uno alla volta mentre ogni moltiplicazione
in sospeso si riempie e la sua risposta scorre verso il basso. Il preset
`countdown(3)` mostra la ricorsione con effetti collaterali e nessun
valore di ritorno; **Caso Base Mancante** fa crescere la torre oltre
`n = 0` finché non appare un banner `RecursionError`.

**Obiettivo di apprendimento:** Lo studente sarà in grado di scomporre una
chiamata ricorsiva in frame della pila, identificare il caso base e
tracciare i valori che tornano giù lungo la pila.

- **Tassonomia di Bloom (2001):** Analizzare — *scomporre, organizzare,
  tracciare*
- **Pattern di interazione:** esecuzione passo-passo con le variabili e il
  lavoro in sospeso di ogni frame visibili

## Come Usarlo

1. Prevedi quanto sarà alta la torre per `factorial(4)`, poi procedi
   passo-passo e conta i frame.
2. Osserva il momento di svolta: il caso base dorato è l'unico frame che
   risponde senza chiedere a nessun altro.
3. Sulla via del ritorno, segui ogni risposta: 1 → 2 → 6 → 24.
4. Prova **countdown(3)** (ricorsione che stampa invece di restituire) e
   **Caso Base Mancante** (perché la regola di arresto conta).

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/recursion-call-stack/main.html"
        height="562px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 24 (Ricorsione e frattali); utile anche per i traceback nel Capitolo 23

### Durata

15 minuti

### Prerequisiti

- Funzioni, parametri e valori di ritorno (Capitoli 4 e 11)

### Attività

1. **Previsione della torre** (4 min): Gli studenti prevedono il numero
   massimo di frame per factorial(4), poi factorial(6) (senza la
   simulazione).
2. **Traccia a due fasi** (5 min): Esegui passo-passo tutti gli 8 passi;
   gli studenti narrano con parole proprie il ritmo "su con le pause, giù
   con le risposte."
3. **Rompilo** (4 min): Esegui Caso Base Mancante. Gli studenti scrivono
   l'unica riga che lo corregge e dicono dove deve andare.

### Verifica

- Lo studente indica la profondità massima della pila per factorial(n)
- Lo studente sa identificare il caso base in una nuova funzione ricorsiva
- Lo studente sa spiegare cosa significa RecursionError e come prevenirlo

## Riferimenti

1. [Python Tutorial — more on defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) — contesto sulle chiamate di funzione
2. [Wikipedia — Call stack](https://en.wikipedia.org/wiki/Call_stack) — il concetto generale
3. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
