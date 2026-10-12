---
hide:
    - toc
---
# Testo a Spirale

Alla fine di questo laboratorio sarai in grado di:

- Usare `turtle.write()` per posizionare testo a posizioni calcolate
- Posizionare caratteri lungo un percorso a spirale usando coordinate polari
- Capire come `setheading()` fa rivolgere ogni carattere nella direzione giusta

Ogni carattere di un messaggio è posizionato lungo una spirale verso l'esterno, ruotato per essere rivolto tangenzialmente lungo la curva. Il risultato è un testo che si avvolge attorno al centro come un guscio di chiocciola.

!!! mascot-welcome "Benvenuto al Testo a Spirale!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    `turtle.write()` può posizionare qualsiasi testo alla posizione attuale della tartaruga.
    Questo laboratorio combina questo con la matematica della spirale per scrivere un messaggio in una spirale!
    Programmiamo insieme!

## Come Funziona

Posiziona i caratteri di un messaggio uno alla volta. Per il carattere `i`, il raggio della spirale cresce con `i` e l'angolo avanza di un passo fisso. `setheading()` allinea ogni carattere tangenzialmente alla direzione della spirale.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

message = "PYTHON IS FUN! " * 3
angle_step = 20
r_start = 20
r_step = 2.2

for i, ch in enumerate(message):
    angle = math.radians(i * angle_step)
    r = r_start + i * r_step
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.goto(x, y)
    heading = (i * angle_step + 90) % 360
    monty.setheading(heading)
    monty.pencolor('royalblue')
    monty.write(ch, font=('Arial', 10, 'bold'))
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni carattere è posizionato a un raggio crescente e ruotato per essere rivolto verso la direzione della spirale.
    I caratteri sembreranno una spirale leggibile, o solo lettere disperse?
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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

message = "PYTHON IS FUN! " * 3
angle_step = 20
r_start = 20
r_step = 2.2

for i, ch in enumerate(message):
    angle = math.radians(i * angle_step)
    r = r_start + i * r_step
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.goto(x, y)
    heading = (i * angle_step + 90) % 360
    monty.setheading(heading)
    monty.pencolor('royalblue')
    monty.write(ch, font=('Arial', 10, 'bold'))`);
</script>

Il messaggio **si avvolge verso l'esterno** — ogni carattere è rivolto tangenzialmente alla curva della spirale. Avevi indovinato?

## Come Funziona

`heading = (i * angle_step + 90) % 360` aggiunge 90° alla direzione radiale perché `setheading(0)` punta a destra (direzione radiale). Aggiungere 90° fa rivolgere la tartaruga tangenzialmente (lungo la spirale). `math.cos(angle)`, `math.sin(angle)` converte da polare a cartesiano per il posizionamento.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `enumerate(message)` | Dà sia l'indice `i` sia il carattere `ch` |
| `r = r_start + i * r_step` | Il raggio cresce linearmente — spirale di Archimede |
| `heading = (i * angle_step + 90) % 360` | Direzione tangenziale — perpendicolare al raggio |
| `monty.write(ch, font=...)` | Posiziona un singolo carattere alla posizione della tartaruga |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Messaggio"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia il messaggio con il tuo nome ripetuto più volte.
    Prevedi: la spirale sembrerà diversa con un messaggio più corto o più lungo?

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
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()
monty.penup()

message = "HELLO WORLD! " * 4
angle_step = 18
r_start = 20
r_step = 2.5

colors = ['crimson', 'darkorange', 'gold', 'forestgreen', 'royalblue', 'purple']

for i, ch in enumerate(message):
    angle = math.radians(i * angle_step)
    r = r_start + i * r_step
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    monty.goto(x, y)
    heading = (i * angle_step + 90) % 360
    monty.setheading(heading)
    monty.pencolor(colors[i % len(colors)])
    monty.write(ch, font=('Arial', 10, 'bold'))`);
</script>

Testo a spirale colorato come l'arcobaleno — ogni carattere ottiene un colore ciclico per un effetto più festivo.

## Esperimenti

1. **Spirale più stretta.** Diminuisci `angle_step` a 10. Saprai che ha funzionato quando più rivoluzioni della spirale entrano nel canvas.

2. **Carattere più grande.** Cambia `font=('Arial', 10, 'bold')` in `font=('Arial', 14, 'bold')` e aumenta `r_step = 4`. Saprai che ha funzionato quando appaiono lettere più grandi.

3. **Spirale logaritmica.** Sostituisci `r = r_start + i * r_step` con `r = 10 * math.exp(0.06 * i)`. Saprai che ha funzionato quando i caratteri si spaziano più velocemente vicino all'esterno.

4. **Inverti la spirale.** Cambia `angle_step` in negativo. Saprai che ha funzionato quando la spirale si avvolge in senso orario invece che antiorario.

!!! mascot-celebration "Tipografia in Movimento!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai combinato coordinate polari con `turtle.write()` per creare testo a spirale!
    Questa tecnica è usata nel design dei loghi e nella tipografia artistica.
    Prossimo: **Display a Sette Segmenti** — numeri digitali da segmenti di linea.
