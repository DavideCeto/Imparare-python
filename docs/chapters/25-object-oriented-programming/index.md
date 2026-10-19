---
title: Programmazione Orientata agli Oggetti
description: Crea le tue classi con __init__, self, metodi, eredità, __str__, e variabili di classe vs di istanza
generated_by: claude skill chapter-content-generator
date: 2026-06-28 14:10:00
version: 0.09
---

# Programmazione Orientata agli Oggetti

Alla fine di questa lezione sarai in grado di:

- Definire una **classe** con `__init__()`, `self`, attributi, e metodi
- Creare **istanze** di classe e accedere ai loro attributi con la notazione punto
- Definire un metodo `__str__()` così che `print()` mostri una descrizione utile
- Usare l'**eredità** (inheritance) e `super()` per costruire sottoclassi che estendono classi genitore

Hai usato oggetti fin dall'inizio — la tartaruga, le stringhe, le liste, e i dizionari sono tutti oggetti.
Ora è il momento di crearne di tuoi.

!!! mascot-welcome "Benvenuto/a al Capitolo 25!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Hai usato oggetti come mattoncini Lego — ora puoi progettare i tuoi mattoncini!
    La programmazione orientata agli oggetti è il modo in cui sono organizzati la maggior parte dei grandi programmi Python.
    Costruiamo qualcosa! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Attributi e Metodi

Sai già che gli oggetti hanno **attributi** (dati memorizzati al loro interno) e **metodi** (funzioni che chiami su di essi).

```python
t = turtle.Turtle()
t.speed(5)          # chiamata di metodo
t.pencolor("red")   # chiamata di metodo — imposta un attributo
```

Ora definirai i tuoi propri oggetti.

## La Parola Chiave `class`

Una **classe** è un progetto per creare oggetti.
Usa `class NomeClasse:` seguito da codice indentato che definisce la classe.
Per convenzione, i nomi delle classi usano il **CamelCase** (ogni parola con la maiuscola, nessun underscore).

```python
class Dog:
    pass   # classe vuota — per ora è solo un segnaposto
```

## `__init__()` — Il Costruttore

`__init__()` è il **costruttore** — un metodo speciale che Python chiama automaticamente quando crei una nuova istanza.
Imposta gli attributi iniziali dell'oggetto.

`self` si riferisce all'istanza specifica che viene creata. Ogni metodo in una classe prende `self` come primo parametro.

Prima di definire gli attributi, nota che `self.nome_attributo = valore` memorizza un valore dentro l'oggetto:

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
initCmLab('', `class Dog:
    def __init__(self, name, breed, age):
        self.name  = name    # attributo di istanza
        self.breed = breed
        self.age   = age

    def bark(self):
        print(f"{self.name} dice: Bau!")

    def describe(self):
        print(f"{self.name} è un {self.breed} di {self.age} anni.")

fido  = Dog("Fido", "Labrador", 3)
bella = Dog("Bella", "Poodle", 5)

fido.describe()
bella.bark()
print(fido.name, fido.age)`);
</script>

## Creare Istanze e la Notazione Punto

Ogni volta che chiami la classe come una funzione, Python crea una nuova **istanza** (un oggetto separato dallo stesso progetto).

```python
fido  = Dog("Fido", "Labrador", 3)   # istanza 1
bella = Dog("Bella", "Poodle", 5)    # istanza 2
```

Accedi agli attributi e ai metodi con la **notazione punto**: `fido.name`, `fido.bark()`.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto crea due istanze di `Student`. Quale studente ha il punteggio più alto?
    Cosa stamperà il ciclo per ciascuno? Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `class Student:
    def __init__(self, name, score):
        self.name  = name
        self.score = score

    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        else:
            return "F"

students = [Student("Alice", 92), Student("Bob", 75), Student("Carol", 88)]

for s in students:
    print(f"{s.name}: {s.score} → {s.grade()}")`);
</script>

### Guardalo: Progetto vs Veri Cani

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nell'ispettore sotto, il programma definisce `class Dog` e poi chiama
    `Dog(...)` due volte. Prevedi: quando `rex.bark()` gira, **come sa Python
    quale nome di cane stampare — quello di Rex o quello di Bella?** Esegui passo passo e guarda
    la freccia arancione!

<iframe src="../../sims/object-instance-inspector/main.html" height="572" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Object Instance Inspector](../../sims/object-instance-inspector/index.md){ .md-button }

La risposta: `self` è sempre l'oggetto **a sinistra del punto**. La classe è solo un progetto a tratteggio — le carte solide sono gli oggetti reali, ognuno con le sue caselle di attributo. L'ultimo passo mostra un altro segreto: `rex.species` non è affatto sulla carta di rex, quindi Python guarda in alto, verso il progetto, dove vive la variabile di classe condivisa.

## `__str__()` — Rappresentazione in Stringa

`__str__()` definisce cosa mostrano `print(obj)` e `str(obj)`.
Senza di esso, `print(fido)` mostra qualcosa come `<__main__.Dog object at 0x...>` — non molto utile.

```python
class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def __str__(self):
        return f"Dog({self.name}, {self.breed})"

fido = Dog("Fido", "Labrador")
print(fido)   # Dog(Fido, Labrador)
```

`__repr__()` è simile ma pensato per gli sviluppatori — dovrebbe idealmente mostrare codice che potresti incollare per ricreare l'oggetto.

## Variabili di Classe vs Variabili di Istanza

Una **variabile di istanza** (definita con `self.`) appartiene a un oggetto specifico.
Una **variabile di classe** (definita direttamente nel corpo della classe, non dentro nessun metodo) è condivisa da tutte le istanze.

```python
class Counter:
    count = 0   # variabile di classe — condivisa da tutte le istanze

    def __init__(self):
        Counter.count += 1   # incrementa il contatore condiviso

a = Counter()
b = Counter()
c = Counter()
print(Counter.count)   # 3 — sono state create tre istanze
```

## Stringhe e Liste come Esempi di OOP

Hai usato la OOP fin dall'inizio — i metodi delle stringhe e delle liste sono solo metodi su oggetti:

```python
name = "monty"
name.upper()       # chiama il metodo upper() sull'oggetto stringa

items = [3, 1, 2]
items.sort()       # chiama il metodo sort() sull'oggetto lista
```

## Eredità

L'**eredità** (inheritance) ti permette di creare una nuova classe (**sottoclasse**) che eredita tutti gli attributi e i metodi di una classe esistente (**classe genitore**).

Usa `class Sottoclasse(ClasseGenitore):` per dichiarare l'eredità.
La funzione `super()` chiama l'`__init__()` della classe genitore così non devi ripetere tutto il suo codice di impostazione.

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
initCmLab('-3', `class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} dice {self.sound}!")

    def __str__(self):
        return f"Animal({self.name})"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Bau")   # chiama l'__init__ del genitore

    def fetch(self):
        print(f"{self.name} va a prendere la palla!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        print(f"{self.name} fa le fusa, contento.")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()     # ereditato da Animal
dog.fetch()     # definito in Dog

cat.speak()     # ereditato da Animal
cat.purr()      # definito in Cat

print(dog)      # usa il __str__ di Animal`);
</script>

## Sovrascrittura dei Metodi (Method Overriding)

Una sottoclasse può **sovrascrivere** (override) un metodo del genitore definendo un metodo con lo stesso nome.
La versione della sottoclasse gira invece di quella del genitore.

```python
class Dog(Animal):
    def speak(self):
        print(f"{self.name} abbaia forte!")   # sovrascrive Animal.speak
```

### Guardalo: Guarda Salire la Ricerca del Metodo

Quando chiami `d.eat()` su un Dog, Python cerca silenziosamente: prima in `class Dog`, e se il metodo non c'è, sale a `class Animal`. Prima di cliccare qualcosa nell'esploratore sotto, prevedi: **quale delle tre chiamate — `d.fetch()`, `d.speak()`, `d.eat()` — ha bisogno di salire fino ad Animal?**

<iframe src="../../sims/inheritance-explorer/main.html" height="507" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Inheritance Explorer](../../sims/inheritance-explorer/index.md){ .md-button }

Clicca tutte e tre le chiamate e guarda le evidenziazioni salire. Nota cosa succede dopo `d.speak()`: il proprio `speak()` di Animal è segnato come **shadowed** (oscurato) — ha vinto la versione di Dog, esattamente come l'esempio di override sopra. L'ultimo pulsante mostra `super()`, il modo gentile per una classe figlia di eseguire comunque la versione del genitore.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Metodo"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La classe `Rectangle` sotto ha gli attributi `width` e `height` ma le mancano due metodi.
    Aggiungi `area()` (restituisce width × height) e `perimeter()` (restituisce 2 × (width + height)).

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
initCmLab('-4', `class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

    # Aggiungi qui area():

    # Aggiungi qui perimeter():

r = Rectangle(4, 7)
print(r)
print("Area:", r.area())
print("Perimetro:", r.perimeter())`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Aggiungi un metodo `birthday()` alla classe `Dog` che incrementa `self.age` di 1. Chiamalo due volte e stampa l'età.
   **Saprai che ha funzionato quando** `fido.age` aumenta di 2 dopo due chiamate a birthday.

2. Crea una sottoclasse `Square(Rectangle)` dove `__init__` prende solo `side` e chiama `super().__init__(side, side)`.
   **Saprai che ha funzionato quando** `Square(5).area()` restituisce `25`.

3. Aggiungi un `__repr__()` a `Dog` che restituisce `f"Dog(name={self.name!r}, age={self.age})"`.
   **Saprai che ha funzionato quando** usare `repr(fido)` mostra una stringa ricostruibile.

4. Crea una classe `BankAccount` con `balance = 0`, un metodo `deposit(n)`, e un metodo `withdraw(n)` che si rifiuta se il saldo diventerebbe negativo.
   **Saprai che ha funzionato quando** prelevare più del saldo stampa un errore e il saldo resta invariato.

5. Crea una lista di tre oggetti `Student` e ordinali per punteggio usando `sorted(students, key=lambda s: s.score)`.
   **Saprai che ha funzionato quando** gli studenti appaiono in ordine crescente di punteggio.

!!! mascot-celebration "Esperto di OOP!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato a progettare i tuoi propri oggetti con classi, eredità, e metodi speciali!
    La OOP è la base di quasi tutto il codice Python professionale — dai framework web ai motori di gioco.
    Stai costruendo vere competenze software. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
