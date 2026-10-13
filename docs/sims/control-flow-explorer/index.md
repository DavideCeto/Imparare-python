---
title: Esploratore del Flusso di Controllo
description: Sposta uno slider del punteggio e guarda esattamente un percorso attraverso un diagramma di flusso if/elif/else illuminarsi mentre le condizioni saltate vengono segnate come mai controllate.
image: /sims/control-flow-explorer/control-flow-explorer.png
og:image: /sims/control-flow-explorer/control-flow-explorer.png
twitter:image: /sims/control-flow-explorer/control-flow-explorer.png
social:
   cards: false
quality_score: 93
---

# Esploratore del Flusso di Controllo

<iframe src="main.html" height="562" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore del Flusso di Controllo a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli studenti sanno leggere una catena elif ma possono ancora credere che
Python controlli ogni condizione. Questo esploratore mostra la verità: le
condizioni vengono controllate dall'alto verso il basso in ordine numerato,
esattamente un percorso si illumina di verde, e le condizioni dopo il primo
`True` vengono segnate **"mai controllato."** Il codice Python a sinistra
evidenzia le righe effettivamente eseguite, collegando il diagramma di
flusso al testo del programma.

**Obiettivo di apprendimento:** Lo studente sarà in grado di prevedere quale
ramo di una catena if/elif/else viene eseguito per un dato input e di
spiegare perché i rami successivi vengono saltati.

- **Tassonomia di Bloom (2001):** Comprendere → Analizzare — *prevedere,
  tracciare, differenziare*
- **Pattern di interazione:** evidenziazione del percorso dal vivo guidata
  da slider con l'ordine di controllo reso esplicito

## Come Usarlo

1. Con il programma **Catena Elif**, prevedi quale ramo viene eseguito per
   il punteggio 85.
2. Sposta lo slider e osserva: i rombi mostrano i verdetti Vero/Falso, il
   percorso vincente si illumina, e i controlli successivi dicono "mai
   controllato."
3. Scorri da 100 a 0 lentamente — il percorso verde scende lungo la catena
   esattamente a 90, 80 e 70.
4. Passa a **If Semplice** e imposta il punteggio sotto 50: la scatola else
   mostra che non succede nulla.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/control-flow-explorer/main.html"
        height="562px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 9 (Prendere decisioni con if/else)

### Durata

10-15 minuti

### Prerequisiti

- Operatori di confronto e il tipo Booleano (sezioni iniziali del Capitolo 9)

### Attività

1. **Prevedi** (3 min): Per i punteggi 95, 85, 75 e 40, gli studenti
   scrivono quale voto assegna la catena elif.
2. **Verifica** (5 min): Controlla ognuno con lo slider. Per ogni
   punteggio, chiedi "quante condizioni ha effettivamente controllato
   Python?"
3. **Caccia al confine** (4 min): Gli studenti trovano il punteggio esatto
   in cui la risposta passa da "B" a "A" — rafforzando i confini con >=.

### Verifica

- Lo studente prevede il ramo scelto per qualsiasi punteggio senza la
  simulazione
- Lo studente sa spiegare perché `score = 95` controlla una sola condizione
- Lo studente sa spiegare cosa succede in un if semplice senza else quando
  la condizione è Falsa

## Riferimenti

1. [Python Tutorial — if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
