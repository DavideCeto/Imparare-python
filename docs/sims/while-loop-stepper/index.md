---
title: Esecutore Passo-Passo del Ciclo While
description: Esegui passo-passo un ciclo while attraverso il suo ritmo controlla-condizione, esegui-corpo con i verdetti True/False timbrati a ogni controllo - e vivi in sicurezza un ciclo infinito.
image: /sims/while-loop-stepper/while-loop-stepper.png
og:image: /sims/while-loop-stepper/while-loop-stepper.png
twitter:image: /sims/while-loop-stepper/while-loop-stepper.png
social:
   cards: false
quality_score: 93
---

# Esecutore Passo-Passo del Ciclo While

<iframe src="main.html" height="502" width="100%" scrolling="no"></iframe>

[Esegui l'Esecutore Passo-Passo del Ciclo While a Schermo Intero](./main.html){ .md-button .md-button--primary }
<br/>
[Modifica nell'Editor p5.js](https://editor.p5js.org/)

## Informazioni su questo MicroSim

Il cuore invisibile di un ciclo while è il controllo ripetuto della
condizione. Questo esecutore passo-passo fa visitare fisicamente alla
freccia la riga `while` prima di ogni giro e vi timbra un verdetto
True/False, così gli studenti interiorizzano il ritmo
controlla-esegui-controlla. Il preset **Bug Infinito** è il classico bug del
decremento mancante eseguito dentro una gabbia sicura: il contachilometri
dei giri gira, il verdetto timbra True per sempre, e un banner di avviso
spiega la correzione — un'esperienza che i limiti di sicurezza di Skulpt
normalmente impediscono.

**Obiettivo di apprendimento:** Lo studente sarà in grado di tracciare i
controlli della condizione di un ciclo while e di identificare perché un
ciclo termina — o non termina mai.

- **Tassonomia di Bloom (2001):** Comprendere → Analizzare — *tracciare,
  prevedere, debuggare*
- **Pattern di interazione:** esecuzione passo-passo con una fase esplicita
  di controllo della condizione e una dimostrazione sandbox di ciclo
  infinito

## Come Usarlo

1. Con **Conto alla Rovescia**, prevedi: quante volte viene eseguito il
   corpo, e quante volte viene controllata la condizione? Esegui passo-passo
   e conta i timbri. (3 giri, 4 controlli — l'ultimo controllo dice False.)
2. Prova **Raddoppia Fino a 100** — il ciclo si ferma a 192, non a 100.
   Perché?
3. Scegli **Bug Infinito** e continua a cliccare: la condizione è True ogni
   singola volta perché niente nel corpo cambia `count`.

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/while-loop-stepper/main.html"
        height="502px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 10 (Cicli while e animazione)

### Durata

10-15 minuti

### Prerequisiti

- Cicli for (Capitolo 7) e operatori di confronto (Capitolo 9)

### Attività

1. **Conta i controlli** (5 min): Gli studenti contano i controlli della
   condizione rispetto alle esecuzioni del corpo per il preset Conto alla
   Rovescia, scoprendo che controlli = giri + 1.
2. **Superamento** (4 min): Con Raddoppia Fino a 100, chiedi agli studenti
   di prevedere il valore stampato prima di procedere passo-passo. La
   maggior parte dice 100; la simulazione mostra 192.
3. **Debug** (4 min): Con Bug Infinito, gli studenti scrivono l'unica riga
   che correggerebbe il ciclo, poi spiegano dove deve andare e perché.

### Verifica

- Lo studente sa esprimere a parole proprie il ritmo
  controlla-esegui-controlla
- Lo studente identifica la riga mancante in un ciclo di conto alla
  rovescia infinito
- Lo studente spiega perché la variabile di un ciclo while deve cambiare
  dentro il corpo

## Riferimenti

1. [Python Tutorial — while Statements](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) — documentazione ufficiale
2. [p5.js](https://p5js.org/) — la libreria JavaScript usata per costruire questo MicroSim
