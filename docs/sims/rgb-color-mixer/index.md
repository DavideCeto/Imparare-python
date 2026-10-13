---
title: Miscelatore di Colori RGB
description: Mescola rosso, verde e blu con gli slider, leggi il codice esadecimale dal vivo con le cifre che cambiano evidenziate, e supera le sfide di abbinamento del colore.
image: /sims/rgb-color-mixer/rgb-color-mixer.png
og:image: /sims/rgb-color-mixer/rgb-color-mixer.png
twitter:image: /sims/rgb-color-mixer/rgb-color-mixer.png
social:
   cards: false
quality_score: 93
---

# Miscelatore di Colori RGB

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui il Miscelatore di Colori RGB a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

I codici esadecimali come `"#FF6B35"` sembrano formule magiche finché gli
studenti non li vedono assemblati. Questo miscelatore mostra lo stesso
colore in tre modi contemporaneamente: il campione, i tre numeri decimali,
e il codice esadecimale — con le due cifre esadecimali di ogni canale
colorate per corrispondere al proprio slider, e il canale mosso per ultimo
evidenziato. Una riga `t.pencolor("#...")` pronta da copiare collega la
simulazione direttamente ai laboratori con la turtle del capitolo, e la
modalità sfida trasforma l'abbinamento dei colori in un gioco con un
misuratore di vicinanza.

**Obiettivo di apprendimento:** Lo studente sarà in grado di produrre un
colore bersaglio regolando i valori di rosso, verde e blu e di
leggere/scrivere il suo codice esadecimale.

- **Tassonomia di Bloom (2001):** Applicare — *usare, dimostrare, risolvere*
- **Pattern di interazione:** slider dei parametri con riscontro immediato
  più una sfida di abbinamento del colore

## Come Usarlo

1. Trascina uno slider alla volta e osserva quali due cifre esadecimali
   cambiano.
2. Mescola questi classici: giallo (R alto, G alto, B basso), viola (R
   alto, G basso, B alto), e grigio (tutti e tre uguali).
3. Clicca **Nuova Sfida** e regola gli slider finché il misuratore di
   vicinanza non dice "Abbinato!"
4. Copia la riga `t.pencolor(...)` in qualsiasi laboratorio con la turtle
   del Capitolo 12.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/rgb-color-mixer/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 12 (Colori, riempimento e arte con la turtle)

### Durata

10 minuti

### Prerequisiti

- Colori della penna della turtle con nomi di colore (Capitolo 5)

### Attività

1. **Prevedi la miscela** (3 min): Gli studenti prevedono le impostazioni
   degli slider per giallo, bianco, nero e grigio, poi verificano.
2. **Detective dell'esadecimale** (3 min): Dato `"#00FF00"`, gli studenti
   dicono di che colore si tratta prima di mescolarlo.
3. **Round di sfida** (4 min): Tre colori di Nuova Sfida; gli studenti
   registrano il codice esadecimale di ogni abbinamento.

### Verifica

- Lo studente produce un colore con nome (arancione, viola, verde acqua)
  entro due tentativi
- Lo studente sa spiegare quali cifre esadecimali appartengono a quale
  canale
- Lo studente sa leggere a colpo d'occhio un semplice codice esadecimale
  come `"#FF0000"`

## Riferimenti

1. [Python turtle — colormode and pencolor](https://docs.python.org/3/library/turtle.html#turtle.pencolor) — documentazione ufficiale dei colori della turtle
2. [MDN — Hex color notation](https://developer.mozilla.org/en-US/docs/Web/CSS/hex-color) — come funzionano i colori esadecimali sul web
3. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
