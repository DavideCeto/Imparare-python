---
hide:
    - toc
---
# Tassellatura a Girandola

Alla fine di questo laboratorio sarai in grado di:

- Memorizzare un triangolo come tre punti d'angolo e dividerlo usando l'aritmetica dei vertici
- Usare una suddivisione ripetuta in stile ricorsivo per trasformare 4 triangoli in 500
- Colorare le forme in base al loro orientamento usando `atan2`

La tassellatura a girandola, scoperta da Charles Radin e John Conway, è costruita da una singola forma umile: un triangolo rettangolo con cateti 1 e 2 (e ipotenusa √5). Ogni triangolo si divide in 5 copie più piccole di se stesso, quelle si dividono in altre 5, e così via per sempre. La parte sorprendente: mentre continui a dividere, i triangoli finiscono per puntare in infinite direzioni diverse — il pattern non si assesta mai in una carta da parati ripetuta.

!!! mascot-welcome "Benvenuto alla Girandola!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Una forma di triangolo. Una regola di divisione. Applicala ancora e ancora
    e ottieni una tassellatura che i matematici hanno dimostrato NON si ripete MAI.
    Costruiamo subito tre cicli di questa!

## Come Funziona

Ogni triangolo è memorizzato come tre punti d'angolo `[a, b, c]` con l'angolo retto in `b`. La funzione `subdivide` trova il punto `h` che si trova all'80% del percorso lungo l'ipotenusa da `a` a `c`, più tre punti medi — e li usa per tagliare il triangolo in esattamente 5 triangoli rettangoli 1:2 più piccoli. Eseguiamo la suddivisione 3 volte su 4 triangoli di partenza, poi riempiamo ogni piccolo triangolo con un colore scelto dalla direzione verso cui punta.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def mid(p, q):
    return [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]

def subdivide(tri):
    a, b, c = tri
    h = [a[0] + 0.8 * (c[0] - a[0]), a[1] + 0.8 * (c[1] - a[1])]
    m1 = mid(a, h)
    m2 = mid(h, b)
    m3 = mid(a, b)
    return [[b, h, c], [a, m1, m3], [m1, h, m2], [m3, m2, b], [m2, m3, m1]]

levels = 3
tris = [[[-190, -190], [190, -190], [190, 0]],
        [[190, 0], [-190, 0], [-190, -190]],
        [[190, 0], [-190, 0], [-190, 190]],
        [[-190, 190], [190, 190], [190, 0]]]
for level in range(levels):
    new = []
    for t in tris:
        new.extend(subdivide(t))
    tris = new
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Iniziamo con 4 grandi triangoli, e ogni ciclo di suddivisione sostituisce
    ogni triangolo con 5 più piccoli. Dopo 3 cicli, quanti piccoli
    triangoli saranno sullo schermo? (Suggerimento: 4 × 5 × 5 × 5.) Indovina, poi esegui!

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

def mid(p, q):
    return [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]

def subdivide(tri):
    a, b, c = tri
    h = [a[0] + 0.8 * (c[0] - a[0]), a[1] + 0.8 * (c[1] - a[1])]
    m1 = mid(a, h)
    m2 = mid(h, b)
    m3 = mid(a, b)
    return [[b, h, c], [a, m1, m3], [m1, h, m2], [m3, m2, b], [m2, m3, m1]]

levels = 3
tris = [[[-190, -190], [190, -190], [190, 0]],
        [[190, 0], [-190, 0], [-190, -190]],
        [[190, 0], [-190, 0], [-190, 190]],
        [[-190, 190], [190, 190], [190, 0]]]
for level in range(levels):
    new = []
    for t in tris:
        new.extend(subdivide(t))
    tris = new

colors = ['gold', 'coral', 'mediumseagreen', 'royalblue', 'orchid', 'turquoise']
monty.pencolor('black')
monty.pensize(1)
for t in tris:
    a, b, c = t
    ang = math.degrees(math.atan2(a[1] - b[1], a[0] - b[0]))
    idx = int(round(ang)) % 360
    monty.fillcolor(colors[(idx // 60) % 6])
    monty.penup()
    monty.goto(a[0], a[1])
    monty.pendown()
    monty.begin_fill()
    monty.goto(b[0], b[1])
    monty.goto(c[0], c[1])
    monty.goto(a[0], a[1])
    monty.end_fill()`);
</script>

**500 triangoli** — 4 × 5³. Avevi indovinato? Nota come la metà superiore (costruita da triangoli di partenza rispecchiati) riceve persino colori diversi, perché i suoi triangoli puntano in direzioni diverse.

## Come Funziona

La chiave della suddivisione è il punto `h`, il piede dell'altezza abbassata dall'angolo retto `b` sull'ipotenusa. Per un triangolo rettangolo 1:2, `h` si trova sempre esattamente all'80% del percorso da `a` a `c` — questo singolo fatto separa una perfetta piccola copia (`[b, h, c]`). Il pezzo rimanente è una copia di dimensione doppia, che i tre punti medi tagliano in altri 4. Poiché le piccole copie sono inclinate dell'angolo irregolare `atan(1/2) ≈ 26,57°` (non un divisore "bello" di 360°), la suddivisione ripetuta continua a creare direzioni completamente nuove — questo è ciò che rende la tassellatura a girandola aperiodica.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `h = [a[0] + 0.8 * (c[0] - a[0]), ...]` | Trova il punto di divisione all'80% dell'ipotenusa |
| `return [[b, h, c], ...]` | Sostituisce un triangolo con le sue 5 copie più piccole |
| `new.extend(subdivide(t))` | Raccoglie tutti i pezzi di questo ciclo di divisione |
| `ang = math.degrees(math.atan2(...))` | Misura in quale direzione punta un triangolo, per la colorazione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Vai un Livello più in Profondità"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione inizia da UN solo grande triangolo e suddivide solo
    `levels = 2` volte, così puoi vedere chiaramente la divisione a 5 vie.
    Cambia in `levels = 3`. Quanti triangoli ti darà 1 × 5 × 5 × 5?

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

def mid(p, q):
    return [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]

def subdivide(tri):
    a, b, c = tri
    h = [a[0] + 0.8 * (c[0] - a[0]), a[1] + 0.8 * (c[1] - a[1])]
    m1 = mid(a, h)
    m2 = mid(h, b)
    m3 = mid(a, b)
    return [[b, h, c], [a, m1, m3], [m1, h, m2], [m3, m2, b], [m2, m3, m1]]

levels = 2
tris = [[[-180, -110], [180, -110], [180, 70]]]
for level in range(levels):
    new = []
    for t in tris:
        new.extend(subdivide(t))
    tris = new

colors = ['gold', 'coral', 'mediumseagreen', 'royalblue', 'orchid', 'turquoise']
monty.pencolor('black')
monty.pensize(1)
for t in tris:
    a, b, c = t
    ang = math.degrees(math.atan2(a[1] - b[1], a[0] - b[0]))
    idx = int(round(ang)) % 360
    monty.fillcolor(colors[(idx // 60) % 6])
    monty.penup()
    monty.goto(a[0], a[1])
    monty.pendown()
    monty.begin_fill()
    monty.goto(b[0], b[1])
    monty.goto(c[0], c[1])
    monty.goto(a[0], a[1])
    monty.end_fill()`);
</script>

`levels = 3` dà **125 triangoli** (5 × 5 × 5). Ogni livello extra moltiplica il conteggio per 5 e restringe ogni lato di un fattore √5.

## Esperimenti

1. **Allontana lo zoom.** Nel primo laboratorio, cambia `levels = 3` in `levels = 2`. Saprai che ha funzionato quando solo 100 grossi triangoli riempiono il quadrato e puoi tracciare a occhio ogni divisione a 5 vie.

2. **Nuovo set di colori.** Sostituisci `'gold'` con `'crimson'` e `'royalblue'` con `'midnightblue'`. Saprai che ha funzionato quando quei colori si scambiano ovunque nel mosaico contemporaneamente.

3. **Secchi di colore più fini.** Cambia `(idx // 60) % 6` in `(idx // 30) % 6`. Saprai che ha funzionato quando i triangoli vicini che prima condividevano un colore si dividono in colori diversi — adesso stai ordinando le direzioni in secchi di 30°.

4. **Metà del cielo.** Elimina gli ultimi due triangoli di partenza dalla lista `tris`. Saprai che ha funzionato quando solo il rettangolo inferiore è tassellato e la metà superiore del canvas resta bianca.

!!! mascot-celebration "Cinque Copie, per Sempre!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena costruito una tassellatura genuinamente aperiodica — 500 triangoli da una
    regola di divisione e un po' di aritmetica dei vertici. I matematici hanno avuto bisogno
    degli anni '90 per trovarla; tu l'hai disegnata in un browser!
    Prossimo: **Piastrella di Pesci in Stile Escher** — sagomare un pesce così perfettamente che le sue copie si incastrano senza spazi vuoti.
