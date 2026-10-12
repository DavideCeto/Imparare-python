---
hide:
    - toc
---
# Display a Sette Segmenti

Alla fine di questo laboratorio sarai in grado di:

- Rappresentare ogni cifra come una maschera di bit di quali dei 7 segmenti sono "accesi"
- Disegnare segmenti di linea orizzontali e verticali a posizioni calcolate
- Visualizzare un numero a più cifre usando un dizionario di pattern di segmento

Un display a sette segmenti come quelli sugli orologi digitali e le calcolatrici. Ogni cifra è codificata come un pattern di 7 flag binari — uno per segmento. Una funzione di disegno legge i flag e disegna i segmenti accesi.

!!! mascot-welcome "Benvenuto al Display a Sette Segmenti!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Gli orologi digitali usano display a sette segmenti — ogni cifra è solo 7 interruttori on/off!
    Questo laboratorio costruisce un renderer di display guidato da dizionario in Python.
    Programmiamo insieme!

## Come Funziona

Ogni cifra è memorizzata come una tupla di 7 booleani: `(top, top-left, top-right, middle, bot-left, bot-right, bottom)`. Una funzione `draw_digit(n, x, y)` controlla ogni flag e disegna il segmento di linea corrispondente.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

w, h = 30, 50
segments = {
    '0': (1,1,1,0,1,1,1), '1': (0,0,1,0,0,1,0),
    '2': (1,0,1,1,1,0,1), '3': (1,0,1,1,0,1,1),
    '4': (0,1,1,1,0,1,0), '5': (1,1,0,1,0,1,1),
    '6': (1,1,0,1,1,1,1), '7': (1,0,1,0,0,1,0),
    '8': (1,1,1,1,1,1,1), '9': (1,1,1,1,0,1,1),
}

def seg_line(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

def draw_digit(ch, x, y):
    s = segments.get(ch, (0,)*7)
    monty.pensize(4)
    monty.pencolor('red')
    if s[0]: seg_line(x, y+h, x+w, y+h)
    if s[1]: seg_line(x, y+h/2, x, y+h)
    if s[2]: seg_line(x+w, y+h/2, x+w, y+h)
    if s[3]: seg_line(x, y+h/2, x+w, y+h/2)
    if s[4]: seg_line(x, y, x, y+h/2)
    if s[5]: seg_line(x+w, y, x+w, y+h/2)
    if s[6]: seg_line(x, y, x+w, y)

number = "2026"
start_x = -(len(number) * (w + 10)) / 2
for i, ch in enumerate(number):
    draw_digit(ch, start_x + i * (w + 10), -h/2)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ogni cifra è codificata come 7 flag — il codice cerca il pattern per ogni carattere.
    Sembrerà un vero display digitale, o solo linee disperse?
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

w, h = 30, 50
segments = {
    '0': (1,1,1,0,1,1,1), '1': (0,0,1,0,0,1,0),
    '2': (1,0,1,1,1,0,1), '3': (1,0,1,1,0,1,1),
    '4': (0,1,1,1,0,1,0), '5': (1,1,0,1,0,1,1),
    '6': (1,1,0,1,1,1,1), '7': (1,0,1,0,0,1,0),
    '8': (1,1,1,1,1,1,1), '9': (1,1,1,1,0,1,1),
}

def seg_line(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

def draw_digit(ch, x, y):
    s = segments.get(ch, (0,)*7)
    monty.pensize(4)
    monty.pencolor('red')
    if s[0]: seg_line(x, y+h, x+w, y+h)
    if s[1]: seg_line(x, y+h/2, x, y+h)
    if s[2]: seg_line(x+w, y+h/2, x+w, y+h)
    if s[3]: seg_line(x, y+h/2, x+w, y+h/2)
    if s[4]: seg_line(x, y, x, y+h/2)
    if s[5]: seg_line(x+w, y, x+w, y+h/2)
    if s[6]: seg_line(x, y, x+w, y)

number = "2026"
start_x = -(len(number) * (w + 10)) / 2
for i, ch in enumerate(number):
    draw_digit(ch, start_x + i * (w + 10), -h/2)`);
</script>

Un **display digitale realistico** — i pattern di segmento producono cifre riconoscibili. Avevi indovinato?

## Come Funziona

Il dizionario `segments` mappa ogni carattere cifra a una 7-tupla. Le posizioni:
- **s[0]**: orizzontale in alto, **s[1]**: verticale in alto a sinistra, **s[2]**: verticale in alto a destra
- **s[3]**: orizzontale al centro, **s[4]**: verticale in basso a sinistra, **s[5]**: verticale in basso a destra, **s[6]**: orizzontale in basso

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `segments = {'0': (1,1,1,0,1,1,1), ...}` | Dizionario: cifra → 7 flag di segmento |
| `s = segments.get(ch, (0,)*7)` | Cerca il pattern, predefinito tutti spenti |
| `if s[0]: seg_line(...)` | Disegna solo i segmenti che sono accesi |
| `start_x = -(len(number)*(w+10))/2` | Centra il display |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Mostra l'Anno della Tua Nascita"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `number = "2026"` con l'anno in cui sei nato.
    Prevedi quali forme di cifra appariranno — poi eseguilo per controllare!

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

w, h = 30, 50
segments = {
    '0': (1,1,1,0,1,1,1), '1': (0,0,1,0,0,1,0),
    '2': (1,0,1,1,1,0,1), '3': (1,0,1,1,0,1,1),
    '4': (0,1,1,1,0,1,0), '5': (1,1,0,1,0,1,1),
    '6': (1,1,0,1,1,1,1), '7': (1,0,1,0,0,1,0),
    '8': (1,1,1,1,1,1,1), '9': (1,1,1,1,0,1,1),
}

def seg_line(x1, y1, x2, y2):
    monty.penup(); monty.goto(x1, y1)
    monty.pendown(); monty.goto(x2, y2)

def draw_digit(ch, x, y):
    s = segments.get(ch, (0,)*7)
    monty.pensize(4)
    monty.pencolor('forestgreen')
    if s[0]: seg_line(x, y+h, x+w, y+h)
    if s[1]: seg_line(x, y+h/2, x, y+h)
    if s[2]: seg_line(x+w, y+h/2, x+w, y+h)
    if s[3]: seg_line(x, y+h/2, x+w, y+h/2)
    if s[4]: seg_line(x, y, x, y+h/2)
    if s[5]: seg_line(x+w, y, x+w, y+h/2)
    if s[6]: seg_line(x, y, x+w, y)

number = "12345"
start_x = -(len(number) * (w + 10)) / 2
for i, ch in enumerate(number):
    draw_digit(ch, start_x + i * (w + 10), -h/2)`);
</script>

Cifre verdi 1-5 visualizzate in sequenza — il pattern di segmento unico di ogni cifra è chiaramente visibile.

## Esperimenti

1. **Disegna un orologio.** Visualizza `"12:30"` aggiungendo un carattere due punti (due puntini). Saprai che ha funzionato quando appare un display orario.

2. **Anima un contatore.** Usa un ciclo per visualizzare da 0 a 9 uno alla volta. Saprai che ha funzionato quando il display scorre tra le cifre.

3. **Rendi il display più grande.** Cambia `w, h = 30, 50` in `w, h = 50, 80`. Saprai che ha funzionato quando appaiono cifre molto più grandi.

4. **Aggiungi segmenti di sfondo fiochi.** Disegna tutti i 7 segmenti in grigio scuro prima di disegnare quelli attivi. Saprai che ha funzionato quando i segmenti inattivi appaiono come ombre tenui.

!!! mascot-celebration "Numeri Digitali!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai costruito un renderer funzionante per display a sette segmenti!
    È esattamente così che i bancomat, le pompe di benzina, e le sveglie visualizzano i numeri.
    Prossimo: **Distintivo Circolare con Nome** — testo disposto in cerchio.
