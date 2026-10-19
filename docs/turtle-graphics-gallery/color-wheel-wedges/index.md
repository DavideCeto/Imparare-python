---
hide:
    - toc
---
# Spicchi della Ruota dei Colori

Alla fine di questo laboratorio sarai in grado di:

- Dividere 360° in angoli di spicchio uguali usando `360 / n`
- Disegnare forme a fetta di torta riempite usando `begin_fill()` con comandi avanti e rotazione
- Capire come le 12 tonalità della ruota dei colori si relazionano tra loro

Dodici spicchi riempiti si irradiano dal centro, ognuno di una tonalità diversa —
rosso, arancione, giallo, verde, blu, viola, e tutti i passaggi intermedi.

!!! mascot-welcome "Benvenuto alla Ruota dei Colori!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio scoprirai come disegnare fette di torta riempite e come tutte le 12 tonalità pure
    si adattano perfettamente attorno a un cerchio. Programmiamo insieme!

## Come Funzionano gli Spicchi

Ogni spicchio è un triangolo: due lati lunghi dal centro e un breve arco che chiude la punta.
Approssimiamo l'arco disegnando diversi piccoli passi avanti mentre giriamo leggermente.

Le 12 tonalità usate sono la ruota dei colori standard: `red`, `orange`, `yellow`, `chartreuse`,
`green`, `springgreen`, `cyan`, `deepskyblue`, `blue`, `purple`, `magenta`, `deeppink`.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

hues = ['red','orange','yellow','chartreuse','green','springgreen',
        'cyan','deepskyblue','blue','purple','magenta','deeppink']
radius = 180
wedge = 360 / 12

for hue in hues:
    monty.color(hue)
    monty.begin_fill()
    monty.forward(radius)
    monty.left(90)
    for _ in range(6):
        monty.forward(radius * 0.1)
        monty.left(5)
    monty.left(90)
    monty.forward(radius)
    monty.left(180 - wedge)
    monty.end_fill()
    # ruota di 30 gradi in senso antiorario fino allo spicchio successivo
    monty.left(30)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni spicchio si estende per `360 / 12 = 30°`. Quanti spicchi entreranno in un cerchio completo?
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

hues = ['red','orange','yellow','chartreuse','green','springgreen',
        'cyan','deepskyblue','blue','purple','magenta','deeppink']
radius = 180
wedge = 360 / 12

for hue in hues:
    monty.color(hue)
    monty.begin_fill()
    monty.forward(radius)
    monty.left(90)
    for _ in range(6):
        monty.forward(radius * 0.1)
        monty.left(5)
    monty.left(90)
    monty.forward(radius)
    monty.left(180 - wedge)
    monty.end_fill()
    # ruota di 30 gradi in senso antiorario fino allo spicchio successivo
    monty.left(30)`);
</script>

Esattamente **12 spicchi** — uno per tonalità, ognuno di 30°, per un totale di 360°. Avevi indovinato?

## Come Funziona

Ogni spicchio è disegnato come una fetta riempita simile a un triangolo: esce lungo un lato, traccia il piccolo arco che arrotonda il bordo, poi torna lungo l'altro lato verso il centro.

Due rotazioni alla fine fanno il lavoro importante. `monty.left(180 - wedge)` annulla la rotazione che Monty ha accumulato disegnando la fetta, riportandolo a puntare nella direzione in cui ha iniziato questo spicchio. Poi `monty.left(30)` — la riga che fa davvero espandere la ruota — lo ruota di un angolo di spicchio così la fetta successiva viene disegnata 30° più avanti. Dodici fette × 30° = 360°, un cerchio completo.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `hues = [...]` | Lista delle 12 tonalità standard della ruota dei colori |
| `wedge = 360 / 12` | Ogni fetta si estende per 30° |
| `monty.forward(radius)` | Disegna il primo lato dello spicchio verso l'esterno |
| `for _ in range(6)` | Approssima l'arco del bordo con 6 piccoli passi avanti+rotazione |
| `monty.forward(radius)` | Disegna il secondo lato di ritorno al centro |
| `monty.left(180 - wedge)` | Annulla la rotazione della fetta, tornando alla sua direzione di partenza |
| `monty.left(30)` | Ruota di uno spicchio (30°) verso la fetta successiva |

## Un Modo Più Breve: Usare `circle()`

Disegnare il bordo con sei piccoli passi `forward`/`left` ci ha mostrato *come*
viene costruito un arco. Ma le tartarughe Python hanno anche un comando integrato
`circle()` che disegna un arco per noi: `monty.circle(radius, wedge)` curva
attraverso `wedge` gradi lungo un cerchio del raggio dato. Quell'unica riga
sostituisce l'intero ciclo interno — **tutto il resto rimane esattamente lo
stesso**, incluse le due rotazioni che girano Monty verso la fetta successiva.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questo programma è più corto, ma fa lo stesso lavoro. Disegnerà la **stessa**
    ruota a 12 colori, una più piccola, o una forma completamente diversa?
    Prevedi, poi clicca Esegui.

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

hues = ['red','orange','yellow','chartreuse','green','springgreen',
        'cyan','deepskyblue','blue','purple','magenta','deeppink']
radius = 180
wedge = 360 / 12

for hue in hues:
    monty.color(hue)
    monty.begin_fill()
    monty.forward(radius)
    monty.left(90)
    monty.circle(radius, wedge)
    monty.left(90)
    monty.forward(radius)
    monty.left(180 - wedge)
    monty.end_fill()
    # ruota di 30 gradi in senso antiorario fino allo spicchio successivo
    monty.left(30)`);
</script>

Stessa ruota, meno righe! Poiché `circle()` fa atterrare Monty esattamente sul
bordo, questa versione ritorna persino precisamente al centro a ogni fetta.
Usa il metodo che preferisci — il ciclo disegnato a mano quando vuoi *vedere*
l'arco mentre viene costruito, e `circle()` quando vuoi solo una curva pulita
in una riga.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Una Variabile Controlla la Ruota"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione memorizza il conteggio delle fette in una variabile, `wedges`, e
    calcola `angle = 360 / wedges` da essa — così un numero imposta la larghezza
    dello spicchio, il bordo, e la rotazione insieme. Prevedi come sarà la ruota con
    `wedges = 5`, poi eseguila per scoprirlo!

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

hues = ['red','orange','yellow','chartreuse','green','springgreen',
        'cyan','deepskyblue','blue','purple','magenta','deeppink']

radius = 180
wedges = 5
angle = 360 / wedges

for hue in hues:
    monty.color(hue)
    monty.begin_fill()
    monty.forward(radius)
    monty.left(90)
    monty.circle(radius, angle)
    monty.left(90)
    monty.forward(radius)
    monty.left(180 - angle)
    monty.end_fill()
    # ruota di 60 gradi in senso antiorario fino allo spicchio successivo
    monty.left(angle)`);
</script>

Eseguilo: `wedges = 5` rende ogni fetta di 72°, e cinque fette riempiono già il cerchio — così il sesto colore (magenta) fa il giro della ruota e si sovrappone al primo (rosso), lasciando visibili cinque fette. Portare il conteggio in una variabile rende facile il riscalaggio: `angle = 360 / wedges` guida la larghezza dello spicchio, il bordo di `circle(radius, angle)`, e la rotazione `monty.left(angle)` tutti in una volta. Mantieni `wedges` uguale al numero di colori in `hues` e ogni tonalità ottiene la sua fetta netta.

## Esperimenti

1. **Prova 8 spicchi.** Usa 8 colori, cambia `360 / 12` in `360 / 8`, adatta l'arco interno a 4 passi × 11,25°, e cambia la rotazione finale in `monty.left(45)`. Saprai che ha funzionato quando 8 fette uguali riempiono il cerchio.

2. **Inclina tutta la ruota.** Aggiungi una singola riga `monty.left(15)` subito prima del ciclo `for`. Saprai che ha funzionato quando l'intera ruota è ruotata di 15° ma si chiude ancora in un cerchio completo.

3. **Riduci gli spicchi alterni.** Usa `for i, hue in enumerate(hues):`, poi imposta `r = radius` per `i` pari e `r = radius // 2` per `i` dispari. Usa `r` in entrambe le righe `forward(...)` e nel passo dell'arco `forward(r * 0.1)`. Saprai che ha funzionato quando spicchi lunghi e corti si alternano attorno alla ruota.

!!! mascot-celebration "Spettacolare!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai disegnato tutte le 12 tonalità della ruota dei colori e imparato come `360 / n` divide
    un cerchio in qualsiasi numero di fette uguali. Gli artisti usano questa stessa ruota ogni giorno!
    Prossimo: **Catena di Pentagoni** per esercitarti con la formula dell'angolo del poligono.
