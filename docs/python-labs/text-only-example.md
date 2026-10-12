---
title: Esempio Skulpt Solo Testo
description: Mostra il layout del laboratorio Skulpt solo testo dove l'area di disegno è nascosta e l'editor riempie l'intera larghezza del contenuto.
---

# Esempio Skulpt Solo Testo

Questa pagina mostra il template del laboratorio Skulpt **solo testo**.
Non appare nessuna area di disegno della tartaruga — l'editor di codice e il pannello di output riempiono l'intera larghezza del contenuto.
Usa questo template per programmi che usano solo `print()` e output di testo, senza grafica turtle.

## Come Funziona

Aggiungi `class="skulpt-text-only"` al div `skulpt-lab` esterno.
Il contenitore del canvas è nascosto dal CSS, ma l'elemento `turtle-target` resta nel DOM
così `runSkulpt()` può ancora inizializzarsi senza errori.

## Esempio 1 — Istruzioni Print

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
initCmLab('', `name = "Python"
version = 3
print("Hello from", name, version)
print("No turtle needed!")
for i in range(1, 6):
    print(i, "squared =", i * i)`);
</script>

## Esempio 2 — Funzione Definita dall'Utente

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
initCmLab('-2', `def greet(first_name, last_name):
    full_name = first_name + " " + last_name
    print("Hello,", full_name + "!")

greet("Ada", "Lovelace")
greet("Grace", "Hopper")
greet("Alan", "Turing")`);
</script>

## Template HTML

Copia questo blocco e sostituisci il codice dentro il `<textarea>` per qualsiasi laboratorio solo testo:

```html
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
initCmLab('', `
# your Python code here
print("Hello!")`);
</script>
```

Per un secondo laboratorio sulla stessa pagina, usa il suffisso `-2` su tutti gli ID e `runSkulpt('-2')` / `resetSkulpt('-2')` sui bottoni (stessa convenzione dei laboratori di disegno).

## Confronto: Template del Laboratorio di Disegno

Per programmi che usano la grafica turtle, ometti la classe `skulpt-text-only` e il canvas appare normalmente:

```html
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
initCmLab('', `
import turtle
t = turtle.Turtle()
t.forward(100)`);
</script>
```
