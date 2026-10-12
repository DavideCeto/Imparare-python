# Comandi Turtle

Alla fine di questa lezione sarai in grado di:

- Muovere una tartaruga avanti, indietro, e in qualsiasi direzione usando `forward()`, `back()`, `left()`, e `right()`
- Cambiare il colore della penna e lo spessore della linea con `color()` e `pensize()`
- Cambiare l'icona della tartaruga usando `shape()`

Ogni programma con la tartaruga inizia con le stesse tre righe di configurazione, e poi dai alla tartaruga una sequenza di comandi — muoviti qui, girati di là, disegna di questo colore. In questo laboratorio proverai i comandi più importanti e vedrai esattamente cosa fa ciascuno.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ciao, sono Monty! Vivo dentro il tuo browser e disegno qualsiasi cosa tu mi dica.
    In questa lezione imparerai i comandi che mi fanno muovere, girare, e cambiare colore.
    Programmiamo insieme!

## Muoversi e Girare

La tartaruga inizia al centro del canvas, girata verso destra. Quattro comandi controllano il movimento:

- `forward(n)` — camminare avanti di `n` passi, disegnando una linea
- `back(n)` — camminare indietro di `n` passi, disegnando una linea
- `left(n)` — girare a sinistra di `n` gradi (senso antiorario)
- `right(n)` — girare a destra di `n` gradi (senso orario)

Due comandi controllano la penna:

- `color('name')` — imposta il colore di disegno (prova `'red'`, `'blue'`, `'green'`, `'orange'`)
- `pensize(n)` — imposta lo spessore della linea; `1` è fine, `10` è grosso

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato **"Muovi di 10 passi"**, **"Gira ↻ gradi"**, e **"Imposta il colore della penna"**.
    `forward()`, `right()`, e `color()` fanno esattamente le stesse cose in Python!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

monty.pensize(3)
monty.color('blue')
monty.forward(100)

monty.right(90)
monty.color('red')
monty.forward(100)

monty.right(90)
monty.color('green')
monty.forward(100)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La tartaruga disegna tre segmenti di linea. Di che colore sarà ciascun segmento?
    Fai la tua previsione — poi clicca Esegui per scoprirlo!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato direttamente su questa pagina.
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

monty.pensize(3)
monty.color('blue')
monty.forward(100)

monty.right(90)
monty.color('red')
monty.forward(100)

monty.right(90)
monty.color('green')
monty.forward(100)`);
</script>

Avevi indovinato? La tartaruga disegna un segmento blu, gira a destra, disegna un segmento rosso, gira a destra di nuovo, e finisce con un segmento verde — una forma a U rovesciata in tre colori.

**Se vedi un messaggio di errore rosso:** Controlla che ogni comando finisca con `()` e che il nome del colore sia tra virgolette — `'blue'` non `blue`.

## Come Funziona

La tartaruga inizia girata verso destra. Ogni chiamata a `color()` imposta il colore della penna per ogni linea disegnata dopo di essa — finché non chiami di nuovo `color()`. `right(90)` ruota la tartaruga di 90 gradi in senso orario, facendola girare verso il basso dopo la prima svolta.

La chiamata `shape('turtle')` alla riga 3 cambia l'icona del cursore da una semplice freccia a una forma di tartaruga. Puoi anche provare `'arrow'`, `'circle'`, `'square'`, o `'classic'`.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `import turtle` | Carica la libreria di grafica turtle |
| `monty = turtle.Turtle()` | Crea una tartaruga e la chiama `monty` |
| `monty.shape('turtle')` | Imposta il cursore come icona a forma di tartaruga |
| `monty.pensize(3)` | Rende la linea spessa 3 pixel |
| `monty.color('blue')` | Imposta il colore della penna su blu |
| `monty.forward(100)` | Si muove di 100 passi avanti, disegnando una linea |
| `monty.right(90)` | Ruota di 90 gradi in senso orario |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi la Riga Mancante"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe disegnare una linea verde che va a destra, poi una linea blu che va in giù.
    Ma entrambe le linee escono dello stesso colore! Aggiungi **una riga** dopo `monty.right(90)` per correggerlo.

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

monty.color('green')
monty.pensize(3)
monty.forward(100)

monty.right(90)
# Add one line here to change the color to blue
monty.forward(100)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia `monty.shape('turtle')` in `monty.shape('circle')`.
   **Saprai che ha funzionato quando** il cursore è un cerchio riempito invece di un'icona a forma di tartaruga.

2. Cambia `monty.pensize(3)` in `monty.pensize(10)`.
   **Saprai che ha funzionato quando** tutte e tre le linee sono notevolmente più spesse.

3. Aggiungi `monty.back(50)` dopo l'ultimo `forward(100)`.
   **Saprai che ha funzionato quando** la tartaruga torna indietro, lasciando una linea verde sopra il segmento verde esistente.

4. Aggiungi `monty.left(90)` invece di `monty.right(90)` per entrambe le svolte.
   **Saprai che ha funzionato quando** la forma curva verso l'alto invece che verso il basso.

5. Aggiungi `monty.hideturtle()` come ultimissima riga.
   **Saprai che ha funzionato quando** l'icona della tartaruga scompare, lasciando un disegno pulito.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai imparato i comandi principali della tartaruga — i blocchi costitutivi di ogni disegno in questo corso!
    Prova gli esperimenti sopra per esplorare cosa altro può fare Monty. Programmiamo insieme!
