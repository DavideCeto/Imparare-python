---
title: Simulatore di Pila e Coda
description: Dai in pasto gli stessi elementi a una pila di piatti e a una fila d'attesa, poi rimuovili e confronta fianco a fianco gli ordini LIFO e FIFO.
image: /sims/stack-queue-simulator/stack-queue-simulator.png
og:image: /sims/stack-queue-simulator/stack-queue-simulator.png
twitter:image: /sims/stack-queue-simulator/stack-queue-simulator.png
social:
   cards: false
quality_score: 93
---

# Simulatore di Pila e Coda

<iframe src="main.html" height="512" width="100%" scrolling="no"></iframe>

[Esegui il Simulatore di Pila e Coda a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

LIFO contro FIFO è una differenza nell'*ordine temporale*, che il solo
output del codice non può mostrare. Questo simulatore lo trasforma in un
esperimento controllato: un pulsante Aggiungi alimenta l'elemento identico
a entrambe le strutture, così l'unica differenza che gli studenti vedono è
l'uscita. `stack.pop()` solleva il piatto più nuovo dalla cima;
`queue.pop(0)` rilascia l'elemento più vecchio dal fronte. Le strisce della
cronologia delle rimozioni danno la battuta finale — la pila restituisce
gli elementi invertiti, la coda nell'ordine originale.

**Obiettivo di apprendimento:** Lo studente sarà in grado di prevedere
l'ordine di rimozione degli elementi da una pila rispetto a una coda e di
abbinare ciascuno alle sue operazioni di lista.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *confrontare,
  dimostrare, prevedere*
- **Pattern di interazione:** push/pop guidati da pulsanti con un confronto
  controllato fianco a fianco

## Come Usarlo

1. Clicca **Aggiungi Elemento** quattro volte — le stesse lettere entrano
   in entrambe le strutture.
2. Prevedi quale lettera rilascerà ciascun pulsante Rimuovi, poi clicca e
   verifica la riga dell'operazione.
3. Svuota entrambe le strutture e leggi le due strisce di cronologia:
   ordine invertito contro ordine originale.
4. Nota il codice: entrambe usano `append()` per aggiungere; solo la
   rimozione è diversa.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/stack-queue-simulator/main.html"
        height="512px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 16 (Liste - Metodi e pattern); ripreso nel Capitolo 30

### Durata

10 minuti

### Prerequisiti

- append() e pop() delle liste (Capitolo 16)

### Attività

1. **Esperimento controllato** (4 min): Aggiungi A-D, prevedi entrambe le
   prime uscite, rimuovi una da ciascuna, verifica.
2. **Gara di cronologia** (3 min): Svuota entrambe le strutture; gli
   studenti scrivono i due ordini di cronologia e nominano i pattern
   (LIFO/FIFO).
3. **Abbinamento al mondo reale** (3 min): Gli studenti abbinano scenari a
   strutture: pulsante annulla (pila), coda di stampa (coda), pulsante
   indietro del browser (pila), fila per il pranzo (coda).

### Verifica

- Lo studente prevede l'ordine di rimozione per entrambe le strutture dopo
  qualsiasi sequenza di aggiunte
- Lo studente sa indicare quale metodo di lista crea una pila contro una
  coda
- Lo studente nomina un esempio del mondo reale per ciascuna

## Riferimenti

1. [Python Tutorial — Using Lists as Stacks and Queues](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
