---
title: Cerchio Unitario — Gradi e Radianti
description: Trascina un punto intorno al cerchio unitario e leggi l'angolo in gradi, radianti e multipli di pi greco, con linee di proiezione di sin e cos e una turtle rotante.
image: /sims/unit-circle-radians/unit-circle-radians.png
og:image: /sims/unit-circle-radians/unit-circle-radians.png
twitter:image: /sims/unit-circle-radians/unit-circle-radians.png
social:
   cards: false
quality_score: 93
---

# Cerchio Unitario — Gradi e Radianti

<iframe src="main.html" height="522" width="100%" scrolling="no"></iframe>

[Esegui il Cerchio Unitario a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Gli studenti incontrano gli angoli due volte in questo libro, parlando due
lingue: la turtle usa i gradi, ma `math.sin()` richiede i radianti. Questa
simulazione ancora la conversione nello spazio. Trascina il punto arancione
intorno al cerchio unitario e leggi lo stesso angolo in tre modi — gradi,
radianti, e multipli di π — mentre barre di proiezione blu e verdi mostrano
`sin` e `cos`, e una turtle al centro ruota per corrispondere alla
direzione.

**Obiettivo di apprendimento:** Lo studente sarà in grado di convertire tra
gradi e radianti e di localizzare un angolo sul cerchio unitario.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *interpretare,
  convertire, usare*
- **Pattern di interazione:** manipolazione diretta (trascina il punto
  dell'angolo) con letture doppie dal vivo e pulsanti di aggancio ai punti
  di riferimento

## Come Usarlo

1. Trascina il punto arancione a 180° — la lettura in radianti mostra π
   (circa 3.14). Un giro completo è 2π.
2. Usa i pulsanti di aggancio per visitare gli angoli di riferimento e
   nota i loro valori in radianti (90° = 0.50π, 45° = 0.25π).
3. Osserva la barra blu del **sin**: dove è più lunga? Dove è zero?
4. Osserva la turtle al centro — la sua direzione è l'angolo, collegando
   `t.setheading(90)` a `math.radians(90)`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/unit-circle-radians/main.html"
        height="522px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 18 (Modulo math e progetti con la turtle)

### Durata

10 minuti

### Prerequisiti

- Direzioni della turtle in gradi (Capitolo 5)
- math.sin() e math.cos() (Capitolo 18)

### Attività

1. **Giro dei punti di riferimento** (4 min): Gli studenti visitano ogni
   angolo di aggancio e registrano gradi, radianti e il multiplo di π in
   una tabella a tre colonne.
2. **Caccia al sin** (3 min): "Trascina finché sin = 1. Dove sei? Trascina
   finché sin = 0. Quanti punti riesci a trovare?"
3. **Converti a mano** (3 min): Gli studenti calcolano i radianti per 60°
   usando la formula, poi verificano trascinando.

### Verifica

- Lo studente converte 90°, 180° e 360° in radianti senza la simulazione
- Lo studente sa indicare dove sin è massimo e dove cos è massimo
- Lo studente sa spiegare perché math.sin(90) non dà 1

## Riferimenti

1. [Python Documentation — math.radians](https://docs.python.org/3/library/math.html#math.radians) — funzione di conversione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
