# Quiz: Benvenuto in Python e Skulpt

Verifica la tua comprensione delle basi di Python, dell'ambiente Skulpt e dei tuoi primi programmi con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è l'interprete Python?

<div class="upper-alpha" markdown>
1. Un sito web dove accedi per scrivere codice Python
2. Un programma che legge il tuo codice Python ed esegue ogni istruzione
3. Un editor a blocchi colorati simile a Scratch
4. Una tastiera speciale per digitare comandi Python
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. L'interprete Python legge il tuo codice una riga alla volta, dall'alto verso il basso, ed esegue ogni istruzione. Pensalo come un lettore velocissimo che trasforma le tue parole in azioni — in modo simile a come cliccare sulla bandierina verde in Scratch avvia l'esecuzione del tuo programma.

    **Concept Tested:** Python Interpreter Overview

---

#### 2. Quale strumento è integrato direttamente in questo libro di testo, così puoi eseguire Python senza aprire una nuova scheda?

<div class="upper-alpha" markdown>
1. Thonny
2. Jupyter Labs
3. Skulpt
4. Visual Studio Code
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Skulpt è una versione di Python che funziona direttamente dentro la pagina web che stai leggendo. Ogni finestra di codice interattiva nei primi capitoli è alimentata da Skulpt — clicchi su Run e il codice viene eseguito proprio sulla pagina, senza bisogno di account o installazioni.

    **Concept Tested:** Skulpt Browser Python

---

#### 3. Cosa mostrerà il seguente codice quando viene eseguito?

```python
print("Ciao!")
print("Ciao ciao!")
```

<div class="upper-alpha" markdown>
1. Ciao! Ciao ciao! su una sola riga
2. Solo la parola Ciao!
3. Ciao! su una riga, poi Ciao ciao! sulla riga successiva
4. Niente — print() ha bisogno di un numero, non di testo
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Ogni chiamata a `print()` mostra il suo testo e poi passa a una nuova riga. Quindi la prima chiamata stampa `Ciao!` e la seconda stampa `Ciao ciao!` sulla riga sottostante. Python esegue ogni istruzione in ordine dall'alto verso il basso, proprio come Scratch esegue i blocchi in uno script.

    **Concept Tested:** print() Function

---

#### 4. Cosa fa il simbolo `#` in un programma Python?

<div class="upper-alpha" markdown>
1. Dice a Python di stampare un numero
2. Avvia un commento che Python ignora durante l'esecuzione del programma
3. Importa una libreria nel tuo programma
4. Crea una nuova tartaruga sullo schermo
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il carattere `#` avvia un commento su una riga. Tutto ciò che si trova su quella riga dopo il `#` è una nota per i lettori umani — l'interprete Python la ignora completamente quando esegue il programma. I commenti aiutano a spiegare cosa fa il tuo codice senza cambiare come funziona.

    **Concept Tested:** Single-Line Comments

---

#### 5. Quale delle seguenti istruzioni causerà un errore in Python?

<div class="upper-alpha" markdown>
1. `print("ciao")`
2. `Print("ciao")`
3. `print("Ciao, mondo!")`
4. `print("123")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Python distingue tra maiuscole e minuscole, quindi `Print` con la P maiuscola non viene riconosciuto come la funzione print integrata. Python risponderà con `NameError: name 'Print' is not defined`. Usa sempre `print()` minuscolo.

    **Concept Tested:** Case Sensitivity

---

#### 6. Perché i programmatori aggiungono righe vuote tra le sezioni di codice?

<div class="upper-alpha" markdown>
1. Python richiede righe vuote, altrimenti il programma va in crash
2. Le righe vuote fanno apparire l'output su schermate separate
3. Le righe vuote dividono il codice in gruppi leggibili, rendendolo più facile da leggere per gli esseri umani
4. Le righe vuote dicono a Python di fare una pausa di un secondo
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python ignora completamente le righe vuote — non hanno alcun effetto su come viene eseguito il programma. Ma per i lettori umani sono molto utili. Le righe vuote dividono il codice in gruppi logici, proprio come gli a capo dividono una storia in scene. È una buona abitudine aggiungerle tra sezioni che svolgono compiti diversi.

    **Concept Tested:** Blank Lines and Readability

---

#### 7. Cosa fa l'istruzione `import`?

<div class="upper-alpha" markdown>
1. Salva il tuo file Python sul tuo computer
2. Dice a Python di mostrare la riga di output successiva
3. Carica un set di strumenti extra (una libreria) così il tuo programma può usarne le funzionalità
4. Crea una nuova variabile per memorizzare un numero
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La parola chiave `import` dice all'interprete Python di caricare una libreria prima di eseguire il resto del tuo programma. Da solo Python sa fare cose di base come `print()`, ma strumenti come `turtle`, `random` e `math` devono prima essere importati. Le istruzioni import vanno sempre proprio in cima al tuo programma.

    **Concept Tested:** import Statement

---

#### 8. Qual è la prima riga corretta da scrivere prima di usare la grafica turtle?

<div class="upper-alpha" markdown>
1. `use turtle`
2. `import turtle`
3. `load turtle`
4. `start turtle`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Devi scrivere `import turtle` per caricare la libreria turtle prima che il tuo programma possa usare qualsiasi comando turtle. La parola chiave è `import` — non `use`, `load` o `start`. Questa riga deve comparire in cima al tuo programma, prima di qualsiasi comando turtle.

    **Concept Tested:** import turtle

---

#### 9. Nel codice `t = turtle.Turtle()`, cosa rappresenta la variabile `t`?

<div class="upper-alpha" markdown>
1. Il numero di passi che la tartaruga farà
2. Il colore della penna della tartaruga
3. Un oggetto tartaruga a cui puoi dare comandi di movimento
4. Il titolo della finestra della tartaruga
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `turtle.Turtle()` crea un nuovo oggetto tartaruga e lo assegna alla variabile `t`. Una volta che hai questa tartaruga, puoi darle comandi usando la notazione col punto — per esempio, `t.forward(100)` dice alla tartaruga `t` di muoversi in avanti di 100 passi disegnando una linea.

    **Concept Tested:** import turtle

---

#### 10. Quale delle seguenti frasi descrive meglio perché Python è un buon linguaggio da imparare dopo Scratch?

<div class="upper-alpha" markdown>
1. Python usa gli stessi blocchi colorati a incastro di Scratch
2. Python è usato solo dai principianti e non ha usi professionali
3. Python usa istruzioni testuali che si leggono quasi come l'inglese comune ed è usato da professionisti in tutto il mondo
4. I programmi Python possono funzionare solo sui siti web, proprio come i progetti Scratch
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python è un linguaggio testuale la cui sintassi si legge quasi come l'inglese comune, il che lo rende un passo naturale dopo i blocchi visuali di Scratch. È uno dei linguaggi di programmazione più popolari al mondo, usato da professionisti in aziende come YouTube, NASA e nella ricerca sull'intelligenza artificiale.

    **Concept Tested:** Python Interpreter Overview

---
