# Quiz: Cicli While e Animazione

Verifica la tua comprensione dei cicli while, break, continue, e dei concetti di animazione con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Qual è la differenza principale tra un ciclo `for` e un ciclo `while`?

<div class="upper-alpha" markdown>
1. Un ciclo `for` può solo disegnare forme con la tartaruga; un ciclo `while` è per stampare testo
2. Un ciclo `for` usa un contatore; un ciclo `while` non può contare
3. Un ciclo `for` si ripete un numero conosciuto di volte; un ciclo `while` si ripete finché una condizione è True
4. Un ciclo `for` gira più velocemente di un ciclo `while`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un ciclo `for` è l'ideale quando sai esattamente quante volte ripetere — come `for i in range(10)`. Un ciclo `while` è l'ideale quando vuoi continuare a ripetere finché una certa condizione resta `True`, senza sapere in anticipo quante iterazioni saranno. Entrambi possono compiere compiti simili, ma ognuno ha situazioni in cui si adatta più naturalmente.

    **Concept Tested:** while Loop

---

#### 2. Cosa stamperà questo programma?

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Done!")
```

<div class="upper-alpha" markdown>
1. `3 2 1 0` poi `Done!`
2. Solo `Done!`
3. `3 2 1` poi `Done!`
4. `3` poi `Done!`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il ciclo parte con count = 3 (True), stampa 3, count diventa 2 (True), stampa 2, count diventa 1 (True), stampa 1, count diventa 0. Ora `0 > 0` è `False`, quindi il ciclo finisce senza stampare 0. Poi si stampa `"Done!"`. Il numero 0 non viene mai stampato perché la condizione viene controllata prima di ogni giro.

    **Concept Tested:** while Loop

---

#### 3. Cosa causa un ciclo infinito in un ciclo `while`?

<div class="upper-alpha" markdown>
1. Usare `break` dentro il corpo del ciclo
2. La condizione del ciclo non diventa mai `False` perché la variabile non viene mai aggiornata
3. Scrivere il corpo del ciclo con più di due righe di codice
4. Far partire il contatore del ciclo da un numero maggiore di 10
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un ciclo infinito si verifica quando la condizione in un ciclo `while` non diventa mai `False` — di solito perché il programmatore ha dimenticato di aggiornare la variabile da cui dipende la condizione. Per esempio, se scrivi `while count > 0:` ma dimentichi `count -= 1` dentro il ciclo, `count` resta lo stesso per sempre e il programma non si ferma mai.

    **Concept Tested:** Infinite Loops to Avoid

---

#### 4. Cosa fa l'istruzione `break` dentro un ciclo?

<div class="upper-alpha" markdown>
1. Pausa il ciclo per un secondo, poi continua
2. Salta l'iterazione attuale e passa a quella successiva
3. Esce dal ciclo immediatamente, anche se la condizione è ancora True
4. Riporta il contatore del ciclo al suo valore iniziale
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `break` esce dal ciclo completamente e immediatamente, saltando alla prima riga di codice dopo il ciclo. Non aspetta che la condizione diventi `False` — semplicemente si ferma. Questo è utile quando succede qualcosa dentro il ciclo che significa che non hai più bisogno di continuare, come trovare la risposta che stavi cercando.

    **Concept Tested:** break Statement

---

#### 5. Cosa fa l'istruzione `continue` dentro un ciclo?

<div class="upper-alpha" markdown>
1. Esce dal ciclo immediatamente, proprio come `break`
2. Salta il resto dell'iterazione attuale e torna a controllare la condizione
3. Stampa una riga vuota e passa all'iterazione successiva del ciclo
4. Converte automaticamente il ciclo `while` in un ciclo `for`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `continue` salta le righe rimanenti nel giro attuale del ciclo e torna direttamente a controllare la condizione. Il ciclo non finisce — salta solo quell'iterazione. Questo è utile per saltare valori specifici: per esempio, usando `continue` quando un numero è pari così che vengano elaborati solo i numeri dispari.

    **Concept Tested:** continue Statement

---

#### 6. Quando viene eseguita la clausola `else` su un ciclo `while`?

<div class="upper-alpha" markdown>
1. Ogni volta che gira il corpo del ciclo
2. Quando la condizione del ciclo è `True` al primo controllo
3. Solo quando il ciclo finisce naturalmente perché la condizione è diventata `False`
4. Solo quando il ciclo finisce perché è stata eseguita un'istruzione `break`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. La clausola `else` su un ciclo `while` gira quando il ciclo finisce normalmente — cioè, quando la condizione diventa `False` da sola. Se il ciclo finisce a causa di un'istruzione `break`, il blocco `else` viene **saltato**. Questo lo rende utile per lo schema "abbiamo trovato quello che stavamo cercando?" nel codice di ricerca.

    **Concept Tested:** else Clause on Loops

---

#### 7. In un ciclo annidato, quante volte gira il corpo del ciclo interno se il ciclo esterno gira 3 volte e il ciclo interno gira 4 volte per ogni giro esterno?

<div class="upper-alpha" markdown>
1. 7 volte (3 + 4)
2. 12 volte (3 × 4)
3. 4 volte
4. 3 volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In un ciclo annidato, il ciclo interno gira completamente per ogni singolo giro del ciclo esterno. Se il ciclo esterno fa 3 giri e il ciclo interno fa 4 giri per ogni giro esterno, il corpo del ciclo interno gira 3 × 4 = 12 volte in totale. I cicli annidati sono potenti per disegnare griglie, tabelle e pattern 2D.

    **Concept Tested:** Nested Loops

---

#### 8. Quale modulo useresti per pausare un programma Python per 2 secondi?

<div class="upper-alpha" markdown>
1. `turtle`
2. `math`
3. `time`
4. `random`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Il modulo `time` contiene funzioni per lavorare con il tempo, incluso `time.sleep(seconds)` che pausa il programma per il numero di secondi specificato. Lo importi con `import time`, poi chiami `time.sleep(2)` per pausare per 2 secondi. Questo è utile per creare timer di conto alla rovescia e controllare la velocità dell'animazione.

    **Concept Tested:** time Module Overview

---

#### 9. Cosa fa `time.sleep(0.5)` in un programma Python?

<div class="upper-alpha" markdown>
1. Esegue il programma 0,5 volte e poi si ferma
2. Imposta l'orologio del programma a 0:05
3. Ripete la riga precedente mezza volta
4. Pausa il programma per mezzo secondo prima di continuare
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `time.sleep(seconds)` pausa il programma per il numero di secondi indicato. Puoi passare valori decimali: `time.sleep(0.5)` pausa per mezzo secondo. Dopo la pausa, il programma continua normalmente. In un ciclo, `time.sleep()` crea un ritardo tra ogni passo — la base dell'animazione semplice.

    **Concept Tested:** time.sleep()

---

#### 10. Perché un ciclo `while` è particolarmente utile per creare animazioni con la tartaruga?

<div class="upper-alpha" markdown>
1. I cicli `while` disegnano il doppio più velocemente dei cicli `for` con la tartaruga
2. La libreria turtle funziona solo dentro i cicli `while`
3. I cicli `while` possono continuare a eseguire un'animazione fotogramma per fotogramma finché non si raggiunge una condizione di arresto
4. I cicli `while` aggiungono automaticamente colori ai disegni con la tartaruga
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Un ciclo `while` è perfetto per l'animazione perché può continuare a girare indefinitamente — o finché non si raggiunge una specifica condizione di arresto — senza bisogno di sapere in anticipo quanti fotogrammi ci saranno. Ogni giro del ciclo può muovere leggermente la tartaruga, creando l'illusione di movimento. Combinato con `time.sleep()`, controlli quanto velocemente gira l'animazione.

    **Concept Tested:** Animation with Turtle Loops

---
