---
title: Liste — Nozioni di Base
description: Scopri le liste di Python — come crearle, accedere agli elementi per indice, fare slice di sottoliste, e capire la differenza tra tipi mutabili e immutabili
generated_by: claude skill chapter-content-generator
date: 2026-06-28 12:30:00
version: 0.09
---

# Liste — Nozioni di Base

Alla fine di questa lezione sarai in grado di:

- Creare una lista Python e accedere agli elementi per indice (incluso l'indicizzazione negativa)
- Fare slice di una sottolista usando la notazione `[start:end]`
- Misurare la lunghezza di una lista con `len()` e verificare l'appartenenza con `in`
- Spiegare la differenza tra tipi **mutabili** (modificabili) e **immutabili** (non modificabili)

Le variabili contengono un valore. Ma cosa succede se hai bisogno di memorizzare un'intera collezione di valori — come i nomi di tutti i tuoi amici, o i punteggi di dieci partite?
È per questo che esistono le **liste**.

!!! mascot-welcome "Benvenuto/a al Capitolo 15!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Le liste sono uno degli strumenti più potenti in Python!
    Una volta che imparerai le liste, ti chiederai come hai fatto a programmare senza di loro.
    Costruiamo la nostra prima collezione! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Il Tipo Lista

Una **lista** è una collezione ordinata e modificabile di elementi.
La crei usando le parentesi quadre, con gli elementi separati da virgole:

```python
colors = ["red", "green", "blue", "yellow"]
scores = [95, 87, 100, 73, 88]
mixed  = ["Monty", 42, True, 3.14]   # le liste possono contenere tipi diversi
empty  = []                           # una lista vuota
```

Le liste possono contenere qualsiasi tipo di valore — stringhe, numeri, booleani, persino altre liste.

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
initCmLab('', `colors = ["red", "green", "blue", "yellow"]
scores = [95, 87, 100, 73, 88]

print("Colori:", colors)
print("Punteggi:", scores)
print("Tipo di colors:", type(colors))`);
</script>

## Indicizzazione delle Liste

Proprio come le stringhe, ogni elemento di una lista ha un **indice** che inizia da `0`.
Usa le parentesi quadre per accedere a un elemento: `my_list[index]`.

```
colors = ["red", "green", "blue", "yellow"]
           0       1        2        3
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Guarda la lista `colors` sopra. Cosa stampa `colors[2]`?
    E `colors[0]`? Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `colors = ["red", "green", "blue", "yellow"]
print("colors[0]:", colors[0])
print("colors[2]:", colors[2])
print("colors[3]:", colors[3])`);
</script>

Avevi indovinato? L'indice `0` è il primo elemento, l'indice `2` è il terzo.

Puoi anche cambiare un elemento usando il suo indice:

```python
colors[1] = "purple"   # sostituisce "green" con "purple"
```

## Indicizzazione Negativa

L'**indicizzazione negativa** ti permette di contare all'indietro dalla fine.
`-1` è l'ultimo elemento, `-2` è il penultimo, e così via.

```
colors = ["red", "green", "blue", "yellow"]
            -4     -3       -2       -1
```

Questo è particolarmente utile quando non sai quanto è lunga la lista ma vuoi sempre l'ultimo elemento.

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
initCmLab('-3', `colors = ["red", "green", "blue", "yellow"]
print("Ultimo elemento:", colors[-1])
print("Penultimo:", colors[-2])`);
</script>

## Slicing delle Liste

Lo **slicing** estrae una porzione di una lista. La sintassi è la stessa dello slicing delle stringhe: `my_list[start:end]`.
Restituisce una nuova lista contenente gli elementi da `start` fino a (ma non includendo) `end`.

```python
scores = [95, 87, 100, 73, 88]
print(scores[1:4])   # [87, 100, 73]
print(scores[:3])    # [95, 87, 100]
print(scores[2:])    # [100, 73, 88]
```

## Misurare la Lunghezza con `len()`

`len()` conta quanti elementi ci sono in una lista. Funziona anche sulle stringhe (contando i caratteri).

```python
colors = ["red", "green", "blue", "yellow"]
print(len(colors))   # 4
```

Usa `len()` quando hai bisogno del numero di elementi — per esempio, per fare un ciclo esattamente tante volte quanti sono gli elementi.

## Verificare l'Appartenenza con `in`

L'**operatore `in`** controlla se un valore è presente in una lista.
Restituisce `True` se il valore viene trovato, `False` altrimenti.

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
initCmLab('-4', `fruits = ["apple", "banana", "mango", "kiwi"]

print("apple" in fruits)     # True
print("grape" in fruits)     # False
print("mango" not in fruits) # False

if "banana" in fruits:
    print("Abbiamo le banane!")`);
</script>

`not in` è l'opposto — restituisce `True` quando l'elemento **non** è nella lista.

## Tipi Mutabili vs Immutabili

**Mutabile** significa che puoi cambiare qualcosa dopo averlo creato.
**Immutabile** significa che una volta creato, non può essere cambiato — devi crearne uno nuovo.

Le liste sono **mutabili** — puoi cambiare qualsiasi elemento, aggiungere elementi, o rimuovere elementi.

Le stringhe sono **immutabili** — una volta creata `"hello"`, non puoi cambiare il carattere `[0]` in qualcos'altro.

| Tipo | Mutabile? | Esempio |
|------|----------|---------|
| `list` | Sì | `colors[0] = "purple"` funziona |
| `str` | No | `word[0] = "P"` genera `TypeError` |
| `int`, `float` | No | `x = 5` poi `x = 6` crea un nuovo int, non cambia quello vecchio |

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
initCmLab('-5', `colors = ["red", "green", "blue"]
print("Prima:", colors)

colors[1] = "purple"   # cambia l'elemento all'indice 1
print("Dopo la modifica:", colors)

# Le stringhe sono immutabili:
word = "hello"
# word[0] = "H"   # questo causerebbe un TypeError!
new_word = "H" + word[1:]   # bisogna creare una nuova stringa
print("Nuova parola:", new_word)`);
</script>

### Guardalo: Una Lista che Cambia Forma da Sola

Le liste sono **mutabili** — cambiano forma sul posto, e ogni cambiamento rinumera gli indici. Nell'esploratore sotto, prevedi prima: **se inserisci un nuovo colore all'indice 1, cosa succede all'indice di ogni colore dopo di esso?** Poi clicca `insert(1, ...)` e guarda.

<iframe src="../../sims/list-index-explorer/main.html" height="482" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim List Index Explorer](../../sims/list-index-explorer/index.md){ .md-button }

Prova qualche click su `append()` e `pop()` e guarda entrambe le righe di indici rinumerarsi. Poi clicca **String Test** per vedere l'esatto `TypeError` che una stringa dà quando provi lo stesso cambiamento sul posto — la divisione mutabile/immutabile su un solo schermo.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Trova il Bug dell'Indice"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto dovrebbe stampare l'*ultimo* elemento della lista usando l'indicizzazione negativa.
    Ma ha un bug di uno scarto di uno. Correggi l'indice così che stampi `"kiwi"`.

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
initCmLab('-6', `fruits = ["apple", "banana", "mango", "kiwi"]

# Bug: questo stampa "mango", non "kiwi"
print("Ultimo frutto:", fruits[-2])`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Crea una lista di cinque dei tuoi film preferiti. Stampa il primo, l'ultimo (usando `-1`), e quello in mezzo.
   **Saprai che ha funzionato quando** tutti e tre si stampano senza errori.

2. Fai slice della tua lista di film per ottenere solo i primi due elementi.
   **Saprai che ha funzionato quando** vedi una lista con esattamente 2 film.

3. Usa `len()` per stampare quanti film ci sono nella tua lista.
   **Saprai che ha funzionato quando** vedi `5` (o qualsiasi numero tu abbia usato).

4. Usa `in` per controllare se il tuo film preferito è nella lista. Stampa `"Found it!"` oppure `"Not there!"`.
   **Saprai che ha funzionato quando** appare il messaggio corretto.

5. Cambia il secondo elemento della tua lista in `"The Matrix"`. Stampa l'intera lista prima e dopo.
   **Saprai che ha funzionato quando** vedi la lista cambiare.

!!! mascot-celebration "Maestro delle Liste!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai creato liste, usato l'indicizzazione e lo slicing, misurato la lunghezza, controllato l'appartenenza, e
    scoperto la differenza mutabile/immutabile! Nel prossimo capitolo imparerai come aggiungere, rimuovere,
    e ordinare gli elementi — rendendo le liste ancora più potenti. Continuiamo a programmare insieme!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
