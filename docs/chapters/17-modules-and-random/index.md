---
title: Moduli e Numeri Casuali
description: Impara come importare moduli, usare gli alias, e sfruttare il modulo random per costruire giochi e arte generativa
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:50:00
version: 0.09
---

# Moduli e Numeri Casuali

Alla fine di questa lezione sarai in grado di:

- Importare un modulo usando la sintassi `import`, `from...import`, e `import...as`
- Generare interi casuali con `random.randint()` e float casuali con `random.random()`
- Scegliere elementi casuali con `random.choice()` e mescolare una lista con `random.shuffle()`
- Usare `random.seed()` per rendere ripetibili i tuoi risultati casuali

Python viene fornito con un'enorme libreria di strumenti extra chiamati **moduli**.
Invece di scrivere tutto da zero, fai `import` dello strumento di cui hai bisogno.
Il modulo `random` è uno dei più divertenti — ti permette di aggiungere sorpresa e varietà ai tuoi programmi.

!!! mascot-welcome "Benvenuto/a al Capitolo 17!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I moduli sono come dei potenziamenti per i tuoi programmi! Importane uno e improvvisamente puoi fare
    cose che Python non poteva fare da solo. Oggi sblocchiamo il modulo `random` —
    perfetto per giochi e arte generativa. Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## L'Istruzione `import`

La libreria standard di Python contiene decine di moduli pronti all'uso.
Per caricare un modulo, scrivi `import module_name` in cima al tuo programma.
Dopo l'importazione, accedi alle sue funzioni con `module.function()`.

```python
import random
print(random.randint(1, 10))   # random number between 1 and 10
```

## `from...import` — Prendi Nomi Specifici

Se hai bisogno solo di una o due funzioni da un modulo, puoi importare solo quei nomi.
Dopo un `from...import`, chiami la funzione direttamente senza il prefisso del modulo.

```python
from random import randint, choice

print(randint(1, 6))       # no "random." needed
print(choice(["a","b","c"]))
```

## `import...as` — Dai un Soprannome a un Modulo

I nomi lunghi dei moduli possono essere abbreviati con `as`:

```python
import random as rnd
print(rnd.randint(1, 100))
```

## `from...import *` — Importa Tutto

`from random import *` importa ogni nome pubblico dal modulo.
Questo è comodo ma può causare confusione se due moduli definiscono una funzione con lo stesso nome.
Usalo solo per esperimenti rapidi, non in programmi seri.

## Il Modulo `random`

Il modulo `random` genera numeri che sembrano imprevedibili.

Prima di provare ogni funzione, ecco un riepilogo di quelle principali:

| Funzione | Restituisce | Esempio |
|----------|---------|---------|
| `randint(a, b)` | Intero casuale da a a b (inclusi) | `randint(1, 6)` → 4 |
| `random()` | Float casuale da 0.0 a 1.0 | `random()` → 0.73... |
| `choice(seq)` | Un elemento casuale da una lista | `choice(["red","blue"])` |
| `shuffle(lst)` | Mescola una lista sul posto (restituisce None) | `shuffle(cards)` |
| `sample(seq, k)` | Lista di k elementi casuali unici | `sample(range(1,50), 6)` |
| `seed(n)` | Imposta il punto di partenza casuale | `seed(42)` → stessi risultati ogni volta |

## `random.randint()` — Interi Casuali

`randint(a, b)` restituisce un intero casuale dove `a <= result <= b`.
Entrambi gli estremi sono inclusi.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto simula il lancio di un dado a 6 facce cinque volte.
    Otterrai mai lo stesso numero due volte di fila? Fai la tua previsione — poi eseguilo!

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
initCmLab('', `import random

print("Rolling a die 5 times:")
for i in range(5):
    roll = random.randint(1, 6)
    print(f"  Roll {i+1}: {roll}")`);
</script>

Eseguilo un paio di volte — i risultati cambiano ogni volta perché i numeri sono casuali.

### Guardalo: La Casualità ha una Forma

Cinque lanci sembrano puro caos. Ma cosa succede dopo **mille** lanci? Prima di cliccare qualcosa nell'istogramma sotto, prevedi: **dopo 1000 lanci di un dado, alcune facce usciranno molto più di altre, o le barre saranno più o meno uguali?**

<iframe src="../../sims/dice-roll-histogram/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Dice Roll Histogram](../../sims/dice-roll-histogram/index.md){ .md-button }

Ora passa il menu a tendina a **Sum of two dice** e lancia di nuovo 1000 volte. Il profilo piatto si trasforma in una montagna con il picco al 7 — riesci a capire perché ci sono più modi per ottenere un 7 che un 2? Quella scoperta è il seme della probabilità.

## `random.choice()` — Scegli da una Lista

`choice(seq)` sceglie un elemento casuale da una sequenza (lista, stringa, o tupla).

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
initCmLab('-2', `import random

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
print("Random color:", random.choice(colors))

directions = ["left", "right", "forward", "back"]
print("Random direction:", random.choice(directions))`);
</script>

## `random.shuffle()` — Mescola una Lista

`shuffle(lst)` riorganizza gli elementi di una lista in ordine casuale.
Modifica la lista **sul posto** e restituisce `None` — quindi non scrivere `lst = shuffle(lst)`.

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
initCmLab('-3', `import random

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print("Before shuffle:", cards[:5], "...")
random.shuffle(cards)
print("After shuffle: ", cards[:5], "...")`);
</script>

## `random.random()` — Float Casuale

`random()` restituisce un float tra 0.0 e 1.0. Il risultato può essere esattamente 0.0 ma non è mai esattamente 1.0.

Questo è utile quando vuoi una *percentuale* o una *probabilità*. Moltiplica per scalarlo:

```python
import random
prob = random.random()           # between 0.0 and 1.0
scaled = random.random() * 100  # between 0.0 and 100.0
```

## `random.sample()` — Scegli Senza Ripetizione

`sample(seq, k)` sceglie `k` elementi unici dalla sequenza (senza ripetizioni).
È come estrarre numeri della lotteria — una volta estratto un numero, non può essere estratto di nuovo.

```python
import random
lottery = random.sample(range(1, 50), 6)
print("Lottery numbers:", sorted(lottery))
```

## `random.seed()` — Casualità Ripetibile

Ogni volta che esegui un programma casuale, Python usa un punto di partenza diverso (chiamato **seme**) così che i risultati siano diversi.

Se chiami `random.seed(n)` con lo stesso numero ogni volta, ottieni esattamente la stessa sequenza "casuale".
Questo è utile per i test — vuoi che il tuo programma si comporti nello stesso modo durante i test.

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
initCmLab('-4', `import random

random.seed(42)
print("With seed 42:", [random.randint(1, 10) for _ in range(5)])

random.seed(42)   # reset to the same seed
print("Same again: ", [random.randint(1, 10) for _ in range(5)])

# No seed — different every run:
print("No seed:   ", [random.randint(1, 10) for _ in range(5)])`);
</script>

## Arte Casuale con Turtle

Mettiamo `random` al lavoro con la grafica turtle — colori, dimensioni, e posizioni casuali per creare arte generativa.

<div class="cm-lab">
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
initCmLab('-5', `import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

colors = ["#FF6B6B", "#FFE66D", "#4ECDC4", "#95E1D3", "#F38181", "#A8E6CF"]

for _ in range(40):
    t.penup()
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    t.goto(x, y)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.pensize(random.randint(1, 4))
    size = random.randint(10, 50)
    sides = random.randint(3, 8)
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    for i in range(sides):
        t.forward(size)
        t.right(360 / sides)
    t.end_fill()`);
</script>

Eseguilo più volte — grazie alla casualità, otterrai un'opera diversa ogni singola volta!

## Creare il Tuo Proprio Modulo

Finora hai solo *usato* moduli che già esistono. Puoi anche **crearne** uno tuo — impacchettare un insieme di funzioni in un file `.py` così che altri programmi (o il tuo futuro te stesso) possano farne `import`, esattamente come `random`.

!!! mascot-warning "Questo Richiede un Vero Ambiente Python"
    ![Monty with a warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Creare un file separato e importarlo funziona solo con una vera installazione Python — Thonny, VS Code, o il terminale. Skulpt esegue un singolo file, quindi questa sezione usa normali blocchi di codice invece di un laboratorio interattivo.

Salva le funzioni sotto in un file chiamato `fibo.py`:

```python
# fibo.py
def fib(n):    # print the Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):   # return the Fibonacci series up to n as a list
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
```

Poi, in un file **diverso** salvato nella stessa cartella, fanne `import` con il suo nome di file (senza il `.py`):

```python
import fibo

fibo.fib(100)            # 0 1 1 2 3 5 8 13 21 34 55 89
numbers = fibo.fib2(100)
print(numbers)            # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

Puoi anche prendere una funzione direttamente, proprio come hai fatto con `random`:

```python
from fibo import fib

fib(20)
```

Python tratta ogni file `.py` allo stesso modo — sia che venga fornito con la libreria standard sia che tu l'abbia scritto cinque minuti fa.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Correggi lo Shuffle"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto cerca di mescolare una lista e stamparla, ma ha un bug —
    assegna il valore di ritorno di `shuffle()` a `cards`, perdendo la lista!
    Correggilo così che la lista venga davvero mescolata e stampata.

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-6"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-6')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-6')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-6"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-6"></div>
  </div>
</div>
<script>
initCmLab('-6', `import random

cards = ["A", "2", "3", "4", "5"]

# Bug: shuffle returns None, not the shuffled list!
cards = random.shuffle(cards)

print("Shuffled:", cards)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Simula il lancio di una moneta 10 volte. Usa `random.choice(["heads", "tails"])` e conta quante teste ottieni.
   **Saprai che ha funzionato quando** vedi un conteggio tra 0 e 10.

2. Scegli 6 numeri della lotteria da 1–49 usando `random.sample(range(1, 50), 6)`. Stampali ordinati.
   **Saprai che ha funzionato quando** vedi 6 numeri unici in ordine.

3. Cambia il conteggio del ciclo dell'arte casuale da `40` a `100`. Nota l'effetto.
   **Saprai che ha funzionato quando** il canvas è molto più riempito di forme.

4. Imposta `random.seed(7)` prima del ciclo dell'arte casuale. Eseguilo due volte.
   **Saprai che ha funzionato quando** entrambe le esecuzioni producono opere identiche.

5. Usa `random.random()` per simulare un evento con il 30% di probabilità: stampa `"Lucky!"` se il risultato è sotto `0.3`.
   Eseguilo 10 volte con un ciclo.
   **Saprai che ha funzionato quando** circa 3 iterazioni su 10 stampano "Lucky!".

!!! mascot-celebration "Mago della Casualità!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato i moduli e padroneggiato il modulo `random`!
    Giochi, simulazioni, e arte generativa dipendono tutti dalla casualità — e ora puoi usarla anche tu.
    Nel prossimo capitolo aggiungeremo potere matematico ai tuoi programmi con la tartaruga. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
