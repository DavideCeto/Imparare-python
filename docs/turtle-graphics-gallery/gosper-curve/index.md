---
hide:
    - toc
---
# Curva di Gosper (Flowsnake)

Alla fine di questo laboratorio sarai in grado di:

- Implementare un sistema-L: un insieme di regole di riscrittura di stringhe applicate ripetutamente
- Tradurre una stringa di caratteri in comandi della tartaruga
- Capire perché la Curva di Gosper è chiamata "flowsnake" — tassella lo spazio esagonale

Una bellissima curva avvolgente che riempie una regione esagonale — la Curva di Gosper, chiamata anche "flowsnake". Costruita da solo due regole di riscrittura di stringhe applicate quattro volte.

!!! mascot-welcome "Benvenuto alla Curva di Gosper!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La Curva di Gosper è costruita con un **sistema-L** — una stringa che riscrive se stessa.
    È la stessa tecnica usata per modellare la vera crescita delle piante nella grafica computerizzata!
    Programmiamo insieme!

## Come Funziona

Inizia con la stringa `'A'`. Applica queste regole di riscrittura ripetutamente:
- `A` → `A-B--B+A++AA+B-`
- `B` → `+A-BB--B-A++A+B`

Dopo 4 iterazioni, traduci il risultato in movimenti della tartaruga:
- `A` o `B` → `forward(step)`
- `+` → `left(60)`
- `-` → `right(60)`

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pencolor('darkorchid')
monty.pensize(1)

def gosper(n):
    s = 'A'
    for _ in range(n):
        new = ''
        for c in s:
            if c == 'A':
                new += 'A-B--B+A++AA+B-'
            elif c == 'B':
                new += '+A-BB--B-A++A+B'
            else:
                new += c
        s = new
    return s

step = 5
instructions = gosper(4)

monty.penup()
monty.goto(-100, 80)
monty.pendown()

for c in instructions:
    if c in 'AB':
        monty.forward(step)
    elif c == '+':
        monty.left(60)
    elif c == '-':
        monty.right(60)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La riscrittura raddoppia la lunghezza della stringa più volte. Dopo 4 iterazioni,
    quanti caratteri lunga sarà approssimativamente la stringa?
    (Ogni A e B si espande in 15 caratteri.) Fai la tua previsione — poi clicca Esegui!

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
monty.pencolor('darkorchid')
monty.pensize(1)

def gosper(n):
    s = 'A'
    for _ in range(n):
        new = ''
        for c in s:
            if c == 'A':
                new += 'A-B--B+A++AA+B-'
            elif c == 'B':
                new += '+A-BB--B-A++A+B'
            else:
                new += c
        s = new
    return s

step = 5
instructions = gosper(4)

monty.penup()
monty.goto(-100, 80)
monty.pendown()

for c in instructions:
    if c in 'AB':
        monty.forward(step)
    elif c == '+':
        monty.left(60)
    elif c == '-':
        monty.right(60)`);
</script>

Dopo 4 iterazioni la stringa ha migliaia di caratteri — e la curva riempie una regione esagonale. Avevi indovinato sul conteggio?

## Come Funziona

Un **sistema-L** (sistema di Lindenmayer) sostituisce caratteri in una stringa usando regole di riscrittura. La stringa rappresenta un programma per la tartaruga. L'intuizione chiave: quando le regole di sostituzione sono progettate correttamente, la forma risultante tassella lo spazio senza spazi vuoti o sovrapposizioni.

Il confine esagonale della Curva di Gosper tassella il piano — sette Curve di Gosper possono essere disposte per formare una Curva di Gosper più grande!

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `s = 'A'` | Assioma iniziale |
| `if c == 'A': new += '...'` | Applica la regola di riscrittura A |
| `if c == 'B': new += '...'` | Applica la regola di riscrittura B |
| `if c in 'AB': forward(step)` | Sia A sia B sono comandi "disegna avanti" |
| `+` e `-` | Gira a sinistra o a destra di 60° |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Prova 3 Iterazioni"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `gosper(4)` in `gosper(3)` e `step = 5` in `step = 10`.
    La curva sarà più grossolana ma più veloce da disegnare. Prevedi come sembrerà più semplice la forma.

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
monty.pencolor('darkorchid')
monty.pensize(2)

def gosper(n):
    s = 'A'
    for _ in range(n):
        new = ''
        for c in s:
            if c == 'A':
                new += 'A-B--B+A++AA+B-'
            elif c == 'B':
                new += '+A-BB--B-A++A+B'
            else:
                new += c
        s = new
    return s

step = 10
instructions = gosper(3)

monty.penup()
monty.goto(-100, 80)
monty.pendown()

for c in instructions:
    if c in 'AB':
        monty.forward(step)
    elif c == '+':
        monty.left(60)
    elif c == '-':
        monty.right(60)`);
</script>

A 3 iterazioni il confine esagonale è chiaramente visibile e il percorso interno avvolgente ha meno anelli.

## Esperimenti

1. **Stampa la stringa.** Aggiungi `print(instructions[:50])` prima del ciclo di disegno. Saprai che ha funzionato quando vedi l'inizio della stringa del sistema-L.

2. **Cambia il colore.** Prova `pencolor('forestgreen')`. Saprai che ha funzionato quando il flowsnake diventa verde.

3. **Prova 5 iterazioni.** Cambia in `gosper(5)` con `step = 3`. Più dettagliato ma più lento. Saprai che ha funzionato quando la curva è molto più densa.

4. **Conta i passi di disegno.** Aggiungi un contatore e `print(counter)` dopo il ciclo. Saprai che ha funzionato quando vedi quanti passi avanti fa la tartaruga.

!!! mascot-celebration "Sistemi-L Sbloccati!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato i sistemi-L — la stessa tecnica usata per modellare la vera crescita delle piante!
    Qualsiasi frattale con una regola di riscrittura di stringhe può essere disegnato in questo modo.
    Prossimo: **Categoria 5 — Simmetria e Tassellatura**, iniziando con la Spirale dei Semi di Girasole.
