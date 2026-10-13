---
title: Modello di Memoria delle Variabili
description: Percorri passo-passo un breve script Python e guarda scatole di memoria etichettate venire create, lette e sostituite man mano che ogni assegnazione viene eseguita.
image: /sims/variable-memory-model/variable-memory-model.png
og:image: /sims/variable-memory-model/variable-memory-model.png
twitter:image: /sims/variable-memory-model/variable-memory-model.png
social:
   cards: false
quality_score: 93
---

# Modello di Memoria delle Variabili

<iframe src="main.html" height="482" width="100%" scrolling="no"></iframe>

[Esegui il Modello di Memoria delle Variabili a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

`score = 10` è magia invisibile finché non riesci a vedere la scatola. Questo
MicroSim rende operativa la metafora del post-it: ogni assegnazione crea o
aggiorna una scatola di memoria etichettata, ogni lettura evidenzia in blu la
scatola osservata, e ogni riassegnazione mostra il vecchio valore mentre
viene sostituito (con una piccola nota "era 10" così gli studenti vedono che
il vecchio valore è sparito).

**Obiettivo di apprendimento:** Lo studente sarà in grado di spiegare cosa
succede in memoria quando una variabile viene creata, letta e riassegnata.

- **Tassonomia di Bloom (2001):** Comprendere — *spiegare, interpretare, prevedere*
- **Pattern di interazione:** esempio guidato passo-passo con scatole di
  memoria etichettate (nessuna animazione)

## Come Usarlo

1. Leggi lo script a sinistra e **prevedi quante scatole esisteranno**
   quando finisce, e cosa conterrà ciascuna.
2. Clicca **Passo Successivo** per eseguire una riga. L'arancione significa
   che una scatola viene **scritta**; il blu significa che una scatola viene
   **letta**.
3. Osserva attentamente `score = score + 5`: Python legge prima il vecchio
   valore, poi lo sostituisce.
4. Prova tutti e tre i programmi. **Sorpresa della Copia** risponde a una
   domanda classica: dopo `b = a`, cambiare `a` cambia anche `b`?

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/variable-memory-model/main.html"
        height="482px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 3 (Variabili e numeri)

### Durata

10 minuti

### Prerequisiti

- print() e l'idea che i programmi vengono eseguiti dall'alto verso il
  basso (Capitoli 1-2)

### Attività

1. **Prevedi** (3 min): Per lo script "Punteggio di Gioco", gli studenti
   scrivono il valore finale di ogni variabile prima di procedere passo-passo.
2. **Esegui passo-passo e verifica** (4 min): Procedi passo dopo passo e
   confronta. Fermati su `score = score + 5` e chiedi: "Cosa succede prima —
   la lettura o la scrittura?"
3. **Sorpresa della Copia** (3 min): Gli studenti prevedono cosa mostra
   `print(b)` dopo `a = 7`. La maggior parte si aspetta 7; la simulazione
   mostra perché è 5.

### Verifica

- Lo studente sa affermare che l'assegnazione memorizza un valore e la
  riassegnazione lo sostituisce
- Lo studente prevede correttamente l'output di uno script di 4 righe che
  usa la riassegnazione
- Lo studente sa spiegare perché cambiare `a` dopo `b = a` non cambia `b`

## Riferimenti

1. [Python Tutorial — Numbers and Variables](https://docs.python.org/3/tutorial/introduction.html) — introduzione ufficiale all'assegnazione
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
