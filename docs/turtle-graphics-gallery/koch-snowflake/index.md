---
hide:
    - toc
---
# Fiocco di Neve di Koch

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione ricorsiva che sostituisce ogni segmento di linea con quattro segmenti più piccoli
- Capire cos'è un "caso base" e perché ferma la ricorsione
- Vedere come applicare una regola semplice ripetutamente crea complessità infinita

Un fiocco di neve a sei punte con bordi cristallini frastagliati — ogni bordo è a sua volta fatto di bordi frastagliati più piccoli, che sono fatti di altri ancora più piccoli. Tre livelli di ricorsione e una regola semplice: fai sporgere ogni segmento in una tacca triangolare.

!!! mascot-welcome "Benvenuto al Fiocco di Neve di Koch!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Il fiocco di neve di Koch è uno dei frattali più famosi. Ha perimetro infinito
    ma area finita — impossibile da immaginare, ma facile da programmare!
    Programmiamo insieme!

## Come Funziona

La regola di Koch per un singolo segmento di linea di lunghezza `n`:
1. Disegna una linea di lunghezza `n/3`
2. Gira a sinistra di 60°, disegna `n/3`
3. Gira a destra di 120°, disegna `n/3`
4. Gira a sinistra di 60°, disegna `n/3`

A ogni livello, ogni segmento diventa quattro segmenti di un terzo della dimensione. Dopo 4 livelli, i bordi sembrano lisciati e cristallini.

Il fiocco di neve è disegnato chiamando questa regola tre volte, girando di 120° tra le chiamate per formare una base di triangolo equilatero.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('royalblue')

def koch(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)
    monty.right(120)
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    koch(300, 4)
    monty.right(120)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Alla profondità 0, `koch(n, 0)` disegna semplicemente una linea retta.
    Alla profondità 1, ogni segmento ha una protuberanza triangolare.
    Alla profondità 4, i bordi sembreranno lisciati o frastagliati?
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
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('royalblue')

def koch(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)
    monty.right(120)
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    koch(300, 4)
    monty.right(120)`);
</script>

**Frastagliati** ma bellissimi — i bordi hanno un aspetto cristallino, simile a un fiocco di neve. Avevi indovinato?

## Come Funziona

Ogni chiamata a `koch(n, depth)` con `depth > 0` fa **quattro chiamate ricorsive** a se stessa con `depth - 1`. Quando `depth` finalmente raggiunge 0, la funzione disegna semplicemente una linea e ritorna. Questo è il **caso base** — senza di esso, la ricorsione non si fermerebbe mai.

Il numero totale di segmenti di linea disegnati è 4^depth: alla profondità 4 questo è 4^4 = **256 segmenti** per lato, o **768 segmenti** per l'intero fiocco di neve.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `if depth == 0: monty.forward(n)` | Caso base: disegna una linea e ferma la ricorsione |
| `n3 = n / 3` | Ogni segmento ricorsivo è un terzo della dimensione |
| `monty.left(60)` | Gira per formare il lato sinistro della protuberanza triangolare |
| `monty.right(120)` | Gira per formare il lato destro della protuberanza (due rotazioni di 60° = 120°) |
| Quattro chiamate `koch()` | Sostituisce un segmento con quattro |

!!! mascot-tip "Cos'è la Ricorsione?"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    La **ricorsione** significa una funzione che chiama se stessa. Il trucco è il **caso base** —
    una condizione che ferma le chiamate. Senza un caso base, la funzione si chiamerebbe
    per sempre (e Python la fermerebbe con un `RecursionError`).

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova la Profondità 2"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `depth=4` in `depth=2` nelle chiamate a `koch()`.
    Prevedi quanto più semplici sembreranno i bordi del fiocco di neve — poi eseguilo per controllare!

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
monty.pencolor('royalblue')

def koch(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)
    monty.right(120)
    koch(n3, depth - 1)
    monty.left(60)
    koch(n3, depth - 1)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    koch(300, 2)
    monty.right(120)`);
</script>

Alla profondità 2, ogni bordo ha solo `4^2 = 16` segmenti — puoi vedere chiaramente le singole protuberanze triangolari su ogni protuberanza bitorzoluta.

## Esperimenti

1. **Prova la profondità 1.** Solo un giro di protuberanze — tre grandi tacche triangolari per lato. Saprai che ha funzionato quando vedi una forma a stella di David.

2. **Aggiungi il riempimento.** Prima del ciclo, aggiungi `monty.fillcolor('lightblue')` e `monty.begin_fill()`. Dopo il ciclo, aggiungi `monty.end_fill()`. Saprai che ha funzionato quando il fiocco di neve è riempito di azzurro chiaro.

3. **Cambia il colore.** Prova `pencolor('white')` con uno sfondo scuro: aggiungi `turtle.bgcolor('navy')` prima di creare `monty`. Saprai che ha funzionato quando vedi un fiocco di neve bianco su blu.

4. **Disegna solo un bordo.** Sostituisci il ciclo `for` con una singola chiamata `koch(300, 4)`. Saprai che ha funzionato quando vedi solo una curva di Koch invece del triangolo completo.

!!! mascot-celebration "Il Tuo Primo Frattale!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena disegnato complessità infinita da una regola ricorsiva di 4 righe!
    Il fiocco di neve di Koch ha perimetro infinito — ogni volta che zoomi, ci sono più protuberanze.
    Prossimo: **Triangolo di Sierpiński** — l'altro frattale iconico.
