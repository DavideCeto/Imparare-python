# Riferimenti: Elaborazione del Testo ed Espressioni Regolari

1. **Regular Expression** — Wikipedia.
   [https://en.wikipedia.org/wiki/Regular_expression](https://en.wikipedia.org/wiki/Regular_expression)
   Copre la storia, la teoria, e la sintassi delle espressioni regolari in tutti i linguaggi di programmazione, spiegando come funzionano i motori di pattern-matching — contesto fondamentale per capire cosa fa internamente il modulo `re` di Python.

2. **String Searching Algorithm** — Wikipedia.
   [https://en.wikipedia.org/wiki/String-searching_algorithm](https://en.wikipedia.org/wiki/String-searching_algorithm)
   Spiega come i computer scansionano efficientemente il testo per i pattern, dando agli studenti le basi concettuali per capire perché `re.search()` e `re.findall()` sono più veloci di un ciclo manuale attraverso i caratteri.

3. **Finite-State Machine** — Wikipedia.
   [https://en.wikipedia.org/wiki/Finite-state_machine](https://en.wikipedia.org/wiki/Finite-state_machine)
   Descrive il modello a macchina a stati che i motori regex usano internamente per far corrispondere le classi di caratteri e i quantificatori, aiutando gli studenti a visualizzare come un pattern come `\d+` scorre il testo di input un carattere alla volta.

4. **Automate the Boring Stuff with Python** di Al Sweigart (No Starch Press; gratuito online su automatetheboringstuff.com).
   Il Capitolo 7 di questo libro è dedicato interamente alle espressioni regolari in Python, percorrendo `re.search`, `re.findall`, `re.sub`, i gruppi, e le classi di caratteri con esempi pratici e del mondo reale perfettamente adatti agli argomenti di questo capitolo.

5. **Python Crash Course** di Eric Matthes (No Starch Press).
   Fornisce una trattazione chiara e adatta ai principianti delle capacità di gestione delle stringhe di Python e del modulo `re`, con esercizi che rafforzano i concetti di pattern matching e trasformazione del testo introdotti in questo capitolo.

6. **Python `re` Module — Official Documentation**
   [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
   Il riferimento autorevole per ogni funzione, flag, e sequenza speciale nel modulo `re` di Python, inclusa la sintassi completa per le classi di caratteri, i quantificatori, le ancore, e gli oggetti pattern compilati usati in tutto questo capitolo.

7. **Regular Expressions in Python — Real Python**
   [https://realpython.com/regex-python/](https://realpython.com/regex-python/)
   Un tutorial approfondito e passo passo che copre `re.search`, `re.findall`, `re.sub`, i gruppi, e i lookahead con esempi annotati ed esercizi interattivi ideali per studenti che imparano le regex per la prima volta.

8. **Python RegEx — W3Schools**
   [https://www.w3schools.com/python/python_regex.asp](https://www.w3schools.com/python/python_regex.asp)
   Offre una pagina di riferimento rapido per il modulo `re` di Python con frammenti di codice provabili per ogni funzione principale e una tabella concisa dei metacaratteri — ottima per studenti che vogliono un bigino insieme a questo capitolo.

9. **Python Regular Expressions — Programiz**
   [https://www.programiz.com/python-programming/regex](https://www.programiz.com/python-programming/regex)
   Presenta le espressioni regolari con diagrammi chiari e spiegazioni adatte ai principianti dei quantificatori, delle classi di caratteri, e della differenza tra `re.search` e `re.match`, supportando direttamente i concetti insegnati in questo capitolo.

10. **Python Regular Expression Tutorial — GeeksforGeeks**
    [https://www.geeksforgeeks.org/regular-expression-python-examples/](https://www.geeksforgeeks.org/regular-expression-python-examples/)
    Fornisce numerosi esempi lavorati di `re.search`, `re.findall`, `re.split`, e `re.sub` con output annotato, offrendo agli studenti problemi di pratica extra e percorsi di pattern-matching che rafforzano gli esercizi di questo capitolo.
