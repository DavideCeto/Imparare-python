---
hide:
    - toc
---
# Esagoni in Espansione

Alla fine di questo laboratorio sarai in grado di:

- Disegnare esagoni concentrici che crescono verso l'esterno dal centro
- Ruotare gli esagoni alterni di 30° per creare un'illusione più complessa
- Capire come i gradienti di colore migliorano il senso di profondità e movimento

Esagoni concentrici, che alternano tra due rotazioni — 0° e 30°. Il gradiente di colore dal centro scuro ai bordi chiari crea una forte illusione di un tunnel esagonale o una superficie che si espande verso di te.

!!! mascot-welcome "Benvenuto agli Esagoni in Espansione!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli esagoni tassellano perfettamente — sei attorno a ogni centro, tutti si incastrano senza spazi.
    Esagoni concentrici con rotazioni alterne creano un'illusione di profondità vertiginosa!
    Programmiamo insieme!

## Come Funziona

Disegna `n` esagoni regolari concentrici. Ogni esagono è centrato sull'origine, con raggio crescente di un passo fisso. Gli esagoni con numero dispari sono ruotati di 30° rispetto a quelli pari. I colori sfumano da navy scuro al centro a blu chiaro al bordo.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

n_hexagons = 12
r_step = 12

for i in range(1, n_hexagons + 1):
    r = i * r_step
    rotation = 30 if i % 2 == 0 else 0
    t = 1 - i / n_hexagons
    blue_val = int(50 + 200 * (1 - t))
    monty.pencolor(0, int(50 * t + 50), blue_val)
    monty.pensize(max(1, n_hexagons - i + 1) // 2)
    monty.penup()
    monty.goto(r, 0)
    monty.setheading(90 + rotation)
    monty.pendown()
    for _ in range(6):
        monty.forward(r)
        monty.left(60)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Esagoni alterni a 0° e 30° — sembreranno forme separate o un pattern unificato?
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

n_hexagons = 12
r_step = 12

for i in range(1, n_hexagons + 1):
    r = i * r_step
    rotation = 30 if i % 2 == 0 else 0
    t = i / n_hexagons
    color_val = int(30 + 200 * t)
    monty.pencolor(0, int(80 * t), color_val)
    monty.pensize(max(1, (n_hexagons - i + 1) // 2))
    monty.penup()
    angle_start = math.radians(rotation)
    monty.goto(r * math.cos(angle_start), r * math.sin(angle_start))
    monty.setheading(90 + rotation)
    monty.pendown()
    for _ in range(6):
        monty.forward(r)
        monty.left(60)`);
</script>

Un **tunnel esagonale** — la rotazione alterna e il gradiente di colore creano un forte senso di profondità. Avevi indovinato?

## Come Funziona

Gli esagoni interni sono disegnati con linee più spesse (più prominenti), quelli esterni con linee più sottili. Il gradiente di colore da scuro (centro) a chiaro (bordo) rafforza l'illusione del tunnel — gli oggetti più lontani sembrano più chiari. L'alternanza di 30° impedisce il semplice aspetto da "telescopio" e crea una complessità simile a una stella.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `rotation = 30 if i%2==0 else 0` | Alterna rotazioni di 0° e 30° |
| `t = i / n_hexagons` | Progresso da 0 (centro) a 1 (bordo) |
| `int(30 + 200 * t)` | Il valore del blu aumenta verso il bordo |
| `pensize(...) // 2` | Linee spesse all'interno, sottili all'esterno |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova i Pentagoni"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `range(6)` in `range(5)` e `left(60)` in `left(72)` nel ciclo interno.
    Prevedi: i pentagoni a 5 lati creeranno un'illusione simile?

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
import math

n_polygons = 12
r_step = 12

for i in range(1, n_polygons + 1):
    r = i * r_step
    rotation = 36 if i % 2 == 0 else 0
    t = i / n_polygons
    monty.pencolor(int(180 * t), 0, int(30 + 200 * t))
    monty.pensize(max(1, (n_polygons - i + 1) // 2))
    monty.penup()
    angle_start = math.radians(rotation)
    monty.goto(r * math.cos(angle_start), r * math.sin(angle_start))
    monty.setheading(90 + rotation)
    monty.pendown()
    for _ in range(5):
        monty.forward(r)
        monty.left(72)`);
</script>

Pentagoni concentrici con alternanza di 36° — un tunnel pentagonale, meno simmetrico degli esagoni ma ugualmente ipnotico.

## Esperimenti

1. **Rimuovi l'alternanza di rotazione.** Imposta `rotation = 0` sempre. Saprai che ha funzionato quando tutti gli esagoni si allineano e il pattern a stella scompare.

2. **Prova i triangoli.** Cambia a 3 lati, `left(120)`, `rotation = 60`. Saprai che ha funzionato quando appaiono triangoli annidati.

3. **Usa un gradiente di colore caldo.** Cambia il colore in rosso/arancione: `pencolor(int(50+200*t), int(100*t), 0)`. Saprai che ha funzionato quando il tunnel sembra braci ardenti.

4. **Aumenta n_hexagons.** Prova `n_hexagons = 20`. Saprai che ha funzionato quando il tunnel si estende molto più verso l'interno.

!!! mascot-celebration "Ipnosi Esagonale!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai creato un'illusione ottica geometrica usando solo esagoni concentrici!
    L'Op Art dimostra che la matematica, il colore, e la ripetizione possono ingannare il sistema visivo.
    Prossimo: **Categoria 9 — Pattern Tipografici!**
