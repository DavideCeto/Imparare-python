---
hide:
    - toc
---
# Doppia Elica del DNA

Alla fine di questo laboratorio sarai in grado di:

- Tracciare un'onda sinusoidale punto per punto con `math.sin()`
- Spostare una seconda onda di 180° (`math.pi`) per creare due filamenti che si incrociano
- Collegare i punti corrispondenti con "pioli" per costruire la scala del DNA

Vista di lato, il DNA sembra una scala attorcigliata: due filamenti che si intrecciano uno sopra e uno sotto l'altro, uniti da pioli (le coppie di basi). Il segreto è pura trigonometria — i due filamenti sono la *stessa* onda sinusoidale, solo spostata di mezzo ciclo. (Questa è una bestia diversa dalla Spirale a Doppia Elica della galleria, che è una spirale della turtle in espansione — qui invece *tracciamo punti* con la matematica.)

!!! mascot-welcome "Benvenuto alla Doppia Elica!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nel 1953, la forma del DNA era uno dei più grandi rompicapo della
    scienza. Stai per disegnarla con due onde sinusoidali e uno
    spostamento di fase — la molecola della vita in meno di 40 righe
    di Python!

## Come Funziona

Entrambi i filamenti sono tracciati come sequenze di punti che attraversano il canvas: per il punto `i`, l'altezza è `amp * sin(theta + phase)` dove `theta` percorre 3 onde complete. Il filamento blu usa `phase = 0` e il filamento rosso usa `phase = math.pi` — uno spostamento di 180°, così dove un filamento è alto l'altro è basso, facendoli sembrare incrociati come una scala attorcigliata. I pioli grigi vengono disegnati prima: ogni 6° punto, una linea dritta collega l'altezza del filamento blu all'altezza del filamento rosso alla stessa x.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

amp = 70
waves = 3
points = 180
offset = math.pi

def strand_y(i, phase):
    theta = 2 * math.pi * waves * i / points + phase
    return amp * math.sin(theta)

def x_at(i):
    return -180 + 360.0 * i / points

monty.pencolor('gray')
monty.pensize(2)
for i in range(0, points + 1, 6):
    x = x_at(i)
    monty.penup()
    monty.goto(x, strand_y(i, 0))
    monty.pendown()
    monty.goto(x, strand_y(i, offset))

monty.pensize(4)
for strand in range(2):
    if strand == 0:
        phase = 0
        monty.pencolor('royalblue')
    else:
        phase = offset
        monty.pencolor('crimson')
    monty.penup()
    for i in range(points + 1):
        monty.goto(x_at(i), strand_y(i, phase))
        if i == 0:
            monty.pendown()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il filamento rosso è il filamento blu spostato di 180°.
    Quando il filamento blu è nel suo punto **più alto**, dove sarà
    il filamento rosso — in alto insieme a lui, nel mezzo, o nel suo
    punto **più basso**? Fai la tua ipotesi, poi clicca Esegui!

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

amp = 70
waves = 3
points = 180
offset = math.pi

def strand_y(i, phase):
    theta = 2 * math.pi * waves * i / points + phase
    return amp * math.sin(theta)

def x_at(i):
    return -180 + 360.0 * i / points

monty.pencolor('gray')
monty.pensize(2)
for i in range(0, points + 1, 6):
    x = x_at(i)
    monty.penup()
    monty.goto(x, strand_y(i, 0))
    monty.pendown()
    monty.goto(x, strand_y(i, offset))

monty.pensize(4)
for strand in range(2):
    if strand == 0:
        phase = 0
        monty.pencolor('royalblue')
    else:
        phase = offset
        monty.pencolor('crimson')
    monty.penup()
    for i in range(points + 1):
        monty.goto(x_at(i), strand_y(i, phase))
        if i == 0:
            monty.pendown()`);
</script>

Nel suo punto più basso — `sin(theta + pi)` è sempre l'esatto opposto di `sin(theta)`. Questa danza a immagine speculare è ciò che fa sembrare attorcigliata la scala. Avevi indovinato?

## Come Funziona

Questo è *plotting parametrico*: invece di guidare la turtle con `forward()` e `left()`, calcoliamo le coordinate di ogni punto da un parametro `i` e ci saltiamo con `goto()`. L'identità `sin(theta + pi) = -sin(theta)` fa sì che i due filamenti siano riflessi perfetti, così si incrociano ovunque `sin(theta) = 0`. Nota che i pioli sono più lunghi a metà strada tra gli incroci (dove i filamenti sono lontani) e si restringono a zero a ogni incrocio — nessun codice extra necessario, lo fa automaticamente la geometria. Disegnare i pioli *prima* dei filamenti mantiene le linee grigie ordinatamente dietro al blu e al rosso.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `theta = 2 * math.pi * waves * i / points + phase` | Fa percorrere a theta 3 onde complete mentre i aumenta |
| `return amp * math.sin(theta)` | Trasforma l'angolo in un'altezza tra -70 e +70 |
| `offset = math.pi` | Spostamento di fase di 180° — tutto il segreto dell'aspetto a elica |
| `for i in range(0, points + 1, 6):` | Ogni 6° punto ottiene un piolo grigio tra i filamenti |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Rompi la Fase"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nel programma qui sotto, `offset` è stato cambiato da `math.pi` a `0`,
    così entrambi i filamenti ottengono la **stessa** fase. Prevedi: come
    appariranno i pioli, e quanti filamenti separati vedrai? Eseguilo, poi
    riporta `offset = math.pi` per riparare il DNA!

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

amp = 70
waves = 3
points = 180
offset = 0

def strand_y(i, phase):
    theta = 2 * math.pi * waves * i / points + phase
    return amp * math.sin(theta)

def x_at(i):
    return -180 + 360.0 * i / points

monty.pencolor('gray')
monty.pensize(2)
for i in range(0, points + 1, 6):
    x = x_at(i)
    monty.penup()
    monty.goto(x, strand_y(i, 0))
    monty.pendown()
    monty.goto(x, strand_y(i, offset))

monty.pensize(4)
for strand in range(2):
    if strand == 0:
        phase = 0
        monty.pencolor('royalblue')
    else:
        phase = offset
        monty.pencolor('crimson')
    monty.penup()
    for i in range(points + 1):
        monty.goto(x_at(i), strand_y(i, phase))
        if i == 0:
            monty.pendown()`);
</script>

Con `offset = 0` ogni piolo collega un punto a se stesso (lunghezza zero!) e il filamento rosso si disegna esattamente sopra quello blu — un'onda solitaria, nessuna elica. Lo spostamento di 180° non è decorazione; *è* la doppia elica.

## Esperimenti

1. **Attorciglia più stretto.** Cambia `waves = 3` in `waves = 5`. Saprai che ha funzionato quando i filamenti si incrociano 10 volte invece di 6.

2. **Aggiungi più coppie di basi.** Cambia il passo dei pioli da `6` a `3` in `range(0, points + 1, 6)`. Saprai che ha funzionato quando la scala ha il doppio dei pioli grigi.

3. **Schiaccia la molecola.** Cambia `amp = 70` in `amp = 35`. Saprai che ha funzionato quando l'elica diventa un nastro stretto attraverso il mezzo del canvas.

4. **Prova un quarto di giro.** Cambia `offset = math.pi` in `offset = math.pi / 2`. Saprai che ha funzionato quando i filamenti continuano a intrecciarsi ma i pioli non si restringono mai del tutto a zero — uno spostamento di 90° non lascia mai incontrare i filamenti.

!!! mascot-celebration "Hai Decifrato il Codice!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Due onde sinusoidali, uno spostamento di fase, qualche piolo grigio —
    e la molecola più famosa della biologia appare sul tuo schermo.
    Prossimo: **Mappa Topografica** — colora l'elevazione di un'isola con
    anelli di curve di livello ondulati, dalle rive verdi a una vetta
    bianca di neve.
