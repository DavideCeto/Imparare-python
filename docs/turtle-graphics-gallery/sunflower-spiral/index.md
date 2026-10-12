---
hide:
    - toc
---
# Spirale dei Semi di Girasole

Alla fine di questo laboratorio sarai in grado di:

- Usare l'angolo d'oro (≈ 137,5°) per posizionare punti in un pattern a spirale di girasole
- Capire perché l'angolo d'oro produce un impacchettamento ottimale
- Calcolare le posizioni dei punti usando `r = sqrt(n)` e angolo `n * 137,5°`

I semi in una vera testa di girasole sono disposti dall'angolo d'oro — 137,508°. Questo laboratorio riproduce esattamente quella spirale. Lo stesso impacchettamento appare nelle pigne, negli ananas, e nei carciofi.

!!! mascot-welcome "Benvenuto al Girasole!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I girasoli hanno scoperto l'angolo d'oro milioni di anni prima dei matematici.
    Impacchetta il maggior numero di semi nel minor spazio — l'algoritmo di impacchettamento ottimale della natura!
    Programmiamo insieme!

## Come Funziona

Il seme `n` è posizionato a coordinate polari `r = scale * sqrt(n)`, angolo `n * golden_angle`. Convertendo in x, y: `x = r * cos(angle)`, `y = r * sin(angle)`. I colori scorrono attraverso una tavolozza solare per ogni "braccio" della spirale.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

golden_angle = 137.508
scale = 8
colors = ['gold', 'darkorange', 'goldenrod', 'orange']

for n in range(200):
    angle = math.radians(n * golden_angle)
    r = scale * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    size = max(2, 8 - r / 20)
    monty.dot(int(size), colors[n % len(colors)])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    200 punti posizionati uno alla volta, ognuno ruotato esattamente di 137,5° dal precedente.
    Formeranno una spirale, una griglia, o qualcosa che sembra un vero girasole?
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

golden_angle = 137.508
scale = 8
colors = ['gold', 'darkorange', 'goldenrod', 'orange']

for n in range(200):
    angle = math.radians(n * golden_angle)
    r = scale * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    size = max(2, 8 - r / 20)
    monty.dot(int(size), colors[n % len(colors)])`);
</script>

Un **vero pattern di girasole** — puoi vedere le spirali in senso orario e antiorario per cui i girasoli sono famosi. Avevi indovinato?

## Come Funziona

`math.sqrt(n)` per il raggio distribuisce i semi uniformemente verso l'esterno — senza di esso tutti i semi si raggrupperebbero vicino al bordo. L'angolo d'oro 137,508° è l'angolo più "irrazionale" possibile, significando che nessun seme atterra mai direttamente davanti a uno precedente. Questo garantisce la massima diffusione e il minimo spazio sprecato.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `golden_angle = 137.508` | L'angolo d'oro — crea un impacchettamento ottimale |
| `r = scale * math.sqrt(n)` | Distribuisce i semi verso l'esterno a un ritmo uniforme |
| `x = r * math.cos(angle)` | Converte polare → coordinata x |
| `y = r * math.sin(angle)` | Converte polare → coordinata y |
| `size = max(2, 8 - r/20)` | Punti più grandi al centro, più piccoli al bordo |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova un Angolo Diverso"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `golden_angle = 137.508` in `golden_angle = 138`.
    Prevedi cosa succederà all'impacchettamento — migliore o peggiore dell'angolo d'oro?
    Eseguilo per confrontare!

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

golden_angle = 138.0
scale = 8
colors = ['royalblue', 'deepskyblue', 'steelblue', 'lightblue']

for n in range(200):
    angle = math.radians(n * golden_angle)
    r = scale * math.sqrt(n)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    size = max(2, 8 - r / 20)
    monty.dot(int(size), colors[n % len(colors)])`);
</script>

A 138°, i semi si raggruppano in raggi radiali — l'impacchettamento è peggiore di 137,508°! L'angolo d'oro è davvero speciale: anche un piccolo cambiamento produce un raggruppamento visibile.

## Esperimenti

1. **Prova 90°.** Cambia in `golden_angle = 90`. Saprai che ha funzionato quando appaiono solo 4 raggi (ogni 4° seme atterra nella stessa direzione).

2. **Usa 400 semi.** Cambia `range(200)` in `range(400)`. Saprai che ha funzionato quando la spirale si estende molto più lontano e sembra più densa.

3. **Usa un colore singolo.** Sostituisci la lista dei colori con solo `'forestgreen'`. Saprai che ha funzionato quando tutti i punti sono dello stesso colore.

4. **Prova l'angolo esatto della sezione aurea.** La sezione aurea φ ≈ 1,618; l'angolo d'oro = 360° × (1 − 1/φ) ≈ 222,5°. Prova questo valore e vedi se differisce da 137,508°.

!!! mascot-celebration "L'Algoritmo della Natura!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato lo stesso algoritmo di impacchettamento che la natura usa in girasoli, pigne, e galassie!
    L'angolo d'oro appare ovunque in biologia perché massimizza l'efficienza delle risorse.
    Prossimo: **Ragnatela** — anelli concentrici collegati da fili radiali.
