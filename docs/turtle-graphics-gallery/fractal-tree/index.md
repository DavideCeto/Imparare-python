---
hide:
    - toc
---
# Albero Frattale

Alla fine di questo laboratorio sarai in grado di:

- Scrivere una funzione ricorsiva binaria che fa crescere un albero con due rami per nodo
- Usare la profondità per controllare sia la lunghezza del ramo sia il colore (tronco marrone, foglie verdi)
- Capire perché la tartaruga deve andare indietro dopo ogni ramo per tornare alla diramazione

Un albero che sembra crescere naturalmente — tronco marrone spesso che si divide in rami più sottili, finendo in punte di foglie verde brillante. Cinque livelli di ricorsione binaria creano più di 30 rami distinti.

!!! mascot-welcome "Benvenuto all'Albero Frattale!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni albero che hai mai visto è un frattale — un tronco che si divide in rami
    che si dividono in rami più piccoli. Questo laboratorio programma esattamente questa regola!
    Programmiamo insieme!

## Come Funziona

`tree(branch_len, depth)`:
1. Se `branch_len < 5`, fermati (caso base)
2. Disegna un ramo della lunghezza attuale (marrone se profondo, verde vicino alle punte)
3. Gira a sinistra di 25°, ricorri con `branch_len * 0.7`
4. Gira a destra di 50°, ricorri con `branch_len * 0.7`
5. Gira a sinistra di 25° (ritorna alla direzione originale)
6. Vai **all'indietro** della stessa lunghezza (ritorna al punto di diramazione)

Il passo 6 è la chiave: la tartaruga deve ripercorrere il ramo così la chiamata ricorsiva successiva inizia dalla posizione corretta.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.left(90)

def tree(branch_len, depth):
    if branch_len < 5:
        return
    if depth <= 2:
        monty.pencolor('forestgreen')
        monty.pensize(1)
    elif depth <= 4:
        monty.pencolor('saddlebrown')
        monty.pensize(2)
    else:
        monty.pencolor('saddlebrown')
        monty.pensize(4)
    monty.forward(branch_len)
    monty.left(25)
    tree(branch_len * 0.7, depth - 1)
    monty.right(50)
    tree(branch_len * 0.7, depth - 1)
    monty.left(25)
    monty.backward(branch_len)

monty.penup()
monty.goto(0, -170)
monty.pendown()
tree(100, 7)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni ramo si divide in due che sono lunghi il 70%. Dopo 7 livelli, quante
    punte di foglie ci saranno? (Suggerimento: 2^7 = ?) Fai la tua previsione — poi clicca Esegui!

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
monty.left(90)

def tree(branch_len, depth):
    if branch_len < 5:
        return
    if depth <= 2:
        monty.pencolor('forestgreen')
        monty.pensize(1)
    elif depth <= 4:
        monty.pencolor('saddlebrown')
        monty.pensize(2)
    else:
        monty.pencolor('saddlebrown')
        monty.pensize(4)
    monty.forward(branch_len)
    monty.left(25)
    tree(branch_len * 0.7, depth - 1)
    monty.right(50)
    tree(branch_len * 0.7, depth - 1)
    monty.left(25)
    monty.backward(branch_len)

monty.penup()
monty.goto(0, -170)
monty.pendown()
tree(100, 7)`);
</script>

`2^7 = 128` potenziali punte di foglie — anche se alcune sono tagliate dal caso base `< 5`. Avevi indovinato?

## Come Funziona

`monty.backward(branch_len)` è il passo di "annullamento": dopo aver ricorso in entrambi i sotto-rami, la tartaruga ritorna dove ha iniziato così la chiamata genitrice può continuare correttamente. Senza questo passo, la tartaruga rimarrebbe bloccata su una punta di foglia e l'albero sembrerebbe disordinato.

`branch_len * 0.7` restringe ogni ramo al 70% del suo genitore. Dopo 7 generazioni: `100 × 0.7^7 ≈ 8` pixel — ancora sopra la soglia di `5`, così tutti i rami vengono disegnati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `if branch_len < 5: return` | Caso base — ferma quando i rami diventano troppo piccoli |
| `monty.forward(branch_len)` | Disegna il ramo attuale |
| `monty.left(25)` poi ricorre | Disegna il sotto-ramo sinistro |
| `monty.right(50)` poi ricorre | Disegna il sotto-ramo destro (50° a destra = 25° a destra del centro) |
| `monty.backward(branch_len)` | Riporta la tartaruga al punto di diramazione |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia l'Angolo del Ramo"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia l'angolo del ramo da 25° a 40°. Come cambierà la forma dell'albero —
    più largo e cespuglioso, o più stretto e alto? Prevedi, poi esegui!

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
monty.left(90)

def tree(branch_len, depth):
    if branch_len < 5:
        return
    if depth <= 2:
        monty.pencolor('forestgreen')
        monty.pensize(1)
    else:
        monty.pencolor('saddlebrown')
        monty.pensize(max(1, depth - 2))
    monty.forward(branch_len)
    monty.left(40)
    tree(branch_len * 0.7, depth - 1)
    monty.right(80)
    tree(branch_len * 0.7, depth - 1)
    monty.left(40)
    monty.backward(branch_len)

monty.penup()
monty.goto(0, -170)
monty.pendown()
tree(100, 7)`);
</script>

Con angoli di ramo a 40° l'albero è molto **più largo e cespuglioso** — si estende basso come una quercia invece di allungarsi verso l'alto come un pino. Angolo più grande = estensione più larga.

## Esperimenti

1. **Fai un pino.** Usa angoli di ramo di 15° invece di 25°. Saprai che ha funzionato quando l'albero è stretto e alto come una conifera.

2. **Riduci la velocità di restringimento.** Cambia `0.7` in `0.85`. I rami si restringono più lentamente, creando un albero più denso. Saprai che ha funzionato quando ci sono molti più rami sottili alle punte.

3. **Aggiungi un tronco.** Prima di chiamare `tree(100, 7)`, aggiungi `monty.pensize(6); monty.pencolor('saddlebrown'); monty.forward(40)` poi chiama `tree(100, 7)`, poi `monty.backward(40)`. Saprai che ha funzionato quando l'albero ha una sezione di tronco di base spessa.

4. **Colora per profondità.** Passa `depth` nella funzione e colora le foglie verde brillante solo quando `depth == 0`. Saprai che ha funzionato quando solo le punte estreme sono colorate diversamente.

!!! mascot-celebration "Hai Fatto Crescere un Albero con il Codice!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ogni albero nel mondo reale segue una regola simile — il tronco si divide in rami,
    i rami si dividono in rametti, i rametti in foglie. La ricorsione è l'algoritmo preferito dalla natura!
    Prossimo: **Curva del Dragone** — un frattale che si piega come un foglio di carta.
