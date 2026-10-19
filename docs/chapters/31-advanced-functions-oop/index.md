---
title: Funzioni Avanzate e OOP
description: Completa le tue competenze di programmazione funzionale e OOP con map, filter, dir, help, le eccezioni personalizzate, @property, i metodi dunder, e la composizione di oggetti
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:10:00
version: 0.09
---

# Funzioni Avanzate e OOP

Alla fine di questa lezione sarai in grado di:

- Usare `map()`, `filter()`, `any()`, `all()`, `chr()`, `ord()`, `dir()`, e `help()` efficacemente
- Creare **classi di eccezione personalizzate** e usare il concatenamento delle eccezioni
- Definire **proprietà** con `@property` e usare i **metodi dunder** per personalizzare il comportamento degli oggetti
- Applicare la **composizione di oggetti** per costruire oggetti complessi da oggetti più semplici

Questo capitolo completa gli strumenti avanzati rimanenti del set di strumenti funzionale e OOP di Python.

!!! mascot-welcome "Benvenuto/a al Capitolo 31!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    È qui che le tue competenze Python raggiungono il livello professionale!
    Eccezioni personalizzate, proprietà, metodi dunder — questi sono gli strumenti che separano il codice da principiante dal codice da esperto.
    Saliamo di livello! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## `map()` e `filter()` con Funzioni Nominate

Hai visto `map()` e `filter()` con le lambda nel Capitolo 22. Funzionano altrettanto bene con funzioni nominate:

```python
def is_even(n):
    return n % 2 == 0

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5, 6]
evens   = list(filter(is_even, numbers))   # [2, 4, 6]
squares = list(map(square, numbers))       # [1, 4, 9, 16, 25, 36]
```

Questo stile è più leggibile delle lambda per la logica complessa.

## `any()` e `all()`

`any(iterable)` restituisce `True` se almeno un elemento è truthy.
`all(iterable)` restituisce `True` se ogni elemento è truthy.

Entrambi fanno corto circuito — si fermano non appena la risposta è conosciuta.

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
initCmLab('', `scores = [75, 92, 88, 60, 95]

print("Qualcuno insufficiente (<70)?", any(s < 70 for s in scores))
print("Tutti promossi (>=60)?", all(s >= 60 for s in scores))
print("Tutti eccellenti (>=90)?", all(s >= 90 for s in scores))

words = ["hello", "world", "Python"]
print("Qualcuna inizia con 'P'?", any(w.startswith("P") for w in words))`);
</script>

## `chr()` e `ord()` — Caratteri e Codici ASCII

`ord(character)` converte un carattere nel suo codice intero ASCII (Unicode).
`chr(integer)` fa il contrario — converte un intero nel suo carattere.

```python
print(ord("A"))   # 65
print(ord("a"))   # 97
print(chr(65))    # "A"
print(chr(9829))  # "♥" — il cuore Unicode
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
initCmLab('-2', `# Stampa le lettere dalla A alla Z usando chr() e ord():
for code in range(ord("A"), ord("Z") + 1):
    print(chr(code), end=" ")
print()

# Semplice cifrario di Cesare (sposta ogni lettera di 3):
def encrypt(text, shift=3):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

print(encrypt("Hello, World!"))`);
</script>

## `dir()` e `help()` — Esplorare gli Oggetti

`dir(obj)` restituisce una lista di tutti gli attributi e i metodi disponibili su `obj`.
`help(obj)` stampa la documentazione dettagliata.

Questi sono i tuoi migliori amici quando esplori un modulo o un oggetto non familiare:

```python
import math
print(dir(math))         # mostra tutte le funzioni di math
help(math.sqrt)          # la documentazione completa di sqrt
```

## `id()` e `hash()`

`id(obj)` restituisce l'indirizzo di memoria unico di un oggetto.
Due variabili con lo stesso `id` sono lo stesso oggetto — non solo uguali, ma letteralmente lo stesso in memoria.

`hash(obj)` restituisce un valore hash (un'impronta digitale intera). I dizionari usano gli hash per ricerche rapide.
Solo gli oggetti immutabili (stringhe, numeri, tuple) possono essere hashati.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto confronta `is` vs `==` per le stringhe. Le stringhe piccole condivideranno lo stesso id?
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
initCmLab('-3', `a = "hello"
b = "hello"
c = "hel" + "lo"   # costruita a pezzi durante l'esecuzione

print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("id(a):", id(a))
print("id(b):", id(b))
print("id(c):", id(c))`);
</script>

## Classi di Eccezione Personalizzate

Puoi creare i tuoi propri tipi di eccezione facendo una sottoclasse di `Exception`.
Le eccezioni personalizzate rendono i tuoi messaggi di errore molto più chiari per chi usa il tuo codice.

```python
class InvalidAgeError(ValueError):
    pass

class NegativeBalanceError(Exception):
    def __init__(self, amount):
        super().__init__(f"Impossibile prelevare {amount} $ — il saldo diventerebbe negativo.")
        self.amount = amount
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
initCmLab('-4', `class InvalidScoreError(ValueError):
    def __init__(self, score):
        super().__init__(f"Il punteggio {score} è fuori dall'intervallo (0-100).")
        self.score = score

def record_score(score):
    if not (0 <= score <= 100):
        raise InvalidScoreError(score)
    return score

for s in [85, 110, -5, 0, 100]:
    try:
        print(f"Registrato: {record_score(s)}")
    except InvalidScoreError as e:
        print(f"Errore: {e}")`);
</script>

## Metodi Statici

Un **metodo statico** appartiene alla classe ma non ha bisogno di accedere a `self` (l'istanza).
Decoralo con `@staticmethod`. Usalo per funzioni di utilità che logicamente appartengono alla classe.

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

print(Temperature.celsius_to_fahrenheit(100))   # 212.0
```

## Proprietà con `@property`

Una **proprietà** ti permette di definire un metodo che si comporta come un attributo.
Questo ti permette di aggiungere validazione o calcolo all'accesso degli attributi senza cambiare l'interfaccia.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Il raggio non può essere negativo.")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)   # chiama il getter
print(c.area)     # proprietà calcolata
c.radius = 10     # chiama il setter (che controlla il valore!)
```

## Panoramica dei Metodi Dunder

I **metodi dunder** (chiamati anche "metodi magici") sono metodi speciali con doppio underscore su entrambi i lati.
Hai già visto `__init__` e `__str__`. Ce ne sono molti altri:

| Metodo | Chiamato quando |
|--------|------------|
| `__len__(self)` | `len(obj)` |
| `__add__(self, other)` | `obj + other` |
| `__eq__(self, other)` | `obj == other` |
| `__lt__(self, other)` | `obj < other` |
| `__contains__(self, item)` | `item in obj` |
| `__iter__(self)` | `for x in obj` |
| `__getitem__(self, key)` | `obj[key]` |

Implementando i dunder, le tue classi personalizzate funzionano naturalmente con gli operatori di Python e le funzioni built-in.

## Composizione di Oggetti

La **composizione di oggetti** significa costruire un oggetto complesso a partire da oggetti più semplici — memorizzando istanze di una classe dentro un'altra.

Questo è spesso meglio delle profonde gerarchie di eredità:

```python
class Engine:
    def __init__(self, horsepower):
        self.hp = horsepower

    def start(self):
        print(f"Motore ({self.hp} CV) in funzione.")

class Car:
    def __init__(self, model, horsepower):
        self.model  = model
        self.engine = Engine(horsepower)   # composizione!

    def drive(self):
        self.engine.start()
        print(f"{self.model} è in movimento.")

car = Car("Python GT", 300)
car.drive()
```

!!! mascot-tip "Composizione invece di Eredità"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Gli sviluppatori Python professionisti preferiscono la composizione alle profonde gerarchie di eredità.
    Invece di `ElectricCar(Car(Vehicle))`, costruisci `ElectricCar` con un attributo `engine`.
    È più facile cambiare singole parti senza rompere codice non collegato.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Metodo Dunder"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La classe `Bag` sotto memorizza elementi, ma `len(bag)` non funziona ancora.
    Aggiungi il metodo dunder `__len__` così che `len(bag)` restituisca il numero di elementi!

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
initCmLab('-5', `class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    # Aggiungi qui __len__, così len(bag) funziona:

bag = Bag()
bag.add("apple")
bag.add("banana")
bag.add("mango")

print("Oggetti:", bag.items)
print("Quanti:", len(bag))   # questa riga fallisce finché non aggiungi __len__`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Usa `any()` per controllare se qualche stringa in una lista ha più di 10 caratteri.
   **Saprai che ha funzionato quando** il risultato è `True` o `False` in base alle lunghezze effettive.

2. Scrivi una funzione di decrittazione del cifrario di Cesare (spostamento di -3 invece di +3). Cripta poi decripta "Hello".
   **Saprai che ha funzionato quando** ottieni di nuovo l'originale "Hello".

3. Aggiungi `__add__` alla classe `Bag` così che `bag1 + bag2` restituisca un nuovo Bag con tutti gli elementi di entrambi.
   **Saprai che ha funzionato quando** `len(bag1 + bag2)` è uguale a `len(bag1) + len(bag2)`.

4. Aggiungi `@property area` a una classe `Rectangle`. Assicurati che venga ricalcolata ogni volta che width o height cambia.
   **Saprai che ha funzionato quando** cambiare `r.width = 10` aggiorna automaticamente `r.area`.

5. Crea una classe `Stack` usando la composizione (ha un attributo `list`) con `push`, `pop`, `peek`, e `__len__`.
   **Saprai che ha funzionato quando** tutte e quattro le operazioni funzionano come previsto.

!!! mascot-celebration "Esperto Python!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai raggiunto il livello avanzato di Python! Eccezioni personalizzate, proprietà, dunder, e composizione sono strumenti usati ogni giorno dagli sviluppatori Python professionisti.
    Gli ultimi capitoli ti portano nel territorio della data science e del machine learning. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
