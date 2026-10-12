---
hide:
    - toc
---
# Campo di Strisce Diagonali

Alla fine di questo laboratorio sarai in grado di:

- Usare `setheading()` per puntare la tartaruga in qualsiasi direzione della bussola
- Tradurre un contatore di ciclo in una coordinata di partenza per spaziare le forme uniformemente
- Usare `penup()` e `pendown()` per riposizionarsi senza disegnare

Trenta linee diagonali parallele attraversano il canvas dal basso-sinistra all'alto-destra,
alternando verde acqua e corallo come un audace pezzo di tessuto.

!!! mascot-welcome "Benvenuto al Campo di Strisce Diagonali!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio imparerai come puntare la tartaruga a qualsiasi angolo e disegnare linee lunghe
    attraverso tutto il canvas. Una formula trasforma un contatore di ciclo in una posizione di partenza.
    Programmiamo insieme!

## Come Funzionano le Strisce

Ogni striscia è una linea diagonale disegnata a un angolo di 45°. La tartaruga:
1. Alza la penna e salta a una posizione di partenza lungo il bordo inferiore
2. Punta esattamente a 45° con `setheading(45)`
3. Disegna una lunga linea attraverso il canvas

La posizione x di partenza è calcolata come `-300 + i * 20` — così la striscia 0 inizia a x = -300,
la striscia 1 a x = -280, la striscia 2 a x = -260, e così via, spaziandole di 20 pixel.

!!! mascot-tip "setheading() contro right()"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    `right(n)` gira in modo **relativo** a dove Monty è già rivolto.
    `setheading(n)` imposta una direzione **assoluta** della bussola: 0° = Est, 90° = Nord, 45° = Nord-Est.
    Usa `setheading()` quando vuoi sempre lo stesso identico angolo, indipendentemente dalle rotazioni precedenti.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.pensize(3)

colors = ['teal', 'coral']

for i in range(30):
    monty.color(colors[i % 2])
    monty.penup()
    monty.goto(-300 + i * 20, -250)
    monty.pendown()
    monty.setheading(45)
    monty.forward(500)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ci sono 30 strisce e 2 colori che si alternano. Quante strisce **verde acqua** appariranno?
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
monty.pensize(3)

colors = ['teal', 'coral']

for i in range(30):
    monty.color(colors[i % 2])
    monty.penup()
    monty.goto(-300 + i * 20, -250)
    monty.pendown()
    monty.setheading(45)
    monty.forward(500)`);
</script>

30 ÷ 2 = **15 strisce verde acqua** (e 15 corallo). Avevi indovinato?

## Come Funziona

`monty.goto(-300 + i * 20, -250)` è la riga chiave. Quando `i = 0` la tartaruga inizia a `(-300, -250)` — l'angolo in basso a sinistra. Ogni incremento di `i` sposta la posizione x di partenza di 20 pixel a destra, distribuendo le strisce uniformemente.

`setheading(45)` viene chiamato dentro il ciclo per reimpostare l'angolo ogni volta, perché il precedente `forward(500)` lascia Monty rivolto nella stessa direzione, ma è buona pratica impostarlo esplicitamente.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `monty.pensize(3)` | Linee più spesse così le strisce sono chiaramente visibili |
| `colors[i % 2]` | Alterna verde acqua (i pari) e corallo (i dispari) |
| `monty.goto(-300 + i * 20, -250)` | Posiziona ogni striscia 20px a destra dell'ultima |
| `monty.setheading(45)` | Punta Monty esattamente a Nord-Est per una diagonale a 45° |
| `monty.forward(500)` | Disegna una lunga linea diagonale attraverso il canvas |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Direzione"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna 30 linee ma vanno tutte orizzontalmente — nessuna diagonale!
    Aggiungi **una riga** dopo `monty.pendown()` per far andare ogni striscia a 45°.

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
monty.pensize(3)

colors = ['teal', 'coral']

for i in range(30):
    monty.color(colors[i % 2])
    monty.penup()
    monty.goto(-300 + i * 20, -250)
    monty.pendown()
    # ADD ONE LINE HERE to point Monty North-East
    monty.forward(500)`);
</script>

La riga mancante è `monty.setheading(45)` — la direzione 45° punta esattamente a Nord-Est.

## Esperimenti

1. **Cambia l'angolo.** Sostituisci `setheading(45)` con `setheading(60)`. Le strisce diventano più inclinate. Prova `setheading(30)` per un angolo più dolce. Saprai che ha funzionato quando le strisce si inclinano visibilmente.

2. **Cambia la spaziatura delle strisce.** Sostituisci `i * 20` con `i * 10`. Le strisce sono più dense. Saprai che ha funzionato quando le linee quasi si sovrappongono.

3. **Aggiungi più colori.** Cambia `colors` in `['teal', 'coral', 'gold']` e `i % 2` in `i % 3`. Saprai che ha funzionato quando tre colori scorrono attraverso le strisce.

4. **Varia la larghezza della linea.** Sostituisci `monty.pensize(3)` con `monty.pensize(1 + i // 5)`. Le prime strisce sono sottili, quelle successive spesse. Saprai che ha funzionato quando le larghezze delle strisce crescono visibilmente.

!!! mascot-celebration "Lavoro Meraviglioso!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato a combinare `goto()`, `setheading()`, e una formula sul contatore del ciclo
    per tassellare un intero canvas con linee diagonali — una tecnica usata in ogni programma grafico!
    Prossimo: **Griglia di Punti** per esplorare il comando `dot()` e la mappatura delle dimensioni.
