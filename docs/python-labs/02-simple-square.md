# Disegnare un Quadrato

Alla fine di questa lezione sarai in grado di:

- Muovere la tartaruga avanti e girarla usando `forward()` e `right()`
- Spiegare cosa controllano i numeri dentro `forward(100)` e `right(90)`
- Disegnare un quadrato ripetendo gli stessi due comandi quattro volte

La tartaruga inizia al centro del canvas e disegna linee mentre si muove —
come una penna attaccata a un robot. In questa lezione le darai i tuoi primi
comandi di disegno e guarderai apparire un quadrato.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ciao, sono Monty! Sono un serpente Python, e oggi ti insegnerò come
    farmi disegnare un quadrato sullo schermo. È più facile di quanto pensi —
    programmiamo insieme!

## Muoversi e Girare

I due comandi più importanti della tartaruga sono `forward()` e `right()`.

`forward(100)` dice alla tartaruga di camminare **avanti** di 100 passi, disegnando una linea mentre procede.
Il numero dentro le parentesi si chiama **parametro** — controlla quanto fa il comando.
Qui, `100` imposta quanto sarà lungo ogni lato del quadrato.

`right(90)` dice alla tartaruga di **girare a destra** di 90 gradi senza disegnare nulla.
Il numero 90 è un quarto di giro — esattamente l'angolo a ogni angolo di un quadrato.

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Muovi di 10 passi"** e il blocco **"Gira ↻ di 15 gradi"**.
    In Python, `forward(100)` e `right(90)` fanno esattamente le stesse cose — solo scritte in modo diverso!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di cliccare Esegui, conta i comandi `forward` nel codice sopra.
    Quanti lati disegnerà la tartaruga? Fai la tua previsione — poi scoprilo!

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

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)

monty.forward(100)
monty.right(90)`);
</script>

Avevi indovinato? La tartaruga disegna **4 lati** — uno per ogni coppia `forward()` + `right()` — creando un quadrato perfetto.

**Se vedi un messaggio di errore rosso:** Controlla l'ortografia — Python distingue tra maiuscole e minuscole,
quindi `Forward(100)` non funzionerà ma `forward(100)` sì.
Assicurati di avere le parentesi `()` attorno a ogni numero.

## Come Funziona

La tartaruga inizia al centro del canvas girata verso destra.
Ogni `forward(100)` la muove di 100 passi nella direzione in cui è attualmente girata.
Ogni `right(90)` la ruota di 90 gradi in senso orario — un quarto di giro.
Dopo quattro coppie avanti-e-gira la tartaruga torna dove è partita: un quadrato perfetto.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `import turtle` | Carica la libreria di grafica turtle |
| `monty = turtle.Turtle()` | Crea una tartaruga e la chiama `monty` |
| `monty.shape('turtle')` | Mostra l'icona a forma di tartaruga invece di una semplice freccia |
| `monty.forward(100)` | Si muove di 100 passi avanti, disegnando una linea |
| `monty.right(90)` | Gira di 90 gradi in senso orario (un angolo di un quadrato) |

!!! mascot-warning "Errore Comune: Angolo di Svolta Sbagliato"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Se cambi `right(90)` in `right(100)` gli angoli non si chiuderanno e non otterrai un quadrato!
    Un quadrato ha bisogno di svolte di *esattamente* 90 gradi. Provalo e guarda quale forma ottieni invece.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Completa il Triangolo"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Un triangolo ha 3 lati. Ogni angolo di un triangolo equilatero gira di 120 gradi.
    Al programma sotto manca **una riga**. Aggiungila così che Monty disegni un triangolo completo!

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

# Draw a triangle - each turn is 120 degrees
monty.forward(100)
monty.right(120)

monty.forward(100)
# Add the missing line here!

monty.forward(100)
monty.right(120)`);
</script>

## Esperimenti

Prova questi cambiamenti al codice del quadrato sopra. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Cambia `100` in `150` in tutte e quattro le chiamate `forward`.
   **Saprai che ha funzionato quando** il quadrato è notevolmente più grande di prima.

2. Cambia tutte e quattro le chiamate `right(90)` in `right(120)` e rimuovi una coppia `forward`/`right` (lasciandone solo tre).
   **Saprai che ha funzionato quando** vedi un triangolo invece di un quadrato.

3. Aggiungi `monty.color('red')` alla riga appena prima del primo `forward`.
   **Saprai che ha funzionato quando** tutti e quattro i lati del quadrato sono rossi invece di neri.

4. Aggiungi `monty.speed(1)` dopo `monty.shape('turtle')` per rallentare molto Monty.
   **Saprai che ha funzionato quando** puoi guardarlo disegnare un lato alla volta.

5. Prova a disegnare due quadrati fianco a fianco: dopo le quattro coppie, aggiungi
   `monty.penup()`, poi `monty.forward(150)`, poi `monty.pendown()`,
   poi ripeti di nuovo le quattro coppie `forward`/`right`.
   **Saprai che ha funzionato quando** vedi due quadrati separati sul canvas.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai appena scritto il tuo primo programma di disegno con la tartaruga — e funziona!
    Nella prossima lezione imparerai a usare un ciclo `for` così non dovrai
    ripetere quelle quattro righe ancora e ancora. Programmiamo insieme!
