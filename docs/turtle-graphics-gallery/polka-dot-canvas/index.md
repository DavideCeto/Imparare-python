---
hide:
    - toc
---
# Canvas a Pois

Alla fine di questo laboratorio sarai in grado di:

- Importare il modulo `random` e chiamare `random.randint()` e `random.choice()`
- Usare un `random.seed()` fisso per rendere i risultati riproducibili
- Scrivere una semplice funzione di disegno di punti e chiamarla molte volte

Duecento punti colorati disseminati attraverso il canvas — ognuno di dimensione,
colore, e posizione casuali — creando un canvas allegro e imprevedibile ogni volta.

!!! mascot-welcome "Benvenuto al Canvas a Pois!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio conoscerai il modulo `random` di Python — uno scrigno di strumenti
    per fare programmi che si comportano diversamente a ogni esecuzione!
    Programmiamo insieme!

## Come Funziona la Casualità

`random.randint(a, b)` restituisce un numero intero casuale tra `a` e `b` (inclusi).
`random.choice(list)` sceglie un elemento casuale da una lista.
`random.seed(n)` fissa il punto di partenza così ottieni sempre la stessa sequenza "casuale" — utile per demo riproducibili.

## Codice di Esempio

```python
import turtle
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

colors = ['red','orange','yellow','green','blue','purple','pink','cyan','coral','gold']

for _ in range(80):
    x = random.randint(-280, 280)
    y = random.randint(-200, 200)
    r = random.randint(8, 40)
    c = random.choice(colors)
    monty.penup()
    monty.goto(x, y)
    monty.dot(r, c)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `random.seed(42)` è impostato prima del ciclo. Se clicchi Reset ed Esegui di nuovo,
    i punti appariranno nelle **stesse** posizioni o in posizioni **diverse**?
    Fai la tua previsione — poi clicca Esegui due volte per scoprirlo!

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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

colors = ['red','orange','yellow','green','blue','purple','pink','cyan','coral','gold']

for _ in range(80):
    x = random.randint(-280, 280)
    y = random.randint(-200, 200)
    r = random.randint(8, 40)
    c = random.choice(colors)
    monty.penup()
    monty.goto(x, y)
    monty.dot(r, c)`);
</script>

I punti appaiono nelle **stesse** posizioni a ogni esecuzione — perché `random.seed(42)` reimposta la sequenza allo stesso punto di partenza. Avevi indovinato?

## Come Funziona

`random.seed(42)` non rende le cose meno casuali — determina solo *quale* sequenza casuale ottieni. Cambia `42` in qualsiasi altro numero e otterrai un pattern completamente diverso (ma ancora riproducibile).

`for _ in range(80)` usa `_` come variabile di ciclo perché in realtà non abbiamo bisogno del contatore — stiamo solo ripetendo 80 volte.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `import random` | Carica il modulo dei numeri casuali di Python |
| `random.seed(42)` | Fissa la sequenza casuale per la riproducibilità |
| `random.randint(-280, 280)` | Intero casuale da -280 a 280 incluso |
| `random.choice(colors)` | Sceglie un elemento casuale dalla lista |
| `monty.dot(r, c)` | Disegna un cerchio riempito di raggio `r` nel colore `c` |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna punti ma appaiono tutti nella stessa posizione!
    Trova e correggi il bug — le coordinate x e y dovrebbero essere casuali, non fisse.

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
import random
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
random.seed(42)

colors = ['red','orange','yellow','green','blue','purple','pink','cyan']

for _ in range(50):
    x = 0
    y = 0
    r = random.randint(8, 40)
    c = random.choice(colors)
    monty.penup()
    monty.goto(x, y)
    monty.dot(r, c)`);
</script>

Sostituisci `x = 0` con `x = random.randint(-280, 280)` e `y = 0` con `y = random.randint(-200, 200)`.

## Esperimenti

1. **Rimuovi il seme.** Elimina `random.seed(42)`. Ora ogni esecuzione produce un pattern diverso. Saprai che ha funzionato quando cliccare Esegui due volte dà disposizioni diverse.

2. **Cambia il seme.** Prova `random.seed(99)` o `random.seed(1)`. Ogni seme produce il proprio pattern unico. Saprai che ha funzionato quando i punti si riorganizzano completamente.

3. **Rendi tutti i punti della stessa dimensione ma di colore casuale.** Cambia `r = random.randint(8, 40)` in `r = 20`. Saprai che ha funzionato quando i punti sono uniformi in dimensione ma colorati.

4. **Raddoppia il conteggio.** Cambia `range(80)` in `range(160)`. Saprai che ha funzionato quando il canvas è molto più densamente riempito di punti.

!!! mascot-celebration "Lavoro Meraviglioso!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato il potere della casualità in Python — e imparato che "casuale" non deve
    significare "incontrollato." I semi ti danno il meglio di entrambi i mondi!
    Prossimo: **Muro di Mattoni** — tassellare una superficie con una funzione e righe a offset.
