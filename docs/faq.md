# Domande frequenti su Python

Benvenuto nelle Domande frequenti di *Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty*.
Le domande sono organizzate dagli argomenti introduttivi fino ai concetti avanzati,
così puoi saltare direttamente a quello che ti serve di più.

---

## Domande per iniziare

### Di che cosa parla questo corso?

*Introduzione a Python — Dalla programmazione visuale a blocchi al codice con Monty* è un corso
basato su progetti che accompagna gli studenti che hanno già imparato Scratch (o un altro
linguaggio a blocchi) e insegna loro a scrivere veri programmi in Python. Il corso parte dalla
grafica turtle, che è visiva e ti fa vedere subito i risultati, e procede passo dopo passo verso
variabili, cicli, funzioni, strutture dati e infine il machine learning. Lungo il percorso
**Monty**, il pitone mascotte, compare in ogni lezione per darti consigli, collegare le idee
a quelle di Scratch e festeggiare i tuoi progressi.

Vedi [course-description.md](course-description.md) per la panoramica completa.

### A chi è rivolto questo corso?

Questo corso è pensato per studenti della scuola primaria e secondaria di primo grado, di circa
**10–13 anni**, che hanno completato almeno un semestre di programmazione a blocchi (Scratch,
Snap! o MIT App Inventor) e sono pronti a passare al codice scritto. Non serve alcuna esperienza
con Python. Bastano una capacità di lettura di base e il saper fare addizioni e sottrazioni.

### Che cosa dovrei sapere già prima di iniziare?

Dovresti avere familiarità con l'idea di **sequenza** (eseguire dei passi in ordine), di
**ciclo** (ripetere delle azioni), di **condizione** (se qualcosa è vero, fai questo) e di
**variabile** (memorizzare un valore con un nome). Se hai usato queste idee in Scratch, sei
pronto. Non servono conoscenze di Python, né matematica oltre l'aritmetica, né installazioni.

### Come si esegue il codice Python in questo manuale?

Ogni lezione dei Capitoli 1–18 contiene uno o più **laboratori Skulpt**: finestre di codice
interattive integrate direttamente nella pagina. Clicchi **Run** e Python viene eseguito subito
nel tuo browser. Niente login, niente account, niente installazioni. Nei Capitoli 19–38 alcuni
esempi usano Python installato sul tuo computer, ma i laboratori Skulpt continuano a comparire
in tutto il manuale.

### Che cos'è Skulpt e perché i Capitoli 1–18 lo usano?

**Skulpt** è una versione di Python che funziona interamente dentro il browser, grazie a
JavaScript. Dato che gira nel browser, gli studenti non devono installare nulla né aprire una
nuova scheda: la finestra del codice è proprio lì nella pagina. I primi 18 capitoli si
concentrano su concetti che Skulpt gestisce bene: print, variabili, cicli, funzioni, liste e
grafica turtle. I capitoli successivi introducono librerie (NumPy, matplotlib, Pillow, Keras)
che richiedono un'installazione completa di Python.

Vedi [chapters/01-welcome-to-python/index.md](chapters/01-welcome-to-python/index.md) per
un'introduzione a Skulpt.

### Chi è Monty e che cosa fa?

**Monty** è il simpatico pitone mascotte che vive dentro questo manuale. Monty ha esattamente
sette compiti: darti il benvenuto all'inizio di ogni lezione, aiutarti a prevedere che cosa
farà il codice prima di eseguirlo, darti i consigli che usano i programmatori esperti,
collegare le idee di Python ai loro equivalenti in Scratch, avvisarti degli errori più comuni,
incoraggiarti quando un concetto è difficile e festeggiare con te alla fine di ogni lezione.
Monty compare solo quando sta facendo una di queste sette cose, mai a caso.

### Devo installare Python per usare questo manuale?

**No**, non per i Capitoli 1–18. Ti basta un browser moderno. I laboratori Skulpt integrati
eseguono Python direttamente nella pagina. Se vuoi andare oltre il manuale, o affrontare i
capitoli più avanzati che usano NumPy, matplotlib o Keras, puoi installare Python da
[python.org](https://www.python.org) oppure usare un ambiente cloud come Google Colab.

Vedi [chapters/28-python-dev-tools/index.md](chapters/28-python-dev-tools/index.md) per le
istruzioni di installazione.

### In che cosa Python è diverso da Scratch?

In Scratch trascini dei blocchi colorati e li incastri tra loro. In Python **scrivi** le
istruzioni come testo. Le idee di base (sequenze, cicli, condizioni, variabili) sono le stesse,
ma scrivere il codice ti dà molta più flessibilità: puoi scrivere cicli che si ripetono milioni
di volte, lavorare con grandi file di dati, creare grafica e costruire modelli di machine
learning. Ogni volta che compare un nuovo concetto di Python, Monty ti mostra l'equivalente in
Scratch, così puoi costruire su quello che sai già.

Vedi [chapters/01-welcome-to-python/index.md](chapters/01-welcome-to-python/index.md) per il
confronto completo tra Scratch e Python.

### Che cosa sarò in grado di costruire alla fine del corso?

Alla fine di questo corso di 38 capitoli sarai in grado di costruire:

- Programmi colorati con la grafica turtle e frattali animati
- Giochi interattivi che usano i clic del mouse e gli eventi della tastiera
- Programmi di elaborazione dati che leggono e scrivono file di testo
- Moduli personalizzati da riutilizzare in più progetti
- Programmi che risolvono labirinti usando gli algoritmi sui grafi
- Dashboard di visualizzazione dei dati con matplotlib
- Una rete neurale che riconosce le cifre scritte a mano del dataset MNIST

### Quanto tempo serve per completare il corso?

Il corso è pensato per circa **un anno scolastico** in un club di programmazione o in un corso
opzionale che si incontra due o tre volte a settimana, oppure per studenti motivati che
studiano da soli per 30–45 minuti a sessione. I 38 capitoli sono organizzati in modo che i
Capitoli 1–18 formino un percorso **base** completo e i Capitoli 19–38 un'estensione di livello
**intermedio-avanzato**.

### Esiste una guida per gli insegnanti?

Sì. Il corso include una **guida dettagliata per gli insegnanti** con indicazioni sui tempi,
mappe dei concetti prerequisiti, spunti di discussione, idee sbagliate più comuni, attività di
approfondimento, rubriche di valutazione e l'allineamento agli standard CSTA K-12 per
l'informatica. Vedi [course-description.md](course-description.md) per una descrizione di tutti
i materiali inclusi.

### Come sono organizzati i capitoli?

I 38 capitoli seguono un grafo di apprendimento di 450 concetti messi in sequenza con cura, in
cui ogni concetto si basa su quelli precedenti. I primi cinque capitoli presentano l'ambiente
Python e la grafica turtle, e stabiliscono il riscontro visivo e immediato come strumento di
apprendimento. I Capitoli 6–18 trattano il nucleo del linguaggio: matematica, cicli, stringhe,
decisioni, funzioni, colori, input e liste. I Capitoli 19–30 introducono collezioni avanzate,
gestione degli errori, ricorsione, OOP, input/output su file e algoritmi. I Capitoli 31–38
trattano visualizzazione dei dati, NumPy, elaborazione delle immagini e machine learning.

---

## Domande sui concetti fondamentali

### Che cos'è l'interprete Python?

L'**interprete Python** è il programma che legge il tuo codice Python ed esegue le sue
istruzioni, una riga alla volta, dall'alto verso il basso. Immaginalo come un lettore
velocissimo che traduce le tue istruzioni, scritte in un linguaggio simile all'inglese, in azioni
che il computer può compiere. Quando clicchi **Run** in un laboratorio Skulpt, è l'interprete
Skulpt (una versione di Python costruita per i browser) a fare esattamente questo lavoro. Quando
esegui un file `.py` da un terminale, l'interprete standard CPython fa la stessa cosa sul tuo
computer.

Vedi [chapters/01-welcome-to-python/index.md](chapters/01-welcome-to-python/index.md).

### Che cos'è l'indentazione e perché è così importante per Python?

**Indentare** significa mettere degli spazi (o un tab) all'inizio di una riga per indicare che
appartiene a un blocco. In Python l'indentazione non è solo una questione di stile: fa parte
della sintassi del linguaggio. Il corpo di un ciclo `for`, un blocco `if` e il corpo di una
funzione sono tutti riconosciuti dalla loro indentazione. La maggior parte dei programmatori
Python usa **4 spazi** per livello.

Esempio: il `print` qui sotto è dentro il ciclo perché è indentato:

```python
for i in range(3):
    print(i)   # indented — runs 3 times
print("done")  # not indented — runs once after the loop
```

Se dimentichi di indentare, Python solleva un `IndentationError`.

Vedi [chapters/02-python-code-structure/index.md](chapters/02-python-code-structure/index.md).

### Che cos'è una variabile?

Una **variabile** è un contenitore con un nome che conserva un valore. La crei con l'operatore di
assegnazione `=`:

```python
score = 10
name = "Monty"
```

Dopo questa riga, `score` si riferisce al numero `10` e `name` al testo `"Monty"`. Puoi usare il
nome della variabile ovunque useresti il valore, e puoi aggiornarla in qualsiasi momento
assegnandole un nuovo valore. Anche in Scratch si chiamavano *variabili*: stessa idea, scritta in
modo diverso.

Vedi [chapters/03-variables-and-numbers/index.md](chapters/03-variables-and-numbers/index.md).

### Quali sono i sei tipi di dati fondamentali di Python?

I sei tipi di dati fondamentali di Python sono:

| Tipo | Esempio | Che cosa contiene |
|------|---------|--------------|
| `int` | `42` | Numeri interi |
| `float` | `3.14` | Numeri decimali |
| `str` | `"hello"` | Testo |
| `bool` | `True` / `False` | Vero o falso |
| `list` | `[1, 2, 3]` | Collezione ordinata e modificabile |
| `dict` | `{"a": 1}` | Coppie chiave-valore |

Puoi sempre controllare il tipo di un valore con `type(value)`.

### Che cos'è un ciclo for?

Un **ciclo `for`** ripete un blocco di codice una volta per ogni elemento di una sequenza. La
forma più comune usa `range()` per contare:

```python
for i in range(4):
    print(i)   # prints 0, 1, 2, 3
```

Puoi anche scorrere una lista, una stringa o qualsiasi altra sequenza. I cicli for sono
l'equivalente in Python del blocco *ripeti N volte* di Scratch. Si usano di continuo per disegnare
forme, elaborare liste e costruire schemi ad accumulatore.

Vedi [chapters/07-for-loops-and-shapes/index.md](chapters/07-for-loops-and-shapes/index.md).

### Che cos'è un ciclo while?

Un **ciclo `while`** ripete un blocco di codice finché una condizione resta `True`. A differenza
di un ciclo `for` (che conta un numero fisso di ripetizioni), un ciclo `while` viene eseguito un
numero di volte che non si conosce in anticipo: dipende da ciò che succede dentro il ciclo.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

I cicli while sono perfetti per le animazioni (continua finché l'utente non clicca stop), per
controllare l'input (continua a chiedere finché l'utente non inserisce un numero valido) e per i
cicli di gioco (continua a giocare finché qualcuno non vince).

Vedi [chapters/10-while-loops-and-animation/index.md](chapters/10-while-loops-and-animation/index.md).

### Come funziona un'istruzione if/elif/else?

Un'**istruzione `if`** esegue un blocco di codice solo quando una condizione è `True`. Aggiungi
**`elif`** (abbreviazione di "else if", altrimenti se) per controllare altre condizioni in ordine.
Aggiungi **`else`** per gestire tutto ciò che non corrisponde:

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep practicing!")
```

Python controlla ogni condizione dall'alto verso il basso ed esegue solo il primo blocco la cui
condizione è `True`. È esattamente come funziona il blocco *se-altrimenti* di Scratch, solo
scritto come testo.

Vedi [chapters/09-decisions-if-else/index.md](chapters/09-decisions-if-else/index.md).

### Che cos'è una funzione e perché dovrei usarla?

Una **funzione** è un blocco di codice riutilizzabile a cui dai un nome e che puoi chiamare
ogni volta che ti serve. Definisci una funzione con `def`:

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Monty")   # prints: Hello, Monty!
greet("Alex")    # prints: Hello, Alex!
```

Le funzioni ti permettono di non scrivere due volte lo stesso codice (il principio DRY),
rendono i programmi più facili da leggere e dividono i problemi grandi in pezzi più piccoli e
gestibili. In Scratch, i blocchi personalizzati funzionano allo stesso modo.

Vedi [chapters/11-functions-parameters-scope/index.md](chapters/11-functions-parameters-scope/index.md).

### Che cos'è una lista?

Una **lista** è una collezione di valori ordinata e modificabile. La crei con le parentesi
quadre:

```python
colors = ["red", "green", "blue"]
print(colors[0])   # red — indexing starts at 0
colors.append("yellow")
```

Le liste sono il cavallo di battaglia per memorizzare dati in Python. Puoi aggiungere elementi
(`append`), toglierli (`remove`, `pop`), ordinarli, scorrerli con un ciclo ed estrarne delle
porzioni (slicing). Ogni lista mantiene gli elementi nell'ordine in cui li hai inseriti.

Vedi [chapters/15-lists-basics/index.md](chapters/15-lists-basics/index.md).

### Che cos'è un dizionario?

Un **dizionario** memorizza i dati come **coppie chiave-valore**. Invece di usare un indice
numerico, cerchi i valori tramite una chiave descrittiva:

```python
grades = {"Alice": 95, "Bob": 88, "Carol": 92}
print(grades["Alice"])  # 95
grades["Dan"] = 79      # add a new entry
```

I dizionari sono perfetti per memorizzare dati con un nome: un registro dei voti, un contatore
della frequenza delle parole, delle impostazioni di configurazione, o qualsiasi situazione in cui
vuoi cercare qualcosa per nome invece che per posizione.

Vedi [chapters/21-dictionaries/index.md](chapters/21-dictionaries/index.md).

### Che cos'è la grafica turtle?

La **grafica turtle** è un modo per disegnare forme controllando una piccola freccia (la
"turtle", cioè la tartaruga) che si muove su un canvas. Le dai comandi come `forward(100)`,
`left(90)` e `pencolor("red")` per guidarne il movimento e l'aspetto. Dato che vedi subito il
risultato di ogni comando, la grafica turtle è un ottimo modo per imparare cicli, funzioni e
coordinate. È il principale strumento di disegno nei Capitoli 5–18 di questo corso.

Vedi [chapters/05-drawing-with-turtle/index.md](chapters/05-drawing-with-turtle/index.md).

### Che cos'è la ricorsione?

La **ricorsione** si ha quando una funzione chiama se stessa. Ogni chiamata ricorsiva lavora su
una versione più piccola del problema, finché non raggiunge il **caso base**: una condizione che
interrompe la catena di chiamate.

```python
def countdown(n):
    if n <= 0:          # base case
        print("Go!")
        return
    print(n)
    countdown(n - 1)    # recursive call
```

La ricorsione è particolarmente potente per i problemi che hanno una struttura naturalmente
auto-simile, come gli alberi frattali, in cui ogni ramo è una versione più piccola dell'intero
albero.

Vedi [chapters/24-recursion-and-fractals/index.md](chapters/24-recursion-and-fractals/index.md).

### Che cos'è un modulo?

Un **modulo** è un file Python (o un insieme di file) che contiene funzioni, variabili e classi
riutilizzabili. Porti un modulo nel tuo programma con `import`:

```python
import math
print(math.sqrt(25))   # 5.0

import random
print(random.randint(1, 10))   # a random number 1-10
```

Python include una grande **libreria standard** di moduli che coprono matematica, gestione dei
file, date, espressioni regolari, strutture dati e molto altro. Puoi anche creare i tuoi moduli e
importarli in altri programmi.

Vedi [chapters/17-modules-and-random/index.md](chapters/17-modules-and-random/index.md).

### Che cos'è una classe in Python?

Una **classe** è un progetto per creare oggetti. Ogni oggetto costruito a partire dalla classe ha
i propri **attributi** (dati) e **metodi** (azioni). Definisci una classe con `class` e ne
prepari gli attributi in un metodo speciale chiamato `__init__`:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " says: Woof!")

fido = Dog("Fido", "Labrador")
fido.bark()   # Fido says: Woof!
```

Hai già usato delle classi: `turtle.Turtle()` e `turtle.Screen()` sono entrambe classi fornite
dal modulo turtle.

Vedi [chapters/25-object-oriented-programming/index.md](chapters/25-object-oriented-programming/index.md).

### Che cos'è una stringa?

Una **stringa** è una sequenza di caratteri di testo racchiusa tra virgolette. Funzionano sia
gli apici singoli `'hello'` sia le virgolette doppie `"hello"`. Le stringhe sono **immutabili**:
non puoi cambiarne i singoli caratteri, ma puoi creare nuove stringhe combinando o trasformando
quelle esistenti:

```python
greeting = "Hello, " + "world!"   # concatenation
upper = greeting.upper()           # "HELLO, WORLD!"
words = greeting.split(", ")      # ["Hello", "world!"]
```

Le stringhe hanno decine di metodi built-in per cercare, dividere, sostituire e formattare il
testo.

Vedi [chapters/08-working-with-strings/index.md](chapters/08-working-with-strings/index.md).

### Qual è la differenza tra una lista, una tupla e un insieme?

Sono tutte e tre collezioni di Python, ma differiscono in modi importanti:

| Collezione | Ordinata? | Modificabile? | Duplicati? |
|------------|----------|-------------|-------------|
| `list` | Sì | Sì (mutabile) | Ammessi |
| `tuple` | Sì | No (immutabile) | Ammessi |
| `set` | No | Sì | Non ammessi |

Usa una **lista** quando l'ordine conta e devi aggiungere o togliere elementi. Usa una **tupla**
per una collezione fissa di valori (come le coordinate `(x, y)`). Usa un **insieme** quando ti
interessa solo sapere se un elemento è presente e ogni elemento deve essere unico.

Vedi [chapters/20-tuples-and-sets/index.md](chapters/20-tuples-and-sets/index.md).

### Che cos'è lo scope in Python?

Lo **scope** (ambito di visibilità) stabilisce in quali punti di un programma una variabile può
essere vista. Una variabile definita dentro una funzione ha **scope locale**: esiste solo dentro
quella funzione. Una variabile definita fuori da tutte le funzioni ha **scope globale**: può
essere vista ovunque. Questo significa che due funzioni possono avere ciascuna la propria
variabile chiamata `count` senza interferire tra loro.

```python
def example():
    x = 10      # local — only visible inside example()

y = 20          # global — visible everywhere
```

Capire lo scope evita un tipo comune di bug in cui sovrascrivi per sbaglio una variabile di
un'altra parte del programma.

Vedi [chapters/11-functions-parameters-scope/index.md](chapters/11-functions-parameters-scope/index.md).

### Che cosa sono BFS e DFS?

**BFS (Breadth-First Search, ricerca in ampiezza)** e **DFS (Depth-First Search, ricerca in
profondità)** sono algoritmi per visitare tutti i nodi di un grafo o di un albero.

- **BFS** usa una **coda** (il primo che entra è il primo che esce). Esplora tutti i vicini alla
  distanza attuale prima di andare più in profondità. BFS **garantisce il percorso più breve** in
  un grafo non pesato.
- **DFS** usa una **pila** (l'ultimo che entra è il primo che esce), oppure la ricorsione. Si
  spinge il più in profondità possibile lungo un percorso prima di tornare indietro.

BFS è la scelta giusta per trovare la strada più breve in un labirinto. DFS è spesso più
semplice da implementare in modo ricorsivo e funziona bene per i problemi in cui bisogna
esplorare tutte le possibilità.

Vedi [chapters/30-algorithms-data-structures/index.md](chapters/30-algorithms-data-structures/index.md).

### Che cos'è la programmazione orientata agli oggetti?

La **programmazione orientata agli oggetti (OOP)** è uno stile di programmazione che organizza il
codice attorno agli **oggetti**: entità che raggruppano dati (attributi) e comportamenti
(metodi). Python è un linguaggio orientato agli oggetti: stringhe, liste, dizionari e la grafica
turtle sono tutti oggetti. Quando chiami `my_list.append(5)`, stai chiamando il metodo `append`
su un oggetto lista. La OOP diventa particolarmente utile per rappresentare cose del mondo
reale: una classe `Player` in un gioco, una classe `Quiz` per un'app di quiz, una classe
`Turtle` per il tuo strumento di disegno.

Vedi [chapters/25-object-oriented-programming/index.md](chapters/25-object-oriented-programming/index.md).

### Che cos'è la struttura dati grafo?

In informatica, un **grafo** è un insieme di **nodi** (chiamati anche vertici) collegati da
**archi**. I grafi rappresentano delle reti: città collegate da strade, pagine web collegate da
link, o stanze di un labirinto collegate da corridoi. In Python i grafi si rappresentano con le
**liste di adiacenza**: dizionari in cui ogni chiave è un nodo e il suo valore è la lista dei
nodi vicini.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
```

BFS e DFS sono i due algoritmi standard per esplorare un grafo.

Vedi [chapters/30-algorithms-data-structures/index.md](chapters/30-algorithms-data-structures/index.md).

### Che cos'è il modulo random?

Il **modulo `random`** fornisce funzioni per generare numeri casuali e fare scelte casuali.
Quelle che userai più spesso in questo corso sono:

- `random.randint(a, b)` — un numero intero casuale tra `a` e `b` (inclusi)
- `random.choice(seq)` — sceglie un elemento a caso da una lista
- `random.random()` — un numero decimale (float) casuale tra 0.0 e 1.0
- `random.shuffle(lst)` — mescola una lista modificandola direttamente

I numeri casuali compaiono in moltissimi progetti di grafica turtle: colori casuali, posizioni
di partenza casuali, gare tra turtle e generatori di cieli stellati.

Vedi [chapters/17-modules-and-random/index.md](chapters/17-modules-and-random/index.md).

### Che cos'è il machine learning?

Il **machine learning** (apprendimento automatico) è un ramo dell'intelligenza artificiale in
cui un programma impara degli schemi dai dati invece di seguire regole scritte a mano. Tu fornisci
degli esempi etichettati e il programma regola dei numeri interni (chiamati **pesi**) finché
non riesce a classificare correttamente nuovi esempi che non ha mai visto. In questo corso usi
la libreria **Keras** per costruire una piccola rete neurale che impara a riconoscere le cifre
scritte a mano del dataset MNIST — 60.000 immagini di addestramento con le cifre da 0 a 9.

Vedi [chapters/37-machine-learning-foundations/index.md](chapters/37-machine-learning-foundations/index.md).

### Che cos'è una list comprehension?

Una **list comprehension** è un modo compatto per costruire una nuova lista trasformando o
filtrando un'altra sequenza. Unisce un ciclo `for` e una condizione `if` facoltativa in
un'unica riga:

```python
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Le list comprehension sono più concise che costruire una lista con `append()` dentro un normale
ciclo `for`, e i programmatori Python esperti le usano di continuo.

Vedi [chapters/22-advanced-collections/index.md](chapters/22-advanced-collections/index.md).

---

## Domande sui dettagli tecnici

### Qual è la differenza tra Python 2 e Python 3?

Python 3 (uscito nel 2008) ha introdotto diversi miglioramenti non compatibili con Python 2.
Per chi inizia, la differenza pratica più grande è che `print` è passato da istruzione
(`print "hello"`) a funzione (`print("hello")`). È cambiata anche la divisione: in Python 2
`5 / 2` restituiva `2` (divisione intera); in Python 3 restituisce `2.5`.
**Questo corso usa Python 3.** Il supporto a Python 2 è terminato a gennaio 2020 e non va
usato per nuovi progetti.

### Che cosa fa la funzione print()?

`print()` mostra un risultato sullo schermo. Le passi uno o più valori separati da virgole e
Python li stampa su un'unica riga separati da spazi, andando poi a capo:

```python
print("Hello", "world")   # Hello world
print(42)                  # 42
print(1 + 1)               # 2
```

`print()` è lo strumento di debug più importante in Python: quando qualcosa va storto,
aggiungere delle istruzioni `print()` che mostrano i valori delle variabili è spesso il modo più
rapido per trovare il bug.

### Come funzionano le f-string?

Una **f-string** (stringa letterale formattata) ti permette di inserire i valori delle variabili
direttamente dentro una stringa: basta mettere una `f` prima delle virgolette di apertura e
racchiudere i nomi delle variabili tra `{}`:

```python
name = "Monty"
score = 95
message = f"Great job, {name}! You scored {score} points."
print(message)
# Great job, Monty! You scored 95 points.
```

Qualsiasi espressione Python tra le parentesi graffe viene calcolata e inserita nella stringa.
Nel Python moderno, le f-string sono il modo preferito per costruire stringhe che contengono
valori di variabili.

Vedi [chapters/14-string-methods-formatting/index.md](chapters/14-string-methods-formatting/index.md).

### Che cosa fa la funzione range()?

`range(n)` genera una sequenza di numeri interi da `0` fino a `n` (escluso). Puoi anche
indicare un inizio, una fine e un passo:

```python
range(5)         # 0, 1, 2, 3, 4
range(2, 8)      # 2, 3, 4, 5, 6, 7
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(5, 0, -1)  # 5, 4, 3, 2, 1
```

`range()` si usa in quasi tutti i cicli `for` che contano. Non crea una lista in memoria:
genera i valori uno alla volta, ed è per questo che resta efficiente anche con intervalli
molto grandi.

### Che cos'è l'operatore modulo?

L'**operatore modulo `%`** restituisce il resto di una divisione:

```python
10 % 3   # 1  (10 divided by 3 = 3 remainder 1)
8 % 2    # 0  (8 divided by 2 = 4 remainder 0)
7 % 5    # 2
```

In questo corso `%` si usa soprattutto per:
- **Pari o dispari**: `if n % 2 == 0:` è vero per i numeri pari
- **Ogni N ripetizioni**: `if i % 10 == 0: print(i)` stampa un valore ogni 10 in un ciclo

Vedi [chapters/06-math-and-arithmetic/index.md](chapters/06-math-and-arithmetic/index.md).

### Come faccio a chiedere un input all'utente?

La funzione built-in `input()` stampa un messaggio e aspetta che l'utente scriva qualcosa.
Restituisce sempre una **stringa**, quindi se ti serve un numero devi convertirla:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"Hi {name}, you are {age} years old!")
```

Se l'utente scrive qualcosa che non si può convertire in `int`, Python solleva un `ValueError`;
racchiudere la conversione in un blocco `try/except` permette di gestire il problema senza
far bloccare il programma.

Vedi [chapters/13-user-input-type-conversion/index.md](chapters/13-user-input-type-conversion/index.md).

### Qual è la differenza tra = e ==?

- `=` è l'**operatore di assegnazione**: memorizza un valore in una variabile: `x = 5`
- `==` è l'**operatore di confronto di uguaglianza**: verifica se due valori sono uguali
  e restituisce `True` o `False`: `x == 5` → `True`

Confonderli è uno degli errori più comuni per chi inizia:

```python
x = 10        # assigns 10 to x
if x == 10:   # checks whether x equals 10
    print("yes")
```

In Python usare `=` dentro una condizione `if` è un `SyntaxError` (a differenza di C o Java,
dove è un bug comune che funziona senza dare errori).

### Che cosa sono gli operatori di confronto?

Gli **operatori di confronto** di Python confrontano due valori e restituiscono `True` o
`False`:

| Operatore | Significato |
|----------|---------|
| `==` | Uguale a |
| `!=` | Diverso da |
| `<` | Minore di |
| `>` | Maggiore di |
| `<=` | Minore o uguale a |
| `>=` | Maggiore o uguale a |

Puoi combinare più confronti con gli operatori logici `and`, `or` e `not`.

### Che cosa fa l'istruzione import?

`import` carica un modulo e rende disponibile il suo contenuto con il nome del modulo:

```python
import math
print(math.pi)      # 3.141592653589793
print(math.sqrt(9)) # 3.0
```

Puoi anche importare solo alcuni nomi da un modulo (`from math import sqrt`) oppure dare al
modulo un alias più corto (`import numpy as np`). L'istruzione `import` esegue il codice del
modulo una sola volta e ne conserva il risultato, quindi importare due volte lo stesso modulo
non costa nulla in più.

### Che cos'è il modulo math?

Il **modulo `math`** fornisce funzioni e costanti matematiche che vanno oltre l'aritmetica di base:

- `math.sqrt(x)` — radice quadrata
- `math.pi` — la costante π (3,14159…)
- `math.sin(x)`, `math.cos(x)` — funzioni trigonometriche (x in radianti)
- `math.radians(degrees)` — converte i gradi in radianti
- `math.floor(x)`, `math.ceil(x)` — arrotonda per difetto o per eccesso a un numero intero
- `math.factorial(n)` — n! (il fattoriale di n)

Il modulo `math` è usato moltissimo nel Capitolo 18 per disegnare onde sinusoidali e altre
figure matematiche con la turtle.

Vedi [chapters/18-math-module-turtle-projects/index.md](chapters/18-math-module-turtle-projects/index.md).

### Che cos'è un traceback?

Un **traceback** è il rapporto di errore di Python. Quando si verifica un errore durante
l'esecuzione, Python stampa la catena di chiamate di funzione che ha portato all'errore (la più
recente per ultima), seguita dal tipo di errore e da un breve messaggio. Leggere un traceback
**dal basso verso l'alto** è il modo più rapido per trovare il problema: l'ultima riga ti dice
che cosa è andato storto, le righe sopra ti dicono dove.

```
Traceback (most recent call last):
  File "my_program.py", line 5, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero
```

Vedi [chapters/23-error-handling-debugging/index.md](chapters/23-error-handling-debugging/index.md).

### Che cos'è un blocco try/except?

Un **blocco `try/except`** permette al tuo programma di gestire gli errori invece di bloccarsi.
Il codice nel blocco `try` viene eseguito normalmente. Se si verifica l'errore indicato, Python
salta al blocco `except` invece di fermarsi:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a whole number!")
```

Conviene intercettare l'eccezione più specifica possibile. Intercettare un generico `Exception`
o usare un `except:` senza tipo rende più difficile trovare i bug in seguito.

Vedi [chapters/23-error-handling-debugging/index.md](chapters/23-error-handling-debugging/index.md).

### Come faccio a leggere un file in Python?

Usa la funzione built-in `open()` insieme all'istruzione `with`. L'istruzione `with` chiude il
file automaticamente quando hai finito, anche se si verifica un errore:

```python
with open("story.txt", "r") as f:
    for line in f:
        print(line.strip())
```

`"r"` indica la modalità di lettura. Usa `"w"` per scrivere (sovrascrive il file) oppure `"a"`
per aggiungere in fondo. `.strip()` toglie il carattere di a capo alla fine di ogni riga.

Vedi [chapters/26-file-input-output/index.md](chapters/26-file-input-output/index.md).

### Che cos'è un'espressione regolare?

Un'**espressione regolare (regex)** è uno schema che descrive un insieme di stringhe. Il modulo
`re` ti permette di cercare, estrarre e sostituire del testo in base a questi schemi:

```python
import re
text = "My phone is 555-1234 and backup is 555-9876"
phones = re.findall(r"\d{3}-\d{4}", text)
# ['555-1234', '555-9876']
```

Pezzi di schema comuni: `\d` corrisponde a una cifra qualsiasi, `\w` a un qualsiasi carattere
di parola, `.` a un carattere qualsiasi; `*` significa zero o più volte, `+` una o più volte,
`?` zero o una volta.

Vedi [chapters/29-text-processing-regex/index.md](chapters/29-text-processing-regex/index.md).

### Quali sono i comandi di movimento della turtle?

I quattro comandi di movimento fondamentali per un oggetto turtle `t` sono:

| Comando | Azione |
|---------|--------|
| `t.forward(n)` | Si sposta di `n` pixel nella direzione attuale |
| `t.backward(n)` | Si sposta di `n` pixel nella direzione opposta |
| `t.left(angle)` | Gira a sinistra di `angle` gradi |
| `t.right(angle)` | Gira a destra di `angle` gradi |

Comandi di supporto: `t.penup()` / `t.pendown()` alzano e abbassano la penna; `t.goto(x, y)`
teletrasporta la turtle in qualsiasi coordinata; `t.speed(n)` controlla la velocità di
disegno (0 è la più veloce).

Vedi [chapters/05-drawing-with-turtle/index.md](chapters/05-drawing-with-turtle/index.md).

### Che cos'è NumPy?

**NumPy** è una libreria Python per il calcolo numerico veloce. Il suo oggetto centrale è
l'**ndarray**, un array multidimensionale che esegue operazioni matematiche elemento per
elemento con una velocità di vari ordini di grandezza superiore alle liste di Python:

```python
import numpy as np
a = np.array([1, 2, 3, 4])
print(a * 2)   # [2 4 6 8]
print(a ** 2)  # [1 4 9 16]
```

NumPy è la base del Python scientifico: matplotlib usa gli array NumPy, e Keras elabora i dati
delle immagini come array NumPy. Il Capitolo 33 tratta le funzioni NumPy usate in questo corso.

Vedi [chapters/33-numpy-scientific-computing/index.md](chapters/33-numpy-scientific-computing/index.md).

### Che cos'è matplotlib?

**matplotlib** è la libreria Python più usata per creare visualizzazioni di dati.
`matplotlib.pyplot` offre un'interfaccia simile a MATLAB per grafici a linee, grafici a
dispersione, grafici a barre e istogrammi:

```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 3]
plt.plot(x, y)
plt.title("My Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

Vedi [chapters/32-data-visualization-matplotlib/index.md](chapters/32-data-visualization-matplotlib/index.md).

### Che cosa significa lambda?

Una **lambda** è una funzione breve e anonima, scritta in un'unica espressione. È utile quando
ti serve una funzione semplice in un solo punto del codice:

```python
square = lambda x: x ** 2
print(square(5))   # 25

# Equivalent def version:
def square(x):
    return x ** 2
```

Le lambda si passano spesso come argomenti a funzioni come `sorted()` e `map()`:
`sorted(words, key=lambda w: len(w))` ordina una lista di parole in base alla lunghezza.

Vedi [chapters/24-recursion-and-fractals/index.md](chapters/24-recursion-and-fractals/index.md).

---

## Domande sui problemi più comuni

### Perché Python mi dice "IndentationError"?

Un `IndentationError` significa che Python ha trovato una riga indentata in modo non coerente
con le righe vicine. Le cause più comuni sono:

1. **Tab e spazi mescolati**: Python 3 li considera caratteri diversi. Usa sempre 4 spazi per
   livello, ovunque.
2. **Livello sbagliato**: hai indentato una riga con troppi o troppo pochi spazi.
3. **Indentazione dimenticata**: una riga che dovrebbe stare dentro un blocco `for`, `if` o
   `def` si trova al livello sbagliato.

Soluzione: imposta il tuo editor in modo che **inserisca sempre spazi** (mai tab) e usa
**4 spazi per livello di indentazione**. La maggior parte degli editor lo fa automaticamente
quando premi Tab.

Vedi [chapters/02-python-code-structure/index.md](chapters/02-python-code-structure/index.md).

### Perché la mia turtle non disegna niente?

Motivi comuni per cui la finestra della turtle resta vuota:

1. **La velocità è `0` ma il programma è finito prima che il canvas venisse mostrato**:
   chiama `turtle.done()` o `wn.mainloop()` alla fine per tenere aperta la finestra.
2. **La penna è alzata**: controlla di aver chiamato `t.pendown()` prima di muoverti.
3. **Il colore è uguale allo sfondo**: se il colore della turtle e quello dello sfondo sono
   uguali, le linee sono invisibili.
4. **`forward(0)`**: spostarsi di zero pixel non disegna nulla.
5. **In Skulpt**: il disegno della turtle di Skulpt compare dentro la pagina, non in una
   finestra separata. Assicurati di guardare l'area di output sotto l'editor del codice.

Vedi [chapters/05-drawing-with-turtle/index.md](chapters/05-drawing-with-turtle/index.md).

### Qual è la differenza tra un errore di sintassi e un errore di runtime?

- Un **errore di sintassi** viene rilevato *prima* che il programma parta. Python non riesce
  nemmeno a leggere il codice perché viola la grammatica di Python: i due punti mancanti dopo
  un `if`, parentesi non chiuse o `def` scritto male. Python mostra un `SyntaxError` con il
  numero di riga.
- Un **errore di runtime** (chiamato anche **eccezione**) viene rilevato *mentre* il programma
  è in esecuzione. Il codice è sintatticamente corretto, ma qualcosa va storto durante
  l'esecuzione: una divisione per zero, la ricerca di una chiave che non esiste in un
  dizionario, la chiamata di un metodo sul tipo sbagliato.

Esiste anche un terzo tipo: gli **errori logici**. Il programma arriva fino in fondo ma produce
la risposta sbagliata. Python non mostra alcun messaggio di errore: devi scoprire lo sbaglio
ragionando sul codice o aggiungendo delle istruzioni `print()`.

Vedi [chapters/23-error-handling-debugging/index.md](chapters/23-error-handling-debugging/index.md).

### Perché il mio ciclo while non finisce mai?

Un **ciclo infinito** si verifica quando la condizione di un ciclo `while` non diventa mai
`False`. Le cause più comuni sono:

1. **Hai dimenticato di aggiornare la variabile del ciclo**: se non cambi mai il valore che
   viene controllato, la condizione resta `True` per sempre.
2. **Aggiornamento sbagliato**: `count += 0` invece di `count += 1`.
3. **Una condizione che non può mai essere `False`**: come `while True:` senza un'istruzione
   `break`.

Soluzione: aggiungi un `print(count)` dentro il ciclo per vedere se il valore cambia davvero.
Se sei bloccato in un laboratorio Skulpt, ricarica la pagina. In un terminale, premi
**Ctrl+C** per interrompere il programma.

Vedi [chapters/10-while-loops-and-animation/index.md](chapters/10-while-loops-and-animation/index.md).

### Perché ottengo un "NameError" per una variabile che ho definito?

`NameError: name 'x' is not defined` significa che Python non trova la variabile `x` nello scope
del punto in cui l'hai usata. Cause comuni:

1. **Errore di battitura**: `scroe` invece di `score`. Python distingue maiuscole e minuscole:
   `Score` e `score` sono nomi diversi.
2. **Definita dentro una funzione**: le variabili locali esistono solo dentro la funzione in
   cui vengono create.
3. **Definita dopo la riga che la usa**: Python legge il codice dall'alto verso il basso; non
   puoi usare una variabile prima della riga che le assegna un valore.
4. **Variabile del ciclo usata dopo il ciclo**: in Python le variabili dei cicli `for` restano
   disponibili dopo il ciclo, ma `for i in []:` non assegna nulla se la lista è vuota.

### Che cosa significa "RecursionError: maximum recursion depth exceeded"?

Questo errore significa che una funzione ricorsiva ha chiamato se stessa così tante volte che
Python ha esaurito lo spazio sullo **stack delle chiamate** (call stack). Il limite predefinito
di ricorsione di Python è di 1000 chiamate. Quasi sempre significa una di queste due cose:

1. **Manca il caso base**: hai dimenticato di scrivere (o di controllare correttamente) la
   condizione che ferma la ricorsione.
2. **Il caso base non viene mai raggiunto**: la chiamata ricorsiva non rende davvero il
   problema più piccolo, avvicinandolo al caso base.

Soluzione: aggiungi un `print(n)` all'inizio della tua funzione ricorsiva per vedere se il
valore diminuisce a ogni chiamata. Se non diminuisce, va corretta la logica del passo ricorsivo.

Vedi [chapters/24-recursion-and-fractals/index.md](chapters/24-recursion-and-fractals/index.md).

### Perché la mia funzione restituisce None invece di un valore?

Ogni funzione Python restituisce `None`, a meno che tu non usi esplicitamente un'istruzione
`return` con un valore. Cause comuni di un `None` inatteso:

1. **Hai dimenticato `return`**: la funzione calcola la risposta ma non la restituisce.
2. **Il `return` è dentro un blocco `if` che non è stato raggiunto**: solo alcuni percorsi del
   codice restituiscono un valore.
3. **`print()` al posto di `return`**: `print()` mostra un valore sullo schermo ma non lo
   rimanda a chi ha chiamato la funzione.

```python
def add(a, b):
    result = a + b
    # Bug: missing return statement below
    # return result

total = add(3, 4)
print(total)   # None — because add() returned nothing
```

Vedi [chapters/11-functions-parameters-scope/index.md](chapters/11-functions-parameters-scope/index.md).

### Che cosa significa "TypeError: can only concatenate str (not 'int') to str"?

Questo errore significa che hai provato a unire una stringa e un numero con `+`. L'operatore
`+` di Python concatena due stringhe oppure somma due numeri, ma non può mescolare le due cose.
Converti prima il numero in stringa:

```python
age = 12
# Bug:
print("I am " + age + " years old.")   # TypeError

# Fix:
print("I am " + str(age) + " years old.")

# Better fix using an f-string:
print(f"I am {age} years old.")
```

Vedi [chapters/08-working-with-strings/index.md](chapters/08-working-with-strings/index.md).

### Perché il mio ciclo for salta l'ultimo numero?

Perché `range(n)` genera i numeri **fino a `n` escluso**. È una scelta voluta:

```python
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4  — stops at 4, not 5
```

Per includere `n`, usa `range(n + 1)`. Per contare da `1` a `10` compresi: `range(1, 11)`.
Questo "limite superiore escluso" è coerente con il funzionamento degli indici in Python:
l'ultimo indice valido di una lista di 5 elementi è `4`, non `5`.

### Come correggo un errore logico se non c'è nessun messaggio di errore?

Gli errori logici sono i bug più difficili perché Python non si lamenta: il programma produce
semplicemente il risultato sbagliato. Alcune strategie:

1. **Aggiungi delle istruzioni print**: stampa i valori delle variabili nei punti chiave per
   confrontare ciò che succede davvero con ciò che ti aspetti.
2. **Segui il codice a mano**: su carta, esegui il codice riga per riga come farebbe Python,
   tenendo traccia del valore di ogni variabile.
3. **Dividi il problema**: prova separatamente pezzi più piccoli del programma per capire quale
   parte produce il risultato sbagliato.
4. **Debug con la paperella di gomma**: spiega il tuo codice ad alta voce (a una paperella di
   gomma, a un amico o a Monty). Spesso è proprio spiegandolo che ti accorgi dell'errore.

Vedi [chapters/23-error-handling-debugging/index.md](chapters/23-error-handling-debugging/index.md).

### Perché 1 == 1.0 restituisce True in Python?

Proprio così! Python confronta i valori `int` e `float` dal punto di vista matematico:
`1 == 1.0` è `True` perché il numero uno è lo stesso indipendentemente dal tipo. Invece
`1 is 1.0` è `False`, perché `is` controlla l'identità degli oggetti (se sono letteralmente lo
stesso oggetto in memoria), non l'uguaglianza matematica. Usa `==` per confrontare i valori.
Usa `is` solo per i confronti con `None`, `True` o `False`.

---

## Domande sulle buone pratiche

### Come dovrei chiamare le mie variabili?

I nomi delle variabili in Python dovrebbero essere:

- **Descrittivi**: `student_count` è molto meglio di `n`, `sc` o `x`
- **In snake case**: parole separate da trattini bassi: `first_name`, `total_score`
- **In minuscolo**: per convenzione, solo le costanti usano `TUTTO_MAIUSCOLO` (`MAX_SIZE = 100`)
- **Non nomi già usati da Python**: evita `list`, `type`, `input`, `id`, `print` come nomi di
  variabile

Dei buoni nomi fanno sì che il codice si legga quasi come una frase: `if score >= passing_grade:`
è molto più chiaro di `if s >= pg:`. Un nome di variabile ben scelto ti risparmia un commento
ed evita confusione.

Vedi [chapters/03-variables-and-numbers/index.md](chapters/03-variables-and-numbers/index.md).

### Quando dovrei scrivere una funzione invece di ripetere il codice?

Scrivi una funzione ogni volta che ti accorgi di **copiare e incollare lo stesso codice** con
solo piccole modifiche. La soglia è più o meno di **tre ripetizioni**: una volta va bene, due
volte è una coincidenza, tre volte è uno schema che vale la pena trasformare in funzione.

Scrivi una funzione anche quando:
- Un blocco di codice diventa così lungo che perdi di vista che cosa fa
- Vuoi dare un nome significativo a un'operazione complessa
- Vuoi poter provare un pezzo di logica da solo

Le funzioni rendono i bug più facili da correggere: ripari la funzione una volta sola invece di
andare a cercare ogni copia del codice incollato.

Vedi [chapters/11-functions-parameters-scope/index.md](chapters/11-functions-parameters-scope/index.md).

### Come scelgo tra una lista e un dizionario?

Usa una **lista** quando:
- Gli elementi sono in ordine e li raggiungi per posizione (`items[0]`, `items[-1]`)
- Stai elaborando una sequenza di cose simili (una lista di punteggi, una lista di colori)

Usa un **dizionario** quando:
- Devi cercare dei valori tramite un nome o una chiave significativa (`grades["Alice"]`)
- Stai associando una cosa a un'altra (parola → frequenza, nome utente → password)
- Vuoi evitare di cercare in una lista un elemento alla volta

Nel dubbio: se ti ritrovi a scrivere spesso `if item in list` per cercare qualcosa, passa a
un dizionario o a un insieme.

Vedi [chapters/21-dictionaries/index.md](chapters/21-dictionaries/index.md).

### Che cos'è il principio DRY?

**DRY** sta per **Don't Repeat Yourself** (non ripeterti). Ogni conoscenza o pezzo di logica
dovrebbe esistere in un solo punto. Quando copi e incolli del codice e poi devi modificarlo,
rischi di dimenticarti di aggiornare una delle copie. Funzioni, moduli e cicli sono tutti
strumenti per evitare le ripetizioni.

Il contrario di DRY è **WET** (Write Everything Twice, scrivi tutto due volte), che porta a
programmi più difficili da mantenere. Applicare DRY con costanza è una delle abitudini più
importanti che un programmatore possa sviluppare.

Vedi [chapters/36-computational-thinking-best-practices/index.md](chapters/36-computational-thinking-best-practices/index.md).

### Quando dovrei usare un ciclo for e quando un ciclo while?

Usa un **ciclo `for`** quando sai in anticipo quante volte ripetere: per scorrere una lista,
elaborare ogni riga di un file o contare da 1 a 10.

Usa un **ciclo `while`** quando il numero di ripetizioni dipende da qualcosa che cambia durante
il ciclo: aspettare l'input dell'utente, far andare un'animazione finché una condizione cambia,
o cercare finché non trovi un elemento.

Un ciclo `while True:` con un `break` all'interno è molto comune nei programmi interattivi per
lo schema "ripeti finché l'utente non vuole smettere".

### Come rendo il mio codice più facile da leggere?

- **Usa nomi significativi**: `player_health` invece di `ph`
- **Tieni le funzioni brevi**: se una funzione supera le 20 righe, valuta di dividerla
- **Lascia una riga vuota** tra le sezioni logiche del programma
- **Usa delle costanti** al posto dei "numeri magici": `MAX_SPEED = 10` invece di un `10`
  sparso ovunque
- **Scrivi una docstring** per ogni funzione, che spieghi che cosa fa, i suoi parametri e che
  cosa restituisce
- **Evita annidamenti troppo profondi**: più di 3 livelli di indentazione sono un segnale che
  è il momento di riorganizzare il codice

Vedi [chapters/36-computational-thinking-best-practices/index.md](chapters/36-computational-thinking-best-practices/index.md).

### Quando dovrei usare try/except?

Usa `try/except` ai **confini del sistema**, cioè nei punti in cui il tuo codice interagisce con
il mondo esterno e le cose possono andare storte in modo imprevedibile:

- Convertire l'input dell'utente in un numero (`int(input(...))`)
- Aprire un file che potrebbe non esistere
- Leggere dati da una fonte esterna (CSV, JSON)

**Non** usare `try/except` per nascondere i bug della tua logica. Se ottieni un `KeyError` in
una ricerca nel tuo dizionario, è un bug da correggere, non qualcosa da far sparire in silenzio
con `except`.

Vedi [chapters/23-error-handling-debugging/index.md](chapters/23-error-handling-debugging/index.md).

### Quando conviene usare la ricorsione?

La ricorsione dà il meglio quando il problema è **naturalmente auto-simile**, cioè quando puoi
esprimere la soluzione del problema grande attraverso lo stesso tipo di problema in scala più
piccola:

- Disegni frattali (ogni ramo è una versione più piccola dell'albero)
- Visita di un albero (sottoalbero sinistro + sottoalbero destro, stesso algoritmo)
- Risoluzione di labirinti con il backtracking
- Elenco delle cartelle (ogni sottocartella è a sua volta una cartella)

La ricorsione può essere più difficile da correggere rispetto all'iterazione, e una ricorsione
profonda usa più memoria (il limite predefinito di Python è di 1000 chiamate). Per i semplici
problemi di conteggio, un ciclo `for` o `while` di solito è più semplice.

Vedi [chapters/24-recursion-and-fractals/index.md](chapters/24-recursion-and-fractals/index.md).

### Come organizzo un programma Python più grande?

Per i programmi che occupano più di una o due schermate di codice:

1. **Dividi il lavoro in funzioni**: un compito chiaro per ogni funzione
2. **Raggruppa le funzioni collegate in moduli**: metti le funzioni di disegno in `drawing.py`
   e quelle sui dati in `data.py`
3. **Usa una funzione `main()`** come punto di ingresso e chiamala con la protezione `if __name__ == "__main__":`
4. **Tieni i dati separati dalla logica di visualizzazione**: prima calcola i risultati, poi stampali o disegnali
5. **Scrivi una breve docstring** all'inizio di ogni file per spiegarne lo scopo

Queste pratiche funzionano sia per uno script di 100 righe sia per un progetto di 10.000 righe,
senza cambiare le abitudini di base.

Vedi [chapters/31-advanced-functions-oop/index.md](chapters/31-advanced-functions-oop/index.md).

### Come uso il controllo di versione con Python?

**Git** è lo strumento standard di controllo di versione per i progetti Python. Il flusso di
lavoro di base:

1. `git init` — crea un nuovo repository nella cartella del progetto
2. `git add my_file.py` — prepara (stage) un file che hai modificato
3. `git commit -m "Add drawing function"` — salva un'istantanea con un messaggio
4. `git log` — mostra la cronologia delle istantanee

Il controllo di versione ti permette di sperimentare in sicurezza: se rompi qualcosa, puoi
sempre tornare all'ultima istantanea funzionante. Per condividere e collaborare, GitHub è il
servizio di hosting più diffuso.

Vedi [chapters/36-computational-thinking-best-practices/index.md](chapters/36-computational-thinking-best-practices/index.md).

---

## Domande sugli argomenti avanzati

### In che modo BFS garantisce il percorso più breve?

BFS esplora i nodi **livello per livello** usando una coda. Dato che una coda funziona con la
regola "primo arrivato, primo servito", BFS elabora sempre tutti i nodi a distanza 1 prima di
qualsiasi nodo a distanza 2, tutti quelli a distanza 2 prima di qualsiasi nodo a distanza 3, e
così via. Questo significa che la prima volta che BFS raggiunge il nodo di arrivo, ci è arrivato
con il minor numero di passi possibile. Un percorso più lungo verso lo stesso arrivo non può
arrivare per primo, perché il percorso più breve è già stato esplorato del tutto a un livello
precedente.

DFS non offre questa garanzia: può scendere in profondità lungo un vicolo cieco prima di
esplorare una strada più breve, quindi può trovare un percorso che non è il più breve.

Vedi [chapters/30-algorithms-data-structures/index.md](chapters/30-algorithms-data-structures/index.md).

### Che cos'è una rete neurale convoluzionale?

Una **rete neurale convoluzionale (CNN)** è un tipo di rete neurale progettata per elaborare dati
con una struttura a griglia, come le immagini. Invece di collegare ogni pixel a ogni neurone
(il che significherebbe milioni di collegamenti), una CNN usa dei piccoli **filtri** (per
esempio griglie di pesi 3×3) che scorrono sull'immagine e rilevano localmente bordi, angoli e
schemi. Sovrapponendo più strati convoluzionali, la rete riesce a riconoscere caratteristiche
sempre più complesse: bordi → forme → oggetti.

Nel Capitolo 38 il corso amplia l'esempio MNIST con una semplice CNN che usa gli strati Keras
`Conv2D` e `MaxPooling2D`.

Vedi [chapters/38-neural-networks-and-mnist/index.md](chapters/38-neural-networks-and-mnist/index.md).

### Che cos'è il dataset MNIST?

**MNIST** (Modified National Institute of Standards and Technology) è un classico dataset di
machine learning che contiene 70.000 immagini in scala di grigi di cifre scritte a mano da 0 a 9,
ognuna di 28×28 pixel. 60.000 immagini servono per l'addestramento e 10.000 per il test. MNIST
è l'"Hello World" del machine learning: i modelli addestrati su questo dataset raggiungono di
solito un'accuratezza del 97–99%, ed è quindi un buon banco di prova per imparare come
funzionano le reti neurali senza bisogno di enormi risorse di calcolo.

Vedi [chapters/37-machine-learning-foundations/index.md](chapters/37-machine-learning-foundations/index.md).

### Qual è la differenza tra apprendimento supervisionato e non supervisionato?

- L'**apprendimento supervisionato** si addestra su **esempi etichettati**: per ogni input viene
  fornita la risposta corretta (l'etichetta). Il modello impara a prevedere l'etichetta per
  nuovi input. Il riconoscimento delle cifre MNIST è supervisionato: ogni immagine è etichettata
  con la cifra corretta (0–9).
- L'**apprendimento non supervisionato** trova una struttura in **dati non etichettati**: non
  viene fornita alcuna risposta corretta. Il modello scopre da solo raggruppamenti, schemi o
  rappresentazioni compresse. Il clustering e gli autoencoder ne sono esempi.

Questo corso si concentra sull'apprendimento supervisionato. L'apprendimento non supervisionato
è citato brevemente in [chapters/37-machine-learning-foundations/index.md](chapters/37-machine-learning-foundations/index.md).

### Che cos'è il broadcasting di NumPy?

Il **broadcasting** è la regola di NumPy per applicare un'operazione tra array di forme diverse.
Quando scrivi `array + 5`, NumPy si comporta come se `5` fosse un array della stessa forma di
`array`, pieno di cinque, e somma elemento per elemento. Più in generale, se due array hanno
forme compatibili, NumPy estende quello più piccolo per farlo corrispondere a quello più grande,
senza copiare i dati.

```python
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a * 2)   # every element multiplied by 2
```

Il broadcasting rende il codice numerico molto più conciso ed efficiente rispetto a scrivere dei
cicli espliciti.

Vedi [chapters/33-numpy-scientific-computing/index.md](chapters/33-numpy-scientific-computing/index.md).

### Come funziona l'elaborazione delle immagini con Pillow?

**Pillow** (PIL) ti permette di aprire, mostrare, modificare e salvare immagini in Python:

```python
from PIL import Image
img = Image.open("photo.jpg")
img.show()                        # display in default viewer
small = img.resize((100, 100))   # resize
gray = img.convert("L")          # convert to grayscale
gray.save("gray_photo.jpg")      # save to file
```

Pillow dà anche accesso ai dati grezzi dei pixel sotto forma di array NumPy, il che ti permette
di modificare i singoli pixel: schiarire un'immagine, invertirne i colori o estrarne delle
caratteristiche per preparare i dati al machine learning.

Vedi [chapters/34-image-processing-pillow/index.md](chapters/34-image-processing-pillow/index.md).

### Che cos'è la programmazione a eventi?

La **programmazione a eventi** (event-driven) è uno stile in cui il programma aspetta degli
**eventi**, cioè azioni dell'utente come clic del mouse o pressioni di tasti, ed esegue una
**funzione di callback** ogni volta che un evento si verifica. Invece di essere eseguito una
sola volta dall'alto verso il basso, il programma entra in un **ciclo degli eventi** (event
loop) che resta in ascolto degli eventi all'infinito.

La grafica turtle usa la programmazione a eventi: `wn.onscreenclick(my_function)` registra
`my_function` come callback per i clic del mouse. Quando l'utente fa clic sul canvas, il modulo
turtle chiama `my_function` passandole le coordinate del clic.

```python
def clicked(x, y):
    t.goto(x, y)

wn.onscreenclick(clicked)
wn.mainloop()   # start the event loop
```

Vedi [chapters/35-advanced-turtle-event-driven/index.md](chapters/35-advanced-turtle-event-driven/index.md).

### Come creo un mio modulo Python?

Creare un modulo è semplice come salvare del codice Python in un file `.py`. Tutte le funzioni,
le variabili o le classi che definisci in quel file diventano disponibili quando un altro
programma lo importa:

```python
# shapes.py
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.right(120)
```

```python
# main.py
import turtle
import shapes

t = turtle.Turtle()
shapes.draw_square(t, 100)
shapes.draw_triangle(t, 80)
```

Entrambi i file devono trovarsi nella stessa cartella (o nel percorso di ricerca dei moduli di
Python). Aggiungi la protezione `if __name__ == "__main__":` in `shapes.py` se vuoi poterlo
provare da solo, senza che quel codice di prova venga eseguito quando il modulo viene importato.

Vedi [chapters/27-standard-library-json/index.md](chapters/27-standard-library-json/index.md).

### Quali sono gli algoritmi di ordinamento più comuni e quando mi servono?

Questo corso presenta tre algoritmi di ordinamento elementari:

- **Bubble sort**: scambia ripetutamente gli elementi vicini che sono nell'ordine sbagliato.
  Facile da capire, lento con liste grandi (O(n²)).
- **Selection sort**: trova l'elemento più piccolo nella parte non ancora ordinata e lo sposta
  in testa. Anche questo è O(n²), ma fa meno scambi del bubble sort.
- **Insertion sort**: costruisce la lista ordinata un elemento alla volta, inserendo ogni nuovo
  elemento nella posizione giusta. È efficiente con dati quasi ordinati.

In pratica non dovrai quasi mai scrivere un tuo algoritmo di ordinamento: le funzioni built-in
di Python `sorted()` e `list.sort()` usano Timsort, che è O(n log n) e sui dati reali batte
tutti e tre gli algoritmi elementari. Si studiano gli algoritmi di ordinamento per capire come i
computer risolvono i problemi di ordinamento e per imparare ad analizzare l'efficienza degli
algoritmi con la notazione O-grande (Big-O).

Vedi [chapters/30-algorithms-data-structures/index.md](chapters/30-algorithms-data-structures/index.md).
