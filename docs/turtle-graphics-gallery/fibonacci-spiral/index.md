---
hide:
    - toc
---
# Spirale di Fibonacci

Alla fine di questo laboratorio sarai in grado di:

- Generare la sequenza di Fibonacci nel codice e usare i suoi valori come raggi degli archi
- Costruire una spirale da archi a quarto di cerchio che pivotano di 90° a ogni passo
- Capire perché la sequenza di Fibonacci appare nelle conchiglie, nei girasoli, e nelle pigne

Archi a quarto di cerchio di raggi 1, 1, 2, 3, 5, 8, 13, 21, 34, e 55 si tassellano insieme perfettamente — ogni arco pivota di 90° nel successivo. La famosa spirale della sezione aurea emerge dalla sequenza numerica più semplice.

!!! mascot-welcome "Benvenuto alla Spirale di Fibonacci!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I numeri di Fibonacci appaiono ovunque in natura — le spirali nella testa di un girasole,
    le camere di una conchiglia di nautilus, la disposizione delle squame di una pigna.
    In questo laboratorio costruirai la spirale tu stesso! Programmiamo insieme!

## Come Funziona

La sequenza di Fibonacci inizia con 1, 1 e ogni nuovo numero è la somma dei due precedenti: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 …

Ogni passo:
1. Disegna un arco a quarto di cerchio con il numero di Fibonacci attuale come raggio
2. Gira a sinistra di 90° così l'arco successivo inizia dall'angolo corretto
3. Avanza al numero di Fibonacci successivo

Gli archi si incastrano tutti insieme perché ogni raggio è uguale alla somma dei due precedenti — che è esattamente come si incastrano i quadrati della tassellatura.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue', 'purple', 'violet', 'hotpink', 'crimson']

a, b = 1, 1
scale = 4

for i in range(10):
    monty.color(colors[i])
    monty.circle(a * scale, 90)
    a, b = b, a + b
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il primo arco ha raggio 1 (× 4 scala = 4 pixel). L'ultimo ha raggio 55 (× 4 = 220 pixel).
    Tutti i 10 archi entreranno sullo schermo, o l'ultimo uscirà dal bordo?
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

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue', 'purple', 'violet', 'hotpink', 'crimson']

a, b = 1, 1
scale = 4

for i in range(10):
    monty.color(colors[i])
    monty.circle(a * scale, 90)
    a, b = b, a + b`);
</script>

Con `scale = 4`, l'arco più grande ha raggio di 220 pixel ed **entra giusto giusto** in un canvas turtle standard. Avevi indovinato?

## Come Funziona

`a, b = b, a + b` è un'assegnazione simultanea che fa avanzare la sequenza di Fibonacci in una riga. Dopo l'assegnazione, il vecchio `b` diventa il nuovo `a`, e il nuovo `b` è la somma.

`monty.circle(a * scale, 90)` disegna esattamente un quarto di cerchio (90°). La tartaruga finisce ruotata di 90° da dove ha iniziato — posizionata perfettamente per l'arco successivo.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `a, b = 1, 1` | Inizia con i primi due numeri di Fibonacci |
| `monty.circle(a * scale, 90)` | Disegna un arco a quarto di cerchio — raggio = numero di Fibonacci × scala |
| `a, b = b, a + b` | Avanza: nuovo a = vecchio b, nuovo b = vecchio a + vecchio b |
| `scale = 4` | Moltiplicatore per far riempire la spirale al canvas |

!!! mascot-tip "La Sezione Aurea"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Mentre la sequenza di Fibonacci cresce, il rapporto di termini consecutivi (es. 55/34 = 1,617…)
    si avvicina sempre più a φ ≈ 1,618 — la **sezione aurea**. Ecco perché la spirale di Fibonacci
    sembra così simile alla vera spirale aurea trovata in natura!

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna archi che hanno tutti lo stesso raggio — nessuna spirale!
    Trova il bug e correggilo così ogni arco usi il raggio di Fibonacci corretto.

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

colors = ['red', 'orange', 'gold', 'green', 'teal', 'blue', 'purple', 'violet', 'hotpink', 'crimson']

a, b = 1, 1
scale = 4

for i in range(10):
    monty.color(colors[i])
    monty.circle(scale, 90)
    a, b = b, a + b`);
</script>

Cambia `monty.circle(scale, 90)` in `monty.circle(a * scale, 90)` — il raggio deve essere `a * scale` così ogni arco usa il numero di Fibonacci attuale.

## Esperimenti

1. **Disegna più archi.** Cambia `range(10)` in `range(12)` ed estendi la lista `colors`. Saprai che ha funzionato quando appaiono due archi extra (ma potrebbero uscire dal bordo!).

2. **Cambia la scala.** Prova `scale = 2` o `scale = 6`. Saprai che ha funzionato quando la spirale si restringe o cresce per adattarsi diversamente al canvas.

3. **Disegna solo gli archi, senza colore.** Sostituisci `monty.color(colors[i])` con `monty.pencolor('black')`. Saprai che ha funzionato quando la spirale è una curva nera pulita.

4. **Usa semicerchi.** Cambia `90` in `180` in `circle()`. Ogni segmento di Fibonacci diventa un semicerchio. Saprai che ha funzionato quando la curva sembra molto diversa.

!!! mascot-celebration "Hai Trovato la Spirale Aurea!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    La sequenza di Fibonacci è uno dei pattern più famosi nella matematica e in natura.
    Ora sai che è solo: `a, b = b, a + b` — ripetuto ancora e ancora!
    Prossimo: **Spirale di Spirali** — disporre molte piccole spirali in un cerchio.
