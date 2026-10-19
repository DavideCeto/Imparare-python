---
title: Funzioni con Parametri e Scope
description: Impara a usare i valori predefiniti dei parametri, gli argomenti keyword, e a capire lo scope delle variabili nelle funzioni Python
generated_by: claude skill chapter-content-generator
date: 2026-06-28 11:55:00
version: 0.09
---

# Funzioni con Parametri e Scope

Alla fine di questa lezione sarai in grado di:

- Scrivere funzioni con **valori predefiniti dei parametri** così che funzionino anche quando chi le chiama salta un argomento
- Usare gli **argomenti keyword** per rendere le chiamate di funzione più facili da leggere
- Spiegare la differenza tra scope **locale** e **globale**
- Identificare se una funzione è **pura** oppure ha **effetti collaterali**

Sai già come definire una funzione e chiamarla.
Ora rendiamo le funzioni ancora più potenti dando loro input più intelligenti e capendo dove vivono le variabili.

!!! mascot-welcome "Benvenuto/a al Capitolo 11!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le funzioni con parametri sono come ordinare da un menu — dici cosa vuoi e la cucina fa il lavoro.
    Oggi renderemo le nostre funzioni ancora più intelligenti dando loro scelte *predefinite*!
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Valori Predefiniti dei Parametri

Un **valore predefinito del parametro** è un valore che la funzione usa automaticamente se chi la chiama non ne fornisce uno.

Scrivi il valore predefinito subito dopo il segno `=` nella definizione della funzione.
Se chi chiama passa un numero, viene usato quel numero. Se no, la funzione ricade sul valore predefinito.

Ecco un esempio. La funzione `draw_square` ha un parametro `size` che per default è `100`.
Chiamare `draw_square()` senza argomenti disegna un quadrato largo 100 passi.
Chiamare `draw_square(50)` disegna un quadrato più piccolo.

```python
import turtle
t = turtle.Turtle()
t.speed(6)

def draw_square(size=100):
    for i in range(4):
        t.forward(size)
        t.right(90)

draw_square(50)    # quadrato piccolo
t.penup()
t.goto(120, 0)
t.pendown()
draw_square()      # usa il valore predefinito: size = 100
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ci sono due chiamate a `draw_square()` — una con un argomento e una senza.
    Quale quadrato pensi che sarà più grande? Fai la tua previsione, poi clicca Esegui!

<div class="cm-lab">
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
initCmLab('', `import turtle
t = turtle.Turtle()
t.speed(6)

def draw_square(size=100):
    for i in range(4):
        t.forward(size)
        t.right(90)

draw_square(50)    # quadrato piccolo
t.penup()
t.goto(120, 0)
t.pendown()
draw_square()      # usa il valore predefinito: size = 100`);
</script>

Avevi indovinato? Il primo quadrato (size 50) è più piccolo. Il secondo usa la size predefinita di 100.

| Riga | Cosa fa |
|------|-------------|
| `def draw_square(size=100):` | Definisce `draw_square` — se salti l'argomento, `size` è 100 |
| `draw_square(50)` | Chiama con size = 50 |
| `draw_square()` | Chiama senza argomento — usa la size predefinita = 100 |

**Regola:** i parametri *con* valori predefiniti devono venire **dopo** qualsiasi parametro *senza* valori predefiniti.

## Argomenti Keyword

Quando chiami una funzione, Python normalmente associa gli argomenti per posizione.
Ma puoi anche usare il *nome* del parametro quando la chiami.
Questo si chiama **argomento keyword** — scrivi `nome=valore` nella chiamata.

Il grande vantaggio: puoi metterli in qualsiasi ordine.

La funzione sotto disegna un poligono colorato. Ha tre parametri: `sides`, `size`, e `color`.
Guarda come gli argomenti keyword fanno leggere la chiamata come inglese semplice:

```python
import turtle
t = turtle.Turtle()
t.speed(6)

def draw_polygon(sides=4, size=80, color="blue"):
    t.pencolor(color)
    for i in range(sides):
        t.forward(size)
        t.right(360 / sides)

draw_polygon(sides=6, color="red", size=60)
```

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
t.speed(6)

def draw_polygon(sides=4, size=80, color="blue"):
    t.pencolor(color)
    for i in range(sides):
        t.forward(size)
        t.right(360 / sides)

draw_polygon(sides=6, color="red", size=60)`);
</script>

La chiamata usa `color` prima di `size`, ma va bene — gli argomenti keyword possono andare in qualsiasi ordine.
Prova a cambiare `sides=6` in `sides=3` per disegnare un triangolo, o cambia `color="red"` con qualsiasi colore preferisci.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, i blocchi personalizzati hanno campi di input etichettati — compili "size" o "color" per nome.
    Gli argomenti keyword di Python funzionano allo stesso modo!
    `draw_polygon(color="red")` è come compilare il campo "color" in un blocco Scratch.

## Scope Locale e Scope Globale

Lo **scope** descrive dove Python può vedere una variabile.

Una variabile creata *dentro* una funzione ha **scope locale**.
Esiste solo mentre la funzione gira. Quando la funzione finisce, quella variabile scompare.

Una variabile creata *fuori* da qualsiasi funzione ha **scope globale**.
Esiste per tutto il programma.

L'esempio sotto mostra entrambi. Una funzione può *leggere* una variabile globale, ma la variabile locale dentro la funzione è invisibile da fuori.

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
initCmLab('-3', `name = "Monty"   # variabile globale

def greet():
    greeting = "Hello"  # variabile locale
    print(greeting + ", " + name + "!")

greet()
# Togli il commento alla riga seguente per vedere un NameError:
# print(greeting)
print("name vale:", name)`);
</script>

| Variabile | Dove definita | Visibile dentro `greet()`? | Visibile fuori `greet()`? |
|----------|--------------|--------------------------|---------------------------|
| `name` | Fuori (globale) | Sì | Sì |
| `greeting` | Dentro `greet()` (locale) | Sì | No — NameError! |

### Guardalo: Stanze per le Variabili

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nel programma **Shadowing Bug** sotto, una funzione imposta `score = 99` mentre
    lo `score` globale è 10. Dopo che la funzione finisce, cosa mostrerà
    `print(score)` — 99 o 10? Fai la tua previsione, poi esegui passo passo
    e guarda le stanze!

<iframe src="../../sims/scope-inspector/main.html" height="512" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Scope Inspector](../../sims/scope-inspector/index.md){ .md-button }

Guarda come la stanza della Funzione appare quando inizia una chiamata e **svanisce al return, portandosi via le sue variabili**. Poi esegui **The global Fix** per vedere l'unico caso in cui una funzione scrive direttamente nella stanza Globale.

## La Parola Chiave `global`

Per default, una funzione può *leggere* una variabile globale ma non può *cambiarla*.

Se vuoi che una funzione aggiorni una variabile globale, usa la **parola chiave `global`** per dire a Python la tua intenzione.

La parola chiave `global score` dentro la funzione dice a Python: "Intendo lo `score` che vive fuori, non uno locale nuovo."

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
initCmLab('-4', `score = 0   # punteggio globale

def add_points(n):
    global score   # usa lo score GLOBALE, non uno nuovo locale
    score = score + n

add_points(10)
add_points(5)
print("Punteggio finale:", score)`);
</script>

Senza la riga `global score`, Python creerebbe una *nuova* variabile locale chiamata `score` e lascerebbe quella globale intatta — che di solito non è quello che vuoi.

## Conflitti di Nomi da Evitare

Se crei una variabile locale con lo *stesso nome* di una variabile globale, quella locale **oscura** (shadow) quella globale dentro quella funzione. Questo può causare bug complicati.

```python
speed = 10   # globale

def reset():
    speed = 0   # crea una NUOVA variabile locale — NON cambia quella globale!
    print("Dentro:", speed)

reset()
print("Fuori:", speed)   # ancora 10!
```

Per stare al sicuro, scegli nomi diversi per le variabili globali e locali — oppure usa `global` se vuoi davvero cambiare il valore globale.

## Costanti per Convenzione

Una **costante** è un valore che non dovrebbe mai cambiare dopo che lo imposti.
Python non lo impone, ma i programmatori seguono una convenzione: scrivere i nomi delle costanti in **MAIUSCOLO** con underscore.

```python
MAX_SPEED = 10
CANVAS_WIDTH = 400
PEN_COLOR = "navy"
```

Il MAIUSCOLO è un segnale per ogni lettore: "Non cambiare questo — trattalo come una regola fissa."

## Scambiare Due Variabili

Ecco un puzzle classico: come scambi i valori di due variabili?

L'approccio *sbagliato* perde dati:

```python
a = 5
b = 10
a = b    # ora a vale 10
b = a    # anche b prende 10 — ops! Il 5 è perso
```

L'approccio *giusto* usa una variabile temporanea:

```python
temp = a   # salva il valore originale di a
a = b      # a prende il valore di b
b = temp   # b prende il valore originale di a
```

Python ha una scorciatoia incorporata che scambia in una riga:

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
initCmLab('-5', `a = 5
b = 10
print("Prima:", a, b)

a, b = b, a   # scorciatoia di Python per lo scambio

print("Dopo: ", a, b)`);
</script>

## Funzioni Pure vs Funzioni con Effetti Collaterali

Una **funzione pura** dà sempre lo stesso output per lo stesso input e non cambia nulla fuori di sé stessa.
Metti dentro lo stesso numero, ottieni sempre lo stesso risultato — come una calcolatrice.

Una funzione con **effetti collaterali** cambia qualcosa fuori di sé stessa, come stampare sullo schermo, modificare una variabile globale, o far disegnare la tartaruga.

```python
# Funzione pura — nessun effetto collaterale, restituisce sempre lo stesso risultato
def square(n):
    return n * n

# Funzione con effetti collaterali — cambia una variabile globale, stampa dell'output
total = 0

def add_to_total(n):
    global total
    total = total + n
    print("Ora il totale è:", total)
```

Le funzioni pure sono più facili da testare perché sono prevedibili.
Gli effetti collaterali non sono una cosa negativa — disegnare con la tartaruga *è* un effetto collaterale — ma sapere quale tipo di funzione stai scrivendo ti aiuta a scrivere codice migliore.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi l'Argomento Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La funzione sotto dovrebbe disegnare un pentagono (5 lati), ma l'argomento keyword `sides` manca dalla chiamata.
    Aggiungi `sides=5` per farlo disegnare un pentagono!

<div class="cm-lab">
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
initCmLab('-6', `import turtle
t = turtle.Turtle()
t.speed(6)

def draw_polygon(sides=4, size=80, color="blue"):
    t.pencolor(color)
    for i in range(sides):
        t.forward(size)
        t.right(360 / sides)

# Aggiungi l'argomento con parola chiave sides per disegnare un pentagono:
draw_polygon(color="green", size=70)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia la size predefinita in `draw_square` da `100` a `150`. Chiama `draw_square()` senza argomenti.
   **Saprai che ha funzionato quando** la tartaruga disegna un quadrato più grande senza che tu passi alcun numero.

2. Aggiungi un quarto parametro `line_width=1` a `draw_polygon` e chiama `t.pensize(line_width)` all'inizio.
   Chiamala con `draw_polygon(sides=3, line_width=5)`.
   **Saprai che ha funzionato quando** il triangolo ha linee visibilmente spesse.

3. Crea una variabile globale `COUNT = 0` e una funzione `increment()` che usa `global COUNT` per aggiungere 1.
   Chiama `increment()` tre volte e `print(COUNT)`.
   **Saprai che ha funzionato quando** vedi `3`.

4. Prova lo scambio *sbagliato* (scrivi `a = b` poi `b = a`) e stampa entrambe le variabili.
   **Saprai che ha funzionato quando** entrambe le variabili mostrano lo stesso valore — dimostrando il bug!

5. Scrivi una funzione pura `cube(n)` che restituisce `n * n * n`.
   Chiamala dentro `print(cube(4))`.
   **Saprai che ha funzionato quando** vedi `64`.

!!! mascot-celebration "Lavoro Fantastico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato a scrivere funzioni più intelligenti con valori predefiniti, argomenti keyword, e scope corretto!
    Queste competenze renderanno ogni funzione che scriverai da ora in poi più flessibile e più facile da leggere per gli altri.
    Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
