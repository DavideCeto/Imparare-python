---
hide:
    - toc
---
# Motivo di Reazione-Diffusione

Alla fine di questo laboratorio sarai in grado di:

- Memorizzare una griglia di numeri in una lista Python piatta e indicizzarla con `i * w + j`
- Aggiornare ogni cella dai suoi vicini usando uno stencil Laplaciano (di diffusione)
- Spiegare come macchie e strisce sulla pelle degli animali emergano da due semplici regole locali

Due sostanze chimiche invisibili, U e V, si diffondono su una griglia 32×32. U nutre V, V consuma U, ed entrambe diffondono verso i loro vicini. Da quattro piccoli quadrati seme, 300 passi di simulazione fanno crescere macchie organiche e strisce simili a vermi — la stessa matematica di Gray-Scott che si ritiene dipinga le macchie del leopardo e le strisce della zebra.

!!! mascot-welcome "Benvenuto alla Reazione-Diffusione!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo programma non viene disegnata nessuna forma — il motivo
    *cresce da solo* dalle regole della chimica, un vicino alla volta.
    Questa è vera scienza computazionale! Sii paziente quando clicchi
    Esegui: 300 passi di simulazione richiedono un po' di tempo.

## Come Funziona

Ogni cella contiene due numeri: `u` (cibo) e `v` (creatura). A ogni passo, ogni cella guarda i suoi 8 vicini per calcolare un **Laplaciano** — una misura di "quanto sono diverso dal mio ambiente circostante" — che fa diffondere entrambe le sostanze chimiche. Poi avviene la reazione: `u * v * v` converte il cibo in creatura, `feed` rifornisce il cibo, e `kill` rimuove la creatura. Dopo tutti i passi, ogni cella viene dipinta come un punto colorato in base a quanto `v` contiene.

## Codice di Esempio

```python
w = 32
u = [1.0] * (w * w)
v = [0.0] * (w * w)

for step in range(300):
    u2 = u[:]
    v2 = v[:]
    for i in range(1, w - 1):
        for j in range(1, w - 1):
            p = i * w + j
            lapu = neighbor_average(u, p) - u[p]
            lapv = neighbor_average(v, p) - v[p]
            uvv = u[p] * v[p] * v[p]
            u2[p] = u[p] + du * lapu - uvv + feed * (1 - u[p])
            v2[p] = v[p] + dv * lapv + uvv - (feed + kill) * v[p]
    u = u2
    v = v2
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La simulazione inizia con solo **4 piccoli quadrati** di sostanza V.
    Dopo 300 passi, l'immagine mostrerà ancora 4 quadrati separati, o
    qualcos'altro? Fai la tua ipotesi, poi clicca Esegui (e dagli un
    momento)!

## Prova Ora

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

w = 32
feed = 0.055
kill = 0.062
du = 0.5
dv = 0.25
steps = 300

u = [1.0] * (w * w)
v = [0.0] * (w * w)

seeds = [[8, 8], [20, 10], [14, 21], [24, 24]]
for s in seeds:
    for i in range(s[0], s[0] + 4):
        for j in range(s[1], s[1] + 4):
            v[i * w + j] = 1.0

for step in range(steps):
    u2 = u[:]
    v2 = v[:]
    for i in range(1, w - 1):
        for j in range(1, w - 1):
            p = i * w + j
            uc = u[p]
            vc = v[p]
            lapu = (u[p-1] + u[p+1] + u[p-w] + u[p+w]) * 0.2 + (u[p-w-1] + u[p-w+1] + u[p+w-1] + u[p+w+1]) * 0.05 - uc
            lapv = (v[p-1] + v[p+1] + v[p-w] + v[p+w]) * 0.2 + (v[p-w-1] + v[p-w+1] + v[p+w-1] + v[p+w+1]) * 0.05 - vc
            uvv = uc * vc * vc
            u2[p] = uc + du * lapu - uvv + feed * (1 - uc)
            v2[p] = vc + dv * lapv + uvv - (feed + kill) * vc
    u = u2
    v = v2

screen = turtle.Screen()
screen.tracer(0)
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

colors = ['midnightblue', 'darkslateblue', 'teal', 'mediumseagreen', 'gold', 'lightyellow']
cell = 10
half = w * cell / 2
for i in range(w):
    for j in range(w):
        level = int(v[i * w + j] * 8)
        if level > 5:
            level = 5
        monty.goto(j * cell - half + 5, half - i * cell - 5)
        monty.dot(14, colors[level])
screen.update()`);
</script>

I quattro quadrati sono spariti da tempo — si sono sciolti, diffusi e fusi in macchie organiche arricciate. Questa è l'emergenza: nessuna riga di codice dice "disegna una forma di verme", eppure appaiono vermi. Avevi indovinato?

## Come Funziona

Lo stencil Laplaciano pesa i 4 vicini sui bordi per 0.2 e i 4 vicini agli angoli per 0.05 — una media smussata dell'ambiente circostante meno la cella stessa. Due dettagli contano enormemente: l'aggiornamento scrive dentro delle **copie** (`u2`, `v2`) così ogni cella vede la stessa immagine "prima", e V diffonde a **metà** della velocità di U (`dv = 0.25` contro `du = 0.5`). Quella differenza nella velocità di diffusione è esattamente ciò che Alan Turing dimostrò nel 1952 poter destabilizzare un miscuglio uniforme in macchie e strisce.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `p = i * w + j` | Trova la cella (i, j) dentro la lista piatta |
| `lapu = (...) * 0.2 + (...) * 0.05 - uc` | Diffusione: media pesata degli 8 vicini meno se stesso |
| `uvv = uc * vc * vc` | La reazione: U + 2V → 3V |
| `u2[p] = uc + ...` | Scrive in una copia così tutte le celle si aggiornano insieme |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Cogli il Motivo a Metà Crescita"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa copia è impostata per fermarsi dopo solo `steps = 60`.
    Prevedi cosa vedrai: macchie finite, quattro quadrati sfocati, o
    niente del tutto? Eseguilo, confrontalo con l'immagine a 300 passi
    sopra, poi prova 150 e 600!

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

w = 32
feed = 0.055
kill = 0.062
du = 0.5
dv = 0.25
steps = 60

u = [1.0] * (w * w)
v = [0.0] * (w * w)

seeds = [[8, 8], [20, 10], [14, 21], [24, 24]]
for s in seeds:
    for i in range(s[0], s[0] + 4):
        for j in range(s[1], s[1] + 4):
            v[i * w + j] = 1.0

for step in range(steps):
    u2 = u[:]
    v2 = v[:]
    for i in range(1, w - 1):
        for j in range(1, w - 1):
            p = i * w + j
            uc = u[p]
            vc = v[p]
            lapu = (u[p-1] + u[p+1] + u[p-w] + u[p+w]) * 0.2 + (u[p-w-1] + u[p-w+1] + u[p+w-1] + u[p+w+1]) * 0.05 - uc
            lapv = (v[p-1] + v[p+1] + v[p-w] + v[p+w]) * 0.2 + (v[p-w-1] + v[p-w+1] + v[p+w-1] + v[p+w+1]) * 0.05 - vc
            uvv = uc * vc * vc
            u2[p] = uc + du * lapu - uvv + feed * (1 - uc)
            v2[p] = vc + dv * lapv + uvv - (feed + kill) * vc
    u = u2
    v = v2

screen = turtle.Screen()
screen.tracer(0)
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

colors = ['midnightblue', 'darkslateblue', 'teal', 'mediumseagreen', 'gold', 'lightyellow']
cell = 10
half = w * cell / 2
for i in range(w):
    for j in range(w):
        level = int(v[i * w + j] * 8)
        if level > 5:
            level = 5
        monty.goto(j * cell - half + 5, half - i * cell - 5)
        monty.dot(14, colors[level])
screen.update()`);
</script>

A 60 passi i quattro semi hanno solo appena iniziato a dissolversi in anelli — il motivo è ancora riconoscibile come "quattro quadrati che si sciolgono". L'emergenza richiede tempo: la struttura interessante appare da qualche parte tra 150 e 300 passi.

## Esperimenti

1. **Cambia la ricetta.** Prova `kill = 0.065` (crescita a corallo) o `feed = 0.035, kill = 0.060` (solitoni). Saprai che ha funzionato quando le forme delle macchie cambiano completamente carattere.

2. **Un solo seme.** Elimina tre dei quattro semi. Saprai che ha funzionato quando una singola macchia fa crescere anelli verso l'esterno come una piccola colonia di corallo.

3. **Nuovo schema di colori.** Sostituisci la lista dei colori con rossi e arancioni per un aspetto a pelle di lava. Saprai che ha funzionato quando il motivo brilla caldo invece che freddo-oceano.

4. **Canvas più grande, griglia più grossolana.** Prova `w = 24` con `cell = 14` e `steps = 400`. Saprai che ha funzionato quando il motivo è più grossolano ma evolve di più nello stesso tempo di esecuzione.

!!! mascot-celebration "Hai Simulato la Natura!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Una griglia, due sostanze chimiche, e matematica dei vicini — e il
    tuo programma ha fatto crescere motivi che nessuno ha disegnato.
    Alan Turing lo immaginò nel 1952; tu l'hai appena eseguito in un
    browser. Hai raggiunto la fine della galleria — esplora la
    **Galleria di Grafica Turtle** per la tua prossima sfida!
