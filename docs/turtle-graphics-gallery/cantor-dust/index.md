---
hide:
    - toc
---
# Polvere di Cantor

Alla fine di questo laboratorio sarai in grado di:

- Disegnare l'insieme di Cantor rimuovendo ricorsivamente il terzo centrale di ogni segmento di linea
- Capire come l'area si riduce a zero mentre la struttura rimane — il paradosso della polvere di Cantor
- Usare una funzione ricorsiva con parametri sia di posizione (`x`) sia di larghezza (`w`)

Sei livelli di linee dell'insieme di Cantor — ogni riga ha il doppio dei segmenti della riga sopra, ma ogni segmento è un terzo lungo. Alla riga 6, ogni segmento è quasi invisibile, eppure la struttura è matematicamente infinita.

!!! mascot-welcome "Benvenuto alla Polvere di Cantor!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Georg Cantor dimostrò nel 1883 che puoi avere un insieme con infiniti punti
    ma lunghezza totale zero. Questo pattern ti mostra come!
    Programmiamo insieme!

## Come Funziona

`cantor(x, y, w, depth)`:
- Disegna una linea orizzontale da `(x, y)` a `(x+w, y)`
- Se `depth > 0`: ricorri sul terzo sinistro `(x, y - 20, w/3, depth-1)` e sul terzo destro `(x + 2*w/3, y - 20, w/3, depth-1)`
- Il terzo centrale **non viene mai disegnato** — quello è lo spazio vuoto

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def cantor(x, y, w, depth):
    colors = ['darkred', 'red', 'orangered', 'orange', 'gold', 'yellow']
    monty.pencolor(colors[min(depth, len(colors) - 1)])
    monty.pensize(max(1, depth))
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.forward(w)
    if depth > 0:
        cantor(x, y - 30, w / 3, depth - 1)
        cantor(x + 2 * w / 3, y - 30, w / 3, depth - 1)

cantor(-250, 200, 500, 5)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni riga ha il doppio delle linee della precedente.
    Dopo 5 livelli, quanti piccoli segmenti di linea ci saranno nella riga inferiore?
    (Suggerimento: 2^5 = ?) Fai la tua previsione — poi clicca Esegui per scoprirlo!

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

def cantor(x, y, w, depth):
    colors = ['darkred', 'red', 'orangered', 'orange', 'gold', 'yellow']
    monty.pencolor(colors[min(depth, len(colors) - 1)])
    monty.pensize(max(1, depth))
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.forward(w)
    if depth > 0:
        cantor(x, y - 30, w / 3, depth - 1)
        cantor(x + 2 * w / 3, y - 30, w / 3, depth - 1)

cantor(-250, 200, 500, 5)`);
</script>

`2^5 = 32` segmenti nella riga inferiore — ognuno largo solo `500 / 3^5 ≈ 2` pixel. Avevi indovinato?

## Come Funziona

La lunghezza totale di tutti i segmenti al livello `n` è `(2/3)^n` della lunghezza originale. Al livello 5, rimane circa il `(2/3)^5 ≈ 13%`. Mentre la profondità → ∞, la lunghezza totale → 0. Eppure un numero infinito di punti rimane — questa è la **Polvere di Cantor**.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.forward(w)` | Disegna il segmento attuale |
| `if depth > 0:` | Caso base: si ferma alla profondità 0 |
| `cantor(x, y-30, w/3, depth-1)` | Sotto-segmento del terzo sinistro, una riga più in basso |
| `cantor(x + 2*w/3, y-30, w/3, depth-1)` | Sotto-segmento del terzo destro |
| Terzo centrale | Non viene mai disegnato — lo spazio vuoto distintivo |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna tutti e tre i terzi invece di rimuovere quello centrale.
    Trova e rimuovi la riga che disegna il segmento centrale.

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

def cantor(x, y, w, depth):
    colors = ['darkred', 'red', 'orangered', 'orange', 'gold', 'yellow']
    monty.pencolor(colors[min(depth, len(colors) - 1)])
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.forward(w)
    if depth > 0:
        cantor(x, y - 30, w / 3, depth - 1)
        cantor(x + w / 3, y - 30, w / 3, depth - 1)
        cantor(x + 2 * w / 3, y - 30, w / 3, depth - 1)

cantor(-250, 200, 500, 4)`);
</script>

Rimuovi la chiamata centrale `cantor(x + w/3, y-30, w/3, depth-1)` — quello è il terzo centrale che l'Insieme di Cantor non disegna mai.

## Esperimenti

1. **Rimuovi il primo terzo invece.** Cambia le due chiamate ricorsive così disegni sempre il terzo centrale e quello destro. Saprai che ha funzionato quando gli spazi vuoti sono a sinistra invece che al centro.

2. **Usa una spaziatura diversa.** Cambia `y - 30` in `y - 20`. Le righe saranno più vicine. Saprai che ha funzionato quando le 6 righe entrano più compattamente.

3. **Colora per livello.** Il codice attuale usa `depth` per il colore — la prima riga è la più scura. Prova a invertire: usa `6 - depth` come indice del colore. Saprai che ha funzionato quando le righe più profonde sono più scure.

4. **Disegna Cantor verticale.** Ruota la tartaruga di 90° e usa il posizionamento `y` invece di `x`. Saprai che ha funzionato quando gli spazi vuoti appaiono verticalmente.

!!! mascot-celebration "Dentro la Polvere!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai visualizzato il paradosso di Cantor: punti infiniti, lunghezza zero!
    L'Insieme di Cantor è il fondamento dell'analisi moderna e della teoria della misura.
    Prossimo: **Albero di Pitagora** — quadrati che crescono da quadrati che crescono da quadrati.
