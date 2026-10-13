---
title: Esploratore dell'Ereditarietà
description: Clicca una chiamata a un metodo e guarda la ricerca risalire l'albero delle classi finché non si evidenzia una corrispondenza - i metodi del genitore sovrascritti appaiono oscurati, e super() risale esplicitamente.
image: /sims/inheritance-explorer/inheritance-explorer.png
og:image: /sims/inheritance-explorer/inheritance-explorer.png
twitter:image: /sims/inheritance-explorer/inheritance-explorer.png
social:
   cards: false
quality_score: 95
---

# Esploratore dell'Ereditarietà

<iframe src="main.html" height="507" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore dell'Ereditarietà a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

Quando chiami un metodo su un oggetto, Python esegue una ricerca invisibile:
guarda prima nella classe propria dell'oggetto, poi risale genitore per
genitore. Questo esploratore rende visibile il dispacciamento. L'albero
delle classi (`Animal` con i figli `Dog` e `Cat`, e un'istanza `d` sotto
Dog) è un diagramma dal vivo; ogni pulsante di chiamata anima la ricerca
balzo dopo balzo con un registro in linguaggio semplice. `d.eat()` manca su
Dog e risale ad Animal (ereditarietà); `d.speak()` si ferma su Dog mentre
la copia di Animal viene segnata come *oscurata* (sovrascrittura); il
preset `super()` mostra un figlio che risale deliberatamente per eseguire
anche la versione del genitore.

**Obiettivo di apprendimento:** Lo studente sarà in grado di determinare il
metodo di quale classe viene eseguito quando un metodo viene chiamato su
un'istanza di una sottoclasse.

- **Tassonomia di Bloom (2001):** Analizzare — *attribuire, organizzare,
  differenziare*
- **Pattern di interazione:** animazione di ricerca clicca-una-chiamata con
  un registro balzo per balzo
- **Libreria:** vis-network (gerarchia delle classi come nodi e archi;
  zoom/pan del mouse disabilitati, pulsanti di navigazione abilitati)

## Come Usarlo

1. Prevedi dove vive ciascuno dei tre metodi, poi clicca **d.fetch()**,
   **d.speak()** e **d.eat()** e segui le evidenziazioni.
2. Nota che `d.eat()` richiede un balzo extra — Dog non definisce mai
   `eat()`, lo eredita.
3. Dopo `d.speak()`, guarda la scatola di Animal: il suo `speak()` è
   segnato come oscurato. La versione del genitore non è mai stata
   eseguita.
4. Clicca il pulsante **super()** per vedere come un figlio può eseguire di
   proposito il metodo del genitore.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/inheritance-explorer/main.html"
        height="507px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 25 (Programmazione orientata agli oggetti)

### Durata

10 minuti

### Prerequisiti

- Classi, istanze e self (Capitolo 25; MicroSim Ispettore delle Istanze
  degli Oggetti)

### Attività

1. **Prevedi i balzi** (4 min): Per ciascuna delle tre chiamate, gli
   studenti scrivono quanti balzi farà la ricerca prima di cliccare.
2. **Sovrascrittura contro ereditarietà** (3 min): Gli studenti spiegano in
   una frase perché `d.speak()` e `d.eat()` finiscono in classi diverse.
3. **Discussione su super()** (3 min): "Quando un figlio vorrebbe eseguire
   anche la versione del genitore?" (Esempio: aggiungere qualcosa al
   saluto di un genitore.)

### Verifica

- Lo studente sa tracciare quale classe risponde a qualsiasi chiamata di
  metodo su un'istanza di Dog
- Lo studente sa definire sovrascrittura ed ereditarietà usando l'albero
- Lo studente sa spiegare cosa cambia super() nella ricerca

## Riferimenti

1. [Python Tutorial — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance) — documentazione ufficiale
2. [vis-network](https://visjs.github.io/vis-network/docs/network/) — la libreria di rete usata per costruire questo MicroSim
