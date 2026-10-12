---
hide:
    - toc
---
# Spirale Quadrata di Archimede

Alla fine di questo laboratorio sarai in grado di:

- Creare una spirale aumentando il passo avanti di una quantità fissa a ogni iterazione
- Capire perché un angolo di rotazione fisso più un passo crescente produce una spirale
- Vedere come cambiare un numero trasforma drammaticamente la forma

Una spirale quadrata stretta si svolge verso l'esterno dal centro — duecento brevi segmenti,
ognuno leggermente più lungo del precedente, tutti girando esattamente di 90° per tracciare un percorso quadrato perfetto.

!!! mascot-welcome "Benvenuto alla Spirale di Archimede!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Nessuna trigonometria necessaria qui — solo un ciclo e una variabile crescente.
    La spirale emerge dalla regola più semplice possibile: vai avanti un po' più ogni volta!
    Programmiamo insieme!

## Come Funziona la Spirale

Ogni passo: muoviti avanti di `step` pixel, gira di 90°, poi aumenta `step` di una piccola quantità.
Poiché il passo cresce un po' ogni volta, ogni lato del "quadrato" è leggermente più lungo
del precedente — così il percorso si avvolge verso l'esterno invece di chiudersi su se stesso.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

step = 2

for i in range(200):
    monty.forward(step)
    monty.right(90)
    step += 1.5
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La tartaruga gira esattamente di 90° ogni passo. Il percorso sembrerà un quadrato, una spirale, o qualcos'altro?
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

step = 2

for i in range(200):
    monty.forward(step)
    monty.right(90)
    step += 1.5`);
</script>

Entrambi! Sembra una **spirale quadrata** — la rotazione di 90° gli dà angoli squadrati, mentre la lunghezza del passo crescente la fa avvolgere verso l'esterno. Avevi indovinato?

## Come Funziona

`step += 1.5` è la chiave. Se `step` non cambiasse mai, la tartaruga disegnerebbe lo stesso quadrato ripetutamente nello stesso posto. Il piccolo incremento a ogni iterazione significa che ogni "lato" è 1,5 pixel più lungo del precedente — abbastanza per spingere il percorso verso l'esterno di una quantità costante per rivoluzione.

Questa è una **spirale di Archimede**: una dove la distanza tra giri successivi è costante.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `step = 2` | Lunghezza del lato di partenza — molto corta all'inizio |
| `monty.forward(step)` | Disegna un segmento della lunghezza attuale |
| `monty.right(90)` | La rotazione fissa di 90° dà il carattere quadrato |
| `step += 1.5` | Fa crescere il passo — la fonte della spirale |
| `range(200)` | 200 passi = 50 "quadrati" completi (4 lati ciascuno) |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna un quadrato ripetutamente nello stesso posto — nessuna spirale!
    Trova e correggi il bug così il percorso si avvolga verso l'esterno.

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

step = 2

for i in range(200):
    monty.forward(step)
    monty.right(90)`);
</script>

Aggiungi `step += 1.5` come ultima riga dentro il ciclo così il passo cresce a ogni iterazione.

## Esperimenti

1. **Prova una spirale triangolare.** Cambia `right(90)` in `right(120)`. Saprai che ha funzionato quando la spirale ha angoli a tre lati invece di quattro.

2. **Prova una spirale esagonale.** Cambia `right(90)` in `right(60)`. Saprai che ha funzionato quando la spirale ha angoli a sei lati.

3. **Accelera la crescita.** Cambia `step += 1.5` in `step += 3`. La spirale si allarga molto più velocemente. Saprai che ha funzionato quando i giri sono più distanti tra loro.

4. **Inizia più grande.** Cambia `step = 2` in `step = 20`. La spirale inizia già espansa e raggiunge il bordo del canvas in meno giri. Saprai che ha funzionato quando i primi giri sono già larghi.

!!! mascot-celebration "Lavoro Meraviglioso!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai fatto una spirale con solo tre righe dentro un ciclo — nessuna matematica oltre l'addizione!
    Prova a cambiare l'angolo di rotazione e guarda la spirale trasformarsi completamente.
    Prossimo: **Spirale di Linee Arcobaleno** — aggiungere fasce di colore alla spirale.
