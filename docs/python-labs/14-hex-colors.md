# Colori Esadecimali e Testo Stilizzato

Alla fine di questa lezione sarai in grado di:

- Impostare il colore di una tartaruga usando un **codice colore esadecimale** come `'#FF5733'`
- Usare `turtle.Screen().bgcolor()` per colorare lo sfondo del canvas
- Scrivere testo stilizzato sul canvas con un carattere, dimensione, e peso specifici

I nomi di colore come `'red'` e `'blue'` sono comodi, ma ti danno solo poche dozzine di scelte. I **codici colore esadecimali** ti danno accesso a più di 16 milioni di colori — ogni tonalità immaginabile — usando un codice a sei cifre che appare come `#FF5733`.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pronto a dipingere con milioni di colori? Oggi imparerai i codici colore che designer
    e sviluppatori web usano ogni giorno — e disegnerai un biglietto di auguri colorato con testo stilizzato!
    Programmiamo insieme!

## Codici Colore Esadecimali

Un **codice colore esadecimale** inizia con `#` seguito da sei caratteri — ciascuno una cifra da 0–9 o una lettera da A–F. I sei caratteri sono in tre coppie, che controllano quanta luce **rossa**, **verde**, e **blu** mescolare:

```
# RR GG BB
  FF 57 33   →  lots of red, some green, a little blue  →  a warm orange-red
```

- `#FF0000` — rosso puro (rosso al massimo, niente verde, niente blu)
- `#00FF00` — verde puro
- `#0000FF` — blu puro
- `#FFFFFF` — bianco (tutti e tre al massimo)
- `#000000` — nero (tutti e tre a zero)

Puoi usare uno strumento come [coolors.co](https://coolors.co) o cercare su Google "hex color picker" per trovare qualsiasi colore desideri.

## Testo Stilizzato

`monty.write()` disegna del testo nella posizione attuale della tartaruga. Aggiungi un argomento `font` per controllare il carattere, la dimensione, e lo stile:

```python
monty.write("Ciao!", font=("Arial", 40, "bold"))
```

I tre valori in `font` sono: **nome del carattere**, **dimensione in punti**, e **stile** (`"normal"`, `"bold"`, o `"italic"`).

## Codice di Esempio

```python
import turtle

screen = turtle.Screen()
screen.bgcolor('#1A1A2E')

monty = turtle.Turtle()
monty.hideturtle()
monty.speed(10)

monty.penup()
monty.goto(-120, 60)
monty.color('#E94560')
monty.write("Ciao,", font=("Arial", 48, "bold"))

monty.goto(-80, -20)
monty.color('#F5A623')
monty.write("Python!", font=("Arial", 48, "bold"))

monty.goto(-60, -100)
monty.color('#00C9A7')
monty.write("Programmiamo!", font=("Arial", 24, "italic"))
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Lo sfondo è `'#1A1A2E'` — un blu molto scuro. I colori del testo sono codici esadecimali brillanti.
    Come pensi che apparirà il contrasto? Il testo sarà facile da leggere?
    Fai la tua previsione — poi clicca Esegui!

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

screen = turtle.Screen()
screen.bgcolor('#1A1A2E')

monty = turtle.Turtle()
monty.hideturtle()
monty.speed(10)

monty.penup()
monty.goto(-120, 60)
monty.color('#E94560')
monty.write("Ciao,", font=("Arial", 48, "bold"))

monty.goto(-80, -20)
monty.color('#F5A623')
monty.write("Python!", font=("Arial", 48, "bold"))

monty.goto(-60, -100)
monty.color('#00C9A7')
monty.write("Programmiamo!", font=("Arial", 24, "italic"))`);
</script>

Avevi indovinato? Sfondo blu notte scuro con testo rosso, arancione, e verde acqua vivaci — il contrasto fa risaltare i colori in un modo che i colori con nome raramente raggiungono.

## Come Funziona

`turtle.Screen()` ti dà un riferimento alla finestra di disegno stessa. `bgcolor()` colora lo sfondo prima che avvenga qualsiasi disegno della tartaruga — così tutto ciò che disegni appare sopra di esso.

`monty.hideturtle()` rimuove completamente l'icona del cursore così il testo resta da solo senza una forma di tartaruga nell'angolo.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `turtle.Screen()` | Ottiene un riferimento alla finestra di disegno |
| `screen.bgcolor('#1A1A2E')` | Colora lo sfondo del canvas con un colore esadecimale |
| `monty.hideturtle()` | Nasconde l'icona della tartaruga — utile per disegni di solo testo |
| `monty.goto(-120, 60)` | Muove il cursore del testo a quella posizione |
| `monty.write("Ciao,", font=("Arial", 48, "bold"))` | Scrive testo in Arial grassetto da 48 punti |

!!! mascot-tip "Trovare il Colore Perfetto"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Cerca su Google **"hex color picker"** e vedrai una ruota dei colori — clicca qualsiasi colore e copia
    il codice `#RRGGBB` che mostra. Incollalo direttamente nella tua stringa Python!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Progetta il Tuo Biglietto"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto imposta uno sfondo ma scrive solo una riga di testo.
    Aggiungi **altre due** chiamate a `write()` con colori esadecimali e posizioni diverse per completare
    un biglietto di auguri a tre righe. Scegli i tuoi colori usando un selettore di colori esadecimali!

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

screen = turtle.Screen()
screen.bgcolor('#0D3B66')

monty = turtle.Turtle()
monty.hideturtle()
monty.speed(10)
monty.penup()

monty.goto(-100, 60)
monty.color('#FAF0CA')
monty.write("Ciao, programmatore!", font=("Arial", 36, "bold"))

# Aggiungi qui altre due righe con write(), con colori e posizioni diversi`);
</script>

## Esperimenti

Prova questi cambiamenti al codice del biglietto di auguri. Prevedi prima, poi esegui!

1. Cambia `screen.bgcolor('#1A1A2E')` in `screen.bgcolor('#FFFFFF')` (bianco).
   **Saprai che ha funzionato quando** lo sfondo diventa bianco — ora controlla se il testo è ancora leggibile.

2. Cambia uno stile di carattere da `"bold"` a `"italic"`.
   **Saprai che ha funzionato quando** quella parola appare inclinata invece che spessa.

3. Cambia una dimensione di carattere da `48` a `72`.
   **Saprai che ha funzionato quando** il testo è notevolmente più grande e potrebbe estendersi fuori dallo schermo.

4. Usa `'Times New Roman'` come nome del carattere per una riga.
   **Saprai che ha funzionato quando** quella riga ha un carattere con grazie invece del sans-serif predefinito.

5. Aggiungi un rettangolo riempito dietro il testo usando `begin_fill()`, `end_fill()`, e un ciclo per disegnare quattro lati — poi usa `hideturtle()` e scrivi il testo sopra.
   **Saprai che ha funzionato quando** il testo appare dentro una scatola colorata.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato 16 milioni di colori e testo stilizzato — i mattoni fondamentali del design digitale!
    Nel prossimo laboratorio userai funzioni matematiche per tracciare un'onda sinusoidale attraverso il canvas.
    Programmiamo insieme!
