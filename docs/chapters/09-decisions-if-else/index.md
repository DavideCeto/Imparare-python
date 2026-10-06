---
title: Prendere Decisioni con If/Else
description: Insegna a Python a fare scelte usando i valori booleani, gli operatori di confronto, gli operatori logici, le diramazioni if/elif/else e i condizionali annidati.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 10:55:00
version: 0.09
---

# Prendere Decisioni con If/Else

## Riepilogo

I programmi devono fare delle scelte — proprio come i blocchi "if/then/else" di Scratch.
Le parole chiave `if`, `elif` ed `else` di Python gestiscono le diramazioni. Questo capitolo
introduce il tipo booleano (`True`/`False`), gli operatori di confronto
(`==`, `!=`, `<`, `>`), gli operatori logici (`and`, `or`, `not`),
i confronti concatenati, e i condizionali annidati per decisioni a più vie.

## Concetti Trattati

Questo capitolo tratta i seguenti 9 concetti del grafo di apprendimento:

1. Boolean Type
2. Comparison Operators
3. Logical Operators
4. Boolean in Conditions
5. Chained Comparisons
6. if Statement
7. if...else Block
8. elif Chains
9. Nested if Statements

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 3: Variabili e Numeri](../03-variables-and-numbers/index.md)
- [Capitolo 6: Matematica e Aritmetica](../06-math-and-arithmetic/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Creare e confrontare valori booleani usando `True`, `False` e gli operatori di confronto
- Scrivere blocchi `if`, `if/else` e `if/elif/else` per far diramare il tuo programma
- Combinare condizioni con `and`, `or` e `not`
- Usare una catena `if/elif/else` per disegnare forme diverse in base al valore di una variabile

Ogni programma utile prende decisioni.
Un gioco deve sapere se un giocatore ha vinto.
Una calcolatrice deve sapere se il denominatore è zero prima di dividere.
L'**istruzione `if`** di Python è il modo in cui i programmi scelgono cosa fare in base a cosa è vero o falso.

!!! mascot-welcome "Benvenuto/a al Capitolo 9!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo è il capitolo in cui i tuoi programmi smettono di essere strade a senso unico! Una volta che conosci `if`, `elif` ed `else`, il tuo codice può rispondere diversamente a situazioni diverse — proprio come un vero decisore. Programmiamo insieme!

## Il Tipo Booleano

Un **booleano** (chiamato così dal matematico George Boole) è un valore che è `True` oppure `False` — e nient'altro.
In Python, `True` e `False` si scrivono con la prima lettera maiuscola.

```python
is_raining = True
has_umbrella = False
print(is_raining)       # True
print(type(True))       # <class 'bool'>
```

I booleani vengono prodotti automaticamente ogni volta che Python **confronta** due valori.

## Operatori di Confronto

Un **operatore di confronto** confronta due valori e restituisce un booleano.
Python ha sei operatori di confronto:

| Operatore | Significato | Esempio | Risultato |
|----------|---------|---------|--------|
| `==` | uguale a | `5 == 5` | `True` |
| `!=` | diverso da | `5 != 3` | `True` |
| `<` | minore di | `3 < 5` | `True` |
| `>` | maggiore di | `5 > 3` | `True` |
| `<=` | minore o uguale a | `5 <= 5` | `True` |
| `>=` | maggiore o uguale a | `4 >= 5` | `False` |

!!! mascot-warning "L'Errore più Comune dei Principianti"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    **`=` NON è la stessa cosa di `==`.** Un singolo `=` *assegna* un valore a una variabile: `x = 5`. Un doppio `==` *confronta* due valori: `x == 5`. Scrivere `if x = 5:` ti darà un `SyntaxError`. Questo errore capita a ogni principiante — ora sai che devi stare attento/a!

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, i blocchi verdi **Operators** includono `=`, `<` e `>` per i confronti, e la categoria **Control** ha i blocchi "if/then" e "if/then/else". L'istruzione `if` di Python e gli operatori di confronto svolgono esattamente gli stessi compiti — li digiti semplicemente invece di trascinarli!

Il programma qui sotto usa i confronti per descrivere un punteggio.
Prima di cliccare su Run, pensa a quali chiamate `print()` verranno effettivamente eseguite.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La variabile `score` è `75`. Guarda attentamente ogni istruzione `if`.
    Quali condizioni sono `True` per un punteggio di 75?
    Quante righe pensi verranno effettivamente stampate?
    Fai la tua previsione — poi clicca su Run!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

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
initCmLab('', `score = 75

print("Score:", score)
print("Is 75 == 75?", score == 75)
print("Is 75 > 50? ", score > 50)
print("Is 75 < 100?", score < 100)
print("Is 75 == 100?", score == 100)

if score >= 60:
    print("Passing grade!")

if score == 100:
    print("Perfect score!")`);
</script>

Avevi indovinato? La riga `"Perfect score!"` NON è stata stampata perché `75 == 100` è `False`. Il corpo dell'`if` viene eseguito solo quando la sua condizione è `True`.

## L'Istruzione if

Un'**istruzione `if`** esegue un blocco di codice solo quando una condizione è `True`.
La struttura è:

```python
if condition:
    # this block runs only when condition is True
    do_something()
```

I due punti `:` alla fine della riga `if` sono obbligatori.
Le righe indentate sotto di essa formano il **corpo dell'if** — vengono eseguite solo quando la condizione è `True`.

## Il Blocco if…else

Un **blocco `if/else`** aggiunge un secondo ramo: codice che viene eseguito quando la condizione è `False`.

```python
temperature = 15

if temperature > 20:
    print("It's warm — wear a t-shirt!")
else:
    print("It's cool — bring a jacket!")
```

Ogni `if/else` esegue *esattamente un* ramo — mai entrambi, mai nessuno.
Quando `temperature` è `15`, la condizione `15 > 20` è `False`, quindi viene eseguito il ramo `else`.

## Catene elif

Quando hai bisogno di più di due scelte, usa **`elif`** (abbreviazione di "else if"):

```python
score = 83

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

Python controlla le condizioni dall'alto verso il basso ed esegue il **primo** ramo la cui condizione è `True`, poi salta tutto il resto.
Per `score = 83`, la prima condizione `True` è `score >= 80`, quindi Python stampa `"B"` e ignora i rami rimanenti.

### Osservalo: Si Illumina un Solo Percorso

L'esploratore qui sotto trasforma una catena elif in un diagramma di flusso. Esattamente **un** percorso si illumina di verde e — questa è la parte importante — le condizioni dopo il primo `True` sono contrassegnate come **"mai controllate"** perché Python non le guarda nemmeno. Prima di muovere il cursore, prevedi: **con un punteggio di 85, quali condizioni vengono controllate, e quale ramo viene eseguito?**

<iframe src="../../sims/control-flow-explorer/main.html" height="562" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Control Flow Explorer](../../sims/control-flow-explorer/index.md){ .md-button }

Fai scorrere lentamente il punteggio da 100 a 0 e osserva il percorso verde scendere lungo la catena un ramo alla volta. Poi prova il programma **Simple if** — cosa succede al diagramma di flusso quando la condizione è False e non c'è un else?

## Operatori Logici

Gli **operatori logici** combinano due valori booleani in uno:

| Operatore | Significato | Esempio | Risultato |
|----------|---------|---------|--------|
| `and` | Entrambi devono essere True | `5 > 3 and 2 < 4` | `True` |
| `or` | Almeno uno deve essere True | `5 > 3 or 2 > 4` | `True` |
| `not` | Inverte True↔False | `not True` | `False` |

```python
age = 13
has_ticket = True

if age >= 10 and has_ticket:
    print("Welcome to the show!")

if age < 5 or age > 65:
    print("Free admission!")
```

### Osservalo: Il Boolean Logic Lab

Invece di memorizzare le tavole di verità, costruiscile tu stesso/a. Imposta gli input A e B nel laboratorio qui sotto e osserva la lampadina del risultato. Prima di iniziare, prevedi: **se A è False, `A and B` accende mai la lampadina — indipendentemente da B?**

<iframe src="../../sims/boolean-logic-lab/main.html" height="512" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Boolean Logic Lab](../../sims/boolean-logic-lab/index.md){ .md-button }

Nota una cosa furtiva: quando A da solo decide la risposta, il blocco B si oscura e dice "Python non ha mai guardato qui." Questo trucco si chiama **valutazione a corto circuito**, e lo incontrerai di nuovo nel Capitolo 19. Il pannello bonus in fondo anticipa un'altra idea del Capitolo 19 — ogni valore, anche `0` e `""`, può comportarsi come un booleano.

## Confronti Concatenati

Python ti permette di scrivere controlli di intervallo in un modo naturale, simile alla matematica:

```python
x = 15

# The Python way (chained):
if 10 < x < 20:
    print("x is between 10 and 20")

# The long way (same thing):
if x > 10 and x < 20:
    print("x is between 10 and 20")
```

Entrambe le forme sono corrette, ma i confronti concatenati si leggono in modo più naturale e somigliano più a come lo scriveresti nella lezione di matematica.

## Istruzioni if Annidate

Un **`if` annidato** è un'istruzione `if` posizionata dentro il corpo di un altro `if`.
Usa l'annidamento quando devi controllare una seconda condizione solo dopo che una prima è già `True`:

```python
is_member = True
age = 14

if is_member:
    if age >= 13:
        print("Full member access!")
    else:
        print("Junior member access!")
else:
    print("Please sign up first.")
```

Mantieni l'annidamento a un massimo di due livelli — il codice annidato troppo in profondità diventa difficile da leggere velocemente.

## if/elif/else con Turtle: Disegna Forme Diverse

Ora usiamo le diramazioni per far disegnare alla turtle forme diverse in base a una variabile.
Il programma qui sotto dovrebbe disegnare una forma diversa in base al valore di `shape_choice` — ma la catena `elif` è incompleta.

!!! mascot-thinking "Tocca a Te — Completa la Catena elif"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma controlla `shape_choice` e disegna un quadrato quando è uguale a `"square"`.
    Aggiungi **altri due blocchi elif** così che `"triangle"` disegni un triangolo (3 lati, svolte di 120°)
    e `"hexagon"` disegni un esagono (6 lati, svolte di 60°).

<div class="cm-lab">
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
initCmLab('-2', `import turtle
t = turtle.Turtle()
t.speed(3)

shape_choice = "triangle"   # try "square", "triangle", "hexagon"

if shape_choice == "square":
    for i in range(4):
        t.forward(100)
        t.right(90)
# Add elif for "triangle" (3 sides, turn 120 degrees each)

# Add elif for "hexagon" (6 sides, turn 60 degrees each)

else:
    t.write("Unknown shape: " + shape_choice, font=("Arial", 14, "normal"))`);
</script>

Una volta che tutte e tre le forme funzionano, prova a impostare `shape_choice = "circle"` per vedere il ramo else disegnare il messaggio "Unknown shape"!

## Esperimenti

Prova questi cambiamenti ai programmi qui sopra. Per ciascuno, prevedi prima cosa succederà, poi eseguilo per verificare!

1. Nel primo laboratorio, cambia `score = 75` in `score = 92`. **Saprai che ha funzionato quando** il blocco `if score >= 60` viene ancora eseguito ma ora anche `score >= 90` sarebbe `True`.
2. Aggiungi un blocco `elif score == 75: print("Exactly 75!")`. **Saprai che ha funzionato quando** riportare `score` a `75` stampa quel messaggio.
3. Nel laboratorio turtle, aggiungi un blocco `elif shape_choice == "pentagon":` che disegni 5 lati con svolte di 72°. **Saprai che ha funzionato quando** `shape_choice = "pentagon"` disegna un pentagono.
4. Aggiungi `t.pencolor("purple")` solo dentro il ramo del triangolo. **Saprai che ha funzionato quando** il triangolo viene disegnato in viola ma il quadrato resta nero.
5. Prova `shape_choice = "hexagon"`. **Saprai che ha funzionato quando** appare un esagono a sei lati sulla tela.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    I tuoi programmi ora possono prendere decisioni! Conosci i valori booleani, sei operatori di confronto, tre operatori logici, e quattro tipi di diramazione: `if`, `if/else`, catene `elif`, e `if` annidati. Questi sono gli elementi costitutivi di ogni programma interattivo mai scritto. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
