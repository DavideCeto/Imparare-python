---
title: Esploratore di Attraversamento del Grafo
description: Esegui passo-passo BFS e DFS sullo stesso grafo, guardando i nodi illuminarsi in ordine di visita mentre la coda o la pila dal vivo che guida ciascun algoritmo viene mostrata accanto al grafo.
image: /sims/graph-traversal-explorer/graph-traversal-explorer.png
og:image: /sims/graph-traversal-explorer/graph-traversal-explorer.png
twitter:image: /sims/graph-traversal-explorer/graph-traversal-explorer.png
social:
   cards: false
quality_score: 95
---

# Esploratore di Attraversamento del Grafo

<iframe src="main.html" height="537" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore di Attraversamento del Grafo a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

L'ondulazione livello-per-livello di BFS e l'immersione profonda di DFS
differiscono per un'unica ragione: la struttura dati che contiene la
frontiera. Questo esploratore mantiene quella struttura sullo schermo —
la **coda** dal vivo (BFS) o la **pila** (DFS) si aggiorna dopo ogni
Passo, e ogni nodo visitato riceve il suo numero di visita timbrato sopra.
Dopo che BFS completa, il passo finale evidenzia il percorso più breve dal
nodo di partenza A all'obiettivo J, la classica ricompensa del "perché
BFS"; DFS sullo stesso grafo produce un ordine completamente diverso
perché la pila afferra sempre la scoperta più recente. Il nodo di
partenza è fissato ad A così i due attraversamenti restano direttamente
confrontabili.

**Obiettivo di apprendimento:** Lo studente sarà in grado di tracciare
l'ordine di visita di BFS e DFS sullo stesso grafo e di attribuire la
differenza alla coda contro la pila.

- **Tassonomia di Bloom (2001):** Analizzare — *differenziare,
  organizzare, tracciare*
- **Pattern di interazione:** esecuzione passo-passo con la struttura dati
  della frontiera mostrata dal vivo
- **Libreria:** vis-network (zoom/pan del mouse disabilitati, pulsanti di
  navigazione abilitati)

## Come Usarlo

1. In modalità BFS, prevedi le prime quattro visite, poi fai Passo e
   controlla la coda dopo ciascuna.
2. Procedi fino alla fine — il click finale rivela il percorso più breve
   da A a J.
3. Passa a DFS e procedi di nuovo: stesso grafo, stesso inizio. Dove i due
   ordini divergono per la prima volta, e quale voce della frontiera lo
   spiega?
4. Osserva il nodo E in BFS: viene visitato ma non scopre "nulla di
   nuovo" — tutto intorno a lui era già stato trovato.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/graph-traversal-explorer/main.html"
        height="537px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 30 (Algoritmi e strutture dati); rafforza i contenuti sul labirinto nella sezione intermedia

### Durata

15 minuti

### Prerequisiti

- Pile e code (Capitolo 16 e il Simulatore di Pila e Coda)
- Grafi come nodi e archi (Capitolo 30)

### Attività

1. **Prevedi l'ondulazione** (5 min): Gli studenti scrivono l'ordine di
   visita atteso di BFS per l'intero grafo, poi verificano passo dopo
   passo.
2. **Prima divergenza** (4 min): Gli studenti trovano il primo passo in
   cui l'ordine di DFS differisce da quello di BFS e lo spiegano usando il
   pannello della frontiera.
3. **Percorso più breve** (4 min): Dopo il passo di ricompensa di BFS, gli
   studenti tracciano il percorso evidenziato e spiegano perché
   l'esplorazione livello-per-livello lo garantisce più breve.

### Verifica

- Lo studente produce a mano l'ordine di visita BFS per un nuovo piccolo
  grafo
- Lo studente sa indicare quale struttura dati produce quale attraversamento
- Lo studente sa spiegare perché BFS trova i percorsi più brevi e DFS
  potrebbe non trovarli

## Riferimenti

1. [Wikipedia — Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) — l'algoritmo e le sue proprietà
2. [vis-network](https://visjs.github.io/vis-network/docs/network/) — la libreria di rete usata per costruire questo MicroSim
