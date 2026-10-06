---
title: Colori, Riempimento e Arte con la Turtle
description: Esplora i codici colore esadecimali, i modelli di colore RGB e HSL, la trasparenza, e come colorare forme solide con begin_fill() e end_fill()
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:00:00
version: 0.09
---

# Colori, Riempimento e Arte con la Turtle

Alla fine di questa lezione sarai in grado di:

- Usare **codici colore esadecimali** e **valori RGB** per impostare qualsiasi colore tu possa immaginare
- Spiegare la differenza tra i modelli di colore **RGB** e **HSL**
- Colorare forme solide riempite usando `begin_fill()` e `end_fill()`
- Impostare sia il **colore della penna** sia il **colore di sfondo** del canvas della tartaruga

I colori fanno venire viva l'arte con la tartaruga. Finora la nostra tartaruga ha disegnato solo contorni.
Oggi sblocchiamo l'intera tavolozza dei colori e impariamo a colorare forme riempite.

!!! mascot-welcome "Benvenuto/a al Capitolo 12!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto a dipingere? Alla fine di questa lezione i tuoi disegni con la tartaruga sembreranno vera arte.
    Mescoliamo un po' di colori e riempiamo qualche forma! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Colore nella Grafica Turtle

Sai già come impostare un colore per nome, come `t.pencolor("red")`.
La tartaruga di Python conosce circa 140 colori con nome, da `"aquamarine"` a `"yellow"`.

Ma ci sono milioni di colori che non hanno un nome. Per raggiungerli, hai bisogno dei **codici colore**.

## Codici Colore Esadecimali

Un **codice colore esadecimale** è un codice di sei caratteri che descrive un colore con precisione.
Ogni codice inizia con il simbolo `#` e contiene esattamente sei lettere e numeri.

```
#FF0000  →  pure red
#00FF00  →  pure green
#0000FF  →  pure blue
#000000  →  black
#FFFFFF  →  white
#FF6347  →  tomato red
```

I sei caratteri si dividono in tre coppie:
- La prima coppia controlla il **rosso** (00 a FF)
- La seconda coppia controlla il **verde** (00 a FF)
- La terza coppia controlla il **blu** (00 a FF)

`FF` significa luminosità massima (255 in decimale). `00` significa nessuna (0).

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna un quadrato in tre diversi colori esadecimali.
    Quali colori pensi che produrranno `#FF00FF` e `#FFFF00`?
    Fai la tua previsione — poi eseguilo per scoprirlo!

```python
import turtle
t = turtle.Turtle()
t.speed(6)
t.pensize(3)

colors = ["#FF0000", "#FF00FF", "#FFFF00"]
positions = [(-150, 0), (0, 0), (150, 0)]

for col, pos in zip(colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.pencolor(col)
    for i in range(4):
        t.forward(80)
        t.right(90)
```

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
t = turtle.Turtle()
t.speed(6)
t.pensize(3)

colors = ["#FF0000", "#FF00FF", "#FFFF00"]
positions = [(-150, 0), (0, 0), (150, 0)]

for col, pos in zip(colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.pencolor(col)
    for i in range(4):
        t.forward(80)
        t.right(90)`);
</script>

Avevi indovinato? `#FF00FF` è magenta (rosso + blu, senza verde) e `#FFFF00` è giallo (rosso + verde, senza blu).

## Il Modello di Colore RGB

Il **modello di colore RGB** mescola luce rossa, verde, e blu per creare ogni altro colore.
È lo stesso modello usato dal tuo schermo — ogni pixel del tuo monitor ha una minuscola luce rossa, una verde, e una blu.

| Colore | Rosso | Verde | Blu |
|-------|-----|-------|------|
| Rosso | 255 | 0 | 0 |
| Verde | 0 | 255 | 0 |
| Blu | 0 | 0 | 255 |
| Giallo | 255 | 255 | 0 |
| Ciano | 0 | 255 | 255 |
| Magenta | 255 | 0 | 255 |
| Bianco | 255 | 255 | 255 |
| Nero | 0 | 0 | 0 |

Puoi usare valori RGB direttamente in turtle convertendoli prima in una stringa di colore esadecimale. La funzione di supporto sotto fa questo calcolo così puoi continuare a pensare in valori da 0 a 255.

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

def to_hex(r, g, b):
    # Convert 0-255 RGB values to a hex color string like "#ff0000"
    return "#%02x%02x%02x" % (r, g, b)

t = turtle.Turtle()
t.speed(6)
t.pensize(4)

# Draw three circles with RGB colors
rgb_colors = [(255, 0, 0), (0, 200, 80), (0, 100, 255)]
positions = [(-120, 0), (0, 0), (120, 0)]

for rgb, pos in zip(rgb_colors, positions):
    t.penup()
    t.goto(pos)
    t.pendown()
    t.pencolor(to_hex(*rgb))
    t.circle(40)`);
</script>

Prova a cambiare i numeri nella lista `rgb_colors`. Ogni numero va da 0 (nessuna) a 255 (luminosità piena).

### Guardalo: Mescola il Tuo Colore

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di toccare gli slider sotto, prevedi: per ottenere un **giallo** brillante,
    quali due slider devono essere alti, e quale basso? Mescolalo e controlla
    il codice esadecimale che ottieni!

<iframe src="../../sims/rgb-color-mixer/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim RGB Color Mixer](../../sims/rgb-color-mixer/index.md){ .md-button }

Guarda il codice esadecimale mentre trascini uno slider — solo le **due cifre** di quel canale cambiano, evidenziate in giallo. Quando trovi un colore che ti piace, copia la riga `t.pencolor(...)` direttamente in qualsiasi laboratorio turtle di questo capitolo. Clicca **New Challenge** per giocare ad abbinare il colore.

## Colori di Sfondo e della Penna

Turtle ti permette di impostare due colori separati contemporaneamente.

- `t.pencolor("red")` — il colore delle linee che la tartaruga disegna
- `t.fillcolor("yellow")` — il colore usato per riempire le forme
- `turtle.bgcolor("lightblue")` — il colore di sfondo del canvas

Puoi anche impostare penna e riempimento insieme:

```python
t.color("blue", "yellow")   # pencolor = blue, fillcolor = yellow
```

## Riempire Forme con `begin_fill()` ed `end_fill()`

Per colorare una forma solida, racchiudi il tuo codice di disegno tra due chiamate:

1. `t.begin_fill()` — dice alla tartaruga "sto per disegnare una forma da riempire"
2. *disegna la forma*
3. `t.end_fill()` — sigilla la forma e la riempie con il colore di riempimento

Prima di guardare il codice, due punti chiave:
- Devi impostare il colore di riempimento *prima* di chiamare `begin_fill()`
- La forma deve essere chiusa (finire dove è iniziata) perché il riempimento appaia corretto

```python
import turtle
t = turtle.Turtle()
t.speed(6)

t.fillcolor("gold")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()
```

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `import turtle
t = turtle.Turtle()
t.speed(6)

t.fillcolor("gold")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()`);
</script>

Prova a cambiare `"gold"` con qualsiasi nome di colore o codice esadecimale. Prova a cambiare `6` in `3` per un triangolo o `5` per un pentagono.

## Le Basi della Teoria del Colore

Prima di mescolare colori sul canvas, capiamo alcuni termini della teoria del colore:

- **Tonalità (Hue)** — la famiglia base del colore (rosso, arancione, giallo, verde, blu, violetto)
- **Saturazione (Saturation)** — quanto è vivido o sbiadito il colore (100% = vivido, 0% = grigio)
- **Luminosità (Lightness)** — quanto è chiaro o scuro il colore (0% = nero, 100% = bianco)
- **Colori complementari** — colori opposti tra loro sulla ruota dei colori (ad es. rosso e verde, blu e arancione). Creano un forte contrasto quando sono posti fianco a fianco.

## Il Modello di Colore HSL

Il **modello di colore HSL** descrive i colori con tre valori: **Tonalità**, **Saturazione**, e **Luminosità**.
Molti designer preferiscono l'HSL perché è più facile da immaginare rispetto all'RGB:
"Voglio un blu moderatamente luminoso, leggermente verdastro" è naturale in HSL ma difficile in RGB.

La tartaruga di Python non supporta l'HSL direttamente, ma il concetto appare nel CSS e negli strumenti di editing delle immagini.
Puoi convertire HSL in RGB usando il modulo `colorsys` (trattato più avanti nel corso).

## Trasparenza e Alpha

In molti sistemi di disegno, il colore ha anche un valore **alpha** che controlla la trasparenza.
Un alpha di 1.0 significa completamente opaco (solido) e 0.0 significa completamente trasparente (invisibile).

La tartaruga di Python non supporta la trasparenza nativamente, ma le librerie di elaborazione delle immagini come Pillow (Capitolo 34) sì.
Per ora, sapere cosa significa alpha ti aiuterà quando lo incontrerai nel web design, negli editor di immagini, e nello sviluppo di giochi.

## Un Fiore Riempito

Combiniamo tutto: colore di riempimento, codici esadecimali, e cicli per creare un fiore colorato.

Prima del codice, nota che `t.circle(r, extent)` disegna un arco di un cerchio. Se `extent=360` è un cerchio completo; `extent=120` disegna un terzo di cerchio, che useremo come "petalo."

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `import turtle
t = turtle.Turtle()
t.speed(0)

petal_colors = ["#FF6347", "#FF8C00", "#FFD700", "#ADFF2F", "#00BFFF", "#9370DB"]

for i in range(6):
    t.fillcolor(petal_colors[i])
    t.begin_fill()
    t.circle(60, 120)   # arc
    t.left(60)
    t.circle(60, 120)   # arc
    t.left(60)
    t.end_fill()
    t.left(60)          # rotate to next petal

t.hideturtle()`);
</script>

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi le Righe Mancanti"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna il contorno di un quadrato rosso, ma dovrebbe essere riempito di blu.
    Aggiungi le tre righe mancanti — imposta il colore di riempimento, apri il riempimento, e chiudi il riempimento —
    per rendere il quadrato blu solido con un bordo rosso!

<div class="cm-lab">
  <div class="cm-editor-wrap">
    <div id="cm-editor-5"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-5')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-5')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-5"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-5"></div>
  </div>
</div>
<script>
initCmLab('-5', `import turtle
t = turtle.Turtle()
t.speed(6)
t.pencolor("red")
t.pensize(3)

# Add: set fill color to "blue"
# Add: begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
# Add: end_fill()`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Nella demo dei colori esadecimali, cambia `#FF0000` in `#FF8800`.
   **Saprai che ha funzionato quando** il primo quadrato diventa arancione.

2. Nella demo dei cerchi RGB, cambia la prima tupla in `(255, 165, 0)`.
   **Saprai che ha funzionato quando** il primo cerchio diventa arancione.

3. Nella demo dell'esagono riempito, aggiungi `turtle.bgcolor("navy")` prima del ciclo.
   **Saprai che ha funzionato quando** lo sfondo diventa blu scuro.

4. Nella demo dell'esagono riempito, aggiungi una riga `t.pencolor("#000000")` prima di `t.begin_fill()`.
   **Saprai che ha funzionato quando** l'esagono ha un contorno nero attorno al riempimento dorato.

5. Modifica il fiore così che ogni petalo sia dello stesso colore ma lo sfondo sia nero.
   **Saprai che ha funzionato quando** il tuo fiore monocolore risplende contro lo sfondo scuro.

!!! mascot-celebration "Lavoro Stupendo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato i codici esadecimali, l'RGB, l'HSL, i colori di riempimento, e i colori di sfondo!
    La tua arte con la tartaruga è ora a colori pieni e piena di vita.
    Continua a sperimentare — ogni grande artista digitale è iniziato esattamente dove sei tu ora!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
