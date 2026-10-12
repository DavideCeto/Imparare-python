---
hide:
    - toc
---
# Felce di Barnsley

Alla fine di questo laboratorio sarai in grado di:

- Usare la scelta casuale pesata per probabilità per applicare una delle quattro trasformazioni per passo
- Tracciare migliaia di punti con `dot()` per costruire gradualmente un'immagine
- Capire i Sistemi di Funzioni Iterate (IFS) — come alcune trasformazioni affini creano forme naturali

Dopo aver tracciato 5000 punti casuali, emerge una foglia di felce fotorealistica dalla pura matematica. Nessun ciclo di disegno, nessun ramo — solo quattro trasformazioni e probabilità.

!!! mascot-welcome "Benvenuto alla Felce di Barnsley!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Michael Barnsley scoprì nel 1988 che puoi generare forme di foglie realistiche
    da sole quattro semplici trasformazioni matematiche applicate casualmente.
    Questo laboratorio ti mostra come! Programmiamo insieme!

## Come Funziona

Quattro trasformazioni sono applicate casualmente, ognuna scelta con una probabilità fissa:
1. **Gambo** (1% di probabilità): `(x, y) → (0, 0.16y)`
2. **Foglioline piccole** (7%): `(x, y) → (0.85x + 0.04y, -0.04x + 0.85y + 1.6)`
3. **Fronda sinistra** (7%): `(x, y) → (0.2x - 0.26y, 0.23x + 0.22y + 1.6)`
4. **Fronda destra** (85%): `(x, y) → (-0.15x + 0.28y, 0.26x + 0.24y + 0.44)`

Iniziando a `(0, 0)`, applica una trasformazione casuale, traccia il punto, ripeti 5000 volte.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()
random.seed(42)

def next_point(x, y):
    r = random.random()
    if r < 0.01:
        return 0, 0.16 * y
    elif r < 0.86:
        return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
    elif r < 0.93:
        return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
    else:
        return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

x, y = 0, 0
scale = 35
for _ in range(5000):
    x, y = next_point(x, y)
    px = x * scale
    py = y * scale - 170
    monty.goto(px, py)
    monty.dot(2, 'forestgreen')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    5000 punti casuali posizionati uno alla volta — sembreranno casuali e dispersi,
    o emergerà una forma riconoscibile?
    Fai la tua previsione — poi clicca Esegui per scoprirlo! (Ci vorrà un momento.)

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()
random.seed(42)

def next_point(x, y):
    r = random.random()
    if r < 0.01:
        return 0, 0.16 * y
    elif r < 0.86:
        return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
    elif r < 0.93:
        return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
    else:
        return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

x, y = 0, 0
scale = 35
for _ in range(5000):
    x, y = next_point(x, y)
    px = x * scale
    py = y * scale - 170
    monty.goto(px, py)
    monty.dot(2, 'forestgreen')`);
</script>

Una **foglia di felce fotorealistica** emerge da punti casuali — nessun caos, solo la probabilità che rivela l'attrattore. Avevi indovinato?

## Come Funziona

Le quattro trasformazioni insieme formano un **Sistema di Funzioni Iterate (IFS)**. I 5000 punti convergono verso l'"attrattore strano" del sistema — l'insieme di punti che resta invariante sotto queste trasformazioni. Poiché le trasformazioni codificano la struttura auto-simile di una felce, l'attrattore sembra una felce.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `random.seed(42)` | Stesso seme → stessa sequenza "casuale" a ogni esecuzione |
| `r = random.random()` | Scegli una trasformazione per probabilità |
| `0.01 / 0.85 / 0.07 / 0.07` | Probabilità delle quattro trasformazioni |
| `scale = 35` | Fattore di scala: le coordinate IFS sono da -3 a 3 → coordinate del canvas |
| `dot(2, 'forestgreen')` | Traccia un piccolo punto verde |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Colore della Foglia"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `'forestgreen'` in `'mediumseagreen'` per il colore principale.
    Poi aggiungi un secondo passaggio con `dot(1, 'limegreen')` per aggiungere luci brillanti.
    Eseguilo due volte e confronta i colori!

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()
random.seed(42)

def next_point(x, y):
    r = random.random()
    if r < 0.01:
        return 0, 0.16 * y
    elif r < 0.86:
        return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
    elif r < 0.93:
        return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
    else:
        return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

x, y = 0, 0
scale = 35
for i in range(5000):
    x, y = next_point(x, y)
    px = x * scale
    py = y * scale - 170
    monty.goto(px, py)
    color = 'limegreen' if y > 6 else 'mediumseagreen'
    monty.dot(2, color)`);
</script>

Colorare per posizione y dà alla felce un gradiente naturale — più scuro alla base, più brillante alla punta — imitando come sembrano le vere foglie alla luce del sole.

## Esperimenti

1. **Raddoppia i punti.** Cambia `range(5000)` in `range(10000)`. La felce si riempie più densamente. Saprai che ha funzionato quando ci sono meno spazi vuoti nella foglia.

2. **Usa un seme diverso.** Cambia `random.seed(42)` in `random.seed(7)`. Il pattern esatto della felce cambia ma la forma generale resta la stessa.

3. **Cambia la dimensione del punto.** Prova `dot(3, 'forestgreen')`. Punti più grandi si riempiono più velocemente ma sembrano più grossolani. Saprai che ha funzionato quando la felce è più spessa.

4. **Stampa il primo punto.** Aggiungi `print(f"First point: {x:.3f}, {y:.3f}")` dentro il ciclo dopo la prima iterazione. Saprai che ha funzionato quando vedi la prima coordinata trasformata.

!!! mascot-celebration "Natura dai Numeri!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai fatto crescere una felce da quattro righe di matematica e un generatore di numeri casuali!
    I Sistemi di Funzioni Iterate sono usati nella compressione delle immagini e nell'arte procedurale.
    Prossimo: **Fiocco di Neve Anti-Koch** — sporgere verso l'interno invece che verso l'esterno.
