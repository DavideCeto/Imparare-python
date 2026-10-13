---
hide:
    - toc
---
# Astroide

Alla fine di questo laboratorio sarai in grado di:

- Tracciare l'astroide usando la sua forma parametrica `x = R*cos³(t)`, `y = R*sin³(t)`
- Disegnare una famiglia di segmenti di linea in stile "string art" il cui inviluppo è l'astroide
- Spiegare cos'è l'*inviluppo* di una curva e come una scala che scivola lungo un muro ne traccia uno

L'astroide è una stella a quattro cuspidi — il percorso tracciato da un punto su un piccolo cerchio che rotola dentro un cerchio quattro volte più grande (un'ipocicloide, cugina dello Spirografo). Nasconde un bellissimo segreto: se una scala scivola giù lungo un muro, le posizioni della scala delineano l'astroide. Disegneremo sia la stella che i "fili" scorrevoli che la rivelano.

!!! mascot-welcome "Benvenuto all'Astroide!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Eleva al cubo un coseno, eleva al cubo un seno — ottieni una stella a
    quattro punte! Poi sovrapporremo il classico string art: decine di
    linee rette che delineano magicamente la stessa stella curva. Nessuna
    curva viene disegnata dai fili, eppure la stella appare. Pronto?

## Come Funziona

Prima il string art: disegna segmenti rettilinei da `(R*cos(a), 0)` sull'asse x a `(0, R*sin(a))` sull'asse y. Ogni segmento soddisfa `a² + b² = R²` — come una scala di lunghezza fissa `R` che scivola giù lungo un muro. Poi la stella stessa: per `t` da 0 a 2π, traccia `x = R * cos(t)**3` e `y = R * sin(t)**3`. L'elevazione al cubo tira i punti verso gli assi, stringendo il cerchio in quattro cuspidi acute — e quella curva è esattamente l'*inviluppo* che i fili delineano.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 170

monty.pencolor('silver')
monty.pensize(1)
n_lines = 40
for i in range(n_lines + 1):
    a = 2 * math.pi * i / n_lines
    monty.penup()
    monty.goto(R * math.cos(a), 0)
    monty.pendown()
    monty.goto(0, R * math.sin(a))

monty.pencolor('crimson')
monty.pensize(3)
steps = 400
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = R * math.cos(t) ** 3
    y = R * math.sin(t) ** 3
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La stella nasce da `cos(t)**3` e `sin(t)**3`.
    Quante punte acute (cuspidi) avrà? Conta i punti dove coseno o seno
    raggiungono 1 o -1... fai la tua ipotesi, poi clicca Esegui!

## Prova Ora

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 170

monty.pencolor('silver')
monty.pensize(1)
n_lines = 40
for i in range(n_lines + 1):
    a = 2 * math.pi * i / n_lines
    monty.penup()
    monty.goto(R * math.cos(a), 0)
    monty.pendown()
    monty.goto(0, R * math.sin(a))

monty.pencolor('crimson')
monty.pensize(3)
steps = 400
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = R * math.cos(t) ** 3
    y = R * math.sin(t) ** 3
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**4 cuspidi** — una su ogni asse, a `(±R, 0)` e `(0, ±R)`, esattamente dove coseno o seno raggiungono ±1. Avevi indovinato?

## Come Funziona

Nessuno dei segmenti argentei è curvo, eppure insieme delineano la stella. Ogni segmento è *tangente* all'astroide — bacia la curva in esattamente un punto senza attraversarla. Una curva che ogni membro di una famiglia di linee tocca in questo modo si chiama l'**inviluppo** della famiglia. L'immagine della scala scorrevole spiega la fisica: mentre una scala di lunghezza `R` scivola da verticale a orizzontale, la sua sezione centrale spazza la regione sotto la curva, ma il suo confine esterno — il punto più lontano che la scala raggiunge mai — è l'astroide. I cubi in `cos³` e `sin³` derivano dall'algebra dell'angolo doppio di un cerchio di raggio `R/4` che rotola dentro un cerchio di raggio `R`.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `x = R * math.cos(t) ** 3` | La forma parametrica dell'astroide — elevare al cubo stringe il cerchio in cuspidi |
| `monty.goto(R * math.cos(a), 0)` | Un'estremità della "scala" sull'asse x |
| `monty.goto(0, R * math.sin(a))` | L'altra estremità sull'asse y — le due estremità soddisfano sempre a² + b² = R² |
| `n_lines = 40` | Quante posizioni della scala disegnare; più linee creano un inviluppo più liscio |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Questo programma dovrebbe disegnare la stella a quattro punte — ma
    disegna invece una semplice linea retta! Guarda bene gli esponenti.
    Trova il bug e correggilo così la stella appare.

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 170
steps = 400

monty.pencolor('crimson')
monty.pensize(3)
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = R * math.cos(t) ** 2
    y = R * math.sin(t) ** 2
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

Gli esponenti dicono `** 2` invece di `** 3`. I quadrati non sono mai negativi, e poiché `cos² + sin² = 1` ogni punto atterra sulla linea retta `x + y = R` — cambia entrambi gli esponenti in `3` e la stella ritorna.

## Esperimenti

1. **Usa più fili.** Cambia `n_lines = 40` in `n_lines = 120`. Saprai che ha funzionato quando la ragnatela argentea diventa così densa che l'inviluppo sembra una curva grigia liscia.

2. **Prova un'ipocicloide diversa.** Sostituisci la `x` e la `y` del ciclo della stella con `x = R * (0.667 * math.cos(t) + 0.333 * math.cos(2 * t))` e `y = R * (0.667 * math.sin(t) - 0.333 * math.sin(2 * t))`. Saprai che ha funzionato quando appare invece una stella a tre cuspidi (il deltoide).

3. **Colora i quadranti.** Prima di disegnare ogni filo, imposta il colore della penna in base a `i` (per esempio argento per `i < 10`, azzurro chiaro per `i < 20`, e così via). Saprai che ha funzionato quando il ventaglio di fili di ogni quadrante ha il proprio colore.

4. **Eleva al cubo di più.** Cambia entrambi i `** 3` in `** 5`. Saprai che ha funzionato quando le braccia della stella diventano ancora più sottili e le cuspidi più acute — potenze dispari più alte stringono di più.

!!! mascot-celebration "Stella della Galleria!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai disegnato una curva in due modi contemporaneamente: direttamente
    da cos³ e sin³, e come inviluppo di quaranta linee rette — e
    combaciavano perfettamente. Questa è matematica vera resa visibile.
    Esplora la **Galleria di Grafica Turtle** per la tua prossima sfida!
