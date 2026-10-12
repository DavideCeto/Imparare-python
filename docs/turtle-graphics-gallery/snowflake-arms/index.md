---
hide:
    - toc
---
# Bracci del Fiocco di Neve

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `arm()` che disegna un ramo con rametti laterali
- Usare un ciclo con `left(60)` per ripetere il braccio sei volte attorno a un centro
- Riconoscere come la simmetria a sei pieghe è costruita da un'unità ripetuta

Sei bracci identici si irradiano dal centro, ognuno con due rami laterali più piccoli —
un fiocco di neve cristallino che cresce da una singola funzione riutilizzabile.

!!! mascot-welcome "Benvenuto ai Bracci del Fiocco di Neve!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I veri fiocchi di neve hanno simmetria a sei pieghe — ogni braccio è identico.
    In questo laboratorio disegnerai un braccio come funzione e la chiamerai sei volte per costruire tutto il cristallo!
    Programmiamo insieme!

## Come Funziona il Fiocco di Neve

La funzione `arm(length)` disegna un braccio: esce dal centro, aggiunge due piccoli rami laterali,
poi ritorna al centro. Chiamarla 6 volte con `left(60)` tra ogni chiamata
(6 × 60° = 360°) assembla il fiocco di neve completo.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.color('steelblue')

def arm(length):
    monty.forward(length)
    monty.left(45)
    monty.forward(length / 3)
    monty.backward(length / 3)
    monty.right(90)
    monty.forward(length / 3)
    monty.backward(length / 3)
    monty.left(45)
    monty.backward(length)

for i in range(6):
    arm(120)
    monty.left(60)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Dopo aver chiamato `arm()` e poi `left(60)`, sei volte, quanti gradi totali ha girato Monty?
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
monty.color('steelblue')

def arm(length):
    monty.forward(length)
    monty.left(45)
    monty.forward(length / 3)
    monty.backward(length / 3)
    monty.right(90)
    monty.forward(length / 3)
    monty.backward(length / 3)
    monty.left(45)
    monty.backward(length)

for i in range(6):
    arm(120)
    monty.left(60)`);
</script>

6 × 60° = **360°** — una rotazione completa, finendo esattamente dove Monty ha iniziato. Avevi indovinato?

## Come Funziona

Dentro `arm()`, la tartaruga esce, aggiunge rami laterali a ±45°, e ritorna:
- `forward(length)` — disegna il braccio principale
- `left(45)` poi `forward/backward` — disegna il rametto sinistro
- `right(90)` poi `forward/backward` — disegna il rametto destro
- `left(45)` poi `backward(length)` — ritorna al centro, rivolto nella direzione originale

La funzione riporta la tartaruga al suo **stato iniziale esatto** — stessa posizione, stessa direzione.
Questo è essenziale per far funzionare il ciclo: ogni chiamata ad `arm()` lascia Monty pronto per il prossimo `left(60)`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def arm(length)` | Un braccio del fiocco di neve — ramo principale più due rametti laterali |
| `monty.left(45)` | Gira di 45° per disegnare il rametto sinistro |
| `monty.right(90)` | Gira di 90° (oltre il centro) per disegnare il rametto destro |
| `monty.left(45)` | Ritorna alla direzione originale |
| `monty.backward(length)` | Ritorna al centro del fiocco di neve |
| `monty.left(60)` | Ruota di 60° — 6 × 60° = 360° per il fiocco di neve completo |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi Più Livelli di Rametti"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Alla funzione `arm()` sotto manca il rametto **destro** — viene disegnato solo quello sinistro!
    Aggiungi le **due righe mancanti** dentro `arm()` per disegnare il rametto destro corrispondente.

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
monty.color('steelblue')

def arm(length):
    monty.forward(length)
    monty.left(45)
    monty.forward(length / 3)
    monty.backward(length / 3)
    # ADD TWO LINES: turn to draw the right twig and return to center heading
    monty.left(45)
    monty.backward(length)

for i in range(6):
    arm(120)
    monty.left(60)`);
</script>

Aggiungi `monty.right(90)` poi `monty.forward(length / 3)` poi `monty.backward(length / 3)` — rispecchiando il rametto sinistro ma girando a destra invece.

## Esperimenti

1. **Cambia l'angolo dei rametti.** Sostituisci `left(45)` e `right(90)` con `left(30)` e `right(60)`. Saprai che ha funzionato quando i rametti sono più stretti, rendendo il fiocco di neve più spinoso.

2. **Fai un fiocco di neve a 4 bracci.** Cambia `range(6)` in `range(4)` e `left(60)` in `left(90)`. Saprai che ha funzionato quando il fiocco di neve ha quattro bracci ad angoli di 90° come un segno più.

3. **Colora ogni braccio diversamente.** Sposta `monty.color(...)` dentro il ciclo, scorrendo attraverso `['steelblue','white','lightblue']`. Saprai che ha funzionato quando ogni braccio è di una tonalità diversa.

4. **Aggiungi piccoli rametti finali.** Dentro `arm()`, prima di `backward(length)`, aggiungi rami laterali più piccoli alla posizione `length / 2`. Saprai che ha funzionato quando ogni braccio ha due set di rametti.

!!! mascot-celebration "Lavoro Bellissimo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un fiocco di neve a simmetria sei pieghe da una singola funzione braccio —
    lo stesso principio usato in tutto il design simmetrico, dai loghi ai mandala!
    Prossimo: **Canvas a Pois** — disperdere centinaia di punti colorati con `random`.
