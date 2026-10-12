---
hide:
    - toc
---
# Figura di Lissajous

Alla fine di questo laboratorio sarai in grado di:

- Tracciare una figura di Lissajous usando `x = A*sin(a*t + δ)`, `y = B*sin(b*t)`
- Capire come il rapporto `a:b` controlla il numero di anelli
- Esplorare come cambiare lo spostamento di fase `δ` ruota e rimodella la figura

Le figure di Lissajous sono le curve tracciate da un punto le cui coordinate x e y oscillano sinusoidalmente a frequenze diverse. Appaiono sugli oscilloscopi e nella visualizzazione del suono.

!!! mascot-welcome "Benvenuto alle Figure di Lissajous!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le figure di Lissajous sono chiamate così da Jules Antoine Lissajous, che le studiò nel 1857.
    Appaiono in fisica, musica, e persino nei design dei loghi!
    Programmiamone una insieme!

## Come Funziona

Per ogni passo temporale `t` da 0 a 2π, calcola `x = A * sin(a*t + delta)` e `y = B * sin(b*t)`. Muovere la tartaruga a `(x, y)` traccia la figura. Il rapporto `a/b` determina la forma.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

A, B = 160, 130
a, b = 3, 2
delta = math.pi / 4
steps = 1000

monty.penup()
monty.pencolor('royalblue')
monty.pensize(2)

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = A * math.sin(a * t + delta)
    y = B * math.sin(b * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Con `a=3, b=2` (rapporto 3:2), la figura dovrebbe avere `a` anelli in una direzione e `b` nell'altra.
    Conta gli anelli — quanti ce ne saranno lungo x? Lungo y?
    Fai la tua previsione — poi clicca Esegui per scoprirlo!

## Provalo Ora

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

A, B = 160, 130
a, b = 3, 2
delta = math.pi / 4
steps = 1000

monty.penup()
monty.pencolor('royalblue')
monty.pensize(2)

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = A * math.sin(a * t + delta)
    y = B * math.sin(b * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**3 anelli lungo x, 2 anelli lungo y** — la curva si incrocia in 3 × 2 = 6 punti. Avevi indovinato?

## Come Funziona

`a:b = 3:2` significa che x oscilla 3 volte per ogni 2 oscillazioni di y. Dove `a` e `b` sono interi senza fattore comune, la curva è chiusa. `delta` sposta la fase x — cambiarla da `π/4` a `0` produce una figura a 8, mentre `π/2` produce una forma simile a un'ellisse.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `A, B = 160, 130` | Ampiezza (dimensione) in x e y |
| `a, b = 3, 2` | Rapporto di frequenza — controlla il numero di anelli |
| `delta = math.pi / 4` | Spostamento di fase — ruota la figura |
| `A * math.sin(a * t + delta)` | x oscilla alla frequenza `a` |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Rapporto"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `a, b = 3, 2` in `a, b = 5, 4`. Quanti incroci appariranno?
    La formula è: incroci = a × b. Prevedilo, poi esegui!

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

A, B = 160, 130
a, b = 5, 4
delta = math.pi / 4
steps = 1000

monty.penup()
monty.pencolor('crimson')
monty.pensize(2)

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = A * math.sin(a * t + delta)
    y = B * math.sin(b * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

`a=5, b=4` → 5×4 = 20 incroci — una figura molto più complessa e ornata.

## Esperimenti

1. **Prova a=1, b=1.** Imposta anche `delta=0`. Il risultato dovrebbe essere una linea diagonale (caso degenere). Prova `delta=pi/2` per un'ellisse. Saprai che ha funzionato quando appare una forma semplice.

2. **Disegna più figure.** Usa un ciclo su valori diversi di `a` e `b` con colori diversi. Saprai che ha funzionato quando più figure di Lissajous si sovrappongono.

3. **Anima la fase.** In un ciclo, aumenta `delta` lentamente e ridisegna. Saprai che ha funzionato quando la figura sembra ruotare.

4. **Prova rapporti non interi.** Usa `a, b = 3, 2.1`. La figura non si chiuderà del tutto — precederà lentamente. Saprai che ha funzionato quando la curva riempie una regione invece di formare un anello chiuso.

!!! mascot-celebration "Arte da Oscilloscopio!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato una figura di Lissajous — gli stessi pattern che appaiono sugli oscilloscopi
    quando due onde sinusoidali vengono inviate agli ingressi x e y!
    Prossimo: **Curva a Rosa** — petali da una singola equazione polare.
