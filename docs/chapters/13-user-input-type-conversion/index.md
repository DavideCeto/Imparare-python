---
title: Input dell'Utente e Conversione di Tipo
description: Impara come ottenere l'input dell'utente con input(), convertire tra tipi di dati, validare l'input, e usare print() efficacemente
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:10:00
version: 0.09
---

# Input dell'Utente e Conversione di Tipo

Alla fine di questa lezione sarai in grado di:

- Usare `input()` per fare una domanda all'utente e leggere la sua risposta
- Convertire tra tipi di dati usando `int()`, `float()`, `str()`, e `bool()`
- Controllare il tipo di un valore con la funzione `type()`
- Validare l'input dell'utente così che il tuo programma non si blocchi con dati sbagliati

Finora i tuoi programmi hanno girato sempre nello stesso modo.
Con `input()`, il tuo programma può avere una conversazione con l'utente — facendo domande e rispondendo alle sue risposte.

!!! mascot-welcome "Benvenuto/a al Capitolo 13!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Oggi i tuoi programmi prendono vita! Invece di girare sempre nello stesso modo,
    faranno domande all'utente e risponderanno alle risposte.
    Preparati a costruire i tuoi primi programmi davvero interattivi! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## La Funzione `input()`

`input()` ferma il programma, stampa un messaggio (chiamato **prompt**), e aspetta che l'utente scriva qualcosa e prema Invio.
Qualsiasi cosa l'utente scriva torna al tuo programma come una **stringa**.

La parola chiave da ricordare: `input()` **restituisce sempre una stringa**, anche se l'utente scrive un numero.

```python
name = input("Come ti chiami? ")
print("Ciao,", name)
```

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
initCmLab('', `name = input("Come ti chiami? ")
print("Ciao,", name + "! Benvenuto in Python!")`);
</script>

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, il blocco **"Chiedi ___ e aspetta"** pausa il programma e memorizza la risposta in una variabile speciale chiamata `answer`.
    In Python, `input("your question")` fa esattamente la stessa cosa — pausa e restituisce la risposta come una stringa.

## Conversione di Tipo

Dato che `input()` restituisce sempre una stringa, devi **convertirla** prima di fare calcoli matematici.

Prima di immergerci, definiamo tre termini:
- **Intero (int):** un numero intero senza punto decimale — `5`, `-12`, `0`
- **Float:** un numero con un punto decimale — `3.14`, `-0.5`, `100.0`
- **Conversione di tipo:** cambiare un valore da un tipo di dato a un altro

### `int()` — Converti in Intero

`int()` converte una stringa (o un float) in un numero intero.
Se la stringa contiene lettere, `int()` genera un `ValueError` — quindi convertila sempre solo dopo aver controllato che l'input sembri un numero.

```python
age_text = input("Quanti anni hai? ")
age = int(age_text)          # converte la stringa in intero
print("L'anno prossimo avrai", age + 1)
```

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
initCmLab('-2', `age_text = input("Quanti anni hai? ")
age = int(age_text)
print("L'anno prossimo avrai", age + 1)`);
</script>

### `float()` — Converti in Numero Decimale

`float()` converte una stringa in un numero con un punto decimale.
Usalo quando hai bisogno di precisione oltre i numeri interi — per prezzi, misure, o temperature.

```python
price = float(input("Inserisci il prezzo: €"))
tax = price * 0.08
print("Totale con le tasse: €" + str(round(price + tax, 2)))
```

### `str()` — Converti in Stringa

`str()` converte un numero (o un altro valore) in una stringa.
Ne hai bisogno quando vuoi unire un numero con del testo usando `+`.

```python
score = 95
print("Il tuo punteggio: " + str(score) + "/100")   # prima bisogna convertirlo in stringa
```

### `bool()` — Converti in True o False

`bool()` converte un valore in `True` o `False`.
Le regole su cosa diventa `False` vanno memorizzate:

| Valore | Risultato di `bool()` |
|-------|----------------|
| `0` | `False` |
| `""` (stringa vuota) | `False` |
| `None` | `False` |
| Qualsiasi altra cosa | `True` |

```python
print(bool(0))       # False
print(bool(""))      # False
print(bool("hi"))    # True
print(bool(42))      # True
```

## La Funzione `type()`

`type()` ti dice qual è il tipo di dato di un valore.
È incredibilmente utile per il debug — quando non sei sicuro se stai lavorando con una stringa o un numero, basta chiederlo a Python.

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
initCmLab('-3', `x = input("Scrivi qualcosa: ")
print("Hai inserito:", x)
print("Tipo di x:", type(x))

y = int(x)
print("Dopo int():", y)
print("Tipo di y:", type(y))`);
</script>

Se scrivi un numero come `42`, vedrai prima `<class 'str'>`, poi `<class 'int'>` dopo la conversione.

## Metodi delle Stringhe: `lower()`, `upper()`, `strip()`

Prima di convertire o validare l'input, è una buona idea **pulirlo** prima.

- `s.lower()` — converte tutte le lettere in minuscolo (`"Hello"` → `"hello"`)
- `s.upper()` — converte tutte le lettere in maiuscolo (`"hello"` → `"HELLO"`)
- `s.strip()` — rimuove gli spazi iniziali e finali (`"  hi  "` → `"hi"`)

Questi tre metodi sono molto utili per gestire l'input:

```python
answer = input("Vuoi continuare? (yes/no) ")
answer = answer.strip().lower()   # prima ripulisci l'input
if answer == "yes":
    print("Ottimo, andiamo avanti!")
else:
    print("OK, mi fermo qui.")
```

## Le Basi della Validazione dell'Input

**Validazione** significa controllare che l'input dell'utente sia sicuro da usare prima di usarlo.

Un approccio semplice è usare `str.isdigit()` — un metodo di stringa che restituisce `True` se tutti i caratteri sono cifre.

Prima di chiamare `int()`, puoi usare `isdigit()` per evitare un crash:

```python
raw = input("Inserisci un numero intero: ")
raw = raw.strip()

if raw.isdigit():
    n = int(raw)
    print("Il doppio è:", n * 2)
else:
    print("Questo non sembra un numero!")
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `raw = input("Inserisci un numero intero: ")
raw = raw.strip()

if raw.isdigit():
    n = int(raw)
    print("Il doppio è:", n * 2)
else:
    print("Questo non sembra un numero intero!")`);
</script>

Provalo due volte: una volta con un numero come `7`, e una volta con lettere come `hello`.

## Suggerimenti su `print()`

`print()` è più potente di quanto sembri. Alcuni trucchi utili:

| Caratteristica | Esempio | Output |
|---------|---------|--------|
| Valori multipli | `print("a", "b", "c")` | `a b c` |
| Separatore personalizzato | `print("a", "b", sep="-")` | `a-b` |
| Nessun ritorno a capo alla fine | `print("Hello", end=" ")` | resta sulla stessa riga |
| Riga vuota | `print()` | riga vuota |

## Verifica di Apprendimento

!!! mascot-thinking "Trova il Bug!"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe sommare due numeri inseriti dall'utente.
    Ma ha un bug — concatena le stringhe invece di sommare i numeri!
    Correggilo così che la matematica funzioni davvero.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-5"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-5')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-5')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-5"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-5"></div>
  </div>
</div>
<script>
initCmLab('-5', `a = input("Inserisci il primo numero: ")
b = input("Inserisci il secondo numero: ")

# Bug: questo unisce le stringhe, non somma i numeri!
print("Somma:", a + b)`);
</script>

Se inserisci `3` e `4`, la versione con il bug stampa `34` invece di `7`.
Correggilo convertendo `a` e `b` con `int()` prima di sommarli.

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia il laboratorio del saluto per chiedere il colore preferito dell'utente. Stampa `"My favorite color is [color] too!"`.
   **Saprai che ha funzionato quando** il programma ripete il colore che hai scritto.

2. Chiedi all'utente una temperatura in Celsius. Convertila: `fahrenheit = (celsius * 9/5) + 32`. Stampa il risultato.
   **Saprai che ha funzionato quando** inserendo `100` stampa `212.0`.

3. Chiedi all'utente il suo nome, poi usa `.upper()` per stamparlo in maiuscolo.
   **Saprai che ha funzionato quando** scrivendo `monty` stampa `MONTY`.

4. Nella demo di validazione, prova a scrivere un numero negativo come `-5`. `isdigit()` lo accetta?
   **Saprai che ha funzionato quando** vedi che `-5` fallisce il controllo `isdigit()` — e capisci perché!

5. Usa `type()` per stampare i tipi di `3.14`, `True`, e `None`.
   **Saprai che ha funzionato quando** vedi `float`, `bool`, e `NoneType`.

!!! mascot-celebration "Progresso Straordinario!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    I tuoi programmi possono ora avere vere conversazioni con gli utenti!
    Hai imparato `input()`, la conversione di tipo, la validazione, e la pulizia delle stringhe.
    Queste competenze appaiono in quasi ogni vero programma Python. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
