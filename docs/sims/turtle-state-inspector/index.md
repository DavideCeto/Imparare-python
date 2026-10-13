---
title: Ispettore dello Stato della Turtle
description: Percorri passo-passo i comandi della turtle mentre un pannello dal vivo mostra lo stato nascosto della turtle - posizione x, y, bussola della direzione, penna su/giù, e colore della penna.
image: /sims/turtle-state-inspector/turtle-state-inspector.png
og:image: /sims/turtle-state-inspector/turtle-state-inspector.png
twitter:image: /sims/turtle-state-inspector/turtle-state-inspector.png
social:
   cards: false
quality_score: 93
---

# Ispettore dello Stato della Turtle

<iframe src="main.html" height="512" width="100%" scrolling="no"></iframe>

[Esegui l'Ispettore dello Stato della Turtle a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli studenti comandano la turtle ma non vedono mai cosa c'è dentro di lei.
Questo ispettore rende visibile lo stato nascosto della turtle: posizione x
e y, direzione (con un quadrante bussola), penna su/giù, e colore della
penna. Ogni click su Comando Successivo esegue un comando della turtle; ogni
valore di stato appena cambiato viene evidenziato, così `t.right(90)`
diventa "la direzione è passata da 0° a 270°" invece di un incantesimo
memorizzato a memoria.

**Obiettivo di apprendimento:** Lo studente sarà in grado di prevedere la
posizione e la direzione della turtle dopo ogni comando e di dimostrare come
i cambiamenti di direzione producano forme.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *interpretare,
  prevedere, dimostrare*
- **Pattern di interazione:** esecuzione passo-passo di una lista di comandi
  con un pannello di stato dal vivo

## Come Usarlo

1. Scegli un programma dal menu a tendina (inizia con **Quadrato**).
2. Prima di ogni click, **prevedi**: dove sarà la turtle, e verso dove sarà
   rivolta?
3. Clicca **Comando Successivo** e controlla i valori evidenziati nel
   pannello.
4. Prova **Demo Penna** per vedere `penup()` e `pendown()` lasciare uno
   spazio vuoto, e osserva il campione di colore della penna cambiare con
   `t.pencolor("red")`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/turtle-state-inspector/main.html"
        height="512px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 5 (Disegnare con la grafica turtle)

### Durata

10-15 minuti

### Prerequisiti

- Comandi base della turtle: forward(), right(), left() (sezioni iniziali del Capitolo 5)
- Oggetti e notazione col punto (Capitolo 4)

### Attività

1. **Prevedi il quadrato** (5 min): Esegui passo-passo il programma
   Quadrato. Prima di ogni comando, gli studenti dicono ad alta voce il
   prossimo valore di direzione (0°, 270°, 180°, 90°).
2. **Matematica della direzione** (4 min): Chiedi perché `t.right(90)` fa
   scendere la direzione di 90. Usa il quadrante bussola per verificare.
3. **Demo Penna** (4 min): Gli studenti prevedono dove la linea disegnata
   avrà uno spazio vuoto prima di procedere passo-passo.

### Verifica

- Lo studente prevede correttamente x, y e direzione dopo due comandi
  qualsiasi
- Lo studente sa spiegare la differenza tra il movimento con penup() e il
  movimento con pendown()
- Lo studente sa elencare i quattro elementi di stato che la turtle tiene
  traccia

## Riferimenti

1. [Python turtle — Turtle graphics](https://docs.python.org/3/library/turtle.html) — documentazione ufficiale del modulo turtle
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
