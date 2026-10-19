---
hide:
    - toc
---
# Triangolo Impossibile

Alla fine di questo laboratorio sarai in grado di:

- Disegnare un poligono riempito da una lista di punti (x, y) scritta direttamente nel codice
- Ruotare una lista di punti intorno al centro usando `sin` e `cos`
- Spiegare come tre sfumature di grigio simulino una profondità 3D in un oggetto che non può esistere

Il triangolo di Penrose — tre travi solide che si trovano ciascuna proprio davanti alla successiva, tutto intorno. Segui una trave qualsiasi con l'occhio e la geometria funziona; guarda l'intero oggetto ed è impossibile da costruire. Il trucco: una forma di trave, disegnata tre volte a 0°, 120° e 240°, in tre sfumature di grigio che il tuo cervello legge come illuminazione tridimensionale.

!!! mascot-welcome "Benvenuto al Triangolo Impossibile!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il matematico Roger Penrose chiamò questo "l'impossibilità nella sua
    forma più pura." Ogni angolo ha senso da solo — ma l'intero oggetto
    non potrebbe mai esistere. Lo costruiremo da UNA lista di cinque
    punti e un trucco di rotazione!

## Come Funziona

La lista `beam` contiene cinque punti (x, y) che delineano una trave a forma di L. La funzione `rotate()` fa girare un punto intorno al centro (0, 0) usando le formule standard di rotazione `rx = x*cos(a) - y*sin(a)` e `ry = x*sin(a) + y*cos(a)`. Un ciclo disegna la trave tre volte — ruotata di 0°, 120° e 240° — riempiendo ogni copia con un grigio più chiaro o più scuro. Poiché le tre forme condividono i bordi perfettamente, si intrecciano nella famosa figura impossibile.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

beam = [(0, 76), (101, -99), (137, -99), (154, -69), (36, 137)]
shades = ['#d8d8d8', '#989898', '#505050']

def rotate(point, angle):
    a = math.radians(angle)
    x = point[0]
    y = point[1]
    rx = x * math.cos(a) - y * math.sin(a)
    ry = x * math.sin(a) + y * math.cos(a)
    return (rx, ry)

def draw_beam(points, color):
    monty.penup()
    monty.goto(points[0][0], points[0][1])
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.pensize(2)
    monty.begin_fill()
    for p in points:
        monty.goto(p[0], p[1])
    monty.goto(points[0][0], points[0][1])
    monty.end_fill()

for i in range(3):
    angle = i * 120
    turned = [rotate(p, angle) for p in beam]
    draw_beam(turned, shades[i])
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Gli stessi cinque punti vengono disegnati tre volte, ruotati di 0°,
    120° e 240°. Le tre travi separate si allineeranno bordo a bordo in
    un unico triangolo chiuso, o ci saranno spazi vuoti tra loro?
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

beam = [(0, 76), (101, -99), (137, -99), (154, -69), (36, 137)]
shades = ['#d8d8d8', '#989898', '#505050']

def rotate(point, angle):
    a = math.radians(angle)
    x = point[0]
    y = point[1]
    rx = x * math.cos(a) - y * math.sin(a)
    ry = x * math.sin(a) + y * math.cos(a)
    return (rx, ry)

def draw_beam(points, color):
    monty.penup()
    monty.goto(points[0][0], points[0][1])
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.pensize(2)
    monty.begin_fill()
    for p in points:
        monty.goto(p[0], p[1])
    monty.goto(points[0][0], points[0][1])
    monty.end_fill()

for i in range(3):
    angle = i * 120
    turned = [rotate(p, angle) for p in beam]
    draw_beam(turned, shades[i])`);
</script>

Le tre travi si incontrano bordo a bordo senza spazi vuoti — e insieme formano un oggetto che non potrebbe mai esistere. Avevi indovinato?

## Come Funziona

Ogni trave sembra una barra 3D solida grazie all'ombreggiatura: il grigio chiaro si legge come una superficie rivolta verso la luce, il grigio scuro come una superficie in ombra. A ogni angolo, il taglio obliquo di una trave la fa sembrare scivolare *dietro* la sua vicina. Girando intorno al triangolo: la trave chiara copre quella scura, quella media copre quella chiara, e quella scura copre quella media. Quella catena circolare di "davanti a" non può mai accadere con oggetti reali — ogni trave dovrebbe trovarsi davanti a tutte le altre contemporaneamente.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `beam = [(0, 76), (101, -99), ...]` | Cinque punti scritti direttamente nel codice che delineano una trave a forma di L |
| `rx = x * math.cos(a) - y * math.sin(a)` | Formula di rotazione: fa girare un punto intorno a (0, 0) di un angolo `a` |
| `turned = [rotate(p, angle) for p in beam]` | Costruisce una nuova lista con ogni punto ruotato |
| `angle = i * 120` | Tre copie a 0°, 120°, 240° — perfetta simmetria a tre vie |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    In questa versione il triangolo è andato in pezzi — tre travi
    solitarie fluttuano con grandi spazi vuoti tra loro. Un numero nel
    ciclo finale è sbagliato. Suggerimento: tre copie devono condividere
    360° in parti uguali. Trovalo e correggilo!

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

beam = [(0, 76), (101, -99), (137, -99), (154, -69), (36, 137)]
shades = ['#d8d8d8', '#989898', '#505050']

def rotate(point, angle):
    a = math.radians(angle)
    x = point[0]
    y = point[1]
    rx = x * math.cos(a) - y * math.sin(a)
    ry = x * math.sin(a) + y * math.cos(a)
    return (rx, ry)

def draw_beam(points, color):
    monty.penup()
    monty.goto(points[0][0], points[0][1])
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.pensize(2)
    monty.begin_fill()
    for p in points:
        monty.goto(p[0], p[1])
    monty.goto(points[0][0], points[0][1])
    monty.end_fill()

for i in range(3):
    angle = i * 100
    turned = [rotate(p, angle) for p in beam]
    draw_beam(turned, shades[i])`);
</script>

Il bug è `angle = i * 100` — le copie atterrano a 0°, 100° e 200°, lasciando spazi vuoti. Tre copie uguali di qualunque cosa richiedono 360° ÷ 3 = 120° tra loro.

## Esperimenti

1. **Fai girare l'intera figura.** Cambia `angle = i * 120` in `angle = i * 120 + 60`. Saprai che ha funzionato quando l'intero triangolo ruota per puntare verso il basso, restando perfettamente unito.

2. **Cambia l'atmosfera con il colore.** Sostituisci la lista delle sfumature con `['#bcd4ec', '#5a8cc0', '#1e4a78']`. Saprai che ha funzionato quando il triangolo diventa di tre sfumature di blu e sembra ancora 3D.

3. **Ribalta l'illuminazione.** Inverti le sfumature in `['#505050', '#989898', '#d8d8d8']`. Saprai che ha funzionato quando l'ombra sembra provenire dal lato opposto — l'ordine "davanti a" sembra diverso?

4. **Rompi l'illusione di proposito.** Riempi tutte e tre le travi con la stessa sfumatura, `'#989898'`. Saprai che ha funzionato quando la figura si appiattisce in un semplice contorno triangolare 2D — prova che è l'ombreggiatura, non il contorno, a simulare il 3D.

5. **I colori del logo di Drive.** Questa stessa forma a tre travi è anche il contorno di base del logo del servizio di archiviazione online di un'azienda molto grande — il tipo di app che milioni di persone usano per salvare documenti e foto nel cloud. Cerca online quel logo e trova i suoi tre codici colore ufficiali RGB (o esadecimali), poi imposta `shades` con quello che hai trovato, per esempio `shades = ['#FFD14F', '#0EBC5F', '#2882FB']`. Saprai che ha funzionato quando il tuo "triangolo impossibile" comincerà a somigliare a un logo che hai già visto! *Un ringraziamento speciale a Sebastian B. per questa divertente aggiunta.*

    ??? question "Mostra soluzione"
        ```python
        import turtle
        import math
        monty = turtle.Turtle()
        monty.speed(0)
        monty.hideturtle()

        beam = [(0, 76), (101, -99), (137, -99), (154, -69), (36, 137)]
        shades = ['#FFD14F', '#0EBC5F', '#2882FB']

        def rotate(point, angle):
            a = math.radians(angle)
            x = point[0]
            y = point[1]
            rx = x * math.cos(a) - y * math.sin(a)
            ry = x * math.sin(a) + y * math.cos(a)
            return (rx, ry)

        def draw_beam(points, color):
            monty.penup()
            monty.goto(points[0][0], points[0][1])
            monty.pendown()
            monty.pencolor(color)
            monty.fillcolor(color)
            monty.pensize(2)
            monty.begin_fill()
            for p in points:
                monty.goto(p[0], p[1])
            monty.goto(points[0][0], points[0][1])
            monty.end_fill()

        for i in range(3):
            angle = i * 120
            turned = [rotate(p, angle) for p in beam]
            draw_beam(turned, shades[i])
        ```

!!! mascot-celebration "Hai Disegnato l'Indisegnabile!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Una lista di punti, una formula di rotazione, tre sfumature di
    grigio — e hai costruito un oggetto che non può esistere da nessuna
    parte nell'universo. Prossimo: **Pulsazione di Anelli Concentrici** —
    anelli di colori in contrasto che sembrano vibrare.
