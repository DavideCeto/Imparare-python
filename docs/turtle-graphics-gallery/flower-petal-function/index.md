---
hide:
    - toc
---
# Fiore con Funzione Petalo

Alla fine di questo laboratorio sarai in grado di:

- Definire una funzione che disegna un petalo e chiamarla più volte
- Passare **parametri** a una funzione per controllare dimensione e colore
- Usare la rotazione tra le chiamate di funzione per assemblare un fiore simmetrico

Otto petali — ognuno una coppia di archi — si irradiano dal centro, scorrendo
attraverso tonalità calde di rosa e magenta per formare un fiore in boccio.

!!! mascot-welcome "Benvenuto al Fiore con Funzione Petalo!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio scriverai una funzione `petal()` una volta e la chiamerai 8 volte.
    Questo è il potere delle funzioni — scrivila una volta, riutilizzala per sempre!
    Programmiamo insieme!

## Come Funziona il Fiore

La funzione `petal(size, color)` disegna un petalo usando due archi `circle()` rivolti in direzioni opposte.
Dopo ogni petalo, la tartaruga ruota di 45° così il petalo successivo punta in una nuova direzione.
8 petali × 45° = 360° — un fiore completo.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 60)
    monty.left(120)
    monty.circle(size, 60)
    monty.left(120)
    monty.end_fill()

colors = ['hotpink','deeppink','magenta','orchid',
          'hotpink','deeppink','magenta','orchid']

for i in range(8):
    petal(80, colors[i])
    monty.left(45)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo chiama `petal()` 8 volte, ruotando di 45° tra ogni chiamata.
    8 × 45° = 360°. Quanti petali appariranno nel fiore finito?
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

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 60)
    monty.left(120)
    monty.circle(size, 60)
    monty.left(120)
    monty.end_fill()

colors = ['hotpink','deeppink','magenta','orchid',
          'hotpink','deeppink','magenta','orchid']

for i in range(8):
    petal(80, colors[i])
    monty.left(45)`);
</script>

Esattamente **8 petali**, uno per chiamata. Avevi indovinato?

## Come Funziona

`monty.circle(size, 60)` disegna solo un arco di 60° di un cerchio — il secondo argomento è l'angolo dell'arco.
Due archi di 60° rivolti in direzioni opposte formano un petalo a forma di foglia.
Le due rotazioni `left(120)` sono la geometria che chiude il petalo tornando al punto di partenza.

La definizione della funzione `def petal(size, color):` avviene una volta prima del ciclo.
Dentro il ciclo, `petal(80, colors[i])` è la **chiamata** — esegue tutto il codice dentro la funzione con `size=80` e `color=colors[i]`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `def petal(size, color):` | Definisce una funzione riutilizzabile per disegnare un petalo |
| `monty.circle(size, 60)` | Disegna un arco di 60° di un cerchio del raggio dato |
| `monty.left(120)` | Gira per rivolgersi nella direzione opposta dell'arco |
| `petal(80, colors[i])` | Chiama la funzione con dimensione e colore specifici |
| `monty.left(45)` | Ruota di 45° così il petalo successivo punta in una nuova direzione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Rotazione"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 8 petali ma puntano tutti nella stessa direzione — tutti sovrapposti!
    Aggiungi **una riga** dentro il ciclo, dopo aver chiamato `petal()`, per ruotare di 45° prima del petalo successivo.

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

def petal(size, color):
    monty.color(color)
    monty.begin_fill()
    monty.circle(size, 60)
    monty.left(120)
    monty.circle(size, 60)
    monty.left(120)
    monty.end_fill()

colors = ['hotpink','deeppink','magenta','orchid',
          'hotpink','deeppink','magenta','orchid']

for i in range(8):
    petal(80, colors[i])
    # ADD ONE LINE HERE to rotate 45° before the next petal`);
</script>

La riga mancante è `monty.left(45)` — 8 petali × 45° = 360°, un fiore completo.

## Esperimenti

1. **Cambia il numero di petali.** Usa `range(6)` e `monty.left(60)`. Saprai che ha funzionato quando 6 petali formano una forma di fiore più semplice.

2. **Fai petali più grandi.** Chiama `petal(120, colors[i])` invece di `petal(80, ...)`. Saprai che ha funzionato quando i petali si estendono più lontano dal centro.

3. **Usa uno stelo verde.** Prima del ciclo, aggiungi `monty.color('green'); monty.pensize(4); monty.goto(0, -150); monty.penup()`. Saprai che ha funzionato quando appare una linea verde spessa sotto il fiore.

4. **Aggiungi un centro giallo.** Dopo il ciclo, aggiungi `monty.penup(); monty.goto(0, -20); monty.dot(40, 'yellow')`. Saprai che ha funzionato quando appare un cerchio giallo al centro dei petali.

!!! mascot-celebration "Lavoro Bellissimo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scritto la tua prima funzione parametrizzata e l'hai chiamata in un ciclo —
    questa è la base di tutto il codice riutilizzabile nella programmazione!
    Prossimo: **Griglia a Nido d'Ape** per vedere funzioni e tassellatura in azione.
