---
title: Gestione degli Errori e Debugging
description: Impara a leggere i traceback, catturare le eccezioni con try/except, generare i tuoi errori, usare assert, e fare debug con istruzioni print strategiche
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:50:00
version: 0.09
---

# Gestione degli Errori e Debugging

Alla fine di questa lezione sarai in grado di:

- Identificare i tre tipi di errori Python: **sintattici**, **di runtime**, e **logici**
- Leggere un **traceback** di Python e trovare esattamente dove sta il problema
- Usare `try/except` per catturare gli errori e mantenere il tuo programma in esecuzione
- Usare `raise`, `assert`, e chiamate `print()` strategiche per trovare e segnalare i bug

Ogni programmatore fa errori. L'abilità non è evitare gli errori — è trovarli e correggerli velocemente.

!!! mascot-welcome "Benvenuto/a al Capitolo 23!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli errori non sono fallimenti — sono indizi! I messaggi di errore di Python sono in realtà molto utili una volta che sai come leggerli.
    Oggi trasformeremo del testo rosso spaventoso in informazioni utili.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Tre Tipi di Errori

Un **errore sintattico** viene rilevato prima che il programma venga eseguito. Python non può nemmeno interpretare il codice.
Un `:` mancante dopo `if`, un'indentazione sbagliata, o una parentesi non corrispondente causano un errore sintattico.

Un **errore di runtime** (chiamato anche **eccezione**) succede mentre il programma è in esecuzione.
Il programma parte, poi va in crash quando raggiunge la riga sbagliata.

Un **errore logico** è il più insidioso — il programma gira senza andare in crash, ma produce il risultato sbagliato.
Python non può rilevare gli errori logici; devi trovarli da solo.

| Tipo di errore | Quando viene rilevato | Esempio |
|------------|--------------|---------|
| Errore sintattico | Prima dell'esecuzione | `:` mancante dopo `if` |
| Errore di runtime | Durante l'esecuzione | `int("hello")` |
| Errore logico | Dopo l'esecuzione | Scarto di uno in un ciclo |

## Tipi Comuni di Eccezioni

Quando si verifica un errore di runtime, Python genera un'**eccezione** — un tipo di errore con un nome.

| Eccezione | Causa |
|-----------|-------|
| `NameError` | Il nome della variabile non esiste |
| `TypeError` | Tipo sbagliato — ad es. sommare una stringa a un intero |
| `ValueError` | Tipo giusto ma valore sbagliato — ad es. `int("hello")` |
| `IndexError` | Indice della lista fuori intervallo |
| `KeyError` | La chiave del dizionario non esiste |
| `ZeroDivisionError` | Divisione per zero |
| `AttributeError` | Il metodo non esiste sull'oggetto |
| `FileNotFoundError` | Il file non si trova |

## Leggere un Traceback

Quando Python va in crash, stampa un **traceback** — una traccia di esattamente dove le cose sono andate male.

```
Traceback (most recent call last):
  File "my_program.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

Leggi dal **basso verso l'alto**:
1. L'ultima riga dà il tipo di eccezione e il messaggio: `ZeroDivisionError: division by zero`
2. Sopra di essa, il codice esatto che è andato in crash: `result = 10 / 0`
3. File e numero di riga così sai dove guardare: `line 5`

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto ha un bug. Quale riga andrà in crash, e quale tipo di eccezione apparirà?
    Fai la tua previsione — poi eseguilo!

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
initCmLab('', `numbers = [10, 20, 30]
print("Primo:", numbers[0])
print("Ultimo:", numbers[5])   # questa riga fallirà!
print("Questa riga non viene mai eseguita.")`);
</script>

Avevi indovinato? `IndexError: list index out of range` — l'indice 5 non esiste in una lista di 3 elementi.

## I Blocchi `try/except`

Un blocco `try/except` permette al tuo programma di catturare un errore e gestirlo con eleganza invece di andare in crash.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Non si può dividere per zero!")
```

Struttura:
1. `try:` — metti qui il codice rischioso
2. `except ErrorType:` — metti qui il codice di recupero; gira solo se si verifica quell'errore

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
initCmLab('-2', `def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Errore: non si può dividere per zero!")
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(7, 3))`);
</script>

## Catturare Eccezioni Specifiche

Cattura più tipi di eccezione con più clausole `except`:

```python
try:
    number = int(input("Inserisci un numero: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("Questo non è un numero valido!")
except ZeroDivisionError:
    print("Non si può dividere per zero!")
```

Catturare eccezioni specifiche è meglio di un semplice `except:` — previene il nascondere bug che non intendevi catturare.

## Le Clausole `else` e `finally`

Due clausole extra opzionali rendono `try/except` ancora più potente:

- `else:` gira solo se il blocco `try` si è completato senza nessuna eccezione
- `finally:` gira **sempre** — che si sia verificata o no un'eccezione; perfetta per la pulizia

```python
try:
    n = int(input("Numero: "))
    result = 10 / n
except (ValueError, ZeroDivisionError) as e:
    print(f"Errore: {e}")
else:
    print(f"Risultato: {result}")   # solo se non si è verificata nessuna eccezione
finally:
    print("Fatto.")               # viene sempre eseguito
```

## L'Istruzione `raise`

Usa `raise` per innescare tu stesso un'eccezione quando l'input viola una regola:

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
initCmLab('-3', `def set_speed(speed):
    if speed < 0:
        raise ValueError("La velocità non può essere negativa.")
    if speed > 300:
        raise ValueError("La velocità supera il massimo (300 km/h).")
    return speed

for s in [60, -10, 400]:
    try:
        result = set_speed(s)
        print(f"Velocità impostata a {result}")
    except ValueError as e:
        print(f"Non valido: {e}")`);
</script>

## L'Istruzione `assert`

`assert condizione, "messaggio"` controlla che qualcosa che credi vero sia effettivamente vero.
Se non lo è, genera `AssertionError`. Usala per controlli interni durante lo sviluppo.

```python
def square(n):
    result = n * n
    assert result >= 0, "Il quadrato non deve essere negativo!"
    return result
```

## Validare l'Input Prima della Conversione

`input()` restituisce sempre una **stringa** — anche quando chiedi un numero. Convertirla direttamente con `int()` va in crash se il testo non è un numero valido:

```python
def cast_to_int():
    user_input = input("Inserisci un numero intero: ")
    return int(user_input)   # va in crash con un ValueError se l'input non è valido

print(cast_to_int())
```

Scrivere una parola invece di un numero genera `ValueError: invalid literal for int() with base 10`. Puoi catturare l'input sbagliato *prima* che vada in crash controllandolo prima con il metodo di stringa `.isdigit()`, poi usando `assert` per fermarti con un messaggio chiaro se il controllo fallisce:

```python
def cast_to_int():
    user_input = input("Inserisci un numero intero: ")
    assert user_input.isdigit(), "Non hai inserito un numero intero!"
    return int(user_input)

print(cast_to_int())
```

`.isdigit()` restituisce `True` solo se ogni carattere nella stringa è una cifra, quindi cattura l'input sbagliato prima che `int()` venga mai eseguito.

## Debug con `print()`

Il più semplice strumento di debug è un'istruzione `print()` strategica. Inseriscile per vedere cosa fa il tuo programma a ogni passo:

```python
def total_price(items):
    total = 0
    for item in items:
        print(f"  DEBUG: aggiungo {item}")   # print di debug temporaneo
        total += item
    print(f"  DEBUG: total = {total}")
    return total
```

Rimuovi i print di debug una volta corretto il problema.

!!! mascot-tip "Usare i Motori di Ricerca per Fare Debug"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Quando vedi un errore che non riconosci, copia l'ultima riga del traceback e incollala in un motore di ricerca — aggiungi "Python" all'inizio.
    La comunità Python è enorme e quasi certamente qualcuno ha già avuto lo stesso errore prima!
    Leggere le soluzioni su Stack Overflow è il modo in cui i programmatori professionisti fanno debug ogni giorno.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Racchiudi il Codice Pericoloso"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto va in crash quando l'utente inserisce qualcosa che non è un numero.
    Racchiudi la chiamata a `int()` in un blocco `try/except ValueError` così che stampi un messaggio gentile invece!

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
initCmLab('-4', `raw = input("Inserisci un numero: ")

# Racchiudi questo codice in try/except, così non va in crash con un input sbagliato:
n = int(raw)
print(f"Doppio: {n * 2}")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Scrivi del codice che innesca deliberatamente un `NameError` usando una variabile non definita, poi catturalo.
   **Saprai che ha funzionato quando** l'errore viene catturato e appare un messaggio gentile invece di un crash.

2. Scrivi una funzione `safe_index(lst, i)` che restituisce `lst[i]` oppure `None` se `i` è fuori intervallo.
   **Saprai che ha funzionato quando** `safe_index([1,2,3], 10)` restituisce `None` senza andare in crash.

3. Aggiungi una clausola `else` a un `try/except` che stampa `"Success!"` solo quando non si verifica nessun errore.
   **Saprai che ha funzionato quando** l'input valido mostra "Success!" e l'input non valido no.

4. Aggiungi una clausola `finally` che stampa sempre `"Calculation complete."` a prescindere da tutto.
   **Saprai che ha funzionato quando** il messaggio appare sia per l'input valido sia per quello non valido.

5. Usa `assert` per verificare che una lista abbia esattamente 3 elementi. Testa con liste di lunghezze diverse.
   **Saprai che ha funzionato quando** una lista di 2 elementi genera `AssertionError` e una lista di 3 elementi passa.

!!! mascot-celebration "Campione del Debugging!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora puoi leggere i traceback, catturare le eccezioni, generare i tuoi errori, e fare debug come un professionista!
    Queste competenze trasformano i messaggi di errore da ostacoli in strumenti.
    Questo è un grande passo avanti. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
