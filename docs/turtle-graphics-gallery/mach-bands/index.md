---
hide:
    - toc
---
# Bande di Mach

Alla fine di questo laboratorio sarai in grado di:

- Costruire stringhe di colore esadecimali come `'#4c4c4c'` da un contatore di ciclo usando divisione intera e resto
- Approssimare un gradiente liscio con una fila di bande grigie piatte e discrete
- Spiegare perché i tuoi occhi inventano strisce chiare e scure a bordi che non sono nell'immagine

Una fila di dieci rettangoli, ognuno riempito con una sfumatura di grigio perfettamente piatta, che avanza dal scuro al chiaro. I tuoi occhi si rifiutano di crederci: a ogni confine vedrai una striscia scura fantasma sul lato più scuro e una striscia chiara fantasma sul lato più chiaro. Queste strisce fantasma si chiamano bande di Mach, dal nome del fisico Ernst Mach che le descrisse negli anni 1860.

!!! mascot-welcome "Benvenuto alle Bande di Mach!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo programma dipinge dieci rettangoli grigi piatti — niente di
    più. Ma il tuo cervello aggiungerà strisce che non sono nel codice!
    Costruiamo il gradiente e cogliamo sul fatto il tuo sistema visivo.

## Come Funziona

Un ciclo conta da 0 a 9 e calcola un valore di luminosità `v = 32 + i * 22`, così ogni banda è un po' più chiara dell'ultima. La funzione `gray()` converte `v` in una stringa di colore esadecimale: `v // 16` sceglie la prima cifra esadecimale e `v % 16` sceglie la seconda, e la coppia di due cifre viene ripetuta tre volte per rosso, verde e blu. Una funzione di supporto disegna ogni banda come un rettangolo riempito.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

digits = '0123456789abcdef'

def gray(v):
    pair = digits[v // 16] + digits[v % 16]
    return '#' + pair + pair + pair

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

bands = 10
band_w = 36
band_h = 280
left = -bands * band_w / 2

for i in range(bands):
    v = 32 + i * 22
    filled_rect(left + i * band_w, -band_h / 2, band_w, band_h, gray(v))
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni rettangolo è riempito con una singola sfumatura piatta di
    grigio — il codice lo garantisce. Quando guarderai l'immagine
    finita, ogni banda sembrerà perfettamente piatta, o vedrai strisce
    extra scure e chiare che si attaccano ai bordi?
    Fai la tua ipotesi, poi clicca Esegui!

## Prova Ora

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

digits = '0123456789abcdef'

def gray(v):
    pair = digits[v // 16] + digits[v % 16]
    return '#' + pair + pair + pair

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

bands = 10
band_w = 36
band_h = 280
left = -bands * band_w / 2

for i in range(bands):
    v = 32 + i * 22
    filled_rect(left + i * band_w, -band_h / 2, band_w, band_h, gray(v))`);
</script>

Ogni banda sembra sagomata — più scura lungo il bordo sinistro e più chiara lungo il bordo destro — anche se ogni pixel dentro una banda è identico. Avevi indovinato?

## Come Funziona

La tua retina non riporta la luminosità grezza — le cellule fotosensibili vicine si inibiscono a vicenda, un trucco chiamato inibizione laterale. Una cellula posizionata appena sul lato scuro di un bordo riceve un'inibizione extra-forte dai suoi vicini più chiari, quindi riporta "ancora più scuro." Una cellula appena sul lato chiaro riceve un'inibizione più debole, quindi riporta "ancora più chiaro." Il risultato è un potenziamento dei bordi integrato: il tuo sistema visivo esagera ogni confine, il che normalmente ti aiuta a vedere i contorni degli oggetti — ma qui inventa strisce che non esistono.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `digits = '0123456789abcdef'` | Le 16 cifre esadecimali, così la cifra `n` è `digits[n]` |
| `pair = digits[v // 16] + digits[v % 16]` | Divide `v` (0–255) nelle sue due cifre esadecimali |
| `'#' + pair + pair + pair` | Ripete la coppia per rosso, verde e blu — quantità uguali danno il grigio |
| `v = 32 + i * 22` | La luminosità di ogni banda sale di 22, da 32 fino a 230 |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Questa versione doveva disegnare la stessa scala liscia da scuro a
    chiaro, ma le bande escono in un ordine mescolato! Una riga in
    `gray()` usa l'operatore sbagliato. Trovala e correggila così il
    gradiente sale di nuovo in modo liscio.

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

digits = '0123456789abcdef'

def gray(v):
    pair = digits[v % 16] + digits[v % 16]
    return '#' + pair + pair + pair

def filled_rect(x, y, w, h, color):
    monty.penup()
    monty.goto(x, y)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    for _ in range(2):
        monty.forward(w)
        monty.left(90)
        monty.forward(h)
        monty.left(90)
    monty.end_fill()

bands = 10
band_w = 36
band_h = 280
left = -bands * band_w / 2

for i in range(bands):
    v = 32 + i * 22
    filled_rect(left + i * band_w, -band_h / 2, band_w, band_h, gray(v))`);
</script>

La riga difettosa costruisce entrambe le cifre esadecimali da `v % 16`, scartando l'importante prima cifra. La correzione è `digits[v // 16] + digits[v % 16]` — la divisione intera dà la cifra delle "sedicine" e il resto dà la cifra delle "unità."

## Esperimenti

1. **Usa più bande, più strette.** Cambia `bands = 10` in `bands = 20`, `band_w = 36` in `band_w = 18`, e `v = 32 + i * 22` in `v = 32 + i * 11`. Saprai che ha funzionato quando la scala sembra quasi un gradiente liscio — ma le strisce fantasma ci sono ancora.

2. **Inverti il gradiente.** Cambia la riga della luminosità in `v = 230 - i * 22`. Saprai che ha funzionato quando le bande vanno da chiaro a scuro da sinistra a destra invece.

3. **Rendilo un gradiente blu.** In `gray()`, cambia la riga di ritorno in `return '#0000' + pair` così cambia solo il canale blu. Saprai che ha funzionato quando le bande passano da quasi-nero a blu brillante — vedi ancora le bande di Mach a colori?

4. **Testa il limite dell'illusione.** Cambia il passo da `22` a `4` (un gradiente molto sottile). Saprai che ha funzionato quando le bande sono quasi della stessa sfumatura — le strisce fantasma sono più deboli ora?

!!! mascot-celebration "Hai Colto i Tuoi Occhi a Barare!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Dieci rettangoli piatti, zero strisce nel codice — eppure strisce
    ovunque tu guardi. Hai anche imparato a costruire qualsiasi colore
    esadecimale da un numero usando `//` e `%`.
    Prossimo: **Sfera di Vasarely** — una griglia piatta di punti che si
    rigonfia fuori dalla pagina.
