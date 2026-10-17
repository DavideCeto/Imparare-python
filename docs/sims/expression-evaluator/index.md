---
title: Valutatore di Espressioni
description: Guarda un'espressione aritmetica Python ridursi un'operazione alla volta esattamente nell'ordine in cui Python la valuta, guidata da una scala di precedenza.
image: /sims/expression-evaluator/expression-evaluator.png
og:image: /sims/expression-evaluator/expression-evaluator.png
twitter:image: /sims/expression-evaluator/expression-evaluator.png
social:
   cards: false
quality_score: 93
---

# Valutatore di Espressioni

<iframe src="main.html" height="422" width="100%" scrolling="no"></iframe>

[Esegui il Valutatore di Espressioni a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

L'ordine delle operazioni viene di solito insegnato come una tabella da
memorizzare. Questo MicroSim permette agli studenti di guardarlo *accadere*:
ogni Passo Successivo evidenzia l'operazione che Python calcola subito dopo e
la riduce al suo valore, mentre una scala di precedenza mostra quale rango
("in esecuzione ora") è attivo. I preset coprono la classica sorpresa di
`2 + 3 * 4`, le parentesi, la valutazione da sinistra a destra, gli
esponenti, e la coppia `//` / `%`.

**Obiettivo di apprendimento:** Lo studente sarà in grado di valutare
un'espressione aritmetica nello stesso ordine in cui lo fa Python, un'
operazione alla volta.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *interpretare,
  eseguire, prevedere*
- **Pattern di interazione:** riduzione passo-passo con una legenda di
  precedenza dal vivo

## Come Usarlo

1. Scegli un'espressione e **prevedi la risposta finale** prima di
   procedere passo-passo.
2. Clicca **Passo Successivo**. L'evidenziazione ambra mostra l'operazione
   che Python esegue subito dopo; la scala mostra perché è stata scelta.
3. Confronta `2 + 3 * 4` con `(2 + 3) * 4` — stessi numeri, risposte diverse.
4. Prova `10 - 4 - 3` per vedere che gli operatori di pari rango vengono
   eseguiti da sinistra a destra.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/expression-evaluator/main.html"
        height="422px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 6 (Matematica e aritmetica)

### Durata

10 minuti

### Prerequisiti

- I sette operatori aritmetici, inclusi `**`, `//` e `%` (Capitolo 6)

### Attività

1. **Prevedi** (3 min): Gli studenti scrivono le risposte per tutte e
   cinque le espressioni preimpostate prima di usare la simulazione.
2. **Esegui passo-passo e verifica** (5 min): Procedi passo dopo passo per
   ogni espressione. Valuta le loro previsioni.
3. **Discuti** (2 min): "Quale previsione ti ha sorpreso di più, e quale
   regola lo spiega?"

### Verifica

- Lo studente valuta correttamente a mano una nuova espressione mista come
  `1 + 2 ** 2 * 3`
- Lo studente sa spiegare perché `10 - 4 - 3` fa 3 e non 9
- Lo studente sa indicare quando le parentesi cambiano un risultato e quando no

## Riferimenti

1. [Python Documentation — Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) — la tabella completa di precedenza
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
