# Quiz: Funzioni con Parametri e Scope

Verifica la tua comprensione dei parametri predefiniti, degli argomenti keyword, dello scope, e delle funzioni pure con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è un valore predefinito di un parametro in una funzione Python?

<div class="upper-alpha" markdown>
1. Il valore che un parametro contiene quando la funzione restituisce `None`
2. Un valore che la funzione usa automaticamente quando chi la chiama non fornisce un argomento per quel parametro
3. Il primo argomento passato a una funzione quando viene chiamata
4. Un parametro che è obbligatorio e deve sempre essere fornito da chi chiama
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un valore predefinito di un parametro è definito nella riga `def` usando `parametro=predefinito`. Quando qualcuno chiama la funzione senza fornire quell'argomento, Python usa automaticamente il valore predefinito. Quando invece fornisce un valore, quel valore sovrascrive il predefinito. Questo rende le funzioni flessibili — funzionano con o senza certi argomenti.

    **Concept Tested:** Default Parameter Values

---

#### 2. Quale chiamata di funzione usa un argomento keyword?

<div class="upper-alpha" markdown>
1. `draw_polygon(6, 80, "red")`
2. `draw_polygon(sides=6, color="red")`
3. `draw_polygon("red", 6, 80)`
4. `draw_polygon(6)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Un argomento keyword usa il nome del parametro seguito da `=` e un valore nella chiamata di funzione: `sides=6` e `color="red"`. Gli argomenti keyword possono essere forniti in qualsiasi ordine perché Python li associa per nome, non per posizione. L'opzione A usa argomenti posizionali, che devono essere nell'ordine corretto.

    **Concept Tested:** Keyword Arguments

---

#### 3. Cos'è lo scope di una variabile?

<div class="upper-alpha" markdown>
1. Quanti caratteri lungo è il nome della variabile
2. Quanto è grande il valore memorizzato nella variabile
3. Quali parti del programma possono vedere e usare la variabile
4. Quante volte la variabile viene usata nel programma
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Lo scope descrive dove nel tuo programma una variabile è visibile e accessibile. Una variabile creata dentro una funzione ha scope **locale** — esiste solo mentre quella funzione gira. Una variabile creata fuori da tutte le funzioni ha scope **globale** — è visibile in tutto il programma.

    **Concept Tested:** Local Scope and Global Scope

---

#### 4. Cosa succede quando provi a usare una variabile locale fuori dalla funzione che l'ha creata?

<div class="upper-alpha" markdown>
1. La variabile mantiene il suo ultimo valore e può essere usata ovunque
2. Python stampa il valore automaticamente senza bisogno di `print()`
3. Python genera un `NameError` perché la variabile non esiste fuori dalla funzione
4. La variabile diventa una variabile globale dopo che la funzione finisce
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una variabile locale esiste solo mentre la sua funzione è in esecuzione. Quando la funzione finisce, la variabile locale scompare. Provare a usarla dopo causa un `NameError: name 'variable' is not defined`. Questo è voluto — le variabili locali prevengono conflitti di nomi tra funzioni.

    **Concept Tested:** Local Scope and Global Scope

---

#### 5. Cosa dice a Python la parola chiave `global` dentro una funzione?

<div class="upper-alpha" markdown>
1. Crea una variabile locale completamente nuova con quel nome dentro questa funzione
2. Elimina la variabile globale quando la funzione finisce
3. Usa la variabile che esiste nello scope globale (esterno), non crearne una locale nuova
4. Stampa il valore della variabile nell'output quando la funzione viene chiamata
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Senza `global`, se assegni un valore a una variabile dentro una funzione, Python crea una nuova variabile locale che oscura quella globale. Scrivere `global score` dentro una funzione dice a Python "Intendo lo `score` che vive fuori, non uno locale nuovo" — quindi le assegnazioni a `score` dentro quella funzione cambiano davvero la variabile globale.

    **Concept Tested:** global Keyword

---

#### 6. Quale output produce questo programma?

```python
speed = 10

def reset():
    speed = 0
    print("Inside:", speed)

reset()
print("Outside:", speed)
```

<div class="upper-alpha" markdown>
1. `Inside: 0` poi `Outside: 0`
2. `Inside: 10` poi `Outside: 10`
3. `Inside: 0` poi `Outside: 10`
4. Un errore perché `speed` è definita due volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Dentro `reset()`, `speed = 0` crea una **nuova variabile locale** chiamata `speed` — NON cambia lo `speed` globale. Quindi dentro la funzione, `speed` è 0. Ma fuori, lo `speed` globale è ancora 10. Questo è un conflitto di nomi comune che causa bug confusi; usare `global speed` dentro la funzione lo risolverebbe se davvero volessi cambiare il valore globale.

    **Concept Tested:** Local Scope and Global Scope

---

#### 7. Per convenzione, come scrivono i programmatori Python il nome di una costante?

<div class="upper-alpha" markdown>
1. Iniziando con una lettera minuscola, come `maxSpeed`
2. Circondato da doppi underscore, come `__max_speed__`
3. In MAIUSCOLO con underscore, come `MAX_SPEED`
4. Iniziando con una lettera maiuscola, come `MaxSpeed`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. I programmatori Python usano il MAIUSCOLO con underscore per segnalare che una variabile è una costante — un valore che non dovrebbe mai cambiare dopo essere stato impostato. Esempi: `MAX_SPEED = 10`, `CANVAS_WIDTH = 400`. Python non lo impone; è una convenzione di denominazione che dice agli altri programmatori "trattalo come una regola fissa."

    **Concept Tested:** Constants by Convention

---

#### 8. Quale regola si applica quando definisci una funzione che ha sia parametri obbligatori sia parametri predefiniti?

<div class="upper-alpha" markdown>
1. I parametri predefiniti devono venire prima dei parametri obbligatori
2. I parametri obbligatori devono venire prima dei parametri predefiniti
3. Non puoi mischiare parametri obbligatori e predefiniti nella stessa funzione
4. I parametri predefiniti devono tutti avere lo stesso valore predefinito
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. I parametri obbligatori (quelli senza valori predefiniti) devono venire prima nella definizione della funzione, seguiti dai parametri con valori predefiniti. Per esempio: `def greet(name, greeting="Hello"):` è valido. Scrivere `def greet(greeting="Hello", name):` causerebbe un `SyntaxError` perché il parametro obbligatorio `name` viene dopo il parametro predefinito.

    **Concept Tested:** Default Parameter Values

---

#### 9. Cos'è una funzione pura?

<div class="upper-alpha" markdown>
1. Una funzione che usa solo numeri, mai stringhe
2. Una funzione definita con `def pure:` invece di `def`
3. Una funzione che produce sempre lo stesso output per gli stessi input e non cambia nulla fuori di sé stessa
4. Una funzione che chiama solo altre funzioni e non usa mai `print()`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Una funzione pura restituisce sempre lo stesso risultato dati gli stessi argomenti, e non cambia nessuna variabile fuori dal proprio scope (nessun effetto collaterale). Le funzioni pure sono più facili da testare e debuggare. Al contrario, una funzione che modifica una variabile globale, stampa sullo schermo, o disegna su un canvas ha effetti collaterali.

    **Concept Tested:** Pure Functions vs Side Effects

---

#### 10. Qual è il modo più veloce per scambiare i valori delle variabili `a` e `b` in Python?

<div class="upper-alpha" markdown>
1. `a = b` poi `b = a`
2. `temp = a`, poi `a = b`, poi `b = temp`
3. `a, b = b, a`
4. `swap(a, b)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Python supporta l'assegnazione multipla che valuta completamente il lato destro prima di assegnare, rendendo `a, b = b, a` uno scambio sicuro in una riga. L'opzione A perde il valore originale di `a`. L'opzione B (l'approccio con variabile temporanea) è corretta ma richiede tre righe. L'opzione D non è una funzione Python built-in.

    **Concept Tested:** Swapping Variables

---
