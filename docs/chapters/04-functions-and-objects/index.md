---
title: Funzioni e Oggetti
description: Scopri come definire e chiamare funzioni usando def, aggiungere parametri posizionali, restituire valori, documentare il codice con le docstring e avere un primo sguardo sulla Standard Library e sugli oggetti Python.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 09:19:38
version: 0.09
---

# Funzioni e Oggetti

Alla fine di questa lezione sarai in grado di:

- Definire una funzione in Python usando `def` e chiamarla per nome
- Aggiungere **parametri** in modo che una funzione possa lavorare con valori diversi ogni volta che la chiami
- Usare un'istruzione `return` per restituire un risultato da una funzione

Immagina di avere un compito da fare più e più volte — ad esempio salutare ogni persona di una lista, calcolare l'area di molti rettangoli diversi, o disegnare la stessa forma in dieci colori diversi.
Potresti scrivere ogni passaggio ogni singola volta.
Oppure potresti dare un nome a quei passaggi, scriverli una sola volta, e usare quel nome ogni volta che ti serve svolgere il compito.
Questo è esattamente ciò che fa una **funzione** in Python.

!!! mascot-welcome "Benvenuto/a al Capitolo 4!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le funzioni sono una delle idee più grandi di tutta la programmazione — ti evitano di scrivere lo stesso codice due volte, mantengono i tuoi programmi ordinati, e ti permettono di costruire cose più grandi a partire da pezzi più piccoli. Hai già usato funzioni in ogni singola lezione — `print()` è una funzione! Oggi impari a costruire le tue. Programmiamo insieme!

## Cos'è una Funzione?

Stai chiamando funzioni fin dal Capitolo 1.
Ogni volta che scrivi `print("Hello")` stai chiamando una funzione chiamata `print`.
Qualcuno ha scritto i passaggi che fanno funzionare `print` — tu la chiami semplicemente per nome e le passi un valore.

Una **funzione** è un gruppo di passaggi con un nome, che puoi eseguire in qualsiasi momento scrivendo il suo nome.

In questo capitolo impari a creare le tue funzioni — non solo a usare quelle che Python fornisce.
La parola chiave che inizia una definizione di funzione è `def`, abbreviazione di "define" (definisci).

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, usavi **"Make a Block"** per creare un blocco personalizzato — un gruppo di blocchi che potevi incastrare ovunque ti servisse quell'azione. Il `def` di Python fa esattamente la stessa cosa. Scrivi i passaggi una volta sola sotto un nome, poi chiami quel nome ovunque ti serva. Stessa idea, solo scritta come testo invece che incastrata come blocchi!

## Definire una Funzione con `def`

Per creare la tua funzione, scrivi:

1. La parola chiave `def`
2. Il nome della funzione (usa lo snake_case, proprio come i nomi di variabile del Capitolo 3)
3. Una coppia di parentesi `()`
4. Due punti `:`
5. Righe indentate che contengono i passaggi da eseguire

Ecco la funzione più semplice possibile:

```python
def greet():
    print("Ciao, programmatore!")
    print("Programmiamolo insieme!")
```

I due punti alla fine della riga `def` sono obbligatori — proprio come i due punti che vedrai più avanti con i cicli e i condizionali.
Tutto ciò che è indentato sotto la riga `def` appartiene al corpo della funzione.
Quando Python legge questo, **ricorda** la funzione ma non esegue ancora i passaggi.
Pensalo come scrivere una ricetta su un cartoncino: scrivere il cartoncino non è la stessa cosa che cucinare davvero il pasto.

## Chiamare una Funzione

Definire una funzione e chiamare una funzione sono due azioni separate.

- **Definire** scrive la ricetta sotto un nome.
- **Chiamare** dice "esegui la ricetta adesso."

Chiami una funzione scrivendo il suo nome seguito da parentesi:

```python
greet()
```

Quella singola riga attiva tutti i passaggi dentro `greet`.
Puoi chiamare la stessa funzione tutte le volte che vuoi — Python esegue l'intero corpo ogni volta.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto definisce `greet()` e poi la chiama tre volte. Quante righe di testo pensi appariranno nell'output? Fai la tua previsione — poi clicca su Run per scoprirlo!

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
initCmLab('', `def greet():
    print("Ciao, programmatore!")
    print("Programmiamolo insieme!")

greet()
greet()
greet()`);
</script>

Avevi indovinato?
Chiamare `greet()` tre volte ha stampato sei righe — due per ogni chiamata.
Questo è il potere delle funzioni: scrivi i passaggi una volta, eseguili tutte le volte che ti servono.

**Se vedi un messaggio di errore rosso:** le due cause più comuni sono i due punti mancanti dopo `def greet()` oppure un'indentazione sbagliata dentro il corpo della funzione.
Python richiede che ogni riga dentro il corpo della funzione sia indentata esattamente di quattro spazi.
Se le righe `print` iniziano al margine sinistro invece di essere indentate, Python ti darà un `IndentationError`.

## Come Funziona

Python legge il tuo programma dall'alto verso il basso, ma non esegue la funzione nel momento in cui incontra `def`.
Legge e ricorda la funzione, poi continua.
Quando finalmente arriva a `greet()`, quello è il segnale — solo allora entra nel corpo della funzione ed esegue entrambe le righe `print`.
Dopo che il corpo della funzione termina, Python torna al punto in cui si era fermato ed esegue la riga successiva.

La tabella qui sotto ripercorre ogni riga del programma:

| Riga | Cosa fa |
|------|-------------|
| `def greet():` | Definisce una nuova funzione chiamata `greet` — Python la ricorda ma non la esegue ancora |
| `    print("Ciao, programmatore!")` | Passaggio 1 dentro il corpo della funzione — indentato di 4 spazi |
| `    print("Programmiamolo insieme!")` | Passaggio 2 dentro il corpo della funzione — indentato di 4 spazi |
| `greet()` | Chiama la funzione — Python entra, esegue entrambi i passaggi, poi torna indietro |

## Parametri Posizionali

Una funzione che fa sempre esattamente la stessa cosa è utile, ma limitata.
Per rendere una funzione flessibile — capace di lavorare con valori diversi ogni volta — le dai dei **parametri**.

Un **parametro** è una variabile che vive dentro la funzione e riceve un valore quando la chiami.
Pensalo come una frase da completare: "Ciao, ______!" è il modello, e lo spazio vuoto viene riempito con un nome diverso ogni volta.

Dichiari i parametri dentro le parentesi di `def`:

```python
def greet(name):
    print("Ciao, " + name + "!")
```

La parola `name` tra le parentesi è il parametro.
Dentro il corpo della funzione, `name` funziona esattamente come qualsiasi variabile del Capitolo 3.

Quando chiami questa funzione, fornisci un valore:

```python
greet("Monty")
greet("Python")
```

I valori `"Monty"` e `"Python"` si chiamano **argomenti** — i valori reali che passi al momento della chiamata.
Python copia il primo argomento nel primo parametro prima di eseguire il corpo della funzione.
Poiché gli argomenti corrispondono per posizione (il primo argomento va al primo parametro), si chiamano **parametri posizionali**.

Prima di cliccare su Run nel laboratorio qui sotto, prevedi cosa vedrai.
Quali nomi appariranno, e in che ordine?

## Provalo Ora — Parametri

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
initCmLab('-2', `def greet(name):
    print("Ciao, " + name + "!")

greet("Monty")
greet("Python")
greet("World")`);
</script>

Ogni chiamata a `greet` ha usato lo stesso modello — `"Ciao, " + name + "!"` — ma con un nome diverso inserito.
Una funzione, tre output diversi.
Prova a cambiare i nomi nelle tre righe di chiamata per salutare i tuoi amici o la tua famiglia!

## L'Istruzione `return`

Finora, ogni funzione ha svolto il suo lavoro chiamando direttamente `print()`.
Ma a volte vuoi che una funzione **calcoli un risultato e lo restituisca**, così il resto del tuo programma può usare quel risultato.

La parola chiave `return` restituisce un valore a chi ha chiamato la funzione.

Ecco una funzione che somma due numeri e restituisce il totale:

```python
def add(a, b):
    result = a + b
    return result
```

Nota che questa funzione **non** chiama `print`.
Invece restituisce il risultato.
Catturi quel valore restituito memorizzandolo in una variabile:

```python
total = add(5, 3)
print(total)
```

Quando Python esegue `add(5, 3)`, copia `5` in `a` e `3` in `b`, calcola `result = 8`, e poi `return result` restituisce `8`.
Quell'`8` diventa il valore di `total`, che viene poi stampato.

La tabella qui sotto mostra cosa fa ogni parte:

| Codice | Cosa fa |
|------|-------------|
| `def add(a, b):` | Definisce una funzione con due parametri |
| `    result = a + b` | Somma i due parametri; memorizza in una variabile locale |
| `    return result` | Restituisce la somma a chi ha chiamato `add` |
| `total = add(5, 3)` | Chiama la funzione; il valore restituito `8` viene memorizzato in `total` |
| `print(total)` | Stampa `8` |

## Osservalo: Segui una Chiamata Attraverso una Funzione

Il MicroSim qui sotto ripercorre una chiamata di funzione al rallentatore: l'argomento vola nello slot del parametro, il corpo calcola, e il valore di ritorno vola indietro verso il punto di chiamata. Prima di cliccare qualsiasi cosa, leggi il programma a sinistra e **prevedi i due numeri che stamperà**. Poi procedi passo passo e osserva da dove arrivano i tuoi numeri.

<iframe src="../../sims/function-call-flow/main.html" height="502" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Function Call Flow](../../sims/function-call-flow/index.md){ .md-button }

Nota che la macchina della funzione viene costruita una sola volta al passaggio `def`, poi usata **due volte** — la stessa ricetta con due ingredienti diversi.

## Funzioni che Restituiscono None

Cosa succede se una funzione non usa mai `return`?

Python deve comunque restituire qualcosa a chi l'ha chiamata.
In quel caso, restituisce automaticamente un valore speciale che conosci dal Capitolo 3: **None**.

Puoi vederlo accadere:

```python
def greet():
    print("Ciao, programmatore!")

result = greet()
print(result)
```

L'output sarà:
```
Ciao, programmatore!
None
```

`greet()` ha stampato una riga, poi Python ha restituito `None` automaticamente.
Quando l'hai memorizzato in `result` e l'hai stampato, hai visto `None`.

Questo è il concetto chiamato **funzioni che restituiscono None**: qualsiasi funzione che termina senza un'istruzione `return` restituisce `None`.
Non te ne accorgerai sempre perché la maggior parte dei programmi non si preoccupa di memorizzare il valore di ritorno di una funzione che fa solo `print` — ma è bene sapere che succede.

!!! mascot-warning "Non Dimenticare `return`!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Un bug molto comune tra i principianti: scrivi una funzione per calcolare un valore, ma dimentichi di aggiungere `return` alla fine. La funzione esegue il calcolo — ma la risposta sparisce! Il codice chiamante riceve `None` invece del numero che si aspettava. Se vedi `None` in un punto dove ti aspettavi un numero vero, controlla se alla tua funzione manca un'istruzione `return`.

## Docstring

I programmatori Python professionisti documentano sempre le loro funzioni con una **docstring** — una stringa di testo che spiega cosa fa la funzione.

Una docstring si scrive sulla prima riga dentro il corpo della funzione, racchiusa tra triple virgolette (`"""`):

```python
def add(a, b):
    """Somma due numeri e restituisce il risultato."""
    result = a + b
    return result
```

Le triple virgolette possono estendersi su più righe se hai bisogno di una spiegazione più lunga:

```python
def greet(name):
    """
    Print a friendly greeting to the given name.
    
    Parameters:
        name (str): The person's name to greet.
    """
    print("Ciao, " + name + "!")
```

Le docstring hanno due scopi.
Primo, aiutano la prossima persona che legge il tuo codice — incluso il te stesso del futuro — a capire cosa fa la funzione senza leggere ogni riga.
Secondo, gli strumenti Python possono leggere le docstring automaticamente e mostrarle come testo di aiuto.
Se digiti `help(add)` in un ambiente Python, Python mostra la docstring che hai scritto.

Scrivere docstring è un'abitudine che vale la pena costruire fin dall'inizio.
In questo corso, ogni funzione che scrivi da ora in poi dovrebbe avere almeno una docstring di una riga.

## La Standard Library: La Cassetta degli Attrezzi Integrata di Python

Hai già usato un pezzo della cassetta degli attrezzi integrata di Python: la funzione `print()`.
Python viene fornito con centinaia di altre funzioni già scritte, organizzate in **moduli** — file pieni di funzioni correlate che puoi caricare nel tuo programma con la parola chiave `import`.

Insieme, tutti questi moduli formano la **Standard Library** — una collezione di strumenti che arriva con ogni installazione di Python, completamente gratis.

Ecco quattro moduli che userai in tutto questo corso:

| Modulo | Cosa contiene | Esempio |
|--------|-----------------|---------|
| `math` | Funzioni e costanti matematiche | `math.sqrt(25)` → `5.0` |
| `random` | Funzioni per generare numeri casuali | `random.randint(1, 6)` → lancia un dado |
| `time` | Funzioni per lavorare con il tempo e le pause | `time.sleep(1)` → mette in pausa per 1 secondo |
| `turtle` | Funzioni e oggetti per disegnare sullo schermo | `turtle.forward(100)` → disegna una linea |

Importi un modulo scrivendo `import` seguito dal nome del modulo in cima al tuo programma.
Dopodiché, accedi alle sue funzioni usando la notazione a punto — il nome del modulo, un punto, poi il nome della funzione:

```python
import math
print(math.sqrt(16))
```

Questo stampa `4.0`.
Il punto collega il modulo (`math`) alla funzione al suo interno (`sqrt`).
Userai questo schema costantemente per il resto del corso.

Incontrerai il modulo `turtle` nel Capitolo 5, `random` nel Capitolo 17, `math` nel Capitolo 18, e molti altri man mano che il corso procede.
Per ora, sappi semplicemente che la Standard Library esiste e che `import` è il modo per sbloccarla.

## Oggetti e Classi: Un Primo Sguardo

Sei quasi pronto/a per incontrare il modulo `turtle`.
Prima di farlo, c'è un'altra idea da anticipare — non spiegarla del tutto, solo introdurla — perché la vedrai nel momento in cui inizierai a disegnare.

Python organizza molte cose come **oggetti**.
Un **oggetto** è un pacchetto che raggruppa due tipi di cose:

- **Dati** (chiamati attributi) — informazioni che l'oggetto conosce su se stesso
- **Azioni** (chiamate metodi) — cose che l'oggetto può fare

L'esempio classico è una turtle sullo schermo.
Un oggetto turtle conosce la sua posizione attuale, la sua direzione, il colore della sua penna, e se la sua penna è alzata o abbassata (questi sono i suoi attributi).
Un oggetto turtle può muoversi in avanti, girare, cambiare colore, e alzare o abbassare la penna (questi sono i suoi metodi).

Quando scriverai codice come questo nel Capitolo 5:

```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)
```

`turtle.Turtle()` crea un nuovo oggetto turtle e lo memorizza nella variabile `t`.
`t.forward(100)` chiama il metodo `forward` su quell'oggetto — la stessa notazione a punto che hai appena visto con i moduli.

Una **classe** è il progetto che descrive quali attributi e metodi ha un oggetto.
`turtle.Turtle` è una classe; `t` è un singolo oggetto (chiamato **istanza**) creato a partire da quel progetto.

Non devi memorizzare tutto questo adesso.
Il punto importante da portare a casa è che gli oggetti vengono forniti con azioni integrate — e chiami quelle azioni scrivendo il nome dell'oggetto, un punto, e il nome del metodo.
Costruirai il modello mentale passo dopo passo a partire dal Capitolo 5, e scriverai le tue classi nel Capitolo 25.

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione qui sotto dovrebbe moltiplicare due numeri e restituire il risultato — ma le manca una riga fondamentale. Al momento, se esegui il codice, `product` riceve `None` invece di `15`. Aggiungi **una riga** dentro la funzione in modo che `print(product)` mostri `15`!

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
initCmLab('-3', `def multiply(a, b):
    """Moltiplica due numeri e restituisce il risultato."""
    result = a * b
    # Aggiungi una riga qui sotto per restituire il risultato

product = multiply(3, 5)
print(product)`);
</script>

Se il tuo output mostra `15`, ce l'hai fatta!
La riga mancante era `return result`.
Senza di essa, Python restituiva silenziosamente `None` — e `None` non è il numero che volevi.

## Esperimenti

Prova questi cambiamenti nei laboratori qui sopra.
Per ciascuno, prevedi prima cosa succederà — poi esegui il codice per verificare!

1. Nel Laboratorio 1, cambia `greet()` in modo che stampi solo una riga: `"Python is awesome!"`. Chiamala cinque volte. **Saprai che ha funzionato quando** l'output mostra cinque righe identiche.
2. Nel Laboratorio 2, aggiungi una quarta chiamata: `greet("your name here")` ma sostituisci `your name here` con il tuo vero nome. **Saprai che ha funzionato quando** l'output ti saluta personalmente nella quarta riga.
3. Nel Laboratorio 2, aggiungi un secondo parametro chiamato `language` alla funzione in modo che stampi `"Ciao, Monty! Stai imparando Python."` Suggerimento: dovrai aggiornare la riga `def` e la riga `print` dentro la funzione. **Saprai che ha funzionato quando** l'output include il nome della lingua.
4. Nel laboratorio della Verifica di Apprendimento, cambia la chiamata in `multiply(7, 6)`. **Saprai che ha funzionato quando** l'output mostra `42`.
5. Scrivi una funzione completamente nuova chiamata `square(n)` che restituisce `n * n`. Chiamala con alcuni numeri diversi e stampa ogni risultato. **Saprai che ha funzionato quando** `square(4)` stampa `16` e `square(10)` stampa `100`.

!!! mascot-celebration "Funzioni Sbloccate!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena imparato una delle competenze più importanti di tutta la programmazione! `def`, parametri, `return`, `None`, docstring, la Standard Library, e un primo sguardo sugli oggetti — un intero capitolo pieno di grandi idee. Nel Capitolo 5 metterai subito al lavoro le funzioni, usando il modulo `turtle` per disegnare sullo schermo. Ci vediamo lì! Programmiamo insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
