---
hide:
    - toc
---
# Spirale a Doppia Elica

Alla fine di questo laboratorio sarai in grado di:

- Disegnare due spirali interlacciate da un singolo ciclo alternando tra due assegnazioni di colore
- Capire l'offset di fase — far iniziare due spirali a 180° di distanza così non si sovrappongono mai
- Vedere come un ciclo può produrre due pattern indipendenti controllando `i % 2`

Due spirali si avvolgono verso l'esterno insieme — una rossa, una blu — distanziate esattamente di metà rivoluzione. Si espandono alla stessa velocità così restano interlacciate per sempre senza mai incrociarsi.

!!! mascot-welcome "Benvenuto alla Doppia Elica!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    La famosa doppia elica del DNA è due filamenti avvolti insieme con un offset di mezzo giro.
    Questo laboratorio costruisce la stessa idea con la grafica turtle — due spirali in un ciclo!
    Programmiamo insieme!

## Come Funziona

L'intuizione chiave: due spirali quadrate che iniziano a 180° di distanza e crescono alla stessa velocità rimarranno sempre esattamente a metà rivoluzione di distanza. Le disegniamo alternando i colori a ogni passo usando `i % 2`:

- Passi pari (0, 2, 4 …) → spirale rossa
- Passi dispari (1, 3, 5 …) → spirale blu

Poiché passi pari consecutivi condividono lo stesso braccio della spirale, i due pattern si intrecciano insieme.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

step = 2

for i in range(400):
    if i % 2 == 0:
        monty.color('crimson')
    else:
        monty.color('royalblue')
    monty.forward(step)
    monty.right(91)
    if i % 2 == 0:
        step += 1
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il passo cresce solo alle iterazioni pari (`i % 2 == 0`).
    Le due spirali resteranno della stessa dimensione, o una crescerà più velocemente dell'altra?
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

for i in range(400):
    if i % 2 == 0:
        monty.color('crimson')
    else:
        monty.color('royalblue')
    monty.forward(step)
    monty.right(91)
    if i % 2 == 0:
        step += 1`);
</script>

Restano della **stessa dimensione** — crescendo esattamente alla stessa velocità perché `step` aumenta a ogni passo pari, ed entrambe le spirali avanzano di quello stesso valore `step`. Avevi indovinato?

## Come Funziona

`right(91)` — leggermente oltre 90° — fa deviare il percorso così i giri della spirale non si trovano esattamente uno sopra l'altro. Ogni giro si sposta di 1° per rivoluzione, dando ai bracci interlacciati la loro separazione visibile.

`step` cresce solo alle iterazioni pari, ma poiché le iterazioni dispari seguono immediatamente e usano lo stesso `step`, entrambe le spirali avanzano della stessa quantità. Il passo si incrementa solo una volta per coppia.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `i % 2 == 0` | Sceglie rosso sui passi pari, blu su quelli dispari |
| `monty.right(91)` | Rotazione di 90° leggermente deviata — mantiene i giri separati |
| `if i % 2 == 0: step += 1` | Fa crescere il passo una volta per coppia di segmenti |
| `range(400)` | 400 passi = 200 segmenti rossi + 200 blu |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Terza Spirale"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Riesci a modificare il codice per disegnare **tre** spirali interlacciate in rosso, blu, e verde?
    Usa `i % 3` invece di `i % 2` e aggiungi una terza condizione di colore.

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

colors = ['crimson', 'royalblue', 'forestgreen']
step = 2

for i in range(600):
    monty.color(colors[i % 3])
    monty.forward(step)
    monty.right(91)
    if i % 3 == 0:
        step += 1`);
</script>

Usare `i % 3` sceglie uno di tre colori a rotazione. Il `step` cresce una volta ogni tre passi — più lento della doppia elica, così i giri si compattano leggermente più stretti.

## Esperimenti

1. **Cambia la deviazione.** Prova `right(92)` o `right(89)`. Più deviazione significa che i giri si spostano più per rivoluzione. Saprai che ha funzionato quando gli spazi dell'intreccio cambiano dimensione.

2. **Aumenta la crescita del passo.** Cambia `step += 1` in `step += 2`. La spirale si espande più velocemente e meno rivoluzioni entrano. Saprai che ha funzionato quando i bracci sono più distanziati.

3. **Usa colori complementari.** Prova `'darkorange'` e `'dodgerblue'` — colori opposti sulla ruota dei colori. Saprai che ha funzionato quando il contrasto tra i bracci è ancora più forte.

4. **Disegna solo una spirale.** Rimuovi l'alternanza di colore e usa un singolo colore. Saprai che ha funzionato quando il pattern a doppio filamento collassa di nuovo in una singola spirale.

!!! mascot-celebration "Il Doppio del Divertimento!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito due spirali in un ciclo usando un solo controllo `i % 2` — lo stesso trucco
    usato nell'animazione per alternare tra due oggetti a ogni fotogramma!
    Prossimo: **Spirale di Fibonacci** — la spirale più famosa in natura.
