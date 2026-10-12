---
hide:
    - toc
---
# Stella Epicicloidale

Alla fine di questo laboratorio sarai in grado di:

- Tracciare un epicicloide usando `x = (R+r)cos(t) - r*cos((R+r)/r * t)`
- Capire come `R/r` (un intero) dà il numero di cuspidi
- Confrontare epicicloidi (rotolamento esterno) con ipotrocoidi (rotolamento interno)

Un epicicloide è tracciato da un punto su un piccolo cerchio che rotola attorno all'esterno di un cerchio più grande. Quando `R/r` è un numero intero, il risultato è una forma simile a una stella con esattamente `R/r` cuspidi a punta.

!!! mascot-welcome "Benvenuto alla Stella Epicicloidale!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Mentre lo Spirografo rotola un cerchio all'interno, l'epicicloide rotola un cerchio all'esterno!
    Quando il rapporto è un numero intero, il risultato è una perfetta forma a stella.
    Programmiamo insieme!

## Come Funziona

`x = (R + r)*cos(t) - r*cos((R+r)/r * t)`
`y = (R + r)*sin(t) - r*sin((R+r)/r * t)`

`R` è il raggio del cerchio base, `r` è il raggio del cerchio rotolante. Quando `R/r = k` (un intero), la curva ha `k` cuspidi.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 100
r = 20
steps = 2000
colors = ['crimson', 'darkorange', 'gold', 'forestgreen', 'royalblue']

monty.pencolor('crimson')
monty.pensize(2)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R + r) * math.cos(t) - r * math.cos((R + r) / r * t)
    y = (R + r) * math.sin(t) - r * math.sin((R + r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `R/r = 100/20 = 5` (un intero). La regola dice che otteniamo `R/r` cuspidi — quante sono?
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

R = 100
r = 20
steps = 2000

monty.pencolor('crimson')
monty.pensize(2)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R + r) * math.cos(t) - r * math.cos((R + r) / r * t)
    y = (R + r) * math.sin(t) - r * math.sin((R + r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**5 cuspidi a punta** — una stella epicicloidale a 5 punte. Avevi indovinato?

## Come Funziona

Ogni cuspide si forma quando il punto di contatto del cerchio rotolante si ferma momentaneamente (la velocità del punto è uguale a zero). Questo accade `R/r` volte per rivoluzione. A ogni arresto, la curva forma una punta netta verso l'esterno — una cuspide.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `R = 100, r = 20` | R/r = 5 → 5 cuspidi |
| `(R + r) * cos(t)` | Posizione del centro del cerchio rotolante |
| `r * cos((R+r)/r * t)` | Punto sul cerchio rotolante |
| `(R+r)/r * t` | Angolo di rotazione proprio del cerchio rotolante |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia a 7 Cuspidi"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `r = 20` per far sì che `R/r = 7`. Quale valore di `r` dà 7 cuspidi da R=100?
    Suggerimento: 100 / r = 7, quindi r = ?

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

R = 105
r = 15
steps = 2000

monty.pencolor('royalblue')
monty.pensize(2)
monty.penup()

for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R + r) * math.cos(t) - r * math.cos((R + r) / r * t)
    y = (R + r) * math.sin(t) - r * math.sin((R + r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

`R=105, r=15` → `R/r = 7` → 7 cuspidi. Una stella epicicloidale a 7 punte!

## Esperimenti

1. **Prova un rapporto non intero.** Usa `R=100, r=30`. La curva non si chiuderà in una rivoluzione. Saprai che ha funzionato quando appare una forma ad anelli irregolare.

2. **Disegna una cardioide.** Usa `R=80, r=80` (rapporto 1:1). Una cardioide ha solo una cuspide e sembra un cuore. Saprai che ha funzionato quando appare una cuspide.

3. **Sovrapponi più epicicloidi.** Usa `R=100` e cicla sui valori di `r` 10, 20, 25, 50 con colori diversi. Saprai che ha funzionato quando 4 forme di stella diverse si sovrappongono.

4. **Confronta ipo contro epi.** Disegna sia un ipotrocoide (Spirografo) sia un epicicloide sullo stesso canvas. Saprai che ha funzionato quando entrambi i tipi di curva appaiono insieme.

!!! mascot-celebration "Stelle da Cerchi Rotolanti!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito una famiglia di curve a stella dalla geometria dei cerchi rotolanti!
    Questi epicicloidi appaiono nei sistemi di ingranaggi planetari e nel design dei motori rotativi.
    Prossimo: **Categoria 8 — Illusioni Ottiche!**
