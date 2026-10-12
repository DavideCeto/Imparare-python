---
hide:
    - toc
---
# Catena Montuosa

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione `mountain(x, peak_y, width, color)` usando punti di passaggio `goto()`
- Stratificare chiamate di funzione dal retro al fronte per creare un senso di profondità
- Usare il valore del colore (scuro contro chiaro) per segnalare la distanza — una tecnica chiave nell'arte

Tre catene montuose stratificate si allontanano in un gradiente di cielo — i picchi lontani sono pallidi
e freddi, i picchi vicini sono blu profondo, creando profondità con nient'altro che il colore.

!!! mascot-welcome "Benvenuto alla Catena Montuosa!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli artisti sanno da secoli che gli oggetti distanti sembrano più chiari e più freddi.
    In questo laboratorio userai lo stesso trucco nel codice per creare un paesaggio con profondità!
    Programmiamo insieme!

## Come Funziona la Profondità

Disegniamo tre strati di montagne in ordine: **sfondo prima, primo piano ultimo**.
Ogni strato usa un blu progressivamente più scuro e più saturo.
Poiché i riempimenti sono opachi, ogni strato anteriore copre parzialmente gli strati dietro di esso,
creando naturalmente l'illusione della distanza.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def mountain(x, peak_y, width, color):
    monty.penup()
    monty.goto(x - width // 2, -190)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    monty.goto(x, peak_y)
    monty.goto(x + width // 2, -190)
    monty.end_fill()

# sky
monty.color('lightsteelblue')
monty.begin_fill()
monty.goto(-300, -190)
monty.goto(-300, 200)
monty.goto(300, 200)
monty.goto(300, -190)
monty.end_fill()

# layers: back to front, light to dark
mountain(   0,  170, 600, 'lightsteelblue')
mountain(-150,  120, 320, 'steelblue')
mountain( 160,  130, 350, 'cornflowerblue')
mountain( -30,   60, 260, 'navy')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Le montagne sono disegnate dal retro al fronte. Quale colore apparirà in primissimo piano?
    Scorri le chiamate di funzione e fai la tua previsione — poi clicca Esegui per scoprirlo!

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

def mountain(x, peak_y, width, color):
    monty.penup()
    monty.goto(x - width // 2, -190)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    monty.goto(x, peak_y)
    monty.goto(x + width // 2, -190)
    monty.end_fill()

monty.color('lightsteelblue')
monty.begin_fill()
monty.goto(-300, -190)
monty.goto(-300, 200)
monty.goto(300, 200)
monty.goto(300, -190)
monty.end_fill()

mountain(   0,  170, 600, 'lightsteelblue')
mountain(-150,  120, 320, 'steelblue')
mountain( 160,  130, 350, 'cornflowerblue')
mountain( -30,   60, 260, 'navy')`);
</script>

La montagna **navy** in primo piano è disegnata ultima e appare più vicina. Avevi indovinato?

## Come Funziona

`mountain()` disegna un triangolo riempito usando tre chiamate `goto()`: base sinistra → vetta → base destra.
La coordinata y della base è sempre `-190` (fondo del canvas) così tutte le montagne condividono una linea di terreno comune.

Il rettangolo del cielo è disegnato prima delle montagne così serve come strato di sfondo — qualsiasi riempimento successivo apparirà sopra di esso.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.goto(x - width//2, -190)` | Base sinistra del triangolo della montagna |
| `monty.goto(x, peak_y)` | La vetta — punto più alto del triangolo |
| `monty.goto(x + width//2, -190)` | Base destra — chiude il triangolo |
| Ordine di disegno: retro → fronte | I disegni successivi appaiono sopra (più vicini all'osservatore) |
| Colore più chiaro = più distante | Trucco della prospettiva atmosferica |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Cima Innevata"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi un **piccolo triangolo bianco** sopra la montagna navy in primo piano per simulare la neve.
    Chiama `mountain()` un'altra volta con una larghezza minore, `peak_y` più alto, e colore `'white'`.

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

def mountain(x, peak_y, width, color):
    monty.penup()
    monty.goto(x - width // 2, -190)
    monty.pendown()
    monty.color(color)
    monty.begin_fill()
    monty.goto(x, peak_y)
    monty.goto(x + width // 2, -190)
    monty.end_fill()

monty.color('lightsteelblue')
monty.begin_fill()
monty.goto(-300,-190); monty.goto(-300,200); monty.goto(300,200); monty.goto(300,-190)
monty.end_fill()

mountain(   0,  170, 600, 'lightsteelblue')
mountain(-150,  120, 320, 'steelblue')
mountain( 160,  130, 350, 'cornflowerblue')
mountain( -30,   60, 260, 'navy')
# ADD ONE CALL: white snow cap on the navy mountain (x=-30, peak slightly higher, narrow width)`);
</script>

Aggiungi `mountain(-30, 70, 80, 'white')` — un triangolo bianco stretto che si sovrappone alla cima del picco navy.

## Esperimenti

1. **Aggiungi un cielo al tramonto.** Cambia il colore del cielo da `'lightsteelblue'` a `'darkorange'`. Saprai che ha funzionato quando la scena sembra crepuscolare.

2. **Aggiungi una linea di alberi.** Prima della montagna in primo piano, aggiungi una fila di piccoli triangoli verde scuro attraverso la base. Saprai che ha funzionato quando una sagoma di foresta appare ai piedi della montagna.

3. **Fai montagne più alte.** Cambia `peak_y = 170` per la catena di sfondo in `220`. Saprai che ha funzionato quando le montagne di sfondo torreggiano sopra la cima del canvas.

4. **Aggiungi un lago.** Disegna un'ellisse blu riempita al centro basso dopo tutte le montagne. Saprai che ha funzionato quando appare uno specchio d'acqua in primo piano.

!!! mascot-celebration "Lavoro Bellissimo!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato disegno a strati, valore di colore, e chiamate di funzione per creare un paesaggio
    con vera profondità visiva — una tecnica da artista implementata in puro Python!
    Prossimo: **Spirale Quadrata di Archimede** — come una lunghezza di passo crescente crea una spirale perfetta.
