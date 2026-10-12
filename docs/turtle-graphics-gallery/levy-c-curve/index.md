---
hide:
    - toc
---
# Curva C di Lévy

Alla fine di questo laboratorio sarai in grado di:

- Implementare la Curva C di Lévy usando la stessa struttura ricorsiva della curva di Koch ma con angoli di 45°
- Confrontare come angoli di sostituzione diversi producono forme frattali completamente diverse
- Capire come un frattale può tassellare il piano — la curva di Lévy si incastra perfettamente in se stessa

Ogni segmento di linea è sostituito da due segmenti uguali che formano un picco ad angolo retto. Dopo 14 iterazioni, la curva si compatta in una forma che ricorda l'ala di un dragone o una foglia increspata.

!!! mascot-welcome "Benvenuto alla Curva C di Lévy!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Già sai che la curva di Koch usa protuberanze di 60°. La Lévy C usa protuberanze di 45° —
    un piccolo cambiamento che produce un frattale completamente diverso e tassellabile!
    Programmiamo insieme!

## Come Funziona

`levy(n, depth)`:
- Se `depth == 0`: disegna una linea di lunghezza `n`
- Altrimenti: gira a sinistra di 45°, ricorri con `n / √2`, gira a destra di 90°, ricorri con `n / √2`, gira a sinistra di 45°

La differenza chiave da Koch: entrambe le chiamate ricorsive vanno nella **stessa direzione**, creando un picco verso l'alto. L'angolo è 45° invece di 60°.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('steelblue')

def levy(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n2 = n / math.sqrt(2)
    monty.left(45)
    levy(n2, depth - 1)
    monty.right(90)
    levy(n2, depth - 1)
    monty.left(45)

monty.penup()
monty.goto(-160, -60)
monty.pendown()
levy(320, 14)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La curva di Koch sporge verso l'esterno in un triangolo. La Lévy usa protuberanze di 45°.
    La forma generale sembrerà più un fiocco di neve o una nuvola?
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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('steelblue')

def levy(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n2 = n / math.sqrt(2)
    monty.left(45)
    levy(n2, depth - 1)
    monty.right(90)
    levy(n2, depth - 1)
    monty.left(45)

monty.penup()
monty.goto(-160, -60)
monty.pendown()
levy(320, 14)`);
</script>

Più simile a una **nuvola o ala** — il compattamento asimmetrico a 45° crea una sagoma irregolare invece di un fiocco di neve simmetrico. Avevi indovinato?

## Come Funziona

Ogni segmento diventa due segmenti di lunghezza `n / √2`. Poiché `(n/√2)^2 + (n/√2)^2 = n^2`, i due sotto-segmenti formano un triangolo isoscele rettangolo con ipotenusa `n` — la lunghezza del segmento originale è preservata geometricamente.

Le ripetute sostituzioni a picco si compattano densamente senza incrociarsi — la curva C di Lévy tassella il piano quando le copie sono posizionate correttamente.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `n / math.sqrt(2)` | Lunghezza del sotto-segmento dal teorema di Pitagora |
| `monty.left(45)` | Prima rotazione — forma il lato sinistro del picco |
| `monty.right(90)` | Gira tra i due sotto-segmenti |
| `monty.left(45)` | Ripristina la direzione originale dopo il picco |
| `depth == 0` | Caso base: disegna un segmento puro |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova la Profondità 8"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `levy(320, 14)` in `levy(320, 8)`. La curva sarà molto meno dettagliata.
    Prevedi come sembrerà con solo 8 livelli di sostituzione — poi eseguilo!

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
monty.pencolor('steelblue')

def levy(n, depth):
    if depth == 0:
        monty.forward(n)
        return
    n2 = n / math.sqrt(2)
    monty.left(45)
    levy(n2, depth - 1)
    monty.right(90)
    levy(n2, depth - 1)
    monty.left(45)

monty.penup()
monty.goto(-160, -60)
monty.pendown()
levy(320, 8)`);
</script>

Alla profondità 8 puoi vedere chiaramente le singole forme a V prima che si compattino insieme. La forma completa è riconoscibile ma più grossolana.

## Esperimenti

1. **Cambia il colore.** Prova `pencolor('darkviolet')`. Saprai che ha funzionato quando la curva diventa viola.

2. **Usa il confronto con Koch.** Prova la regola di Koch (`left(60)`, nessun `right`, ecc.) sulla stessa lunghezza di partenza per confrontare. Saprai che ha funzionato quando vedi la forma di Koch invece.

3. **Penna più spessa.** Aggiungi `monty.pensize(2)` prima della chiamata a levy. Saprai che ha funzionato quando le linee della curva sono più spesse e più facili da vedere.

4. **Ribalta la curva.** Inizia rivolto verso Sud (`monty.setheading(270)`) e adatta la posizione di partenza. Saprai che ha funzionato quando la curva pende verso il basso come una stalattite.

!!! mascot-celebration "Ali Frattali!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai cambiato un angolo (60° → 45°) e ottenuto un frattale completamente diverso!
    Questo è il potere del pensiero parametrico — piccoli cambiamenti, grande impatto.
    Prossimo: **Curva di Gosper** — un frattale che tassella lo spazio esagonale.
