---
hide:
    - toc
---
# Illusione del Muro del Caffè

Alla fine di questo laboratorio sarai in grado di:

- Disegnare un pattern a muro del caffè dove ogni riga di tessere è spostata di metà tessera
- Capire perché le linee di malta sembrano convergere anche se sono parallele
- Usare cicli annidati per costruire una griglia tassellata con offset di riga alternati

L'Illusione del Muro del Caffè fu notata per la prima volta su un caffè a Bristol, in Inghilterra. Righe di tessere nere e bianche con sottili linee di malta grigie tra di esse — ogni linea di malta è perfettamente orizzontale e parallela, eppure sembrano inclinate!

!!! mascot-welcome "Benvenuto all'Illusione del Muro del Caffè!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nel 1979, un ricercatore chiamato Richard Gregory notò questa illusione sulle tessere
    di un muro di un caffè a Bristol. Le linee di malta sono perfettamente parallele — ma sembrano inclinate!
    Programmiamolo insieme e vediamo se inganna anche i tuoi occhi!

## Come Funziona

Disegna una griglia di rettangoli neri e bianchi. Le righe dispari sono spostate a destra di metà larghezza di una tessera. Tra le righe, disegna una sottile linea di malta grigia orizzontale. Le tessere con offset + il colore della malta creano l'illusione di linee divergenti.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

tile_w = 40
tile_h = 25
mortar = 3
cols = 8
rows = 7

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

ox = -(cols * tile_w) / 2
oy = -(rows * (tile_h + mortar)) / 2

for row in range(rows):
    offset = (row % 2) * (tile_w / 2)
    y = oy + row * (tile_h + mortar)
    filled_rect(ox - tile_w, y, (cols + 2) * tile_w, mortar, 'gray')
    for col in range(-1, cols + 1):
        color = 'black' if (col + row) % 2 == 0 else 'white'
        filled_rect(ox + col * tile_w + offset, y + mortar, tile_w, tile_h, color)

filled_rect(ox - tile_w, oy + rows * (tile_h + mortar), (cols + 2) * tile_w, mortar, 'gray')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni linea di malta grigia è disegnata perfettamente orizzontale — il codice lo garantisce.
    Sembreranno ancora inclinate dopo aver aggiunto le tessere nere e bianche?
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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

tile_w = 40
tile_h = 25
mortar = 3
cols = 8
rows = 7

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

ox = -(cols * tile_w) / 2
oy = -(rows * (tile_h + mortar)) / 2

for row in range(rows):
    offset = (row % 2) * (tile_w / 2)
    y = oy + row * (tile_h + mortar)
    filled_rect(ox - tile_w, y, (cols + 2) * tile_w, mortar, 'gray')
    for col in range(-1, cols + 1):
        color = 'black' if (col + row) % 2 == 0 else 'white'
        filled_rect(ox + col * tile_w + offset, y + mortar, tile_w, tile_h, color)

filled_rect(ox - tile_w, oy + rows * (tile_h + mortar), (cols + 2) * tile_w, mortar, 'gray')`);
</script>

Le linee grigie **sembrano inclinate** anche se il codice le disegna perfettamente orizzontali! Avevi indovinato?

## Come Funziona

Il colore grigio della malta si trova tra le tessere scure e quelle chiare. Il tuo sistema visivo giudica la posizione della linea in base al contrasto locale. Quando le tessere nere e bianche su entrambi i lati di una linea di malta sono spostate, il contrasto del bordo fa sembrare che la malta si inclini verso il lato più scuro.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `offset = (row % 2) * (tile_w / 2)` | Le righe alterne sono spostate di metà tessera |
| `mortar = 3` | Strisce grigie sottili tra le righe — la chiave dell'illusione |
| `'black' if (col+row)%2==0 else 'white'` | Colorazione a scacchiera dentro ogni riga |
| `filled_rect(...)` | Aiutante per disegnare un rettangolo riempito |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Colore della Malta"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `'gray'` nelle linee di malta in `'black'`. L'illusione scomparirà o cambierà?
    L'illusione richiede un colore di malta tra il nero e il bianco. Cosa prevedi?

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

tile_w = 40
tile_h = 25
mortar = 3
cols = 8
rows = 7

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

ox = -(cols * tile_w) / 2
oy = -(rows * (tile_h + mortar)) / 2

for row in range(rows):
    offset = (row % 2) * (tile_w / 2)
    y = oy + row * (tile_h + mortar)
    filled_rect(ox - tile_w, y, (cols + 2) * tile_w, mortar, 'black')
    for col in range(-1, cols + 1):
        color = 'black' if (col + row) % 2 == 0 else 'white'
        filled_rect(ox + col * tile_w + offset, y + mortar, tile_w, tile_h, color)

filled_rect(ox - tile_w, oy + rows * (tile_h + mortar), (cols + 2) * tile_w, mortar, 'black')`);
</script>

Con la malta nera, l'illusione si attenua considerevolmente — la malta si fonde con le tessere nere e perde il suo ruolo di elemento "intermedio" che crea l'inclinazione apparente.

## Esperimenti

1. **Aumenta lo spessore della malta.** Cambia `mortar = 3` in `mortar = 8`. Saprai che ha funzionato quando le strisce grigie sono molto più larghe.

2. **Prova tessere colorate.** Sostituisci `'black'` con `'navy'` e `'white'` con `'lightyellow'`. Saprai che ha funzionato quando appaiono tessere colorate — l'illusione funziona ancora?

3. **Rimuovi l'offset di riga.** Cambia `offset = (row % 2) * (tile_w / 2)` in `offset = 0`. Saprai che ha funzionato quando l'illusione scompare — tutte le tessere si allineano.

4. **Varia la quantità di offset.** Prova `offset = (row % 2) * (tile_w / 3)` o `tile_w / 4`. Saprai che ha funzionato quando appare una forza diversa dell'illusione.

!!! mascot-celebration "Il Tuo Cervello È Stato Ingannato di Nuovo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    L'illusione del muro del caffè ci insegna che la percezione non riguarda solo ciò che c'è —
    riguarda il contrasto locale e il contesto. Linee perfettamente parallele sembrano inclinate!
    Prossimo: **Motivo Moiré** — due griglie sovrapposte che creano pattern di battimento.
