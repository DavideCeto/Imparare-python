---
hide:
    - toc
---
# Nome ad Albero Binario

Alla fine di questo laboratorio sarai in grado di:

- Convertire una lettera in un numero con `ord()` ed estrarre i suoi bit binari con `//` e `%`
- Tracciare un percorso giù per un albero binario — sinistra per 0, destra per 1
- Disegnare la stessa struttura a ogni livello usando cicli annidati

Ogni lettera nel tuo nome è segretamente un numero, e ogni numero è segretamente una stringa di bit. Questo laboratorio disegna un albero binario a cinque livelli, poi traccia ogni lettera di un nome giù per l'albero — ramificando a sinistra per ogni bit 0 e a destra per ogni bit 1. Ogni lettera atterra sulla propria foglia!

!!! mascot-welcome "Benvenuto al Nome ad Albero Binario!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I computer memorizzano le lettere come numeri, e i numeri come bit.
    Oggi *vedrai* quei bit — come percorsi colorati attraverso un
    albero. Programmiamolo insieme!

## Come Funziona

`ord('M') - 64` dà 13, perché M è la 13ª lettera dell'alfabeto. Scritto in cinque bit, 13 è `01101`. Partendo dalla radice, la turtle legge i bit da sinistra a destra: 0 significa "scendi a sinistra", 1 significa "scendi a destra". Dopo cinque mosse ogni lettera arriva alla propria foglia unica — ecco perché cinque bit possono etichettare 32 lettere diverse.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

name = 'MONTY'
top = 160
drop = 50

pos = 0
for ch in name:
    n = ord(ch) - 64
    monty.penup()
    monty.goto(0, top)
    monty.pendown()
    x = 0
    y = top
    off = 88
    d = 16
    while d >= 1:
        bit = (n // d) % 2
        if bit == 1:
            x = x + off
        else:
            x = x - off
        y = y - drop
        monty.goto(x, y)
        off = off / 2
        d = d // 2
    pos = pos + 1
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    MONTY ha 5 lettere, ma la lettera T appare una volta e la Y una
    volta — tutte e 5 le lettere sono diverse. Tutti e 5 i percorsi
    colorati finiranno su foglie **diverse**, oppure due percorsi
    atterreranno sulla stessa foglia? Fai la tua ipotesi, poi clicca
    Esegui!

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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

name = 'MONTY'
colors = ['crimson', 'darkorange', 'forestgreen', 'royalblue', 'purple']
top = 160
drop = 50

monty.pencolor('lightgray')
monty.pensize(1)
for level in range(5):
    for i in range(2 ** level):
        x = 0
        off = 88
        for j in range(level):
            bit = (i // (2 ** (level - 1 - j))) % 2
            if bit == 1:
                x = x + off
            else:
                x = x - off
            off = off / 2
        y = top - drop * level
        monty.penup()
        monty.goto(x, y)
        monty.pendown()
        monty.goto(x - off, y - drop)
        monty.penup()
        monty.goto(x, y)
        monty.pendown()
        monty.goto(x + off, y - drop)

monty.pensize(3)
pos = 0
for ch in name:
    n = ord(ch) - 64
    monty.pencolor(colors[pos % 5])
    monty.penup()
    monty.goto(0, top)
    monty.pendown()
    x = 0
    y = top
    off = 88
    bits = ''
    d = 16
    while d >= 1:
        bit = (n // d) % 2
        bits = bits + str(bit)
        if bit == 1:
            x = x + off
        else:
            x = x - off
        y = y - drop
        monty.goto(x, y)
        off = off / 2
        d = d // 2
    monty.penup()
    monty.goto(x, y - 16)
    monty.write(ch, False, 'center')
    monty.goto(-180 + pos * 74, -140)
    monty.write(ch + ' = ' + bits, False, 'left')
    pos = pos + 1`);
</script>

Ogni lettera atterra sulla propria foglia — lettere diverse significano sempre pattern di bit diversi, quindi i loro percorsi devono separarsi da qualche parte. Avevi indovinato?

## Come Funziona

L'impalcatura grigia viene disegnata per prima: a ognuno dei 5 livelli, il ciclo visita ogni nodo (ce ne sono `2 ** level`) e disegna i suoi due rami figli. L'apertura del ramo `off` si dimezza a ogni livello (88, 44, 22, 11...) così i rami non collidono mai. Poi il numero di ogni lettera viene scomposto a partire dal bit più significativo: dividendo per 16, 8, 4, 2, 1 e prendendo `% 2` si ottengono i cinque bit nell'ordine di lettura, guidando la penna colorata giù per l'albero.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `n = ord(ch) - 64` | Posizione della lettera nell'alfabeto: A=1 ... Z=26 |
| `bit = (n // d) % 2` | Estrae un bit; d conta alla rovescia 16, 8, 4, 2, 1 |
| `off = off / 2` | Dimezza l'apertura del ramo a ogni livello in giù |
| `monty.write(ch + ' = ' + bits, ...)` | Stampa la stringa di bit completa della lettera sotto l'albero |

## Verifica di Apprendimento

!!! mascot-thinking "Tocca a Te — Codifica le Tue Iniziali"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Questa versione più piccola traccia solo tre lettere — ma è
    impostata su 'ABC'. A è 1, che in cinque bit è `00001` — quattro
    mosse a sinistra, poi una a destra. Cambia `name` con le **tue
    iniziali** e prevedi su quale lato dell'albero atterrerà ogni
    lettera prima di eseguirlo!

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

name = 'ABC'
colors = ['crimson', 'royalblue', 'forestgreen']
top = 160
drop = 50

pos = 0
for ch in name:
    n = ord(ch) - 64
    monty.pencolor(colors[pos])
    monty.pensize(3)
    monty.penup()
    monty.goto(0, top)
    monty.pendown()
    x = 0
    y = top
    off = 88
    bits = ''
    d = 16
    while d >= 1:
        bit = (n // d) % 2
        bits = bits + str(bit)
        if bit == 1:
            x = x + off
        else:
            x = x - off
        y = y - drop
        monty.goto(x, y)
        off = off / 2
        d = d // 2
    monty.penup()
    monty.goto(x, y - 20)
    monty.write(ch, False, 'center')
    pos = pos + 1`);
</script>

Le lettere all'inizio dell'alfabeto (numeri piccoli) iniziano con bit 0, quindi derivano a sinistra; le lettere da Q in poi iniziano con un bit 1 e vanno a destra. Iniziali come 'AZ' si dividono verso i bordi opposti dell'albero!

## Esperimenti

1. **Traccia l'intero alfabeto.** Imposta `name` su 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' e usa `colors[pos % 5]`. Saprai che ha funzionato quando ogni foglia dall'estrema sinistra fino alla posizione 26 ha un percorso.

2. **Albero a sei bit.** Cambia `top` in 180, fai partire `d` da 32, e aggiungi un sesto livello al ciclo dell'impalcatura (`range(6)`). Saprai che ha funzionato quando l'albero guadagna un'intera riga extra di rami più piccoli.

3. **Conta le foglie.** Aggiungi un ciclo che mette un piccolo `monty.dot(4, 'gray')` a tutte e 32 le posizioni delle foglie dell'ultima riga. Saprai che ha funzionato quando vedi esattamente 32 puntini.

4. **Decodificatore di parole segrete.** Elimina le etichette delle lettere (entrambe le chiamate `write`) e chiedi a un amico di decodificare la tua parola solo dai percorsi. Saprai che ha funzionato quando riesce a leggere i bit direttamente dal disegno.

!!! mascot-celebration "Parli Binario!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena disegnato ciò che ogni computer fa con il testo —
    trasformare lettere in bit! ASCII, Unicode, i file, e l'intero
    internet si basano su questa singola idea. Prossimo: **Caccia tra
    Tartarughe** — una tartaruga predatrice dà la caccia alla sua preda
    con `atan2()`.
