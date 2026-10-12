# Variabili per il Tuo Disegno

Alla fine di questa lezione sarai in grado di:

- Memorizzare un numero in una variabile e usarlo nel tuo codice
- Cambiare la dimensione di un quadrato modificando solo una riga
- Spiegare perché le variabili rendono i programmi più facili da modificare

Nella lezione del quadrato semplice, i numeri `100` e `90` apparivano otto volte ciascuno. Se volevi un quadrato più grande dovevi cambiare otto righe. Le **variabili** ti permettono di scrivere il numero una volta e usarlo ovunque — cambia la variabile e cambia tutto il disegno.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto a rendere più intelligente il tuo codice? Oggi ti mostrerò come funzionano le variabili —
    e perché ogni programmatore le usa. Programmiamo insieme!

## Cos'è una Variabile?

Una **variabile** è una scatola con un nome che contiene un valore. La crei scrivendo un nome, un segno di uguale, e il valore:

```python
distance = 100
```

Dopo questa riga, Python ricorda che `distance` è uguale a `100`. Ogni volta che scrivi `distance` più avanti nel tuo codice, Python usa `100` al suo posto.

Dai alle variabili nomi descrittivi — `distance` è molto più chiaro di `d` o `x`.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Imposta [distance] a 100"** nel cassetto Variabili.
    In Python, `distance = 100` fa esattamente la stessa cosa: crea una variabile chiamata
    `distance` e ci memorizza dentro il valore `100`.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 100
angle = 90

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La tartaruga usa `distance` per ogni chiamata `forward()` e `angle` per ogni chiamata `right()`.
    Quale forma disegnerà? Fai la tua previsione — poi clicca Esegui per scoprirlo!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere Monty disegnare direttamente su questa pagina.
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

distance = 100
angle = 90

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)`);
</script>

Avevi indovinato? Con `angle = 90`, ogni svolta è un quarto di cerchio, quindi la tartaruga disegna un quadrato perfetto.

**Se vedi un messaggio di errore rosso:** Controlla che il nome della tua variabile sia scritto esattamente nello stesso modo ovunque — `distance` e `Distance` sono due nomi diversi in Python.

## Come Funziona

Python legge il file dall'alto verso il basso. Quando raggiunge `distance = 100`, memorizza il valore `100` in memoria sotto il nome `distance`. Ogni volta che vede dopo `forward(distance)`, cerca quel valore memorizzato e lo usa — proprio come leggere un appunto che hai lasciato a te stesso.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `distance = 100` | Crea una variabile chiamata `distance` e ci memorizza dentro `100` |
| `angle = 90` | Crea una variabile chiamata `angle` e ci memorizza dentro `90` |
| `monty.forward(distance)` | Si muove avanti di 100 passi (legge il valore della variabile) |
| `monty.right(angle)` | Gira a destra di 90 gradi (legge il valore della variabile) |

!!! mascot-warning "Errore Comune: Errore di Battitura nel Nome della Variabile"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se scrivi `distanse` su una riga e `distance` su un'altra, Python le tratta come due
    variabili diverse — e la seconda non ha ancora nessun valore. Vedrai un `NameError`.
    Python distingue anche tra maiuscole e minuscole: `Distance` ≠ `distance`.

## Verifica di Apprendimento

!!! mascot-warning "Trova il Bug!"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe disegnare un quadrato, ma va in crash con un `NameError`.
    C'è un errore di battitura in un nome di variabile. Riesci a trovarlo e correggerlo?

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

distnace = 80
angle = 90

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)

monty.forward(distance)
monty.right(angle)`);
</script>

## Esperimenti

Prova questi cambiamenti al codice sopra. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia `distance = 100` in `distance = 150`.
   **Saprai che ha funzionato quando** il quadrato è notevolmente più grande di prima.

2. Cambia `distance = 100` in `distance = 40`.
   **Saprai che ha funzionato quando** il quadrato è circa la metà.

3. Cambia `angle = 90` in `angle = 120` e riduci le quattro coppie a tre coppie di `forward`/`right`.
   **Saprai che ha funzionato quando** vedi un triangolo invece di un quadrato.

4. Aggiungi `monty.color('purple')` appena prima della prima riga `forward`.
   **Saprai che ha funzionato quando** tutti e quattro i lati del quadrato sono viola.

5. Aggiungi una terza variabile: `monty.pensize(thickness)` e imposta `thickness = 5` in cima.
   **Saprai che ha funzionato quando** le linee sono notevolmente più spesse, e puoi cambiare `thickness` in un solo posto per influenzare tutti e quattro i lati.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato le variabili — una delle idee più potenti in tutta la programmazione!
    Nel prossimo laboratorio combinerai le variabili con un ciclo `for` così non dovrai
    ripetere affatto quelle quattro righe. Programmiamo insieme!
