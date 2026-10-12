---
hide:
    - toc
---
# Spirale di Linee Arcobaleno

Alla fine di questo laboratorio sarai in grado di:

- Aggiungere un ciclo di colori a una spirale crescente usando `i % len(colors)`
- Vedere come l'intervallo di fasciatura interagisce con il periodo della spirale
- Capire perché lo stesso pattern modulo funziona sia per i colori che per le forme

La spirale quadrata di Archimede ritorna — questa volta ogni segmento è colorato scorrendo
attraverso sei tonalità arcobaleno. Le fasce di colore marciano diagonalmente attraverso i bracci della spirale.

!!! mascot-welcome "Benvenuto alla Spirale di Linee Arcobaleno!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    In questo laboratorio aggiungerai solo due righe extra alla spirale del laboratorio precedente
    e trasformerai un pattern monocromatico in un arcobaleno completo. Questo è il potere di `%`!
    Programmiamo insieme!

## Come Funziona l'Arcobaleno

Le uniche aggiunte alla spirale di Archimede sono:
1. Una lista `colors` con sei tonalità
2. `monty.color(colors[i % 6])` dentro il ciclo — una riga

Poiché ogni rivoluzione della spirale ha 4 segmenti e i colori scorrono ogni 6 segmenti,
i confini di colore tagliano diagonalmente attraverso i bracci della spirale invece di allinearsi con gli angoli.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
step = 2

for i in range(200):
    monty.color(colors[i % 6])
    monty.forward(step)
    monty.right(90)
    step += 1.5
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Ci sono 6 colori e 200 segmenti. Quante volte si ripeterà l'intera sequenza di colori?
    (Suggerimento: 200 ÷ 6 = ?) Fai la tua previsione — poi clicca Esegui per scoprirlo!

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

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
step = 2

for i in range(200):
    monty.color(colors[i % 6])
    monty.forward(step)
    monty.right(90)
    step += 1.5`);
</script>

200 ÷ 6 = 33 cicli completi con 2 segmenti rimanenti — così l'arcobaleno completo appare **33 volte**, ognuno un po' più grande del precedente. Avevi indovinato?

## Come Funziona

`colors[i % 6]` mappa il contatore del ciclo `i` a un indice di colore: 0→rosso, 1→arancione, 2→giallo, 3→verde, 4→blu, 5→viola, 0→rosso di nuovo. Il pattern si ripete ogni 6 passi non importa quanto grande diventi `i`.

Poiché la spirale ha simmetria a 4 lati ma il periodo del colore è 6, le strisce diagonali di colore attraversano gli angoli del quadrato in punti diversi a ogni rivoluzione — creando un pattern visivamente complesso da una matematica molto semplice.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = [...]` | Sei tonalità arcobaleno |
| `i % 6` | Mappa qualsiasi intero a 0–5 per indicizzare la lista di colori |
| `monty.color(colors[i % 6])` | Cambia colore a ogni segmento |
| Tutte le altre righe | Identiche alla spirale di Archimede |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Cambia il Periodo del Colore"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cosa succede quando il periodo del colore corrisponde al periodo della spirale?
    Cambia `i % 6` in `i % 4`. Con 4 colori e angoli a 4 lati, i colori si allineeranno con gli angoli.
    Prevedi come sembrerà — poi eseguilo per controllare!

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

colors = ['red', 'orange', 'blue', 'green']
step = 2

for i in range(200):
    monty.color(colors[i % 4])
    monty.forward(step)
    monty.right(90)
    step += 1.5`);
</script>

Con `i % 4` e una spirale quadrata a 90°, ogni colore occupa esattamente un lato per rivoluzione — creando quattro strisce diagonali nette allineate con i bracci della spirale.

## Esperimenti

1. **Prova 2 colori.** Cambia in `['red', 'blue']` e `i % 2`. Saprai che ha funzionato quando la spirale alterna rosso e blu segmento per segmento.

2. **Prova 12 colori.** Usa l'intera lista di 12 tonalità della ruota dei colori dal laboratorio **Spicchi della Ruota dei Colori**. Saprai che ha funzionato quando appaiono fasce arcobaleno più strette e più varie.

3. **Cambia in una spirale triangolare.** Mantieni i colori arcobaleno e cambia `right(90)` in `right(120)`. Saprai che ha funzionato quando la spirale ha angoli triangolari con fasce arcobaleno diagonali.

4. **Colora per rivoluzione.** Sostituisci `i % 6` con `(i // 4) % 6`. Ora tutti i quattro segmenti di ogni rivoluzione condividono lo stesso colore. Saprai che ha funzionato quando appaiono anelli quadrati a colore solido.

!!! mascot-celebration "Lavoro Fantastico!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scoperto che `i % n` e `i // n` ti danno due modi diversi di mappare il tempo al colore —
    segmento per segmento contro rivoluzione per rivoluzione. Stessa spirale, aspetto completamente diverso!
    Prossimo: **Spirale Esagonale** — cambiare un angolo trasforma l'intera forma.
