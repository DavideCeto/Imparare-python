---
title: Ricerca delle Chiavi nel Dizionario
description: Digita una chiave e guarda il cassetto corrispondente scattare aperto - o incontra un KeyError - poi fai gareggiare un dizionario contro una lista per sentire perché la ricerca nel dizionario è un solo balzo.
image: /sims/dictionary-key-lookup/dictionary-key-lookup.png
og:image: /sims/dictionary-key-lookup/dictionary-key-lookup.png
twitter:image: /sims/dictionary-key-lookup/dictionary-key-lookup.png
social:
   cards: false
quality_score: 93
---

# Ricerca delle Chiavi nel Dizionario

<iframe src="main.html" height="532" width="100%" scrolling="no"></iframe>

[Esegui la Ricerca delle Chiavi nel Dizionario a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Perché la ricerca nel dizionario è istantanea, e perché una chiave mancante
fa crashare? Questa simulazione disegna il dizionario come un mobile di
cassetti con le chiavi scritte sulle ante. Una chiave digitata fa scattare
aperto il cassetto corrispondente in "un solo balzo"; una chiave mancante
mostra il vero banner `KeyError` — oppure, con l'interruttore `.get()`, un
educato `None`. La modalità di confronto mette gli stessi dati in una
lista e conta quanti elementi devono essere controllati uno per uno,
piantando il seme dell'efficienza senza alcun gergo sulle tabelle hash.

**Obiettivo di apprendimento:** Lo studente sarà in grado di spiegare come
un dizionario trova un valore da una chiave e perché una chiave mancante
solleva KeyError mentre `.get()` no.

- **Tassonomia di Bloom (2001):** Comprendere — *spiegare, confrontare,
  dedurre*
- **Pattern di interazione:** ricerca digita-una-chiave con una modalità di
  confronto lista-contro-dizionario

## Come Usarlo

1. Cerca `grace` — il cassetto si apre in un balzo.
2. Prova `Grace` con la G maiuscola: le chiavi devono corrispondere
   esattamente, quindi ottieni un `KeyError`.
3. Seleziona **usa .get()** e ripeti: `None` invece di un crash.
4. Seleziona **confronta con una ricerca in lista** e cerca `guido` (l'ultimo
   cassetto): la lista controlla tutti e cinque gli elementi; il dizionario
   impiega comunque un solo balzo.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/dictionary-key-lookup/main.html"
        height="532px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 21 (Dizionari)

### Durata

10 minuti

### Prerequisiti

- Creare dizionari e accedere ai valori tramite chiave (sezioni iniziali
  del Capitolo 21)
- Liste e l'operatore in (Capitoli 15-16)

### Attività

1. **Esercizio di corrispondenza esatta** (3 min): Gli studenti prevedono
   il risultato per `grace`, `Grace` e `gracie`, poi testano tutte e tre.
2. **Crash contro None** (3 min): Stessa chiave mancante con le parentesi e
   con .get(); gli studenti scrivono una frase su quando sceglierebbero
   ciascuno.
3. **La gara** (4 min): Con il confronto attivo, gli studenti cercano la
   prima, la media e l'ultima chiave e registrano i conteggi dei controlli
   della lista contro quelli del dizionario.

### Verifica

- Lo studente sa spiegare perché `phone_book["Grace"]` fallisce quando la
  chiave è `"grace"`
- Lo studente sa indicare cosa restituisce `.get()` per una chiave mancante
- Lo studente sa spiegare perché i dizionari sono più veloci delle liste
  per le ricerche

## Riferimenti

1. [Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
