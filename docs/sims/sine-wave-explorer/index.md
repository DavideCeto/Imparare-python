---
title: Esploratore dell'Onda Sinusoidale
description: Trascina gli slider di ampiezza, frequenza e fase e guarda y = A*sin(f*x + p) ridisegnarsi istantaneamente, con un'equazione dal vivo e una curva di riferimento sin(x) semplice.
image: /sims/sine-wave-explorer/sine-wave-explorer.png
og:image: /sims/sine-wave-explorer/sine-wave-explorer.png
twitter:image: /sims/sine-wave-explorer/sine-wave-explorer.png
social:
   cards: false
quality_score: 95
---

# Esploratore dell'Onda Sinusoidale

<iframe src="main.html" height="492" width="100%" scrolling="no"></iframe>

[Esegui l'Esploratore dell'Onda Sinusoidale a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

Il progetto con la turtle e l'onda sinusoidale del capitolo funziona, ma
ogni cambio di parametro richiede un ciclo di modifica-e-riesecuzione.
Questo esploratore chiude il ciclo di riscontro: gli slider di ampiezza,
frequenza e fase ridisegnano `y = A × sin(f·x + p)` istantaneamente,
l'equazione sostituita si aggiorna dal vivo, e una curva di riferimento
tratteggiata `sin(x)` semplice rende ogni cambiamento misurabile rispetto
alla stessa base di confronto.

**Obiettivo di apprendimento:** Lo studente sarà in grado di dimostrare
come ampiezza, frequenza e fase cambino ciascuna la forma di un'onda
sinusoidale.

- **Tassonomia di Bloom (2001):** Applicare — *dimostrare, usare, risolvere*
- **Pattern di interazione:** slider dei parametri con ridisegno immediato
- **Libreria:** Plotly.js (grafico di funzione matematica con tooltip al
  passaggio del mouse)

## Come Usarlo

1. Prevedi quale slider rende l'onda più alta, poi prova ogni slider uno
   alla volta.
2. Seleziona **mostra sin(x) semplice** e scorri la fase — la tua onda
   scivola a sinistra rispetto al riferimento tratteggiato.
3. Imposta la frequenza a 2: quante onde complete entrano ora tra 0 e 4π?
4. Passa il mouse sulla curva per leggere i valori esatti (x, y).

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/sine-wave-explorer/main.html"
        height="492px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 18 (Modulo math e progetti con la turtle)

### Durata

10 minuti

### Prerequisiti

- math.sin() e il progetto con la turtle e l'onda sinusoidale (Capitolo 18)

### Attività

1. **Uno slider alla volta** (4 min): Gli studenti descrivono in una frase
   cosa cambia ogni slider, mantenendo fissi gli altri due.
2. **Gara col riferimento** (3 min): Con il sin(x) tratteggiato attivo, gli
   studenti impostano A = 2, f = 2 e contano quanti picchi di riferimento
   entrano sotto uno dei loro.
3. **Abbina la turtle** (3 min): Gli studenti trovano le impostazioni degli
   slider che corrispondono visivamente alla forma d'onda del progetto con
   la turtle `amplitude = 80, frequency = 0.05`.

### Verifica

- Lo studente nomina correttamente il parametro che controlla altezza,
  numero di ondulazioni, e spostamento sinistra-destra
- Lo studente sa disegnare y = 2 sin(x) contro y = sin(2x) senza la
  simulazione
- Lo studente collega gli slider alle variabili del progetto con la turtle

## Riferimenti

1. [Python Documentation — math.sin](https://docs.python.org/3/library/math.html#math.sin) — documentazione ufficiale
2. [Plotly.js Documentation](https://plotly.com/javascript/) — la libreria di grafici usata
