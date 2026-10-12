# Disegnare un Segnale di Stop

Alla fine di questa lezione sarai in grado di:

- Usare le variabili per memorizzare il colore, la dimensione, e il numero di lati di una forma
- Usare un ciclo `for` per disegnare qualsiasi poligono regolare senza ripetere codice
- Riempire una forma con il colore usando `begin_fill()` ed `end_fill()`

Un segnale di stop è un ottagono — un poligono regolare a 8 lati. Invece di scrivere a mano otto
coppie `forward`/`right`, userai un ciclo e una formula per disegnarlo in solo
poche righe.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto a salire di livello? In questa lezione disegneremo un vero segnale di stop —
    riempimento rosso, testo STOP bianco, e tutto il resto. Un ciclo `for` farà tutto
    il lavoro pesante per noi. Programmiamo insieme!

## Usare le Variabili per le Proprietà della Forma

Quando memorizzi la dimensione e il colore in **variabili**, cambiare l'intero disegno è facile
quanto modificare una riga. Una **variabile** è una scatola con un nome che contiene un valore — dalle un nome
descrittivo così il codice è facile da leggere.

```python
distance = 50   # length of each side
sides = 8       # number of sides (8 = octagon)
my_color = "red"
```

L'angolo di svolta per qualsiasi poligono regolare segue una formula semplice: dividi 360 per il numero
di lati. Per un ottagono: 360 ÷ 8 = 45 gradi.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato le **variabili** nel cassetto Variabili — `imposta [distance] a 50`.
    In Python, `distance = 50` fa esattamente la stessa cosa: crea una variabile chiamata
    `distance` e ci memorizza dentro il valore 50.

## Riempire una Forma con il Colore

Due comandi lavorano in coppia per colorare l'interno di qualsiasi forma:

- `begin_fill()` — dice alla tartaruga "inizia a ricordare il percorso"
- `end_fill()` — dice alla tartaruga "adesso riempi tutto dentro quel percorso"

Tutto ciò che viene disegnato tra queste due chiamate viene riempito con il colore attuale. Se
ne dimentichi una delle due, il riempimento non apparirà.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides  # works for any regular polygon
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)
monty.begin_fill()

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.end_fill()
monty.hideturtle()

monty.penup()
monty.right(110)
monty.forward(80)
monty.color('white')
monty.write('STOP', font=("Arial", 30, "normal"))
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda la riga `for i in range(sides):` — e ricorda che `sides = 8`.
    Quante volte si ripeterà il ciclo? E di che colore sarà l'interno della forma?
    Fai le tue previsioni — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per disegnare il segnale di stop direttamente su questa pagina.
Nessun account necessario — tutto gira nel tuo browser.

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
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides  # works for any regular polygon
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)
monty.begin_fill()

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.end_fill()
monty.hideturtle()

monty.penup()
monty.right(110)
monty.forward(80)
monty.color('white')
monty.write('STOP', font=("Arial", 30, "normal"))`);
</script>

Avevi indovinato? Il ciclo gira **8 volte** (una per ogni lato dell'ottagono) e
l'interno si riempie di rosso perché `my_color = "red"` è stato impostato prima di `begin_fill()`.

## Come Funziona

La formula dell'angolo di svolta `360 / sides` è il segreto: gli angoli esterni di qualsiasi poligono
regolare sommano sempre esattamente a 360 gradi. Dividi per il numero di lati e ottieni
l'angolo per un angolo.

`goto(-50, 100)` muove la tartaruga a un angolo di partenza senza disegnare — `penup()` alza
prima la penna così non appare nessuna linea. `pendown()` la riabbassa prima che inizi il disegno.

`hideturtle()` rimuove l'icona della tartaruga quando il disegno è finito così non coprirà l'opera.

`write('STOP', font=...)` posiziona del testo nella posizione attuale della tartaruga usando la
famiglia di font, la dimensione, e lo stile specificati.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `distance = 50` | Lunghezza di ogni lato in pixel |
| `sides = 8` | Numero di lati — cambialo per ottenere un poligono diverso |
| `angle = 360 / sides` | Angolo di svolta — la formula funziona per qualsiasi poligono regolare |
| `my_color = "red"` | Memorizza il colore in una variabile così è facile da cambiare |
| `penup() / goto() / pendown()` | Si muove alla posizione di partenza senza disegnare una linea |
| `begin_fill() / end_fill()` | Riempie tutto ciò che viene disegnato tra di loro con il colore attuale |
| `for i in range(sides):` | Ripete il corpo del ciclo una volta per ogni lato |
| `hideturtle()` | Nasconde il cursore della tartaruga quando il disegno è finito |
| `write('STOP', font=...)` | Scrive del testo nella posizione attuale della tartaruga |

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe disegnare un ottagono rosso riempito, ma quando lo esegui la forma
    non ha riempimento — solo un contorno. Una riga è nel posto sbagliato. Riesci a trovarla e
    correggerla?

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
monty.shape('turtle')

distance = 50
sides = 8
angle = 360 / sides
my_color = "red"

monty.penup()
monty.goto(-50, 100)
monty.pendown()
monty.color(my_color)

for i in range(sides):
    monty.forward(distance)
    monty.right(angle)

monty.begin_fill()  # bug: this is in the wrong place!
monty.end_fill()
monty.hideturtle()`);
</script>

## Esperimenti

Prova questi cambiamenti al codice del segnale di stop sopra. Prevedi cosa succederà prima, poi eseguilo!

1. Cambia `my_color = "red"` in `"blue"`.
   **Saprai che ha funzionato quando** l'ottagono si riempie di blu invece di rosso.

2. Cambia `distance = 50` in `80`.
   **Saprai che ha funzionato quando** il segnale di stop è notevolmente più grande.

3. Cambia `sides = 8` in `6` — e nota che `angle = 360 / sides` resta uguale (si ricalcola automaticamente).
   **Saprai che ha funzionato quando** vedi un esagono riempito invece di un ottagono.

4. Cambia `'STOP'` con la tua propria parola.
   **Saprai che ha funzionato quando** la tua parola appare sul segnale in bianco.

5. Cambia `monty.color('white')` (il colore del testo) in `'yellow'`.
   **Saprai che ha funzionato quando** il testo sul segnale diventa giallo. Riesci ancora a leggerlo facilmente?

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai disegnato un segnale di stop usando variabili, un ciclo, e comandi di riempimento — Python sul serio!
    Prova a cambiare `sides` a 3 o 5 e guarda quali segnali puoi inventare.
    Programmiamo insieme!
