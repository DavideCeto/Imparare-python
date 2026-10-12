---
hide:
    - toc
---
# Albero di Pitagora

Alla fine di questo laboratorio sarai in grado di:

- Disegnare un frattale basato sul teorema di Pitagora usando quadrati ricorsivi
- Colorare i quadrati per profondità — marrone alla base, verde alle foglie
- Capire come un teorema geometrico diventa un frattale visivo

Un albero di quadrati: ogni quadrato genera due quadrati più piccoli sul suo lato superiore, disposti come un triangolo rettangolo. I quadrati marroni alla base passano a quadrati foglia verde brillante attraverso 7 livelli ricorsivi.

!!! mascot-welcome "Benvenuto all'Albero di Pitagora!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il teorema di Pitagora dice `a² + b² = c²` per un triangolo rettangolo.
    Questo frattale rende quel teorema *visibile* — i due quadrati più piccoli SONO letteralmente `a²` e `b²`!
    Programmiamo insieme!

## Come Funziona

`pytree(x, y, w, angle, depth)` disegna un quadrato di larghezza `w` alla posizione `(x, y)` rivolto verso `angle`. Poi disegna ricorsivamente due quadrati più piccoli sul lato superiore — sinistra all'angolo `+45°`, destra all'angolo `-45°` — ognuno con larghezza `w * cos(45°) ≈ w * 0,707`.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def draw_square(x, y, w, angle, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(angle)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(w)
        monty.left(90)
    monty.end_fill()

def pytree(x, y, w, angle, depth):
    leaf_colors = ['saddlebrown', 'brown', 'peru', 'darkolivegreen',
                   'olivedrab', 'yellowgreen', 'lawngreen', 'lime']
    color = leaf_colors[min(depth, len(leaf_colors) - 1)]
    draw_square(x, y, w, angle, color)
    if depth < 7 and w > 4:
        rad = math.radians(angle + 90)
        top_x = x + w * math.cos(math.radians(angle))
        top_y = y + w * math.sin(math.radians(angle))
        w2 = w * math.cos(math.radians(45))
        pytree(top_x, top_y, w2, angle + 45, depth + 1)
        rx = top_x + w * math.cos(math.radians(angle + 90))
        ry = top_y + w * math.sin(math.radians(angle + 90))
        pytree(rx - w2 * math.cos(math.radians(angle)),
               ry - w2 * math.sin(math.radians(angle)), w2, angle - 45, depth + 1)

pytree(-30, -200, 60, 90, 0)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    I quadrati si restringono di `cos(45°) ≈ 0,707` a ogni livello. Dopo 7 livelli,
    quanto piccoli saranno i quadrati foglia? (Suggerimento: `60 × 0,707^7 ≈ ?`)
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

def draw_square(x, y, w, angle, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(angle)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(w)
        monty.left(90)
    monty.end_fill()

def pytree(x, y, w, angle, depth):
    leaf_colors = ['saddlebrown', 'brown', 'peru', 'darkolivegreen',
                   'olivedrab', 'yellowgreen', 'lawngreen', 'lime']
    color = leaf_colors[min(depth, len(leaf_colors) - 1)]
    draw_square(x, y, w, angle, color)
    if depth < 7 and w > 4:
        top_x = x + w * math.cos(math.radians(angle))
        top_y = y + w * math.sin(math.radians(angle))
        w2 = w * math.cos(math.radians(45))
        pytree(top_x, top_y, w2, angle + 45, depth + 1)
        rx = top_x + w * math.cos(math.radians(angle + 90))
        ry = top_y + w * math.sin(math.radians(angle + 90))
        pytree(rx - w2 * math.cos(math.radians(angle)),
               ry - w2 * math.sin(math.radians(angle)), w2, angle - 45, depth + 1)

pytree(-30, -200, 60, 90, 0)`);
</script>

Dopo 7 livelli: `60 × 0,707^7 ≈ 3,7` pixel — esattamente alla soglia `w > 4`. Avevi indovinato?

## Come Funziona

Ogni ricorsione riduce `w` di `cos(45°) ≈ 0,707`. Il fatto geometrico chiave: quando costruisci un triangolo isoscele rettangolo sulla cima di un quadrato di lato `w`, ognuno dei due nuovi quadrati ha lato `w × cos(45°)`. E `cos²(45°) + cos²(45°) = 0,5 + 0,5 = 1` — questo è il teorema di Pitagora in forma geometrica!

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `draw_square(x, y, w, angle, color)` | Disegna un quadrato riempito nell'albero |
| `w2 = w * cos(45°)` | I sotto-quadrati sono √2/2 ≈ 70,7% della dimensione del genitore |
| `depth + 1` | Traccia la profondità per la scelta del colore e l'arresto |
| `if depth < 7 and w > 4:` | Due condizioni di arresto: profondità massima O troppo piccolo |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Usa un Triangolo Rettangolo Non Uguale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia i due angoli di ramificazione da `±45°` a `+30°` (sinistra) e `-60°` (destra).
    L'albero si inclinerà asimmetricamente. Prevedi da quale parte — poi eseguilo per controllare!

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

def draw_square(x, y, w, angle, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(angle)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for _ in range(4):
        monty.forward(w)
        monty.left(90)
    monty.end_fill()

def pytree(x, y, w, angle, depth):
    leaf_colors = ['saddlebrown', 'brown', 'peru', 'darkolivegreen',
                   'olivedrab', 'yellowgreen', 'lawngreen', 'lime']
    color = leaf_colors[min(depth, len(leaf_colors) - 1)]
    draw_square(x, y, w, angle, color)
    if depth < 7 and w > 4:
        top_x = x + w * math.cos(math.radians(angle))
        top_y = y + w * math.sin(math.radians(angle))
        wL = w * math.cos(math.radians(30))
        wR = w * math.cos(math.radians(60))
        pytree(top_x, top_y, wL, angle + 30, depth + 1)
        rx = top_x + w * math.cos(math.radians(angle + 90))
        ry = top_y + w * math.sin(math.radians(angle + 90))
        pytree(rx - wR * math.cos(math.radians(angle)),
               ry - wR * math.sin(math.radians(angle)), wR, angle - 60, depth + 1)

pytree(-30, -200, 60, 90, 0)`);
</script>

Con angoli `30°/60°` i rami sinistri sono più lunghi dei destri — l'albero si inclina a sinistra e sembra più naturale, come un albero battuto dal vento.

## Esperimenti

1. **Simmetrico ma più piccolo.** Cambia entrambi gli offset d'angolo a `30°`. Saprai che ha funzionato quando l'albero è più alto e più stretto.

2. **Rimuovi il riempimento.** Cambia `begin_fill()`/`end_fill()` in solo disegnare il contorno (rimuovi quelle chiamate). Saprai che ha funzionato quando vedi solo i contorni dei quadrati.

3. **Più profondità.** Cambia `depth < 7` in `depth < 9`. I quadrati foglia diventano molto piccoli. Saprai che ha funzionato quando l'albero è molto più denso alle punte.

4. **Colori autunnali.** Cambia la lista `leaf_colors` in `['saddlebrown', 'sienna', 'peru', 'chocolate', 'darkorange', 'orange', 'gold', 'yellow']`. Saprai che ha funzionato quando l'albero ha tonalità autunnali.

!!! mascot-celebration "Teorema Visualizzato!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai trasformato `a² + b² = c²` in un albero vivo e crescente — geometria resa visibile!
    Ogni coppia di quadrati figli rappresenta letteralmente i due termini del teorema di Pitagora.
    Prossimo: **Frattale a T-Square** — angoli che generano angoli.
