# Quiz: Variabili e Numeri

Verifica la tua comprensione di variabili, interi, float e regole di denominazione con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Cos'è una variabile in Python?

<div class="upper-alpha" markdown>
1. Una parola che Python riserva per uso proprio
2. Una posizione di memoria con un nome che contiene un valore nella memoria del tuo programma
3. Un tipo di ciclo che ripete un blocco di codice
4. Un simbolo speciale usato per scrivere commenti
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Una variabile è una posizione di memoria etichettata nella memoria del tuo programma. Le dai un nome, ci memorizzi dentro un valore, e Python ricorda quel valore per te. Pensala come un post-it con un nome sul davanti e il valore attuale sul retro — quando ti serve, lo cerchi per nome.

    **Concept Tested:** Variable Assignment

---

#### 2. Cosa significa il segno `=` nell'istruzione Python `score = 10`?

<div class="upper-alpha" markdown>
1. Verifica se `score` è uguale a `10`
2. Aggiunge `10` al valore attuale di `score`
3. Memorizza il valore `10` nella variabile chiamata `score`
4. Stampa il numero `10` nell'area di output
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. In Python, `=` è l'operatore di assegnazione — significa "prendi il valore a destra e memorizzalo nella variabile a sinistra." È un'istruzione a senso unico; il valore fluisce da destra verso sinistra. Non significa "è uguale a" come in matematica — quel confronto usa `==` (due segni di uguale).

    **Concept Tested:** Variable Assignment

---

#### 3. Quale nome di variabile segue la convenzione di denominazione snake_case di Python?

<div class="upper-alpha" markdown>
1. `MyScore`
2. `my-score`
3. `myscore`
4. `my_score`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. Lo snake_case unisce le parole con underscore e mantiene tutte le lettere minuscole: `my_score`. `MyScore` usa lettere maiuscole (quello è camelCase o PascalCase). `my-score` usa un trattino, che Python legge come sottrazione. `myscore` attacca le parole senza alcun separatore, rendendolo più difficile da leggere.

    **Concept Tested:** Variable Naming (snake_case)

---

#### 4. Che tipo di numero è `3.14` in Python?

<div class="upper-alpha" markdown>
1. Un intero (`int`)
2. Una stringa (`str`)
3. Un float (`float`)
4. Un booleano (`bool`)
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Qualsiasi numero con una virgola decimale è un float (abbreviazione di numero a virgola mobile) in Python. Gli interi sono numeri interi senza virgola decimale. `3.14` ha una virgola decimale, quindi Python lo memorizza come `float`. Usi i float per misurazioni, denaro e valori che non cadono esattamente su un numero intero.

    **Concept Tested:** Floats

---

#### 5. Cosa stamperà Python quando questo codice viene eseguito?

```python
score = 10
score = 25
print(score)
```

<div class="upper-alpha" markdown>
1. `10`
2. `25`
3. `10` e poi `25` su due righe
4. Un errore, perché non puoi assegnare una variabile due volte
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Python legge ogni riga in ordine. Prima memorizza `10` in `score`, poi sostituisce quel valore con `25`. Quando viene eseguito `print(score)`, la variabile contiene `25`. Non c'è alcun errore — riassegnare una variabile è del tutto normale ed è il modo in cui i programmi aggiornano i valori mentre vengono eseguiti.

    **Concept Tested:** Variable Reassignment

---

#### 6. Quale nome di variabile causerebbe un errore in Python?

<div class="upper-alpha" markdown>
1. `player_score`
2. `_hidden`
3. `1st_place`
4. `total_points`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. I nomi di variabile non possono iniziare con una cifra. `1st_place` inizia con `1`, quindi Python genera un `SyntaxError`. I nomi di variabile devono iniziare con una lettera o un underscore. `player_score`, `_hidden` e `total_points` seguono tutti questa regola e sono nomi validi.

    **Concept Tested:** Variable Naming Rules

---

#### 7. Cosa stampa Python quando dividi due interi usando `/`?

```python
result = 10 / 2
print(result)
```

<div class="upper-alpha" markdown>
1. `5` (un intero)
2. `5.0` (un float)
3. `10/2` (una frazione)
4. Un errore, perché non puoi dividere interi
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In Python 3, dividere con `/` restituisce sempre un float, anche quando il risultato è un numero intero. Quindi `10 / 2` dà `5.0`, non `5`. Se vuoi un risultato intero, usa invece l'operatore di divisione intera `//`: `10 // 2` dà `5`.

    **Concept Tested:** Floats

---

#### 8. Qual è il valore di `None` in Python?

<div class="upper-alpha" markdown>
1. Il numero intero zero (`0`)
2. Una stringa vuota senza caratteri (`""`)
3. Un valore speciale che significa "nessun valore ancora" o "niente qui"
4. Il valore booleano `False`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `None` è un valore speciale di Python di tipo `NoneType` che significa "nessun valore" o "niente qui." È diverso da `0` (un intero), `""` (una stringa vuota) e `False` (un booleano) — ognuno di questi è comunque qualcosa, mentre `None` significa l'assenza totale di un valore.

    **Concept Tested:** None Value

---

#### 9. Cosa c'è di sbagliato nel nome di variabile `my-score`?

<div class="upper-alpha" markdown>
1. È troppo lungo e rallenterà il programma
2. Python legge il trattino come segno meno e pensa che tu stia sottraendo due variabili
3. I nomi di variabile devono iniziare con una lettera maiuscola
4. Non puoi usare la lettera `y` in un nome di variabile
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Il trattino `-` è l'operatore di sottrazione di Python. Quando Python vede `my-score`, lo legge come la variabile `my` meno la variabile `score`, non come un unico nome. Questo causa un `NameError` perché `my` e `score` non sono state definite. Usa sempre un underscore `_` per unire le parole in un nome di variabile.

    **Concept Tested:** Variable Naming Rules

---

#### 10. Quale delle seguenti descrive meglio quando usare un intero rispetto a un float?

<div class="upper-alpha" markdown>
1. Usa sempre i float — sono più precisi degli interi
2. Usa gli interi per le cose che conti (lati, vite, punteggio) e i float per misurazioni o decimali
3. Usa gli interi per il testo e i float per i numeri
4. Usa i float nella prima metà di un programma e gli interi nella seconda metà
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Gli interi (`int`) servono per cose intere e contabili — numero di vite, punteggio di gioco, numero di lati di una forma. I float (`float`) servono per valori che possono avere parti decimali — altezze, prezzi, percentuali, pi greco. Scegliere il tipo giusto rende il tuo codice più chiaro ed evita risultati decimali inaspettati.

    **Concept Tested:** Integers

---
