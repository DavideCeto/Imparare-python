---
hide:
    - toc
---
# Pulsazione di Anelli Concentrici

Alla fine di questo laboratorio sarai in grado di:

- Costruire un bersaglio sovrapponendo cerchi riempiti dal più grande al più piccolo
- Generare una sequenza decrescente dove ogni passo si restringe di una percentuale
- Spiegare come il contrasto tra colori caldi/freddi faccia sembrare un'immagine ferma vibrare

Un bersaglio di anelli che alternano colori caldi (arancione, cremisi) e colori freddi (blu, verde acqua), con gli anelli che si stringono sempre più sottili verso il centro. Fissalo e gli anelli sembrano scintillare e pulsare — i colori caldi spingono in avanti mentre quelli freddi si ritirano, e i tuoi occhi non si stabilizzano mai.

!!! mascot-welcome "Benvenuto alla Pulsazione di Anelli Concentrici!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I colori caldi balzano verso di te, i colori freddi sprofondano via
    — e quando li alterni in anelli che si restringono, l'intera
    immagine inizia a vibrare. Gli artisti op art chiamano questo
    vibrazione. Creiamone un po'!

## Come Funziona

Non esiste un comando "anello" — il trucco è la sovrapposizione. Disegniamo un cerchio riempito di raggio 180, poi uno leggermente più piccolo sopra di esso, poi uno ancora più piccolo, ciascuno nel colore successivo. Ogni cerchio copre il centro di quello precedente, così resta visibile solo un anello di ogni colore. Il divario tra i raggi inizia a 30 e viene moltiplicato per 0.85 ogni volta, così gli anelli diventano più stretti man mano che si affollano verso il centro.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['darkorange', 'royalblue', 'crimson', 'teal']

def filled_circle(r, color):
    monty.penup()
    monty.goto(0, -r)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    monty.circle(r)
    monty.end_fill()

r = 180.0
step = 30.0
i = 0
while r > 4:
    filled_circle(r, colors[i % 4])
    r = r - step
    step = step * 0.85
    if step < 5:
        step = 5
    i = i + 1
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il primo cerchio ha raggio 180 e ogni nuovo cerchio è più piccolo,
    con il passo che si riduce del 15% ogni volta.
    L'anello **più largo** finirà sul bordo esterno o al centro?
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

colors = ['darkorange', 'royalblue', 'crimson', 'teal']

def filled_circle(r, color):
    monty.penup()
    monty.goto(0, -r)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    monty.circle(r)
    monty.end_fill()

r = 180.0
step = 30.0
i = 0
while r > 4:
    filled_circle(r, colors[i % 4])
    r = r - step
    step = step * 0.85
    if step < 5:
        step = 5
    i = i + 1`);
</script>

L'anello più largo è all'esterno — la larghezza di ogni anello è uguale al `step` corrente, che inizia a 30 e si restringe a ogni ciclo. Avevi indovinato?

## Come Funziona

Il tuo occhio mette a fuoco i colori caldi (lunghezze d'onda lunghe, come rosso e arancione) in modo leggermente diverso dai colori freddi (lunghezze d'onda corte, come il blu). Posti fianco a fianco ad alto contrasto, il confine tra loro non si stabilizza mai del tutto sulla tua retina — i colori combattono, e il bordo sembra scintillare. La larghezza decrescente degli anelli amplifica questo effetto: man mano che gli anelli diventano più sottili verso il centro, i bordi in lotta si affollano sempre più vicini, così il centro del bersaglio ronza più forte.

## Tabella Esplicativa

| Riga | Cosa fa |
|------|-------------|
| `filled_circle(r, colors[i % 4])` | Dipinge un disco pieno — ogni disco copre il centro di quello precedente |
| `r = r - step` | Il cerchio successivo è più piccolo, lasciando visibile un anello del vecchio colore |
| `step = step * 0.85` | Ogni anello è il 15% più sottile dell'ultimo — una sequenza decrescente |
| `if step < 5: step = 5` | Mantiene gli anelli larghi almeno 5 pixel così il ciclo finisce sempre |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug"
    ![Monty warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Anche questa versione doveva disegnare un bersaglio — ma ottieni
    solo UN gigantesco disco pieno. Il ciclo disegna davvero sette
    cerchi in quattro colori. Dove sono finiti gli altri sei? Correggi
    il codice così tutti gli anelli appaiono.

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

colors = ['darkorange', 'royalblue', 'crimson', 'teal']

def filled_circle(r, color):
    monty.penup()
    monty.goto(0, -r)
    monty.setheading(0)
    monty.pendown()
    monty.pencolor(color)
    monty.fillcolor(color)
    monty.begin_fill()
    monty.circle(r)
    monty.end_fill()

r = 20.0
i = 0
while r < 181:
    filled_circle(r, colors[i % 4])
    r = r + 25
    i = i + 1`);
</script>

I cerchi vengono disegnati dal più piccolo al più grande, così ogni nuovo disco seppellisce tutti quelli precedenti — vedi solo l'ultimo, il cerchio più grande. La sovrapposizione funziona solo partendo dal più grande: inizia a `r = 180.0` e conta *all'indietro*.

## Esperimenti

1. **Crea anelli di larghezza uguale.** Elimina la riga `step = step * 0.85`. Saprai che ha funzionato quando ogni anello ha la stessa larghezza di 30 pixel — vibra ancora tanto?

2. **Aumenta la stretta.** Cambia `0.85` in `0.75`. Saprai che ha funzionato quando gli anelli si assottigliano molto più in fretta e il centro diventa un bersaglio denso e ronzante.

3. **Vai al massimo contrasto.** Cambia la lista dei colori in `['red', 'blue', 'red', 'blue']`. Saprai che ha funzionato quando il bersaglio è di sole due colori in contrasto — molte persone trovano che questa versione vibri di più.

4. **Calmalo.** Cambia i colori in `['navy', 'royalblue', 'steelblue', 'teal']` — tutti freddi. Saprai che ha funzionato quando gli anelli sembrano tranquilli invece di pulsare, dimostrando che il combattimento caldo/freddo era il motore.

!!! mascot-celebration "Hai Fatto Muovere un'Immagine Ferma!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Cerchi sovrapposti, un passo decrescente, e colori caldi/freddi in
    contrasto — questa è una macchina completa di vibrazione op art in
    circa 25 righe di Python. Questo chiude le illusioni ottiche!
    Esplora la **Galleria di Grafica Turtle** per la tua prossima sfida!
