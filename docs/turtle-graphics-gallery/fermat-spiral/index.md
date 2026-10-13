---
hide:
    - toc
---
# Spirale di Fermat

Alla fine di questo laboratorio sarai in grado di:

- Tracciare la spirale di Fermat `r = k * sqrt(theta)` usando `math.sqrt`
- Spiegare perché la crescita a radice quadrata fa avvicinare gli anelli man mano che si va verso l'esterno
- Usare il segno `±` per disegnare due braccia speculari da una singola equazione

La spirale di Fermat cresce con la *radice quadrata* dell'angolo, quindi ogni nuovo anello è impacchettato un po' più stretto del precedente — a differenza della spirale di Archimede dagli anelli equidistanti. E poiché l'equazione in realtà è `r = ±k*sqrt(θ)`, ha *due* braccia: un braccio più e un braccio meno, che si avvolgono fuori dall'origine in perfetta simmetria a 180°.

!!! mascot-welcome "Benvenuto alla Spirale di Fermat!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pierre de Fermat studiò questa spirale nel 1636 — e la natura l'ha
    amata per prima! Le infiorescenze dei semi di girasole impacchettano
    i loro semi lungo spirali di Fermat. Una radice quadrata, due
    braccia eleganti. Disegniamola!

## Come Funziona

Per ogni angolo `theta` da 0 a 8π (quattro giri completi), calcola `r = k * math.sqrt(theta)`, poi converti in `x = r * cos(theta)` e `y = r * sin(theta)`. Questo disegna il braccio *più*. Poi ripeti con `r = -k * math.sqrt(theta)`: un raggio negativo posiziona ogni punto esattamente dal lato opposto dell'origine, producendo un secondo braccio che è lo specchio a 180° del primo.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

k = 35
steps = 600
arms = [[1, 'crimson'], [-1, 'royalblue']]

monty.pensize(2)
for arm in arms:
    sign = arm[0]
    monty.pencolor(arm[1])
    monty.penup()
    for i in range(steps + 1):
        theta = 8 * math.pi * i / steps
        r = sign * k * math.sqrt(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `theta` va da 0 a `8 * math.pi`, e un giro completo è `2 * math.pi`.
    Quante volte complete si avvolgerà ogni braccio intorno al centro?
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

k = 35
steps = 600
arms = [[1, 'crimson'], [-1, 'royalblue']]

monty.pensize(2)
for arm in arms:
    sign = arm[0]
    monty.pencolor(arm[1])
    monty.penup()
    for i in range(steps + 1):
        theta = 8 * math.pi * i / steps
        r = sign * k * math.sqrt(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)`);
</script>

**4 giri** — `8π / 2π = 4` viaggi completi intorno al centro per ogni braccio. Avevi indovinato?

## Come Funziona

Guarda bene la spaziatura degli anelli: vicino al centro il divario tra un giro e il successivo è ampio, ma ogni anello più lontano è un po' più vicino a quello precedente. Questa è la radice quadrata all'opera. Dopo 1 giro il raggio è proporzionale a `sqrt(2π)`; dopo 4 giri è solo `sqrt(8π)` — due volte più grande, non quattro volte. La crescita continua a rallentare, così gli anelli si affollano insieme. Il braccio meno funziona perché un `r` negativo moltiplicato per `cos` e `sin` ribalta sia `x` che `y`, ruotando ogni punto esattamente di 180° intorno all'origine — un solo segno, uno specchio perfetto.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `r = sign * k * math.sqrt(theta)` | La regola di Fermat: il raggio cresce con la radice quadrata dell'angolo |
| `arms = [[1, 'crimson'], [-1, 'royalblue']]` | Il `±`: il segno `+1` e il segno `-1` danno le due braccia speculari |
| `theta = 8 * math.pi * i / steps` | Percorre l'angolo su quattro giri completi |
| `x = r * math.cos(theta)` | Da polari a cartesiane; un `r` negativo atterra a 180° oltre l'origine |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Aggiungi il Secondo Braccio"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna solo il braccio cremisi *più* — la
    lista `arms` ha una sola voce. Aggiungi **una voce alla lista** così
    appaia anche il braccio blu *meno*. Dove inizierà il braccio blu
    rispetto a quello rosso?

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

k = 35
steps = 600
arms = [[1, 'crimson']]

monty.pensize(2)
for arm in arms:
    sign = arm[0]
    monty.pencolor(arm[1])
    monty.penup()
    for i in range(steps + 1):
        theta = 8 * math.pi * i / steps
        r = sign * k * math.sqrt(theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        if i == 0:
            monty.goto(x, y)
            monty.pendown()
        else:
            monty.goto(x, y)`);
</script>

Cambia la lista in `arms = [[1, 'crimson'], [-1, 'royalblue']]` — il braccio blu inizia dalla stessa origine ma si avvolge fuori dal lato opposto, intrecciandosi perfettamente tra gli anelli rossi.

## Esperimenti

1. **Avvolgiti più lontano.** Cambia `8 * math.pi` in `18 * math.pi` e `k = 35` in `k = 24`. Saprai che ha funzionato quando ogni braccio fa 9 giri e gli anelli esterni sembrano quasi uniformemente impacchettati.

2. **Rompi la radice quadrata.** Cambia `math.sqrt(theta)` semplicemente in `theta` e imposta `k = 7`. Saprai che ha funzionato quando gli anelli diventano equidistanti — hai trasformato la spirale di Fermat in una spirale di Archimede.

3. **Cresci più in fretta invece.** Prova `r = sign * 1.2 * theta ** 1.5` (e mantieni 8π). Saprai che ha funzionato quando i divari si *allargano* verso l'esterno — l'opposto di Fermat.

4. **Puntini da girasole.** Elimina il blocco `if i == 0:`, mantieni la penna alzata per tutto il tempo, e dopo aver calcolato `x` e `y` chiama `monty.goto(x, y)` poi `monty.dot(5)`. Saprai che ha funzionato quando le braccia diventano file di semi come un'infiorescenza di girasole.

!!! mascot-celebration "Scienziato delle Spirali!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Crescita a radice quadrata, un segno ±, e coordinate polari — hai
    disegnato una curva vecchia di 400 anni che i girasoli stanno
    coltivando da sempre. Prossimo: **Astroide** — una stella a quattro
    punte nascosta dentro una famiglia di segmenti di linea scorrevoli.
