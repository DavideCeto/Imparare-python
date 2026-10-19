---
title: Modulo math e Progetti con la Turtle
description: Usa abs(), round(), math.sqrt(), sin(), cos(), e pi per costruire un'onda sinusoidale ondulata e una gara di tartarughe casuale
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:00:00
version: 0.09
---

# Modulo math e Progetti con la Turtle

Alla fine di questa lezione sarai in grado di:

- Usare le funzioni built-in `abs()` e `round()` per operazioni comuni sui numeri
- Importare e usare `math.sqrt()`, `math.floor()`, `math.ceil()`, `math.sin()`, `math.cos()`, e `math.pi`
- Convertire tra radianti e gradi usando `math.radians()` e `math.degrees()`
- Costruire due progetti completi con la turtle: un disegno di **onda sinusoidale** e una **simulazione di gara di tartarughe**

Il modulo `math` dà a Python superpoteri per lavorare con i numeri — radici quadrate, onde sinusoidali, logaritmi, e altro.
In questo capitolo userai quei superpoteri per creare due bellissimi progetti interattivi con la tartaruga.

!!! mascot-welcome "Benvenuto/a al Capitolo 18!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sapevi che le curve morbide che vedi nei giochi e nelle animazioni sono disegnate con il seno e il coseno?
    Oggi imparerai gli strumenti matematici che lo rendono possibile — e poi disegneremo la nostra onda!
    Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Funzioni Numeriche Built-in

Python ha due utili funzioni numeriche incorporate — nessun import necessario.

`abs(x)` restituisce il **valore assoluto** di un numero: la distanza da zero, sempre positiva.

```python
print(abs(-7))    # 7
print(abs(5))     # 5
print(abs(-3.14)) # 3.14
```

`round(x)` arrotonda un numero all'intero più vicino (o a un numero dato di cifre decimali).

```python
print(round(3.7))      # 4
print(round(3.2))      # 3
print(round(3.14159, 2)) # 3.14
```

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
initCmLab('', `print("abs(-42):", abs(-42))
print("abs(7):", abs(7))

print("round(2.7):", round(2.7))
print("round(2.3):", round(2.3))
print("round(3.14159, 3):", round(3.14159, 3))`);
</script>

## Il Modulo `math`

Importa il modulo con `import math`. Poi accedi alle funzioni usando `math.function_name()`.

Prima di provarle, ecco una guida rapida alle funzioni principali:

| Funzione | Cosa fa | Esempio |
|----------|-------------|---------|
| `math.sqrt(x)` | Radice quadrata di x | `math.sqrt(25)` → 5.0 |
| `math.floor(x)` | Arrotonda in giù all'intero più vicino | `math.floor(3.9)` → 3 |
| `math.ceil(x)` | Arrotonda in su all'intero più vicino | `math.ceil(3.1)` → 4 |
| `math.pi` | La costante π (3.14159...) | |
| `math.sin(x)` | Seno di x (x in **radianti**) | `math.sin(math.pi/2)` → 1.0 |
| `math.cos(x)` | Coseno di x (x in **radianti**) | `math.cos(0)` → 1.0 |
| `math.radians(d)` | Converte i gradi in radianti | `math.radians(180)` → π |
| `math.degrees(r)` | Converte i radianti in gradi | `math.degrees(math.pi)` → 180.0 |
| `math.log(x)` | Logaritmo naturale di x | `math.log(1)` → 0.0 |
| `math.factorial(n)` | n! (fattoriale di n) | `math.factorial(5)` → 120 |

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
initCmLab('-2', `import math

print("sqrt(144):", math.sqrt(144))
print("floor(4.9):", math.floor(4.9))
print("ceil(4.1):", math.ceil(4.1))
print("pi:", math.pi)
print("factorial(6):", math.factorial(6))
print("degrees(pi):", math.degrees(math.pi))`);
</script>

## Seno e Coseno — Radianti vs Gradi

`math.sin()` e `math.cos()` di Python si aspettano il loro input in **radianti**, non in gradi.

Un **radiante** è un modo diverso di misurare gli angoli.
Un cerchio completo = 360° = 2π radianti.
Un mezzo cerchio = 180° = π radianti.

Per convertire: usa `math.radians(degrees)` per andare da gradi → radianti.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `math.sin(math.radians(90))` chiede il seno di 90 gradi.
    In trigonometria, `sin(90°) = 1.0`. Pensi che Python darà la risposta giusta?
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
initCmLab('-3', `import math

print("sin(0°):", math.sin(math.radians(0)))
print("sin(90°):", math.sin(math.radians(90)))
print("sin(180°):", round(math.sin(math.radians(180)), 10))
print("cos(0°):", math.cos(math.radians(0)))
print("cos(90°):", round(math.cos(math.radians(90)), 10))`);
</script>

### Guardalo: Un Angolo, Due Lingue

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La tartaruga parla in gradi, ma `math.sin()` parla in radianti. Prima di
    trascinare il punto arancione sotto, prevedi: **quanti radianti sono mezzo giro
    (180°)?** Trascina il punto lì e controlla la tua risposta!

<iframe src="../../sims/unit-circle-radians/main.html" height="522" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Unit Circle](../../sims/unit-circle-radians/index.md){ .md-button }

Avevi indovinato? Mezzo giro è esattamente **π radianti** (circa 3.14). Guarda la piccola tartaruga al centro — la sua direzione corrisponde sempre all'angolo, e le barre blu e verde mostrano `math.sin()` e `math.cos()` per qualsiasi angolo tu scelga.

## Progetto 1 — Onda Sinusoidale con Turtle

Un'**onda sinusoidale** è l'onda morbida e ripetuta a forma di S che vedi in fisica e musica.

L'idea: avanza attraverso lo schermo da sinistra a destra. Per ogni posizione x, calcola `y = amplitude * sin(x * frequency)`. Sposta la tartaruga a `(x, y)`. Il risultato è un'onda morbida.

Prima di eseguire il codice, nota che:
- `amplitude` controlla quanto è alta l'onda (l'altezza del picco in pixel)
- `frequency` (in realtà un fattore di scala) controlla quanti cicli appaiono nella finestra
- `math.sin()` restituisce sempre un valore tra `-1.0` e `1.0`, quindi moltiplichiamo per `amplitude` per scalarlo

<div class="cm-lab">
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
initCmLab('-4', `import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("royalblue")

amplitude = 80    # altezza dell'onda
frequency = 0.05  # quanto velocemente oscilla

t.penup()
t.goto(-190, 0)
t.pendown()

for x in range(-190, 191):
    y = amplitude * math.sin(x * frequency)
    t.goto(x, y)

t.hideturtle()`);
</script>

Prova a cambiare `amplitude` a `150` per un'onda più alta o `frequency` a `0.1` per un'onda più rapida.

### Guardalo: Suona l'Onda Come uno Strumento

Modificare i numeri e rieseguire funziona, ma gli slider sono più rapidi per costruire l'intuizione. Nell'esploratore sotto, prevedi prima: **quale slider rende l'onda più alta, e quale ne infila più ondulazioni nello stesso spazio?** Poi trascina ogni slider uno alla volta e guarda l'equazione aggiornarsi.

<iframe src="../../sims/sine-wave-explorer/main.html" height="492" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Sine Wave Explorer](../../sims/sine-wave-explorer/index.md){ .md-button }

Seleziona **show plain sin(x)** per mantenere l'onda originale come riferimento punteggiato — poi muovi la fase e guarda la tua onda scorrere a sinistra oltre di essa. Queste sono esattamente le variabili `amplitude` e `frequency` del progetto con la tartaruga sopra.

## Progetto 2 — Simulazione di Gara di Tartarughe

Ora combiniamo `random` e un ciclo `for` per simulare una gara di tartarughe!

Tre tartarughe partono da sinistra e si muovono a destra con salti di lunghezza casuale. La prima ad attraversare x = 150 vince.

Prima del codice: `random.randint(1, 10)` dà a ogni tartaruga una dimensione di passo casuale a ogni turno.
Controlliamo dopo ogni movimento se qualche tartaruga ha attraversato il traguardo.

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

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.penup()
t1.goto(-160, 40)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(-160, 0)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("green")
t3.penup()
t3.goto(-160, -40)

racers = [t1, t2, t3]
names = ["Red", "Blue", "Green"]
finish = 150

while True:
    for i, racer in enumerate(racers):
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= finish:
            print(f"{names[i]} vince!")
            racer.write("Vincitore!", font=("Arial", 12, "bold"))
            turtle.done()
            break
    else:
        continue
    break`);
</script>

Eseguilo più volte — il vincitore cambia ogni volta perché i passi sono casuali!

!!! mascot-tip "Come si Interrompe il Ciclo"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Il pattern `for/else` qui è un trucco di Python: la clausola `else` su un ciclo `for` gira solo se il ciclo è terminato *senza* incontrare un `break`. Quindi se nessuna tartaruga ha attraversato il traguardo in questo giro, continuiamo (`continue`) il ciclo `while True`. Nel momento in cui una tartaruga vince, usciamo (`break`) da entrambi i cicli.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Quarta Corridora"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La gara di tartarughe ha tre corridori. Aggiungi una quarta tartaruga chiamata `t4` con colore `"orange"`,
    che parte da y = `-80`. Aggiungi `"Orange"` alla lista `names` e `t4` alla lista `racers`.
    La gara dovrebbe ora avere quattro concorrenti!

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
import random

t1 = turtle.Turtle()
t1.shape("turtle"); t1.color("red"); t1.penup(); t1.goto(-160, 60)
t2 = turtle.Turtle()
t2.shape("turtle"); t2.color("blue"); t2.penup(); t2.goto(-160, 20)
t3 = turtle.Turtle()
t3.shape("turtle"); t3.color("green"); t3.penup(); t3.goto(-160, -20)

# Aggiungi qui t4 (arancione, che parte da y=-60)

racers = [t1, t2, t3]          # aggiungi t4 anche qui
names = ["Red", "Blue", "Green"]  # aggiungi qui "Orange"
finish = 150

while True:
    for i, racer in enumerate(racers):
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= finish:
            print(f"{names[i]} vince!")
            break
    else:
        continue
    break`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia `amplitude` nell'onda sinusoidale a `40` e `frequency` a `0.1`.
   **Saprai che ha funzionato quando** l'onda è più corta e più rapida.

2. Disegna un'**onda cosinusoidale** sostituendo `math.sin` con `math.cos`.
   **Saprai che ha funzionato quando** l'onda inizia dal suo picco invece che da zero.

3. Disegna due onde sullo stesso canvas — una blu, una rossa, con ampiezze diverse.
   **Saprai che ha funzionato quando** appaiono due onde sovrapposte.

4. Rendi più ampio l'intervallo dei passi della gara di tartarughe: `randint(1, 20)` invece di `randint(1, 10)`.
   **Saprai che ha funzionato quando** la gara finisce più velocemente ma i risultati sono più imprevedibili.

5. Stampa `math.factorial(10)` e `math.log(math.e)`.
   **Saprai che ha funzionato quando** vedi `3628800` e approssimativamente `1.0`.

!!! mascot-celebration "Mago della Matematica!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un'onda sinusoidale e una gara di tartarughe usando vera matematica — davvero impressionante!
    Da qui ci muoviamo verso un Python più avanzato: booleani, collezioni, e gestione degli errori.
    Sei pronto per il livello successivo! Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
