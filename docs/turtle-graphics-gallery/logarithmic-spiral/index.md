---
hide:
    - toc
---
# Spirale Logaritmica Colorata

Alla fine di questo laboratorio sarai in grado di:

- Usare `math.cos()` e `math.sin()` per convertire coordinate polari in posizioni cartesiane `(x, y)`
- Disegnare una curva tracciando molti punti con `goto()` invece di usare `forward()` e `right()`
- Colorare ogni segmento in base alla sua posizione angolare usando `angle % 360` per scorrere tra le tonalità

Una spirale lisciata e continuamente curva — nessun segmento retto o angolo. Ogni rivoluzione della spirale è colorata scorrendo attraverso rosso, arancione, giallo, verde, blu, e viola, così i bracci brillano come un nastro arcobaleno.

!!! mascot-welcome "Benvenuto alla Spirale Logaritmica!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Finora, ogni spirale era fatta di segmenti di linea retta. Questa è diversa —
    usiamo funzioni matematiche per calcolare posizioni esatte, dando una curva veramente lisciata.
    Programmiamo insieme!

## Come Funziona

Una spirale logaritmica in coordinate polari è `r = a · e^(b·θ)` — il raggio cresce esponenzialmente mentre l'angolo aumenta. Convertiamo ogni punto polare `(r, θ)` in cartesiano `(x, y)` usando:

```
x = r · cos(θ)
y = r · sin(θ)
```

Poi `goto(x, y)` muove la tartaruga a quel punto. Con piccoli passi angolari e la penna abbassata, questo traccia una curva lisciata.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
a = 0.5
b = 0.15

monty.penup()
for i in range(600):
    theta = i * 0.05
    r = a * math.exp(b * theta)
    x = r * math.cos(theta) * 30
    y = r * math.sin(theta) * 30
    monty.goto(x, y)
    hue_index = int(math.degrees(theta) % 360 / 60)
    monty.pencolor(colors[hue_index])
    monty.pendown()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Moltiplichiamo `r` per 30 per scalare la spirale e farla entrare nel canvas.
    La spirale sembrerà lisciata o frastagliata? (Ogni passo è di solo 0,05 radianti.)
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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
a = 0.5
b = 0.15

monty.penup()
for i in range(600):
    theta = i * 0.05
    r = a * math.exp(b * theta)
    x = r * math.cos(theta) * 30
    y = r * math.sin(theta) * 30
    monty.goto(x, y)
    hue_index = int(math.degrees(theta) % 360 / 60)
    monty.pencolor(colors[hue_index])
    monty.pendown()`);
</script>

**Lisciata** — ogni passo di 0,05 radianti è abbastanza piccolo che l'occhio non può rilevare i singoli segmenti di linea. Avevi indovinato?

## Come Funziona

`math.exp(b * theta)` è la funzione esponenziale — il raggio cresce lentamente all'inizio e accelera verso l'esterno. Moltiplicare per `30` scala il risultato per riempire il canvas. `math.degrees(theta) % 360` converte i radianti in gradi e usa il modulo per scorrere tra 0–360 non importa quante rivoluzioni abbiamo fatto.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `theta = i * 0.05` | Angolo in radianti; 0,05 rad per passo per la fluidità |
| `r = a * math.exp(b * theta)` | Il raggio cresce esponenzialmente — formula della spirale logaritmica |
| `x = r * math.cos(theta) * 30` | Converte polare in x cartesiano, scalato al canvas |
| `y = r * math.sin(theta) * 30` | Converte polare in y cartesiano, scalato al canvas |
| `math.degrees(theta) % 360 / 60` | Mappa l'angolo a un indice di colore: un colore ogni 60° |

!!! mascot-tip "Coordinate Polari e Cartesiane"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Le coordinate **polari** descrivono un punto con `(r, θ)` — distanza dall'origine e angolo.
    Le coordinate **cartesiane** usano `(x, y)` — distanze orizzontale e verticale.
    Convertire tra le due è uno dei trucchi più utili nella grafica computazionale!

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna una linea retta invece di una spirale — il raggio non cambia mai!
    Trova e correggi il bug.

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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
a = 0.5
b = 0.15

monty.penup()
for i in range(600):
    theta = i * 0.05
    r = a
    x = r * math.cos(theta) * 30
    y = r * math.sin(theta) * 30
    monty.goto(x, y)
    hue_index = int(math.degrees(theta) % 360 / 60)
    monty.pencolor(colors[hue_index])
    monty.pendown()`);
</script>

Cambia `r = a` in `r = a * math.exp(b * theta)` — senza la crescita esponenziale, il raggio resta costante e la tartaruga traccia un cerchio a raggio fisso invece di una spirale.

## Esperimenti

1. **Falla crescere più velocemente.** Cambia `b = 0.15` in `b = 0.25`. La spirale si allarga molto più velocemente. Saprai che ha funzionato quando meno rivoluzioni entrano sul canvas.

2. **Falla crescere più lentamente.** Cambia `b = 0.15` in `b = 0.07`. Più rivoluzioni si compattano strettamente insieme. Saprai che ha funzionato quando i bracci sono molto più vicini tra loro.

3. **Rimuovi il colore.** Sostituisci la riga `pencolor()` con `monty.pencolor('black')`. Saprai che ha funzionato quando la spirale è un'unica curva nera pulita.

4. **Raddoppia la risoluzione.** Cambia `i * 0.05` in `i * 0.025` e `range(600)` in `range(1200)`. La curva diventa ancora più lisciata. Saprai che ha funzionato quando non riesci a vedere nessun angolo.

!!! mascot-celebration "Matematico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato `math.cos()` e `math.sin()` — la base di tutta la grafica computerizzata —
    per convertire coordinate polari in posizioni di pixel. Così funzionano i videogiochi, le mappe,
    e le simulazioni per posizionare oggetti nello spazio!
    Prossimo: **Spirale a Doppia Elica** — due spirali interlacciate in un singolo ciclo.
