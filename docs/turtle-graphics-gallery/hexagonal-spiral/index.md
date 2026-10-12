---
hide:
    - toc
---
# Spirale Esagonale

Alla fine di questo laboratorio sarai in grado di:

- Cambiare un numero (l'angolo di rotazione) per trasformare una spirale quadrata in una esagonale
- Colorare i segmenti con un gradiente da blu a verde scorrendo una lista di colori
- Capire perché 60° produce angoli esagonali mentre 90° produce angoli quadrati

Un cambiamento di parametro — girare di 60° invece di 90° — trasforma la familiare spirale quadrata in una elegante spirale esagonale. Ogni segmento è tinto in un fresco gradiente da blu a verde che scorre verso l'esterno mentre la spirale cresce.

!!! mascot-welcome "Benvenuto alla Spirale Esagonale!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Negli ultimi due laboratori hai visto una spirale quadrata. Ora cambiamo solo UN numero e guardiamo
    l'intera forma trasformarsi. Programmiamo insieme!

## Come Funziona

Un esagono regolare ha sei lati. A ogni angolo, la tartaruga gira dell'**angolo esterno** di un esagono: `360 / 6 = 60°`. Poiché facciamo anche crescere la lunghezza del passo a ogni iterazione, il percorso si avvolge verso l'esterno invece di chiudersi in un esagono.

La lista di colori ha sette tonalità dal navy profondo attraverso il ciano fino al verde. `i % len(colors)` mappa ogni indice di segmento a un colore, scorrendo continuamente mentre la spirale cresce.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['navy', 'blue', 'dodgerblue', 'deepskyblue',
          'cyan', 'mediumaquamarine', 'green']
step = 2

for i in range(240):
    monty.color(colors[i % len(colors)])
    monty.forward(step)
    monty.right(60)
    step += 0.8
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La spirale quadrata usava `right(90)`. Questa usa `right(60)`.
    Gli angoli sembreranno più netti o più arrotondati della spirale quadrata?
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

colors = ['navy', 'blue', 'dodgerblue', 'deepskyblue',
          'cyan', 'mediumaquamarine', 'green']
step = 2

for i in range(240):
    monty.color(colors[i % len(colors)])
    monty.forward(step)
    monty.right(60)
    step += 0.8`);
</script>

Gli angoli sono **meno netti** — le rotazioni di 60° sono più dolci delle rotazioni di 90°, dando alla spirale un aspetto più rotondo e fluido. Avevi indovinato?

## Come Funziona

`right(60)` crea angoli esagonali perché 60° è l'angolo esterno di un esagono regolare (360° ÷ 6 = 60°). Il `step` crescente impedisce al percorso di chiudersi in un esagono — invece si avvolge verso l'esterno un anello alla volta.

`colors[i % len(colors)]` usa `len(colors)` invece di scrivere a mano `7`. Questa è buona pratica: se aggiungi o rimuovi un colore, il modulo si adatta automaticamente.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = [...]` | Gradiente a sette tonalità da navy a verde |
| `i % len(colors)` | Mappa l'indice del segmento alla lista di colori — funziona per qualsiasi lunghezza di lista |
| `monty.right(60)` | Angolo esagonale — `360 / 6 = 60°` |
| `step += 0.8` | Fa crescere il passo — fonte della spirale |
| `range(240)` | 240 passi = 40 "esagoni" completi (6 lati ciascuno) |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto disegna lo stesso esagono ripetutamente nello stesso posto — nessuna spirale!
    Trova la riga mancante e aggiungila così il percorso si avvolga verso l'esterno.

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

colors = ['navy', 'blue', 'dodgerblue', 'deepskyblue',
          'cyan', 'mediumaquamarine', 'green']
step = 2

for i in range(240):
    monty.color(colors[i % len(colors)])
    monty.forward(step)
    monty.right(60)`);
</script>

Aggiungi `step += 0.8` come ultima riga dentro il ciclo — senza di essa, ogni segmento è della stessa lunghezza e il percorso traccia semplicemente lo stesso esagono ripetutamente.

## Esperimenti

1. **Prova una spirale pentagonale.** Cambia `right(60)` in `right(72)` (360/5). Saprai che ha funzionato quando la spirale ha angoli a cinque lati invece di sei.

2. **Prova una spirale triangolare.** Cambia `right(60)` in `right(120)` (360/3). Saprai che ha funzionato quando gli angoli diventano rotazioni nette di 120°.

3. **Accelera la crescita.** Cambia `step += 0.8` in `step += 2`. I giri si allargano più velocemente. Saprai che ha funzionato quando ci sono meno anelli, più distanziati.

4. **Passa a colori caldi.** Sostituisci la lista `colors` con `['darkred', 'red', 'orangered', 'orange', 'gold', 'yellow', 'lightyellow']`. Saprai che ha funzionato quando la spirale passa da un rosso ardente attraverso il giallo.

!!! mascot-celebration "Lavoro Eccellente!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scoperto che **un numero** — l'angolo di rotazione — determina la forma poligonale di una spirale.
    Cambia 60° → 90° → 120° e guarda l'intero pattern trasformarsi!
    Prossimo: **Spirale Triangolare** — spingere l'angolo di rotazione ancora più oltre.
