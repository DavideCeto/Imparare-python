---
hide:
    - toc
---
# Cerchi Annidati

Alla fine di questo laboratorio sarai in grado di:

- Usare `circle()` per disegnare cerchi di dimensioni diverse
- Usare `goto()` per riposizionare la tartaruga tra le forme
- Capire perché l'**ordine di disegno** è importante quando le forme si sovrappongono

Venti anelli concentrici che alternano ciano e blu navy pulsano verso l'esterno dal centro
come un'increspatura congelata nel tempo.

!!! mascot-welcome "Benvenuto ai Cerchi Annidati!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio disegnerai cerchi dal più grande al più piccolo, ognuno che copre il precedente.
    Gli anelli che vedi sono le fette di colore che sbirciano da dietro i cerchi più piccoli.
    Programmiamo insieme!

## Come Funzionano gli Anelli

`monty.circle(radius)` disegna un cerchio, ma la tartaruga inizia dal **fondo** del cerchio, non dal centro.
Per mantenere tutti i cerchi centrati sullo stesso punto, usiamo `monty.goto(0, -radius)` prima di ogni cerchio —
posizionando la tartaruga `radius` pixel *sotto* il centro.

Disegniamo dal **più grande al più piccolo** così che ogni nuovo cerchio ricopra ordinatamente il centro del precedente, lasciando visibile solo un sottile anello del colore precedente al bordo.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['navy', 'cyan']

for i in range(19, -1, -1):
    radius = 10 + i * 15
    monty.color(colors[i % 2])
    monty.penup()
    monty.goto(0, -radius)
    monty.pendown()
    monty.begin_fill()
    monty.circle(radius)
    monty.end_fill()
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il ciclo conta alla rovescia: i = 19, 18, 17 … 1, 0.
    L'ultimo cerchio disegnato (i = 0) si trova proprio al centro — sarà **navy** o **ciano**?
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

colors = ['navy', 'cyan']

for i in range(19, -1, -1):
    radius = 10 + i * 15
    monty.color(colors[i % 2])
    monty.penup()
    monty.goto(0, -radius)
    monty.pendown()
    monty.begin_fill()
    monty.circle(radius)
    monty.end_fill()`);
</script>

`i = 0` → `0 % 2 = 0` → `colors[0]` → **navy**. Il centro del bersaglio è sempre navy. Avevi indovinato?

## Come Funziona

`range(19, -1, -1)` conta alla rovescia da 19 a 0 — i tre argomenti sono inizio, fine (esclusa), e passo. Un passo di -1 conta all'indietro.

Ogni iterazione calcola `radius = 10 + i * 15`, quindi i raggi sono 295, 280, 265 … 25, 10 pixel. `colors[i % 2]` sceglie navy quando `i` è pari e ciano quando `i` è dispari, creando gli anelli alternati.

La riga critica è `monty.goto(0, -radius)` — senza di essa, ogni cerchio inizierebbe da dove è finito l'ultimo, disperdendo i cerchi casualmente attraverso il canvas.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `range(19, -1, -1)` | Conta alla rovescia da 19 a 0 (incluso) |
| `radius = 10 + i * 15` | Ogni anello è 15 pixel più largo del successivo interno |
| `colors[i % 2]` | Alterna tra indice 0 (navy) e indice 1 (ciano) |
| `monty.goto(0, -radius)` | Si muove al fondo del cerchio così è centrato all'origine |
| `monty.circle(radius)` | Disegna un cerchio completo con il raggio dato |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Correggi la Centratura"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 20 cerchi ma iniziano tutti dallo stesso punto — una spirale confusa!
    Aggiungi **una riga** dentro il ciclo (dopo `monty.penup()`) per centrare ogni cerchio all'origine.

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

colors = ['navy', 'cyan']

for i in range(19, -1, -1):
    radius = 10 + i * 15
    monty.color(colors[i % 2])
    monty.penup()
    # ADD ONE LINE HERE to move to (0, -radius)
    monty.pendown()
    monty.begin_fill()
    monty.circle(radius)
    monty.end_fill()`);
</script>

La riga mancante è `monty.goto(0, -radius)` — riposiziona la tartaruga al fondo di ogni cerchio così il centro è sempre all'origine.

## Esperimenti

1. **Inverti la direzione del ciclo.** Cambia `range(19, -1, -1)` in `range(20)`. Ora disegni prima il più piccolo. Saprai che ha funzionato quando gli anelli sembrano uguali ma Monty li disegna dall'interno verso l'esterno.

2. **Cambia lo spazio tra gli anelli.** Sostituisci `i * 15` con `i * 10`. Gli anelli sono più vicini tra loro. Prova `i * 25` per anelli più larghi. Saprai che ha funzionato quando il numero di anelli visibili cambia.

3. **Prova tre colori.** Cambia `colors` in `['navy', 'cyan', 'white']` e usa `i % 3`. Saprai che ha funzionato quando vedi un pattern a bersaglio a tre tonalità.

4. **Fai un'ellisse.** Sostituisci `monty.circle(radius)` con `monty.circle(radius, steps=60)` — il `circle()` di turtle può approssimare un'ellisse allungando prima con `monty.shapesize()`. Saprai che ha funzionato quando gli anelli non sono più perfettamente rotondi.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai usato cicli che contano alla rovescia, `goto()` per un posizionamento preciso, e l'ordine di disegno per costruire
    un bersaglio perfetto — tutte abilità fondamentali per qualsiasi programma di disegno.
    Prossimo: **Raggiera a Stella** — linee che si irradiano da un singolo punto centrale.
