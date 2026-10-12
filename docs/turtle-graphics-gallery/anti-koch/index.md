---
hide:
    - toc
---
# Fiocco di Neve Anti-Koch

Alla fine di questo laboratorio sarai in grado di:

- Modificare la regola di Koch per sporgere verso l'interno invece che verso l'esterno a livelli alterni
- Vedere come un cambio di segno in una regola frattale produce forme drammaticamente diverse
- Capire il concetto di alternanza delle regole nei sistemi ricorsivi

Mentre il fiocco di neve di Koch sporge sempre verso l'esterno, l'Anti-Koch alterna: le profondità pari sporgono verso l'esterno, quelle dispari sporgono verso l'interno. Il risultato è una forma con sia punte appuntite sia tacche concave.

!!! mascot-welcome "Benvenuto al Fiocco di Neve Anti-Koch!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Hai visto la curva di Koch sporgere verso l'esterno a ogni livello. Cosa succederebbe se
    invertissimo la direzione a ogni altro livello? Un cambio di segno dà un frattale completamente diverso!
    Programmiamo insieme!

## Come Funziona

`antikoch(n, depth, direction)`:
- `direction = 1` → sporge **verso l'esterno** (sinistra 60°, sinistra 60°, sinistra 60°, poi destra 120° tra l'una e l'altra)
- `direction = -1` → sporge **verso l'interno** (gli angoli sono negati)

A ogni chiamata ricorsiva, `direction` si inverte: `direction * -1`.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('mediumvioletred')

def antikoch(n, depth, direction):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    antikoch(n3, depth - 1, -direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, -direction)
    monty.right(120 * direction)
    antikoch(n3, depth - 1, -direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, -direction)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    antikoch(300, 4, 1)
    monty.right(120)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il Koch standard sporge sempre verso l'esterno, dando una forma puramente appuntita.
    L'Anti-Koch alterna le direzioni. Sembrerà più arrotondato, o più frastagliato?
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
monty.pencolor('mediumvioletred')

def antikoch(n, depth, direction):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    antikoch(n3, depth - 1, -direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, -direction)
    monty.right(120 * direction)
    antikoch(n3, depth - 1, -direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, -direction)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    antikoch(300, 4, 1)
    monty.right(120)`);
</script>

Le sporgenze alternate creano una forma con sia tacche verso l'interno SIA punte verso l'esterno — **più complessa** del puro Koch perché entrambe le direzioni appaiono. Avevi indovinato?

## Come Funziona

`60 * direction` rende l'angolo di rotazione positivo (sinistra) quando `direction = 1` e negativo (destra = verso l'interno) quando `direction = -1`. Passare `-direction` a ogni chiamata ricorsiva inverte la direzione a ogni livello, così i segmenti a profondità pari sporgono in un modo e quelli a profondità dispari sporgono nell'altro.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| Parametro `direction` | 1 = sporge verso l'esterno, -1 = sporge verso l'interno |
| `monty.left(60 * direction)` | Direzione positiva = sinistra; negativa = destra |
| `antikoch(n3, depth-1, -direction)` | Inverte la direzione a ogni livello ricorsivo |
| Stessa struttura di Koch | La forma della sporgenza è identica — solo rispecchiata |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Sporgi Sempre verso l'Interno"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cosa succederebbe se non invertissi mai — passando sempre `-1` come direzione?
    Cambia `antikoch(300, 4, 1)` in `antikoch(300, 4, -1)` e la direzione iniziale sempre verso l'interno.
    Prevedi come differisce dal Koch standard — poi eseguilo!

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
monty.pencolor('mediumvioletred')

def antikoch(n, depth, direction):
    if depth == 0:
        monty.forward(n)
        return
    n3 = n / 3
    antikoch(n3, depth - 1, direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, direction)
    monty.right(120 * direction)
    antikoch(n3, depth - 1, direction)
    monty.left(60 * direction)
    antikoch(n3, depth - 1, direction)

monty.penup()
monty.goto(-150, 90)
monty.pendown()

for _ in range(3):
    antikoch(300, 4, -1)
    monty.right(120)`);
</script>

Le sporgenze sempre verso l'interno (`direction = -1` ovunque) creano un fiocco di neve di Koch che cresce **verso l'interno** — le sporgenze si intaccano nel triangolo invece di irradiarsi verso l'esterno.

## Esperimenti

1. **Confronta fianco a fianco.** Esegui prima il Koch standard (left(60), right(120), left(60)) poi l'Anti-Koch. Saprai che ha funzionato quando puoi vedere entrambe le forme.

2. **Confronto a profondità 2.** Prova entrambi con `depth=2` per vedere chiaramente le sporgenze. Saprai che ha funzionato quando sporgenze e tacche individuali sono visibili.

3. **Cambia il colore.** Prova `pencolor('darkcyan')`. Saprai che ha funzionato quando la curva diventa verde acqua.

4. **Riempi il fiocco di neve.** Aggiungi `begin_fill()` prima del ciclo e `end_fill()` dopo. Saprai che ha funzionato quando l'interno è riempito.

!!! mascot-celebration "Categoria 4 Completata!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai completato 15 pattern frattali — Koch, Sierpiński, Dragone, Hilbert, Barnsley, e altro!
    I frattali dimostrano che la complessità infinita emerge da semplici regole ricorsive.
    Prossimo: **Categoria 5 — Simmetria e Tassellatura!**
