---
hide:
    - toc
---
# Curva a Rosa

Alla fine di questo laboratorio sarai in grado di:

- Tracciare una curva a rosa usando `r = cos(k * theta)` in coordinate polari
- Capire come un `k` dispari dà `k` petali e un `k` pari dà `2k` petali
- Convertire polare `(r, theta)` in cartesiano `(x, y)` per il tracciamento

Una curva simile a un fiore fatta dalla semplice equazione `r = cos(k*θ)`. Cambiare `k` cambia il conteggio dei petali — un `k` dispari dà `k` petali, un `k` pari dà `2k` petali.

!!! mascot-welcome "Benvenuto alla Curva a Rosa!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Un'equazione breve produce questi pattern a petalo: `r = cos(k * theta)`.
    La matematica nella sua forma più bella — un intero fiore da tre caratteri!
    Programmiamo insieme!

## Come Funziona

Per theta da 0 a 2π (o 4π per k pari), calcola `r = scale * cos(k * theta)`. Converti in cartesiano: `x = r * cos(theta)`, `y = r * sin(theta)`. Collega i punti per tracciare i petali.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

k = 5
scale = 140
steps = 1000
colors = ['crimson', 'darkorange', 'gold', 'forestgreen', 'royalblue']

for petal in range(k):
    monty.pencolor(colors[petal % len(colors)])
    monty.penup()
    monty.pensize(2)

monty.pencolor('crimson')
monty.penup()
for i in range(steps + 1):
    theta = 2 * math.pi * i / steps
    r = scale * math.cos(k * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Con `k=5` (dispari), la regola dice che otteniamo `k` petali. Quanti petali sono?
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

k = 5
scale = 140
steps = 1000

monty.pencolor('crimson')
monty.pensize(2)
monty.penup()
for i in range(steps + 1):
    theta = 2 * math.pi * i / steps
    r = scale * math.cos(k * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**5 petali** — un k dispari dà esattamente k petali. Avevi indovinato?

## Come Funziona

Quando `cos(k*theta) < 0`, `r` è negativo, che in coordinate polari posiziona il punto 180° opposto. Questo ripassa attraverso il centro creando le forme a petalo. Per un `k` pari, la riflessione a 180° crea un insieme aggiuntivo di petali.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `r = scale * math.cos(k * theta)` | Equazione polare della curva a rosa |
| `x = r * math.cos(theta)` | Converte r, theta polari in x |
| `y = r * math.sin(theta)` | Converte r, theta polari in y |
| `k = 5` | Dispari: 5 petali; prova k=4 per 8 petali |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova k=4 (pari)"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `k = 5` in `k = 4`. Un k pari dà 2k petali — quindi quanti petali appariranno?
    Cambia anche l'intervallo in `range(steps * 2)` e dividi per `steps * 2` per k pari.
    Prevedi, poi eseguilo!

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

k = 4
scale = 130
steps = 2000

monty.pencolor('royalblue')
monty.pensize(2)
monty.penup()
for i in range(steps + 1):
    theta = 4 * math.pi * i / steps
    r = scale * math.cos(k * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

`k=4` → 8 petali (2×4). Le curve a rosa con k pari hanno bisogno che theta vada da 0 a 4π per completare tutti i petali.

## Esperimenti

1. **Prova k=3.** Saprai che ha funzionato quando 3 petali appaiono in una disposizione a triangolo.

2. **Usa `sin` invece di `cos`.** Sostituisci `math.cos(k * theta)` con `math.sin(k * theta)`. Saprai che ha funzionato quando i petali ruotano di 90°/k.

3. **Disegna tutti i k dispari da 1 a 9.** Usa un ciclo e colori diversi. Saprai che ha funzionato quando appaiono 5 curve a rosa sovrapposte.

4. **Riempi i petali.** Chiama `begin_fill()` ed `end_fill()` attorno al ciclo di disegno. Saprai che ha funzionato quando i petali sono riempiti.

!!! mascot-celebration "Fiorendo con la Matematica!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Un'equazione — `r = cos(k*theta)` — disegna tutti questi pattern floreali!
    Questa è la bellezza delle coordinate polari: forme complesse da equazioni semplici.
    Prossimo: **Spirografo** — cerchi che rotolano dentro cerchi.
