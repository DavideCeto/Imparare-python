---
hide:
    - toc
---
# Piastrella di Pesci in Stile Escher

Alla fine di questo laboratorio sarai in grado di:

- Memorizzare un contorno di forma come lista di punti `(x, y)`
- Spiegare la regola della tassellatura: qualunque protuberanza ESCE da un lato deve diventare un'intaccatura ENTRA sul lato opposto
- Tassellare una forma sullo schermo per traslazione, alternando due colori

L'artista M.C. Escher riempiva intere pareti con lucertole, uccelli e pesci che si incastrano senza spazi vuoti e senza sovrapposizioni. Il suo segreto era semplice e brillante: iniziare con una forma che tassella (come un rettangolo), e ogni volta che spingi una protuberanza fuori da un lato, scavare la stessa identica protuberanza nel lato opposto. Questo programma costruisce un pesce in questo modo — il suo naso è la protuberanza, la sua coda è l'intaccatura corrispondente — poi stampa 16 copie in un banco perfettamente incastrato.

!!! mascot-welcome "Benvenuto alla Fabbrica dei Pesci!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I pesci di Escher sembrano impossibili da progettare — ma iniziano come un
    semplice rettangolo! Pieghi il lato sinistro in un naso, tagli la stessa forma
    dal lato destro come coda, e le copie si incastrano come pezzi di un puzzle.

## Come Funziona

Il contorno del pesce è una lista di punti che traccia un rettangolo 80×50 i cui lati sono stati rimodellati in coppie corrispondenti. Il naso sul lato sinistro ai punti `(-14, 35), (-6, 25), (-14, 15)` riappare sul lato destro spostato esattamente di `+80`: `(66, 35), (74, 25), (66, 15)`. L'incavo del ventre sul lato inferiore in `(40, -8)` riappare sul lato superiore spostato di `+50` come `(40, 42)`. Poiché ogni protuberanza corrisponde a un'intaccatura a distanza di una tassella, le copie posizionate ogni 80 pixel in orizzontale e 50 pixel in verticale si incastrano senza spazi vuoti.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

outline = [(0, 0), (25, 0), (40, -8), (55, 0), (80, 0),
           (66, 15), (74, 25), (66, 35), (80, 50),
           (55, 50), (40, 42), (25, 50), (0, 50),
           (-14, 35), (-6, 25), (-14, 15)]

def draw_fish(x, y, color):
    monty.penup()
    monty.color(color, color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    for px, py in outline:
        monty.goto(x + px, y + py)
    monty.goto(x, y)
    monty.end_fill()
    monty.penup()
    monty.goto(x + 6, y + 31)
    monty.dot(7, 'black')
    monty.dot(3, 'white')

for row in range(4):
    for col in range(4):
        x = -150 + col * 80
        y = -100 + row * 50
        if (row + col) % 2 == 0:
            draw_fish(x, y, 'coral')
        else:
            draw_fish(x, y, 'lightseagreen')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il colore viene scelto da `(row + col) % 2` — una regola a scacchiera.
    Il pesce direttamente SOPRA un pesce corallo sarà corallo o verde mare?
    Decidi, poi esegui il programma e controlla una colonna.

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

outline = [(0, 0), (25, 0), (40, -8), (55, 0), (80, 0),
           (66, 15), (74, 25), (66, 35), (80, 50),
           (55, 50), (40, 42), (25, 50), (0, 50),
           (-14, 35), (-6, 25), (-14, 15)]

def draw_fish(x, y, color):
    monty.penup()
    monty.color(color, color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    for px, py in outline:
        monty.goto(x + px, y + py)
    monty.goto(x, y)
    monty.end_fill()
    monty.penup()
    monty.goto(x + 6, y + 31)
    monty.dot(7, 'black')
    monty.dot(3, 'white')

for row in range(4):
    for col in range(4):
        x = -150 + col * 80
        y = -100 + row * 50
        if (row + col) % 2 == 0:
            draw_fish(x, y, 'coral')
        else:
            draw_fish(x, y, 'lightseagreen')`);
</script>

**Verde mare** — salendo di una riga, `row + col` passa da pari a dispari (o da dispari a pari), quindi il colore si inverte sempre. Avevi indovinato?

## Come Funziona

Verifica tu stesso l'incastro con le coordinate. Il pesce alla colonna `c` disegna l'intaccatura della sua coda ai punti assoluti `c*80 + (66, 15)`, `c*80 + (74, 25)`, `c*80 + (66, 35)`. Il suo vicino a destra inizia a `(c+1)*80` e disegna il suo naso a `(c+1)*80 - 14 = c*80 + 66` e `(c+1)*80 - 6 = c*80 + 74` — gli *stessi identici* punti, percorsi nella direzione opposta. L'acqua della coda di un pesce è il naso del pesce successivo. Lo stesso trucco, spostato di 50 invece di 80, fa in modo che la schiena arcuata di ogni pesce culli il ventre del pesce sopra di lui.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `outline = [(0, 0), (25, 0), (40, -8), ...]` | La forma del pesce come punti attorno a un rettangolo modificato |
| `(-14, 35), (-6, 25), (-14, 15)` | La protuberanza del naso — corrisponde esattamente all'intaccatura della coda 80 px a destra |
| `monty.goto(x + px, y + py)` | Trasla ogni punto alla posizione nella griglia di questo pesce |
| `if (row + col) % 2 == 0:` | Regola a scacchiera che alterna i due colori di riempimento |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Qualcuno ha piegato troppo in profondità la coda di questo pesce, e ora ci sono
    spazi vuoti bianchi a forma di diamante nel banco — Escher non approverebbe!
    Confronta i punti della coda con i punti del naso. Un numero rompe
    la regola "protuberanza uguale intaccatura spostata di 80". Correggilo!

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

outline = [(0, 0), (25, 0), (40, -8), (55, 0), (80, 0),
           (66, 15), (60, 25), (66, 35), (80, 50),
           (55, 50), (40, 42), (25, 50), (0, 50),
           (-14, 35), (-6, 25), (-14, 15)]

def draw_fish(x, y, color):
    monty.penup()
    monty.color(color, color)
    monty.goto(x, y)
    monty.pendown()
    monty.begin_fill()
    for px, py in outline:
        monty.goto(x + px, y + py)
    monty.goto(x, y)
    monty.end_fill()
    monty.penup()
    monty.goto(x + 6, y + 31)
    monty.dot(7, 'black')
    monty.dot(3, 'white')

for row in range(4):
    for col in range(4):
        x = -150 + col * 80
        y = -100 + row * 50
        if (row + col) % 2 == 0:
            draw_fish(x, y, 'coral')
        else:
            draw_fish(x, y, 'lightseagreen')`);
</script>

Il punto centrale della coda è `(60, 25)`, ma il punto centrale del naso è `(-6, 25)`, e `-6 + 80 = 74`. Cambia `(60, 25)` di nuovo in `(74, 25)` e i diamanti bianchi scompaiono — protuberanza e intaccatura corrispondono di nuovo.

## Esperimenti

1. **Nuovi colori per il banco.** Cambia `'coral'` in `'gold'` e `'lightseagreen'` in `'slateblue'`. Saprai che ha funzionato quando la scacchiera di pesci passa alla nuova coppia ovunque.

2. **Naso più lungo.** Cambia entrambi i punti del naso `(-14, 35)` e `(-14, 15)` in `(-24, 35)` e `(-24, 15)`, E i punti corrispondenti della coda `(66, 35)` e `(66, 15)` in `(56, 35)` e `(56, 15)`. Saprai che ha funzionato quando ogni pesce ottiene una faccia più aguzza e il banco continua ad avere zero spazi vuoti.

3. **Occhio più grande.** Cambia `monty.dot(7, 'black')` in `monty.dot(11, 'black')` e il punto bianco da `3` a `5`. Saprai che ha funzionato quando tutti e 16 i pesci sembrano bene svegli.

4. **Ventre più profondo.** Cambia il punto del ventre `(40, -8)` in `(40, -16)` e il punto della schiena `(40, 42)` in `(40, 34)`. Saprai che ha funzionato quando i pesci sembrano più paffuti e ogni riga continua a incastrarsi perfettamente nella riga sopra.

!!! mascot-celebration "Hai Tassellato Meglio di Escher!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora conosci il segreto della tassellatura: ogni protuberanza che ESCE deve essere
    un'intaccatura corrispondente che ENTRA sul lato opposto. Con questa unica regola puoi
    trasformare rettangoli in pesci, uccelli, lucertole — qualsiasi cosa!
    Prossimo: **Regioni Colorate di Voronoi** — colora l'intero canvas in base a quale punto seme è più vicino.
