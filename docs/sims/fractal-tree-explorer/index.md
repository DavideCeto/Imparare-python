---
title: Esploratore dell'Albero Frattale
description: Trascina gli slider di angolo del ramo, profondità e restringimento e guarda un albero ricorsivo ridisegnarsi istantaneamente, con ogni livello di ricorsione tinto del proprio colore.
image: /sims/fractal-tree-explorer/fractal-tree-explorer.png
og:image: /sims/fractal-tree-explorer/fractal-tree-explorer.png
twitter:image: /sims/fractal-tree-explorer/fractal-tree-explorer.png
social:
   cards: false
quality_score: 93
---

# Esploratore dell'Albero Frattale

<iframe src="main.html" height="552" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore dell'Albero Frattale a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Il frattale con la turtle del capitolo richiede un ciclo di
modifica-e-riesecuzione per ogni cambio di parametro; questo esploratore
chiude il ciclo con tre slider. Ogni livello di ricorsione è tinto del
proprio colore (tronco marrone fino a rametti verdi), il che trasforma lo
slider della profondità in una dimostrazione dal vivo dei livelli di
ricorsione. Il contatore delle "chiamate ricorsive" raddoppia più o meno a
ogni +1 di profondità — collegando la bellezza dell'albero alla pila delle
chiamate — e Istantanea mantiene un fantasma grigio così gli studenti
possono confrontare i progetti.

**Obiettivo di apprendimento:** Lo studente sarà in grado di dimostrare
come l'angolo del ramo, la profondità e il fattore di restringimento
modellano un albero ricorsivo e di progettarne uno proprio.

- **Tassonomia di Bloom (2001):** Applicare → Creare — *dimostrare,
  sperimentare, progettare*
- **Pattern di interazione:** slider dei parametri con ridisegno immediato,
  più confronto con istantanea

## Come Usarlo

1. Prevedi cosa fa il contatore delle chiamate quando la profondità passa
   da 6 a 7, poi trascina e verifica (raddoppia più o meno: due chiamate
   ricorsive per ramo).
2. Scorri lo slider dell'**angolo** da 10° a 60° — dal pioppo al banyan.
3. Clicca **Istantanea**, cambia uno slider, e confronta con il fantasma.
4. Sfida di progettazione: crea un salice piangente (angolo grande,
   restringimento alto), poi un cespuglio spelacchiato (Randomizza e
   perfeziona).

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/fractal-tree-explorer/main.html"
        height="552px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 24 (Ricorsione e frattali)

### Durata

10-15 minuti

### Prerequisiti

- Il programma ricorsivo dell'albero con la turtle (Capitolo 24)
- Il modello della pila delle chiamate (MicroSim Pila delle Chiamate Ricorsive)

### Attività

1. **Caccia al raddoppio** (4 min): Gli studenti registrano il conteggio
   delle chiamate alle profondità 4, 5, 6, 7 e descrivono il pattern
   (2^(profondità+1) − 1).
2. **Studi a uno slider** (4 min): Cambia solo l'angolo, poi solo il
   restringimento; gli studenti scrivono una frase per slider sul suo
   effetto visivo.
3. **Galleria di progetti** (5 min): Ogni studente fa un'istantanea del
   proprio albero migliore e registra i suoi tre valori di parametro
   perché un compagno lo riproduca.

### Verifica

- Lo studente prevede il conteggio approssimativo delle chiamate per una
  data profondità
- Lo studente sa mappare ogni slider alla sua riga nel codice draw_tree
  del capitolo
- Lo studente sa riprodurre un albero bersaglio dai suoi tre parametri

## Riferimenti

1. [Wikipedia — Fractal canopy](https://en.wikipedia.org/wiki/Fractal_canopy) — la famiglia di frattali a cui appartiene questo albero
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
