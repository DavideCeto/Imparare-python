---
title: Esecutore di Codice Passo-Passo
description: Percorri un breve programma Python una riga alla volta, osservando la freccia di esecuzione dell'interprete muoversi dall'alto verso il basso e l'output apparire riga per riga.
image: /sims/code-stepper/code-stepper.png
og:image: /sims/code-stepper/code-stepper.png
twitter:image: /sims/code-stepper/code-stepper.png
social:
   cards: false
quality_score: 93
---

# Esecutore di Codice Passo-Passo

<iframe src="main.html" height="452" width="100%" scrolling="no"></iframe>

[Esegui l'Esecutore di Codice Passo-Passo a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

L'Esecutore di Codice Passo-Passo rende visibile il comportamento più
fondamentale dell'interprete Python: un programma viene eseguito **una riga
alla volta, dall'alto verso il basso**. Gli studenti cliccano su Passo
Successivo per muovere una freccia di esecuzione attraverso un breve
programma mentre la console di output si riempie di una riga per ogni passo.
I commenti e le righe vuote vengono visibilmente saltati con una nota in
linguaggio semplice che ne spiega il motivo.

**Obiettivo di apprendimento:** Lo studente sarà in grado di prevedere quale
riga di un breve programma Python verrà eseguita successivamente e di
spiegare che Python esegue le istruzioni in ordine, dall'alto verso il basso.

- **Tassonomia di Bloom (2001):** Comprendere — *spiegare, prevedere, tracciare*
- **Pattern di interazione:** esempio guidato passo-passo (nessuna animazione)

## Come Usarlo

1. Leggi il programma nel pannello di sinistra e **prevedi l'output** prima
   di cliccare qualsiasi cosa.
2. Clicca **Passo Successivo** per eseguire una riga. Osserva la freccia
   arancione e la nota sotto i pannelli.
3. Clicca **Precedente** per tornare indietro di un passo, o **Reimposta**
   per ricominciare.
4. Usa il menu a tendina per provare tutti e tre i programmi. "Commenti
   Ovunque" mostra che un `print()` dentro un commento non viene mai
   eseguito; "Python Fa i Conti" mostra la differenza tra `print(2 + 3)` e
   `print("2 + 3")`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/code-stepper/main.html"
        height="452px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), prime settimane di Python

### Durata

10 minuti

### Prerequisiti

- Nessuno — questo MicroSim supporta il Capitolo 1 (Benvenuto in Python e
  Skulpt) e il Capitolo 2 (Struttura del codice Python)

### Attività

1. **Prevedi** (3 min): Gli studenti leggono il "Programma di Saluto" e
   scrivono cosa pensano sarà l'output, in ordine.
2. **Esegui passo-passo e verifica** (4 min): Gli studenti eseguono ogni riga
   passo dopo passo e confrontano la console con la loro previsione. Chiedi:
   "Perché la riga vuota e il commento non hanno prodotto output?"
3. **Domanda trabocchetto** (3 min): Passa a "Commenti Ovunque" e chiedi agli
   studenti di prevedere prima di procedere: "Quante righe verranno
   stampate?" (Risposta: 2 — il print commentato non viene mai eseguito.)

### Verifica

- Lo studente prevede correttamente l'ordine dell'output per un nuovo
  programma di 5 righe
- Lo studente sa affermare che Python salta le righe di commento e le righe
  vuote
- Lo studente sa spiegare perché `print("2 + 3")` non stampa `5`

## Riferimenti

1. [Python Tutorial — Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html) — documentazione ufficiale su come l'interprete esegue il codice
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
