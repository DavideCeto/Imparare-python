# Cambiare Colori con If-Else

Alla fine di questa lezione sarai in grado di:

- Scrivere un'istruzione `if/else` per fare una scelta nel tuo codice
- Usare l'operatore modulo `%` per verificare se un numero è dispari o pari
- Disegnare un quadrato con lati rossi e blu che si alternano

Cosa succede se vuoi che la tartaruga disegni alcuni lati in rosso e altri in blu — automaticamente? Un'istruzione `if/else` fa una scelta ogni volta che il ciclo gira, così ogni lato può essere di un colore diverso senza nessun lavoro extra da parte tua.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    I cicli si ripetono, ma cosa succede se hai bisogno che qualcosa sia *diverso* in alcune ripetizioni?
    È per questo che esiste `if/else`! Oggi insegnerai a Monty a scegliere i colori automaticamente.
    Programmiamo insieme!

## If-Else: Fare Scelte

Un'istruzione **if/else** esegue un blocco di codice quando una condizione è vera e un blocco diverso quando è falsa:

```python
if condition:
    # viene eseguito quando la condizione è True
else:
    # viene eseguito quando la condizione è False
```

Per alternare i colori ogni altro lato, devi sapere se il contatore del ciclo `i` è **dispari** o **pari**. L'**operatore modulo** `%` ti dà il resto dopo la divisione. `i % 2` è:
- `0` quando `i` è pari (0, 2, 4, …)
- `1` quando `i` è dispari (1, 3, 5, …)

!!! mascot-tip "Ponte Scratch"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    In Scratch hai usato il blocco **"Se … allora / altrimenti"** per fare una scelta.
    In Python, `if condition:` / `else:` fa esattamente la stessa cosa — solo scritta come testo!

## Codice di Esempio

```python
import turtle
monty = turtle.Turtle()
monty.shape('turtle')

distance = 100
angle = 90

for i in range(4):
    if i % 2 == 0:
        monty.color('red')
    else:
        monty.color('blue')
    monty.forward(distance)
    monty.right(angle)
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `i` va 0, 1, 2, 3. Quali valori rendono vero `i % 2 == 0`?
    Il primo lato sarà rosso o blu? Fai la tua previsione — poi clicca Esegui!

## Provalo Ora

Modifica il codice sotto e clicca **Esegui** per vedere il risultato direttamente su questa pagina.
Nessun account necessario — tutto gira nel tuo browser.

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
monty.shape('turtle')

distance = 100
angle = 90

for i in range(4):
    if i % 2 == 0:
        monty.color('red')
    else:
        monty.color('blue')
    monty.forward(distance)
    monty.right(angle)`);
</script>

Avevi indovinato? Quando `i` è 0 o 2, `i % 2 == 0` è vero, quindi quei lati sono rossi. Quando `i` è 1 o 3, è falso, quindi quei lati sono blu — alternandosi tutto intorno al quadrato.

## Come Funziona

Il contatore del ciclo `i` inizia a 0. A ogni ripetizione viene controllata la condizione `if`: `i % 2` è uguale a 0? Se sì, il colore diventa rosso. Se no, il colore diventa blu. Dopo il blocco `if/else`, `forward` e `right` girano sempre — sono allo stesso livello di indentazione dell'`if`, non dentro nessuno dei due rami.

## Tabella delle Spiegazioni

| Riga | Cosa fa |
|------|-------------|
| `for i in range(4):` | Si ripete 4 volte; `i` è 0, 1, 2, poi 3 |
| `if i % 2 == 0:` | Vero quando `i` è pari (0, 2); falso quando `i` è dispari (1, 3) |
| `    monty.color('red')` | Gira solo quando la condizione è vera (indentata di 8 spazi — dentro l'`if`) |
| `else:` | Cosa fare quando la condizione è falsa |
| `    monty.color('blue')` | Gira solo quando la condizione è falsa |
| `monty.forward(distance)` | Gira sempre — allo stesso livello dell'`if`, non dentro nessuno dei due rami |

!!! mascot-warning "L'Indentazione È la Chiave"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Le righe dentro il ramo `if` hanno bisogno di 8 spazi (4 per il ciclo + 4 per l'if).
    Le righe dentro il ramo `else` hanno bisogno anch'esse di 8 spazi.
    `monty.forward(distance)` ha bisogno solo di 4 (è nel ciclo ma non in nessuno dei due rami).
    Confondi questi e le righe sbagliate saranno nei blocchi sbagliati!

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Aggiungi le Righe Mancanti"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il programma sotto disegna un esagono dove ogni **terzo** lato dovrebbe essere verde
    e gli altri lati dovrebbero essere arancioni. La condizione usa `i % 3 == 0`.
    Aggiungi le **due righe di colore mancanti** — una dentro l'`if` e una dentro l'`else`!

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
monty.shape('turtle')

sides = 6
angle = 360 / sides

for i in range(sides):
    if i % 3 == 0:
        # Aggiungi qui monty.color('green')
        pass
    else:
        # Aggiungi qui monty.color('orange')
        pass
    monty.forward(80)
    monty.right(angle)`);
</script>

## Esperimenti

Prova questi cambiamenti al quadrato con colori alternati originale. Prevedi prima!

1. Scambia i colori — metti `'blue'` nel ramo `if` e `'red'` nel ramo `else`.
   **Saprai che ha funzionato quando** il primo lato è blu invece di rosso.

2. Cambia `monty.color('red')` in `monty.pensize(6)` (rimuovi la riga `color` e aggiungi `pensize`).
   **Saprai che ha funzionato quando** i lati alternati sono spessi mentre gli altri restano fini.

3. Cambia `range(4)` in `range(6)` e `angle` in `60` per disegnare un esagono.
   **Saprai che ha funzionato quando** vedi una forma a 6 lati con colori alternati.

4. Cambia la condizione da `i % 2 == 0` a `i > 1`.
   **Saprai che ha funzionato quando** i primi due lati sono di un colore e gli ultimi due di un altro.

5. Aggiungi un terzo colore: usa `elif i % 3 == 1:` tra i blocchi `if` ed `else`.
   **Saprai che ha funzionato quando** i lati scorrono attraverso tre colori.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora puoi prendere decisioni dentro un ciclo — questa è la combinazione su cui si basano la maggior parte dei programmi reali!
    Il prossimo passo: creerai le tue proprie *funzioni* per organizzare il tuo codice di disegno.
    Programmiamo insieme!
