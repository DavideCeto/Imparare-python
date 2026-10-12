---
hide:
    - toc
---
# Spirale Triangolare

Alla fine di questo laboratorio sarai in grado di:

- Usare `right(120)` per creare una spirale triangolare con angoli equilateri netti
- Colorare ogni terzo della spirale di un colore caldo diverso usando la divisione intera
- Capire come `i // n` raggruppa i segmenti in fasce di colore invece di scorrere segmento per segmento

Tre fasce di colore caldo — rosso, arancione, e oro — si estendono verso l'esterno lungo i bracci di una spirale triangolare stretta. Cambia un numero e l'intero carattere della forma cambia.

!!! mascot-welcome "Benvenuto alla Spirale Triangolare!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Abbiamo visto spirali quadrate (90°) e spirali esagonali (60°). Ora spingiamo l'angolo ancora più oltre —
    120° dà gli angoli più netti finora. Programmiamo insieme!

## Come Funziona

Un triangolo equilatero ha angoli interni di 60° e **angoli esterni di 120°** (360° ÷ 3 = 120°). Girare di 120° a ogni passo dà alla spirale angoli triangolari.

Per la colorazione, `(i // 60) % 3` divide il ciclo di 180 passi in tre terzi uguali e sceglie un colore per ogni terzo. La divisione intera (`//`) raggruppa i segmenti insieme invece di scorrere uno per uno.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

colors = ['crimson', 'darkorange', 'gold']
step = 2

for i in range(180):
    monty.color(colors[(i // 60) % 3])
    monty.forward(step)
    monty.right(120)
    step += 1.5
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La spirale quadrata aveva 4 lati per rivoluzione e quella esagonale ne aveva 6.
    Quanti lati per rivoluzione ha la spirale triangolare?
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

colors = ['crimson', 'darkorange', 'gold']
step = 2

for i in range(180):
    monty.color(colors[(i // 60) % 3])
    monty.forward(step)
    monty.right(120)
    step += 1.5`);
</script>

**3 lati** per rivoluzione — uno per ogni rotazione di 120°. La spirale forma angoli triangolari netti. Avevi indovinato?

## Come Funziona

`(i // 60) % 3` funziona così: per i primi 60 passi, `i // 60 = 0`, quindi colore 0 (crimson). Per i passi 60–119, `i // 60 = 1`, quindi colore 1 (arancione). Per i passi 120–179, colore 2 (oro). Questo crea fasce solide lungo i bracci della spirale invece di sfarfallio segmento per segmento.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `colors = [...]` | Tre tonalità calde — una per ogni terzo del ciclo |
| `(i // 60) % 3` | Raggruppa 60 segmenti in ogni fascia di colore |
| `monty.right(120)` | Angolo triangolare — 360° ÷ 3 = 120° |
| `step += 1.5` | Fa crescere il passo a ogni segmento |
| `range(180)` | 180 passi = 60 "triangoli" completi (3 lati ciascuno) |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Passa ai Colori per Segmento"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Cambia `(i // 60) % 3` in `i % 3`. Ora ogni singolo segmento scorre attraverso
    i tre colori. Prevedi come sarà diverso l'aspetto — poi eseguilo per controllare!

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

colors = ['crimson', 'darkorange', 'gold']
step = 2

for i in range(180):
    monty.color(colors[i % 3])
    monty.forward(step)
    monty.right(120)
    step += 1.5`);
</script>

Con `i % 3`, ogni lato di ogni piccolo triangolo ottiene il proprio colore — creando un pattern a righe, segmento per segmento. La versione `i // 60` dà fasce di colore più ampie attraverso interi bracci della spirale.

## Esperimenti

1. **Prova 4 colori con `i // 45`.** Usa `['red','orange','gold','yellow']` e `(i // 45) % 4`. Saprai che ha funzionato quando la spirale ha quattro regioni di colore distinte.

2. **Falla girare nell'altra direzione.** Cambia `right(120)` in `left(120)`. Saprai che ha funzionato quando la spirale si avvolge nella direzione opposta.

3. **Raddoppia la velocità di crescita.** Cambia `step += 1.5` in `step += 3`. Gli spazi tra i bracci si allargano drammaticamente. Saprai che ha funzionato quando solo 2–3 rivoluzioni entrano sullo schermo.

4. **Inizia da un passo grande.** Cambia `step = 2` in `step = 40`. La spirale inizia già espansa. Saprai che ha funzionato quando i primi giri sono già larghi.

!!! mascot-celebration "Pensiero Acuto!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai scoperto due modi per colorare una spirale: `i % n` per pattern segmento per segmento,
    e `i // n` per fasce di colore ampie. Lo stesso trucco funziona in qualsiasi ciclo!
    Prossimo: **Spirale che Collassa verso l'Interno** — avvolgersi verso un punto invece di crescere verso l'esterno.
