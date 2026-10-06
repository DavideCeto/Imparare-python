# Quiz: Colori, Riempimento e Arte con la Turtle

Verifica la tua comprensione dei codici colore esadecimali, del modello di colore RGB, e del riempimento delle forme con la grafica turtle con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa rappresenta il codice colore esadecimale `#FF0000`?

<div class="upper-alpha" markdown>
1. Blu puro
2. Verde puro
3. Rosso puro
4. Bianco
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. In un codice colore esadecimale, i sei caratteri si dividono in tre coppie: la prima coppia controlla il rosso, la seconda controlla il verde, e la terza controlla il blu. `#FF0000` ha `FF` (massimo = 255) per il rosso e `00` (nessuno) per verde e blu — quindi è rosso puro. `#0000FF` sarebbe blu puro e `#00FF00` sarebbe verde puro.

    **Concept Tested:** Hex Color Codes

---

#### 2. Quale colore produce `#FFFF00`?

<div class="upper-alpha" markdown>
1. Bianco (tutti i colori al massimo)
2. Giallo (rosso + verde, senza blu)
3. Ciano (verde + blu, senza rosso)
4. Magenta (rosso + blu, senza verde)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `#FFFF00` ha rosso massimo (`FF`), verde massimo (`FF`), e nessun blu (`00`). Nel modello di colore RGB, mescolare luce rossa piena e luce verde piena produce il giallo. Questa è la stessa ragione per cui un semaforo giallo usa LED rossi e verdi. `#FFFFFF` sarebbe bianco (tutti al massimo) e `#00FFFF` sarebbe ciano.

    **Concept Tested:** Hex Color Codes

---

#### 3. Cosa usa il modello di colore RGB per creare tutti i colori?

<div class="upper-alpha" markdown>
1. Pigmenti rossi, gialli, e blu mescolati insieme
2. Combinazioni di luce rossa, verde, e blu a diverse intensità
3. Una tavolozza di 140 colori pre-nominati scelti da Python
4. Valori di tonalità, saturazione, e luminosità da 0 a 360
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il modello RGB mescola luce rossa, verde, e blu a intensità variabili (0–255 ciascuna) per creare ogni colore che il tuo schermo può mostrare. Ogni pixel su un monitor ha tre minuscole luci — rossa, verde, e blu — e la loro luminosità combinata produce il colore che vedi. Questo è diverso dal mescolare la pittura (dove rosso + verde = marrone scuro).

    **Concept Tested:** RGB Color Model

---

#### 4. Quali valori RGB producono il bianco puro?

<div class="upper-alpha" markdown>
1. Rosso=0, Verde=0, Blu=0
2. Rosso=255, Verde=0, Blu=0
3. Rosso=128, Verde=128, Blu=128
4. Rosso=255, Verde=255, Blu=255
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Il bianco è prodotto da tutti e tre i canali di colore al loro valore massimo: Rosso=255, Verde=255, Blu=255. In esadecimale, questo è `#FFFFFF`. Al contrario, il nero è tutti zeri: Rosso=0, Verde=0, Blu=0 (esadecimale `#000000`). Il grigio è prodotto da valori uguali tra 0 e 255, come (128, 128, 128).

    **Concept Tested:** RGB Color Model

---

#### 5. Cosa fa `t.fillcolor("gold")`?

<div class="upper-alpha" markdown>
1. Riempie immediatamente tutto il canvas di colore dorato
2. Cambia il colore delle linee che la tartaruga disegna in dorato
3. Imposta il colore che verrà usato per riempire la prossima forma disegnata con `begin_fill()` e `end_fill()`
4. Cambia il cursore della tartaruga stesso in un colore dorato
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.fillcolor()` imposta il colore di riempimento — il colore usato per colorare l'interno delle forme quando usi `begin_fill()` e `end_fill()`. Non riempie nulla immediatamente. È separato da `pencolor()`, che controlla il colore del contorno. Puoi impostare entrambi insieme con `t.color(pencolor, fillcolor)`.

    **Concept Tested:** begin_fill() and end_fill()

---

#### 6. Qual è l'ordine corretto delle chiamate per disegnare una forma riempita?

<div class="upper-alpha" markdown>
1. Disegna la forma, poi chiama `begin_fill()`, poi chiama `end_fill()`
2. Chiama `end_fill()`, disegna la forma, poi chiama `begin_fill()`
3. Chiama `begin_fill()`, disegna la forma, poi chiama `end_fill()`
4. Chiama `begin_fill()` ed `end_fill()` nello stesso momento prima di disegnare
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. L'ordine corretto è: (1) `t.begin_fill()` per segnalare l'inizio della regione da riempire, (2) disegna la forma, (3) `t.end_fill()` per sigillare la regione e colorarla con il colore di riempimento. Se le chiami nell'ordine sbagliato, il riempimento non fa nulla o produce risultati inaspettati. La forma dovrebbe anche essere chiusa (finire dove è iniziata) per un riempimento pulito.

    **Concept Tested:** begin_fill() and end_fill()

---

#### 7. Cosa fa `t.color("blue", "yellow")`?

<div class="upper-alpha" markdown>
1. Imposta il colore della penna a giallo e il colore di riempimento a blu
2. Imposta il colore della penna a blu e il colore di riempimento a giallo
3. Mescola blu e giallo per creare verde sia per la penna sia per il riempimento
4. Imposta il colore di sfondo a blu e il colore della penna a giallo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.color(pencolor, fillcolor)` imposta entrambi i colori contemporaneamente. Il primo argomento è il colore della penna (contorno) e il secondo è il colore di riempimento. Quindi `t.color("blue", "yellow")` disegna contorni in blu e riempie le forme di giallo. Questa è una comoda scorciatoia per chiamare `t.pencolor()` e `t.fillcolor()` separatamente.

    **Concept Tested:** Background and Pen Colors

---

#### 8. Quale valore esadecimale rappresenta il colore nero?

<div class="upper-alpha" markdown>
1. `#FFFFFF`
2. `#FF0000`
3. `#808080`
4. `#000000`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `#000000` ha zero per tutti e tre i canali di colore — niente rosso, niente verde, niente blu — il che produce il nero. `#FFFFFF` è bianco (tutti i canali al massimo). `#FF0000` è rosso. `#808080` ha tutti i canali a 128, che è grigio medio.

    **Concept Tested:** Hex Color Codes

---

#### 9. Perché una forma deve essere chiusa (finire dove è iniziata) perché `end_fill()` funzioni correttamente?

<div class="upper-alpha" markdown>
1. Python genera un errore se la forma non è chiusa prima che venga chiamato `end_fill()`
2. Una forma non chiusa lascia un vuoto nel contorno, causando una fuoriuscita del riempimento fuori dal confine previsto
3. `end_fill()` può riempire solo forme con esattamente quattro lati
4. Chiudere la forma dice a Python di aggiungere un contorno extra in un colore diverso
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Python riempie la regione delimitata dal percorso tracciato dalla tartaruga tra `begin_fill()` ed `end_fill()`. Se la forma non è chiusa — se il punto finale non è lo stesso del punto iniziale — c'è un vuoto nel confine. Python riempie comunque qualcosa, ma il riempimento potrebbe estendersi oltre o fuori dalla forma prevista in modi inaspettati.

    **Concept Tested:** begin_fill() and end_fill()

---

#### 10. Come imposti il colore di sfondo del canvas in un programma turtle?

<div class="upper-alpha" markdown>
1. `t.background("lightblue")`
2. `t.fillcolor("lightblue")`
3. `wn.bgcolor("lightblue")`
4. `turtle.fill("lightblue")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `bgcolor()` è un metodo dell'oggetto Screen (solitamente memorizzato in una variabile come `wn`). Chiami `wn.bgcolor("lightblue")` per cambiare lo sfondo del canvas. `t.fillcolor()` imposta il colore di riempimento per le forme della tartaruga, non lo sfondo. `t.background()` e `turtle.fill()` non sono metodi turtle validi.

    **Concept Tested:** Background and Pen Colors

---
