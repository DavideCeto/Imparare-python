---
title: Matematica e Aritmetica
description: Padroneggia gli operatori aritmetici di Python, la precedenza degli operatori, la divisione intera, il modulo e l'elevamento a potenza — poi collega la matematica alla grafica turtle.
generated_by: claude skill chapter-content-generator
date: 2026-06-28 10:10:29
version: 0.09
---

# Matematica e Aritmetica

## Riepilogo

Python è una potente calcolatrice. Questo capitolo esplora ogni operatore aritmetico:
divisione intera (`//`), resto (`%`), elevamento a potenza (`**`), ordine delle operazioni,
numeri negativi e notazione scientifica. Imparerai anche ad assegnare più
variabili in una volta e a usare operatori aumentati come `+=` per rendere il tuo codice più breve.

## Concetti Trattati

Questo capitolo tratta i seguenti 10 concetti del grafo di apprendimento:

1. Multiple Assignment
2. Augmented Assignment Operators
3. Division Returns Float
4. Integer Division Operator
5. Modulo Operator
6. Exponentiation Operator
7. Arithmetic Operators
8. Order of Operations
9. Negative Numbers
10. Scientific Notation Floats

## Prerequisiti

Questo capitolo si basa sui concetti di:

- [Capitolo 3: Variabili e Numeri](../03-variables-and-numbers/index.md)

---

Alla fine di questa lezione sarai in grado di:

- Calcolare risultati usando i sette operatori aritmetici di Python (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Spiegare la differenza tra la divisione normale (`/`) e la divisione intera (`//`)
- Usare operatori di assegnazione aumentata come `+=` per aggiornare una variabile in un solo passaggio
- Disegnare qualsiasi poligono regolare applicando la formula `360 / lati` alla tua turtle

Python conosce già tutta la matematica. Quando scrivi un'espressione come `10 * 3` o `2 ** 8`, Python la valuta all'istante — nessuna calcolatrice necessaria.

!!! mascot-welcome "Benvenuto/a al Capitolo 6!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Questo è il capitolo in cui Python diventa il tuo aiutante matematico personale! Esploreremo ogni operatore aritmetico che Python conosce — inclusi alcuni che non esistono in Scratch — e finiremo usando la matematica per disegnare qualsiasi poligono regolare tu possa immaginare. Programmiamo insieme!

## Operatori Aritmetici

Un **operatore aritmetico** è un simbolo che dice a Python di eseguire un calcolo matematico.
Ne conosci già quattro dalla lezione di matematica: `+`, `-`, `*` e `/`.
Python ne aggiunge altri tre particolarmente utili nella programmazione.

Ecco l'insieme completo:

| Operatore | Nome | Esempio | Risultato |
|----------|------|---------|--------|
| `+` | Addizione | `10 + 3` | `13` |
| `-` | Sottrazione | `10 - 3` | `7` |
| `*` | Moltiplicazione | `10 * 3` | `30` |
| `/` | Divisione | `10 / 3` | `3.3333...` |
| `//` | Divisione Intera | `10 // 3` | `3` |
| `%` | Modulo (resto) | `10 % 3` | `1` |
| `**` | Elevamento a Potenza | `10 ** 3` | `1000` |

Gli ultimi tre — `//`, `%` e `**` — potrebbero essere nuovi per te, ma li userai costantemente tutti e tre.

!!! mascot-tip "Ponte con Scratch"
    ![Monty with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch, la tavolozza verde **Operators** ha blocchi per `+`, `-`, `×` e `÷`. Python usa le stesse idee ma tu digiti i simboli direttamente invece di trascinare blocchi. I tre operatori bonus di Python — `**`, `//` e `%` — non hanno equivalenti in Scratch, ma sbloccano un intero nuovo mondo di trucchi matematici!

Il programma qui sotto esegue tutti e sette gli operatori insieme così puoi vedere il loro output fianco a fianco.

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di cliccare su Run, guarda due righe: `print(10 / 3)` e `print(10 // 3)`.
    Pensi che stamperanno lo stesso numero o numeri diversi?
    E `print(10 % 3)` — a cosa equivale "il resto dopo la divisione"?
    Fai le tue previsioni, poi clicca su Run per scoprirlo!

## Provalo Ora

Modifica il codice qui sotto e clicca **Run** per vedere il risultato.

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

<div class="cm-lab cm-text-only">
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
initCmLab('', `print("Addition:        ", 10 + 3)
print("Subtraction:     ", 10 - 3)
print("Multiplication:  ", 10 * 3)
print("Division:        ", 10 / 3)
print("Integer division:", 10 // 3)
print("Modulo:          ", 10 % 3)
print("Exponentiation:  ", 10 ** 3)`);
</script>

Avevi indovinato? `10 / 3` e `10 // 3` danno risposte *diverse* — una mantiene il decimale, l'altra lo scarta. E `10 % 3` è uguale a `1`, perché 10 ÷ 3 = 3 con **1** di resto.

## Come Funziona

Guardiamo più da vicino i tre operatori che potrebbero essere nuovi per te.

**`/` — La divisione restituisce sempre un float.** Un **float** (abbreviazione di "numero a virgola mobile") è qualsiasi numero con una virgola decimale — come `3.3333`, `5.0` o `-0.75`. In Python, l'operatore `/` dà *sempre* un float, anche quando i numeri si dividono esattamente: `10 / 2` dà `5.0`, non `5`.

**`//` — La divisione intera mantiene solo il numero intero.** L'operatore `//` divide e scarta tutto ciò che viene dopo la virgola decimale. `10 // 3` = `3`. Pensalo come chiedersi: "Quante volte entra *completamente* 3 dentro 10?" Tre volte — con qualcosa che avanza.

**`%` — Il modulo ti dà il resto.** Dopo aver inserito tre 3 dentro 10 (cioè 9), rimane `10 − 9 = 1` di resto, quindi `10 % 3` = `1`. Il modulo è utile per verificare se un numero è pari (`n % 2 == 0` è `True` quando n è pari) e per creare pattern ripetuti.

**`**` — Elevamento a potenza.** Due asterischi insieme significano "elevato alla potenza di." `2 ** 8` = 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 256. `10 ** 3` = 10 × 10 × 10 = 1000.

### Osservalo: L'Orologio del Modulo

Il resto è più facile da capire come **conteggio circolare**. L'Orologio del Modulo qui sotto mostra `%` in due modi contemporaneamente: contando intorno a un quadrante che si ripete al raggiungimento del divisore, e dividendo i puntini in righe uguali con gli avanzi evidenziati in arancione. Prima di toccare i cursori, prevedi: **quanto vale `17 % 5`?** Poi trascina i cursori e verifica.

<iframe src="../../sims/modulo-clock/main.html" height="502" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Modulo Clock](../../sims/modulo-clock/index.md){ .md-button }

Sposta il divisore a **2** e muovi il dividendo — il simulatore ti dice se ogni numero è pari o dispari. Questo è esattamente il trucco `n % 2` che userai nei capitoli successivi.

## Ordine delle Operazioni

Python segue lo stesso ordine delle operazioni che usi nella lezione di matematica — **PEMDAS**:

1. Le **P**arentesi si calcolano per prime
2. Gli **E**sponenti (`**`) subito dopo
3. **M**oltiplicazione, **D**ivisione, `//` e `%` — da sinistra a destra
4. **A**ddizione e **S**ottrazione — da sinistra a destra

| Espressione | Come la legge Python | Risultato |
|------------|---------------------|--------|
| `2 + 3 * 4` | `2 + (3 * 4)` = `2 + 12` | `14` |
| `(2 + 3) * 4` | `5 * 4` | `20` |
| `10 - 2 ** 3` | `10 - (2 ** 3)` = `10 - 8` | `2` |
| `15 // 4 % 2` | `(15 // 4) % 2` = `3 % 2` | `1` |

Nel dubbio, aggiungi parentesi. `(2 + 3) * 4` è più chiaro di `2 + 3 * 4`, e le parentesi extra non causano mai errori.

### Osservalo: Guarda un'Espressione Risolversi

!!! mascot-thinking "Cosa Pensi Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il MicroSim qui sotto inizia con `2 + 3 * 4`. Quale operazione calcolerà
    Python per prima — il `+` o il `*`? E quale sarà il risultato finale?
    Fai la tua previsione, poi clicca su Next Step per osservare l'espressione
    risolversi un'operazione alla volta!

<iframe src="../../sims/expression-evaluator/main.html" height="422" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Expression Evaluator](../../sims/expression-evaluator/index.md){ .md-button }

Avevi indovinato? Prova ogni espressione nel menu a tendina — l'ultima, `17 // 5 + 17 % 5`, mostra come `//` e `%` lavorano in squadra.

## Numeri Negativi

I numeri negativi funzionano esattamente come ti aspetteresti — basta mettere un segno meno davanti:

```python
temperature = -15
print(temperature + 5)    # -10
print(temperature * -2)   # 30   (negative × negative = positive)
print(abs(temperature))   # 15   (abs() gives the absolute value)
```

Python segue le regole standard dei segni: negativo × positivo = negativo, negativo × negativo = positivo.

## Notazione Scientifica dei Float

I numeri molto grandi o molto piccoli possono essere scritti in **notazione scientifica** usando la lettera `e`.
Il numero dopo `e` è la potenza di dieci per cui moltiplicare:

```python
speed_of_light = 3e8        # 3 × 10^8 = 300,000,000
electron_mass  = 9.11e-31   # 9.11 × 10^−31 (incredibly tiny)
print(speed_of_light)       # 300000000.0
print(2.5e3)                # 2500.0
```

Vedrai la notazione scientifica più spesso nelle simulazioni scientifiche e quando lavori con probabilità molto piccole.

## Assegnazione Multipla

Python ti permette di assegnare valori a due o più variabili sulla stessa riga.
Questo si chiama **assegnazione multipla**, e funziona elencando i nomi delle variabili a sinistra e i valori a destra, separati da virgole:

```python
x, y = 10, 20
print(x)    # 10
print(y)    # 20
```

L'assegnazione multipla è particolarmente potente per **scambiare due variabili** in una sola riga — qualcosa che normalmente richiede tre righe:

```python
a = 5
b = 100
a, b = b, a      # swap in one line!
print(a, b)      # 100  5
```

## Operatori di Assegnazione Aumentata

I programmatori hanno spesso bisogno di aggiornare una variabile aggiungendole qualcosa, sottraendole qualcosa, o raddoppiandola.
Python fornisce un'abbreviazione chiamata **operatori di assegnazione aumentata**:

| Abbreviazione | Equivale a | Effetto |
|-----------|---------|--------|
| `x += 5` | `x = x + 5` | Aggiunge 5 a x |
| `x -= 5` | `x = x - 5` | Sottrae 5 da x |
| `x *= 2` | `x = x * 2` | Raddoppia x |
| `x /= 2` | `x = x / 2` | Dimezza x (restituisce un float) |
| `x //= 2` | `x = x // 2` | Dimezza x come intero |
| `x %= 3` | `x = x % 3` | Mantiene il resto dopo ÷ 3 |
| `x **= 2` | `x = x ** 2` | Eleva x al quadrato |

Userai `+=` costantemente una volta che inizierai a scrivere cicli.
Per esempio, `count += 1` aggiunge 1 a un contatore ogni volta che il ciclo si ripete.

## Matematica e Turtle: Disegnare Qualsiasi Poligono Regolare

Ecco dove l'aritmetica incontra l'arte.
Ogni **poligono regolare** — una forma in cui tutti i lati sono uguali e tutti gli angoli sono uguali — ha una proprietà fondamentale:
la turtle deve girare dello **stesso angolo** a ogni angolo, e quell'angolo è sempre:

```
turn_angle = 360 / number_of_sides
```

- Triangolo (3 lati): `360 / 3` = **120°** per svolta
- Quadrato (4 lati): `360 / 4` = **90°** per svolta
- Pentagono (5 lati): `360 / 5` = **72°** per svolta
- Esagono (6 lati): `360 / 6` = **60°** per svolta

Il programma qui sotto disegna un poligono — ma manca la riga che calcola l'angolo di svolta.

!!! mascot-thinking "Tocca a Te — Aggiungi la Riga Mancante"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    La turtle vuole disegnare un triangolo ma non sa di quanto girare a ogni angolo.
    Aggiungi **una riga** sotto il commento per calcolare `turn_angle` usando `360` e `sides`.
    Usa `/` (non `//`) così la formula dà un angolo decimale preciso per qualsiasi poligono!

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
t = turtle.Turtle()
sides = 3
# Add one line here: calculate turn_angle using 360 and sides

for i in range(sides):
    t.forward(100)
    t.right(turn_angle)`);
</script>

Una volta che il triangolo appare, prova a cambiare `sides` in `5` o `6` — la formula si adatta automaticamente!

## Esperimenti

Prova questi cambiamenti al programma del poligono qui sopra. Per ciascuno, prevedi prima cosa succederà, poi eseguilo per verificare!

1. Cambia `sides = 3` in `sides = 5`. **Saprai che ha funzionato quando** vedi un pentagono a cinque lati.
2. Cambia in `sides = 6`. **Saprai che ha funzionato quando** vedi un esagono che somiglia a una cella di un nido d'ape.
3. Prova `sides = 360`. **Saprai che ha funzionato quando** la turtle traccia qualcosa che sembra quasi un cerchio perfetto.
4. Aggiungi `t.pencolor("blue")` prima del ciclo `for`. **Saprai che ha funzionato quando** tutte le linee diventano blu.
5. Cambia `t.forward(100)` in `t.forward(300 // sides)`. **Saprai che ha funzionato quando** i poligoni più grandi disegnano linee più lunghe e quelli più piccoli disegnano linee più corte.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai sbloccato l'intero toolkit aritmetico di Python — sette operatori, l'ordine delle operazioni, e due potenti scorciatoie di assegnazione. Soprattutto, hai collegato la matematica all'arte con un'unica formula. È esattamente così che pensano i programmatori! Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Commentati](./references.md)
