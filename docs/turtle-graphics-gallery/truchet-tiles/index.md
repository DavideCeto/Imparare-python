---
hide:
    - toc
---
# Piastrelle di Truchet

Alla fine di questo laboratorio sarai in grado di:

- Riempire una griglia con tessere ad arco orientate casualmente usando `random.choice`
- Capire come le scelte casuali locali creano struttura globale inaspettata
- Vedere come due orientamenti di tessera con estremità di arco corrispondenti formano percorsi continui avvolgenti

Una griglia di tessere quadrate, ognuna contenente un arco `/` o un arco `\` scelto casualmente. Poiché gli archi delle tessere adiacenti si collegano ai loro bordi condivisi, il posizionamento casuale forma percorsi simili a fiumi vaganti che si avvolgono attraverso tutto il canvas.

!!! mascot-welcome "Benvenuto alle Piastrelle di Truchet!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni tessera è scelta casualmente — eppure i percorsi che formano sembrano progettati!
    Questa è l'emergenza: pattern globali complessi da semplici scelte casuali locali.
    Programmiamo insieme!

## Come Funziona

Ogni tessera è un quadrato di dimensione `s`. Due orientamenti:
- **Tipo A**: arco dall'angolo in basso a sinistra all'angolo in alto a destra (quarto di cerchio in basso a sinistra, poi in alto a destra)
- **Tipo B**: arco dall'angolo in alto a sinistra all'angolo in basso a destra

A ogni posizione della griglia, scegli casualmente A o B e disegna i due archi.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(5)

s = 40

def tile(x, y, t):
    monty.pensize(2)
    monty.pencolor('navy')
    monty.penup()
    if t == 'A':
        monty.goto(x, y)
        monty.setheading(0)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x + s, y + s)
        monty.setheading(180)
        monty.pendown()
        monty.circle(s/2, 90)
    else:
        monty.goto(x + s, y)
        monty.setheading(90)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x, y + s)
        monty.setheading(270)
        monty.pendown()
        monty.circle(s/2, 90)

cols, rows = 9, 8
ox = -cols * s / 2
oy = -rows * s / 2

for row in range(rows):
    for col in range(cols):
        t = random.choice(['A', 'B'])
        tile(ox + col * s, oy + row * s, t)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni tessera è scelta casualmente. Gli archi formeranno curve isolate, o percorsi collegati?
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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(5)

s = 40

def tile(x, y, t):
    monty.pensize(2)
    monty.pencolor('navy')
    monty.penup()
    if t == 'A':
        monty.goto(x, y)
        monty.setheading(0)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x + s, y + s)
        monty.setheading(180)
        monty.pendown()
        monty.circle(s/2, 90)
    else:
        monty.goto(x + s, y)
        monty.setheading(90)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x, y + s)
        monty.setheading(270)
        monty.pendown()
        monty.circle(s/2, 90)

cols, rows = 9, 8
ox = -cols * s / 2
oy = -rows * s / 2

for row in range(rows):
    for col in range(cols):
        t = random.choice(['A', 'B'])
        tile(ox + col * s, oy + row * s, t)`);
</script>

**Percorsi collegati e avvolgenti** — gli archi si uniscono ai bordi delle tessere per formare curve continue che vagano attraverso il canvas. Avevi indovinato?

## Come Funziona

Entrambi i tipi di tessera posizionano archi con estremità ai punti medi dei bordi della tessera. Poiché tutte le tessere usano gli stessi punti medi dei bordi, gli archi delle tessere adiacenti si collegano sempre — indipendentemente dall'orientamento scelto. La scelta casuale determina solo quali due paia di punti medi dei bordi sono collegati dagli archi di ogni tessera.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `random.seed(5)` | Casualità riproducibile — stesso pattern a ogni esecuzione |
| `random.choice(['A', 'B'])` | Scegli l'orientamento per ogni tessera |
| `circle(s/2, 90)` | Arco a quarto di cerchio con raggio metà della dimensione della tessera |
| `setheading(angle)` | Posiziona la tartaruga per iniziare l'arco dall'angolo corretto |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Seme"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `random.seed(5)` in `random.seed(42)`.
    Il pattern delle tessere cambierà ma i percorsi continueranno ad avvolgersi senza interruzioni.
    Eseguilo e confronta i due pattern!

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
random.seed(42)

s = 40

def tile(x, y, t):
    monty.pensize(2)
    monty.pencolor('darkred')
    monty.penup()
    if t == 'A':
        monty.goto(x, y)
        monty.setheading(0)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x + s, y + s)
        monty.setheading(180)
        monty.pendown()
        monty.circle(s/2, 90)
    else:
        monty.goto(x + s, y)
        monty.setheading(90)
        monty.pendown()
        monty.circle(s/2, 90)
        monty.penup()
        monty.goto(x, y + s)
        monty.setheading(270)
        monty.pendown()
        monty.circle(s/2, 90)

cols, rows = 9, 8
ox = -cols * s / 2
oy = -rows * s / 2

for row in range(rows):
    for col in range(cols):
        t = random.choice(['A', 'B'])
        tile(ox + col * s, oy + row * s, t)`);
</script>

Una disposizione completamente diversa di percorsi avvolgenti — ma tutti ancora collegati, dimostrando che la proprietà vale per qualsiasi seme.

## Esperimenti

1. **Aggiungi una griglia di sfondo.** Prima di posizionare le tessere, disegna linee di griglia grigie. Saprai che ha funzionato quando i confini delle tessere sono visibili.

2. **Rendi gli archi più spessi.** Cambia `pensize(2)` in `pensize(4)`. Saprai che ha funzionato quando i percorsi sembrano più marcati.

3. **Usa due colori.** Colora gli archi di tipo A rossi e quelli di tipo B blu. Saprai che ha funzionato quando puoi distinguere visivamente i due orientamenti.

4. **Rimuovi il seme.** Elimina `random.seed(5)`. Ogni esecuzione produrrà un pattern diverso. Saprai che ha funzionato quando il pattern cambia ogni volta che clicchi Esegui.

!!! mascot-celebration "Emergenza!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai creato struttura complessa da scelte casuali locali — questa è l'emergenza!
    Le piastrelle di Truchet furono progettate da Sébastien Truchet nel 1704 — e sorprendono ancora le persone oggi.
    Prossimo: **Stella Geometrica Islamica** — costruzione precisa da regole angolari.
