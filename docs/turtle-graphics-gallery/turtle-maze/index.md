---
hide:
    - toc
---
# Generatore di Labirinti con la Turtle

Alla fine di questo laboratorio sarai in grado di:

- Generare un labirinto usando l'algoritmo del backtracker ricorsivo (ricerca in profondità)
- Rappresentare una griglia di celle come una lista 2D e tracciare quali muri sono stati rimossi
- Disegnare il labirinto usando `goto()` per disegnare i segmenti dei muri

Un labirinto perfetto — ogni coppia di celle collegata da esattamente un percorso — generato dall'algoritmo del backtracker ricorsivo. L'algoritmo scava passaggi rimuovendo muri tra vicini non visitati scelti casualmente.

!!! mascot-welcome "Benvenuto al Generatore di Labirinti!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I labirinti sono un uso classico del backtracking ricorsivo — un algoritmo di informatica
    dove esplori il più lontano possibile prima di tornare indietro.
    Generiamone uno insieme!

## Come Funziona

**Backtracker ricorsivo**: inizia a (0,0). Segnalo visitato. Visita casualmente vicini non visitati rimuovendo il muro condiviso. Quando bloccato, torna indietro. Questo produce un "labirinto perfetto" dove ogni cella è raggiungibile.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

COLS, ROWS = 12, 10
cell = 25
ox = -COLS * cell / 2
oy = -ROWS * cell / 2

walls_removed = set()
visited = [[False]*COLS for _ in range(ROWS)]

def neighbors(r, c):
    result = []
    for dr, dc, direction in [(-1,0,'N'),(1,0,'S'),(0,-1,'W'),(0,1,'E')]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
            result.append((nr, nc, direction))
    return result

def carve(r, c):
    visited[r][c] = True
    dirs = neighbors(r, c)
    random.shuffle(dirs)
    for nr, nc, d in dirs:
        if not visited[nr][nc]:
            walls_removed.add((r, c, d))
            carve(nr, nc)

import sys
sys.setrecursionlimit(5000)
carve(0, 0)

def draw_wall(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

monty.pencolor('navy')
monty.pensize(2)

for r in range(ROWS):
    for c in range(COLS):
        x = ox + c * cell
        y = oy + r * cell
        if r == ROWS - 1 or not (r, c, 'N') in walls_removed:
            draw_wall(x, y+cell, x+cell, y+cell)
        if c == 0 or not (r, c, 'W') in walls_removed:
            draw_wall(x, y, x, y+cell)
draw_wall(ox, oy, ox + COLS*cell, oy)
draw_wall(ox + COLS*cell, oy, ox+COLS*cell, oy+ROWS*cell)

monty.pencolor('forestgreen')
monty.goto(ox + 2, oy + 2)
monty.dot(8, 'forestgreen')
monty.goto(ox + COLS*cell - 2, oy + ROWS*cell - 2)
monty.dot(8, 'red')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    L'algoritmo usa `random.seed(42)` — lo stesso seme dà sempre lo stesso labirinto.
    Il risultato sembrerà casuale e tortuoso, o strutturato e regolare?
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
import random
import sys
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

COLS, ROWS = 12, 10
cell = 25
ox = -COLS * cell / 2
oy = -ROWS * cell / 2

walls_removed = set()
visited = [[False]*COLS for _ in range(ROWS)]

def neighbors(r, c):
    result = []
    for dr, dc, direction in [(-1,0,'N'),(1,0,'S'),(0,-1,'W'),(0,1,'E')]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
            result.append((nr, nc, direction))
    return result

def carve(r, c):
    visited[r][c] = True
    dirs = neighbors(r, c)
    random.shuffle(dirs)
    for nr, nc, d in dirs:
        if not visited[nr][nc]:
            walls_removed.add((r, c, d))
            carve(nr, nc)

sys.setrecursionlimit(5000)
carve(0, 0)

def draw_wall(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

monty.pencolor('navy')
monty.pensize(2)

for r in range(ROWS):
    for c in range(COLS):
        x = ox + c * cell
        y = oy + r * cell
        if r == ROWS - 1 or (r, c, 'N') not in walls_removed:
            draw_wall(x, y+cell, x+cell, y+cell)
        if c == 0 or (r, c, 'W') not in walls_removed:
            draw_wall(x, y, x, y+cell)
draw_wall(ox, oy, ox + COLS*cell, oy)
draw_wall(ox + COLS*cell, oy, ox+COLS*cell, oy+ROWS*cell)

monty.penup()
monty.goto(ox + 2, oy + 2)
monty.dot(8, 'forestgreen')
monty.goto(ox + COLS*cell - 2, oy + ROWS*cell - 2)
monty.dot(8, 'red')`);
</script>

Un **labirinto che sembra casuale ma perfetto** — percorsi tortuosi senza anelli, garantito risolvibile. Avevi indovinato?

## Come Funziona

Il backtracker ricorsivo usa lo stack delle chiamate per "ricordare" il suo percorso. Quando una cella non ha vicini non visitati, la funzione ritorna — tornando indietro alla cella precedente. `walls_removed` registra quali muri sono stati scavati così il passo del disegno sa quali muri saltare.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `walls_removed = set()` | Traccia quali muri sono stati scavati |
| `random.shuffle(dirs)` | Randomizza l'ordine di esplorazione dei vicini |
| `carve(nr, nc)` | DFS ricorsivo — esplora il vicino scelto |
| `if (r,c,'N') not in walls_removed` | Disegna solo i muri che non sono stati scavati |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Seme"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `random.seed(42)` in `random.seed(7)`.
    Verrà generato un labirinto completamente diverso dallo stesso algoritmo.
    Prevedi: sembrerà simile o completamente diverso?

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
import random
import sys
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(7)

COLS, ROWS = 12, 10
cell = 25
ox = -COLS * cell / 2
oy = -ROWS * cell / 2

walls_removed = set()
visited = [[False]*COLS for _ in range(ROWS)]

def neighbors(r, c):
    result = []
    for dr, dc, direction in [(-1,0,'N'),(1,0,'S'),(0,-1,'W'),(0,1,'E')]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and not visited[nr][nc]:
            result.append((nr, nc, direction))
    return result

def carve(r, c):
    visited[r][c] = True
    dirs = neighbors(r, c)
    random.shuffle(dirs)
    for nr, nc, d in dirs:
        if not visited[nr][nc]:
            walls_removed.add((r, c, d))
            carve(nr, nc)

sys.setrecursionlimit(5000)
carve(0, 0)

def draw_wall(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

monty.pencolor('darkred')
monty.pensize(2)

for r in range(ROWS):
    for c in range(COLS):
        x = ox + c * cell
        y = oy + r * cell
        if r == ROWS - 1 or (r, c, 'N') not in walls_removed:
            draw_wall(x, y+cell, x+cell, y+cell)
        if c == 0 or (r, c, 'W') not in walls_removed:
            draw_wall(x, y, x, y+cell)
draw_wall(ox, oy, ox + COLS*cell, oy)
draw_wall(ox + COLS*cell, oy, ox+COLS*cell, oy+ROWS*cell)

monty.penup()
monty.goto(ox + 2, oy + 2)
monty.dot(8, 'forestgreen')
monty.goto(ox + COLS*cell - 2, oy + ROWS*cell - 2)
monty.dot(8, 'gold')`);
</script>

Un labirinto completamente diverso dal seme 7 — ma ancora perfettamente collegato con esattamente un percorso tra ogni due celle.

## Esperimenti

1. **Rendilo più grande.** Cambia in `COLS=20, ROWS=16` e `cell=18`. Saprai che ha funzionato quando appare un labirinto più grande e più complesso.

2. **Aggiungi apertura di entrata e uscita.** Rimuovi i muri di confine in basso a sinistra e in alto a destra. Saprai che ha funzionato quando il labirinto ha un'apertura chiara di inizio e fine.

3. **Mostra la soluzione.** Dopo aver generato il labirinto, trova un percorso da (0,0) a (ROWS-1, COLS-1) usando BFS e disegnalo in rosso. Saprai che ha funzionato quando un percorso rosso mostra la soluzione.

4. **Usa forme di cella diverse.** Disegna piccoli cerchi al centro di ogni cella invece di linee di muro. Saprai che ha funzionato quando il labirinto sembra una rete basata su nodi.

!!! mascot-celebration "Hai Generato un Labirinto!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai implementato la ricerca in profondità per generare un labirinto perfetto!
    Questo algoritmo è usato nella generazione di livelli di giochi, nel routing di rete, e nel design di puzzle.
    Prossimo: **Proiezione di Superficie Parametrica** — matematica 3D proiettata su 2D.
