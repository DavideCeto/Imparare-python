# Tracciare un'Onda Sinusoidale

Alla fine di questa lezione sarai in grado di:

- Importare la libreria `math` e usare `math.sin()` per calcolare valori seno
- Usare un ciclo `for` con `goto()` per tracciare una funzione matematica attraverso il canvas
- Modificare l'ampiezza e il colore dell'onda cambiando due variabili

Le grafiche turtle non servono solo per le forme — puoi usarle per **tracciare funzioni matematiche**. La tartaruga visita centinaia di punti lungo l'asse x, calcola il valore y per ciascuno, e li collega con `goto()`. Il risultato sembra un grafico, disegnato dal vivo.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Sapevi che Python può disegnare la matematica? Oggi traccerai un'onda sinusoidale — la forma delle onde dell'oceano,
    del suono, e della luce — direttamente nel browser. Programmiamo insieme!

## La Funzione Seno

La **funzione seno** `math.sin(angolo)` prende un angolo in **radianti** e restituisce un valore tra -1 e 1. Un'onda sinusoidale completa va da 0 fino a 1, torna giù attraverso 0 fino a -1, e torna su a 0 — una curva lisciata a forma di S.

Due passi per tracciarla con turtle:
1. Scorri `x` da -180 a 180
2. Converti `x` in radianti con `math.radians(x)`, poi chiama `math.sin()` per ottenere `y`
3. Moltiplica `y` per un'**ampiezza** (come 80) per scalarla alla dimensione del canvas
4. Usa `goto(x, y * amplitude)` per muovere la tartaruga

```python
import math
for x in range(-180, 180):
    y = math.sin(math.radians(x))
    monty.goto(x, y * 80)
```

## Codice di Esempio

```python
import turtle
import math

monty = turtle.Turtle()
monty.shape('turtle')
monty.speed(10)

amplitude = 80
monty.color('blue')
monty.pensize(2)

monty.penup()
monty.goto(-180, 0)
monty.pendown()

for x in range(-180, 180):
    y = math.sin(math.radians(x))
    monty.goto(x, y * amplitude)

monty.hideturtle()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La tartaruga visiterà 360 punti da x = -180 a x = 179 e disegnerà una linea attraverso tutti.
    Che forma ti aspetti di vedere? Sembrerà liscia o frastagliata?
    Fai la tua previsione — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato direttamente su questa pagina.
Nessun account necessario — tutto gira nel tuo browser.

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
monty.shape('turtle')
monty.speed(10)

amplitude = 80
monty.color('blue')
monty.pensize(2)

monty.penup()
monty.goto(-180, 0)
monty.pendown()

for x in range(-180, 180):
    y = math.sin(math.radians(x))
    monty.goto(x, y * amplitude)

monty.hideturtle()`);
</script>

Avevi indovinato? Una curva a S liscia distesa attraverso il canvas — un ciclo completo della funzione seno, scalata a 80 pixel di altezza.

## Come Funziona

`math.radians(x)` converte i gradi in radianti (l'unità che `math.sin()` si aspetta). Il valore restituito è tra -1 e 1, quindi moltiplicarlo per `amplitude` (80) lo allunga a ±80 pixel — un'onda visibile.

Iniziare con `penup()` e `goto(-180, 0)` posiziona la tartaruga sul bordo sinistro dell'onda senza disegnare prima una linea lì. Poi `pendown()` fa iniziare l'onda esattamente a x = -180.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `import math` | Carica la libreria matematica (fornisce `sin`, `cos`, `radians`, ecc.) |
| `amplitude = 80` | Controlla quanto è alta l'onda — più grande = più alta |
| `math.radians(x)` | Converte i gradi in radianti (richiesto da `math.sin`) |
| `math.sin(...)` | Restituisce un valore tra -1 e 1 per quell'angolo |
| `y * amplitude` | Scala il valore alle coordinate del canvas |
| `monty.goto(x, y * amplitude)` | Muove la tartaruga al punto successivo sulla curva |

!!! mascot-tip "Prova Anche math.cos()"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Sostituisci `math.sin` con `math.cos` e guarda come si sposta l'onda.
    L'onda coseno è identica in forma al seno ma spostata a sinistra di 90 gradi —
    quindi invece di iniziare a 0 inizia al suo picco!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Disegna Due Onde"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna un'onda sinusoidale. Aggiungi **quattro righe** dopo che finisce il primo ciclo per:
    alzare la penna (`penup`), tornare a `(-180, 0)`, abbassare la penna (`pendown`),
    e disegnare un secondo ciclo in `'red'` usando `math.cos` invece di `math.sin`.

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
monty.speed(10)

amplitude = 80
monty.pensize(2)

monty.color('blue')
monty.penup()
monty.goto(-180, 0)
monty.pendown()

for x in range(-180, 180):
    y = math.sin(math.radians(x))
    monty.goto(x, y * amplitude)

# Aggiungi qui delle righe per tornare alla posizione iniziale e disegnare un'onda coseno rossa
monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice dell'onda sinusoidale. Prevedi prima, poi esegui!

1. Cambia `amplitude = 80` in `amplitude = 160`.
   **Saprai che ha funzionato quando** l'onda è il doppio alta e i picchi arrivano quasi alla cima del canvas.

2. Cambia `amplitude = 80` in `amplitude = 30`.
   **Saprai che ha funzionato quando** l'onda è molto più piatta — quasi una linea retta.

3. Sostituisci `math.sin` con `math.cos`.
   **Saprai che ha funzionato quando** l'onda inizia al suo picco (y = amplitude) invece che a zero.

4. Cambia `range(-180, 180)` in `range(-360, 360, 2)` (passo di 2).
   **Saprai che ha funzionato quando** vedi due cicli completi dell'onda attraverso il canvas.

5. Moltiplica i radianti per `2` prima di passarli a `math.sin`: `math.sin(math.radians(x) * 2)`.
   **Saprai che ha funzionato quando** l'onda completa due cicli completi nello stesso intervallo di x.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai tracciato una funzione matematica con turtle — stai scrivendo lo stesso tipo di codice che scienziati
    e ingegneri usano per visualizzare dati! Prova a combinare sin e cos nello stesso ciclo per pattern interessanti.
    Programmiamo insieme!
