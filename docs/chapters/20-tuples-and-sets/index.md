---
title: Tuple e Insiemi
description: Impara i tipi tuple e set di Python — sequenze immutabili per dati fissi, e collezioni non ordinate per elementi unici e matematica degli insiemi
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:20:00
version: 0.09
---

# Tuple e Insiemi

Alla fine di questa lezione sarai in grado di:

- Creare e scomporre le **tuple**, e spiegare quando usarle invece delle liste
- Restituire valori multipli da una funzione usando una tupla
- Creare un **insieme** (set) e usare `union()`, `intersection()`, e `difference()` per la matematica degli insiemi
- Verificare l'appartenenza in un insieme e aggiungere o rimuovere elementi

Python ti offre quattro tipi principali di collezione. Hai padroneggiato le liste. Ora conosciamo altri due: le tuple e gli insiemi.

!!! mascot-welcome "Benvenuto/a al Capitolo 20!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le tuple sono come liste bloccate sul posto — perfette per cose che non dovrebbero mai cambiare.
    Gli insiemi sono come sacchetti dove i duplicati sono vietati e l'ordine non conta.
    Esploriamo entrambi! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Tipo Tuple

Una **tupla** è una collezione ordinata e immutabile (non modificabile) di elementi.
La crei usando le parentesi, con gli elementi separati da virgole.

```python
point = (3, 5)
rgb   = (255, 128, 0)
empty = ()
```

Le tuple sembrano e si comportano molto come le liste, ma non possono essere cambiate dopo la creazione.
Non puoi aggiungere, rimuovere, o riassegnare elementi in una tupla.

### Quando Usare una Tupla Invece di una Lista

Usa una tupla quando i dati sono *fissi* e non dovrebbero cambiare:

| Caso d'uso | Esempio |
|----------|---------|
| Coordinate | `(x, y)` oppure `(x, y, z)` |
| Valori di colore RGB | `(255, 0, 128)` |
| Giorni della settimana | `("Mon", "Tue", ...)` |
| Valori di ritorno di funzioni | return `(lat, lng)` |

Usa una lista quando hai bisogno di aggiungere, rimuovere, o cambiare elementi nel tempo.

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
initCmLab('', `point = (3, 5)
print("Punto:", point)
print("x:", point[0], "y:", point[1])
print("Tipo:", type(point))

# Le tuple supportano indicizzazione e slicing come le liste:
colors = ("red", "green", "blue", "yellow")
print("Primo:", colors[0])
print("Ultimo:", colors[-1])
print("Slice:", colors[1:3])`);
</script>

## Sintassi della Tupla a un Solo Elemento

Una tupla con *un* solo elemento ha bisogno di una virgola finale — altrimenti Python vede solo delle parentesi attorno a un valore:

```python
not_a_tuple = (42)    # solo l'intero 42
is_a_tuple  = (42,)   # una tupla che contiene 42
```

La virgola finale è il segnale per Python che intendi una tupla.

## Scomposizione delle Tuple

La **scomposizione delle tuple** (tuple unpacking) assegna ogni elemento di una tupla a una variabile separata in un solo passo.
Questo rende il codice pulito ed espressivo.

```python
point = (10, 20)
x, y = point          # spacchetta in x e y
print(x)              # 10
print(y)              # 20
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto scompone una tupla con tre elementi.
    Quali valori pensi che avranno `a`, `b`, e `c`?
    Fai la tua previsione — poi eseguilo!

<div class="cm-lab cm-text-only">
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
initCmLab('-2', `rgb = (255, 128, 0)
r, g, b = rgb
print(f"Rosso={r}, Verde={g}, Blu={b}")

# Scambia due variabili con lo spacchettamento di tuple:
x = 10
y = 20
x, y = y, x
print(f"Dopo lo scambio: x={x}, y={y}")`);
</script>

## Le Tuple come Valori di Ritorno

Le funzioni possono restituire valori multipli impacchettandoli in una tupla.
Chi chiama la funzione scompone il risultato:

```python
def min_max(numbers):
    return (min(numbers), max(numbers))

lo, hi = min_max([3, 1, 7, 2, 9])
print(f"Min: {lo}, Max: {hi}")
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `def divide(a, b):
    quotient  = a // b   # divisione intera
    remainder = a % b    # resto
    return quotient, remainder   # restituisce una tupla

q, r = divide(17, 5)
print(f"17 / 5 = {q} con resto {r}")`);
</script>

## Il Tipo Set

Un **insieme** (set) è una collezione non ordinata di elementi **unici**. Due proprietà chiave:
1. Nessun duplicato — aggiungere lo stesso elemento due volte non ha effetto
2. Nessun ordine garantito — gli elementi possono essere stampati in qualsiasi ordine

Crea un insieme con le parentesi graffe `{}` oppure il costruttore `set()`:

```python
fruits = {"apple", "banana", "mango", "apple"}   # i duplicati vengono rimossi!
print(fruits)   # {"mango", "banana", "apple"} — l'ordine può variare
```

Gli insiemi sono più utili per:
- Rimuovere duplicati da una lista
- Verifiche di appartenenza rapide (più veloci delle liste per grandi collezioni)
- Operazioni matematiche sugli insiemi

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)   # rimuove i duplicati
print("Lista originale:", numbers)
print("Insieme senza duplicati:", unique)
print("Numero di elementi unici:", len(unique))

# Verifica di appartenenza:
print("3 in unique:", 3 in unique)
print("7 in unique:", 7 in unique)`);
</script>

## Metodi degli Insiemi: `add()`, `remove()`, `discard()`

- `s.add(x)` — aggiunge `x` all'insieme (nessun effetto se già presente)
- `s.remove(x)` — rimuove `x`; genera `KeyError` se non trovato
- `s.discard(x)` — rimuove `x` se presente; non fa nulla silenziosamente se non trovato

Usa `discard()` quando non sei sicuro se l'elemento esiste.

## Operazioni sugli Insiemi: Unione, Intersezione, Differenza

Prima di provarle, ecco cosa significa ogni operazione:

- **Unione (`|`)** — tutti gli elementi di entrambi gli insiemi (senza duplicati)
- **Intersezione (`&`)** — solo gli elementi che appaiono in *entrambi* gli insiemi
- **Differenza (`-`)** — elementi nel primo insieme ma non nel secondo

```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A | B  → {1, 2, 3, 4, 5, 6}   union
A & B  → {3, 4}               intersection
A - B  → {1, 2}               in A but not B
B - A  → {5, 6}               in B but not A
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-5"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-5')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-5')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-5"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-5"></div>
  </div>
</div>
<script>
initCmLab('-5', `python_students = {"Alice", "Bob", "Carol", "Dave"}
math_students   = {"Carol", "Dave", "Eve", "Frank"}

both   = python_students & math_students   # intersezione
either = python_students | math_students   # unione
only_python = python_students - math_students  # differenza

print("Sia Python sia Matematica:", both)
print("In almeno un corso:", either)
print("Solo Python:", only_python)`);
</script>

### Guardalo: Operazioni sugli Insiemi su un Diagramma di Venn

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Nel diagramma sotto, l'insieme A ha dog, cat, fish, e bird; l'insieme B ha cat,
    bird, snake, e hamster. Prima di cliccare qualsiasi pulsante di operazione, prevedi:
    **quali animali ti darà `A & B`?** Poi clicca e guarda quale regione
    si illumina!

<iframe src="../../sims/set-operations-venn/main.html" height="542" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Set Operations Venn](../../sims/set-operations-venn/index.md){ .md-button }

Clicca tutte e quattro le operazioni e guarda quale regione si illumina per ciascuna. Poi modifica gli insiemi — scrivi i tuoi elementi, e prova a inserire lo stesso animale due volte in un insieme per vedere il duplicato collassare. Nota che `A & B` senza elementi condivisi dà `set()`, il modo in cui Python scrive un insieme vuoto.

## Frozenset

Un **frozenset** è una versione immutabile di un insieme — non puoi aggiungere o rimuovere elementi dopo la creazione.
Questo lo rende usabile come chiave di dizionario o memorizzabile dentro un altro insieme (gli insiemi normali non possono farlo).

```python
fs = frozenset([1, 2, 3])
print(fs)        # frozenset({1, 2, 3})
# fs.add(4)      # AttributeError — un frozenset è immutabile
```

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Trova gli Interessi Condivisi"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Due amici hanno elencato i loro animali preferiti. Scrivi del codice per trovare quali animali piacciono a *entrambi*.
    Usa l'operatore di intersezione degli insiemi `&` per trovare gli elementi condivisi!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-6"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-6')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-6')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-6"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-6"></div>
  </div>
</div>
<script>
initCmLab('-6', `alice_favorites = {"cat", "dog", "rabbit", "parrot"}
bob_favorites   = {"dog", "hamster", "parrot", "fish"}

# Trova gli animali che piacciono SIA ad Alice SIA a Bob:
shared = alice_favorites  # sostituisci questa riga con l'operazione corretta

print("Piacciono a entrambi:", shared)`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Crea una tupla con sette colori dell'arcobaleno. Scomponi i primi tre in `r`, `o`, `y`.
   **Saprai che ha funzionato quando** tre nomi di colori vengono stampati senza errori.

2. Scrivi una funzione `circle_stats(radius)` che restituisce l'area e la circonferenza come una tupla.
   Usa `math.pi`. Scomponi e stampa entrambi i valori.
   **Saprai che ha funzionato quando** raggio 5 dà area ≈ 78.54 e circonferenza ≈ 31.42.

3. Converti la lista `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]` in un insieme e poi di nuovo in una lista ordinata.
   **Saprai che ha funzionato quando** vedi `[1, 2, 3, 4, 5, 6, 9]` — duplicati rimossi.

4. Prova ad aggiungere un elemento a un frozenset. Leggi attentamente il messaggio di errore.
   **Saprai che ha funzionato quando** vedi `AttributeError: 'frozenset' object has no attribute 'add'`.

5. Usa l'operatore di unione `|` per unire due insiemi di numeri e stampa il risultato ordinato.
   **Saprai che ha funzionato quando** vedi una lista combinata senza duplicati.

!!! mascot-celebration "Esperto delle Collezioni!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato le tuple per i dati fissi e gli insiemi per le collezioni di elementi unici!
    Ora hai quattro strumenti di collezione: list, tuple, set, e (il prossimo) dictionary.
    Ognuno ha il suo posto — sapere quando usare quale è una vera competenza di programmazione!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
