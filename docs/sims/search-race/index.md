---
title: Gara di Ricerca
description: Scegli un bersaglio ed esegui passo-passo la ricerca lineare e binaria fianco a fianco - lineare avanza faticosamente da sinistra a destra mentre binaria scarta metà scaffale a ogni controllo.
image: /sims/search-race/search-race.png
og:image: /sims/search-race/search-race.png
twitter:image: /sims/search-race/search-race.png
social:
   cards: false
quality_score: 93
---

# Gara di Ricerca

<iframe src="main.html" height="522" width="100%" scrolling="no"></iframe>

[Esegui la Gara di Ricerca a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Il Big-O è astratto finché non lo senti. Questa gara esegue la ricerca
lineare e binaria sullo stesso scaffale di 31 scatole numerate: lineare
controlla scatola dopo scatola mentre binaria controlla il centro e
oscura la metà scartata — 31 → 15 → 7 → 3 → 1. I contatori di controlli
per corsia quantificano il divario, i bersagli dispari sono assenti di
proposito (entrambe le ricerche devono scoprirlo), e il preset
**scaffale mescolato (trappola!)** offre la giustificazione chiave del
capitolo: la ricerca binaria può perdere un valore che è proprio lì,
perché dimezzare funziona solo su dati ordinati.

**Obiettivo di apprendimento:** Lo studente sarà in grado di confrontare
il numero di controlli necessari alla ricerca lineare e binaria e di
giustificare perché la ricerca binaria richiede dati ordinati.

- **Tassonomia di Bloom (2001):** Analizzare → Valutare — *confrontare,
  testare, giustificare*
- **Pattern di interazione:** scegli un bersaglio, poi esegui passo-passo o
  auto-play entrambe le ricerche fianco a fianco

## Come Usarlo

1. Prevedi entrambi i conteggi di controlli per il bersaglio 24, poi fai
   Passo e confronta.
2. Sposta il bersaglio a 62 (l'ultima scatola): lineare richiede 31
   controlli, binaria ne richiede ancora solo 5.
3. Scegli un bersaglio dispari come 33 — non è sullo scaffale. Come lo
   scopre ciascuna ricerca?
4. Passa allo **scaffale mescolato (trappola!)** e guarda la ricerca
   binaria perdersi.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/search-race/main.html"
        height="522px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 30 (Algoritmi e strutture dati)

### Durata

10-15 minuti

### Prerequisiti

- Liste e indicizzazione (Capitoli 15-16)
- La funzione binary_search del capitolo

### Attività

1. **Caccia al caso peggiore** (4 min): Gli studenti trovano il bersaglio
   che fa lavorare di più la ricerca lineare, poi quello che fa lavorare
   di più quella binaria — il caso peggiore di quella binaria è comunque
   solo 5 controlli.
2. **Canto del dimezzamento** (3 min): Esegui passo-passo la ricerca
   binaria mentre la classe scandisce l'intervallo che si restringe: 31,
   15, 7, 3, 1.
3. **La trappola** (5 min): Sullo scaffale mescolato, gli studenti trovano
   un bersaglio che la ricerca binaria manca, poi spiegano il fallimento
   in una frase.

### Verifica

- Lo studente prevede il numero massimo di controlli della ricerca
  binaria per 31 scatole (5) e per ~1000 scatole (circa 10)
- Lo studente sa spiegare perché la ricerca binaria richiede dati
  ordinati usando la trappola
- Lo studente sa indicare quale ricerca scegliere per dati non ordinati

## Riferimenti

1. [Wikipedia — Binary search](https://en.wikipedia.org/wiki/Binary_search) — l'algoritmo e la sua storia
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
