---
hide:
    - toc
---
# Onde Concentriche

Alla fine di questo laboratorio sarai in grado di:

- Disegnare ellissi concentriche per simulare increspature d'acqua da più punti di caduta
- Usare colori sfumati per dare un senso di forza dell'onda che diminuisce con la distanza
- Combinare più fonti di increspature che si sovrappongono e creano pattern di interferenza

Tre sistemi di anelli concentrici centrati in punti diversi — come tre ciottoli lanciati nell'acqua. Dove gli anelli si sovrappongono, creano sottili pattern di interferenza.

!!! mascot-welcome "Benvenuto alle Onde Concentriche!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Lancia un ciottolo in acqua calma e guarda gli anelli espandersi verso l'esterno.
    Lancia tre ciottoli e guarda gli anelli interferire tra loro!
    Programmiamo insieme la matematica delle onde!

## Come Funziona

`ripple(cx, cy, n_rings, max_r, color)` disegna `n_rings` cerchi concentrici da un centro. La dimensione della penna diminuisce con ogni anello (gli anelli esterni sono più sottili — meno energia). Tre centri di increspatura sono posizionati in punti diversi.

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.speed(0)
monty.hideturtle()

def ripple(cx, cy, n_rings, max_r, base_color):
    for i in range(1, n_rings + 1):
        r = i * max_r / n_rings
        strength = n_rings - i + 1
        monty.pensize(max(1, strength // 3))
        monty.pencolor(base_color)
        monty.penup()
        monty.goto(cx, cy - r)
        monty.pendown()
        monty.circle(r)

ripple(-80, -20, 8, 100, 'royalblue')
ripple(60, 40, 7, 80, 'deepskyblue')
ripple(0, -60, 6, 70, 'steelblue')
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Tre centri di increspatura in posizioni diverse — i loro anelli si sovrapporranno o resteranno separati?
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

def ripple(cx, cy, n_rings, max_r, base_color):
    for i in range(1, n_rings + 1):
        r = i * max_r / n_rings
        strength = n_rings - i + 1
        monty.pensize(max(1, strength // 3))
        monty.pencolor(base_color)
        monty.penup()
        monty.goto(cx, cy - r)
        monty.pendown()
        monty.circle(r)

ripple(-80, -20, 8, 100, 'royalblue')
ripple(60, 40, 7, 80, 'deepskyblue')
ripple(0, -60, 6, 70, 'steelblue')`);
</script>

Gli anelli **si sovrappongono** dove i sistemi di increspatura si incontrano — creando un pattern di interferenza visivo ai loro confini. Avevi indovinato?

## Come Funziona

`goto(cx, cy - r)` si muove al fondo di ogni cerchio prima di disegnarlo. `circle(r)` disegna il cerchio completo. La dimensione maggiore della penna per gli anelli interni simula più energia d'onda vicino alla fonte.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `r = i * max_r / n_rings` | Raggi degli anelli uniformemente spaziati dal centro al massimo |
| `strength = n_rings - i + 1` | Gli anelli interni sono più forti (numero più alto) |
| `pensize(max(1, strength//3))` | Linee più spesse per gli anelli interni, più forti |
| `goto(cx, cy - r)` | Posiziona la tartaruga al fondo del cerchio |

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi una Quarta Increspatura"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Aggiungi una quarta chiamata a `ripple()` in una posizione a tua scelta con colore `'navy'`.
    Dove si sovrapporrà di più con gli anelli esistenti?

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

def ripple(cx, cy, n_rings, max_r, base_color):
    for i in range(1, n_rings + 1):
        r = i * max_r / n_rings
        strength = n_rings - i + 1
        monty.pensize(max(1, strength // 3))
        monty.pencolor(base_color)
        monty.penup()
        monty.goto(cx, cy - r)
        monty.pendown()
        monty.circle(r)

ripple(-80, -20, 8, 100, 'royalblue')
ripple(60, 40, 7, 80, 'deepskyblue')
ripple(0, -60, 6, 70, 'steelblue')
ripple(-30, 60, 5, 60, 'navy')`);
</script>

Quattro sistemi di increspatura sovrapposti — più regioni di interferenza dove gli anelli si incrociano.

## Esperimenti

1. **Cambia la spaziatura degli anelli.** Sostituisci gli anelli uniformemente spaziati con `r = max_r * (i / n_rings) ** 2` — la spaziatura al quadrato fa raggrupparsi gli anelli vicino al centro. Saprai che ha funzionato quando gli anelli interni sono più densi.

2. **Anima l'increspatura.** Disegna gli anelli in ordine inverso (il più esterno prima) per creare un effetto di animazione. Saprai che ha funzionato quando gli anelli sembrano espandersi verso l'esterno.

3. **Usa anelli colorati.** Dai a ogni anello una tonalità leggermente diversa — anelli interni più scuri, esterni più chiari. Saprai che ha funzionato quando c'è un gradiente dal centro al bordo.

4. **Un'increspatura gigante.** Chiama `ripple(0, 0, 15, 170, 'teal')` una volta. Saprai che ha funzionato quando 15 anelli riempiono quasi tutto il canvas.

!!! mascot-celebration "Facendo Onde!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai simulato increspature d'acqua con cerchi concentrici e sfumatura della dimensione della penna!
    La stessa matematica modella le onde sonore, le onde luminose, e persino i pattern di trasmissione radio.
    Prossimo: **Categoria 7 — Curve Matematiche!**
