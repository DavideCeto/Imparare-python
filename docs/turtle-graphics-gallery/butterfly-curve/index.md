---
hide:
    - toc
---
# Curva a Farfalla

Alla fine di questo laboratorio sarai in grado di:

- Tracciare la curva a farfalla di Temple H. Fay usando la sua equazione polare parametrica
- Capire come `exp(cos(t))` e `cos(4t)` si combinano per creare le forme delle ali
- Vedere come una singola equazione parametrica può produrre forme organiche e complesse

La curva a farfalla è una famosa curva parametrica scoperta da Temple H. Fay nel 1989. La sua equazione polare `r = exp(cos t) - 2cos(4t) + sin⁵(t/12)` genera una forma che assomiglia incredibilmente ad ali di farfalla.

!!! mascot-welcome "Benvenuto alla Curva a Farfalla!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questa curva fu scoperta nel 1989 da Temple H. Fay.
    Un'equazione fa una farfalla — matematica e arte in perfetta armonia!
    Programmiamo insieme!

## Come Funziona

Per t da 0 a 12π, calcola `r = exp(cos(t)) - 2*cos(4*t) + sin(t/12)^5`. Poi converti da polare a cartesiano: `x = scale * r * cos(t)`, `y = scale * r * sin(t)`. Il risultato con molti lobi ha bisogno di 12π per completarsi.

## Codice di Esempio

```python
import turtle
import math
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

scale = 50
steps = 2000
monty.pencolor('royalblue')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 12 * math.pi * i / steps
    r = (math.exp(math.cos(t)) - 2 * math.cos(4 * t)
         + math.sin(t / 12) ** 5)
    x = scale * r * math.cos(t)
    y = scale * r * math.sin(t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La formula mescola `exp(cos(t))` con `cos(4t)`.
    Il risultato sembrerà ali, una stella, o qualcosa di completamente diverso?
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

scale = 50
steps = 2000
monty.pencolor('royalblue')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 12 * math.pi * i / steps
    r = (math.exp(math.cos(t)) - 2 * math.cos(4 * t)
         + math.sin(t / 12) ** 5)
    x = scale * r * math.cos(t)
    y = scale * r * math.sin(t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

**Ali di farfalla** — il termine `exp(cos t)` crea i grandi lobi mentre `cos(4t)` aggiunge piccole oscillazioni che formano i dettagli delle ali. Avevi indovinato?

## Come Funziona

`exp(cos(t))` oscilla tra `exp(-1) ≈ 0,37` e `exp(1) ≈ 2,72`. Il termine sottratto `2*cos(4*t)` può rendere `r` negativo, aggiungendo dettagli interni. Il termine `sin(t/12)^5` crea l'allungamento delle punte delle ali variando lentamente attraverso l'intervallo di 12π.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `math.exp(math.cos(t))` | Lobo principale — oscilla tra 0,37 e 2,72 |
| `2 * math.cos(4 * t)` | Sottrae 4 oscillazioni — crea il dettaglio delle ali |
| `math.sin(t / 12) ** 5` | Termine che varia lentamente — allunga le punte delle ali |
| `12 * math.pi` | Giro completo per far chiudere la curva |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Rimuovi un Termine"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Rimuovi `math.sin(t / 12) ** 5` dalla formula (impostalo a 0).
    Come cambia la curva senza quel termine?
    Prevedi, poi eseguilo!

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

scale = 50
steps = 2000
monty.pencolor('crimson')
monty.pensize(1)
monty.penup()

for i in range(steps + 1):
    t = 12 * math.pi * i / steps
    r = math.exp(math.cos(t)) - 2 * math.cos(4 * t)
    x = scale * r * math.cos(t)
    y = scale * r * math.sin(t)
    if i == 0:
        monty.goto(x, y)
        monty.pendown()
    else:
        monty.goto(x, y)`);
</script>

Senza `sin(t/12)^5`, la curva è più simmetrica — due lobi uguali invece della forma allungata della punta dell'ala.

## Esperimenti

1. **Cambia la scala.** Prova `scale = 70`. Saprai che ha funzionato quando la curva è più grande.

2. **Aumenta i passi.** Prova `steps = 5000`. Saprai che ha funzionato quando la curva è più lisciata.

3. **Usa il coefficiente 3 invece di 2 per `cos(4t)`.** I lobi interni cambieranno. Saprai che ha funzionato quando il dettaglio dell'ala sembra diverso.

4. **Traccia la curva in più colori.** Dividi il ciclo in segmenti di `steps//6` punti ciascuno e cambia il colore per ogni segmento. Saprai che ha funzionato quando parti diverse della curva hanno colori diversi.

!!! mascot-celebration "Matematica Bellissima!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai programmato una delle curve parametriche più eleganti della matematica!
    La curva a farfalla mostra come `exp`, `cos`, e `sin` possano congiurare per fare arte.
    Prossimo: **Stella Epicicloidale** — cerchi che rotolano all'esterno di cerchi.
