# Quiz: Benvenuto in Python e Skulpt

Prova la tua comprensione dei concetti base di Python, dell'ambiente Skulpt e dei tuoi primi programmi con queste domande. Fai clic su "Mostra Risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è l'interprete Python?

<div class="upper-alpha" markdown>
1. Un sito web dove accedi per scrivere codice Python
2. Un programma che legge il tuo codice Python ed esegue ogni istruzione
3. Un editor di blocchi colorati simile a Scratch
4. Una tastiera speciale per digitare comandi Python
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. L'interprete Python legge il tuo codice una riga alla volta dall'alto verso il basso ed esegue ogni istruzione. Pensa a esso come un lettore super veloce che trasforma le tue[...]

    **Concetto Testato:** Panoramica dell'Interprete Python

---

#### 2. Quale strumento è integrato direttamente in questo libro di testo così puoi eseguire Python senza aprire una nuova scheda?

<div class="upper-alpha" markdown>
1. Thonny
2. Jupyter Labs
3. Skulpt
4. Visual Studio Code
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Skulpt è una versione di Python che viene eseguita direttamente dentro la pagina web che stai leggendo. Ogni casella di codice interattiva nei primi capitoli è alimentata da Skulpt — puoi[...]

    **Concetto Testato:** Skulpt Browser Python

---

#### 3. Cosa visualizzerà il seguente codice quando viene eseguito?

```python
print("Ciao!")
print("Arrivederci!")
```

<div class="upper-alpha" markdown>
1. Ciao! Arrivederci! su una riga
2. Solo la parola Ciao!
3. Ciao! su una riga, poi Arrivederci! sulla riga successiva
4. Niente — print() ha bisogno di un numero, non di testo
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Ogni chiamata `print()` visualizza il suo testo e poi passa a una nuova riga. Quindi la prima chiamata stampa `Ciao!` e la seconda stampa `Arrivederci!` sulla riga sottostante. Python esegue[...]

    **Concetto Testato:** Funzione print()

---

#### 4. Cosa fa il simbolo `#` in un programma Python?

<div class="upper-alpha" markdown>
1. Dice a Python di stampare un numero
2. Inizia un commento che Python ignora quando esegue il programma
3. Importa una libreria nel tuo programma
4. Crea una nuova tartaruga sullo schermo
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. Il carattere `#` inizia un commento su singola riga. Tutto su quella riga dopo il `#` è una nota per i lettori umani — l'interprete Python la ignora completamente[...]

    **Concetto Testato:** Commenti su Singola Riga

---

#### 5. Quale dei seguenti causerà un errore in Python?

<div class="upper-alpha" markdown>
1. `print("ciao")`
2. `Print("ciao")`
3. `print("Ciao, mondo!")`
4. `print("123")`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. Python è sensibile alle maiuscole, quindi `Print` con una P maiuscola non è riconosciuto come la funzione print incorporata. Python risponderà con un `NameError: name 'Print' is not[...]

    **Concetto Testato:** Sensibilità alle Maiuscole

---

#### 6. Perché i programmatori aggiungono righe vuote tra sezioni di codice?

<div class="upper-alpha" markdown>
1. Python richiede righe vuote o il programma si arresterà in modo anomalo
2. Le righe vuote fanno apparire l'output su schermi separati
3. Le righe vuote dividono il codice in gruppi leggibili, rendendo più facile per gli umani leggerlo
4. Le righe vuote dicono a Python di fare una pausa per un secondo
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Python ignora completamente le righe vuote — non hanno effetto su come viene eseguito il programma. Ma i lettori umani le trovano molto utili. Le righe vuote dividono il codice in[...]

    **Concetto Testato:** Righe Vuote e Leggibilità

---

#### 7. Cosa fa l'istruzione `import`?

<div class="upper-alpha" markdown>
1. Salva il tuo file Python sul computer
2. Dice a Python di visualizzare la riga di output successiva
3. Carica un toolkit extra (libreria) così il tuo programma può usare le sue funzioni
4. Crea una nuova variabile per immagazzinare un numero
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. La parola chiave `import` dice all'interprete Python di caricare una libreria prima di eseguire il resto del tuo programma. Di per sé Python sa come fare cose base come `p[...]

    **Concetto Testato:** Istruzione import

---

#### 8. Quale è la prima riga corretta da scrivere prima di usare la grafica tartaruga?

<div class="upper-alpha" markdown>
1. `use turtle`
2. `import turtle`
3. `load turtle`
4. `start turtle`
</div>

??? question "Mostra Risposta"
    La risposta corretta è **B**. Devi scrivere `import turtle` per caricare la libreria turtle prima che il tuo programma possa usare qualsiasi comando turtle. La parola chiave è `import` — non `use`, `load`, o `star[...]

    **Concetto Testato:** import turtle

---

#### 9. Nel codice `t = turtle.Turtle()`, cosa rappresenta la variabile `t`?

<div class="upper-alpha" markdown>
1. Il numero di passi che la tartaruga farà
2. Il colore della penna della tartaruga
3. Un oggetto tartaruga a cui puoi dare comandi di movimento
4. Il titolo della finestra della tartaruga
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. `turtle.Turtle()` crea un nuovo oggetto tartaruga e lo assegna alla variabile `t`. Una volta che hai questa tartaruga, puoi darle comandi usando la notazione del punto — per es[...]

    **Concetto Testato:** import turtle

---

#### 10. Quale dei seguenti descrive meglio perché Python è un buon linguaggio da imparare dopo Scratch?

<div class="upper-alpha" markdown>
1. Python usa gli stessi blocchi colorati snap-together di Scratch
2. Python viene utilizzato solo dai principianti e non ha usi professionali
3. Python usa istruzioni basate su testo che legge quasi come l'inglese semplice ed è usato da professionisti in tutto il mondo
4. I programmi Python possono essere eseguiti solo su siti web, proprio come i progetti Scratch
</div>

??? question "Mostra Risposta"
    La risposta corretta è **C**. Python è un linguaggio basato su testo la cui sintassi legge quasi come l'inglese semplice, rendendolo un passo naturale dai blocchi visivi di Scratch. È uno dei linguaggi di programmazione più[...]

    **Concetto Testato:** Panoramica dell'Interprete Python

---
