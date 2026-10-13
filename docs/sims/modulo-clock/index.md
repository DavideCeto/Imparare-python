---
title: Orologio del Modulo
description: Vedi il resto come un conteggio circolare su un quadrante e come puntini raggruppati in righe uguali con gli avanzi evidenziati.
image: /sims/modulo-clock/modulo-clock.png
og:image: /sims/modulo-clock/modulo-clock.png
twitter:image: /sims/modulo-clock/modulo-clock.png
social:
   cards: false
quality_score: 93
---

# Orologio del Modulo

<iframe src="main.html" height="502" width="100%" scrolling="no"></iframe>

[Esegui l'Orologio del Modulo a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

"Ciò che avanza dividendo" è una frase astratta. Questo MicroSim dà al
resto due forme concrete contemporaneamente: un quadrante da orologio che si
riavvolge al divisore (conta 17 salti intorno a un quadrante a 5 posizioni e
atterri su 2) e una vista di raggruppamento (17 puntini in righe di 5
lasciano 2 avanzi arancioni). Quando il divisore è 2, la simulazione annuncia
pari o dispari — il classico trucco `n % 2`.

**Obiettivo di apprendimento:** Lo studente sarà in grado di spiegare il
resto come conteggio circolare e di usare `%` per verificare pari/dispari e
scorrere i valori ciclicamente.

- **Tassonomia di Bloom (2001):** Comprendere → Applicare — *spiegare,
  usare, dimostrare*
- **Pattern di interazione:** slider dei parametri con riscontro visivo
  immediato

## Come Usarlo

1. Prevedi `17 % 5`, poi controlla entrambe le viste: il quadrante atterra
   sulla tua risposta e le righe di puntini la mostrano come avanzo.
2. Trascina lentamente verso l'alto lo slider **Dividendo** e osserva il
   resto ciclare 0, 1, 2, 3, 4, 0, 1, 2... — quel pattern ripetuto è il
   superpotere del modulo.
3. Imposta il **Divisore** a 2 e prova diversi dividendi: resto 0 significa
   pari, resto 1 significa dispari.
4. Trova una coppia dividendo/divisore senza avanzi. Cosa dice questo sui
   due numeri?

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/modulo-clock/main.html"
        height="502px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 6 (Matematica e aritmetica)

### Durata

10 minuti

### Prerequisiti

- Divisione e divisione intera `//` (Capitolo 6)

### Attività

1. **Prevedi** (2 min): Gli studenti calcolano a mano `17 % 5`, `20 % 4` e
   `9 % 2`.
2. **Verifica** (4 min): Controlla ognuno con gli slider. Chiedi agli
   studenti di descrivere cosa fa il quadrante quando il dividendo sale
   esattamente di un divisore.
3. **Caccia a pari/dispari** (4 min): Con divisore 2, gli studenti
   classificano cinque numeri come pari o dispari prima di muovere lo
   slider, poi verificano.

### Verifica

- Lo studente sa calcolare `n % d` per numeri piccoli senza la simulazione
- Lo studente sa spiegare perché i resti restano sempre tra 0 e divisore − 1
- Lo studente sa indicare come `n % 2` dice se n è pari

## Riferimenti

1. [Python Documentation — Binary arithmetic operations](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) — l'operatore `%`
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
