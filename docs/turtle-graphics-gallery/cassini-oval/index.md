---
hide:
    - toc
---
# Ovale di Cassini

Alla fine di questo laboratorio sarai in grado di:

- Tracciare ovali di Cassini — punti dove il *prodotto* delle distanze da due fuochi è uguale a `b * b`
- Usare la forma polare con una protezione per radice quadrata per gestire valori che non esistono
- Osservare una singola costante `b` cambiare l'intera topologia della curva: un ovale, una figura a otto, o due lobi separati

Un'ellisse mantiene costante la *somma* delle distanze da due punti focali. Un ovale di Cassini mantiene invece costante il *prodotto* — e quel singolo cambiamento crea una famiglia di forme mutevoli. A seconda di come `b` si confronta con la distanza focale `c`, ottieni un ovale a forma di arachide, una perfetta figura a otto (la lemniscata), o due lobi separati a forma di uovo.

!!! mascot-welcome "Benvenuto all'Ovale di Cassini!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    L'astronomo Giovanni Cassini pensava che i pianeti tracciassero queste
    curve. Si sbagliava sui pianeti — ma le curve sono straordinarie:
    sposta un numero e un singolo ovale *si lacera in due*!

## Come Funziona

Scegli due fuochi a `(-c, 0)` e `(c, 0)`. Un punto appartiene alla curva quando `distanza1 * distanza2 = b * b`. In coordinate polari questo diventa `r*r = c*c*cos(2*theta) + o - sqrt(c**4 * cos(2*theta)**2 + (b**4 - c**4))`. Per ogni angolo calcoliamo prima il valore sotto la radice quadrata — se è negativo, non esiste alcun punto a quell'angolo e lo saltiamo semplicemente. Poiché `r*r` può avere due risposte valide a un singolo angolo, disegniamo puntini sia per il ramo `+` che per quello `-` invece di trascinare una linea con la penna.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

c = 100
steps = 400

def draw_cassini(b, color):
    for i in range(steps):
        theta = 2 * math.pi * i / steps
        cos2 = math.cos(2 * theta)
        disc = c ** 4 * cos2 * cos2 + (b ** 4 - c ** 4)
        if disc < 0:
            continue
        root = math.sqrt(disc)
        for sign in [1, -1]:
            r2 = c * c * cos2 + sign * root
            if r2 > 0:
                r = math.sqrt(r2)
                monty.penup()
                monty.goto(r * math.cos(theta), r * math.sin(theta))
                monty.dot(3, color)

draw_cassini(120, 'royalblue')
draw_cassini(100, 'forestgreen')
draw_cassini(90, 'crimson')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    I fuochi si trovano a distanza `c = 100` dal centro, e disegniamo
    `b = 120`, `b = 100` e `b = 90`. Quale `b` dà la figura a otto: più
    grande di `c`, uguale a `c`, o più piccolo di `c`? Fai la tua
    ipotesi, poi clicca Esegui!

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

c = 100
steps = 400

def draw_cassini(b, color):
    for i in range(steps):
        theta = 2 * math.pi * i / steps
        cos2 = math.cos(2 * theta)
        disc = c ** 4 * cos2 * cos2 + (b ** 4 - c ** 4)
        if disc < 0:
            continue
        root = math.sqrt(disc)
        for sign in [1, -1]:
            r2 = c * c * cos2 + sign * root
            if r2 > 0:
                r = math.sqrt(r2)
                monty.penup()
                monty.goto(r * math.cos(theta), r * math.sin(theta))
                monty.dot(3, color)

draw_cassini(120, 'royalblue')
draw_cassini(100, 'forestgreen')
draw_cassini(90, 'crimson')

monty.penup()
monty.goto(-c, 0)
monty.dot(8, 'black')
monty.goto(c, 0)
monty.dot(8, 'black')

labels = [['b = 120 (un ovale)', 'royalblue'], ['b = 100 (un otto)', 'forestgreen'], ['b = 90 (due lobi)', 'crimson']]
for i in range(3):
    monty.goto(-185, 180 - 16 * i)
    monty.pencolor(labels[i][1])
    monty.write(labels[i][0])`);
</script>

**Uguale** — esattamente a `b = c` la curva verde si stringe attraverso il punto centrale, formando la famosa figura a otto chiamata lemniscata di Bernoulli. Avevi indovinato?

## Come Funziona

Pensa a un punto esattamente tra i due fuochi (l'origine). Le sue due distanze sono entrambe `c`, quindi il loro prodotto è `c * c`. Se il prodotto obiettivo `b * b` è più grande di quello, la curva ha spazio per passare sopra il centro e avvolge entrambi i fuochi in un'unica arachide blu. Se `b * b` è più piccolo, il centro è irraggiungibile — la curva deve restare vicina a un fuoco o all'altro, quindi si divide in due lobi cremisi. Esattamente a `b = c` la curva tocca *appena* l'origine: la figura a otto. Una costante che attraversa una soglia ribalta la topologia da un pezzo a due.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `disc = c ** 4 * cos2 * cos2 + (b ** 4 - c ** 4)` | Il valore sotto la radice quadrata — negativo significa nessun punto a questo angolo |
| `if disc < 0: continue` | La protezione: salta gli angoli dove la curva non esiste |
| `for sign in [1, -1]:` | Prova sia il ramo `+` che quello `-` — alcuni angoli hanno due raggi |
| `monty.dot(3, color)` | Disegna un puntino; i puntini gestiscono meglio delle linee di penna le curve che si dividono in pezzi |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Dividi l'Ovale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma qui sotto disegna un singolo ovale viola con `b = 130`.
    Cambia **un numero** così la curva si divide in due lobi separati.
    Ricorda la regola che hai appena imparato — `b` dovrebbe finire più
    grande o più piccolo di `c = 100`?

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

c = 100
b = 130
steps = 500

for i in range(steps):
    theta = 2 * math.pi * i / steps
    cos2 = math.cos(2 * theta)
    disc = c ** 4 * cos2 * cos2 + (b ** 4 - c ** 4)
    if disc < 0:
        continue
    root = math.sqrt(disc)
    for sign in [1, -1]:
        r2 = c * c * cos2 + sign * root
        if r2 > 0:
            r = math.sqrt(r2)
            monty.penup()
            monty.goto(r * math.cos(theta), r * math.sin(theta))
            monty.dot(3, 'purple')

monty.penup()
monty.goto(-c, 0)
monty.dot(8, 'black')
monty.goto(c, 0)
monty.dot(8, 'black')`);
</script>

Qualunque `b` *più piccolo* di `c` funziona — prova `b = 80` e l'ovale si lacera in due lobi, ciascuno abbracciato a un fuoco.

## Esperimenti

1. **Avvicinati alla divisione.** Prova `b = 101`, poi `b = 99`. Saprai che ha funzionato quando 101 dà un'arachide molto stretta e 99 dà due lobi uniti da quasi nulla.

2. **Riduci `b` ben sotto `c`.** Imposta `b = 60` nel programma della Verifica di Apprendimento. Saprai che ha funzionato quando i due lobi diventano piccole uova strette abbracciate ai puntini neri dei fuochi.

3. **Sposta i fuochi.** Cambia `c = 100` in `c = 60` nel programma principale. Saprai che ha funzionato quando tutte e tre le curve diventano ovali singoli — con i fuochi più vicini tra loro, ogni `b` è ora più grande di `c`, così anche la curva cremisi avvolge entrambi i fuochi.

4. **Conta gli angoli esistenti.** Aggiungi una variabile contatore, aggiungi 1 ogni volta che viene disegnato un puntino per `b = 90`, e fai un `print` alla fine. Saprai che ha funzionato quando il conteggio stampato nel pannello di output è molto inferiore a `steps * 2` — prova che la protezione ha saltato gli angoli impossibili.

!!! mascot-celebration "Cambiatore di Topologia!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai osservato una costante che attraversa una soglia strappare una
    singola curva in due pezzi — i matematici lo chiamano un cambiamento
    di *topologia*, e tu l'hai programmato con una sola protezione `if`.
    Prossimo: **Spirale di Fermat** — una radice quadrata manda due
    braccia speculari ad avvolgersi fuori dall'origine.
