#!/usr/bin/env python3
"""
Traduce in italiano i nomi dei concetti nei quiz e negli elenchi dei capitoli.

- Nei file docs/chapters/*/quiz.md sostituisce le righe
  "**Concept Tested:** <nome inglese>" con "**Concetto verificato:** <nome italiano>".
- Nelle sezioni "## Concetti Trattati" di docs/chapters/*/index.md traduce le
  voci dell'elenco numerato.

I nomi seguono la tabella T qui sotto (stessa traduzione ovunque). I nomi che
sono codice, come plt.show(), restano invariati. Utile dopo una
sincronizzazione con l'originale inglese: i concetti nuovi, non ancora nella
tabella, vengono elencati e lasciati com'erano.

Nessuna dipendenza esterna (solo libreria standard).

Esempi:
  python scripts/traduci_concetti.py --check   # elenca solo cosa manca
  python scripts/traduci_concetti.py           # applica le traduzioni
"""

import argparse
import re
from pathlib import Path

T = {
"abs() Function": "Funzione abs()",
"Absolute Positioning goto()": "Posizionamento assoluto con goto()",
"Abstraction": "Astrazione",
"Accessing Values by Key": "Accesso ai valori tramite chiave",
"Adding and Updating Entries": "Aggiungere e aggiornare voci",
"Anchors": "Ancore",
"Animation with Turtle Loops": "Animazione con i cicli della turtle",
"any() and all()": "any() e all()",
"append() Method": "Metodo append()",
"argmax": "argmax",
"*args": "*args",
"Arithmetic Operators": "Operatori aritmetici",
"Array Shape": "Forma di un array",
"Array Slicing": "Slicing degli array",
"assert Statement": "Istruzione assert",
"Augmented Assignment Operators": "Operatori di assegnazione composta",
"Axis Labels and Titles": "Etichette degli assi e titoli",
"Background and Pen Colors": "Colori dello sfondo e della penna",
"Base Case": "Caso base",
"begin_fill() and end_fill()": "begin_fill() e end_fill()",
"BFS": "BFS (ricerca in ampiezza)",
"BFS and DFS": "BFS e DFS",
"Big-O Notation": "Notazione O-grande",
"Binary Search": "Ricerca binaria",
"Blank Lines and Readability": "Righe vuote e leggibilità",
"bool() Conversion": "Conversione con bool()",
"Boolean in Conditions": "Booleani nelle condizioni",
"Boolean Type": "Tipo booleano",
"break Statement": "Istruzione break",
"Broadcasting": "Broadcasting",
"Browser-Based Python Environments": "Ambienti Python nel browser",
"Bubble Sort": "Bubble sort",
"Callback Functions": "Funzioni callback",
"Call Stack": "Pila delle chiamate",
"CamelCase Naming Convention": "Convenzione di nomi CamelCase",
"Case Sensitivity": "Distinzione tra maiuscole e minuscole",
"Chained Comparisons": "Confronti concatenati",
"Chart Types": "Tipi di grafici",
"Checking for None with is": "Controllare None con is",
"chr() and ord()": "chr() e ord()",
"class Keyword": "Parola chiave class",
"Class vs Instance Variables": "Variabili di classe e variabili di istanza",
"Clearing and Resetting": "Cancellare e reimpostare",
"CNN Properties": "Proprietà delle CNN",
"CNN vs Dense Networks": "CNN e reti dense a confronto",
"Code Block Structure": "Struttura dei blocchi di codice",
"Color Mode Conversion": "Conversione della modalità colore",
"Common Exception Types": "Tipi di eccezioni comuni",
"Comparison Operators": "Operatori di confronto",
"Compound Conditions": "Condizioni composte",
"Constants by Convention": "Costanti per convenzione",
"continue Statement": "Istruzione continue",
"Conv2D Layer": "Livello Conv2D",
"count() and index() Methods": "Metodi count() e index()",
"Countdown Loop": "Ciclo del conto alla rovescia",
"Creating Dictionaries": "Creare dizionari",
"Creating Instances": "Creare istanze",
"Cropping Images": "Ritagliare le immagini",
"CSV Module": "Modulo csv",
"Current Working Directory": "Cartella di lavoro corrente",
"Custom Exception Classes": "Classi di eccezioni personalizzate",
"Custom Modules": "Moduli personalizzati",
"Decomposition": "Scomposizione",
"Default Parameter Values": "Valori predefiniti dei parametri",
"def Keyword": "Parola chiave def",
"Dictionary Comprehensions": "Dictionary comprehension",
"Dictionary from zip()": "Dizionario da zip()",
"dir() and help()": "dir() e help()",
"Division Returns Float": "La divisione restituisce un float",
"Docstrings": "Docstring",
"Dot Notation": "Notazione a punto",
"Drawing circle() and Polygons": "Disegnare con circle() e poligoni",
"Drawing Star Patterns": "Disegnare motivi a stella",
"Dropout": "Dropout",
"DRY Principle": "Principio DRY",
"Dunder Methods": "Metodi dunder",
"Element-Wise Math": "Calcoli elemento per elemento",
"elif Chains": "Catene elif",
"else and finally Clauses": "Clausole else e finally",
"else Clause on Loops": "Clausola else nei cicli",
"enumerate()": "enumerate()",
"Epoch": "Epoca",
"Escape Characters": "Caratteri di escape",
"Event-Driven Model": "Modello a eventi",
"Event Loop": "Ciclo degli eventi",
"Exponentiation Operator": "Operatore di elevamento a potenza",
"extend() Method": "Metodo extend()",
"File Modes": "Modalità di apertura dei file",
"filter()": "filter()",
"Flatten Layer": "Livello Flatten",
"Floats": "Numeri decimali (float)",
"for Loop over Sequence": "Ciclo for su una sequenza",
"for Loop with range()": "Ciclo for con range()",
"Fractal Tree": "Albero frattale",
"from...import Syntax": "Sintassi from...import",
"f-Strings": "f-string",
"Function Calls": "Chiamate di funzione",
"Functions Returning None": "Funzioni che restituiscono None",
"global Keyword": "Parola chiave global",
"Google Colab": "Google Colab",
"Graph and Adjacency List": "Grafo e lista di adiacenza",
"Grid Lines": "Linee della griglia",
"Hex Color Codes": "Codici colore esadecimali",
"Histograms": "Istogrammi",
"if...else Block": "Blocco if...else",
"if Statement": "Istruzione if",
"Image Attributes": "Attributi delle immagini",
"Image Formats": "Formati delle immagini",
"Image Mode": "Modalità dell'immagine",
"Implicit vs Explicit Conversion": "Conversione implicita ed esplicita",
"import...as Alias": "Alias con import...as",
"Importing matplotlib": "Importare matplotlib",
"Importing NumPy": "Importare NumPy",
"Importing Pillow": "Importare Pillow",
"import Statement": "Istruzione import",
"import turtle": "import turtle",
"Indentation as Syntax": "L'indentazione come sintassi",
"Infinite Loops to Avoid": "Cicli infiniti da evitare",
"Inheritance": "Ereditarietà",
"__init__() Constructor": "Costruttore __init__()",
"input() Function": "Funzione input()",
"Input Validation": "Validazione dell'input",
"insert() Method": "Metodo insert()",
"Installing Python": "Installare Python",
"int() Conversion": "Conversione con int()",
"Integer Division Operator": "Operatore di divisione intera",
"Integers": "Numeri interi",
"isinstance()": "isinstance()",
"join() Method": "Metodo join()",
"json.dumps()": "json.dumps()",
"JSON Format": "Formato JSON",
"json.loads()": "json.loads()",
"json Module Functions": "Funzioni del modulo json",
"JSON Type Mapping": "Corrispondenza tra tipi JSON e Python",
"Jupyter Notebooks": "Notebook Jupyter",
"keyboard events and listen()": "Eventi della tastiera e listen()",
"KeyError": "KeyError",
"Key Membership with in": "Verificare una chiave con in",
"Keys, Values, and Items": "Chiavi, valori ed elementi",
"Keyword Arguments": "Argomenti con nome",
"**kwargs": "**kwargs",
"Lambda Functions": "Funzioni lambda",
"Line Iteration": "Leggere un file riga per riga",
"List Comprehensions": "List comprehension",
"List Indexing": "Indici delle liste",
"List Length with len()": "Lunghezza di una lista con len()",
"List Slicing": "Slicing delle liste",
"List Type": "Tipo lista",
"Local Scope and Global Scope": "Scope locale e scope globale",
"Logical Operators": "Operatori logici",
"Loop Accumulator Pattern": "Schema dell'accumulatore nei cicli",
"Loop Counter Variable": "Variabile contatore del ciclo",
"Loss Function": "Funzione di perdita",
"map()": "map()",
"math.degrees()": "math.degrees()",
"math.factorial()": "math.factorial()",
"math.floor() and math.ceil()": "math.floor() e math.ceil()",
"math.pi": "math.pi",
"math.radians()": "math.radians()",
"math.sin() and Turtle Projects": "math.sin() e progetti con la turtle",
"math.sqrt()": "math.sqrt()",
"max(), min(), sum()": "max(), min(), sum()",
"MaxPooling2D": "MaxPooling2D",
"mean and std": "Media e deviazione standard",
"Meaningful Names": "Nomi significativi",
"Membership with in": "Appartenenza con in",
"MNIST Dataset": "Dataset MNIST",
"model.compile()": "model.compile()",
"model.fit()": "model.fit()",
"Modularity": "Modularità",
"Modulo Operator": "Operatore modulo",
"Multi-Line Strings": "Stringhe su più righe",
"Multiple Assignment": "Assegnazione multipla",
"Multiple Lines": "Più linee nello stesso grafico",
"Mutable vs Immutable": "Mutabile e immutabile",
"Named Colors": "Colori con nome",
"__name__ Guard": "Controllo con __name__",
"Negative Indexing": "Indici negativi",
"Negative Numbers": "Numeri negativi",
"Nested Dictionaries": "Dizionari annidati",
"Nested if Statements": "Istruzioni if annidate",
"Nested Loops": "Cicli annidati",
"Neural Network Layers": "Livelli di una rete neurale",
"None Value": "Il valore None",
"np.linspace()": "np.linspace()",
"np.zeros() and np.ones()": "np.zeros() e np.ones()",
"NumPy Arrays": "Array NumPy",
"Object Composition": "Composizione di oggetti",
"onkey()": "onkey()",
"onscreenclick()": "onscreenclick()",
"ontimer()": "ontimer()",
"Order of Operations": "Ordine delle operazioni",
"os Module": "Modulo os",
"os.path": "os.path",
"Overfitting": "Overfitting",
"Pair Programming": "Programmazione in coppia",
"Pattern Elements": "Elementi delle espressioni regolari",
"Pattern Recognition": "Riconoscimento di schemi",
"Pen Size and Color": "Spessore e colore della penna",
"penup() and pendown()": "penup() e pendown()",
"pip": "pip",
"Pixel Data": "Dati dei pixel",
"plt.show()": "plt.show()",
"pop() Method": "Metodo pop()",
"Positional Parameters": "Parametri posizionali",
"Position Query xcor() ycor()": "Leggere la posizione con xcor() e ycor()",
"print() Function": "Funzione print()",
"@property Decorator": "Decoratore @property",
"Pure Functions vs Side Effects": "Funzioni pure ed effetti collaterali",
"Python 2 vs Python 3": "Python 2 e Python 3 a confronto",
"Python Interpreter Overview": "Panoramica dell'interprete Python",
"Python Keywords": "Parole chiave di Python",
"Python REPL": "REPL di Python",
"Quantifiers": "Quantificatori",
"Queue (FIFO)": "Coda (FIFO)",
"Radians vs Degrees": "Radianti e gradi",
"raise Statement": "Istruzione raise",
"random.choice()": "random.choice()",
"random.randint()": "random.randint()",
"random.random()": "random.random()",
"random.sample()": "random.sample()",
"random.seed()": "random.seed()",
"random.shuffle()": "random.shuffle()",
"Range with Start Stop Step": "range() con inizio, fine e passo",
"Raw Strings": "Stringhe raw",
"Raw Strings for Regex": "Stringhe raw per le regex",
"Reading Files": "Leggere i file",
"Reading Multiple Inputs": "Leggere più input",
"Reading Tracebacks": "Leggere un traceback",
"readlines()": "readlines()",
"Recursion Concept": "Il concetto di ricorsione",
"Recursive Factorial": "Fattoriale ricorsivo",
"Refactoring": "Refactoring",
"re.findall()": "re.findall()",
"ReLU Activation": "Attivazione ReLU",
"re Module": "Modulo re",
"remove() Method": "Metodo remove()",
"Removing Entries": "Rimuovere voci",
"replace() Method": "Metodo replace()",
"re.search()": "re.search()",
"Resizing Images": "Ridimensionare le immagini",
"re.split()": "re.split()",
"re.sub()": "re.sub()",
"Return Values": "Valori restituiti",
"RGB Color Model": "Modello di colore RGB",
"RNNs and LSTMs": "RNN e LSTM",
"round() Function": "Funzione round()",
"Running Scripts": "Eseguire gli script",
"Safe Access with get()": "Accesso sicuro con get()",
"Saving Figures": "Salvare i grafici",
"Saving Images": "Salvare le immagini",
"Scatter Plots": "Grafici a dispersione",
"Scientific Notation Floats": "Float in notazione scientifica",
"self": "self",
"Set Difference": "Differenza tra insiemi",
"setheading() Direction": "Direzione con setheading()",
"Set Intersection": "Intersezione tra insiemi",
"Set Methods": "Metodi degli insiemi",
"Set Type": "Tipo insieme (set)",
"Set Union": "Unione di insiemi",
"Short-Circuit Evaluation": "Valutazione a corto circuito",
"Single-Element Tuple Syntax": "Sintassi della tupla con un solo elemento",
"Single-Line Comments": "Commenti su una riga",
"Single vs Double Quotes": "Virgolette singole e doppie",
"Skulpt Browser Python": "Skulpt: Python nel browser",
"Softmax Activation": "Attivazione softmax",
"sorted() and reversed()": "sorted() e reversed()",
"sort() Method": "Metodo sort()",
"split() Method": "Metodo split()",
"Stack (LIFO)": "Pila (LIFO)",
"Stack Pattern": "Schema della pila",
"Standard Library": "Libreria standard",
"Statement vs Expression": "Istruzioni ed espressioni",
"str() Conversion": "Conversione con str()",
"String Concatenation": "Concatenazione di stringhe",
"String Immutability": "Immutabilità delle stringhe",
"String Indexing": "Indici delle stringhe",
"String Length with len()": "Lunghezza di una stringa con len()",
"String Repetition": "Ripetizione di stringhe",
"String Search Methods": "Metodi di ricerca nelle stringhe",
"String Slicing": "Slicing delle stringhe",
"String Type": "Tipo stringa",
"__str__() Method": "Metodo __str__()",
"Subplots": "Sottografici (subplot)",
"super()": "super()",
"Supervised vs Unsupervised Learning": "Apprendimento supervisionato e non supervisionato",
"Swapping Variables": "Scambiare variabili",
"sys Module": "Modulo sys",
"Ternary Expression": "Espressione ternaria",
"Test-Driven Thinking": "Pensare per test",
"Thonny IDE": "IDE Thonny",
"time Module Overview": "Panoramica del modulo time",
"time.sleep()": "time.sleep()",
"Training with model.fit()": "Addestramento con model.fit()",
"Train/Validation/Test Splits": "Suddivisione in training, validazione e test",
"Truthiness and Falsiness": "Valori considerati veri e falsi",
"try/except Blocks": "Blocchi try/except",
"Tuples as Return Values": "Tuple come valori restituiti",
"Tuple Type": "Tipo tupla",
"Tuple Unpacking": "Spacchettamento delle tuple",
"Turtle Appearance": "Aspetto della turtle",
"turtle.dot()": "turtle.dot()",
"Turtle Movement Commands": "Comandi di movimento della turtle",
"turtle.Screen() Object": "L'oggetto turtle.Screen()",
"Type Conversion": "Conversione di tipo",
"type() Function": "Funzione type()",
"Types of Errors": "Tipi di errori",
"Variable Assignment": "Assegnazione di variabili",
"Variable Naming Rules": "Regole per i nomi delle variabili",
"Variable Naming (snake_case)": "Nomi delle variabili (snake_case)",
"Variable Reassignment": "Riassegnazione di variabili",
"Version Control": "Controllo di versione",
"Virtual Environments": "Ambienti virtuali",
"while Loop": "Ciclo while",
"Whitespace Rules": "Regole sugli spazi",
"with Statement": "Istruzione with",
"Writing Text with turtle.write()": "Scrivere testo con turtle.write()",
"Writing to a File": "Scrivere su un file",
"zip()": "zip()",
}

QUIZ_RE = re.compile(r"^([ \t]*)\*\*Concept Tested:\*\* (.+?)([ \t]*\r?)$", re.M)
ITEM_RE = re.compile(r"^(\d+\. )(.+?)([ \t]*\r?)$")


def traduci_quiz(testo, mancanti):
    def sostituisci(m):
        nome = m.group(2)
        if nome not in T:
            mancanti.add(nome)
            return m.group(0)
        return m.group(1) + "**Concetto verificato:** " + T[nome] + m.group(3)
    return QUIZ_RE.subn(sostituisci, testo)


def traduci_elenco(testo, mancanti):
    righe = testo.split("\n")
    n = 0
    dentro = False
    for i, riga in enumerate(righe):
        if riga.startswith("## "):
            dentro = riga.startswith("## Concetti Trattati")
            continue
        m = ITEM_RE.match(riga)
        if not (dentro and m):
            continue
        nome = m.group(2)
        if nome in T.values():
            continue  # già tradotto
        if nome not in T:
            mancanti.add(nome)
            continue
        righe[i] = m.group(1) + T[nome] + m.group(3)
        n += 1
    return "\n".join(righe), n


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--docs", default="docs", help="cartella docs (default: docs)")
    parser.add_argument("--check", action="store_true",
                        help="non modifica i file, elenca solo i concetti da tradurre")
    args = parser.parse_args()

    capitoli = Path(args.docs) / "chapters"
    mancanti = set()
    totale = 0
    for f in sorted(capitoli.glob("*/quiz.md")) + sorted(capitoli.glob("*/index.md")):
        testo = f.read_text(encoding="utf-8")
        if f.name == "quiz.md":
            nuovo, n = traduci_quiz(testo, mancanti)
        else:
            nuovo, n = traduci_elenco(testo, mancanti)
        if n:
            totale += n
            print(f"{f}: {n} sostituzioni")
            if not args.check:
                f.write_text(nuovo, encoding="utf-8")

    azione = "da fare" if args.check else "fatte"
    print(f"\nSostituzioni {azione}: {totale}")
    if mancanti:
        print(f"Concetti non presenti nella tabella T ({len(mancanti)}), da aggiungere:")
        for nome in sorted(mancanti):
            print(f"  {nome}")


if __name__ == "__main__":
    main()
