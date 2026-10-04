---
title: Lavorare con le Stringhe
description: Esplora il tipo stringa di Python — virgolette, concatenazione, ripetizione, caratteri di escape, len(), immutabilità, stringhe raw e turtle.write() per etichette sulla tela.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 10:40:00
version: 0.09
---

# Lavorare con le Stringhe

## Riepilogo

Il testo in Python si chiama *stringa*. Questo capitolo introduce il tipo stringa,
virgolette singole contro doppie, concatenazione (unire stringhe), ripetizione, caratteri
di escape come `\n`, misurare la lunghezza con `len()`, stringhe raw, e
l'immutabilità delle stringhe. Come progetto pratico userai `turtle.write()` per
disegnare etichette e testo direttamente sulla tua tela turtle.

## Concetti Trattati

Questo capitolo tratta i seguenti 9 concetti del grafo di apprendimento:

1. String Type
2. Single vs Double Quotes
3. String Concatenation
4. String Repetition
5. Escape Characters
6. String Length with len()
7. String Immutability
8. Raw Strings
9. Writing Text with turtle.write()

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 5: Disegnare con la Grafica Turtle](../05-drawing-with-turtle/index.md)
- [Capitolo 7: Cicli For e Disegno di Forme](../07-for-loops-and-shapes/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Creare stringhe usando virgolette singole o doppie
- Unire stringhe con `+` (concatenazione) e ripeterle con `*`
- Usare caratteri di escape come `\n` e `\t` per controllare la disposizione del testo
- Disegnare testo etichettato direttamente sulla tela turtle con `turtle.write()`

I numeri non sono gli unici dati con cui lavora Python.
Il **testo** — nomi, frasi, emoji, percorsi di file, URL — è altrettanto importante.
Python chiama il testo **stringa**, e questo capitolo ti dà gli strumenti per creare, combinare e mostrare stringhe nei tuoi programmi.

!!! mascot-welcome "Benvenuto/a al Capitolo 8!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le stringhe aprono un intero nuovo lato di Python! Una volta che sai lavorare con il testo, i tuoi programmi turtle possono disegnare etichette, punteggi e messaggi direttamente sulla tela. Programmiamo insieme!

## Il Tipo Stringa

Una **stringa** è qualsiasi sequenza di caratteri — lettere, cifre, spazi, punteggiatura, emoji — racchiusa tra virgolette.
Python memorizza le stringhe con il nome di tipo `str`.

```python
greeting = "Hello, Coder!"
species  = 'Python snake'
number   = "42"             # still a string, not an integer!
```

Nota che `"42"` (con le virgolette) è una *stringa*, non il numero 42.
Se provassi a sommare `"42" + 1` Python ti darebbe un errore — stringhe e numeri sono tipi diversi.

## Virgolette Singole contro Doppie

Python accetta sia le virgolette singole `'...'` sia quelle doppie `"..."` per le stringhe.
Funzionano in modo identico — scegli quella che preferisci, basta essere coerenti.

Il motivo principale per conoscerle entrambe è **quando la tua stringa contiene un apostrofo o dei segni di virgolette**:

```python
msg1 = "It's a great day!"     # apostrophe inside — use double quotes
msg2 = 'She said "wow!"'       # quote marks inside — use single quotes
```

Se usi accidentalmente lo stesso tipo di virgolette sia dentro che fuori dalla stringa, Python si confonde e ti dà un `SyntaxError`.

## Concatenazione di Stringhe

**Concatenazione** significa unire due o più stringhe una dopo l'altra.
Python usa l'operatore `+` per la concatenazione:

```python
first = "Monty"
last  = "Python"
full  = first + " " + last
print(full)    # Monty Python
```

Puoi concatenare tutte le stringhe che vuoi in un'unica espressione.
Nota che Python **non** aggiunge automaticamente uno spazio — devi includere tu stesso `" "` se ne vuoi uno.

Il programma qui sotto costruisce un messaggio di saluto da due variabili.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda l'ultima chiamata a `print()` prima di cliccare su Run.
    `name` è `"Alex"` e `greeting` è `"Hello, "`.
    Cosa stamperà esattamente il programma su quell'ultima riga?
    Fai la tua previsione — poi scoprilo!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato.

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
initCmLab('', `name = "Alex"
greeting = "Hello, "
farewell = "See you later, "

# Concatenation: joining strings with +
print(greeting + name + "!")
print(farewell + name + "!")

# Repetition: repeat a string with *
print("-" * 20)
print("Ha" * 4)`);
</script>

Avevi indovinato? Il primo `print()` mostra `Hello, Alex!`. Nota come `"-" * 20` crea una linea divisoria di esattamente venti trattini — molto più veloce che digitarli uno per uno!

## Ripetizione di Stringhe

Proprio come `+` unisce stringhe, `*` **ripete** una stringa un numero di volte indicato:

```python
print("Echo! " * 3)    # Echo! Echo! Echo!
print("=" * 30)        # ============================== (30 equals signs)
```

La ripetizione di stringhe è comoda per creare separatori visivi, bordi e pattern.
Il numero a destra deve essere un intero — `"ha" * 2.5` dà un errore.

## Caratteri di Escape

Alcuni caratteri non possono essere digitati direttamente dentro una stringa.
Python fornisce i **caratteri di escape** — speciali sequenze di due caratteri che iniziano con una barra rovesciata `\`:

| Escape | Significato | Output di esempio |
|--------|---------|----------------|
| `\n` | Nuova riga | Passa alla riga successiva |
| `\t` | Tabulazione | Aggiunge uno spazio della dimensione di un tab |
| `\\` | Barra rovesciata letterale | Stampa `\` |
| `\'` | Virgoletta singola letterale | Stampa `'` dentro una stringa con virgolette singole |
| `\"` | Virgoletta doppia letterale | Stampa `"` dentro una stringa con virgolette doppie |

```python
print("Line one\nLine two\nLine three")
print("Name:\tMonty\nAge:\t12")
print("She said \"Wow!\"")
```

Il `\n` (nuova riga) è uno dei caratteri di escape più usati — permette a una singola chiamata `print()` di produrre più righe di output.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, il blocco **Say** mostra un messaggio alla volta in un fumetto. Il `print()` di Python è simile, ma molto più flessibile — puoi stampare più righe, aggiungere tabulazioni, unire variabili e testo, e mostrare numeri tutto in una sola chiamata!

## Lunghezza di una Stringa con len()

La funzione `len()` conta quanti caratteri ci sono in una stringa — inclusi spazi e punteggiatura:

```python
word  = "Python"
print(len(word))          # 6
sentence = "Hello, world!"
print(len(sentence))      # 13
print(len(""))            # 0  (empty string has length zero)
```

`len()` è una delle **funzioni integrate** di Python — non devi importare nulla, funziona e basta.
Userai `len()` costantemente: per controllare se una password è abbastanza lunga, misurare l'input dell'utente, o controllare quanti caratteri mostrare.

## Immutabilità delle Stringhe

Una volta creata una stringa, **non puoi cambiare i singoli caratteri al suo interno**.
Questa proprietà si chiama **immutabilità**:

```python
name = "Monty"
name[0] = "B"    # ← ERROR! You can't change a single character
```

Questo sorprende i principianti che si aspettano che le stringhe funzionino come una lista.
Per "cambiare" una stringa, crei una *nuova* stringa a partire da quella vecchia:

```python
name = "Monty"
name = "B" + name[1:]    # creates a brand-new string "Bonty"
print(name)              # Bonty
```

L'immutabilità non è un difetto — rende le stringhe più veloci e sicure da usare.
Imparerai lo slicing delle stringhe (la parte `[1:]` qui sopra) in un capitolo successivo.

## Stringhe Raw

A volte vuoi che Python ignori completamente i caratteri di escape.
Per esempio, se stai scrivendo un percorso di file Windows come `C:\new_folder\text.txt`, `\n` e `\t` verrebbero interpretati come una nuova riga e una tabulazione!

Una **stringa raw** si crea mettendo `r` prima della virgoletta di apertura.
Dentro una stringa raw, le barre rovesciate sono trattate come caratteri letterali:

```python
# Without r: \n becomes a newline, \t becomes a tab
print("C:\new_folder\text.txt")    # messy output!

# With r: backslashes are literal
print(r"C:\new_folder\text.txt")   # C:\new_folder\text.txt
```

Le stringhe raw si usano più comunemente per percorsi di file e pattern (che imparerai nel Capitolo 29).

!!! mascot-warning "Attenzione!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Una stringa raw non può terminare con un numero **dispari** di barre rovesciate. `r"path\"` dà un `SyntaxError` perché l'ultimo `\"` sembra una virgoletta con escape. Se devi terminare una stringa con una barra rovesciata, usa semplicemente una stringa normale e scrivi `"\\"` (due barre rovesciate = una barra rovesciata letterale).

## Scrivere Testo con turtle.write()

La funzione `turtle.write()` disegna un'etichetta di testo direttamente sulla tela nella posizione attuale della turtle.
Questo permette ai tuoi disegni di includere titoli, didascalie, punteggi, o qualsiasi altro testo.

La forma di base è:

```python
t.write("Hello, turtle world!", font=("Arial", 16, "normal"))
```

L'argomento `font` è una tupla di tre valori: il nome del font, la dimensione in punti, e lo stile (`"normal"`, `"bold"` o `"italic"`).

Il programma qui sotto disegna un poligono e poi lo etichetta.

!!! mascot-thinking "Tocca a Te — Aggiungi l'Etichetta"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna un pentagono ma non lo etichetta ancora.
    Aggiungi **una riga** dopo il ciclo per chiamare `t.write()` e mostrare il testo `"Pentagon"` sulla tela.
    **Suggerimento:** sposta prima `t.penup()` e posiziona la turtle con `t.goto(-40, -120)`, poi chiama `t.write()`.

<div class="cm-lab">
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
initCmLab('-2', `import turtle
t = turtle.Turtle()
t.speed(3)

# Draw a pentagon
sides = 5
turn_angle = 360 / sides
for i in range(sides):
    t.forward(80)
    t.right(turn_angle)

# Move to a label position and write the name
t.penup()
t.goto(-40, -120)
# Add one line here to call t.write() and display "Pentagon"
# Use font=("Arial", 16, "bold") for a nice look`);
</script>

Una volta che l'etichetta appare, prova a cambiare la dimensione del font, lo stile, o il testo stesso!

## Esperimenti

Prova questi cambiamenti ai programmi qui sopra. Per ciascuno, prevedi prima cosa succederà, poi eseguilo per verificare!

1. Nel primo laboratorio, cambia `name = "Alex"` con il tuo nome. **Saprai che ha funzionato quando** il saluto stampa il tuo nome.
2. Cambia `"Ha" * 4` in `"Ha" * 10`. **Saprai che ha funzionato quando** vedi dieci "Ha" in fila.
3. Nel laboratorio turtle, aggiungi una riga `print(len("Pentagon"))`. **Saprai che ha funzionato quando** vedi `8` stampato sotto la tela.
4. Cambia il testo dell'etichetta in `"My " + str(sides) + "-sided shape"`. **Saprai che ha funzionato quando** l'etichetta dice "My 5-sided shape".
5. Prova a cambiare `sides = 5` in `sides = 8` e l'etichetta in `"Octagon"`. **Saprai che ha funzionato quando** vedi una forma a otto lati con l'etichetta corretta.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato il tipo stringa di Python! Puoi unire stringhe con `+`, ripeterle con `*`, aggiungere a capo e tabulazioni con i caratteri di escape, misurarne la lunghezza con `len()`, e persino disegnare etichette di testo direttamente sulla tela turtle. Le stringhe sono ovunque nella programmazione — e ora sai come usarle. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
