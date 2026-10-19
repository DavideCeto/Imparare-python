---
hide:
    - toc
---
# Semaforo

Alla fine di questo laboratorio sarai in grado di:

- Scomporre un oggetto del mondo reale in primitive di disegno (rettangolo + cerchi)
- Scrivere una funzione `light(y, color)` e chiamarla tre volte per assemblare una scena
- Posizionare forme verticalmente usando un argomento di coordinata y

Un classico semaforo a tre luci si erge sullo schermo — rosso in alto, giallo nel mezzo,
verde in basso — costruito da un rettangolo e tre chiamate di funzione.

!!! mascot-welcome "Benvenuto al Semaforo!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni disegno complesso è in realtà solo forme semplici impilate insieme.
    In questo laboratorio decomporrai un semaforo in primitive e lo assemblerai con funzioni!
    Programmiamo insieme!

## Come Funziona il Semaforo

L'alloggiamento è un alto rettangolo scuro disegnato prima. Poi `light(y, color)` disegna un
cerchio riempito alla posizione verticale `y`. Tre chiamate a `light()` con valori y e colori diversi
impilano i tre segnali dentro l'alloggiamento.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

def light(y, color):
    monty.penup()
    monty.goto(0, y - 25)
    monty.dot(50, color)

rect(-35, -140, 70, 290, 'dimgray')
light(100,  'red')
light(  0,  'orange')
light(-100, 'green')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `light(y, color)` disegna un punto a `(0, y - 25)`. Perché sottrarre 25?
    Pensa a dove è centrato `dot()` prima di cliccare Esegui — poi controlla la tua risposta!

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

def rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

def light(y, color):
    monty.penup()
    monty.goto(0, y - 25)
    monty.dot(50, color)

rect(-35, -140, 70, 290, 'dimgray')
light(100,  'red')
light(  0,  'orange')
light(-100, 'green')`);
</script>

`dot()` è centrato sulla posizione della tartaruga. Sottrarre 25 (metà del diametro del punto di 50) sposta il centro per allinearsi visivamente con il valore y passato. Avevi indovinato?

## Come Funziona

Disegnare il rettangolo dell'alloggiamento **prima** assicura che appaia dietro le luci. Poiché i riempimenti sono opachi, i punti colorati disegnati dopo appaiono sopra il rettangolo grigio — stratificazione corretta senza nessun trucco extra.

L'aiutante `rect()` riutilizza lo stesso pattern `for side in [w, h, w, h]` visto nei laboratori del muro di mattoni e dello skyline — una volta che imparai un pattern, funziona ovunque.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `rect(x, y, w, h, color)` | Disegna un rettangolo riempito — riutilizzabile per qualsiasi forma a scatola |
| `rect(-35, -140, 70, 290, 'dimgray')` | L'alloggiamento: 70px di larghezza, 290px di altezza |
| `def light(y, color)` | Disegna un punto segnale alla posizione y data |
| `monty.dot(50, color)` | Cerchio riempito di diametro 50 alla posizione attuale |
| `light(100, 'red')` | Luce superiore (y più alto = più in alto sullo schermo) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi un Quarto Segnale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Alcuni segnali ferroviari hanno una **quarta** luce bianca in fondo.
    Aggiungi un'altra chiamata a `light()` per mettere un punto bianco a `y = -180`, ed estendi l'alloggiamento per adattarsi.

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

def rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    for side in [w, h, w, h]:
        monty.forward(side)
        monty.left(90)
    monty.end_fill()

def light(y, color):
    monty.penup()
    monty.goto(0, y - 25)
    monty.dot(50, color)

rect(-35, -190, 70, 380, 'dimgray')
light(150,  'red')
light( 50,  'orange')
light(-50, 'green')
# AGGIUNGI UNA RIGA: luce bianca a y = -150`);
</script>

Aggiungi `light(-150, 'white')` come ultima riga.

## Esperimenti

1. **Fai un semaforo pedonale.** Sostituisci le tre luci colorate con due — `light(60, 'red')` e `light(-60, 'green')`. Rendi l'alloggiamento più alto e stretto. Saprai che ha funzionato quando appare un segnale cammina/non camminare.

2. **Aggiungi un palo.** Prima di disegnare l'alloggiamento, disegna un rettangolo grigio sottile e alto dal fondo dell'alloggiamento al fondo del canvas. Saprai che ha funzionato quando il semaforo appare montato su un palo.

3. **Aggiungi anelli di luminescenza.** Prima di ogni chiamata a `dot()`, disegna un punto leggermente più grande in una tonalità più chiara dello stesso colore. Saprai che ha funzionato quando ogni luce sembra avere un'aureola.

4. **Mostra solo una luce attiva.** Cambia due dei colori delle luci in `'darkgray'` così solo una è "accesa". Saprai che ha funzionato quando due luci sono spente e una è luminosa.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai decomposto un oggetto del mondo reale in strati di primitive e l'hai assemblato
    con funzioni — esattamente il flusso di lavoro usato da ogni designer UI e artista di videogiochi!
    Prossimo: **Banco di Pesci** — disegnare la forma di una creatura con una funzione.
