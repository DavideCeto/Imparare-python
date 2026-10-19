---
title: Collezioni Avanzate e Funzioni Built-in
description: Padroneggia enumerate(), zip(), *args, **kwargs, max/min/sum/sorted, map/filter, e potenti pattern di costruzione delle collezioni
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:40:00
version: 0.09
---

# Collezioni Avanzate e Funzioni Built-in

Alla fine di questa lezione sarai in grado di:

- Usare `enumerate()` per cicli indicizzati e `zip()` per combinare iterabili
- Scrivere funzioni flessibili con `*args` e `**kwargs`
- Costruire dizionari da due liste usando `zip()`
- Usare `max()`, `min()`, `sum()`, `sorted()`, `reversed()`, `map()`, e `filter()` con sicurezza

Le funzioni built-in di Python sono un set di strumenti potente. Questo capitolo raccoglie le più utili così puoi scrivere codice più corto e pulito che fa di più.

!!! mascot-welcome "Benvenuto/a al Capitolo 22!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il set di strumenti built-in di Python è come un coltellino svizzero — c'è uno strumento per quasi tutto!
    Oggi imparerai quelli a cui ricorrerai più spesso.
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## `enumerate()` — Ciclo con un Indice

`enumerate(iterable)` incapsula una lista (o qualsiasi sequenza) e ti dà sia l'indice *sia* l'elemento a ogni iterazione del ciclo.
Senza `enumerate()`, avresti bisogno di una variabile contatore separata.

```python
# Senza enumerate — contatore manuale:
fruits = ["apple", "banana", "mango"]
for i in range(len(fruits)):
    print(i, fruits[i])

# Con enumerate — più pulito:
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Entrambi producono lo stesso output. `enumerate()` inizia da 0 per default; usa `enumerate(fruits, 1)` per iniziare da 1.

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
initCmLab('', `menu = ["Burger", "Pizza", "Salad", "Pasta"]

print("Menù:")
for num, item in enumerate(menu, 1):
    print(f"  {num}. {item}")`);
</script>

## `zip()` — Combina Iterabili in Parallelo

`zip(a, b)` accoppia gli elementi di due (o più) iterabili passo dopo passo.
Si ferma quando il più corto degli iterabili finisce.

```python
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 91]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto fa lo zip di due liste di lunghezza diversa.
    Quante coppie pensi che produrrà `zip()`?
    Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `letters = ["A", "B", "C", "D", "E"]
numbers = [1, 2, 3]

pairs = list(zip(letters, numbers))
print("Coppie:", pairs)
print("Quante:", len(pairs))`);
</script>

Avevi indovinato? `zip()` si ferma a 3 coppie perché `numbers` finisce per primo.

## Dizionario da Due Liste con `zip()`

Combina `zip()` con `dict()` per costruire un dizionario da due liste parallele — una di chiavi, una di valori:

```python
keys   = ["name", "age", "city"]
values = ["Alice", 14, "Paris"]

d = dict(zip(keys, values))
print(d)   # {"name": "Alice", "age": 14, "city": "Paris"}
```

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
initCmLab('-3', `countries = ["France", "Japan", "Brazil"]
capitals  = ["Paris", "Tokyo", "Brasília"]

capital_map = dict(zip(countries, capitals))
print(capital_map)
print("Capitale del Giappone:", capital_map["Japan"])`);
</script>

## `*args` — Numero Variabile di Argomenti Posizionali

A volte vuoi una funzione che possa accettare qualsiasi numero di argomenti.
`*args` raccoglie tutti gli argomenti posizionali extra in una tupla.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(10, 20))        # 30
print(total(5, 5, 5, 5))    # 20
```

## `**kwargs` — Numero Variabile di Argomenti Keyword

`**kwargs` raccoglie gli argomenti keyword extra in un dizionario.

```python
def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

describe(name="Monty", species="python", color="green")
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
initCmLab('-4', `def total(*args):
    return sum(args)

def describe(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Totale:", total(10, 20, 30, 40))

print("Profilo di Monty:")
describe(name="Monty", level=7, language="Python")`);
</script>

## Funzioni di Aggregazione: `max()`, `min()`, `sum()`

Queste tre funzioni built-in funzionano su qualsiasi iterabile di numeri (o di valori comparabili per max/min):

```python
scores = [73, 100, 87, 55, 92]

print("Massimo:", max(scores))    # 100
print("Minimo:", min(scores))    # 55
print("Somma:", sum(scores))    # 407
print("Media:", sum(scores) / len(scores))  # 81.4
```

## `sorted()` e `reversed()`

`sorted(iterable)` restituisce una nuova lista ordinata senza modificare l'originale.
`reversed(iterable)` restituisce un iteratore che scorre gli elementi in ordine inverso.

| Funzione | Modifica l'originale? | Restituisce |
|----------|-------------------|---------|
| `list.sort()` | Sì | None |
| `sorted(list)` | No | Nuova lista ordinata |
| `list.reverse()` | Sì | None |
| `reversed(list)` | No | Iteratore |

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(numbers)               # crescente
desc_nums   = sorted(numbers, reverse=True) # decrescente
```

## `isinstance()` — Controllo del Tipo

`isinstance(value, type)` restituisce `True` se il valore è del tipo dato (o di un sottotipo).
È più sicuro che usare `type(x) == int` perché gestisce l'eredità.

```python
print(isinstance(42, int))         # True
print(isinstance(3.14, float))     # True
print(isinstance("hi", str))       # True
print(isinstance([1,2], list))     # True
print(isinstance(42, (int, float)))# True — si possono indicare più tipi
```

## `map()` e `filter()`

`map(func, iterable)` applica una funzione a ogni elemento e restituisce i risultati.
`filter(func, iterable)` mantiene solo gli elementi per cui la funzione restituisce `True`.

Entrambi restituiscono iteratori — racchiudili in `list()` per vedere i risultati:

```python
numbers = [1, 2, 3, 4, 5, 6]

doubled  = list(map(lambda x: x * 2, numbers))
evens    = list(filter(lambda x: x % 2 == 0, numbers))

print("Raddoppiati:", doubled)   # [2, 4, 6, 8, 10, 12]
print("Pari:", evens)       # [2, 4, 6]
```

Una **lambda** è una piccola funzione anonima scritta su una riga: `lambda x: x * 2` significa "prendi x, restituisci x per 2."

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
initCmLab('-5', `scores = [45, 78, 92, 61, 88, 73, 55]

passing  = list(filter(lambda s: s >= 70, scores))
bonus    = list(map(lambda s: s + 5, scores))

print("Punteggi sufficienti:", passing)
print("Tutti i punteggi + 5:", bonus)
print("Massimo:", max(scores), "Minimo:", min(scores), "Media:", round(sum(scores)/len(scores), 1))`);
</script>

## Costruttori di Collezioni

Puoi convertire tra tipi di collezione usando `list()`, `tuple()`, `set()`, e `dict()`:

```python
my_list  = list(range(5))         # [0, 1, 2, 3, 4]
my_tuple = tuple([1, 2, 3])       # (1, 2, 3)
my_set   = set([3, 1, 4, 1, 5])   # {1, 3, 4, 5}
```

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Usa enumerate e zip Insieme"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto stampa i nomi dei giocatori e i loro punteggi, ma l'output sembra disordinato.
    Correggilo per usare `zip()` per accoppiare i nomi con i punteggi e `enumerate()` partendo da 1 per numerare le voci.
    Ogni riga dovrebbe sembrare: `1. Alice: 95`

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
initCmLab('-6', `names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 91]

# Correzione: usa enumerate(zip(...), 1) per stampare "1. Alice: 95" ecc.
for name in names:
    print(name)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Usa `enumerate(["Mon","Tue","Wed","Thu","Fri"], 1)` per stampare una lista numerata dei giorni della settimana.
   **Saprai che ha funzionato quando** vedi `1. Mon`, `2. Tue`, ecc.

2. Scrivi una funzione `my_max(*args)` che restituisce l'argomento più grande senza usare la funzione built-in `max()`.
   **Saprai che ha funzionato quando** `my_max(3, 9, 1, 7)` restituisce `9`.

3. Usa `filter()` per mantenere solo le stringhe più lunghe di 4 caratteri da `["cat","elephant","dog","hippo"]`.
   **Saprai che ha funzionato quando** vedi `["elephant","hippo"]`.

4. Usa `sorted(words, key=len)` per ordinare una lista di parole per la loro lunghezza (la più corta prima).
   **Saprai che ha funzionato quando** le parole corte appaiono prima di quelle lunghe.

5. Usa `dict(zip(range(1, 6), ["one","two","three","four","five"]))` per costruire un dizionario numero-parola.
   **Saprai che ha funzionato quando** `d[3]` stampa `"three"`.

!!! mascot-celebration "Maestro delle Funzioni Built-in!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Sei salito di livello con enumerate, zip, args, kwargs, map, filter, e altro!
    Questi strumenti rendono il codice Python più corto, più leggibile, e più potente.
    I programmatori professionisti usano ognuno di questi regolarmente. Ottimo lavoro!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
