---
title: Laboratorio di Logica Booleana
description: Imposta input True/False che alimentano and, or e not, guarda una lampada del risultato, e vedi la valutazione a corto circuito oscurare l'operando che Python non controlla mai.
image: /sims/boolean-logic-lab/boolean-logic-lab.png
og:image: /sims/boolean-logic-lab/boolean-logic-lab.png
twitter:image: /sims/boolean-logic-lab/boolean-logic-lab.png
social:
   cards: false
quality_score: 93
---

# Laboratorio di Logica Booleana

<iframe src="main.html" height="512" width="100%" scrolling="no"></iframe>

[Esegui il Laboratorio di Logica Booleana a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Le tabelle di verità vengono di solito memorizzate; questo laboratorio
permette agli studenti di *costruirle*. Due input True/False alimentano un
blocco operatore (`and`, `or`, `not`) collegato a una lampada del risultato.
Il laboratorio rende visibile anche la valutazione a corto circuito: quando
l'input A da solo decide la risposta (`False and ...`, `True or ...`), il
blocco B si oscura con un distintivo "Python non ha mai guardato qui." Un
pannello di veridicità mostra i verdetti di `bool()` per valori come `0`,
`""`, `[]` e `None`, anticipando il Capitolo 19.

**Obiettivo di apprendimento:** Lo studente sarà in grado di determinare il
risultato di espressioni `and`, `or` e `not` e di spiegare quando Python
salta la valutazione del secondo operando.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *classificare,
  spiegare, dimostrare*
- **Pattern di interazione:** selettori di input con una visualizzazione
  immediata del circuito e della lampada

## Come Usarlo

1. Costruisci tutte e quattro le righe della tabella di verità di `and`
   provando ogni combinazione A/B. Quale singola combinazione accende la
   lampada?
2. Passa a `or` e trova l'unica combinazione che NON la accende.
3. Imposta A a False con `and` — osserva B oscurarsi. Cambia B: il
   risultato cambia mai? Questa è la valutazione a corto circuito.
4. Nel pannello bonus, prova `bool(0)`, `bool("")` e `bool([3, 7])`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/boolean-logic-lab/main.html"
        height="512px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitoli 9 e 19

### Durata

10 minuti

### Prerequisiti

- Operatori di confronto che producono True/False (Capitolo 9)

### Attività

1. **Costruisci le tabelle** (4 min): Gli studenti registrano tutte e
   quattro le combinazioni per `and` e `or` in una tabella di verità su
   carta, usando il laboratorio per verificare.
2. **Scoperta del corto circuito** (3 min): "Impostalo così che cambiare B
   non faccia nulla. In quanti modi puoi farlo?" (Due: False-and, True-or.)
3. **Classificazione di veridicità** (3 min): Gli studenti prevedono
   True/False per tutti gli otto valori bonus, poi verificano.

### Verifica

- Lo studente completa le tabelle di verità di and/or a memoria
- Lo studente sa nominare le due situazioni di corto circuito
- Lo studente sa classificare 0, "", [] e None come falsi

## Riferimenti

1. [Python Documentation — Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) — incluso il comportamento di corto circuito
2. [Python Documentation — Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) — l'elenco dei valori falsi
3. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
