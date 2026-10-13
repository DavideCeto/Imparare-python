---
hide:
    - toc
---
# Epitrocoide

Alla fine di questo laboratorio sarai in grado di:

- Tracciare un'epitrocoide — la curva lasciata da una penna su un cerchio che rotola *all'esterno* di un cerchio più grande
- Spiegare come la differenza di segno tra `(R + r)` e `(R - r)` separa il rotolamento esterno da quello interno
- Prevedere il numero di anelli dal rapporto `R / r`

Un piccolo cerchio di raggio `r` rotola intorno all'*esterno* di un grande cerchio di raggio `R`, con una penna attaccata a distanza `d` dal centro del cerchio piccolo. La penna traccia anelli simili a fiori chiamati epitrocoide — il cugino a rotolamento esterno dell'ipotrocoide dello Spirografo.

!!! mascot-welcome "Benvenuto all'Epitrocoide!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nel laboratorio dello Spirografo un cerchio rotolava intorno
    all'*interno* di un anello. Questa volta il cerchio piccolo rotola
    intorno all'*esterno* — e solo due cambi di segno nella matematica
    ribaltano l'intero pattern!

## Come Funziona

Al tempo `t`, il centro del cerchio piccolo si trova a distanza `R + r` dall'origine (i due cerchi si toccano, quindi i loro centri sono separati da un raggio grande più un raggio piccolo). La penna oscilla intorno a quel centro mobile, dando:

`x = (R + r) * cos(t) - d * cos((R + r) / r * t)`
`y = (R + r) * sin(t) - d * sin((R + r) / r * t)`

Confronta con lo Spirografo (ipotrocoide): il rotolamento interno usa `(R - r)` e `+ d` nella riga `x`. Quella differenza di segno è l'intera distinzione tra rotolare dentro e rotolare fuori. La curva forma `R / r` anelli prima di chiudersi.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

R = 100
r = 20
d = 40
steps = 1200
colors = ['crimson', 'darkorange', 'gold', 'forestgreen', 'royalblue']

monty.pensize(2)
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R + r) * math.cos(t) - d * math.cos((R + r) / r * t)
    y = (R + r) * math.sin(t) - d * math.sin((R + r) / r * t)
    monty.pencolor(colors[(i * 5) // (steps + 1)])
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La curva forma `R / r` anelli prima di chiudersi. Con `R = 100` e
    `r = 20`, quanti anelli vedrai? Fai la tua ipotesi, poi clicca Esegui!

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

R = 100
r = 20
d = 40
steps = 1200
colors = ['crimson', 'darkorange', 'gold', 'forestgreen', 'royalblue']

monty.pensize(2)
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R + r) * math.cos(t) - d * math.cos((R + r) / r * t)
    y = (R + r) * math.sin(t) - d * math.sin((R + r) / r * t)
    monty.pencolor(colors[(i * 5) // (steps + 1)])
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**5 anelli** — `R / r = 100 / 20 = 5`, e ogni anello ottiene il suo colore. Avevi indovinato?

## Come Funziona

Ogni volta che il cerchio piccolo rotola una volta intorno al proprio centro, la penna oscilla fuori e dentro — quella oscillazione è un anello. Rotolare intorno all'esterno del cerchio grande richiede esattamente `R / r = 5` di quelle oscillazioni, quindi la curva si chiude dopo 5 anelli. La distanza della penna `d` controlla quanto è drammatico ogni anello: `d` più grande di `r` dà grandi anelli aperti, `d` più piccolo di `r` dà protuberanze dolci, e `d` uguale a `r` dà punte acute (quel caso speciale si chiama epicicloide).

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `x = (R + r) * math.cos(t) - d * math.cos((R + r) / r * t)` | Centro del cerchio rotolante più l'oscillazione della penna — `(R + r)` significa rotolare *all'esterno* |
| `d = 40` | Spostamento della penna dal centro del cerchio piccolo; `d` più grande significa anelli più grandi |
| `(R + r) / r * t` | Quanto velocemente gira la penna — il cerchio rotolante gira 6 volte per giro completo |
| `colors[(i * 5) // (steps + 1)]` | Divide i 1200 passi in 5 fasce di colore, una per anello |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Fai Rotolare il Cerchio all'Interno"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto usa gli *stessi* `R`, `r` e `d`, ma questa è la
    formula dello Spirografo (rotolamento interno). Eseguilo e confrontalo
    con la curva sopra. Poi convertilo nell'epitrocoide a rotolamento
    esterno: cambia ogni `(R - r)` in `(R + r)` e il `+ d` nella riga `x`
    in `- d`. In che direzione punteranno gli anelli dopo la tua modifica?

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

R = 100
r = 20
d = 40
steps = 1200

monty.pencolor('purple')
monty.pensize(2)
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
    y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

La curva a rotolamento interno ripiega i suoi 5 anelli *verso l'interno* e resta piccola; dopo i tuoi cambi di segno gli anelli si ribaltano *verso l'esterno* e l'intera curva cresce — stessi tre numeri, rotolamento opposto.

## Esperimenti

1. **Cambia `r = 20` in `r = 25`.** Ora `R / r = 4`. Saprai che ha funzionato quando la curva si chiude con esattamente 4 anelli.

2. **Imposta `d = 20` (uguale a `r`).** Saprai che ha funzionato quando gli anelli rotondi si affinano in 5 punte acute — un'epicicloide.

3. **Prova `d = 10` (più piccolo di `r`).** Saprai che ha funzionato quando gli anelli si appiattiscono in 5 protuberanze dolci senza incroci.

4. **Imposta `r = 30` così `R / r` non è un numero intero.** Cambia `2 * math.pi` in `6 * math.pi` così la curva ha tempo di chiudersi. Saprai che ha funzionato quando 10 anelli si intrecciano prima che la curva si incontri da sola.

!!! mascot-celebration "Rotolando all'Esterno!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena scoperto che un solo segno più-o-meno decide se un cerchio
    rotola dentro o fuori — e cambia completamente l'immagine.
    Prossimo: **Superellisse** — un esponente che trasforma una stella in
    un cerchio in un quadrato arrotondato.
