# Quiz: Disegnare con la Grafica Turtle

Verifica la tua comprensione dei comandi di grafica turtle, del controllo della penna e dell'impostazione dello schermo con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cosa crea `turtle.Screen()` in un programma turtle?

<div class="upper-alpha" markdown>
1. L'agente di disegno turtle che si muove e disegna linee
2. La finestra di disegno dove appariranno tutte le tue forme
3. Il colore dello sfondo dietro la turtle
4. Un elenco di tutti i comandi turtle disponibili
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `turtle.Screen()` crea la finestra di disegno — la tela vuota dove la tua turtle disegnerà. Pensala come il palcoscenico di uno spettacolo teatrale: lo allestisci prima che gli attori si esibiscano. La memorizzi in una variabile (comunemente `wn` per "window") così da poterle dare istruzioni come cambiare il colore di sfondo.

    **Concept Tested:** turtle.Screen() Object

---

#### 2. Quale comando muove la turtle di 100 pixel in avanti nella direzione verso cui è rivolta?

<div class="upper-alpha" markdown>
1. `t.move(100)`
2. `t.go(100)`
3. `t.forward(100)`
4. `t.walk(100)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.forward(100)` dice alla turtle di camminare in avanti di 100 pixel nella direzione verso cui è attualmente rivolta, disegnando una linea. La turtle inizia rivolta verso destra (Est). Le altre opzioni — `move()`, `go()` e `walk()` — non sono metodi turtle validi e causerebbero un `AttributeError`.

    **Concept Tested:** Turtle Movement Commands

---

#### 3. La turtle inizia sempre al centro dello schermo rivolta verso quale direzione?

<div class="upper-alpha" markdown>
1. Nord (su)
2. Sud (giù)
3. Ovest (sinistra)
4. Est (destra)
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Quando crei una nuova `turtle.Turtle()`, inizia al centro dello schermo rivolta verso Est (destra). Il primo `t.forward(100)` disegnerà quindi una linea puntata verso destra. Usi `t.right()` e `t.left()` per cambiare la direzione verso cui è rivolta prima di muoverla.

    **Concept Tested:** Turtle Movement Commands

---

#### 4. Cosa fa `t.penup()`?

<div class="upper-alpha" markdown>
1. Fa muovere la turtle più velocemente
2. Cambia il colore della penna in bianco
3. Solleva la penna così la turtle può muoversi senza disegnare una linea
4. Cancella l'ultima linea disegnata dalla turtle
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.penup()` solleva la penna virtuale dalla tela, così la turtle può spostarsi in una nuova posizione senza lasciare traccia. È così che crei spazi vuoti in un disegno. Dopo essersi spostata nella nuova posizione, chiama `t.pendown()` per riabbassare la penna così i movimenti successivi disegnano linee.

    **Concept Tested:** penup() and pendown()

---

#### 5. Uno studente esegue questo codice e non vede nulla disegnato sulla tela. Cosa è più probabile che sia sbagliato?

```python
import turtle
t = turtle.Turtle()
t.penup()
t.forward(100)
t.forward(100)
```

<div class="upper-alpha" markdown>
1. `forward()` non funziona dopo `penup()`
2. La turtle ha bisogno di uno `Screen()` prima di potersi muovere
3. Lo studente ha dimenticato di chiamare `t.pendown()` prima di disegnare
4. Devi importare turtle due volte per disegnare due linee
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Lo studente ha chiamato `t.penup()` ma non ha mai chiamato `t.pendown()`. La turtle si muove esattamente dove comandato — ma con la penna alzata, non lascia traccia sulla tela. Aggiungere `t.pendown()` prima del secondo `forward()` (o tra i due, a seconda di dove dovrebbe trovarsi lo spazio vuoto) risolverebbe il problema.

    **Concept Tested:** penup() and pendown()

---

#### 6. Quale comando imposta il colore di sfondo della finestra turtle su azzurro chiaro?

<div class="upper-alpha" markdown>
1. `t.bgcolor("lightblue")`
2. `wn.bgcolor("lightblue")`
3. `t.pencolor("lightblue")`
4. `turtle.background("lightblue")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `bgcolor()` è un metodo dell'oggetto **Screen**, non dell'oggetto Turtle. Lo chiami come `wn.bgcolor("lightblue")` dove `wn` è la variabile che contiene il tuo `turtle.Screen()`. Il metodo `pencolor()` della turtle cambia solo il colore della penna di disegno, non lo sfondo.

    **Concept Tested:** turtle.Screen() Object

---

#### 7. Cosa fa `t.pensize(5)`?

<div class="upper-alpha" markdown>
1. Fa muovere la turtle 5 volte più velocemente
2. Imposta lo spessore delle linee disegnate dalla turtle a 5 pixel
3. Cambia la forma della turtle in un cerchio di dimensione 5
4. Disegna un quadrato con lati lunghi 5 pixel
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.pensize(5)` imposta la larghezza (spessore) delle linee disegnate dalla turtle a 5 pixel. La dimensione predefinita è 1 pixel, piuttosto sottile. Aumentare lo spessore della penna a 3, 5 o 10 crea linee più marcate e visibili. Non influisce sulla velocità, sulla forma, o sulla dimensione delle forme disegnate.

    **Concept Tested:** Pen Size and Color

---

#### 8. Quale comando turtle rende invisibile il cursore della turtle senza cancellare il disegno?

<div class="upper-alpha" markdown>
1. `t.erase()`
2. `t.invisible()`
3. `t.hideturtle()`
4. `t.penup()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `t.hideturtle()` rende invisibile il cursore della turtle così non appare sul tuo disegno finito. Il disegno stesso resta completamente visibile sullo schermo. Puoi far riapparire la turtle con `t.showturtle()`. Questo è utile quando vuoi mostrare un'opera pulita senza il cursore a freccia sopra di essa.

    **Concept Tested:** Turtle Appearance

---

#### 9. Di quanti gradi dovrebbe girare la turtle per fare un angolo retto (come l'angolo di un quadrato)?

<div class="upper-alpha" markdown>
1. 45 gradi
2. 90 gradi
3. 180 gradi
4. 360 gradi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un angolo retto è di 90 gradi — un quarto di un cerchio completo di 360 gradi. Per disegnare un quadrato, ripeti `forward()` e `right(90)` quattro volte. È esattamente come la geometria che impari a scuola: gli angoli di un quadrato sono tutti di 90 gradi.

    **Concept Tested:** Turtle Movement Commands

---

#### 10. Cosa fa `t.shape("turtle")`?

<div class="upper-alpha" markdown>
1. Disegna una forma a tartaruga sulla tela nel colore attuale della turtle
2. Cambia l'aspetto del cursore della turtle da una freccia a una tartaruga a fumetti
3. Crea un secondo oggetto turtle chiamato "turtle"
4. Importa un'immagine di una tartaruga da internet
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `t.shape("turtle")` cambia l'aspetto del cursore della turtle — la piccola icona che mostra dove si trova la turtle sullo schermo. Invece della punta di freccia predefinita, mostra una tartaruga a fumetti vista dall'alto. Sono disponibili sei forme integrate: `"arrow"`, `"turtle"`, `"circle"`, `"square"`, `"triangle"` e `"classic"`.

    **Concept Tested:** Turtle Appearance

---
