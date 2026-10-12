# Quiz: Turtle Avanzata e Programmazione Guidata da Eventi

Verifica la tua comprensione del modello guidato da eventi, dei callback, degli eventi del mouse, degli eventi della tastiera, e dell'animazione basata su timer con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è la differenza principale tra la programmazione sequenziale e quella guidata da eventi?

<div class="upper-alpha" markdown>
1. I programmi sequenziali usano funzioni; quelli guidati da eventi no
2. I programmi sequenziali eseguono il codice dall'alto verso il basso riga per riga; quelli guidati da eventi aspettano gli eventi e rispondono con funzioni di callback
3. I programmi sequenziali sono più lenti; quelli guidati da eventi girano in parallelo
4. I programmi sequenziali usano i cicli; quelli guidati da eventi usano invece le istruzioni if/else
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. I programmi sequenziali eseguono ogni riga in ordine dall'alto verso il basso e poi finiscono. I programmi guidati da eventi avviano un ciclo di eventi che aspetta indefinitamente. Quando si verifica un evento (un clic del mouse, una pressione di tasto, o uno scatto del timer), il ciclo chiama la funzione di callback registrata. Il programma non sa in anticipo quando o quante volte scatteranno gli eventi.

    **Concept Tested:** Event-Driven Model

---

#### 2. Cos'è una funzione di callback nella programmazione guidata da eventi?

<div class="upper-alpha" markdown>
1. Una funzione che chiama sé stessa (ricorsione)
2. Una funzione che scrivi che viene passata come argomento e chiamata automaticamente quando si verifica un evento specifico
3. Una funzione che controlla se si è verificato un evento e restituisce True o False
4. Una funzione che annulla tutti gli eventi in sospeso quando viene chiamata
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un callback è una funzione che definisci e passi a una funzione di registrazione di eventi. Non la chiami tu stesso — il ciclo di eventi la chiama automaticamente quando scatta l'evento corrispondente. Per esempio, `screen.onscreenclick(my_function)` registra `my_function` come callback per i clic del mouse, e il sistema di eventi la chiama con le coordinate del clic.

    **Concept Tested:** Callback Functions

---

#### 3. Cosa fa `screen.onscreenclick(callback)`?

<div class="upper-alpha" markdown>
1. Fa muovere la turtle ovunque l'utente clicchi sullo schermo
2. Pausa il programma e aspetta che l'utente clicchi prima di continuare
3. Registra una funzione di callback da chiamare con le coordinate x, y ogni volta che l'utente clicca sul canvas
4. Rileva i clic singoli contro quelli doppi e chiama funzioni diverse
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `screen.onscreenclick(callback)` registra una funzione per gestire i clic del mouse sul canvas della turtle. Quando l'utente clicca, Python chiama automaticamente `callback(x, y)`, dove `x` e `y` sono le coordinate nello spazio delle coordinate della turtle (il centro è 0, 0). Puoi poi usare quelle coordinate per disegnare, muovere la turtle, o innescare qualsiasi altra azione.

    **Concept Tested:** onscreenclick()

---

#### 4. Cosa fa `screen.listen()`, e perché devi chiamarlo?

<div class="upper-alpha" markdown>
1. Riproduce audio attraverso gli altoparlanti del computer quando vengono premuti i tasti
2. Permette al canvas della turtle di ricevere eventi della tastiera — senza di esso, i callback della tastiera vengono ignorati
3. Inizia a registrare tutti gli eventi in un file di log per il debug
4. Fa girare la turtle nella direzione dell'ultima pressione di tasto
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `screen.listen()` dice allo screen della turtle di dirigere l'input della tastiera al sistema di eventi. Senza chiamarlo prima, i callback di `screen.onkey()` verranno registrati ma non scatteranno mai — gli eventi della tastiera vengono semplicemente ignorati. Chiama sempre `screen.listen()` dopo aver configurato i tuoi callback della tastiera e prima di `screen.mainloop()`.

    **Concept Tested:** keyboard events and listen()

---

#### 5. Quali argomenti riceve il callback da `screen.onscreenclick(callback)`?

<div class="upper-alpha" markdown>
1. Nessun argomento — controlli `screen.last_click` per ottenere la posizione
2. Le coordinate x e y del clic nello spazio delle coordinate della turtle
3. Il numero del pulsante del mouse (1 per sinistro, 2 per destro)
4. Una tupla di `(x, y, button, timestamp)` per il clic
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. La funzione di callback deve accettare due parametri: `x` e `y` — le coordinate del clic nello spazio delle coordinate della turtle dove (0,0) è il centro dello schermo. Definisci il tuo callback come `def on_click(x, y):` e il sistema di eventi li riempie automaticamente quando l'utente clicca.

    **Concept Tested:** onscreenclick()

---

#### 6. Cosa fa `screen.ontimer(callback, milliseconds)`?

<div class="upper-alpha" markdown>
1. Pausa il programma per il numero dato di millisecondi
2. Misura quanti millisecondi impiega una funzione per girare
3. Chiama la funzione di callback ripetutamente ogni N millisecondi per sempre
4. Chiama la funzione di callback una volta dopo il ritardo specificato in millisecondi
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `screen.ontimer(callback, ms)` chiama la funzione di callback una volta dopo `ms` millisecondi. Per creare un ciclo di animazione ripetuto, il callback deve ri-registrarsi chiamando di nuovo `screen.ontimer(callback, ms)` alla fine di ogni chiamata. Questo è il pattern standard per l'animazione con la turtle: aggiorna la posizione, disegna, poi pianifica la chiamata successiva.

    **Concept Tested:** ontimer()

---

#### 7. Cosa fa `screen.mainloop()` in un programma turtle guidato da eventi?

<div class="upper-alpha" markdown>
1. Esegue il ciclo principale di Python che elabora le operazioni sulle liste
2. Avvia il ciclo di eventi che mantiene aperta la finestra e distribuisce gli eventi ai callback
3. Itera su tutte le turtle registrate e le muove di un passo
4. Stampa un riepilogo di tutti gli eventi che si sono verificati durante il programma
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `screen.mainloop()` avvia il ciclo di eventi della turtle. Mantiene aperta la finestra, osserva gli eventi (clic, pressioni di tasti, timer), e chiama le funzioni di callback appropriate quando scattano gli eventi. Senza `mainloop()`, la finestra si chiuderebbe immediatamente dopo la configurazione. Questa chiamata blocca — il codice dopo di essa non gira finché la finestra non viene chiusa.

    **Concept Tested:** Event Loop

---

#### 8. Come registri un callback per la pressione del tasto freccia Su?

<div class="upper-alpha" markdown>
1. `screen.onkey("Up", go_forward)`
2. `screen.onkeypress(go_forward, 38)` (usando il codice tasto per Up)
3. `screen.onkey(go_forward, "Up")`
4. `turtle.listen_key("Up", go_forward)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La sintassi corretta è `screen.onkey(callback, key_name)` — prima la funzione di callback, poi la stringa del nome del tasto. Le stringhe dei nomi per i tasti freccia sono `"Up"`, `"Down"`, `"Left"`, `"Right"`. Per i tasti lettera, usa la lettera stessa: `"w"`. Per altri tasti: `"space"`, `"Return"`, `"Escape"`. Ricorda di chiamare `screen.listen()` perché gli eventi dei tasti funzionino.

    **Concept Tested:** onkey()

---

#### 9. Cos'è un ciclo di eventi?

<div class="upper-alpha" markdown>
1. Un ciclo for che itera su una lista di eventi una volta
2. Un ciclo ricorrente che aspetta che si verifichino gli eventi e chiama le funzioni di callback corrispondenti
3. Un tipo speciale di ciclo while che gira solo quando c'è input dell'utente
4. Il programma principale che crea oggetti evento e li distribuisce manualmente
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un ciclo di eventi è un ciclo continuo mantenuto dal framework (il `mainloop()` della turtle, in questo caso) che controlla continuamente gli eventi. Quando si verifica un evento, il ciclo identifica quale callback è stato registrato per quell'evento e lo chiama. Dopo che il callback finisce, il ciclo torna ad aspettare. Questa è la base di tutte le applicazioni interattive — giochi, GUI, e app web usano tutti cicli di eventi.

    **Concept Tested:** Event Loop

---

#### 10. Cosa fa `t.dot(20, "steelblue")`?

<div class="upper-alpha" markdown>
1. Cambia il colore della penna della turtle in steelblue
2. Disegna il contorno di un cerchio con diametro 20 in steelblue
3. Disegna un cerchio riempito (punto) con diametro 20 pixel in steelblue nella posizione attuale della turtle
4. Muove la turtle di 20 pixel verso le coordinate steelblue
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.dot(size, color)` disegna un cerchio riempito del diametro specificato nella posizione attuale della turtle. Non muove la turtle. Questo è utile nei programmi guidati da eventi dove vuoi timbrare un punto in una posizione cliccata: `t.goto(x, y)` poi `t.dot(20, "steelblue")`. Il punto viene disegnato immediatamente senza bisogno di chiamate separate a `begin_fill()` / `end_fill()`.

    **Concept Tested:** turtle.dot()

---
