# Quiz: Programmazione Orientata agli Oggetti

Verifica la tua comprensione delle classi, delle istanze, dei costruttori, dell'eredità, e del modello OOP di Python con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è una classe in Python?

<div class="upper-alpha" markdown>
1. Una funzione che restituisce una lista di oggetti
2. Un progetto per creare oggetti, che definisce i loro attributi e metodi
3. Un tipo di variabile che memorizza valori multipli
4. Un ciclo speciale usato per elaborare gruppi di elementi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una classe è un progetto o modello per creare oggetti. Definisce quali dati (attributi) e comportamenti (metodi) avrà ogni istanza di quella classe. Definisci una classe con la parola chiave `class`, e poi crei singoli oggetti (istanze) chiamando la classe come una funzione.

    **Concept Tested:** class Keyword

---

#### 2. Qual è lo scopo di `__init__()` in una classe?

<div class="upper-alpha" markdown>
1. Stampare il contenuto dell'oggetto quando viene creato
2. Importare la classe da un altro file
3. Inizializzare gli attributi di un'istanza quando l'oggetto viene creato per la prima volta
4. Eliminare l'oggetto dalla memoria quando non è più necessario
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `__init__()` è il costruttore — un metodo speciale che Python chiama automaticamente ogni volta che crei una nuova istanza. Imposta lo stato iniziale dell'oggetto assegnando valori agli attributi con `self.nome_attributo = valore`. Senza `__init__()`, l'oggetto non avrebbe attributi finché non li imposti manualmente.

    **Concept Tested:** __init__() Constructor

---

#### 3. A cosa si riferisce `self` dentro un metodo di classe?

<div class="upper-alpha" markdown>
1. Alla definizione della classe stessa
2. All'istanza più recentemente creata della classe
3. All'istanza specifica su cui viene chiamato il metodo
4. A una parola chiave obbligatoria che significa "questo è un metodo, non una funzione"
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `self` è un riferimento all'istanza particolare su cui viene chiamato il metodo. Quando scrivi `fido.bark()`, Python passa `fido` come argomento `self` automaticamente. Dentro `bark()`, `self.name` si riferisce a `fido.name`. Ogni metodo in una classe prende `self` come primo parametro, anche se Python lo riempie automaticamente — non lo passi mai tu stesso.

    **Concept Tested:** self

---

#### 4. Come crei un'istanza di una classe chiamata `Dog`?

<div class="upper-alpha" markdown>
1. `Dog.create("Fido", "Labrador")`
2. `new Dog("Fido", "Labrador")`
3. `Dog = instance("Fido", "Labrador")`
4. `fido = Dog("Fido", "Labrador")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Crei un'istanza chiamando la classe come una funzione con gli argomenti che `__init__()` si aspetta (dopo `self`). Python chiama automaticamente `__init__()` e restituisce una nuova istanza. A differenza di altri linguaggi, Python non usa la parola chiave `new` — chiami semplicemente il nome della classe con le parentesi.

    **Concept Tested:** Creating Instances

---

#### 5. Per cosa si usa la notazione punto con gli oggetti?

<div class="upper-alpha" markdown>
1. Per sommare due oggetti insieme con l'operatore `+`
2. Per accedere agli attributi di un oggetto e chiamare i suoi metodi
3. Per importare un metodo specifico da una classe
4. Per controllare se un oggetto è uguale a un altro
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La notazione punto (`oggetto.attributo` oppure `oggetto.metodo()`) è il modo in cui accedi ai dati memorizzati dentro un oggetto o chiami i comportamenti definiti su di esso. Per esempio, `fido.name` legge l'attributo `name`, e `fido.bark()` chiama il metodo `bark`. Hai usato la notazione punto fin dall'inizio con le stringhe (`"hello".upper()`), le liste (`items.append(x)`), e la tartaruga (`t.forward(100)`).

    **Concept Tested:** Dot Notation

---

#### 6. Cosa controlla `__str__()` in una classe?

<div class="upper-alpha" markdown>
1. Come l'oggetto viene memorizzato in memoria
2. Cosa Python mostra quando usi `print(obj)` o `str(obj)` sull'oggetto
3. Come l'oggetto si confronta con altri oggetti con `==`
4. Quante istanze della classe possono essere create
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `__str__()` definisce la rappresentazione in stringa leggibile dall'uomo di un oggetto. Senza di esso, `print(fido)` mostra qualcosa di poco utile come `<__main__.Dog object at 0x10a3b2c>`. Con `__str__()` che restituisce `f"Dog({self.name}, {self.breed})"`, `print(fido)` mostra invece `Dog(Fido, Labrador)`.

    **Concept Tested:** __str__() Method

---

#### 7. Qual è la differenza tra una variabile di classe e una variabile di istanza?

<div class="upper-alpha" markdown>
1. Le variabili di classe sono più veloci da accedere; le variabili di istanza sono più lente
2. Una variabile di classe è condivisa da tutte le istanze; una variabile di istanza appartiene a un oggetto specifico
3. Le variabili di classe sono definite con `self`; le variabili di istanza sono definite senza `self`
4. Le variabili di classe possono contenere solo numeri; le variabili di istanza possono contenere qualsiasi tipo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una variabile di istanza (`self.name = value`) appartiene a un oggetto specifico. Cambiarla su un'istanza non influenza nessun'altra. Una variabile di classe è definita nel corpo della classe (non dentro un metodo) ed è condivisa da tutte le istanze. Un uso comune delle variabili di classe è contare quante istanze sono state create.

    **Concept Tested:** Class vs Instance Variables

---

#### 8. Come si dichiara l'eredità in Python?

<div class="upper-alpha" markdown>
1. `class Puppy extends Dog:`
2. `class Puppy inherits Dog:`
3. `class Puppy(Dog):`
4. `class Puppy from Dog:`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Metti il nome della classe genitore tra parentesi dopo il nome della sottoclasse: `class Puppy(Dog):`. La sottoclasse eredita automaticamente tutti gli attributi e i metodi dal genitore. Solo Python usa la sintassi `(ClasseGenitore)` per l'eredità; altri linguaggi usano `extends` o parole chiave simili.

    **Concept Tested:** Inheritance

---

#### 9. Cosa fa `super()` dentro il costruttore di una sottoclasse?

<div class="upper-alpha" markdown>
1. Crea un'istanza aggiuntiva della classe genitore
2. Elimina la classe genitore così che resti solo la sottoclasse
3. Chiama il metodo `__init__()` della classe genitore per impostare gli attributi ereditati
4. Restituisce un riferimento alla classe in cima alla catena di eredità
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `super().__init__(...)` chiama il costruttore della classe genitore, così puoi eseguire il suo codice di impostazione senza riscriverlo. Questo è importante perché la sottoclasse ha bisogno anche degli attributi del genitore. Per esempio, se `Animal.__init__` imposta `self.name` e `self.sound`, chiamare `super().__init__(name, sound)` in una sottoclasse gestisce tutto questo automaticamente.

    **Concept Tested:** super()

---

#### 10. Quale convenzione di denominazione usa Python per i nomi delle classi?

<div class="upper-alpha" markdown>
1. `snake_case` (tutto minuscolo con underscore)
2. `ALL_CAPS` (tutto maiuscolo con underscore)
3. `camelCase` (prima parola minuscola, resto con maiuscola)
4. `CamelCase` (ogni parola con maiuscola, nessun underscore)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. I nomi delle classi Python usano il CamelCase (chiamato anche PascalCase) — ogni parola inizia con una lettera maiuscola e non ci sono underscore: `Dog`, `Student`, `BankAccount`, `LinkedList`. Questa è una convenzione della PEP 8 (la guida di stile di Python). Al contrario, i nomi di variabili e funzioni usano `snake_case`, e le costanti usano `ALL_CAPS`.

    **Concept Tested:** CamelCase Naming Convention

---
