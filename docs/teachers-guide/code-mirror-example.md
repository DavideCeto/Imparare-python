---
hide:
  toc
---
# Editor Python CodeMirror

I laboratori Skulpt standard usano una semplice `<textarea>` per l'inserimento
del codice — volutamente minimale così che i capitoli 1–18 restino semplici
da distribuire e condividere.
Per programmi più lunghi (20+ righe), un vero editor di codice con **numeri di
riga** ed **evidenziazione della sintassi** fa una differenza significativa:
quando Skulpt segnala `NameError on line 27`, gli studenti possono saltare
direttamente al problema invece di contare le righe manualmente.

Questa pagina è una prova di concetto autonoma.
Carica **CodeMirror 5** da un CDN e lo collega a Skulpt — tutto dentro questo
singolo file Markdown, senza modifiche al CSS condiviso, al JavaScript, o a
`mkdocs.yml`.

## Cosa Aggiunge CodeMirror

| Funzionalità | `textarea` semplice | CodeMirror |
|---|---|---|
| Numeri di riga | no | sì |
| Evidenziazione della sintassi | no | sì |
| Auto-indentazione su Invio | no | sì |
| Tab → 4 spazi | manuale | integrato |
| Corrispondenza delle parentesi | no | sì |

## Demo dal Vivo — Albero Frattale

Il programma qui sotto è di 37 righe.
Senza numeri di riga, `NameError on line 27` manda gli studenti a scandagliare.
Con i numeri di riga, trovano il problema immediatamente.

Clicca **Run** per far crescere l'albero, poi prova a modificare `depth`
(attualmente `6`) o la lunghezza del tronco (attualmente `80`).

<!-- Skulpt runtime (same CDN used by all Skulpt labs in this textbook) -->
<script src="https://skulpt.org/js/skulpt.min.js" type="text/javascript"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js" type="text/javascript"></script>

<!-- CodeMirror 5: editor core, Python language mode, Dracula dark theme -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/dracula.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>

<style>
  #cm-lab { margin: 1rem 0; }
  #cm-layout {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    flex-wrap: wrap;
  }
  #cm-editor-wrap { flex: 1; min-width: 300px; }
  .CodeMirror {
    height: auto;
    min-height: 420px;
    font-size: 14px;
    border-radius: 4px;
    line-height: 1.6;
  }
  .CodeMirror-scroll { min-height: 420px; }
  #cm-turtle {
    width: 400px;
    height: 400px;
    border: 1px solid #555;
    border-radius: 4px;
    flex-shrink: 0;
    background: #fff;
  }
  #cm-controls { margin: 8px 0; display: flex; gap: 8px; }
  #cm-controls button {
    padding: 6px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 600;
  }
  #cm-run-btn   { background: #4CAF50; color: white; }
  #cm-run-btn:hover { background: #45a049; }
  #cm-reset-btn { background: #888; color: white; }
  #cm-reset-btn:hover { background: #666; }
  #cm-output {
    font-family: monospace;
    font-size: 13px;
    min-height: 24px;
    padding: 4px 8px;
    background: #282a36;
    color: #f8f8f2;
    border-radius: 4px;
    margin-top: 8px;
    white-space: pre-wrap;
  }
  .cm-err { color: #ff5555; }
</style>

<div id="cm-lab">
  <div id="cm-layout">
    <div id="cm-editor-wrap">
      <div id="cm-editor"></div>
      <div id="cm-controls">
        <button id="cm-run-btn"   onclick="runCmLab()">&#9654; Run</button>
        <button id="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
      </div>
      <div id="cm-output"></div>
    </div>
    <div id="cm-turtle"></div>
  </div>
</div>

<script>
// Store the original code as an array of strings (avoids backtick escaping issues).
var _cmLines = [
  'import turtle',
  '',
  '# Create the drawing turtle',
  't = turtle.Turtle()',
  't.speed(0)',
  't.hideturtle()',
  't.left(90)  # Point upward',
  '',
  'def tree(branch_len, depth):',
  '    """Draw one branch of a fractal tree, then recurse."""',
  '    if branch_len < 5:',
  '        return  # Base case — too short to continue',
  '',
  '    # Choose color and thickness based on depth',
  '    if depth <= 2:',
  '        t.pencolor("lime green")',
  '        t.pensize(1)',
  '    elif depth <= 4:',
  '        t.pencolor("saddlebrown")',
  '        t.pensize(2)',
  '    else:',
  '        t.pencolor("saddlebrown")',
  '        t.pensize(5)',
  '',
  '    t.forward(branch_len)       # Draw this branch segment',
  '',
  '    t.left(25)',
  '    tree(branch_len * 0.7, depth - 1)  # Left sub-branch',
  '',
  '    t.right(50)',
  '    tree(branch_len * 0.7, depth - 1)  # Right sub-branch',
  '',
  '    t.left(25)',
  '    t.backward(branch_len)      # Return to fork point',
  '',
  '# Grow the tree! Try changing 80 (trunk length) or 6 (depth)',
  'tree(80, 6)'
];
var _cmOriginalCode = _cmLines.join('\n');

var cmEditor = CodeMirror(document.getElementById('cm-editor'), {
  value:          _cmOriginalCode,
  mode:           'python',
  theme:          'dracula',
  lineNumbers:    true,
  indentUnit:     4,
  tabSize:        4,
  indentWithTabs: false,
  lineWrapping:   false,
  extraKeys: {
    Tab: function(cm) { cm.replaceSelection('    ', 'end'); }
  }
});

function _esc(text) {
  return text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function runCmLab() {
  var code   = cmEditor.getValue();
  var output = document.getElementById('cm-output');
  var target = document.getElementById('cm-turtle');

  target.innerHTML = '';
  output.innerHTML = '';

  Sk.configure({
    output: function(text) { output.innerHTML += _esc(text); },
    read: function(x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles['files'][x] === undefined)
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles['files'][x];
    },
    __future__:    Sk.python3,
    killableWhile: true,
    killableFor:   true,
  });

  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'cm-turtle';
  Sk.TurtleGraphics.width  = 400;
  Sk.TurtleGraphics.height = 400;

  Sk.misceval.asyncToPromise(function() {
    return Sk.importMainWithBody('<stdin>', false, code, true);
  }).catch(function(err) {
    output.innerHTML += '<span class="cm-err">' + _esc(err.toString()) + '</span>';
  });
}

function resetCmLab() {
  cmEditor.setValue(_cmOriginalCode);
  document.getElementById('cm-turtle').innerHTML = '';
  document.getElementById('cm-output').innerHTML = '';
}
</script>

---

## Copiare Questo nella Tua Pagina

Incolla questi cinque blocchi in qualsiasi pagina Markdown per ottenere un
laboratorio CodeMirror + Skulpt.
Sostituisci il codice Python in `_cmLines` con il tuo programma.

Questa pagina è una prova di concetto autonoma: `runCmLab` e `resetCmLab`
sono definiti **in linea** e leggono da `cmEditor.getValue()`. I laboratori
di produzione in tutto il manuale usano invece il file condiviso
`js/codemirror-lab.js`, che gestisce più laboratori per pagina tramite un
registro di suffissi (`initCmLab`) e aggiunge un pulsante Run ⇄ Pause:
mentre un programma è in esecuzione, cliccare **Pause** blocca il disegno
della turtle (utile per discussioni o screenshot) e **Resume** lo
continua. Se il codice viene modificato durante la pausa, il pulsante
cambia in **Run New Code** e avvia un'esecuzione nuova con il nuovo codice
invece di riprendere quella vecchia. **Reset** ferma un programma in
esecuzione. Vedi [Il Pulsante Run ⇄ Pause](run-pause-buttons.md) per la
tabella completa dei comportamenti e la motivazione del design. La versione
minimale in linea qui sotto non include la funzionalità di pausa.

```html
<!-- 1. Skulpt runtime -->
<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>

<!-- 2. CodeMirror 5 (editor core + Python mode + Dracula theme) -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/theme/dracula.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>

<!-- 3. Layout styles -->
<style>
  #cm-lab { margin: 1rem 0; }
  #cm-layout { display: flex; gap: 12px; align-items: flex-start; flex-wrap: wrap; }
  #cm-editor-wrap { flex: 1; min-width: 300px; }
  .CodeMirror { height: auto; min-height: 420px; font-size: 14px; border-radius: 4px; line-height: 1.6; }
  .CodeMirror-scroll { min-height: 420px; }
  #cm-turtle { width: 400px; height: 400px; border: 1px solid #555; border-radius: 4px; flex-shrink: 0; }
  #cm-controls { margin: 8px 0; display: flex; gap: 8px; }
  #cm-controls button { padding: 6px 20px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; font-weight: 600; }
  #cm-run-btn   { background: #4CAF50; color: white; }
  #cm-run-btn:hover { background: #45a049; }
  #cm-reset-btn { background: #888; color: white; }
  #cm-reset-btn:hover { background: #666; }
  #cm-output { font-family: monospace; font-size: 13px; padding: 4px 8px; background: #282a36;
               color: #f8f8f2; border-radius: 4px; margin-top: 8px; white-space: pre-wrap; }
  .cm-err { color: #ff5555; }
</style>

<!-- 4. Editor structure -->
<div id="cm-lab">
  <div id="cm-layout">
    <div id="cm-editor-wrap">
      <div id="cm-editor"></div>
      <div id="cm-controls">
        <button id="cm-run-btn"   onclick="runCmLab()">&#9654; Run</button>
        <button id="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
      </div>
      <div id="cm-output"></div>
    </div>
    <div id="cm-turtle"></div>
  </div>
</div>

<!-- 5. Editor initialisation and run/reset logic -->
<script>
var _cmLines = [
  'import turtle',
  '# YOUR PYTHON PROGRAM HERE',
  't = turtle.Turtle()',
  't.forward(100)'
];
var _cmOriginalCode = _cmLines.join('\n');

var cmEditor = CodeMirror(document.getElementById('cm-editor'), {
  value:          _cmOriginalCode,
  mode:           'python',
  theme:          'dracula',
  lineNumbers:    true,
  indentUnit:     4,
  tabSize:        4,
  indentWithTabs: false,
  extraKeys: { Tab: function(cm) { cm.replaceSelection('    ', 'end'); } }
});

function _esc(t) {
  return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function runCmLab() {
  var code   = cmEditor.getValue();
  var output = document.getElementById('cm-output');
  var target = document.getElementById('cm-turtle');
  target.innerHTML = '';
  output.innerHTML = '';

  Sk.configure({
    output: function(text) { output.innerHTML += _esc(text); },
    read: function(x) {
      if (Sk.builtinFiles === undefined || Sk.builtinFiles['files'][x] === undefined)
        throw "File not found: '" + x + "'";
      return Sk.builtinFiles['files'][x];
    },
    __future__: Sk.python3,
    killableWhile: true,
    killableFor:   true,
  });

  (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'cm-turtle';
  Sk.TurtleGraphics.width  = 400;
  Sk.TurtleGraphics.height = 400;

  Sk.misceval.asyncToPromise(function() {
    return Sk.importMainWithBody('<stdin>', false, code, true);
  }).catch(function(err) {
    output.innerHTML += '<span class="cm-err">' + _esc(err.toString()) + '</span>';
  });
}

function resetCmLab() {
  cmEditor.setValue(_cmOriginalCode);
  document.getElementById('cm-turtle').innerHTML = '';
  document.getElementById('cm-output').innerHTML = '';
}
</script>
```

---

## Quando Usare CodeMirror invece della Textarea Semplice

| Usa la `textarea` semplice quando… | Usa CodeMirror quando… |
|---|---|
| I programmi sono di 5–15 righe | I programmi sono di 20+ righe |
| Il focus è su un singolo concetto nuovo | Più funzioni o cicli annidati |
| Stai scrivendo un laboratorio standard del manuale | Gli insegnanti proietteranno e navigheranno il codice |
| Conta la semplicità nello scrivere la pagina | Gli studenti leggeranno messaggi di errore con numeri di riga |

I laboratori Skulpt standard nei capitoli 1–18 restano con `<textarea>` —
intenzionalmente. CodeMirror vale la configurazione extra per dimostrazioni
più lunghe dove navigare verso un numero di riga specifico fa parte della
lezione.
