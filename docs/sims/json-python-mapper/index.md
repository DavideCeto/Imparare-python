---
title: Mappatore dei Tipi da JSON a Python
description: Modifica il JSON a sinistra e guarda gli oggetti Python che diventa a destra, con true/True, null/None, e ogni abbinamento di tipo colorato.
image: /sims/json-python-mapper/json-python-mapper.png
og:image: /sims/json-python-mapper/json-python-mapper.png
twitter:image: /sims/json-python-mapper/json-python-mapper.png
social:
   cards: false
quality_score: 95
---

# Mappatore dei Tipi da JSON a Python

<iframe src="main.html" height="442" width="100%" scrolling="no"></iframe>

[Esegui il Mappatore dei Tipi da JSON a Python a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

Il JSON sembra ingannevolmente simile a Python, quindi le differenze
(`true` contro `True`, `null` contro `None`, solo virgolette doppie,
niente virgole finali) causano confusione silenziosa. Questo mappatore a
due pannelli rende visibile la conversione: modifica il JSON a sinistra e
l'oggetto Python che `json.loads()` costruirebbe si ridisegna dal vivo a
destra, con ogni abbinamento di tipo colorato e tooltip al passaggio del
mouse che nominano entrambi i tipi. Due preset deliberatamente rotti
mostrano i classici errori JSON con spiegazioni amichevoli invece di
criptici errori del parser.

**Obiettivo di apprendimento:** Lo studente sarà in grado di convertire
valori tra testo JSON e oggetti Python e di identificare la mappatura dei
tipi in ciascuna direzione.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *interpretare,
  convertire, classificare*
- **Pattern di interazione:** modifica dal vivo a due pannelli con codifica
  a colori per tipo
- **Libreria:** HTML personalizzato (nessuna libreria di grafici necessaria)

## Come Usarlo

1. Prevedi cosa diventano `true` e `null`, poi controlla il preset **Il
   trio insidioso**.
2. Modifica il pannello sinistro: aggiungi una nuova chiave, cambia un
   numero in un decimale, annida una lista — il pannello destro segue ogni
   battitura.
3. Prova entrambi i preset **Rotti** e leggi la spiegazione amichevole del
   perché JSON rifiuta ciò che Python accetterebbe.
4. Passa il mouse sui valori colorati a destra per leggere l'abbinamento
   di tipo.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/json-python-mapper/main.html"
        height="442px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 27 (Libreria standard e JSON)

### Durata

10 minuti

### Prerequisiti

- Dizionari e liste (Capitoli 15 e 21)
- json.loads() e json.dumps() (Capitolo 27)

### Attività

1. **Esercizio del trio** (3 min): Gli studenti scrivono a memoria gli
   equivalenti Python di `true`, `false` e `null`, poi verificano con il
   preset.
2. **Costruisci un record** (4 min): Gli studenti scrivono JSON che
   descrive se stessi (nome, età, lista di hobby) e confermano i tipi
   Python a destra.
3. **Caccia ai bug** (3 min): Usando i preset rotti, gli studenti indicano
   l'unica modifica che corregge ogni errore.

### Verifica

- Lo studente converte su carta un frammento JSON nel suo letterale Python
- Lo studente sa nominare le due regole JSON che Python non condivide
- Lo studente sa spiegare perché le chiavi JSON sono sempre stringhe

## Riferimenti

1. [Python Documentation — json module](https://docs.python.org/3/library/json.html) — documentazione ufficiale con la tabella completa di conversione
2. [json.org](https://www.json.org/json-en.html) — lo standard JSON
