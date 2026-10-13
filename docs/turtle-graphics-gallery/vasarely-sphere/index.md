---
hide:
    - toc
---
# Sfera di Vasarely

Alla fine di questo laboratorio sarai in grado di:

- Disegnare una griglia regolare di punti con cicli annidati
- Misurare la distanza di ogni punto dal centro con `math.sqrt`
- Mappare la distanza sulla dimensione del punto così una griglia piatta sembra rigonfiarsi in una sfera 3D

Una griglia di punti perfettamente regolare — tranne che dentro un cerchio centrale, i punti si gonfiano in base a quanto sono vicini al centro. Quel singolo cambiamento fa sembrare che una sfera spinga fuori dalla pagina piatta. L'artista ungherese-francese Victor Vasarely, il "nonno dell'op art," usò esattamente questo trucco nei suoi famosi dipinti *Vega*.

!!! mascot-welcome "Benvenuto alla Sfera di Vasarely!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni punto in questa immagine si trova esattamente su una griglia
    piatta e quadrata. Eppure una sfera 3D si rigonfierà proprio verso di
    te! Victor Vasarely ha trasformato questo trucco in arte famosa in
    tutto il mondo — ora tocca a te.

## Come Funziona

Due cicli annidati posizionano un punto ogni 28 pixel in una griglia 13 × 13. Per ogni punto calcoliamo la sua distanza `d` dal centro usando il teorema di Pitagora: `d = sqrt(x*x + y*y)`. Se il punto è dentro il raggio `R`, calcoliamo un fattore di rigonfiamento con `cos(d / R * pi / 2)` — vale 1 al centro e svanisce a 0 al bordo — e aggiungiamo `bulge * swell` alla dimensione del punto. I punti fuori da `R` restano piccoli, così la sfera si trova dentro una griglia calma e piatta.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

spacing = 28
n = 6
R = 130
base = 9
bulge = 16

for row in range(-n, n + 1):
    for col in range(-n, n + 1):
        x = col * spacing
        y = row * spacing
        d = math.sqrt(x * x + y * y)
        size = base
        if d < R:
            swell = math.cos(d / R * math.pi / 2)
            size = base + bulge * swell
        monty.goto(x, y)
        monty.dot(int(size), 'navy')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La spaziatura della griglia non cambia mai — solo la **dimensione**
    del punto cambia. Il centro dell'immagine sembrerà una zona piatta
    di punti più grandi, o una palla 3D che spinge fuori dalla pagina?
    Fai la tua ipotesi, poi clicca Esegui!

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
monty.penup()

spacing = 28
n = 6
R = 130
base = 9
bulge = 16

for row in range(-n, n + 1):
    for col in range(-n, n + 1):
        x = col * spacing
        y = row * spacing
        d = math.sqrt(x * x + y * y)
        size = base
        if d < R:
            swell = math.cos(d / R * math.pi / 2)
            size = base + bulge * swell
        monty.goto(x, y)
        monty.dot(int(size), 'navy')`);
</script>

La maggior parte delle persone vede una palla che si rigonfia fuori dalla pagina — il tuo cervello legge "più grande" come "più vicino" e costruisce automaticamente la forma 3D. Avevi indovinato?

## Come Funziona

Il tuo sistema visivo indovina costantemente la profondità dalla dimensione: le cose più vicine sembrano più grandi. Quando la dimensione del punto cresce in modo liscio verso il centro, la spiegazione più semplice per il tuo cervello è che la superficie stessa si sta curvando verso di te — quindi percepisce una sfera. La funzione coseno è il segreto: cambia lentamente vicino al centro e velocemente vicino al bordo, esattamente come la superficie di una vera palla che si inclina lontano da te.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `for row in range(-n, n + 1):` | I cicli annidati visitano tutte le 13 × 13 = 169 posizioni della griglia |
| `d = math.sqrt(x * x + y * y)` | Distanza pitagorica dal punto al centro |
| `swell = math.cos(d / R * math.pi / 2)` | 1 al centro, svanisce a 0 al bordo del rigonfiamento |
| `size = base + bulge * swell` | Mappa la distanza sulla dimensione del punto — l'intera illusione in una riga |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione calcola `swell` ma non lo **usa** mai, quindi la
    sfera è sparita — ogni punto resta della stessa dimensione. Aggiungi
    **una riga** dentro il blocco `if` (subito dopo che `swell` viene
    calcolato) per riportare indietro il rigonfiamento!

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
monty.penup()

spacing = 28
n = 6
R = 130
base = 9
bulge = 16

for row in range(-n, n + 1):
    for col in range(-n, n + 1):
        x = col * spacing
        y = row * spacing
        d = math.sqrt(x * x + y * y)
        size = base
        if d < R:
            swell = math.cos(d / R * math.pi / 2)
        monty.goto(x, y)
        monty.dot(int(size), 'navy')`);
</script>

La riga mancante è `size = base + bulge * swell` — senza di essa, `swell` viene calcolato e buttato via, e ogni punto mantiene la dimensione base.

## Esperimenti

1. **Rendi il rigonfiamento più forte.** Cambia `bulge = 16` in `bulge = 22`. Saprai che ha funzionato quando i punti centrali quasi si toccano e la sfera sembra ancora più rotonda.

2. **Crea un'ammaccatura invece di un rigonfiamento.** Cambia la riga della dimensione in `size = base + bulge - bulge * swell` così i punti *si restringono* verso il centro. Saprai che ha funzionato quando la griglia sembra ammaccarsi lontano da te.

3. **Fai crescere la sfera.** Cambia `R = 130` in `R = 180`. Saprai che ha funzionato quando il rigonfiamento inghiotte quasi tutta la griglia, lasciando piatti solo gli angoli.

4. **Sposta la sfera fuori centro.** Cambia la riga della distanza in `d = math.sqrt((x - 56) * (x - 56) + y * y)`. Saprai che ha funzionato quando il rigonfiamento scivola verso il lato destro della griglia.

!!! mascot-celebration "Hai Fatto Rigonfiare la Carta Piatta!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Un'istruzione `if` e un coseno hanno trasformato una noiosa griglia
    in op art 3D — la stessa matematica che Vasarely usava nelle gallerie
    di tutto il mondo. Prossimo: **Griglia Scintillante** — punti bianchi
    che lampeggiano neri quando non stai guardando.
