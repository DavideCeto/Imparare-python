---
title: Variabili e Numeri
description: Scopri come creare variabili, memorizzare interi e numeri decimali, seguire le convenzioni di denominazione di Python e capire il valore None.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 08:55:45
version: 0.09
---

# Variabili e Numeri

Alla fine di questa lezione sarai in grado di:

- Creare una variabile in Python e memorizzare un numero al suo interno
- Dare un nome alle variabili usando lo `snake_case` e scegliere nomi chiari e descrittivi
- Spiegare la differenza tra un numero intero e un numero decimale

Immagina di giocare a un videogioco e di dover ricordare il tuo punteggio.
Potresti provare a tenerlo a mente — ma cosa succede se cambia?
E se ti serve quel numero in cinque punti diversi del tuo codice?
Una **variabile** risolve questo problema.
Una variabile è una posizione etichettata nella memoria del tuo programma.
Le dai un nome, ci metti dentro un valore, e Python ricorda quel valore per te.

!!! mascot-welcome "Benvenuto/a al Capitolo 3!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le variabili sono una delle idee più potenti di tutta la programmazione — e le hai già usate in Scratch! Oggi impariamo come Python fa la stessa cosa con poche battute di tastiera. Programmiamo insieme!

## Cos'è una Variabile?

Immagina un post-it sulla tua scrivania.
Sul davanti c'è scritto un nome — come **punteggio** — e sul retro scrivi il valore attuale, come **10**.
Ogni volta che hai bisogno di sapere il punteggio, lo giri e lo leggi.
Se il punteggio cambia, cancelli il vecchio numero e ne scrivi uno nuovo — ma il nome sul davanti resta lo stesso.

In Python, una variabile funziona esattamente come quel post-it.
Crei una variabile scrivendo il suo nome, poi un segno di uguale, poi il valore che vuoi memorizzare.
Questo si chiama **assegnazione di variabile**:

```python
score = 10
```

- Il nome a sinistra (`score`) è l'etichetta della variabile.
- Il segno di uguale (`=`) significa "memorizza questo valore con questo nome."
- Il valore a destra (`10`) è ciò che viene memorizzato.

Nota che `=` in Python **non** significa "è uguale a" come in matematica.
È un'istruzione a senso unico: "prendi il valore a destra e mettilo nella scatola a sinistra."
Il valore fluisce sempre da destra verso sinistra.

Dopo aver memorizzato un valore, puoi rileggerlo usando `print()`:

```python
score = 10
print(score)
```

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, cliccavi sul blocco **"Set score to 10"** per creare una variabile e darle un valore iniziale. In Python, `score = 10` fa esattamente la stessa cosa — stessa idea, solo scritta come testo invece che incastrata come blocchi!

## Codice di Esempio

Ecco un breve programma che crea due variabili e le stampa entrambe.
Leggilo prima di eseguirlo.

```python
score = 10
lives = 3
print(score)
print(lives)
```

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di cliccare su Run, guarda queste quattro righe. Il programma memorizza due numeri e poi li stampa. Cosa pensi mostrerà l'output — appariranno entrambi i numeri, o solo uno? E in che ordine? Fai la tua previsione, poi clicca su Run per scoprirlo!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato proprio su questa pagina.
Non serve alcun account — tutto viene eseguito nel tuo browser.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `score = 10
lives = 3
print(score)
print(lives)`);
</script>

Avevi indovinato?
Python ha stampato `10` sulla prima riga e `3` sulla seconda — un valore per ogni chiamata a `print()`, nell'ordine in cui sono apparse.

**Se vedi un messaggio di errore rosso:** controlla attentamente l'ortografia.
Python distingue tra maiuscole e minuscole, quindi `Score = 10` e `score = 10` sono due variabili completamente diverse.
Assicurati che non ci siano spazi extra attorno al segno `=`.

## Come Funziona

Quando Python esegue `score = 10`, riserva un piccolo spazio di memoria, ci scrive dentro `10` e attacca l'etichetta `score`.
Quando Python incontra poi `print(score)`, cerca quell'etichetta, recupera il valore memorizzato e lo mostra.

La tabella qui sotto spiega ogni riga del programma:

| Riga | Cosa fa |
|------|-------------|
| `score = 10` | Crea una variabile chiamata `score` e ci memorizza dentro l'intero `10` |
| `lives = 3` | Crea una seconda variabile chiamata `lives` e ci memorizza dentro `3` |
| `print(score)` | Cerca il valore in `score` e lo stampa |
| `print(lives)` | Cerca il valore in `lives` e lo stampa |

Ogni variabile è indipendente.
Cambiarne una non influisce sull'altra.
Puoi avere tutte le variabili che vuoi — la memoria del tuo programma può contenerne migliaia.

## Dare un Nome alle Variabili

Python ti permette di chiamare una variabile quasi in qualsiasi modo — ma ci sono regole da seguire:

- **Inizia con una lettera o un underscore** — non con una cifra. `score` va bene; `1score` causa un errore.
- **Usa solo lettere, cifre e underscore** — niente spazi, trattini o simboli come `@` o `!`.
- **Evita le parole chiave di Python** — parole come `print`, `for`, `if` e `while` sono riservate. Python ha bisogno di quelle parole per sé.

Python distingue anche tra **maiuscole e minuscole**: `Score`, `SCORE` e `score` sono tre variabili completamente separate.
Mescolare accidentalmente maiuscole e minuscole è una delle fonti di bug più comuni per i principianti.

### Snake_case: Lo Stile di Denominazione di Python

Quando il nome di una variabile ha più di una parola, i programmatori Python uniscono le parole con underscore e mantengono tutte le lettere minuscole.
Questo stile si chiama **snake_case** (immagina gli underscore come un serpente disteso tra le parole).

La tabella qui sotto mostra errori comuni nei nomi e le loro correzioni in snake_case:

| Nome problematico | Cosa c'è di sbagliato | Nome migliore |
|-----------------|-------------|-------------|
| `myscore` | Le parole sono attaccate — difficile da leggere | `my_score` |
| `MyScore` | Le lettere maiuscole appartengono a un altro stile di denominazione | `my_score` |
| `my score` | Gli spazi non sono ammessi nei nomi di variabile | `my_score` |
| `my-score` | Python legge il trattino come **sottrazione** — `my - score` — non come un nome! | `my_score` |
| `x` | Troppo vago — cosa significa `x`? | `player_score` |
| `s` | Le lettere singole non danno alcuna informazione | `lives_remaining` |

### Nomi di Variabile Significativi

I nomi di variabile migliori descrivono esattamente cosa contiene la variabile.
Un nome come `player_score` ti dice immediatamente cosa rappresenta il numero.
Un nome come `x` non ti dà alcuna informazione.

Questo è importante perché i programmi crescono.
Un programma che scrivi oggi potrebbe essere di 10 righe — facile da tenere a mente.
Ma i programmi crescono fino a centinaia e migliaia di righe.
Quando succede, un buon nome fa la differenza tra codice che puoi leggere e codice che sembra un rompicapo.

!!! mascot-warning "Trappole nei Nomi!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Attento/a al trattino! Se scrivi `my-score` invece di `my_score`, Python legge il trattino come segno meno e pensa che tu stia sottraendo una variabile chiamata `score` da una variabile chiamata `my`. Usa un **underscore** (`_`), mai un trattino (`-`), per unire le parole in un nome. Altre trappole comuni: nomi di una sola lettera come `x` che non dicono nulla, lettere maiuscole che rompono lo snake_case, e l'uso accidentale di una parola chiave Python come nome di variabile.

## Interi: Numeri Interi

Ora che sai come creare e nominare variabili, vediamo più da vicino i tipi di numeri che Python capisce.

Un numero intero — senza virgola decimale — si chiama **intero**, o `int` in breve.
Gli interi possono essere positivi, negativi o zero.
Usi gli interi per le cose che conti: il numero di vite in un gioco, il numero di lati di una forma, il punteggio di un giocatore.

```python
sides = 6
lives = 3
temperature = -5
```

Tutte e tre quelle variabili contengono interi.

## Float: Numeri Decimali

Un numero con una virgola decimale si chiama **float** — abbreviazione di "numero a virgola mobile" ("floating-point number").
I float si usano per misurazioni e valori che non cadono esattamente su un numero intero.

```python
price = 4.99
height = 1.75
pi = 3.14159
```

Il nome "float" deriva dal modo in cui i computer memorizzano questi numeri internamente — la virgola decimale può "galleggiare" (float) in posizioni diverse.
Non hai bisogno di conoscere i dettagli interni.
Ciò che conta è quando usare ciascun tipo:

| Tipo | Tipo Python | Quando usarlo | Esempi |
|------|-------------|-------------|---------|
| Numero intero | `int` | Conteggi, punteggi di gioco, numero di ripetizioni | `0`, `7`, `-12`, `1000` |
| Numero decimale | `float` | Misurazioni, denaro, percentuali, medie | `3.14`, `0.5`, `-2.7`, `99.0` |

Un dettaglio importante: dividere due interi con `/` restituisce sempre un float, anche quando il risultato è un numero intero.

```python
result = 10 / 2
print(result)
```

Questo stampa `5.0`, non `5` — nota la virgola decimale.
Python usa `//` (divisione intera) se vuoi un risultato intero: `10 // 2` restituisce `5`.

## Riassegnazione di Variabile

Una delle cose più potenti delle variabili è che puoi cambiarle.
**Riassegni** una variabile scrivendo di nuovo il suo nome a sinistra di `=` con un nuovo valore a destra.
Python scarta il vecchio valore e memorizza quello nuovo sotto la stessa etichetta.

Ecco un programma che cambia un punteggio a metà esecuzione:

```python
score = 10
print(score)

score = 25
print(score)
```

Leggilo prima di eseguirlo.
Il primo `print` mostra il valore originale.
La seconda assegnazione lo sostituisce.
Il secondo `print` mostra il valore aggiornato.

## Codice di Esempio — Riassegnazione

```python
score = 10
print(score)

score = 25
print(score)
```

## Provalo Ora — Riassegnazione

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `score = 10
print(score)

score = 25
print(score)`);
</script>

Python ha stampato prima `10` e poi `25`.
Il nome `score` è rimasto lo stesso; è cambiato solo il valore.

Puoi anche usare il valore attuale di una variabile per calcolarne uno nuovo:

```python
score = 10
score = score + 5
print(score)
```

Python valuta prima il lato destro: `score + 5` è `10 + 5`, che è uguale a `15`.
Poi memorizza `15` di nuovo in `score`.
Questo pattern — "prendi il vecchio valore, aggiungi qualcosa, memorizza il risultato" — compare costantemente nei programmi veri.

## Osservalo: Scatole in Memoria

Il MicroSim qui sotto ti permette di *osservare* le scatole-post-it mentre uno script viene eseguito. Prima di cliccare qualsiasi cosa, guarda lo script a sinistra e **prevedi quante scatole esisteranno alla fine — e quale valore conterrà ciascuna**. Poi clicca **Next Step** per verificare, una riga alla volta.

<iframe src="../../sims/variable-memory-model/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Variable Memory Model](../../sims/variable-memory-model/index.md){ .md-button }

Non perderti il programma **Copy Surprise** nel menu a tendina: dopo `b = a`, cambiare `a` cambia anche `b`? Fai la tua previsione, poi procedi passo passo per scoprirlo.

## None: Il Valore "Niente"

Python ha un valore speciale che non è né un intero né un float.
Si chiama **None**, e il suo tipo si chiama `NoneType`.

None significa "nessun valore ancora" o "niente qui."
Lo vedrai in due situazioni comuni:

1. Quando vuoi che una variabile esista ma non hai ancora deciso il suo valore.
2. Quando una funzione termina senza restituire nulla — Python restituisce automaticamente `None` in quel caso.

```python
winner = None
print(winner)
print(type(winner))
```

Eseguendo quel programma si stampa:
```
None
<class 'NoneType'>
```

None non è zero.
None non è una stringa vuota.
None è una cosa speciale a sé, che significa "l'assenza di un valore."
Pensalo come un post-it che esiste sulla tua scrivania ma non ha ancora nulla scritto sul retro.

Più avanti nel corso userai None per segnare l'inizio di una ricerca, rappresentare una casella vuota in un tabellone di gioco, o segnalare che una funzione non ha trovato ciò che cercava.

## Cosa Ti Dice `type()`

Python ha una funzione integrata chiamata `type()` che ti dice che tipo di valore è memorizzato in una variabile.
L'hai vista usata con `None` sopra.
Eccola con un intero e un float:

```python
score = 10
price = 4.99

print(type(score))
print(type(price))
```

Output:
```
<class 'int'>
<class 'float'>
```

La parola `class` nell'output è il modo in cui Python descrive le categorie di valori.
Per ora, leggi semplicemente `<class 'int'>` come "questo è un intero" e `<class 'float'>` come "questo è un float."
Imparerai molto di più sulle classi più avanti nel corso.

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto crea due variabili — `player_score` e `bonus_points`. Stampa `player_score` senza problemi, ma manca qualcosa: `bonus_points` non viene mai stampata. Aggiungi **una riga** in modo che l'output mostri entrambi i numeri, uno per riga.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `player_score = 42
bonus_points = 10
print(player_score)
# Add one line below to also print bonus_points`);
</script>

Se il tuo output mostra `42` sulla prima riga e `10` sulla seconda, ce l'hai fatta!
La riga mancante era `print(bonus_points)`.

## Esperimenti

Prova questi cambiamenti nei laboratori qui sopra.
Per ciascuno, prevedi prima cosa succederà — poi esegui il codice per verificare!

1. Nel Laboratorio 1, cambia `score = 10` in `score = 750`. **Saprai che ha funzionato quando** l'output mostra `750` invece di `10`.
2. Nel Laboratorio 1, aggiungi una terza variabile chiamata `high_score` impostata a `100`. Aggiungi una riga `print(high_score)`. **Saprai che ha funzionato quando** vedi tre numeri nell'output.
3. Nel Laboratorio 2 (quello della riassegnazione), cambia `score = 25` in `score = score * 2`. **Saprai che ha funzionato quando** l'output mostra `10` sulla prima riga e `20` sulla seconda.
4. Crea una variabile float chiamata `average_score` e impostala a `87.5`. Stampala. **Saprai che ha funzionato quando** l'output mostra `87.5`.
5. Crea una variabile chiamata `champion` e impostala a `None`. Stampala. Poi riassegna `champion` a `1`. Stampala di nuovo. **Saprai che ha funzionato quando** l'output mostra `None` su una riga e `1` sulla successiva.

!!! mascot-celebration "Hai Imparato le Variabili!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Variabili, interi, float, denominazione snake_case, riassegnazione, None — ora hai i mattoni fondamentali su cui è costruito ogni programma Python. Ogni capitolo da qui in poi userà quello che hai appena imparato. Lavoro splendido, programmatore! Programmiamo insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
