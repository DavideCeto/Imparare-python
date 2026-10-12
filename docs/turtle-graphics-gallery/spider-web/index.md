---
hide:
    - toc
---
# Ragnatela

Alla fine di questo laboratorio sarai in grado di:

- Disegnare raggi radiali dal centro usando angoli distanziati di 30°
- Collegare i raggi con anelli poligonali concentrici usando `goto()`
- Combinare due tipi di ciclo (radiale e anulare) per costruire una ragnatela completa

Una ragnatela realistica con 12 fili radiali e 6 anelli concentrici — tutti disegnati con `goto()` usando coordinate polari convertite in x, y.

!!! mascot-welcome "Benvenuto alla Ragnatela!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Una ragnatela usa due idee geometriche: linee radiali e anelli concentrici.
    Questo laboratorio disegna entrambi usando `goto()` e la matematica dei cerchi!
    Programmiamo insieme!

## Come Funziona

**Raggi**: per ciascuno dei 12 angoli (0°, 30°, 60°, … 330°), disegna una linea dal centro al raggio 120.
**Anelli**: per ogni raggio di anello (20, 40, 60, 80, 100, 120), visita tutti i 12 punti di intersezione dei raggi e collegali.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

n_spokes = 12
n_rings = 6
max_r = 120
angles = [i * 360 / n_spokes for i in range(n_spokes)]

monty.pencolor('gray')
monty.pensize(1)

for ang in angles:
    monty.penup()
    monty.goto(0, 0)
    monty.pendown()
    rad = math.radians(ang)
    monty.goto(max_r * math.cos(rad), max_r * math.sin(rad))

for ring in range(1, n_rings + 1):
    r = ring * max_r / n_rings
    monty.penup()
    rad0 = math.radians(angles[0])
    monty.goto(r * math.cos(rad0), r * math.sin(rad0))
    monty.pendown()
    for ang in angles[1:] + [angles[0]]:
        rad = math.radians(ang)
        monty.goto(r * math.cos(rad), r * math.sin(rad))

monty.penup()
monty.goto(0, 0)
monty.pendown()
monty.dot(10, 'black')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Disegniamo 12 raggi e 6 anelli. Quanti lati di poligono avrà ogni anello?
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

n_spokes = 12
n_rings = 6
max_r = 120
angles = [i * 360 / n_spokes for i in range(n_spokes)]

monty.pencolor('gray')
monty.pensize(1)

for ang in angles:
    monty.penup()
    monty.goto(0, 0)
    monty.pendown()
    rad = math.radians(ang)
    monty.goto(max_r * math.cos(rad), max_r * math.sin(rad))

for ring in range(1, n_rings + 1):
    r = ring * max_r / n_rings
    monty.penup()
    rad0 = math.radians(angles[0])
    monty.goto(r * math.cos(rad0), r * math.sin(rad0))
    monty.pendown()
    for ang in angles[1:] + [angles[0]]:
        rad = math.radians(ang)
        monty.goto(r * math.cos(rad), r * math.sin(rad))

monty.penup()
monty.goto(0, 0)
monty.pendown()
monty.dot(10, 'black')`);
</script>

Ogni anello è un **poligono a 12 lati** — un lato per raggio. Con 12 raggi equamente spaziati, ogni lato si estende per 30°. Avevi indovinato?

## Come Funziona

`angles[1:] + [angles[0]]` visita tutti i 12 raggi poi ritorna al primo — chiudendo ogni poligono anulare. `r * math.cos(rad), r * math.sin(rad)` converte polare (r, angle) in cartesiano (x, y).

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `angles = [i * 360 / n_spokes for i in range(n_spokes)]` | 12 angoli di raggio equamente spaziati |
| `r = ring * max_r / n_rings` | Il raggio dell'anello cresce uniformemente verso l'esterno |
| `angles[1:] + [angles[0]]` | Visita tutti i raggi, poi chiudi l'anello |
| `math.cos(rad), math.sin(rad)` | Convertono l'angolo in offset x, y |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi Più Raggi"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `n_spokes = 12` in `n_spokes = 8`. Quanti lati di poligono avrà ogni anello?
    Prevedi, poi eseguilo per controllare!

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

n_spokes = 8
n_rings = 6
max_r = 120
angles = [i * 360 / n_spokes for i in range(n_spokes)]

monty.pencolor('darkblue')
monty.pensize(1)

for ang in angles:
    monty.penup()
    monty.goto(0, 0)
    monty.pendown()
    rad = math.radians(ang)
    monty.goto(max_r * math.cos(rad), max_r * math.sin(rad))

for ring in range(1, n_rings + 1):
    r = ring * max_r / n_rings
    monty.penup()
    rad0 = math.radians(angles[0])
    monty.goto(r * math.cos(rad0), r * math.sin(rad0))
    monty.pendown()
    for ang in angles[1:] + [angles[0]]:
        rad = math.radians(ang)
        monty.goto(r * math.cos(rad), r * math.sin(rad))

monty.penup()
monty.goto(0, 0)
monty.pendown()
monty.dot(10, 'black')`);
</script>

8 raggi → anelli ottagonali a 8 lati — ogni anello è ora un ottagono invece di un poligono a 12 lati.

## Esperimenti

1. **Aggiungi un ragno.** Dopo il disegno, posiziona un cerchio riempito a `(30, 30)` usando `monty.dot(20, 'black')`. Saprai che ha funzionato quando un ragno appare sulla ragnatela.

2. **Usa cerchi concentrici invece di poligoni.** Sostituisci il codice di disegno degli anelli con `monty.circle(r)` a ogni raggio di anello. Saprai che ha funzionato quando gli anelli sembrano rotondi.

3. **Colora gli anelli.** Crea una lista di colori per anello e usa `monty.pencolor(ring_colors[ring])`. Saprai che ha funzionato quando ogni anello è di un colore diverso.

4. **Rendi la ragnatela asimmetrica.** Invece di una spaziatura uniforme, usa angoli non uniformi. Saprai che ha funzionato quando la ragnatela sembra irregolare come una vera ragnatela.

!!! mascot-celebration "Geometria a Otto Zampe!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai disegnato una ragnatela usando solo coordinate polari e `goto()`!
    La combinazione di strutture radiali e anulari appare ovunque in natura e ingegneria.
    Prossimo: **Fulmine** — zigzag frastagliato ricorsivo.
