---
title: Dizionari
description: Padroneggia i dizionari Python — coppie chiave-valore, accesso sicuro con get(), iterazione, annidamento, e dictionary comprehension
generated_by: claude skill chapter-content-generator
date: 2026-06-28 13:30:00
version: 0.09
---

# Dizionari

Alla fine di questa lezione sarai in grado di:

- Creare un dizionario e accedere ai valori per chiave
- Recuperare in sicurezza i valori con `get()` per evitare `KeyError`
- Aggiungere, aggiornare, e rimuovere voci, e iterare su chiavi, valori, e coppie
- Usare dizionari annidati e dictionary comprehension

Un dizionario mappa **chiavi** a **valori** — esattamente come un dizionario del mondo reale mappa le parole alle definizioni.
I dizionari sono una delle strutture di dati più usate in Python.

!!! mascot-welcome "Benvenuto/a al Capitolo 21!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Immagina una rubrica telefonica che puoi consultare in qualsiasi ordine, a cui puoi aggiungere nuovi contatti, e che puoi cercare in un istante.
    Questo è un dizionario Python! Costruiamone uno. Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Creare un Dizionario

Un dizionario si crea con le parentesi graffe `{}`. Ogni voce è una coppia `chiave: valore`, separata da virgole.

```python
phone_book = {
    "Alice": "555-1234",
    "Bob":   "555-5678",
    "Carol": "555-9012"
}
```

Le chiavi devono essere univoche all'interno di un dizionario.
Le chiavi sono di solito stringhe o numeri. I valori possono essere qualsiasi cosa — stringhe, numeri, liste, persino altri dizionari.

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
initCmLab('', `student = {
    "name": "Monty",
    "grade": 7,
    "score": 92.5,
    "clubs": ["coding", "chess"]
}

print("Student:", student)
print("Type:", type(student))
print("Keys:", list(student.keys()))`);
</script>

## Accedere ai Valori per Chiave

Usa le parentesi quadre con la chiave per recuperare un valore:

```python
phone_book["Alice"]   # "555-1234"
```

Se la chiave non esiste, Python genera un `KeyError` — quindi fai attenzione.

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto cerca di accedere sia a una chiave che esiste sia a una che non esiste.
    Cosa pensi che succeda quando una chiave manca? Fai la tua previsione — poi eseguilo!

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
initCmLab('-2', `grades = {"Alice": 95, "Bob": 87, "Carol": 91}

print("Alice's grade:", grades["Alice"])
print("Bob's grade:", grades["Bob"])

# Uncomment the next line to see a KeyError:
# print("Dave's grade:", grades["Dave"])`);
</script>

## Accesso Sicuro con `get()`

`dict.get(key)` restituisce il valore se la chiave esiste, oppure `None` se non esiste — nessun crash.
Puoi anche fornire un valore predefinito: `dict.get(key, default)`.

```python
grades = {"Alice": 95, "Bob": 87}
print(grades.get("Alice"))          # 95
print(grades.get("Dave"))           # None
print(grades.get("Dave", 0))        # 0 — custom default
```

Usa `get()` ogni volta che non sei sicuro se una chiave esiste.

### Guardalo: Un Mobiletto di Cassetti Etichettati

Un dizionario funziona come un mobiletto dove ogni cassetto ha la sua chiave scritta sul davanti — Python salta direttamente al cassetto giusto senza aprire gli altri. Prima di provare la ricerca sotto, prevedi: **cosa succede se scrivi `Grace` con la G maiuscola invece di `grace`?**

<iframe src="../../sims/dictionary-key-lookup/main.html" height="532" width="100%" scrolling="no"></iframe>

[Esplora il MicroSim Dictionary Key Lookup](../../sims/dictionary-key-lookup/index.md){ .md-button }

Prova una chiave mancante in entrambi i modi: con le parentesi quadre ottieni il crash `KeyError`, e con la casella **.get()** ottieni un gentile `None`. Poi controlla **compare with a list search** — la lista deve controllare cassetto dopo cassetto, mentre il dizionario fa sempre un solo salto. Questa differenza è il motivo per cui le rubriche, i glossari, e gli inventari di gioco usano tutti i dizionari.

## Aggiungere e Aggiornare Voci

Aggiungi una nuova chiave o aggiorna una esistente usando la stessa sintassi di assegnazione:

```python
grades["Dave"] = 78     # new key
grades["Alice"] = 96    # update existing key
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
initCmLab('-3', `inventory = {"apples": 10, "bananas": 5}
print("Start:", inventory)

inventory["oranges"] = 8    # add new item
inventory["apples"] = 12    # update existing
print("After update:", inventory)`);
</script>

## Rimuovere Voci

- `d.pop(key)` — rimuove la chiave e restituisce il suo valore (genera `KeyError` se mancante a meno che tu non passi un valore predefinito)
- `del d[key]` — rimuove la chiave (genera `KeyError` se mancante)

```python
grades.pop("Bob")      # removes Bob, returns 87
del grades["Carol"]    # removes Carol
```

## Chiavi, Valori, e Coppie

Tre metodi del dizionario ti danno diverse vedute dei dati:

- `d.keys()` — tutte le chiavi
- `d.values()` — tutti i valori
- `d.items()` — tutte le coppie `(chiave, valore)` come tuple

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
initCmLab('-4', `scores = {"Alice": 95, "Bob": 87, "Carol": 91}

print("Keys:", list(scores.keys()))
print("Values:", list(scores.values()))
print("Items:", list(scores.items()))`);
</script>

## Iterare su un Dizionario

Puoi fare un ciclo sulle chiavi, sui valori, o sulle coppie chiave-valore:

```python
# Loop over keys:
for name in scores:
    print(name)

# Loop over key-value pairs (most common):
for name, score in scores.items():
    print(f"{name}: {score}")
```

## Appartenenza delle Chiavi con `in`

Usa `in` per controllare se una chiave esiste senza causare un `KeyError`:

```python
if "Alice" in scores:
    print("Alice's score:", scores["Alice"])
```

## Dizionari Annidati

Un dizionario può contenere altri dizionari come valori.
Questo è perfetto per rappresentare dati strutturati — come una lista di contatti dove ogni contatto ha diversi campi.

```python
contacts = {
    "Alice": {"phone": "555-1234", "email": "alice@example.com"},
    "Bob":   {"phone": "555-5678", "email": "bob@example.com"}
}

# Access Alice's phone:
print(contacts["Alice"]["phone"])
```

## Dictionary Comprehension

Una **dictionary comprehension** costruisce un nuovo dizionario a partire da una sequenza esistente, in modo simile a una list comprehension.

Sintassi: `{espressione_chiave: espressione_valore for elemento in iterabile}`

Prima della comprehension, ecco l'equivalente nella forma lunga per rendere chiaro il pattern:

```python
# Long way:
squares = {}
for n in range(1, 6):
    squares[n] = n * n

# Comprehension — same result:
squares = {n: n * n for n in range(1, 6)}
```

## Il Pattern del Dizionario con Valore Predefinito

Un pattern comune è costruire un dizionario dove le chiavi mancanti dovrebbero partire da un valore predefinito.
L'approccio manuale usa `get()`:

```python
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
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
initCmLab('-5', `text = "the cat sat on the mat the cat"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in sorted(word_count.items()):
    print(f"  {word}: {count}")`);
</script>

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Costruisci un Registro Voti"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto crea un registro voti vuoto.
    Aggiungi tre studenti — `"Alice"` con 95, `"Bob"` con 87, e `"Carol"` con 91 —
    poi stampa il nome e il voto di ogni studente usando un ciclo `for` su `.items()`.

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
initCmLab('-6', `grade_book = {}

# Add Alice (95), Bob (87), and Carol (91):


# Print each name and grade:
for name, grade in grade_book.items():
    print(f"{name}: {grade}")`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Crea un dizionario di capitali: `{"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasília"}`.
   Stampa la capitale del Giappone.
   **Saprai che ha funzionato quando** vedi `Tokyo`.

2. Aggiungi un nuovo paese al tuo dizionario delle capitali e stampa tutte le chiavi.
   **Saprai che ha funzionato quando** il nuovo paese appare nella lista delle chiavi.

3. Usa una dictionary comprehension per creare `{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}` (cubi da 1 a 5).
   **Saprai che ha funzionato quando** vedi quelle cinque coppie chiave-valore.

4. Prova `capitals.get("Germany", "Unknown")` quando "Germany" non è nel dizionario.
   **Saprai che ha funzionato quando** vedi "Unknown" invece di un `KeyError`.

5. Conta la frequenza di ogni lettera in `"mississippi"` usando il pattern del dizionario con valore predefinito.
   **Saprai che ha funzionato quando** vedi `{"m": 1, "i": 4, "s": 4, "p": 2}`.

!!! mascot-celebration "Mago dei Dizionari!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Hai padroneggiato una delle strutture di dati più potenti di Python!
    I dizionari sono ovunque — nelle API, nei file di configurazione, nei database, e nei modelli di machine learning.
    Nel prossimo capitolo combineremo tutti e quattro i tipi di collezione con le potenti funzioni built-in di Python!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
