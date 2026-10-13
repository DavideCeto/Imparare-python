---
hide:
    - toc
---
# Superellisse

Alla fine di questo laboratorio sarai in grado di:

- Tracciare la famiglia delle superellissi `|x/a|^n + |y/b|^n = 1` usando la sua forma parametrica
- Mostrare come un esponente `n` trasformi una forma da stella a cerchio a quadrato arrotondato
- Scrivere una semplice istruzione `if` per mantenere il segno di un valore mentre si eleva il suo valore assoluto a una potenza

Un'equazione, tre forme completamente diverse. La regola della superellisse `|x/a|^n + |y/b|^n = 1` disegna una stella appuntita a quattro braccia quando `n` è piccolo, un cerchio perfetto a `n = 2`, e un quadrato arrotondato sempre più squadrato mentre `n` cresce. I designer la adorano — la forma a quadrato arrotondato "squircle" delle icone delle app è una superellisse.

!!! mascot-welcome "Benvenuto alla Superellisse!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Un cerchio è `x*x + y*y = 1` — l'esponente è 2. Ma chi ha detto che
    debba essere 2? Alza o abbassa l'esponente e il cerchio si trasforma
    in stelle e squircle. Un solo numero controlla l'intera famiglia!

## Come Funziona

Percorriamo `t` intorno a un cerchio e deformiamo ogni punto con l'esponente: `x = a * sign(cos t) * |cos t|^(2/n)` e `y = b * sign(sin t) * |sin t|^(2/n)`. La parte `sign` ricorda in quale quadrante siamo (un semplice `if` lo imposta a `1` o `-1`), e la potenza `2/n` fa la trasformazione. Blocchiamo i valori assoluti con un piccolo epsilon così non calcoliamo mai una potenza frazionaria di esattamente zero.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

a = 160
b = 160
steps = 360

def draw_superellipse(n, color):
    monty.pencolor(color)
    monty.penup()
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        c = math.cos(t)
        s = math.sin(t)
        sign_c = 1
        if c < 0:
            sign_c = -1
        sign_s = 1
        if s < 0:
            sign_s = -1
        ac = abs(c)
        if ac < 0.000001:
            ac = 0.000001
        av = abs(s)
        if av < 0.000001:
            av = 0.000001
        x = a * sign_c * ac ** (2.0 / n)
        y = b * sign_s * av ** (2.0 / n)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)

monty.pensize(2)
draw_superellipse(0.8, 'crimson')
draw_superellipse(2, 'forestgreen')
draw_superellipse(4, 'royalblue')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Appariranno tre curve: `n = 0.8`, `n = 2` e `n = 4`.
    Quale assomiglierà di più a un quadrato — l'`n` più piccolo o il più grande?
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

a = 160
b = 160
steps = 360

def draw_superellipse(n, color):
    monty.pencolor(color)
    monty.penup()
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        c = math.cos(t)
        s = math.sin(t)
        sign_c = 1
        if c < 0:
            sign_c = -1
        sign_s = 1
        if s < 0:
            sign_s = -1
        ac = abs(c)
        if ac < 0.000001:
            ac = 0.000001
        av = abs(s)
        if av < 0.000001:
            av = 0.000001
        x = a * sign_c * ac ** (2.0 / n)
        y = b * sign_s * av ** (2.0 / n)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)

monty.pensize(2)
draw_superellipse(0.8, 'crimson')
draw_superellipse(2, 'forestgreen')
draw_superellipse(4, 'royalblue')

labels = [['n = 0.8', 'crimson'], ['n = 2', 'forestgreen'], ['n = 4', 'royalblue']]
monty.penup()
for i in range(3):
    monty.goto(-185, 175 - 16 * i)
    monty.pencolor(labels[i][1])
    monty.write(labels[i][0])`);
</script>

L'`n` **più grande** — la curva blu `n = 4` si rigonfia verso gli angoli come un quadrato arrotondato, mentre la curva cremisi `n = 0.8` si restringe verso l'interno in una stella. Avevi indovinato?

## Come Funziona

L'esponente `2/n` rimodella il cerchio. A `n = 2` la potenza è esattamente 1, quindi nulla cambia — un cerchio perfetto. Quando `n > 2` la potenza è *minore* di 1, il che spinge i valori intermedi di coseno e seno verso 1, ingrassando la curva verso gli angoli — più grande diventa `n`, più ci si avvicina a un vero quadrato. Quando `n < 2` la potenza è *maggiore* di 1, il che schiaccia i valori intermedi verso 0, risucchiando i lati verso gli assi e lasciando una stella appuntita. Tutte e tre le curve si toccano esattamente negli stessi quattro punti sugli assi, perché lì il coseno o il seno vale 1 e qualunque potenza di 1 resta 1.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `x = a * sign_c * ac ** (2.0 / n)` | La superellisse parametrica: mantieni il segno, eleva la grandezza alla potenza `2/n` |
| `if c < 0: sign_c = -1` | Un semplice `if` implementa la funzione segno — nessun trucco necessario |
| `if ac < 0.000001: ac = 0.000001` | Blocco epsilon così non eleviamo mai esattamente 0 a una potenza frazionaria |
| `draw_superellipse(4, 'royalblue')` | Una funzione, chiamata tre volte — questa è una *famiglia* parametrica |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Questo programma dovrebbe disegnare uno squircle completo `n = 4` —
    ma quando lo esegui, appare solo la metà superiore! Una delle due
    istruzioni `if` del segno è scomparsa. Trova il punto e aggiungi le
    due righe mancanti.

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

a = 150
b = 150
n = 4
steps = 360

monty.pencolor('royalblue')
monty.pensize(3)
monty.penup()
for i in range(steps + 1):
    t = 2 * math.pi * i / steps
    c = math.cos(t)
    s = math.sin(t)
    sign_c = 1
    if c < 0:
        sign_c = -1
    sign_s = 1
    ac = abs(c)
    if ac < 0.000001:
        ac = 0.000001
    av = abs(s)
    if av < 0.000001:
        av = 0.000001
    x = a * sign_c * ac ** (2.0 / n)
    y = b * sign_s * av ** (2.0 / n)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

`sign_s` viene impostato a `1` ma non viene mai ribaltato — aggiungi `if s < 0:` e `    sign_s = -1` subito sotto, e `y` potrà finalmente diventare negativo per disegnare la metà inferiore.

## Esperimenti

1. **Crea una vera famiglia di ellissi.** Cambia `b = 160` in `b = 100`. Saprai che ha funzionato quando tutte e tre le forme si schiacciano in versioni larghe — stella, ellisse e rettangolo arrotondato.

2. **Vai all'estremo: aggiungi `draw_superellipse(10, 'purple')`.** Saprai che ha funzionato quando una forma viola abbraccia l'esterno, assomigliando quasi esattamente a un quadrato con piccolissimi angoli arrotondati.

3. **Vai appuntito: aggiungi `draw_superellipse(0.5, 'darkorange')`.** Saprai che ha funzionato quando appare una stella arancione a quattro braccia dentro quella cremisi, con punte ancora più acute.

4. **Disegna l'intera trasformazione.** Sostituisci le tre chiamate con un ciclo: `for n10 in range(8, 41, 4):` poi `draw_superellipse(n10 / 10.0, 'gray')`. Saprai che ha funzionato quando nove curve grigie si aprono a ventaglio dolcemente da stella a squircle.

!!! mascot-celebration "Maestro dello Squircle!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai trasformato una stella in un cerchio in un quadrato arrotondato
    girando una sola manopola — l'esponente `n`. Questo è il potere di
    una famiglia parametrica: una formula, forme infinite.
    Prossimo: **Ovale di Cassini** — guarda un ovale dividersi in due
    mentre una singola costante cambia.
