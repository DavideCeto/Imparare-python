# Leggere l'Output e i Messaggi di Errore

Alla fine di questa lezione sarai in grado di:

- Distinguere l'output normale da un messaggio di errore solo dal colore
- Leggere cosa dice un messaggio di errore per capire dove il tuo programma è andato storto
- Usare dei checkpoint con `print()` per individuare esattamente quale riga ha causato un crash

Quando il tuo programma Python gira, due tipi di testo possono apparire nella casella di output.
L'**output normale** — qualsiasi cosa stampata con `print()` — appare in nero.
I **messaggi di errore** — prodotti quando Python trova un problema — appaiono in rosso.
Il colore rende facile vedere a colpo d'occhio se il tuo programma è terminato con successo o si è bloccato.

!!! mascot-welcome "Benvenuto a Questa Lezione!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Ogni programmatore vede messaggi di errore — anche quelli professionisti!
    Imparare a leggerli con calma è una delle abilità più utili che costruirai.
    Programmiamo insieme!

## Output Normale: Tutto Va Bene

Quando un programma gira senza nessun problema, ogni chiamata a `print()` produce una riga di testo nero nella casella di output.
Esegui il programma sotto e guarda l'output — tutto nero, niente rosso.

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
initCmLab('', `name = "Alex"
score = 42
bonus = 8
total = score + bonus

print("Giocatore:", name)
print("Punteggio:", score)
print("Bonus:", bonus)
print("Totale:", total)
print("Programma terminato correttamente!")`);
</script>

Tutte e cinque le righe si stampano in nero — il programma è girato dall'inizio alla fine senza nessun problema.

## Output di Errore: Qualcosa È Andato Storto

Ora guarda cosa succede quando Python incontra un problema a metà di un programma.
Il programma sotto stampa due righe con successo, poi cerca di usare una variabile chiamata `high_score` che non è mai stata creata.
Python non può continuare, quindi si ferma e segnala l'errore.

!!! mascot-thinking "Come Pensi che Sarà l'Output?"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Prima di cliccare Esegui, conta le chiamate a `print()` nel programma sotto.
    Quante righe di output pensi che appariranno — e di che colore sarà ciascuna?
    Fai la tua previsione, poi clicca Esegui!

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
initCmLab('-2', `name = "Alex"
score = 42

print("Giocatore:", name)
print("Punteggio:", score)

# Ops — high_score non è mai stata creata!
print("Record:", high_score)

print("Questa riga non viene mai eseguita.")`);
</script>

Avevi indovinato?
Due righe nere sono apparse per le due chiamate a `print()` andate a buon fine.
Poi un messaggio di errore rosso è apparso — Python si è fermato quando ha raggiunto la riga rotta.
L'ultima `print()` non è mai girata perché il programma si è bloccato prima di arrivarci.

## Come Leggere un NameError

Il messaggio rosso dice qualcosa come:

```
NameError: name 'high_score' is not defined on line 8
```

Ecco cosa significa ogni parte:

| Parte | Significato |
|------|---------|
| `NameError` | Il tipo di errore — Python ha trovato un nome che non riconosce |
| `'high_score'` | Il nome esatto della variabile che Python non è riuscito a trovare |
| `on line 8` | Il numero della riga dove è avvenuto il crash |

Per correggere questo errore hai due scelte:

1. **Crea la variabile prima di usarla** — aggiungi `high_score = 100` da qualche parte sopra la riga 8.
2. **Rimuovi o correggi la riga rotta** — se `high_score` non dovrebbe esserci, eliminala.

!!! mascot-tip "Le Righe Nere Sono i Tuoi Indizi"
    ![Monty with a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Quando un programma si blocca, guarda l'ultima riga nera nell'output — quella ti dice la cosa più recente che ha funzionato. L'errore è avvenuto da qualche parte tra quella riga e la `print()` successiva che ti aspettavi. Usa questo come punto di partenza quando cerchi il bug!

## Usare i Checkpoint con Print per Trovare i Bug

I programmatori professionisti spesso aggiungono chiamate temporanee a `print()` per tracciare esattamente dove un programma si ferma.
Ognuna dice "sono arrivato fin qui."
Quando vedi l'ultimo checkpoint nero e poi un errore rosso, sai che il crash è avvenuto tra quei due punti.

Ecco lo stesso programma rotto con i checkpoint aggiunti.
Nota come i checkpoint ti aiutano a individuare la riga del problema con più precisione:

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
initCmLab('-3', `print("Checkpoint 1: programma avviato")

name = "Alex"
score = 42
print("Checkpoint 2: variabili create")

total = score + 10
print("Checkpoint 3: totale calcolato:", total)

# Togli il # qui sotto per introdurre un errore e guarda dove si fermano i checkpoint:
# print("Record:", high_score)

print("Checkpoint 4: tutto fatto!")`);
</script>

Tutti e quattro i checkpoint si stampano in nero — il programma è sano.
Ora rimuovi il `#` davanti a `print("Record:", high_score)` ed eseguilo di nuovo.
Il Checkpoint 3 sarà l'ultima riga nera, e l'errore rosso apparirà subito dopo —
dicendoti che il crash è avvenuto tra il Checkpoint 3 e il Checkpoint 4.

!!! mascot-warning "Il Rosso Non Significa Fallimento — Significa Informazione"
    ![Monty warning](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Un messaggio di errore rosso non è un segno che sei scarso nella programmazione. È Python che ti dice esattamente cosa è andato storto e dove. Leggilo attentamente — contiene quasi sempre il numero di riga e il nome di qualsiasi cosa Python non sia riuscito a trovare. Il messaggio è tuo amico!

## Esperimenti

Prova questi cambiamenti. Per ciascuno, prevedi il pattern di colore dell'output prima di eseguire!

1. Nel Laboratorio 2, aggiungi `high_score = 500` su una nuova riga sopra `print("Record:", high_score)`.
   **Saprai che ha funzionato quando** tutto l'output è nero e "Record: 500" appare.

2. Nel Laboratorio 2, cambia `score = 42` in `score = "forty-two"` (una parola invece di un numero).
   Poi cambia `print("Punteggio:", score)` in `print("Punteggio + 1:", score + 1)`.
   **Saprai che ha funzionato quando** vedi un `TypeError` rosso — Python non può addizionare una parola e un numero.

3. Nel Laboratorio 3, rimuovi il `#` dalla riga rotta ed eseguila.
   Conta le righe di checkpoint nere nell'output.
   **Saprai che ha funzionato quando** riesci a identificare quale checkpoint è stato l'ultimo e spiegare perché il Checkpoint 4 non è mai apparso.

4. Nel Laboratorio 1, rinomina `total` in `final_total` nel calcolo ma lascia `print("Totale:", total)` invariato.
   **Saprai che ha funzionato quando** un `NameError` rosso per `total` appare dopo le prime tre righe nere.

!!! mascot-celebration "Sai Leggere i Messaggi di Errore!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Nero significa successo, rosso significa "guarda qui." Ora sai come leggere entrambi — e come usare i checkpoint con print per dare la caccia a un bug. Questa è vera abilità di debugging! Programmiamo insieme!
