---
title: Altri Booleani e Condizionali
description: Approfondisci la tua comprensione della truthiness, della valutazione a corto circuito, delle espressioni ternarie, di match/case, e delle condizioni composte
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:10:00
version: 0.09
---

# Altri Booleani e Condizionali

Alla fine di questa lezione sarai in grado di:

- Spiegare la **truthiness** e la **falsiness** — come qualsiasi valore Python possa comportarsi come True o False
- Usare la **valutazione a corto circuito** per scrivere condizioni più sicure e veloci
- Scrivere **espressioni ternarie** compatte e usare l'istruzione `match/case` di Python
- Combinare condizioni con `and`, `or`, e `not` per costruire una logica booleana potente

Hai usato le istruzioni `if` dal Capitolo 9. Ora è il momento di capire come funziona davvero il sistema di verità di Python — e sbloccare alcune scorciatoie potenti.

!!! mascot-welcome "Benvenuto/a al Capitolo 19!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sapevi che Python tratta molte cose come True o False — non solo `True` e `False`?
    Oggi sbirceremo dietro le quinte e scopriremo alcuni trucchi booleani intelligenti!
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Truthiness e Falsiness

In Python, **ogni valore** può essere testato in un'istruzione `if`, non solo `True` e `False`.

Un valore è **falsy** se Python lo tratta come `False` in un contesto booleano:

| Valori falsy |
|-------------|
| `False` |
| `0` (intero zero) |
| `0.0` (float zero) |
| `""` (stringa vuota) |
| `[]` (lista vuota) |
| `{}` (dizionario vuoto) |
| `None` |

Tutto il resto è **truthy** — inclusi i numeri diversi da zero, le stringhe non vuote, e le liste non vuote.

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
initCmLab('', `values = [0, 1, "", "hello", [], [0], None, False, True]
for v in values:
    label = "TRUTHY" if v else "FALSY"
    print(repr(v), "->", label)`);
</script>

La truthiness ti permette di scrivere controlli concisi. Invece di `if len(name) > 0:`, scrivi semplicemente `if name:`.

## Valutazione a Corto Circuito

Quando Python valuta un'espressione `and` o `or`, si ferma non appena conosce la risposta.
Questo si chiama **valutazione a corto circuito** (short-circuit evaluation).

Con `and`: se il lato sinistro è falsy, Python lo restituisce immediatamente senza controllare il lato destro.
Con `or`: se il lato sinistro è truthy, Python lo restituisce immediatamente.

Questo è importante perché può prevenire errori — e fornisce un utile pattern di valore predefinito:

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
initCmLab('-2', `name = ""
greeting = name or "sconosciuto"   # se name è falsy, usa "sconosciuto"
print(f"Ciao, {greeting}!")

name = "Monty"
greeting = name or "sconosciuto"   # name è truthy, quindi viene usato
print(f"Ciao, {greeting}!")

# and fa il cortocircuito: se data è None, .upper() non viene mai eseguito
data = None
result = data and data.upper()
print("Risultato:", result)   # None — nessun crash!`);
</script>

## Funzioni che Restituiscono None

Ogni funzione Python che non ha un'istruzione `return` restituisce automaticamente `None`.
Questo spiazza molti principianti:

```python
def add(a, b):
    result = a + b
    # dimenticato di scrivere: return result

x = add(3, 4)
print(x)   # None — ops!
```

Usa sempre `return` quando vuoi che una funzione restituisca un valore.

## Controllare None con `is`

Per controllare se un valore è `None`, usa `is None` piuttosto che `== None`.

```python
result = get_data()

if result is None:
    print("Non è tornato niente")
else:
    print("Ricevuto:", result)
```

`is` controlla l'identità (lo stesso identico oggetto in memoria), mentre `==` controlla l'uguaglianza di valore.
Per `None`, `True`, e `False`, usa sempre `is`.

## Conversione Implicita vs Esplicita

Python a volte converte i valori automaticamente — questo si chiama **conversione implicita**.
Quando converti deliberatamente usando `int()`, `str()`, ecc., questo si chiama **conversione esplicita**.

```python
# Implicita: Python converte automaticamente int in float nei calcoli misti
result = 3 + 2.5   # 5.5 — l'int 3 è diventato automaticamente il float 3.0

# Esplicita: sei tu a controllare la conversione
n = int("42")
s = str(3.14)
b = bool(0)
```

Capire la differenza ti aiuta a individuare dove Python ti sta "aiutando" — e quando quell'aiuto potrebbe causare sorprese.

## Leggere Input Multipli

Puoi chiedere diversi valori su una riga usando `split()`:

```python
x, y = input("Inserisci x e y: ").split()
x = int(x)
y = int(y)
print(f"Somma: {x + y}")
```

L'utente scrive qualcosa come `3 7`, `split()` restituisce `["3", "7"]`, e Python lo scompone in `x` e `y`.

## L'Espressione Ternaria Condizionale

Un'**espressione ternaria** condensa un semplice if/else in una sola riga.
Il formato è: `valore_se_vero if condizione else valore_se_falso`.

```python
# if/else normale:
if score >= 70:
    grade = "pass"
else:
    grade = "fail"

# Ternario — stesso risultato, in una riga:
grade = "pass" if score >= 70 else "fail"
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto usa un'espressione ternaria annidata.
    Cosa stamperà per `score = 85`? E per `score = 55`?
    Fai la tua previsione — poi eseguilo!

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
initCmLab('-3', `for score in [95, 85, 55]:
    label = "eccellente" if score >= 90 else ("buono" if score >= 70 else "da migliorare")
    print(f"Punteggio {score}: {label}")`);
</script>

## Condizioni Composte

Usa `and`, `or`, e `not` per combinare più condizioni:

```python
age = 15
has_ticket = True

if age >= 13 and has_ticket:
    print("Puoi entrare.")

if age < 5 or age > 65:
    print("Ingresso ridotto!")

if not has_ticket:
    print("Ti serve un biglietto!")
```

| Operatore | Significato | Vero quando |
|----------|---------|-----------|
| `and` | Entrambi devono essere veri | `True and True` |
| `or` | Almeno uno deve essere vero | `True or False` |
| `not` | Inverte vero/falso | `not False` |

## `match/case` — Il Pattern Matching di Python

Python 3.10 ha introdotto **`match/case`**, che confronta un valore con diversi pattern — simile a una lunga catena di `if/elif` ma molto più pulito.

```python
command = input("Comando (start/stop/pause): ").strip().lower()

match command:
    case "start":
        print("Avvio!")
    case "stop":
        print("Mi fermo!")
    case "pause":
        print("In pausa!")
    case _:
        print("Comando sconosciuto.")
```

Il caso `_` è il **carattere jolly** (wildcard) — corrisponde a qualsiasi cosa non già gestita.
Usa `|` dentro un case per far corrispondere più valori:

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
initCmLab('-4', `day = input("Inserisci un giorno (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ").strip().title()

match day:
    case "Sat" | "Sun":
        print(f"{day}: Fine settimana!")
    case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
        print(f"{day}: Giorno feriale.")
    case _:
        print(f"I don't recognize '{day}'.")`);
</script>

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Correggi il Valore Predefinito"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe salutare un utente per nome — oppure dire "Ciao, sconosciuto!" se non viene inserito nulla.
    Ma gli operandi di `or` sono invertiti, quindi dice sempre "sconosciuto".
    Scambiali per correggerlo!

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
initCmLab('-5', `name = input("Inserisci il tuo nome (o premi Invio per saltare): ").strip()

# Bug: "sconosciuto" è truthy, quindi vince sempre!
greeting = "sconosciuto" or name

print(f"Ciao, {greeting}!")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Stampa `bool([])`, `bool([0])`, `bool("")`, e `bool(" ")` (uno spazio).
   **Saprai che ha funzionato quando** vedi `False`, `True`, `False`, `True`.

2. Scrivi un'espressione ternaria che restituisce `"even"` se un numero è divisibile per 2, altrimenti `"odd"`.
   **Saprai che ha funzionato quando** `7` dà `"odd"` e `8` dà `"even"`.

3. Usa `match/case` per classificare un punteggio: 90+ → "A", 80–89 → "B", 70–79 → "C", sotto 70 → "F".
   **Saprai che ha funzionato quando** inserendo `85` dà "B".

4. Usa un `or` a corto circuito per assegnare un valore predefinito `timeout = user_value or 30`.
   **Saprai che ha funzionato quando** un input vuoto dà `30` e `"60"` dà `"60"`.

5. Scrivi una condizione composta che valida un nome utente: truthy E lunghezza >= 3 E nessuno spazio.
   **Saprai che ha funzionato quando** `"ab"` fallisce (troppo corto) e `"hello world"` fallisce (ha uno spazio).

!!! mascot-celebration "Maestro dei Booleani!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato la truthiness, il corto circuito, le espressioni ternarie, e match/case!
    Questi strumenti ti permettono di scrivere una logica condizionale più intelligente e pulita in molte meno righe.
    Più ci pratichi, più ti sembreranno naturali. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
