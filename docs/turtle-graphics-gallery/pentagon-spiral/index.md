---
hide:
    - toc
---
# Spirale Pentagonale a Fasce Colorate

Alla fine di questo laboratorio sarai in grado di:

- Creare una spirale pentagonale usando `right(72)` — l'angolo esterno di un pentagono regolare
- Produrre fasce di colore diagonali scegliendo un intervallo di fasciatura che non divide esattamente il periodo del pentagono
- Prevedere come il periodo della fasciatura interagisce con il periodo del poligono per creare pattern visivi

Una spirale pentagonale con angoli a cinque lati — colorata in fasce di cinque tonalità che tagliano diagonalmente attraverso i bracci perché 5 colori × spirale a 5 lati = fasce allineate, mentre intervalli non multipli creano strisce diagonali.

!!! mascot-welcome "Benvenuto alla Spirale Pentagonale!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo laboratorio è l'ultimo della nostra serie di spirali — e riunisce tutto:
    angoli dei poligoni, fasciatura dei colori con `i // n`, e l'interazione tra due periodi.
    Programmiamo insieme!

## Come Funziona

Un pentagono regolare ha **5 lati** con angoli esterni di 360° ÷ 5 = **72°**. Girare di 72° a ogni passo crea una spirale pentagonale.

Per le fasce di colore, `(i // 5) % 5` cambia colore ogni 5 passi — corrispondendo esattamente al periodo del pentagono. Questo fa allineare ogni fascia con un lato intero della spirale. Prova `(i // 7) % 5` invece e le fasce si spostano diagonalmente!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['crimson', 'darkorange', 'gold', 'mediumseagreen', 'royalblue']
step = 2

for i in range(250):
    monty.color(colors[(i // 5) % 5])
    monty.forward(step)
    monty.right(72)
    step += 1.2
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il colore cambia ogni 5 passi e il pentagono ha 5 lati per rivoluzione.
    Le fasce di colore si allineeranno con i bracci della spirale, o li taglieranno diagonalmente?
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

colors = ['crimson', 'darkorange', 'gold', 'mediumseagreen', 'royalblue']
step = 2

for i in range(250):
    monty.color(colors[(i // 5) % 5])
    monty.forward(step)
    monty.right(72)
    step += 1.2`);
</script>

Le fasce **si allineano** con i bracci — ogni braccio è di un colore unico perché il periodo della fascia (5) corrisponde al periodo del poligono (5). Avevi indovinato?

## Come Funziona

Quando l'intervallo della fascia di colore divide esattamente il periodo del poligono, i colori si allineano con i lati. Quando non corrispondono — per esempio, usando 7 passi per fascia di colore su una spirale a 5 lati — le fasce sembrano tagliare diagonalmente attraverso i bracci, creando l'effetto visivo di strisce diagonali.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `right(72)` | Angolo esterno del pentagono: 360° ÷ 5 = 72° |
| `(i // 5) % 5` | Cambia colore ogni 5 segmenti; scorre tra 5 colori |
| `step += 1.2` | Fa crescere il passo — fonte della spirale |
| `range(250)` | 250 passi = 50 rivoluzioni "pentagono" (5 lati ciascuna) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Crea Fasce Diagonali"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `i // 5` in `i // 7`. Ora il periodo del colore (7) non divide esattamente il
    periodo del pentagono (5). Prevedi come cambieranno le fasce — poi eseguilo per controllare!

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

colors = ['crimson', 'darkorange', 'gold', 'mediumseagreen', 'royalblue']
step = 2

for i in range(250):
    monty.color(colors[(i // 7) % 5])
    monty.forward(step)
    monty.right(72)
    step += 1.2`);
</script>

Con `i // 7`, i confini di colore non si allineano più con gli angoli del pentagono — tagliano attraverso i bracci diagonalmente, producendo un effetto di tessitura a righe attraverso la spirale.

## Esperimenti

1. **Prova `i // 3`.** Tre passi per fascia è più corto di un lato del pentagono (5 passi). Saprai che ha funzionato quando i colori cambiano dentro ogni braccio, creando un pattern a righe più fine.

2. **Usa 3 colori invece di 5.** Cambia la lista in `['crimson', 'gold', 'royalblue']` e `% 5` in `% 3`. Saprai che ha funzionato quando appaiono solo tre colori, scorrendo in un pattern non allineato.

3. **Rendila esagonale.** Cambia `right(72)` in `right(60)` e `range(250)` in `range(300)`. Saprai che ha funzionato quando gli angoli diventano meno netti.

4. **Aumenta la larghezza della fascia.** Cambia `i // 5` in `i // 15`. Ogni colore occupa 3 lati interi del pentagono. Saprai che ha funzionato quando le fasce di colore sono molto più larghe.

!!! mascot-celebration "Categoria Completata!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato tutti i 10 pattern a spirale — da quadrato semplice a logaritmico a doppia elica!
    Ogni spirale usava la stessa idea fondamentale ma con variazioni sottili che trasformavano il risultato.
    Prossimo: **Categoria 4 — Frattali e Ricorsione!**
