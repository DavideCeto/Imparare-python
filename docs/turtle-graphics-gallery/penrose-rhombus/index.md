---
hide:
    - toc
---
# Tassellatura a Rombi di Penrose

Alla fine di questo laboratorio sarai in grado di:

- Usare i numeri complessi come punti 2D per fare geometria con l'aritmetica semplice
- Applicare due regole di suddivisione ricorsiva (sottile → 2 pezzi, spesso → 3 pezzi)
- Spiegare perché il rapporto aureo fa in modo che questa tassellatura non si ripeta mai

Negli anni '70, Roger Penrose scoprì due forme di rombo — una spessa, una sottile — che possono tassellare un pavimento per sempre senza che il pattern si ripeta mai. Questo programma costruisce la sua famosa tassellatura P3 per "deflazione": inizia con un sole di 10 triangoli aurei attorno al centro, poi suddivide ripetutamente ogni triangolo in triangoli aurei più piccoli usando il rapporto aureo φ ≈ 1,618. Quattro cicli dopo, rombi dorati e blu fioriscono in stelle e soli su tutto il canvas.

!!! mascot-welcome "Benvenuto alla Tassellatura Che Non si Ripete Mai!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Due forme di rombo, due regole di divisione, un numero magico: φ.
    Fai scorrere questo pattern in qualsiasi direzione e NON si allineerà
    mai con se stesso. Facciamolo crescere da dieci triangoli!

## Come Funziona

Ogni triangolo è memorizzato come `[kind, a, b, c]` dove gli angoli sono numeri complessi — `complex(x, y)` agisce come un punto 2D, e `a + (b - a) / phi` trova il punto che divide il lato `ab` secondo il rapporto aureo. Un mezzo-rombo *sottile* si divide in 2 triangoli più piccoli; uno *spesso* si divide in 3. Dopo aver suddiviso 4 volte, riempiamo ogni triangolo (spesso = oro, sottile = blu reale) e poi tracciamo solo i due lati esterni `c → a → b`, così ogni coppia di triangoli appare come un unico rombo completo.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

phi = (1 + math.sqrt(5)) / 2

triangles = []
for i in range(10):
    a1 = (2 * i - 1) * math.pi / 10
    a2 = (2 * i + 1) * math.pi / 10
    b = complex(math.cos(a1), math.sin(a1)) * 195
    c = complex(math.cos(a2), math.sin(a2)) * 195
    if i % 2 == 0:
        b, c = c, b
    triangles.append(['thin', complex(0, 0), b, c])

levels = 4
for level in range(levels):
    new = []
    for kind, a, b, c in triangles:
        if kind == 'thin':
            p = a + (b - a) / phi
            new.append(['thin', c, p, b])
            new.append(['thick', p, c, a])
        else:
            q = b + (a - b) / phi
            r = b + (c - b) / phi
            new.append(['thick', r, c, a])
            new.append(['thick', q, r, b])
            new.append(['thin', r, q, a])
    triangles = new
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni ciclo, ogni triangolo sottile diventa 2 pezzi ma ogni triangolo spesso
    diventa 3. Dopo 4 cicli di questo, quale colore pensi che coprirà di più
    l'immagine — oro (spesso) o blu reale (sottile)? Indovina, poi esegui!

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

phi = (1 + math.sqrt(5)) / 2

triangles = []
for i in range(10):
    a1 = (2 * i - 1) * math.pi / 10
    a2 = (2 * i + 1) * math.pi / 10
    b = complex(math.cos(a1), math.sin(a1)) * 195
    c = complex(math.cos(a2), math.sin(a2)) * 195
    if i % 2 == 0:
        b, c = c, b
    triangles.append(['thin', complex(0, 0), b, c])

levels = 4
for level in range(levels):
    new = []
    for kind, a, b, c in triangles:
        if kind == 'thin':
            p = a + (b - a) / phi
            new.append(['thin', c, p, b])
            new.append(['thick', p, c, a])
        else:
            q = b + (a - b) / phi
            r = b + (c - b) / phi
            new.append(['thick', r, c, a])
            new.append(['thick', q, r, b])
            new.append(['thin', r, q, a])
    triangles = new

for kind, a, b, c in triangles:
    if kind == 'thin':
        monty.fillcolor('royalblue')
    else:
        monty.fillcolor('gold')
    monty.penup()
    monty.goto(a.real, a.imag)
    monty.begin_fill()
    monty.goto(b.real, b.imag)
    monty.goto(c.real, c.imag)
    monty.goto(a.real, a.imag)
    monty.end_fill()

monty.pencolor('#333333')
monty.pensize(1)
for kind, a, b, c in triangles:
    monty.penup()
    monty.goto(c.real, c.imag)
    monty.pendown()
    monty.goto(a.real, a.imag)
    monty.goto(b.real, b.imag)`);
</script>

**Vince l'oro.** Dopo 4 cicli ci sono 210 mezzi-rombi spessi e solo 130 sottili — e ogni rombo spesso è anche più "grasso". (Curiosità: il rapporto spesso-sottile si avvicina esattamente a φ man mano che continui a suddividere.) Avevi indovinato?

## Come Funziona

I due tipi di triangolo sono le metà dei due rombi di Penrose: il rombo sottile (angoli di 36°) e il rombo spesso (angoli di 72°). I tagli al rapporto aureo come `a + (b - a) / phi` dividono ognuno in copie più piccole perfette — funziona solo perché i lati di un triangolo aureo sono in rapporto φ : φ : 1. Poiché φ è irrazionale, i numeri di tessere spesse e sottili non possono mai assestarsi in un rapporto ordinato di numeri intieri, quindi nessuna copia spostata del pattern può mai corrispondere a se stessa: la tassellatura è aperiodica. Nota la simmetria a 5 punte ovunque — la "simmetria proibita" che le normali carte da parati ripetute non possono avere. Quando gli scienziati trovarono questo stesso pattern a 5 punte congelato in una lega metallica nel 1982 (li chiamarono quasicristalli), valse a Dan Shechtman il Premio Nobel.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `phi = (1 + math.sqrt(5)) / 2` | Il rapporto aureo, 1,618... — il motore di tutta la tassellatura |
| `b = complex(math.cos(a1), math.sin(a1)) * 195` | Posiziona un angolo su un cerchio usando un numero complesso come punto (x, y) |
| `p = a + (b - a) / phi` | Taglia il lato `ab` nel punto del rapporto aureo |
| `new.append(['thick', p, c, a])` | Aggiunge uno dei triangoli più piccoli che sostituisce quello vecchio |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Deflaziona più in Profondità"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione si ferma a `levels = 2`, così puoi ancora vedere i dieci grandi
    spicchi del sole di partenza. Cambialo in `levels = 4`.
    Ogni ciclo restringe i rombi di un fattore φ — il pattern al centro
    sembrerà ancora un sole quando avrai finito?

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

phi = (1 + math.sqrt(5)) / 2

triangles = []
for i in range(10):
    a1 = (2 * i - 1) * math.pi / 10
    a2 = (2 * i + 1) * math.pi / 10
    b = complex(math.cos(a1), math.sin(a1)) * 195
    c = complex(math.cos(a2), math.sin(a2)) * 195
    if i % 2 == 0:
        b, c = c, b
    triangles.append(['thin', complex(0, 0), b, c])

levels = 2
for level in range(levels):
    new = []
    for kind, a, b, c in triangles:
        if kind == 'thin':
            p = a + (b - a) / phi
            new.append(['thin', c, p, b])
            new.append(['thick', p, c, a])
        else:
            q = b + (a - b) / phi
            r = b + (c - b) / phi
            new.append(['thick', r, c, a])
            new.append(['thick', q, r, b])
            new.append(['thin', r, q, a])
    triangles = new

for kind, a, b, c in triangles:
    if kind == 'thin':
        monty.fillcolor('royalblue')
    else:
        monty.fillcolor('gold')
    monty.penup()
    monty.goto(a.real, a.imag)
    monty.begin_fill()
    monty.goto(b.real, b.imag)
    monty.goto(c.real, c.imag)
    monty.goto(a.real, a.imag)
    monty.end_fill()

monty.pencolor('#333333')
monty.pensize(1)
for kind, a, b, c in triangles:
    monty.penup()
    monty.goto(c.real, c.imag)
    monty.pendown()
    monty.goto(a.real, a.imag)
    monty.goto(b.real, b.imag)`);
</script>

Sì — un sole più piccolo di dieci rombi dorati sopravvive esattamente al centro, ora circondato da stelle blu. La deflazione restringe il pattern ma il motivo del sole continua a riapparire a ogni scala.

## Esperimenti

1. **Un ciclo in più.** Nel primo laboratorio, cambia `levels = 4` in `levels = 5` (aspetta qualche secondo — sono 890 triangoli). Saprai che ha funzionato quando i rombi si restringono di nuovo e appaiono nuove stelle a cinque punte che prima non erano visibili.

2. **Modalità notturna.** Scambia i colori: rendi il sottile `'gold'` e lo spesso `'midnightblue'`. Saprai che ha funzionato quando la tassellatura si ribalta in prevalenza scura con contorni di stelle dorate.

3. **Mostra i triangoli nascosti.** Nel ciclo di disegno dei bordi in fondo, aggiungi `monty.goto(c.real, c.imag)` come riga finale dentro il ciclo. Saprai che ha funzionato quando appare una cucitura attraverso ogni rombo, rivelando i due triangoli di cui è realmente fatto.

4. **Restringi il sole.** Cambia entrambi i `* 195` in `* 120`. Saprai che ha funzionato quando l'intero decagono si ritira verso il centro con spazio bianco intorno.

!!! mascot-celebration "Simmetria Proibita Sbloccata!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Due forme, due regole, e il rapporto aureo — e hai disegnato un pattern
    che non si ripete mai, con la simmetria a 5 punte che i cristalli non
    avrebbero mai dovuto avere. Penrose lo dimostrò; tu lo hai programmato!
    Sfoglia la **Galleria della Grafica Turtle** per la tua prossima sfida!
