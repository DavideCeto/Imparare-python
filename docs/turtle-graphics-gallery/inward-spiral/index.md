---
hide:
    - toc
---
# Spirale che Collassa verso l'Interno

Alla fine di questo laboratorio sarai in grado di:

- Creare una spirale che converge a un punto diminuendo la lunghezza del passo a ogni iterazione
- Colorare i segmenti dal blu brillante all'esterno al bianco al centro usando una lista di dissolvenza
- Capire la differenza tra sequenze crescenti (verso l'esterno) e sequenze decrescenti (verso l'interno)

Invece di crescere verso l'esterno, questa spirale collassa verso l'interno — iniziando larga e convergendo a un punto quasi invisibile al centro. I segmenti sfumano da blu profondo all'esterno a quasi bianco mentre la spirale si stringe verso un punto.

!!! mascot-welcome "Benvenuto alla Spirale verso l'Interno!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Tutte le spirali finora sono crescite verso l'esterno. Ora eseguiamo la stessa idea al contrario —
    inizia grande e restringiti verso zero. Programmiamo insieme!

## Come Funziona

Il passo inizia grande (a `200`) e diminuisce di una piccola quantità a ogni iterazione. Quando `step` raggiunge 0 il percorso è convergito a un punto. Una lista di colori sfuma dal blu scuro attraverso tonalità più chiare fino a quasi bianco, così i segmenti esterni sembrano più audaci e quelli interni svaniscono.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['midnightblue', 'navy', 'blue', 'royalblue',
          'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
step = 200

i = 0
while step > 1:
    monty.color(colors[min(i // 25, len(colors) - 1)])
    monty.forward(step)
    monty.right(91)
    step -= 1
    i += 1
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il passo inizia a 200 e diminuisce di 1 a ogni iterazione. Il ciclo usa `right(91)` —
    leggermente più di 90°. La spirale si avvolgerà in senso orario o antiorario?
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

colors = ['midnightblue', 'navy', 'blue', 'royalblue',
          'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
step = 200

i = 0
while step > 1:
    monty.color(colors[min(i // 25, len(colors) - 1)])
    monty.forward(step)
    monty.right(91)
    step -= 1
    i += 1`);
</script>

La spirale si avvolge **in senso orario** perché `right()` gira in senso orario. L'angolo di 91° — solo 1° oltre un angolo retto — fa deviare leggermente il percorso così i giri non si sovrappongono esattamente. Avevi indovinato?

## Come Funziona

`while step > 1` gira finché il passo non diventa troppo piccolo per avere importanza. A ogni iterazione `step -= 1` restringe il segmento del percorso — l'opposto di `step += n` nelle spirali verso l'esterno.

`min(i // 25, len(colors) - 1)` mappa l'indice dell'iterazione a un colore ma lo limita così non andiamo mai oltre l'ultimo colore nella lista, anche se il ciclo gira più del previsto.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `step = 200` | Inizia con un segmento lungo |
| `while step > 1` | Continua finché i segmenti non sono minuscoli |
| `step -= 1` | Si restringe di 1 pixel a ogni passo — crea la spirale verso l'interno |
| `right(91)` | Leggermente più di 90° — impedisce ai giri di sovrapporsi esattamente |
| `min(i // 25, len(colors) - 1)` | Avanza il colore ogni 25 passi, limitato alla fine della lista |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Tasso di Convergenza"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La spirale attualmente diminuisce di 1 per passo. Cambia `step -= 1` in `step -= 2`.
    Prevedi come cambierà la spirale — poi eseguila per vedere se avevi ragione!

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

colors = ['midnightblue', 'navy', 'blue', 'royalblue',
          'cornflowerblue', 'lightskyblue', 'lightcyan', 'white']
step = 200

i = 0
while step > 1:
    monty.color(colors[min(i // 25, len(colors) - 1)])
    monty.forward(step)
    monty.right(91)
    step -= 2
    i += 1`);
</script>

Con `step -= 2` la spirale converge due volte più velocemente — raggiunge il centro in metà dei passi, così ci sono meno rivoluzioni e i giri sono spaziati più distanti.

## Esperimenti

1. **Prova `right(89)`.** Un grado in meno di 90° avvolge la spirale nella direzione di rotazione opposta. Saprai che ha funzionato quando i giri si inclinano dall'altra parte.

2. **Inizia ancora più grande.** Cambia `step = 200` in `step = 300`. Più rivoluzioni entrano prima della convergenza. Saprai che ha funzionato quando la spirale occupa più del canvas.

3. **Usa colori caldi.** Sostituisci i blu con `['darkred', 'red', 'orangered', 'orange', 'gold', 'yellow', 'lightyellow', 'white']`. Saprai che ha funzionato quando la spirale passa da rosso profondo a giallo pallido.

4. **Rendila esagonale.** Cambia `right(91)` in `right(61)`. Saprai che ha funzionato quando gli angoli sembrano più arrotondati.

!!! mascot-celebration "Brillante!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai visto la stessa regola della spirale funzionare in entrambe le direzioni — verso l'esterno E verso l'interno —
    solo cambiando `+=` in `-=`. La convergenza è solo divergenza al contrario!
    Prossimo: **Spirale Logaritmica Colorata** — usare la trigonometria per disegnare una spirale veramente curva.
