---
title: Ispettore degli Ambiti
description: Esegui passo-passo un programma con variabili globali e locali, osservando le stanze di ambito apparire e svanire e le ricerche di nomi sondare prima il locale, poi il globale.
image: /sims/scope-inspector/scope-inspector.png
og:image: /sims/scope-inspector/scope-inspector.png
twitter:image: /sims/scope-inspector/scope-inspector.png
social:
   cards: false
quality_score: 93
---

# Ispettore degli Ambiti

<iframe src="main.html" height="512" width="100%" scrolling="no"></iframe>

[Esegui l'Ispettore degli Ambiti a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

L'ambito è l'idea più astratta della prima metà del libro: le variabili che
"vivono" in stanze invisibili. Questo ispettore disegna le stanze. La
stanza Globale è sempre sullo schermo; ogni chiamata di funzione apre una
stanza Funzione temporanea che svanisce al ritorno — portando via con sé le
sue variabili. Ogni ricerca di nome evidenzia la scatola effettivamente
usata da Python, e quando una ricerca locale fallisce, un distintivo dice
"non trovato qui → controlla la stanza Globale." Il preset Bug di
Oscuramento mostra uno `score = 99` locale che nasconde il 10 globale; il
preset La Correzione con global mostra la parola chiave `global` che scrive
direttamente nella stanza Globale.

**Obiettivo di apprendimento:** Lo studente sarà in grado di determinare a
quale variabile si riferisce un nome in qualsiasi riga, differenziando
variabili locali, globali e oscurate.

- **Tassonomia di Bloom (2001):** Analizzare — *differenziare, attribuire,
  debuggare*
- **Pattern di interazione:** esecuzione passo-passo con stanze di ambito
  annidate ed evidenziazione delle ricerche

## Come Usarlo

1. Inizia con **Leggi il Globale**: osserva la stanza Funzione vuota
   apparire, e la ricerca scendere fino alla stanza Globale.
2. Passa a **Bug di Oscuramento** e prevedi: cosa mostra il `print(score)`
   finale? Esegui passo-passo — la scatola locale 99 viene buttata via
   insieme alla sua stanza.
3. Esegui **La Correzione con global** per vedere come la parola chiave
   `global` cambia dove atterra la scrittura.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/scope-inspector/main.html"
        height="512px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 11 (Funzioni con parametri e scope)

### Durata

15 minuti

### Prerequisiti

- Definire e chiamare funzioni (Capitolo 4)
- Variabili e assegnazione (Capitolo 3)

### Attività

1. **Giro delle stanze** (4 min): Esegui passo-passo Leggi il Globale.
   Chiedi: "quando esiste la stanza Funzione, e quando no?"
2. **Prevedi il bug** (5 min): Prima di eseguire passo-passo Bug di
   Oscuramento, gli studenti votano: 99 o 10? Esegui passo-passo e
   identifica l'esatto passo in cui la scatola locale viene distrutta.
3. **Confronto della correzione** (4 min): Esegui La Correzione con global
   e fai esprimere agli studenti in una frase cosa cambia `global score`.

### Verifica

- Lo studente prevede correttamente l'output di un programma con
  oscuramento
- Lo studente sa spiegare perché una variabile locale scompare dopo la
  chiamata
- Lo studente sa indicare quando serve la parola chiave `global` e perché è
  rara

## Riferimenti

1. [Python FAQ — What are the rules for local and global variables?](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python) — spiegazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
