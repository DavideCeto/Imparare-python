---
hide:
    - toc
---
# Curva di Hilbert

Alla fine di questo laboratorio sarai in grado di:

- Implementare una curva che riempie lo spazio usando due funzioni mutuamente ricorsive
- Capire cosa significa "riempire lo spazio" — una curva che visita ogni punto di una regione
- Vedere come due funzioni possono chiamarsi a vicenda avanti e indietro (ricorsione mutua)

Una curva continua che riempie un'intera regione quadrata senza incrociarsi. Alla profondità 5, la Curva di Hilbert visita `4^5 = 1024` piccoli quadrati — senza lasciare spazi vuoti.

!!! mascot-welcome "Benvenuto alla Curva di Hilbert!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    David Hilbert scoprì questa curva che riempie lo spazio nel 1891. È usata oggi
    nell'indicizzazione di database, nell'elaborazione delle immagini, e nelle antenne frattali!
    Programmiamo insieme!

## Come Funziona

Due funzioni — `hilbert_a()` e `hilbert_b()` — producono ognuna una forma a "U". Si chiamano a vicenda per riempire lo spazio ricorsivamente:

- `hilbert_a(n)`: gira a sinistra, chiama B, avanti, chiama A, gira a destra, avanti, chiama A, gira a sinistra, avanti, chiama B, gira a destra
- `hilbert_b(n)`: gira a destra, chiama A, avanti, chiama B, gira a sinistra, avanti, chiama B, gira a destra, avanti, chiama A, gira a sinistra

Il parametro `n` controlla la profondità — alla profondità 0, viene disegnato solo `forward()`, nessuna rotazione. Questo impedisce la ricorsione infinita.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('teal')
monty.pensize(1)

step = 6

def hilbert_a(n):
    if n == 0:
        return
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)

def hilbert_b(n):
    if n == 0:
        return
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)

monty.penup()
monty.goto(-170, -170)
monty.pendown()
hilbert_a(5)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Una curva "che riempie lo spazio" visita ogni punto di una regione.
    La curva sembrerà una griglia di forme a U, o un singolo percorso avvolgente?
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
monty.pencolor('teal')
monty.pensize(1)

step = 6

def hilbert_a(n):
    if n == 0:
        return
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)

def hilbert_b(n):
    if n == 0:
        return
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)

monty.penup()
monty.goto(-170, -170)
monty.pendown()
hilbert_a(5)`);
</script>

Un **singolo percorso avvolgente** che riempie il quadrato — ogni cella visitata esattamente una volta, senza mai incrociarsi. Avevi indovinato?

## Come Funziona

`hilbert_a` e `hilbert_b` si chiamano a vicenda — questa è la **ricorsione mutua**. Ogni funzione produce una forma a U orientata diversamente, e insieme riempiono tutto il quadrato.

Alla profondità `n`, la curva ha `4^n` segmenti. Alla profondità 5, sono `4^5 = 1024` piccoli quadrati visitati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `if n == 0: return` | Caso base — ferma la ricorsione |
| `hilbert_a` chiama `hilbert_b` | Ricorsione mutua — ogni funzione ha bisogno dell'altra |
| `monty.left(90)` / `right(90)` | Rotazioni di orientamento tra le forme a U |
| `monty.forward(step)` | Collega forme a U adiacenti |
| `step = 6` | Dimensione di ogni segmento unitario |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova la Profondità 3"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `hilbert_a(5)` in `hilbert_a(3)`. Quante celle verranno visitate?
    (`4^3 = ?`). Prevedi, poi eseguilo per vedere chiaramente la struttura più semplice.

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
monty.pencolor('teal')
monty.pensize(2)

step = 40

def hilbert_a(n):
    if n == 0:
        return
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)

def hilbert_b(n):
    if n == 0:
        return
    monty.right(90)
    hilbert_a(n - 1)
    monty.forward(step)
    monty.left(90)
    hilbert_b(n - 1)
    monty.forward(step)
    hilbert_b(n - 1)
    monty.left(90)
    monty.forward(step)
    hilbert_a(n - 1)
    monty.right(90)

monty.penup()
monty.goto(-170, -170)
monty.pendown()
hilbert_a(3)`);
</script>

La profondità 3 con `step = 40` rende ogni forma a U abbastanza grande da vedere chiaramente — puoi tracciare il percorso da un'estremità all'altra.

## Esperimenti

1. **Cambia il colore.** Prova `pencolor('crimson')`. Saprai che ha funzionato quando la curva diventa rossa.

2. **Aggiungi colore per passo.** Usa una variabile contatore e `pencolor(colors[counter % len(colors)])` dentro il passo. Saprai che ha funzionato quando la curva è multicolore.

3. **Prova la profondità 4.** Torna a `step = 12` e `hilbert_a(4)`. Saprai che ha funzionato quando vedi un pattern a griglia più denso.

4. **Disegna solo hilbert_b.** Chiama `hilbert_b(4)` invece di `hilbert_a(4)`. Saprai che ha funzionato quando vedi un orientamento leggermente diverso della stessa curva che riempie lo spazio.

!!! mascot-celebration "Spazio Riempito!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato la **ricorsione mutua** — due funzioni che si chiamano a vicenda — per costruire
    una delle curve più famose della matematica. È usata nei veri sistemi GPS!
    Prossimo: **Polvere di Cantor** — un frattale fatto di spazi vuoti invece di linee.
