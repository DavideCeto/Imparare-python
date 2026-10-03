# Glossario dei termini

#### abs() — valore assoluto

Una funzione built-in che restituisce la grandezza non negativa di un numero, convertendo i numeri negativi nei loro equivalenti positivi e lasciando invariati i numeri non negativi.

**Esempio:** `abs(-7)` restituisce `7`; `abs(5)` restituisce `5`; `abs(-3.14)` restituisce `3.14`.

#### Posizionamento assoluto: goto(x, y), setx(), sety()

Metodi della turtle che spostano la turtle in un punto specifico dello schermo invece che relativamente alla sua posizione attuale: `goto(x, y)` si sposta alle coordinate indicate; `setx(x)` cambia solo la coordinata x; `sety(y)` cambia solo la y.

**Esempio:** `t.goto(0, 0)` sposta la turtle al centro dello schermo; `t.goto(-200, 100)` la sposta nella zona in alto a sinistra.

#### Panoramica sui tipi di dati astratti

Una descrizione concettuale di una struttura dati definita dal suo comportamento (le operazioni che supporta e le loro regole) piuttosto che da come è implementata, permettendo ai programmatori di ragionare sui dati senza preoccuparsi dei dettagli di basso livello.

**Esempio:** Uno stack è un tipo di dato astratto definito dalle operazioni push e pop; può essere implementato usando una lista Python.

#### Accedere ad attributi e chiamare metodi (obj.attr, obj.method())

La notazione a punto usata per leggere o impostare un attributo di un oggetto (`obj.attribute`) o per invocare uno dei suoi metodi (`obj.method(argomenti)`).

**Esempio:** `player.score = 100` imposta un attributo; `player.level_up()` chiama un metodo sullo stesso oggetto `player`.

#### Accedere ai valori tramite chiave (d[key])

Il metodo per recuperare un valore memorizzato in un dizionario inserendo la chiave tra parentesi quadre dopo il nome del dizionario; se la chiave non esiste, Python genera un `KeyError`.

**Esempio:** `student["name"]` restituisce `"Alex"` da un dizionario in cui `"name"` è una chiave; accedere a una chiave mancante come `student["phone"]` genera un errore.

#### Funzioni di attivazione: relu, softmax

Funzioni matematiche applicate all'output di ogni neurone in uno strato di rete neurale: `relu` (Rectified Linear Unit) restituisce zero per gli input negativi e l'input stesso per quelli positivi; `softmax` converte una lista di valori in probabilità che sommano a 1.

**Esempio:** Gli strati nascosti usano tipicamente `relu` per introdurre non linearità; lo strato finale di un classificatore usa `softmax` per restituire una probabilità per ciascuna classe.

#### Metodi .add(), .remove(), .discard()

Metodi degli insiemi che modificano un insieme: `.add(item)` inserisce un elemento; `.remove(item)` elimina un elemento e genera `KeyError` se manca; `.discard(item)` elimina un elemento silenziosamente se esiste, o non fa nulla se non esiste.

**Esempio:** `s.add(5)` aggiunge 5; `s.discard(99)` non fa nulla se 99 non è nell'insieme, evitando un errore.

#### Aggiungere e aggiornare coppie chiave-valore

Il modo per inserire una nuova coppia chiave-valore in un dizionario o cambiare il valore di una chiave esistente usando l'assegnazione con la notazione a parentesi quadre.

**Esempio:** `inventory["apples"] = 10` aggiunge una nuova voce; `inventory["apples"] = 15` la aggiorna se `"apples"` esisteva già.

#### Rappresentazione a lista di adiacenza

Un modo per rappresentare un grafo memorizzando, per ogni nodo, una lista degli altri nodi a cui è direttamente collegato, tipicamente come un dizionario in cui le chiavi sono i nomi dei nodi e i valori sono liste di vicini.

**Esempio:** `graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}` rappresenta un grafo triangolare in cui A è collegato sia a B che a C.

#### Alternanza con |

Un operatore regex che corrisponde al pattern alla sua sinistra oppure al pattern alla sua destra, funzionando come un OR logico all'interno di un'espressione regolare.

**Esempio:** `r"cat|dog"` corrisponde a una stringa contenente `"cat"` oppure `"dog"`.

#### Ancore: ^ (inizio), $ (fine)

Simboli regex speciali che corrispondono a posizioni in una stringa anziché a caratteri: `^` richiede che la corrispondenza inizi proprio all'inizio della stringa; `$` richiede che finisca proprio alla fine.

**Esempio:** `r"^\d+"` corrisponde a una stringa che inizia con cifre; `r"\.$"` corrisponde a una stringa che termina con un punto.

#### Cicli di animazione

Cicli ripetuti di cancella-disegna-aggiorna che creano l'illusione del movimento ridisegnando rapidamente una scena con posizioni leggermente cambiate, in modo simile ai fotogrammi di un film.

**Esempio:** Un semplice ciclo di animazione con turtle chiama `clear()`, aggiorna la posizione della palla, disegna la palla, poi richiama il ciclo molte volte al secondo.

#### Animazione con turtle (cicli basati su fotogrammi)

Una tecnica per creare immagini in movimento nella grafica turtle cancellando ripetutamente il canvas e ridisegnando le posizioni aggiornate dentro un ciclo, usando `tracer()` e `update()` per un'animazione fluida.

**Esempio:** Un'animazione di una palla cancella la vecchia posizione, calcola quella nuova, disegna la palla lì, e ripete rapidamente così la palla sembra muoversi in modo fluido.

#### Operatori aritmetici: +, -, *, /

I quattro operatori matematici di base in Python: `+` somma, `-` sottrae, `*` moltiplica e `/` divide due valori numerici.

**Esempio:** `total = price * quantity + tax` usa tre operatori aritmetici in una sola espressione.

#### Operazioni sugli array e nozioni di base sul broadcasting

La funzionalità di NumPy che applica gli operatori aritmetici a interi array elemento per elemento, ed espande automaticamente un array più piccolo per farlo corrispondere alla forma di uno più grande quando si eseguono operazioni tra array di dimensioni diverse.

**Esempio:** `np.array([1, 2, 3]) + np.array([10, 20, 30])` restituisce `array([11, 22, 33])` senza alcun ciclo.

#### Istruzione assert con messaggi di errore

Uno strumento di debug che verifica una condizione e genera un `AssertionError` con un messaggio opzionale se la condizione è `False`, usato per verificare le ipotesi all'interno di un programma durante lo sviluppo.

**Esempio:** `assert score >= 0, "Score must not be negative"` interrompe il programma con quel messaggio se `score` risulta in qualche modo negativo.

#### Attributi — proprietà di un oggetto

Variabili che appartengono a un oggetto specifico e memorizzano dati che ne descrivono le caratteristiche; vi si accede usando la notazione a punto dopo il nome dell'oggetto.

**Esempio:** Se `player` è un oggetto, `player.name` e `player.score` sono attributi che memorizzano il nome e il punteggio del giocatore.

#### Operatori di assegnazione aumentata (+=, -=, *=, /=)

Operatori abbreviati che combinano un'operazione aritmetica con l'assegnazione, aggiornando il valore di una variabile in base al suo valore attuale senza riscrivere due volte il nome della variabile.

**Esempio:** `score += 10` aggiunge 10 al valore attuale di `score`, equivalente a scrivere `score = score + 10`.

#### Autoencoder — panoramica

Un'architettura di rete neurale con un encoder che comprime i dati di input in una rappresentazione compatta e un decoder che ricostruisce i dati originali, addestrata per minimizzare l'errore di ricostruzione.

**Esempio:** Un autoencoder addestrato su immagini di volti impara un codice compresso per ogni volto; il codice può essere usato per rimozione del rumore, generazione o rilevamento di anomalie.

#### Colore di sfondo e colore della penna

Due impostazioni di colore separate nella grafica turtle: il colore di sfondo riempie l'intera finestra di disegno ed è impostato con `bgcolor()`; il colore della penna determina il colore delle linee disegnate dalla turtle ed è impostato con `pencolor()`.

**Esempio:** `screen.bgcolor("black"); t.pencolor("white")` crea un effetto cielo stellato in cui le linee bianche sono visibili sullo sfondo scuro.

#### Dimensione del batch ed epoche

Due iperparametri di addestramento: la dimensione del batch è il numero di esempi di addestramento elaborati prima che i pesi del modello vengano aggiornati; un'epoca è un intero passaggio attraverso tutto il dataset di addestramento.

**Esempio:** Con 1000 campioni, `batch_size=32` ed `epochs=5` significa che il modello aggiorna i pesi circa 31 volte per epoca e si addestra per 5 epoche (155 aggiornamenti totali).

#### Tracciamento dei colori nella BFS (bianco, grigio, nero)

Una tecnica classica di implementazione della BFS in cui i nodi sono etichettati bianco (non visitato), grigio (scoperto ma non ancora completamente elaborato) o nero (completamente esplorato), per tracciare i progressi ed evitare di rivisitare i nodi.

**Esempio:** Quando la BFS incontra per la prima volta un vicino, lo marca grigio e lo aggiunge alla coda; dopo aver elaborato tutti i suoi vicini, lo marca nero.

#### BFS per la ricerca di percorsi

L'applicazione della ricerca in ampiezza (Breadth-First Search) per scoprire il percorso più breve tra due nodi in un grafo, registrando il genitore di ogni nodo durante l'attraversamento e ripercorrendo a ritroso dalla destinazione alla sorgente.

**Esempio:** In una griglia a labirinto, la BFS trova il numero minimo di passi dall'inizio alla fine esplorando tutte le celle raggiungibili un passo alla volta.

#### Concetto di ricerca binaria

Un algoritmo efficiente per trovare un valore in una lista ordinata dimezzando ripetutamente l'intervallo di ricerca — controllando l'elemento centrale ed eliminando metà degli elementi rimanenti — invece di controllare ogni elemento uno per uno.

**Esempio:** Indovinare un numero tra 1 e 100 tentando sempre il punto medio (50, poi 25 o 75, ecc.) è una ricerca binaria; trova qualsiasi numero in al massimo 7 tentativi.

#### Righe vuote e leggibilità del codice

La pratica di inserire righe vuote tra sezioni di codice — ad esempio tra definizioni di funzioni o gruppi logici di istruzioni — per rendere i programmi più facili da scorrere e capire.

**Esempio:** Inserire una riga vuota prima e dopo ogni definizione di funzione aiuta i lettori a vedere rapidamente dove finisce una funzione e inizia la successiva.

#### bool() — conversione a booleano

Una funzione built-in che converte un valore in `True` o `False` seguendo le regole di verità (truthiness) di Python: `0`, `None`, stringhe vuote e collezioni vuote diventano `False`; tutto il resto diventa `True`.

**Esempio:** `bool(0)` restituisce `False`; `bool("hello")` restituisce `True`; `bool([])` restituisce `False`.

#### Tipo booleano (bool) — True e False

Un tipo di dato Python che contiene esattamente uno di due valori — `True` o `False` — usato per rappresentare il risultato di confronti e per controllare il flusso di istruzioni `if` e cicli.

**Esempio:** `is_raining = True` memorizza un fatto sì/no; `5 > 3` restituisce `True` e `5 < 3` restituisce `False`.

#### Algoritmo di ricerca in ampiezza (BFS)

Un algoritmo di attraversamento dei grafi che esplora tutti i vicini di un nodo di partenza prima di passare ai loro vicini, visitando i nodi livello per livello verso l'esterno, ed è garantito trovare il percorso più breve in un grafo non pesato.

**Esempio:** La BFS su un grafo stradale trova il minor numero di tratti stradali tra due città esplorando tutte le città a un salto di distanza prima di quelle a due salti.

#### break — uscire anticipatamente da un ciclo

Un'istruzione che termina immediatamente il ciclo `for` o `while` più vicino, saltando le iterazioni rimanenti e proseguendo con il codice dopo il ciclo.

**Esempio:** `for n in range(100):` / `if n == 5: break` interrompe il ciclo non appena `n` raggiunge 5 invece di continuare fino a 99.

#### Costruire un selettore di colori con turtle

Un progetto di grafica turtle che crea regioni colorate cliccabili sullo schermo, dimostrando la gestione degli eventi, la matematica delle coordinate e la logica condizionale per cambiare il colore di disegno attivo quando l'utente clicca.

**Esempio:** Viene disegnata una fila di rettangoli colorati, e un gestore `onscreenclick` controlla quale rettangolo è stato cliccato per aggiornare il colore della penna.

#### Funzioni di callback

Funzioni passate come argomenti a un'altra funzione o registrate presso un sistema di eventi, così da poter essere chiamate in seguito — automaticamente, in risposta a un evento — invece di essere chiamate direttamente.

**Esempio:** In `screen.onscreenclick(draw_dot)`, `draw_dot` è una callback che il sistema turtle chiama automaticamente ogni volta che si verifica un evento di click.

#### Chiamare una funzione

L'azione di eseguire una funzione precedentemente definita scrivendone il nome seguito da parentesi, passando opzionalmente argomenti all'interno delle parentesi.

**Esempio:** Dopo aver definito `def greet(name): print("Hello, " + name)`, scrivere `greet("Alex")` esegue la funzione e stampa `Hello, Alex`.

#### Sensibilità alle maiuscole/minuscole in Python

La proprietà di Python per cui le lettere maiuscole e minuscole sono trattate come caratteri diversi, quindi `Name`, `name` e `NAME` sono tre nomi di variabile distinti e non collegati.

**Esempio:** Se memorizzi un valore in `score` ma in seguito scrivi `Score`, Python genererà un `NameError` perché non riconosce `Score`.

#### Classi di caratteri: [a-z], [A-Z], [0-9]

Sintassi regex che usa le parentesi quadre per definire un insieme di caratteri, dove un intervallo come `a-z` corrisponde a qualsiasi lettera minuscola singola, `A-Z` a qualsiasi lettera maiuscola, e `0-9` a qualsiasi singola cifra.

**Esempio:** `r"[aeiou]"` corrisponde a qualsiasi vocale; `r"[A-Za-z]"` corrisponde a qualsiasi lettera indipendentemente dal maiuscolo/minuscolo.

#### Verificare None con is None

Il modo consigliato per verificare se una variabile contiene il valore `None`, usando l'operatore `is` invece di `==`, perché `is` controlla l'identità (lo stesso identico oggetto) piuttosto che l'uguaglianza.

**Esempio:** `if result is None: print("No value returned")` verifica in modo sicuro la presenza di `None` senza innescare comportamenti inattesi da un'uguaglianza sovraccaricata.

#### Verificare l'appartenenza di una chiave con in

Usare la parola chiave `in` con un dizionario per verificare se una determinata chiave esiste nel dizionario, restituendo `True` o `False` senza generare un errore.

**Esempio:** `if "score" in student:` controlla se la chiave `"score"` esiste prima di provare ad accedervi.

#### Verificare l'appartenenza con in

Una parola chiave usata in un'espressione booleana per verificare se un valore esiste come elemento di una lista, stringa, tupla o altra sequenza, restituendo `True` o `False`.

**Esempio:** `"apple" in fruits` restituisce `True` se la lista `fruits` contiene `"apple"`.

#### Verificare l'appartenenza con in (insiemi)

Usare la parola chiave `in` per verificare se un valore è membro di un insieme; questa operazione è molto veloce per gli insiemi (molto più veloce che cercare in una lista) perché gli insiemi usano l'hashing internamente.

**Esempio:** `if "python" in known_words:` verifica se una parola esiste nell'insieme di parole conosciute quasi istantaneamente, anche per insiemi molto grandi.

#### Metodi di classe __str__() e __repr__()

Due metodi speciali che controllano come vengono visualizzati gli oggetti: `__str__()` fornisce una descrizione leggibile e amichevole usata da `print()` e `str()`; `__repr__()` fornisce una descrizione inequivocabile orientata allo sviluppatore usata nella REPL e per il debug.

**Esempio:** `str(Dog("Buddy"))` potrebbe restituire `"Dog named Buddy"` mentre `repr(Dog("Buddy"))` restituisce `"Dog('Buddy', age=3)"` con tutti i dati necessari per ricreare l'oggetto.

#### Parola chiave class — definire una classe

La parola chiave Python usata per iniziare la definizione di una nuova classe, seguita dal nome della classe e da due punti, dopo i quali un blocco indentato contiene gli attributi e i metodi della classe.

**Esempio:** `class Dog:` inizia la definizione di una classe `Dog`; tutto ciò che è indentato sotto fa parte della classe.

#### Cancellare: clear(), reset()

Due metodi della turtle che cancellano i disegni: `clear()` cancella tutte le linee disegnate dalla turtle ma mantiene la sua posizione, colore e impostazioni attuali; `reset()` cancella i disegni e riporta anche la turtle al centro con le impostazioni predefinite.

**Esempio:** In un gioco, chiamare `t.clear()` all'inizio di ogni fotogramma cancella il disegno precedente prima di ridisegnare la scena aggiornata.

#### Commenti nel codice — quando e perché

La pratica di aggiungere commenti con `#` per spiegare il perché dietro un codice complesso o non ovvio — il ragionamento, il contesto o l'intento — piuttosto che ripetere ciò che il codice rende già chiaro.

**Esempio:** `# Reverse the list so newest entries appear first` spiega l'intento; `# adds 1 to x` su `x += 1` non aggiunge alcun valore.

#### Riutilizzabilità del codice

L'obiettivo di progettazione di scrivere codice — in particolare funzioni e moduli — in modo sufficientemente generale da poter essere usato in più punti o progetti senza doverlo riscrivere.

**Esempio:** Una funzione `calculate_area(width, height)` può essere chiamata ovunque serva un'area, invece di riscrivere la formula di moltiplicazione ogni volta.

#### Grafici a barre colorati e visualizzazione dati in Jupyter

L'uso di matplotlib o altre librerie all'interno di un Jupyter notebook per creare rappresentazioni visive dei dati — come barre colorate — mostrate direttamente nell'output del notebook.

**Esempio:** `plt.bar(subjects, scores, color=["red","blue","green"]); plt.show()` mostra un grafico a barre colorato dei punteggi dei test direttamente nel notebook.

#### Il colore nella grafica turtle

Il sistema che turtle usa per impostare i colori di disegno e riempimento, accettando stringhe di colori con nome, stringhe esadecimali o tuple RGB (dopo aver chiamato `colormode(255)`), e applicato con metodi come `color()`, `pencolor()` e `fillcolor()`.

**Esempio:** `screen.colormode(255); t.color((100, 149, 237))` imposta la penna su un blu cornflower usando una tupla RGB.

#### Colore: color(), pencolor(), fillcolor()

Metodi della turtle che impostano i colori di disegno: `color(c)` imposta sia il colore della penna che quello di riempimento insieme; `pencolor(c)` imposta solo il colore della linea; `fillcolor(c)` imposta solo il colore di riempimento interno delle forme.

**Esempio:** `t.color("blue")` rende sia il contorno che il riempimento blu; `t.pencolor("red"); t.fillcolor("yellow")` li imposta separatamente.

#### Commenti (su singola riga con #)

Testo in un programma Python che inizia con il carattere `#` e viene completamente ignorato dall'interprete; i commenti servono solo a spiegare il codice ai lettori umani.

**Esempio:** `# This loop draws a square` posto sopra un ciclo dice al lettore cosa fa il codice senza influire sulla sua esecuzione.

#### Eccezioni comuni: ValueError, TypeError, IndexError, KeyError, NameError, ZeroDivisionError

Sei tipi di errore Python frequentemente incontrati: `ValueError` (valore del tipo sbagliato), `TypeError` (tipo di dato sbagliato), `IndexError` (indice fuori intervallo), `KeyError` (chiave del dizionario non trovata), `NameError` (variabile non definita), `ZeroDivisionError` (divisione per zero).

**Esempio:** `int("hello")` genera `ValueError`; `"text" + 5` genera `TypeError`; `[][0]` genera `IndexError`.

#### Pattern regex comuni: \d (cifra), \w (carattere di parola), \s (spazio bianco)

Tre classi di caratteri abbreviate frequentemente usate nelle espressioni regolari: `\d` corrisponde a qualsiasi cifra `0-9`; `\w` corrisponde a qualsiasi lettera, cifra o underscore; `\s` corrisponde a qualsiasi carattere di spaziatura (spazio, tab, a capo).

**Esempio:** `r"\d\d\d-\d\d\d\d"` corrisponde a un pattern di numero di telefono come `555-1234`; `r"\w+"` corrisponde a un'intera parola.

#### Operatori di confronto: >, <, >=, <=, ==, !=

Operatori che confrontano due valori e restituiscono un risultato booleano: `>` (maggiore di), `<` (minore di), `>=` (maggiore o uguale a), `<=` (minore o uguale a), `==` (uguale a), `!=` (diverso da).

**Esempio:** `score >= 90` restituisce `True` se il punteggio è 90 o superiore, cosa che potresti usare per decidere se stampare "A grade".

#### Conda — gestore di ambienti e pacchetti

Uno strumento che installa pacchetti Python e crea ambienti isolati così che progetti diversi possano usare versioni diverse delle librerie senza interferire tra loro.

**Esempio:** Puoi usare conda per creare un ambiente con una libreria più vecchia per un progetto scolastico e un ambiente separato con una libreria più recente per un progetto personale.

#### Espressioni condizionali (ternarie): x if condizione else y

Un'espressione compatta su una sola riga che restituisce uno di due valori a seconda di una condizione, scritta come `valore_se_vero if condizione else valore_se_falso`.

**Esempio:** `label = "adult" if age >= 18 else "minor"` imposta `label` in una riga invece di un blocco `if...else` di quattro righe.

#### Costanti (per convenzione, TUTTO_MAIUSCOLO)

Valori in un programma che non devono mai cambiare durante l'esecuzione, indicati scrivendone i nomi interamente in lettere maiuscole con underscore, anche se Python non impedisce tecnicamente la riassegnazione.

**Esempio:** `MAX_PLAYERS = 4` e `GRAVITY = 9.8` sono costanti i cui nomi TUTTO_MAIUSCOLO segnalano ai lettori che questi valori dovrebbero restare fissi.

#### continue — saltare alla prossima iterazione

Un'istruzione che salta il resto dell'iterazione corrente del ciclo e passa direttamente alla successiva, senza uscire completamente dal ciclo.

**Esempio:** `for n in range(10):` / `if n % 2 == 0: continue` / `print(n)` stampa solo i numeri dispari saltando quelli pari.

#### Conv2D — strati convoluzionali

Uno strato di Keras che applica un insieme di piccoli filtri (kernel) su un'immagine per rilevare pattern locali come bordi, texture e forme, formando il blocco costitutivo principale delle reti di riconoscimento immagini.

**Esempio:** `Conv2D(32, (3, 3), activation="relu")` applica 32 filtri 3×3 diversi all'immagine di input per rilevare 32 diverse caratteristiche di basso livello.

#### Convertire le stringhe di input in numeri con int() / float()

Il passaggio necessario di avvolgere `input()` con `int()` o `float()` per trasformare il testo digitato dall'utente in un valore numerico utilizzabile nei calcoli.

**Esempio:** `age = int(input("Enter your age: "))` converte il testo digitato in un intero così puoi scrivere `age + 1` senza un `TypeError`.

#### Reti neurali convoluzionali (CNN)

Un tipo di architettura di rete neurale progettata per elaborare dati a griglia come le immagini, usando strati convoluzionali per rilevare pattern locali e strati di pooling per ridurre la dimensione spaziale.

**Esempio:** Il sistema di riconoscimento immagini nell'app fotocamera del tuo telefono è alimentato da una CNN addestrata a identificare oggetti da milioni di foto etichettate.

#### Creare un dizionario con {}

La sintassi per creare un nuovo dizionario racchiudendo coppie `chiave: valore` separate da virgola tra parentesi graffe, con ogni chiave e il suo valore separati da due punti.

**Esempio:** `ages = {"Alice": 12, "Bob": 13, "Carol": 11}` crea un dizionario che associa nomi a età.

#### Creare una lista con []

La sintassi per creare una nuova lista in Python inserendo zero o più elementi separati da virgola tra parentesi quadre.

**Esempio:** `empty = []` crea una lista vuota; `numbers = [1, 2, 3, 4, 5]` crea una lista di cinque interi.

#### Creare un insieme con {} o set()

I due modi per creare un insieme: parentesi graffe con elementi (`{1, 2, 3}`) o il costruttore `set()` con un iterabile (`set([1, 2, 3])`); un insieme vuoto deve essere creato con `set()` perché `{}` crea un dizionario vuoto.

**Esempio:** `vowels = {"a", "e", "i", "o", "u"}` usa le parentesi graffe; `digits = set(range(10))` converte un range in un insieme.

#### Creare una tupla con ()

La sintassi per creare una nuova tupla inserendo elementi separati da virgola tra parentesi tonde; le parentesi sono in realtà opzionali — sono le virgole a creare la tupla.

**Esempio:** `colors = ("red", "green", "blue")` crea una tupla; `pair = 1, 2` crea anch'essa una tupla `(1, 2)` perché è la virgola che conta.

#### Creare un oggetto turtle.Screen()

L'atto di chiamare `turtle.Screen()` per ottenere un riferimento alla finestra di disegno, che permette di impostarne dimensioni, colore di sfondo, titolo e di rispondere agli eventi.

**Esempio:** `screen = turtle.Screen(); screen.bgcolor("lightblue")` crea l'oggetto schermo e ne imposta il colore di sfondo.

#### Creare un oggetto turtle.Turtle()

L'atto di chiamare `turtle.Turtle()` per creare una nuova turtle — un cursore di disegno — che può essere spostata, ruotata e personalizzata per disegnare linee e forme sullo schermo.

**Esempio:** `t = turtle.Turtle()` crea una turtle chiamata `t`; poi `t.forward(100)` la sposta in avanti di 100 pixel.

#### Creare moduli personalizzati (file .py)

La pratica di salvare funzioni e variabili Python in un file `.py` che altri programmi possono importare, permettendo di organizzare, condividere e riutilizzare il codice tra più progetti.

**Esempio:** Salvare `def greet(name): print("Hi", name)` in `helpers.py` permette a un altro file di fare `from helpers import greet` e chiamarla.

#### Creare istanze di una classe

Il processo di chiamare una classe come una funzione per produrre un nuovo oggetto indipendente con una propria copia degli attributi della classe, inizializzato da `__init__()`.

**Esempio:** `my_dog = Dog("Buddy", 3)` crea un nuovo oggetto `Dog`; `your_dog = Dog("Max", 5)` ne crea uno separato.

#### Nozioni di base sulla lettura di file CSV

Il processo di leggere un file i cui valori sono separati da virgole (Comma-Separated Values), tipicamente eseguito dividendo ogni riga sulle virgole o usando il modulo `csv` di Python.

**Esempio:** Una riga `"Alice,90,A"` da un file CSV può essere divisa con `.split(",")` per ottenere `["Alice", "90", "A"]`.

#### File CSV — leggere/scrivere dati strutturati

File che memorizzano dati tabellari (righe e colonne) come testo semplice, con i valori di ogni riga separati da virgole, leggibili dal modulo `csv` di Python per una gestione affidabile di campi tra virgolette e caratteri speciali.

**Esempio:** `import csv` / `with open("data.csv") as f: reader = csv.reader(f)` / `for row in reader: print(row)` legge ogni riga come una lista.

#### Normalizzazione/preprocessing dei dati

Il passaggio di trasformare i dati grezzi di input in un intervallo numerico coerente — ad esempio dividendo i valori dei pixel per 255 per riportarli dall'intervallo 0–255 a 0–1 — così che la rete neurale si addestri in modo più stabile e veloce.

**Esempio:** `x_train = x_train / 255.0` riporta i valori dei pixel di MNIST all'intervallo 0–1 prima di passarli al modello.

#### Debug con istruzioni print()

Una tecnica semplice che consiste nell'inserire chiamate temporanee a `print()` in punti strategici di un programma per visualizzare i valori delle variabili e tracciare l'esecuzione, aiutando a individuare dove si verifica un comportamento inatteso.

**Esempio:** Aggiungere `print("x =", x)` prima di un calcolo conferma se `x` contiene il valore giusto prima che l'operazione venga eseguita.

#### Valori predefiniti dei parametri

Valori specificati nella definizione di una funzione che vengono usati quando chi chiama la funzione non fornisce l'argomento corrispondente, rendendo opzionali quei parametri.

**Esempio:** `def greet(name, greeting="Hello"): print(greeting + ", " + name)` può essere chiamata come `greet("Alex")` o `greet("Alex", "Hi")`.

#### Definire una funzione con def

Il modo per creare un blocco di codice nominato e riutilizzabile in Python scrivendo la parola chiave `def`, un nome di funzione, parentesi per i parametri, due punti e un corpo indentato di istruzioni.

**Esempio:** `def greet(name): print("Hello, " + name)` definisce una funzione chiamata `greet` che può essere chiamata molte volte con nomi diversi.

#### Strati densi — strati completamente connessi

Un tipo di strato di rete neurale in cui ogni neurone dello strato riceve input da ogni neurone dello strato precedente, imparando una combinazione pesata di tutti gli input.

**Esempio:** `Dense(128, activation="relu")` crea uno strato con 128 neuroni, ciascuno connesso a ogni input, adatto a compiti di apprendimento generici.

#### Algoritmo di ricerca in profondità (DFS)

Un algoritmo di attraversamento dei grafi che segue un percorso il più a fondo possibile prima di tornare indietro e provarne un altro, esplorando i nodi andando il più lontano possibile in una direzione prima di cambiare.

**Esempio:** La DFS su un file system esplora un'intera cartella e tutte le sue sottocartelle prima di passare alla cartella successiva allo stesso livello.

#### DFS e BFS per risolvere labirinti

L'applicazione sia della DFS (esplorare completamente un percorso prima di provarne un altro) sia della BFS (esplorare tutti i percorsi livello per livello) per trovare una via attraverso un labirinto, con la BFS che garantisce la soluzione più breve.

**Esempio:** In un labirinto a griglia, la DFS potrebbe trovare rapidamente un percorso lungo e tortuoso; la BFS impiegherà più tempo ma restituirà sempre il percorso più breve.

#### DFS con ricorsione e backtracking

Un'implementazione della ricerca in profondità in cui ogni nodo viene visitato tramite una chiamata di funzione ricorsiva, e il ritorno dalla chiamata esegue automaticamente il backtracking al nodo precedente per provare un altro percorso.

**Esempio:** Un risolutore ricorsivo di labirinti richiama se stesso per ogni vicino, marca il percorso come visitato e fa "backtracking" rimuovendo il marcatore quando non esiste un percorso in avanti.

#### Comprehension di dizionari

Una sintassi concisa su una riga per creare un nuovo dizionario calcolando coppie chiave-valore da un iterabile, opzionalmente filtrate da una condizione, tutto dentro parentesi graffe.

**Esempio:** `{name: len(name) for name in ["Alice", "Bob"]}` produce `{"Alice": 5, "Bob": 3}`.

#### Metodi dei dizionari: .keys(), .values(), .items()

Metodi built-in dei dizionari che restituiscono oggetti vista: `.keys()` restituisce tutte le chiavi; `.values()` restituisce tutti i valori; `.items()` restituisce tutte le coppie (chiave, valore) come tuple.

**Esempio:** `for subject, grade in report.items(): print(subject, grade)` itera su ogni coppia materia-voto in un dizionario di pagella.

#### Tipo dizionario (dict) — coppie chiave-valore

Un tipo di dato Python che memorizza una collezione non ordinata di coppie in cui ogni chiave univoca è associata a un valore, permettendo una ricerca veloce dei valori tramite la loro chiave.

**Esempio:** `student = {"name": "Alex", "grade": 8, "score": 95}` memorizza tre informazioni correlate sotto chiavi descrittive.

#### dir() — elenca attributi/metodi di un oggetto

Una funzione built-in che restituisce un elenco ordinato dei nomi di tutti gli attributi e metodi disponibili su un dato oggetto o nell'ambito corrente, utile per esplorare cosa si può fare con un valore.

**Esempio:** `dir("hello")` mostra tutti i metodi delle stringhe come `upper`, `lower`, `split` e molti altri.

#### Direzione: setheading(angle)

Un metodo della turtle che imposta la direzione della turtle a un angolo assoluto in gradi, dove 0 è destra (est), 90 è su (nord), 180 è sinistra (ovest) e 270 è giù (sud).

**Esempio:** `t.setheading(90)` punta la turtle verso l'alto; `t.setheading(0)` la punta verso destra.

#### La divisione restituisce sempre un float in Python 3

Una regola in Python 3 secondo cui l'operatore `/` produce sempre un risultato in virgola mobile anche quando entrambi gli operandi sono interi e il quoziente è un numero intero.

**Esempio:** `10 / 2` vale `5.0`, non `5`; usa `10 // 2` se ti serve il risultato intero `5`.

#### Docstring — documentare le funzioni

Una stringa letterale posta come prima istruzione nel corpo di una funzione, classe o modulo, racchiusa tra virgolette triple, che descrive cosa fa la funzione e può essere letta dalla funzione `help()`.

**Esempio:** `def area(r): """Return the area of a circle with radius r.""" return 3.14 * r * r` include una docstring che descrive lo scopo della funzione.

#### Disegnare un'onda sinusoidale con turtle e math

Un progetto di grafica turtle che combina `math.sin()` con un ciclo per spostare la turtle lungo un percorso ondulato, dimostrando come le funzioni matematiche possano produrre curve visive.

**Esempio:** `for x in range(-300, 300): t.goto(x, 100 * math.sin(math.radians(x)))` disegna un'onda sinusoidale fluida sullo schermo.

#### Disegnare frattali con ricorsione e turtle

Una tecnica di grafica turtle che usa funzioni ricorsive per disegnare pattern autosimili come il triangolo di Sierpiński o il fiocco di neve di Koch, dove ogni livello di ricorsione disegna copie più piccole della stessa forma.

**Esempio:** Una funzione ricorsiva `branch(length)` disegna una linea, poi richiama se stessa due volte con una lunghezza minore a due angoli diversi, costruendo un frattale a forma di albero.

#### Disegnare forme su un canvas

Il processo di usare le funzioni di una libreria di disegno per rendere forme geometriche — come rettangoli, cerchi e linee — specificando programmaticamente coordinate, dimensioni e colori.

**Esempio:** `canvas.fill_style = "red"; canvas.fill_circle(200, 150, 50)` disegna un cerchio rosso pieno centrato in (200, 150) con raggio 50.

#### Disegnare forme: circle(radius), disegnare quadrati/poligoni con i cicli

Tecniche di disegno turtle: `circle(r)` disegna un cerchio di raggio `r`; quadrati e poligoni regolari si disegnano ripetendo `forward()` e `right()` in un ciclo, girando di 360 diviso il numero di lati.

**Esempio:** `for _ in range(6): t.forward(80); t.right(60)` disegna un esagono regolare girando di 60° (360°÷6) sei volte.

#### Dropout — regolarizzazione per prevenire l'overfitting

Uno strato di Keras che azzera casualmente una frazione degli output dei neuroni durante l'addestramento, costringendo la rete a non affidarsi troppo a un singolo neurone e riducendo l'overfitting sui dati di addestramento.

**Esempio:** `Dropout(0.5)` disattiva casualmente il 50% dei neuroni a ogni passo di addestramento, il che aiuta il modello a generalizzare meglio su nuovi dati.

#### Principio DRY (Don't Repeat Yourself)

Un principio di progettazione del software secondo cui ogni informazione o logica dovrebbe esistere in esattamente un solo punto di una codebase, riducendo la duplicazione e rendendo più facile applicare le modifiche in modo coerente.

**Esempio:** Se ti accorgi di copiare e incollare le stesse cinque righe in tre punti, il principio DRY suggerisce di mettere quelle righe in una funzione e chiamarla tre volte invece.

#### Principio DRY e pattern di riutilizzo del codice

La pratica combinata di evitare logica duplicata (Don't Repeat Yourself) e gli specifici pattern di programmazione — come funzioni, cicli e moduli — che permettono di scrivere il codice una volta e richiamarlo molte volte.

**Esempio:** Estrarre la logica ripetuta di verifica della password in una funzione `validate_password(pw)` permette a ogni parte del programma di chiamare un'unica funzione condivisa e manutenibile invece di contenere una propria copia.

#### Catene elif (else-if)

Un modo per verificare più condizioni in sequenza aggiungendo una o più clausole `elif` tra un `if` e un `else` opzionale, così Python verifica ogni condizione in ordine ed esegue solo il primo blocco corrispondente.

**Esempio:** Verificare un voto: `if score >= 90: ... elif score >= 70: ... else: ...` copre in tre rami A, sufficienza e bocciatura.

#### Clausola else in try/except

Un blocco opzionale dopo le clausole `except` che viene eseguito solo se il blocco `try` è terminato senza generare alcuna eccezione, mantenendo separato il codice del percorso di successo da quello di gestione degli errori.

**Esempio:** `try: n = int(input(...))` / `except ValueError: print("Not a number")` / `else: print("Got:", n)` stampa il valore solo quando la conversione è riuscita.

#### Clausola else sui cicli

Un blocco opzionale che segue un ciclo `for` o `while` e viene eseguito solo se il ciclo è terminato normalmente — cioè non è stato interrotto da un'istruzione `break`.

**Esempio:** `for item in inventory:` / `if item == target: break` / `else: print("Not found")` segnala solo quando l'elemento non è mai stato trovato.

#### enumerate() — iterare con indice e valore

Una funzione built-in che avvolge un iterabile e restituisce coppie (indice, valore) durante un ciclo `for`, così puoi accedere contemporaneamente alla posizione di un elemento e all'elemento stesso.

**Esempio:** `for i, name in enumerate(["Alice", "Bob", "Carol"]): print(i, name)` stampa `0 Alice`, `1 Bob`, `2 Carol`.

#### Caratteri di escape (\n, \t, \\, \")

Sequenze speciali di due caratteri che iniziano con un backslash e rappresentano caratteri difficili da digitare direttamente dentro una stringa, come un a capo `\n`, un tab `\t`, un backslash letterale `\\`, o una virgoletta `\"`.

**Esempio:** `print("Line 1\nLine 2")` stampa due righe separate perché `\n` dice a Python di andare a capo.

#### Escape di caratteri speciali con \

La pratica di porre un backslash prima di un metacarattere regex (come `.`, `*`, `+`, `(`, `)`) per farlo corrispondere letteralmente invece di trattarlo come un operatore speciale.

**Esempio:** `r"\."` corrisponde a un punto letterale, mentre `r"."` corrisponde a qualsiasi singolo carattere.

#### Gestione degli eventi: onscreenclick(function)

Un metodo dello schermo turtle che registra una funzione di callback da chiamare ogni volta che l'utente clicca sulla finestra di disegno, passando alla funzione le coordinate x e y del click.

**Esempio:** `screen.onscreenclick(draw_dot)` fa sì che la turtle disegni un punto ovunque l'utente clicchi sul canvas.

#### Modello di programmazione guidata dagli eventi

Un paradigma di programmazione in cui il flusso di esecuzione è determinato dalle azioni dell'utente o dagli eventi di sistema — come click del mouse, pressioni di tasti o timer — invece che da un ordine sequenziale fisso.

**Esempio:** Un programma di grafica turtle che disegna un punto ovunque l'utente clicchi usa la programmazione guidata dagli eventi: l'evento di click attiva la funzione di disegno.

#### except TipoEccezione as e — catturare eccezioni specifiche

Un modo per catturare solo un particolare tipo di eccezione e assegnare l'oggetto eccezione a una variabile, permettendo di stampare un messaggio di errore dettagliato o intraprendere un'azione specifica per quell'errore.

**Esempio:** `except ValueError as e: print("Bad input:", e)` cattura solo `ValueError` e stampa il messaggio dell'eccezione.

#### Gerarchia delle eccezioni — capire la classe base Exception

L'organizzazione ad albero dei tipi di eccezione built-in di Python, dove le classi più generali si trovano più in alto (come `Exception`) e gli errori specifici come `ValueError` e `TypeError` sono sottoclassi più in basso.

**Esempio:** `except Exception as e:` cattura quasi ogni errore perché `ValueError`, `TypeError` e la maggior parte degli altri ereditano tutti da `Exception`.

#### Elevamento a potenza (**)

Un operatore aritmetico che eleva un numero a una potenza, calcolando il risultato della moltiplicazione di una base per se stessa un dato numero di volte.

**Esempio:** `2 ** 8` è uguale a `256`; `9 ** 0.5` è uguale a `3.0`, la radice quadrata di 9.

#### f-string (stringhe letterali formattate)

Una sintassi moderna di Python in cui una `f` prima della virgoletta di apertura permette di valutare espressioni dentro parentesi graffe `{}` e inserirle direttamente nella stringa, rendendo la formattazione concisa e leggibile.

**Esempio:** `name = "Alex"; age = 12; f"Hello, {name}! You are {age} years old."` produce `"Hello, Alex! You are 12 years old."`.

#### Reti feedforward

Un'architettura di rete neurale in cui le informazioni fluiscono in una sola direzione — dallo strato di input attraverso gli strati nascosti fino allo strato di output — senza cicli o connessioni di retroazione.

**Esempio:** Un semplice modello Keras `Sequential` con strati `Dense` è una rete feedforward; l'input entra da un lato ed esce una previsione dall'altro.

#### Modalità dei file: 'r' (lettura), 'w' (scrittura), 'a' (append), 'b' (binario)

Opzioni passate a `open()` che determinano come si accede al file: `'r'` apre in lettura (predefinito); `'w'` apre in scrittura e cancella il contenuto esistente; `'a'` aggiunge in coda al contenuto esistente; `'b'` apre in modalità binaria per file non di testo.

**Esempio:** `open("log.txt", "a")` apre il file così che ogni nuova `write()` aggiunga alla fine senza cancellare le righe precedenti.

#### file.close() — chiudere il file handle

Un metodo dei file che scarica eventuali dati non ancora scritti, rilascia le risorse di sistema occupate dal file aperto e marca l'oggetto file come inutilizzabile; non chiudere i file può causare perdita di dati o fughe di risorse.

**Esempio:** Dopo aver letto o scritto, chiamare `f.close()` assicura che il file venga salvato e rilasciato correttamente.

#### file.read() — leggere l'intero file come stringa

Un metodo dei file che legge l'intero contenuto di un file aperto e lo restituisce come un'unica stringa.

**Esempio:** `content = f.read()` memorizza ogni byte del file come un'unica lunga stringa in `content`.

#### file.readline() — leggere una riga alla volta

Un metodo dei file che legge e restituisce la riga successiva di un file aperto come stringa, facendo avanzare il cursore interno del file; restituisce una stringa vuota quando viene raggiunta la fine del file.

**Esempio:** Chiamare ripetutamente `f.readline()` restituisce ogni riga una alla volta finché il file non è esaurito.

#### file.readlines() — leggere tutte le righe in una lista

Un metodo dei file che legge tutte le righe di un file aperto e le restituisce come una lista di stringhe, dove ogni stringa termina con un carattere di a capo `\n`.

**Esempio:** `lines = f.readlines()` restituisce una lista come `["Line 1\n", "Line 2\n", "Line 3\n"]`.

#### file.write() — scrivere una stringa su file

Un metodo dei file che scrive una stringa in un file aperto alla posizione attuale del cursore; non aggiunge automaticamente un a capo, quindi devi includere `\n` esplicitamente se necessario.

**Esempio:** `f.write("Hello, world!\n")` scrive il testo seguito da un a capo nel file.

#### Riempimento: begin_fill(), end_fill()

Una coppia di metodi della turtle che insieme coloriscono l'interno di qualsiasi forma disegnata tra di essi: chiama `begin_fill()` prima di disegnare la forma e `end_fill()` dopo, e Python riempie l'area racchiusa con il colore di riempimento attuale.

**Esempio:** `t.fillcolor("green"); t.begin_fill(); draw_triangle(); t.end_fill()` disegna un triangolo verde pieno.

#### filter() — filtrare elementi in base a una condizione

Una funzione built-in che applica una funzione di test a ogni elemento di un iterabile e restituisce un iteratore contenente solo gli elementi per cui il test restituisce `True`.

**Esempio:** `list(filter(lambda x: x > 0, [-1, 2, -3, 4]))` restituisce `[2, 4]`, mantenendo solo i numeri positivi.

#### Clausola finally — si esegue sempre

Un blocco opzionale alla fine di una struttura `try/except` che viene eseguito indipendentemente dal fatto che si sia verificata un'eccezione o meno, comunemente usato per rilasciare risorse come chiudere un file o una connessione di rete.

**Esempio:** `try: f = open("data.txt")` / `finally: f.close()` garantisce che il file venga chiuso anche se si verifica un errore durante la lettura.

#### Strato Flatten — rimodellare per gli strati densi

Uno strato di Keras che rimodella un tensore multidimensionale (come una mappa di caratteristiche di un'immagine 2D) in un vettore monodimensionale, facendo da ponte tra gli strati convoluzionali e gli strati densi completamente connessi.

**Esempio:** Dopo gli strati `Conv2D` e `MaxPooling2D`, uno strato `Flatten()` converte la griglia 2D di caratteristiche in una lista piatta che gli strati `Dense` possono elaborare.

#### float() — conversione a float

Una funzione built-in che converte un intero o una stringa numerica in un numero in virgola mobile con un punto decimale.

**Esempio:** `float("3.14")` restituisce `3.14`; `float(5)` restituisce `5.0`.

#### Float (float) — numeri decimali

Un tipo di dato Python che rappresenta numeri con un punto decimale, memorizzato in un formato che consente un ampio intervallo di valori ma può introdurre piccole differenze di arrotondamento in alcuni calcoli.

**Esempio:** `3.14`, `-0.5` e `2.0` sono float; `1/3` restituisce `0.3333333333333333` invece della frazione esatta.

#### Ciclo for con range()

Un pattern comune che usa `range()` per generare una sequenza di interi e ripete un blocco di codice per ogni intero, fornendo un modo semplice per ciclare un numero specifico di volte.

**Esempio:** `for i in range(5): print(i)` stampa `0`, `1`, `2`, `3` e `4`.

#### Ciclo for — iterare su una sequenza

Un'istruzione di controllo del flusso che ripete un blocco di codice una volta per ogni elemento di una sequenza — come una lista, una stringa o un range — passando automaticamente all'elemento successivo dopo ogni ripetizione.

**Esempio:** `for color in ["red", "green", "blue"]: print(color)` stampa ogni colore su una riga propria.

#### from ... import * — importare tutto (usare con parsimonia)

Un modo per importare tutti i nomi pubblici di un modulo direttamente nel namespace corrente in una sola volta; generalmente sconsigliato perché può creare conflitti di nomi e rende difficile capire da dove provenga un nome.

**Esempio:** `from math import *` permette di scrivere `sqrt(4)` direttamente, ma potrebbe sovrascrivere una variabile che avevi chiamato `sqrt` in precedenza.

#### from ... import ... — importare nomi specifici

Una variante dell'istruzione `import` che carica solo i nomi specificati da un modulo direttamente nel namespace corrente, così possono essere usati senza il prefisso del nome del modulo.

**Esempio:** `from math import sqrt, pi` permette di scrivere `sqrt(16)` e `pi` invece di `math.sqrt(16)` e `math.pi`.

#### Frozenset (insiemi immutabili)

Una variante del tipo di dato insieme il cui contenuto non può essere cambiato dopo la creazione, rendendo i frozenset hashabili e utilizzabili come chiavi di dizionario o elementi di altri insiemi.

**Esempio:** `fs = frozenset([1, 2, 3])` crea un insieme immutabile; provare `fs.add(4)` genera un `AttributeError`.

#### Parametri di funzione (posizionali)

Variabili elencate tra le parentesi di un'istruzione `def` che ricevono i valori passati quando la funzione viene chiamata, abbinati in base alla loro posizione nell'elenco degli argomenti.

**Esempio:** In `def add(a, b): return a + b`, chiamare `add(3, 5)` assegna `3` ad `a` e `5` a `b` in base alla posizione.

#### Funzioni che restituiscono None implicitamente

Il comportamento delle funzioni Python che terminano l'esecuzione senza un'istruzione `return`, restituendo automaticamente il valore speciale `None` a qualsiasi codice che le abbia chiamate.

**Esempio:** `def say_hi(): print("Hi")` non ha `return`, quindi `x = say_hi()` memorizza `None` in `x` anche se "Hi" è stato stampato.

#### Le funzioni senza return restituiscono None

Una regola in Python secondo cui qualsiasi funzione che raggiunge la fine del proprio corpo senza eseguire un'istruzione `return` restituisce automaticamente il valore `None` a chi l'ha chiamata.

**Esempio:** `def greet(): print("Hi")` restituisce `None`; `result = greet()` memorizza `None` in `result` anche se "Hi" è stato stampato.

#### Metodo .get() — accesso sicuro a una chiave con valore predefinito

Un metodo dei dizionari che restituisce il valore di una chiave specificata se la chiave esiste, o un valore predefinito (come `None` o un valore di riserva specificato) se la chiave non è presente, senza generare un errore.

**Esempio:** `student.get("score", 0)` restituisce il punteggio se esiste o `0` se la chiave `"score"` non è mai stata aggiunta.

#### Parola chiave global — accedere a una variabile globale dentro una funzione

Una dichiarazione dentro una funzione che dice a Python che un particolare nome di variabile si riferisce alla variabile di ambito globale invece di crearne una nuova locale, permettendo alla funzione di leggere e modificare il valore globale.

**Esempio:** `def add_point(): global score; score += 1` modifica la variabile globale `score` invece di crearne una copia locale.

#### Ambito globale — variabili a livello di modulo

L'area di un programma al di fuori di tutte le funzioni dove le variabili possono essere accedute da qualsiasi punto dello stesso file, incluso dentro le funzioni che vi fanno riferimento (ma senza riassegnarle senza la parola chiave `global`).

**Esempio:** `MAX_SIZE = 100` definita in cima a un file è una variabile globale leggibile dentro qualsiasi funzione di quel file.

#### Grafo — nodi e archi

Una struttura dati composta da un insieme di nodi (detti anche vertici) che rappresentano entità e archi che collegano coppie di nodi, usata per modellare relazioni come amicizie, strade o reti di computer.

**Esempio:** Una rete sociale è un grafo in cui ogni persona è un nodo e ogni amicizia è un arco che collega due nodi.

#### help() — mostrare la documentazione

Una funzione built-in che stampa la docstring e le informazioni d'uso per una funzione, modulo, classe o metodo, fornendo un riferimento rapido senza uscire dalla shell Python.

**Esempio:** `help(str.split)` mostra una spiegazione di come funziona il metodo `.split()`, inclusi i suoi parametri.

#### Valori di colore esadecimali (#FA057F)

Un modo di specificare un colore come un numero esadecimale a sei cifre preceduto da `#`, dove le prime due cifre impostano l'intensità del rosso, le due centrali il verde e le ultime due il blu, ciascuna compresa tra `00` (nessuno) e `FF` (massimo).

**Esempio:** `"#FF0000"` è rosso puro; `"#00FF00"` è verde puro; `"#FA057F"` è un rosa acceso usato in strumenti di design e pagine web.

#### Nascondere/mostrare la turtle: hideturtle(), showturtle()

Metodi della turtle che controllano se il cursore turtle è visibile sullo schermo: `hideturtle()` lo rende invisibile mentre continua a disegnare; `showturtle()` lo rende di nuovo visibile.

**Esempio:** Chiamare `t.hideturtle()` prima di un disegno complesso lo fa apparire più velocemente perché lo schermo non deve ridisegnare il cursore a ogni passo.

#### Istruzione if

Un'istruzione di controllo del flusso che esegue un blocco di codice solo quando una condizione specificata risulta `True`, permettendo ai programmi di prendere decisioni.

**Esempio:** `if score >= 60: print("You passed!")` stampa il messaggio solo quando il punteggio è 60 o superiore.

#### Blocco if...else

Una struttura di controllo del flusso che esegue un blocco di codice quando una condizione è `True` e un blocco diverso quando è `False`, garantendo che venga sempre eseguito esattamente uno dei due percorsi.

**Esempio:** `if temperature > 30: print("Hot day")` / `else: print("Nice day")` stampa esattamente un messaggio in base alla temperatura.

#### Image.open(path) — aprire un'immagine

Una funzione di Pillow che apre un file immagine da un percorso dato e restituisce un oggetto Image che puoi ispezionare, modificare e salvare.

**Esempio:** `img = Image.open("photo.jpg")` carica l'immagine così puoi chiamare `img.size` per ottenerne le dimensioni.

#### image.show() — mostrare un'immagine

Un metodo di Pillow che apre l'immagine nel visualizzatore di immagini predefinito del sistema operativo, utile per controllare rapidamente come appare un'immagine durante lo sviluppo.

**Esempio:** `img.show()` apre l'immagine in Preview su Mac o Foto su Windows senza salvare un file separato.

#### import ... as ... — assegnare un alias a un modulo

Un modo per importare un modulo con un nome più breve o più comodo, così scrivi quell'alias invece del nome completo del modulo in tutto il codice.

**Esempio:** `import numpy as np` permette di scrivere `np.array([1, 2, 3])` invece di `numpy.array([1, 2, 3])`.

#### import matplotlib.pyplot as plt

Il modo standard per importare il sotto-modulo di plotting di matplotlib, assegnandogli l'alias breve `plt` così puoi chiamare `plt.plot()`, `plt.show()` e altre funzioni in modo conciso.

**Esempio:** `import matplotlib.pyplot as plt; plt.plot([1, 2, 3], [4, 1, 7]); plt.show()` crea e mostra un semplice grafico a linee.

#### import numpy as np

Il modo standard per importare NumPy, usando l'alias `np` così che tutte le funzioni di NumPy possano essere chiamate con il prefisso più breve, seguendo una convenzione Python quasi universale.

**Esempio:** Dopo `import numpy as np`, scrivi `np.zeros(5)` invece di `numpy.zeros(5)` in tutto il codice.

#### Istruzione import

Un'istruzione che carica un modulo (un file di codice Python) nel programma corrente, rendendo disponibili le funzioni, le classi e le variabili del modulo sotto il nome del modulo stesso.

**Esempio:** `import math` carica il modulo math così puoi chiamare `math.sqrt(16)` per ottenere `4.0`.

#### import turtle

L'istruzione che carica il modulo di grafica turtle integrato in Python, rendendo disponibili tutte le funzioni e classi di disegno turtle per creare programmi visivi.

**Esempio:** `import turtle` è sempre la prima riga in un programma turtle; dopo, puoi creare un oggetto `turtle.Turtle()` e iniziare a disegnare.

#### Importare il modulo re

Il passaggio di scrivere `import re` all'inizio di un file Python per caricare il modulo delle espressioni regolari e rendere disponibili le sue funzioni — come `re.search()`, `re.findall()` e `re.sub()`.

**Esempio:** Dopo `import re`, puoi chiamare `re.findall(r"\w+", sentence)` per estrarre tutte le parole da una frase.

#### L'indentazione come sintassi (regole sugli spazi bianchi)

La regola in Python per cui gli spazi o i tab all'inizio di una riga determinano a quale blocco di codice appartiene un'istruzione, rendendo l'indentazione una parte obbligatoria del linguaggio e non solo una scelta di stile.

**Esempio:** Il corpo di un'istruzione `if` deve essere indentato di quattro spazi; se non lo è, Python genera un `IndentationError`.

#### Cicli infiniti e come evitarli

Un ciclo la cui condizione non diventa mai `False`, facendolo girare per sempre; si evita assicurandosi che la variabile del ciclo cambi a ogni iterazione o includendo un'istruzione `break` che prima o poi si attiva.

**Esempio:** `while True: ...` è intenzionalmente infinito e deve contenere un `break`; dimenticare di scrivere `count += 1` dentro `while count < 10:` crea anch'esso un ciclo infinito accidentale.

#### Ereditarietà — nozioni di base

Una funzionalità della programmazione orientata agli oggetti in cui una nuova classe (figlia o sottoclasse) viene creata estendendo una classe esistente (genitore o superclasse), ottenendo automaticamente tutti gli attributi e i metodi del genitore.

**Esempio:** Una classe `Cat` che eredita da una classe `Animal` ha automaticamente l'attributo `name` e il metodo `eat()` di `Animal` senza doverli ridefinire.

#### __init__() — metodo costruttore

Un metodo speciale in una classe Python che viene chiamato automaticamente quando viene creato un nuovo oggetto, usato per impostare i valori iniziali degli attributi dell'oggetto.

**Esempio:** `def __init__(self, name, age): self.name = name; self.age = age` viene eseguito automaticamente quando scrivi `Dog("Buddy", 3)`.

#### Nozioni di base sulla validazione dell'input

La pratica di verificare che il valore inserito da un utente soddisfi i requisiti attesi — come essere un numero, rientrare in un certo intervallo o non essere vuoto — prima di usarlo nei calcoli.

**Esempio:** Dopo aver chiamato `input()`, potresti controllare `if response.isdigit()` prima di convertire con `int()` per evitare un crash se l'utente digita una lettera.

#### Funzione input() — leggere testo dall'utente

Una funzione built-in che mette in pausa il programma, aspetta che l'utente digiti qualcosa e prema Invio, e restituisce il testo digitato come stringa.

**Esempio:** `name = input()` memorizza qualsiasi cosa l'utente digiti nella variabile `name`.

#### input() — leggere l'input dell'utente

Una funzione built-in di Python che mette in pausa l'esecuzione del programma, mostra una stringa di prompt opzionale, aspetta che l'utente digiti una riga di testo e prema Invio, poi restituisce quel testo come stringa.

**Esempio:** `name = input("Enter your name: ")` memorizza in `name` qualsiasi cosa l'utente digiti.

#### Installare Python localmente

Il processo di scaricare l'interprete Python da python.org e configurarlo sul proprio computer così da poter eseguire programmi Python senza bisogno di una connessione internet o di uno strumento basato sul web.

#### int() — conversione a intero

Una funzione built-in che converte un valore — come un float o una stringa di cifre — in un intero, troncando qualsiasi parte decimale per i float e generando un `ValueError` se la stringa non è un numero valido.

**Esempio:** `int("42")` restituisce l'intero `42`; `int(3.9)` restituisce `3` troncando (non arrotondando) il decimale.

#### int(), float(), str(), bool() — conversioni di tipo

Quattro funzioni built-in che convertono un valore da un tipo di dato a un altro: `int()` in numero intero, `float()` in decimale, `str()` in testo, e `bool()` in `True` o `False`.

**Esempio:** `int("5") + 3` dà `8`; `str(100)` dà `"100"` per l'uso nella concatenazione di stringhe.

#### Divisione intera (//)

Un operatore aritmetico che divide due numeri e arrotonda il risultato per difetto al numero intero più vicino, scartando qualsiasi resto decimale.

**Esempio:** `17 // 5` dà `3` perché 5 entra in 17 tre volte intere con 2 di resto.

#### Interi (int) — numeri interi, positivi e negativi

Un tipo di dato Python che rappresenta numeri interi senza punto decimale, che possono essere positivi, negativi o zero, e supporta operazioni aritmetiche esatte senza arrotondamenti.

**Esempio:** `3`, `-17` e `0` sono tutti interi; puoi calcolare `7 // 2` per ottenere l'intero `3` senza mantenere alcun resto.

#### ipycanvas — disegno su canvas in Jupyter

Una libreria Python per i Jupyter notebook che avvolge l'API Canvas HTML5, permettendo di disegnare forme, immagini e testo programmaticamente dentro una cella del notebook.

**Esempio:** `from ipycanvas import Canvas; c = Canvas(width=400, height=300); c.fill_rect(10, 10, 100, 50)` disegna un rettangolo in una cella di un Jupyter notebook.

#### isinstance() — verificare se un oggetto è un'istanza di un tipo

Una funzione built-in che restituisce `True` se un dato oggetto è un'istanza della classe specificata o di una delle sue sottoclassi, e `False` altrimenti, fornendo un controllo di tipo più sicuro rispetto a `type() ==`.

**Esempio:** `isinstance(42, int)` restituisce `True`; `isinstance("hello", int)` restituisce `False`.

#### Iterare su un dizionario

Il processo di usare un ciclo `for` per visitare ogni chiave (per impostazione predefinita), o ogni valore o coppia chiave-valore quando si usano `.values()` o `.items()`, per elaborare tutte le voci di un dizionario.

**Esempio:** `for key in d: print(key, d[key])` stampa ogni chiave e il suo valore associato dal dizionario `d`.

#### Iterare su una lista con for

Il pattern comune di usare un ciclo `for` per visitare ogni elemento di una lista uno alla volta, elaborando o stampando ogni elemento in sequenza.

**Esempio:** `for score in scores: print(score)` stampa ogni punteggio della lista su una riga propria.

#### Iterare sulle righe di un file con for

Il pattern comune di usare un ciclo `for` direttamente su un oggetto file per leggere una riga alla volta senza caricare l'intero file in memoria, cosa efficiente per file di grandi dimensioni.

**Esempio:** `with open("words.txt") as f:` / `for line in f: print(line.strip())` stampa ogni riga senza l'a capo finale.

#### Jupyter Notebook — ambiente computazionale interattivo

Uno strumento basato sul web che permette di mischiare codice Python eseguibile, spiegazioni testuali e grafici in un unico documento fatto di celle, così puoi raccontare una storia con i tuoi dati e il tuo codice insieme.

**Esempio:** Un data scientist scrive una cella di intestazione che spiega un grafico, poi una cella di codice che disegna il grafico, ed entrambe appaiono insieme nello stesso notebook.

#### JupyterLab — ambiente Jupyter avanzato

Una versione aggiornata e più potente dei Jupyter Notebook che aggiunge un browser di file, più schede e una finestra di terminale accanto ai notebook in un unico spazio di lavoro basato sul browser.

#### Panoramica sulla libreria keras

Una libreria Python di alto livello per costruire e addestrare reti neurali, progettata per rendere il deep learning accessibile fornendo blocchi costitutivi semplici e leggibili per definire architetture di modelli.

**Esempio:** `from tensorflow import keras` dà accesso a strumenti per costruire classificatori di immagini, analizzatori di testo e altri modelli di IA in poche righe di codice.

#### Gestori di eventi da tastiera (turtle onkey)

Una funzione di turtle che registra una funzione di callback da chiamare ogni volta che viene premuto un tasto specifico, abilitando programmi interattivi controllati da tastiera.

**Esempio:** `screen.onkey(move_up, "Up")` chiama `move_up()` ogni volta che l'utente preme la freccia Su.

#### Argomenti con nome (keyword arguments)

Un modo di chiamare una funzione nominando esplicitamente ogni parametro e il suo valore, così gli argomenti possono essere passati in qualsiasi ordine indipendentemente dalla loro posizione nella definizione della funzione.

**Esempio:** `draw_box(width=100, height=50, color="blue")` rende chiaro cosa significa ogni valore e permette qualsiasi ordine.

#### Funzioni lambda (funzioni anonime)

Un modo per definire una piccola funzione a una sola espressione senza nome usando la parola chiave `lambda`, spesso usata per operazioni brevi passate come argomenti ad altre funzioni.

**Esempio:** `double = lambda x: x * 2` crea una funzione senza nome memorizzata in `double`; `double(5)` restituisce `10`.

#### len() — lunghezza di una sequenza

Una funzione built-in di Python che restituisce il numero di elementi in qualsiasi sequenza o collezione, incluse stringhe (caratteri), liste (elementi), tuple, dizionari (chiavi) e insiemi.

**Esempio:** `len("hello")` restituisce `5`; `len([1, 2, 3])` restituisce `3`; `len({})` restituisce `0`.

#### len() — numero di elementi in una lista

Una funzione built-in che restituisce un intero pari al numero di elementi attualmente memorizzati in una lista (o qualsiasi sequenza).

**Esempio:** `len([10, 20, 30])` restituisce `3`; `len([])` restituisce `0` per una lista vuota.

#### Comprehension di liste

Una sintassi concisa su una riga per creare una nuova lista applicando un'espressione a ogni elemento di un iterabile, opzionalmente filtrata da una condizione, tutto dentro parentesi quadre.

**Esempio:** `[x * 2 for x in range(5)]` produce `[0, 2, 4, 6, 8]`; `[x for x in scores if x >= 60]` mantiene solo i punteggi sufficienti.

#### Concatenazione e ripetizione di liste

La possibilità di unire due liste usando `+` per creare una nuova lista combinata, o di ripetere gli elementi di una lista usando `*` un numero specificato di volte.

**Esempio:** `[1, 2] + [3, 4]` produce `[1, 2, 3, 4]`; `["go"] * 3` produce `["go", "go", "go"]`.

#### Indicizzazione delle liste (basata su 0, indici negativi)

Il metodo per accedere a un singolo elemento di una lista tramite la sua posizione, dove il primo elemento è all'indice `0`; gli indici negativi contano dalla fine, con `-1` come ultimo elemento.

**Esempio:** Per `colors = ["red", "green", "blue"]`, `colors[0]` è `"red"` e `colors[-1]` è `"blue"`.

#### I metodi delle liste come esempio di OOP

Un'osservazione per cui le liste Python sono oggetti, e chiamare metodi come `.append()` o `.sort()` su di esse è un esempio concreto di programmazione orientata agli oggetti in cui dati e comportamento sono raggruppati insieme.

**Esempio:** `my_list.append(5)` è OOP: `my_list` è l'oggetto e `.append()` è un metodo che modifica quella specifica lista.

#### Metodi delle liste: .append(), .insert(), .extend()

Metodi built-in delle liste che aggiungono elementi: `.append(item)` aggiunge un elemento alla fine; `.insert(index, item)` aggiunge un elemento in una posizione specifica; `.extend(iterable)` aggiunge tutti gli elementi di un altro iterabile alla fine.

**Esempio:** `fruits.append("mango")` aggiunge `"mango"` alla fine; `fruits.insert(0, "apple")` mette `"apple"` all'inizio.

#### Metodi delle liste: .index(), .count()

Metodi built-in delle liste che effettuano ricerche: `.index(value)` restituisce l'indice della prima occorrenza di un valore (genera `ValueError` se non trovato); `.count(value)` restituisce quante volte un valore compare.

**Esempio:** `["a","b","c"].index("b")` restituisce `1`; `[1,2,2,3].count(2)` restituisce `2`.

#### Metodi delle liste: .remove(), .pop(), .clear()

Metodi built-in delle liste che rimuovono elementi: `.remove(value)` elimina la prima occorrenza di un valore; `.pop(index)` rimuove e restituisce l'elemento all'indice dato (l'ultimo se non viene fornito un indice); `.clear()` rimuove tutti gli elementi.

**Esempio:** `scores.pop()` rimuove e restituisce l'ultimo punteggio; `names.remove("Alex")` elimina il primo `"Alex"` trovato.

#### Metodi delle liste: .sort(), .reverse(), .copy()

Metodi built-in delle liste che riordinano o duplicano una lista: `.sort()` ordina gli elementi sul posto (crescente per impostazione predefinita); `.reverse()` inverte l'ordine sul posto; `.copy()` restituisce una nuova lista con gli stessi elementi.

**Esempio:** `scores.sort()` riordina la lista dal più basso al più alto; `steps.reverse()` capovolge l'ordine dei passi.

#### Slicing delle liste

L'operazione di estrarre una sotto-lista da una lista specificando un indice di inizio, un indice di fine (esclusivo) e un passo opzionale, usando la stessa sintassi `[inizio:fine:passo]` dello slicing delle stringhe.

**Esempio:** `numbers[1:4]` restituisce gli elementi agli indici 1, 2 e 3; `numbers[::-1]` restituisce una copia invertita dell'intera lista.

#### Tipo lista (list) — collezione ordinata e modificabile

Un tipo di dato Python che memorizza una sequenza ordinata di elementi di qualsiasi tipo; le liste possono essere modificate dopo la creazione aggiungendo, rimuovendo o sostituendo elementi.

**Esempio:** `fruits = ["apple", "banana", "cherry"]` crea una lista di tre stringhe che può essere modificata in seguito.

#### list(), tuple(), set(), dict() — costruttori di collezioni

Funzioni built-in che creano una nuova collezione del tipo specificato, opzionalmente a partire da un iterabile esistente; `dict()` può anche accettare argomenti con nome per impostare le coppie chiave-valore iniziali.

**Esempio:** `list(range(5))` produce `[0, 1, 2, 3, 4]`; `set("hello")` produce `{'h', 'e', 'l', 'o'}`.

#### Programmazione letterata con Jupyter

Uno stile di scrittura di programmi nei Jupyter notebook in cui le celle di codice sono alternate a celle di testo narrativo, così un notebook si legge come un documento illustrato che per di più è anche eseguibile.

**Esempio:** Un Jupyter notebook potrebbe avere una cella markdown che spiega una formula statistica, seguita immediatamente da una cella di codice che la implementa e la verifica.

#### Ambito locale — variabili dentro le funzioni

L'area di un programma in cui una variabile è accessibile; le variabili create dentro una funzione esistono solo per la durata di quella chiamata e non possono essere viste o usate dal codice al di fuori della funzione.

**Esempio:** La variabile `total` creata dentro `def calculate():` scompare quando la funzione termina e non può essere accessibile dal resto del programma.

#### Operatori logici: and, or, not

Operatori che combinano o invertono valori booleani: `and` è `True` solo quando entrambi i lati sono `True`; `or` è `True` quando almeno un lato è `True`; `not` inverte `True` in `False` e viceversa.

**Esempio:** `age >= 10 and age <= 13` è `True` solo quando l'età è compresa tra 10 e 13 inclusi.

#### Variabile contatore del ciclo (i, j)

Una variabile — comunemente chiamata `i` o `j` per convenzione — che tiene traccia di quale iterazione di un ciclo è in corso, tipicamente usata come variabile di ciclo nei cicli `for` con `range()`.

**Esempio:** `for i in range(10): print(i)` usa `i` come contatore che va da `0` a `9`.

#### Funzioni di perdita (loss): categorical_crossentropy

Una funzione di perdita comunemente usata per problemi di classificazione multi-classe che misura quanto la distribuzione di probabilità prevista dal modello differisca da quella vera codificata one-hot.

**Esempio:** Se il modello prevede `[0.1, 0.8, 0.1]` per un'immagine che è realmente della classe 1 (`[0, 1, 0]`), la categorical crossentropy dà una perdita bassa perché la previsione era per lo più corretta.

#### Reti LSTM — panoramica

Un tipo di rete neurale ricorrente con celle di memoria speciali e meccanismi di gating che la aiutano a imparare dipendenze a lungo raggio nelle sequenze senza perdere le informazioni precedenti.

**Esempio:** Una LSTM addestrata su testo può generare frasi coerenti perché "ricorda" parole di molti passi precedenti nella sequenza.

#### Panoramica sul machine learning — supervisionato vs non supervisionato

Un'introduzione al ramo dell'intelligenza artificiale in cui i computer imparano pattern dai dati: l'apprendimento supervisionato si addestra su esempi etichettati (input → risposta corretta); l'apprendimento non supervisionato trova pattern nascosti in dati non etichettati.

**Esempio:** Addestrare un modello a classificare foto di gatti e cani usando immagini etichettate è supervisionato; raggruppare i clienti in segmenti senza etichette è non supervisionato.

#### map() e filter() — nozioni di base di programmazione funzionale

Due funzioni di ordine superiore che applicano una funzione a una collezione senza cicli espliciti, seguendo uno stile di programmazione funzionale: `map()` trasforma ogni elemento; `filter()` seleziona gli elementi che superano un test.

**Esempio:** `list(map(str.upper, ["a","b","c"]))` dà `["A","B","C"]`; `list(filter(lambda x: x>0, [-1,2,-3,4]))` dà `[2,4]`.

#### map() — applicare una funzione a ogni elemento

Una funzione built-in che applica una data funzione a ogni elemento di un iterabile e restituisce un iteratore dei risultati, evitando la necessità di scrivere un ciclo esplicito per semplici trasformazioni.

**Esempio:** `list(map(int, ["1", "2", "3"]))` converte una lista di stringhe in `[1, 2, 3]`.

#### Istruzione match/case (Python 3.10+, pattern matching strutturale)

Un'istruzione di controllo del flusso introdotta in Python 3.10 che confronta un valore con una serie di pattern ed esegue il blocco appartenente al primo pattern corrispondente, simile a uno switch in altri linguaggi.

**Esempio:** `match command:` / `case "quit": exit()` / `case "help": show_help()` instrada il flusso del programma in base al comando dell'utente.

#### math — funzioni matematiche

Un modulo della libreria standard che fornisce funzioni e costanti matematiche, come radice quadrata, funzioni trigonometriche, logaritmi e il valore di pi greco, da usare nei calcoli.

**Esempio:** `import math; math.sqrt(144)` restituisce `12.0`.

#### math.radians() — da gradi a radianti

Una funzione del modulo `math` che converte un angolo da gradi a radianti, l'unità richiesta da `math.sin()`, `math.cos()` e altre funzioni trigonometriche.

**Esempio:** `math.radians(180)` restituisce `3.141592...` (π), perché 180 gradi equivalgono a π radianti.

#### math.sin(), math.cos(), math.pi

Funzioni e una costante del modulo `math`: `sin(x)` e `cos(x)` restituiscono il seno e il coseno dell'angolo `x` in radianti; `math.pi` è la costante π ≈ 3,14159.

**Esempio:** `math.sin(math.pi / 2)` restituisce `1.0` perché il seno di 90 gradi (π/2 radianti) è 1.

#### math.sqrt(), math.floor(), math.ceil()

Tre funzioni del modulo `math`: `sqrt(x)` restituisce la radice quadrata di `x`; `floor(x)` arrotonda per difetto all'intero più vicino; `ceil(x)` arrotonda per eccesso all'intero più vicino.

**Esempio:** `math.floor(3.9)` restituisce `3`; `math.ceil(3.1)` restituisce `4`; `math.sqrt(25)` restituisce `5.0`.

#### Panoramica sulla libreria matplotlib

Una popolare libreria Python di terze parti per creare grafici statici, animati e interattivi, ampiamente usata nella data science e nel calcolo scientifico per visualizzare i dati.

**Esempio:** `import matplotlib.pyplot as plt` dà accesso a funzioni per creare grafici a linee, a barre, istogrammi e a dispersione.

#### max(), min() — trovare massimo/minimo

Funzioni built-in che restituiscono il valore più grande o più piccolo da una collezione di elementi o da più argomenti; accettano anche una funzione `key` per personalizzare il confronto.

**Esempio:** `max([3, 7, 1, 9])` restituisce `9`; `min("apple", "banana", "cherry")` restituisce `"apple"` (il primo in ordine alfabetico).

#### MaxPooling2D — strati di pooling

Uno strato di Keras che riduce la dimensione spaziale di una mappa di caratteristiche prendendo il valore massimo all'interno di ogni piccola finestra, rendendo la rappresentazione più piccola e più robusta a piccoli spostamenti.

**Esempio:** `MaxPooling2D((2, 2))` dimezza sia la larghezza che l'altezza della mappa di caratteristiche mantenendo solo il valore più grande in ogni blocco 2×2.

#### Nomi significativi per variabili e funzioni

La pratica di scegliere nomi che descrivono chiaramente lo scopo di una variabile o l'azione di una funzione, rendendo il codice autoesplicativo e più facile da leggere senza commenti aggiuntivi.

**Esempio:** `calculate_total_price()` è un nome di funzione significativo; `f()` non lo è — il lettore non può capire cosa faccia `f()` senza leggerne il corpo.

#### Nomi di variabili significativi

La pratica di scegliere nomi di variabili che descrivono chiaramente i dati che contengono, rendendo i programmi più facili da leggere e correggere rispetto all'uso di nomi di una sola lettera o vaghi.

**Esempio:** Usare `student_count` invece di `x` dice immediatamente al lettore che la variabile memorizza il numero di studenti.

#### Metodi — funzioni che appartengono a un oggetto

Funzioni definite dentro una classe che operano sui dati propri dell'oggetto; vengono chiamate usando la notazione a punto e ricevono automaticamente l'oggetto stesso come primo argomento.

**Esempio:** `turtle.forward(100)` chiama il metodo `forward` su un oggetto turtle, spostando in avanti di 100 unità quella specifica turtle.

#### Metriche: accuracy

Una misura delle prestazioni per i modelli di classificazione che riporta la frazione di previsioni che corrispondevano esattamente alle etichette vere, espressa come decimale o percentuale.

**Esempio:** Un'accuracy di `0.97` significa che il modello ha classificato correttamente 97 esempi su ogni 100 di test.

#### Dataset MNIST — riconoscimento di cifre scritte a mano

Un classico dataset di riferimento di 70.000 immagini in scala di grigi di cifre scritte a mano (0–9), ciascuna di 28×28 pixel, ampiamente usato per imparare e testare modelli di classificazione delle immagini.

**Esempio:** Addestrare una rete neurale su MNIST per identificare correttamente le cifre scritte a mano è uno degli esercizi introduttivi di machine learning più comuni.

#### mobilechelonian — grafica turtle in Jupyter

Una libreria Python che fornisce un ambiente di grafica turtle eseguibile dentro una cella di Jupyter notebook, rendendo accessibile il disegno in stile turtle senza una finestra grafica separata.

**Esempio:** `from mobilechelonian import Turtle; t = Turtle(); t.forward(100); t.right(90)` disegna dentro una cella Jupyter.

#### model.compile() — funzione di perdita, ottimizzatore, metriche

Un metodo di Keras che configura il modello per l'addestramento specificando come misurare l'errore (funzione di perdita), come aggiornare i pesi (ottimizzatore) e quali statistiche tracciare (metriche).

**Esempio:** `model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])` prepara il modello a minimizzare l'errore di classificazione.

#### model.evaluate() — verificare l'accuracy

Un metodo di Keras che misura le prestazioni del modello su un dataset di test separato che non è stato usato durante l'addestramento, restituendo la perdita e qualsiasi metrica tracciata.

**Esempio:** `loss, acc = model.evaluate(x_test, y_test)` dà l'accuracy finale su dati che il modello non ha mai visto.

#### model.fit() — addestrare il modello

Un metodo di Keras che addestra il modello alimentandolo con batch di dati di addestramento, calcolando la perdita e aggiornando i pesi ripetutamente per un numero specificato di epoche.

**Esempio:** `model.fit(x_train, y_train, epochs=10, batch_size=32)` addestra il modello per 10 passaggi attraverso i dati di addestramento.

#### model.predict() — fare previsioni

Un metodo di Keras che passa nuovi dati di input attraverso il modello addestrato e ne restituisce l'output, come probabilità di classe o valori di regressione, per ogni campione di input.

**Esempio:** `predictions = model.predict(x_new)` restituisce un array di probabilità softmax per ogni immagine in `x_new`.

#### Modularità — suddividere il codice in funzioni

La pratica di suddividere un programma grande in funzioni più piccole e nominate che svolgono ciascuna un compito chiaramente definito, rendendo il programma complessivo più facile da capire, testare e modificare.

**Esempio:** Invece di un unico script lungo, un gioco potrebbe avere funzioni separate: `draw_board()`, `get_player_move()` e `check_winner()`, ciascuna responsabile di un compito.

#### Operatore modulo (%) — resto della divisione

Un operatore aritmetico che restituisce il resto rimanente dopo aver diviso un numero per un altro, utile per verificare se un numero è pari o dispari e per ciclare attraverso intervalli.

**Esempio:** `17 % 5` dà `2` perché 17 diviso 5 fa 3 con un resto di 2; `n % 2 == 0` verifica se `n` è pari.

#### Gestori di eventi di click del mouse (onscreenclick)

Una funzione di turtle che registra una funzione di callback da chiamare automaticamente con le coordinate (x, y) ogni volta che l'utente clicca sulla finestra di disegno.

**Esempio:** `screen.onscreenclick(handle_click)` registra `handle_click` così che ogni click attivi `handle_click(x, y)` con la posizione del click.

#### Movimento: forward(), backward(), left(), right()

Quattro metodi fondamentali della turtle che la spostano e la ruotano: `forward(n)` si sposta di `n` pixel nella direzione attuale; `backward(n)` si sposta all'indietro; `left(angle)` ruota a sinistra di `angle` gradi; `right(angle)` ruota a destra.

**Esempio:** `t.forward(100); t.right(90)` sposta la turtle in avanti e poi la ruota per disegnare un lato e un angolo di un quadrato.

#### Stringhe multiriga (virgolette triple)

Una stringa che si estende su più di una riga, creata racchiudendo il testo con tre virgolette singole `'''` o tre virgolette doppie `"""`, mantenendo tutti gli a capo al suo interno.

**Esempio:** `"""Line one\nLine two\nLine three"""` memorizza tre righe di testo in un'unica variabile stringa.

#### Assegnazione multipla (a, b = 1, 2)

Una funzionalità di Python che assegna valori a più variabili in una singola istruzione abbinando ogni nome a sinistra al valore corrispondente a destra.

**Esempio:** `x, y = 10, 20` imposta `x` a `10` e `y` a `20` contemporaneamente; puoi anche usare `a, b = b, a` per scambiare due valori.

#### Guardia __name__ == "__main__"

Un pattern comune di Python che esegue un blocco di codice solo quando lo script viene eseguito direttamente (non importato come modulo), verificando se la variabile speciale `__name__` è uguale a `"__main__"`.

**Esempio:** `if __name__ == "__main__": main()` impedisce l'esecuzione di `main()` quando un altro file importa il modulo per le sue funzioni.

#### Guardia __name__ == "__main__" per moduli eseguibili

Il pattern di racchiudere il codice di esecuzione principale di uno script Python dentro `if __name__ == "__main__":` così che il codice venga eseguito quando il file viene eseguito direttamente ma venga saltato quando il file è importato come modulo da un altro script.

**Esempio:** Un modulo di supporto `utils.py` con `if __name__ == "__main__": run_tests()` esegue i propri test solo quando lo esegui direttamente, non quando un altro script ne importa le funzioni.

#### Colori con nome (red, green, blue, orange, ecc.)

Nomi di colore predefiniti integrati nella grafica turtle e in molte altre librerie Python che permettono di specificare i colori usando parole inglesi facili da ricordare invece di codici numerici.

**Esempio:** `t.color("tomato")` e `t.color("dodgerblue")` usano colori con nome; turtle supporta oltre 100 di questi nomi tra cui `"lime"`, `"gold"` e `"orchid"`.

#### Dizionari annidati

Un dizionario in cui alcuni o tutti i valori sono a loro volta dizionari, permettendo di memorizzare e accedere a dati gerarchici complessi con più livelli di chiavi.

**Esempio:** `school = {"Alice": {"grade": 8, "score": 90}, "Bob": {"grade": 7, "score": 85}}` memorizza i dati di ogni studente sotto il proprio nome.

#### Istruzioni if annidate

Un'istruzione `if` (o `if...else`) posta dentro il corpo di un'altra istruzione `if`, permettendo ai programmi di verificare una seconda condizione solo dopo che la prima è stata confermata vera.

**Esempio:** `if is_member: if balance >= 10: print("Purchase allowed")` verifica prima l'iscrizione, poi il saldo.

#### Liste annidate (liste di liste)

Una lista che contiene altre liste come suoi elementi, usata per rappresentare dati bidimensionali come griglie, tabelle o matrici.

**Esempio:** `grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` è una griglia 3×3; `grid[1][2]` accede al valore `6`.

#### Cicli annidati

Un ciclo posto dentro il corpo di un altro ciclo, così che per ogni iterazione del ciclo esterno, il ciclo interno esegua tutte le proprie iterazioni.

**Esempio:** Due cicli `for` annidati con variabili `row` e `col` possono visitare ogni cella di una griglia, come le caselle di una scacchiera.

#### None — valore nullo/vuoto, NoneType

Un valore speciale di Python che rappresenta l'assenza intenzionale di qualsiasi valore, appartenente a un proprio tipo chiamato `NoneType`; viene restituito dalle funzioni che non restituiscono esplicitamente nulla.

**Esempio:** Una funzione che stampa un messaggio ma non ha un'istruzione `return` restituisce `None`; verificare `if result is None` controlla se una funzione ha restituito qualcosa di utile.

#### Parola chiave nonlocal — accedere a una variabile dell'ambito racchiudente

Una dichiarazione dentro una funzione annidata (interna) che dice a Python che un nome di variabile si riferisce alla variabile nell'ambito della funzione (esterna) racchiudente più vicina, permettendo alla funzione interna di modificarla.

**Esempio:** Una funzione interna usa `nonlocal counter` per aggiornare una variabile `counter` definita nella funzione esterna che la racchiude.

#### np.argmax() — indice del valore massimo

Una funzione di NumPy che restituisce l'indice del valore più grande in un array, utile per trovare quale categoria ha ricevuto il punteggio più alto nell'output di un modello di machine learning.

**Esempio:** `np.argmax([0.1, 0.8, 0.1])` restituisce `1`, indicando che il secondo elemento (indice 1) ha il valore più alto.

#### np.array() — creare array

Una funzione di NumPy che converte una lista Python (o lista di liste) in un array NumPy, una struttura dati efficiente che supporta operazioni matematiche veloci elemento per elemento.

**Esempio:** `arr = np.array([1, 2, 3, 4]); arr * 3` produce `array([3, 6, 9, 12])` in un solo passaggio.

#### Panoramica sulla libreria numpy

Una potente libreria Python di terze parti che fornisce un tipo di dato array veloce e funzioni matematiche per operare su interi array in una volta sola, costituendo la base della maggior parte del lavoro Python scientifico e di data science.

**Esempio:** `import numpy as np; np.array([1, 2, 3]) * 2` restituisce `array([2, 4, 6])` senza bisogno di un ciclo.

#### Oggetti e classi — panoramica concettuale

Un modello di programmazione in cui dati e azioni correlate sono raggruppati insieme in un'unica unità chiamata oggetto; gli oggetti vengono creati da modelli chiamati classi, che ne definiscono gli attributi (dati) e i metodi (comportamenti).

**Esempio:** Una classe `Dog` potrebbe definire attributi come `name` e `breed` e metodi come `bark()` e `fetch()`, e ogni singolo cane è un oggetto separato creato da quella classe.

#### Funzione open()

Una funzione built-in di Python che apre un file e restituisce un oggetto file tramite cui puoi leggere o scrivere nel file; devi specificare il percorso del file e opzionalmente la modalità.

**Esempio:** `f = open("notes.txt", "r")` apre `notes.txt` in lettura e memorizza l'oggetto file in `f`.

#### Ottimizzatore: Adam

Un popolare algoritmo di ottimizzazione a discesa del gradiente usato per addestrare reti neurali che regola automaticamente il tasso di apprendimento per ogni parametro, combinando i vantaggi del momentum e dei tassi di apprendimento adattivi.

**Esempio:** `optimizer="adam"` in `model.compile()` dice a Keras di usare l'algoritmo Adam, che tipicamente si addestra più velocemente della discesa del gradiente di base.

#### os — interfaccia con il sistema operativo

Un modulo della libreria standard che fornisce funzioni per interagire con il sistema operativo, inclusi il lavoro con file e cartelle, la lettura delle variabili d'ambiente e l'esecuzione di comandi di sistema.

**Esempio:** `import os; os.getcwd()` restituisce il percorso della cartella di lavoro corrente.

#### os.path — operazioni sui percorsi dei file

Un sotto-modulo di `os` che fornisce funzioni per manipolare le stringhe di percorso di file e cartelle in un modo che funziona correttamente su qualsiasi sistema operativo.

**Esempio:** `os.path.exists("data.txt")` restituisce `True` se il file esiste; `os.path.join("folder", "file.txt")` costruisce un percorso che funziona su Windows e Mac.

#### Controllo della penna: penup(), pendown(), pensize()

Metodi della turtle che controllano se la turtle disegna mentre si muove: `penup()` solleva la penna così il movimento non lascia traccia; `pendown()` abbassa la penna così il movimento disegna una linea; `pensize(n)` imposta lo spessore della linea in pixel.

**Esempio:** `t.penup(); t.goto(100, 0); t.pendown()` sposta la turtle senza disegnare, poi riprende a disegnare dalla nuova posizione.

#### Panoramica su PIL (Python Imaging Library) / Pillow

Una libreria Python di terze parti per aprire, modificare e salvare file immagine in molti formati; Pillow è il fork attivamente mantenuto della PIL originale.

**Esempio:** `from PIL import Image` dà accesso a funzioni per aprire un JPEG, ridimensionarlo, convertirlo in scala di grigi e salvare il risultato.

#### pip — installatore di pacchetti Python

Lo strumento standard da riga di comando che scarica e installa librerie Python da internet, rendendo facile aggiungere a Python nuove funzionalità come il web scraping o l'elaborazione delle immagini.

**Esempio:** Eseguire `pip install pillow` nel terminale scarica e installa la libreria immagine Pillow così puoi usarla nei tuoi programmi.

#### Dati dei pixel e array di immagini

La rappresentazione di un'immagine come una griglia bidimensionale in cui ogni cella contiene il valore di colore di un pixel; in Pillow o NumPy, questi dati possono essere letti e modificati come un array 2D o 3D.

**Esempio:** Convertire un'immagine in un array NumPy con `np.array(img)` dà un array 3D in cui ogni pixel è `[red, green, blue]`.

#### Disegnare un'onda sinusoidale (plotting)

Un comune compito introduttivo di visualizzazione dati che genera una lista di valori x, calcola `math.sin()` per ciascuno, e passa entrambe le liste a `plt.plot()` per disegnare una curva ondulata fluida.

**Esempio:** `x = [i/10 for i in range(63)]; y = [math.sin(v) for v in x]; plt.plot(x, y)` disegna un ciclo completo di un'onda sinusoidale.

#### plt.grid() — mostrare le linee della griglia

Una funzione di matplotlib che aggiunge una griglia di linee di riferimento orizzontali e verticali a un grafico, rendendo più facile leggere i valori dei dati dal grafico.

**Esempio:** `plt.grid(True)` aggiunge le linee della griglia; `plt.grid(True, linestyle="--", alpha=0.5)` usa linee tratteggiate semitrasparenti.

#### plt.plot(x, y) — grafico a linee

Una funzione di matplotlib che disegna un grafico a linee che collega i punti dati definiti da liste corrispondenti di valori x e valori y.

**Esempio:** `plt.plot([0, 1, 2, 3], [0, 1, 4, 9])` disegna una linea attraverso i punti (0,0), (1,1), (2,4), (3,9), producendo una curva simile a una parabola.

#### plt.show() — mostrare il grafico

Una funzione di matplotlib che rende tutti i grafici attualmente creati e li mostra in una finestra o in linea in un Jupyter notebook; senza di essa, il grafico viene creato in memoria ma non viene mai mostrato.

**Esempio:** Dopo aver chiamato `plt.plot(...)` e `plt.title(...)`, chiamare `plt.show()` apre la finestra con il grafico completato.

#### plt.title(), plt.xlabel(), plt.ylabel() — etichette

Funzioni di matplotlib che aggiungono un titolo sopra il grafico ed etichette agli assi x e y, rendendo i grafici più facili da interpretare.

**Esempio:** `plt.title("Temperature Over Time"); plt.xlabel("Day"); plt.ylabel("°C")` etichetta gli assi di un grafico della temperatura.

#### Interrogare la posizione: xcor(), ycor(), heading()

Metodi della turtle che riportano lo stato attuale della turtle: `xcor()` restituisce la coordinata x; `ycor()` restituisce la coordinata y; `heading()` restituisce la direzione verso cui è rivolta la turtle in gradi.

**Esempio:** `print(t.xcor(), t.ycor())` stampa la posizione attuale della turtle, utile per il debug o il rilevamento di collisioni.

#### Funzione print()

Una funzione built-in di Python che mostra uno o più valori come testo nella console o nel terminale, terminando con un a capo per impostazione predefinita.

**Esempio:** `print("Hello, world!")` stampa il testo `Hello, world!` sullo schermo.

#### print() — output sulla console

Una funzione built-in di Python che mostra testo o valori nel terminale o nella finestra della console, con caratteri separatore e finale opzionali, rendendo visibile all'utente l'output del programma.

**Esempio:** `print("Score:", score)` mostra `Score: 42` se `score` è `42`; `print("a", "b", sep="-")` mostra `a-b`.

#### Chiedere input all'utente (passando una stringa a input())

La pratica di passare una stringa descrittiva come argomento a `input()` così che l'utente veda un messaggio che spiega cosa deve digitare prima che il programma aspetti il suo input.

**Esempio:** `age = input("How old are you? ")` mostra la domanda e memorizza la risposta, rendendo il programma più amichevole di un cursore vuoto.

#### Funzioni pure vs funzioni con effetti collaterali

Una distinzione tra le funzioni che restituiscono sempre lo stesso output per lo stesso input e non cambiano nulla al di fuori di se stesse (pure), e le funzioni che influenzano lo stato esterno come stampare, scrivere file o modificare variabili globali (effetti collaterali).

**Esempio:** `def double(x): return x * 2` è pura; `def log(x): print(x)` ha un effetto collaterale perché cambia ciò che appare sullo schermo.

#### Differenze tra Python 2 e Python 3

Due versioni principali del linguaggio Python non pienamente compatibili tra loro; Python 3 è lo standard attuale e include miglioramenti come `print()` che è una funzione invece che un'istruzione, e la divisione che restituisce sempre un risultato decimale.

**Esempio:** In Python 2, `print "Hello"` funziona, ma in Python 3 devi scrivere `print("Hello")` con le parentesi.

#### Panoramica sull'interprete Python

Un programma che legge il codice Python un'istruzione alla volta ed esegue immediatamente ciascuna istruzione, traducendo il Python leggibile dagli umani in azioni che il computer può eseguire senza dover compilare prima l'intero programma.

**Esempio:** Quando digiti `print("Hello!")` e premi Invio in una shell Python, l'interprete legge quella riga e mostra subito `Hello!` sullo schermo.

#### Parole chiave di Python (parole riservate)

Parole speciali integrate nel linguaggio Python — come `if`, `for`, `while`, `def`, `return` e `True` — che hanno significati fissi e non possono essere usate come nomi di variabili o funzioni.

**Esempio:** Provare a nominare una variabile `for = 5` causa un `SyntaxError` perché `for` è una parola chiave riservata.

#### Quantificatori: + (uno o più), * (zero o più), ? (opzionale)

Simboli regex posti dopo un carattere o un gruppo per specificare quante volte può ripetersi: `+` richiede almeno un'occorrenza; `*` ne permette zero o più; `?` rende opzionale l'elemento precedente (zero o una).

**Esempio:** `r"\d+"` corrisponde a una o più cifre; `r"colou?r"` corrisponde sia a `"color"` che a `"colour"`.

#### Operazioni sulla coda: enqueue (append()), dequeue (pop(0))

Le due operazioni fondamentali di una coda: enqueue aggiunge un elemento in fondo alla coda (implementato con `.append()`); dequeue rimuove e restituisce l'elemento in testa (implementato con `.pop(0)`).

**Esempio:** `queue = []; queue.append("Alice"); queue.append("Bob"); queue.pop(0)` restituisce `"Alice"`, che è arrivata per prima.

#### Coda — FIFO (First In, First Out)

Un tipo di dato astratto in cui gli elementi vengono aggiunti a un'estremità (il fondo) e rimossi dall'altra (la testa), così che l'elemento che ha aspettato più a lungo viene sempre servito per primo.

**Esempio:** Una coda di stampa è FIFO — il primo documento inviato alla stampante è il primo a essere stampato.

#### raise — generare eccezioni manualmente

Un'istruzione che attiva deliberatamente un'eccezione, sia per rilanciarne una già catturata sia per segnalare una condizione di errore con un messaggio specifico a chi ha chiamato il codice.

**Esempio:** `if age < 0: raise ValueError("Age cannot be negative")` interrompe il programma con un messaggio descrittivo quando vengono rilevati dati non validi.

#### random — generazione di numeri casuali

Un modulo della libreria standard che fornisce funzioni per generare numeri pseudo-casuali, fare scelte casuali e mescolare sequenze, utile per giochi, simulazioni e campionamento.

**Esempio:** `import random; random.randint(1, 6)` simula il lancio di un dado a sei facce.

#### random.choice(sequence)

Una funzione del modulo `random` che restituisce un singolo elemento scelto casualmente da una sequenza non vuota come una lista o una stringa.

**Esempio:** `random.choice(["rock", "paper", "scissors"])` restituisce una delle tre opzioni a caso.

#### random.randint(min, max)

Una funzione del modulo `random` che restituisce un intero casuale tra `min` e `max`, inclusi entrambi gli estremi.

**Esempio:** `random.randint(1, 10)` restituisce un numero intero casuale tra 1 e 10 ogni volta che viene chiamata.

#### random.seed() — riproducibilità

Una funzione del modulo `random` che inizializza il generatore di numeri casuali con un valore di partenza specificato, assicurando che venga prodotta la stessa sequenza di numeri casuali ogni volta che il programma viene eseguito — utile per i test.

**Esempio:** `random.seed(42); print(random.randint(1, 100))` stampa sempre lo stesso numero quando il seed è `42`.

#### random.shuffle(list)

Una funzione del modulo `random` che riordina casualmente sul posto gli elementi di una lista, modificando la lista originale invece di crearne una nuova.

**Esempio:** `cards = [1, 2, 3, 4, 5]; random.shuffle(cards)` riordina `cards` in un ordine casuale ogni volta.

#### range() — generare una sequenza di numeri

Una funzione built-in che produce su richiesta una sequenza immutabile di interi senza memorizzarli tutti, comunemente usata per controllare il numero di iterazioni in un ciclo `for`.

**Esempio:** `range(5)` genera `0, 1, 2, 3, 4`; `range(10, 0, -2)` genera `10, 8, 6, 4, 2`.

#### range(start, stop, step)

Una funzione built-in che genera una sequenza di interi da `start` fino a (ma non incluso) `stop`, incrementando di `step` ogni volta; `start` e `step` sono opzionali e valgono per impostazione predefinita `0` e `1`.

**Esempio:** `range(2, 10, 2)` genera `2, 4, 6, 8`; `range(5)` genera `0, 1, 2, 3, 4`.

#### Raspberry Pi come piattaforma Python

Un piccolo ed economico computer a scheda singola che esegue Linux e viene fornito con Python preinstallato, rendendolo un dispositivo popolare per imparare a programmare e costruire progetti di physical computing.

**Esempio:** Gli studenti usano un Raspberry Pi per eseguire un programma Python che controlla luci LED collegate ai pin GPIO della scheda.

#### Stringhe raw per i pattern regex (r"...")

Una stringa preceduta da `r` che dice a Python di trattare i backslash come caratteri letterali invece che come sequenze di escape, rendendo più facili da scrivere e leggere i pattern regex.

**Esempio:** `r"\n"` è una stringa di due caratteri (backslash + n) usata nelle regex; senza la `r`, `"\n"` sarebbe un carattere di a capo.

#### re — espressioni regolari

Un modulo della libreria standard che fornisce strumenti per cercare, confrontare e manipolare stringhe usando pattern chiamati espressioni regolari, che descrivono forme di testo anziché testo esatto.

**Esempio:** `import re; re.search(r"\d+", "Order 42")` trova il numero `42` dentro la stringa.

#### re.findall(pattern, string) — trovare tutte le corrispondenze

Una funzione del modulo `re` che restituisce una lista di tutte le corrispondenze non sovrapposte di un pattern trovate in una stringa, nell'ordine in cui compaiono.

**Esempio:** `re.findall(r"\d+", "Call 911 or 112")` restituisce `["911", "112"]`.

#### re.search(pattern, string) — trovare la prima corrispondenza

Una funzione del modulo `re` che scansiona una stringa e restituisce un oggetto match per la prima posizione in cui viene trovato il pattern, o `None` se non esiste alcuna corrispondenza.

**Esempio:** `re.search(r"\d+", "I have 3 cats")` restituisce un oggetto match per `"3"`; verificare `if re.search(...):` controlla in modo sicuro l'esistenza di una corrispondenza.

#### re.split(pattern, string) — dividere in base a un pattern

Una funzione del modulo `re` che divide una stringa in ogni punto in cui il pattern corrisponde, restituendo una lista dei pezzi tra le corrispondenze.

**Esempio:** `re.split(r"\s+", "hello   world  there")` divide su qualsiasi spazio bianco, restituendo `["hello", "world", "there"]`.

#### re.sub(pattern, replacement, string) — sostituire le corrispondenze

Una funzione del modulo `re` che sostituisce ogni occorrenza di un pattern in una stringa con una stringa di sostituzione specificata e restituisce il risultato modificato.

**Esempio:** `re.sub(r"\d", "*", "Phone: 555-1234")` restituisce `"Phone: ***-****"` sostituendo ogni cifra con `*`.

#### Leggere un traceback (stack trace)

La competenza di interpretare l'output di errore di Python, che elenca la catena di chiamate di funzione che hanno portato al crash e indica, in fondo, il file, il numero di riga e il tipo di errore.

**Esempio:** Un traceback che mostra `ZeroDivisionError: division by zero` alla riga 12 ti dice esattamente dove guardare nel tuo codice per trovare il bug.

#### Leggere e scrivere file JSON (modulo json)

L'uso del modulo `json` integrato in Python per serializzare oggetti Python (dizionari, liste) in un file di testo in formato JSON con `json.dump()` e per analizzare file JSON e riconvertirli in oggetti Python con `json.load()`.

**Esempio:** `import json` / `with open("settings.json", "w") as f: json.dump({"level": 3, "score": 500}, f)` salva le impostazioni di gioco; `json.load(f)` le rilegge.

#### Leggere la documentazione con help() e dir()

La competenza di usare `help()` integrata in Python per leggere la docstring di una funzione e `dir()` per elencare gli attributi e i metodi disponibili di un oggetto, permettendo di esplorare codice sconosciuto senza uscire dall'interprete.

**Esempio:** `dir(str)` mostra tutti i metodi delle stringhe; `help(str.replace)` spiega esattamente come funziona `.replace()` e quali argomenti accetta.

#### Reti ricorrenti (RNN) — panoramica

Una classe di rete neurale in cui le connessioni possono formare cicli diretti, permettendo alla rete di mantenere uno stato nascosto attraverso i passi temporali, rendendole adatte a dati sequenziali come testo o serie temporali.

**Esempio:** Una RNN può elaborare una frase parola per parola, tenendo traccia del contesto delle parole precedenti per capire meglio il significato di ogni nuova parola.

#### Caso base e caso ricorsivo della ricorsione

Le due parti essenziali di qualsiasi funzione ricorsiva: il caso base è una condizione che ferma la ricorsione restituendo un risultato senza una chiamata ricorsiva; il caso ricorsivo scompone il problema in una versione più piccola e richiama di nuovo la funzione.

**Esempio:** In una funzione fattoriale, `if n == 1: return 1` è il caso base e `return n * factorial(n - 1)` è il caso ricorsivo.

#### Profondità di ricorsione e stack overflow

Il limite al numero di volte in cui una funzione può richiamare se stessa prima che Python generi un `RecursionError`; ogni chiamata aggiunge un frame allo stack delle chiamate, e Python ha una profondità massima predefinita (di solito 1000) per evitare che il programma vada in crash.

**Esempio:** Una funzione ricorsiva che non raggiunge mai il suo caso base continua a richiamare se stessa finché Python non genera `RecursionError: maximum recursion depth exceeded`.

#### Ricorsione — una funzione che richiama se stessa

Una tecnica di programmazione in cui una funzione risolve un problema richiamando se stessa con una versione più piccola o più semplice del problema, continuando finché non viene raggiunto un caso base che interrompe la catena di chiamate.

**Esempio:** Una funzione ricorsiva che conta alla rovescia da `n` richiama se stessa con `n - 1` finché non raggiunge `0`, punto in cui si ferma.

#### Rimuovere voci: .pop(), del

Due modi per eliminare una coppia chiave-valore da un dizionario: `.pop(key)` rimuove la coppia e restituisce il valore; `del d[key]` rimuove la coppia senza restituire nulla.

**Esempio:** `removed = inventory.pop("apples")` rimuove `"apples"` e ne memorizza il valore; `del inventory["apples"]` la rimuove scartando il valore.

#### repl.it — IDE Python online

Una piattaforma basata sul web dove puoi scrivere, eseguire e condividere programmi Python da qualsiasi dispositivo con un browser, fornendo un editor, una console e l'archiviazione dei file tutto in un unico posto.

**Esempio:** Puoi avviare un nuovo repl Python su repl.it, digitare il tuo codice a sinistra e vedere l'output a destra senza installare nulla.

#### Rimodellare gli array (array.reshape())

Un metodo di NumPy che cambia la forma (dimensioni) di un array senza cambiarne i dati, ad esempio convertendo una lista piatta di 12 numeri in una griglia 3×4.

**Esempio:** `np.arange(12).reshape(3, 4)` trasforma la sequenza 0–11 in un array 2D di 3 righe e 4 colonne.

#### Istruzione return

Un'istruzione dentro il corpo di una funzione che termina immediatamente la funzione e invia un valore specificato indietro a chi l'ha chiamata; senza di essa, la funzione restituisce `None`.

**Esempio:** `def square(n): return n * n` invia indietro il risultato così `result = square(5)` memorizza `25`.

#### reversed() — restituire un iteratore inverso

Una funzione built-in che restituisce un iteratore che produce gli elementi di una sequenza in ordine inverso senza modificare l'originale né creare una copia invertita completa.

**Esempio:** `list(reversed([1, 2, 3]))` produce `[3, 2, 1]`; `for c in reversed("abc"): print(c)` stampa `c`, `b`, `a`.

#### Modello di colore RGB

Un metodo per rappresentare i colori specificando l'intensità delle componenti di luce rossa, verde e blu, ciascuna tipicamente compresa tra 0 e 255, che vengono combinate per produrre qualsiasi colore visibile.

**Esempio:** RGB `(255, 0, 0)` è rosso; `(0, 255, 0)` è verde; `(128, 0, 128)` è viola; `(255, 255, 255)` è bianco.

#### round() — arrotondare un numero

Una funzione built-in che arrotonda un numero in virgola mobile all'intero più vicino o a un numero specificato di cifre decimali.

**Esempio:** `round(3.7)` restituisce `4`; `round(3.14159, 2)` restituisce `3.14`.

#### Eseguire script Python dal terminale

Eseguire un file `.py` salvato digitando `python filename.py` (o `python3 filename.py`) in una finestra a riga di comando, il che fa sì che l'interprete esegua l'intero file dall'inizio alla fine.

**Esempio:** Dopo aver salvato `hello.py`, apri un terminale, navighi fino alla cartella del file e digiti `python hello.py` per vedere l'output.

#### Impostazione dello schermo: setup(width, height), bgcolor(color), title(text)

Tre metodi chiamati su un oggetto `turtle.Screen()` che configurano la finestra di disegno: `setup()` ne imposta le dimensioni in pixel; `bgcolor()` imposta il colore di sfondo; `title()` imposta il testo mostrato nella barra del titolo.

**Esempio:** `screen.setup(600, 400); screen.bgcolor("black"); screen.title("My Drawing")` crea una finestra nera di 600×400.

#### Cercare su Stack Overflow e nella documentazione

La competenza pratica di trovare risposte a domande di programmazione cercando nella documentazione ufficiale di Python o sul sito di domande e risposte della community Stack Overflow, dove milioni di domande di programmazione hanno già ricevuto risposta.

**Esempio:** Cercare su Stack Overflow "python list remove duplicates" restituisce decine di soluzioni che usano insiemi o comprehension di liste che puoi studiare e adattare.

#### Parametro self

Un primo parametro convenzionale in ogni definizione di metodo d'istanza che si riferisce allo specifico oggetto su cui viene chiamato il metodo, permettendo al metodo di accedere e modificare gli attributi propri dell'oggetto.

**Esempio:** In `def bark(self): print(self.name, "says woof!")`, `self.name` si riferisce al nome del cane particolare che ha chiamato `bark()`.

#### Modello Sequential

Un tipo di modello Keras che impila gli strati in una sequenza lineare, dove i dati fluiscono dal primo strato attraverso ogni strato successivo in ordine, usato per la maggior parte delle architetture di rete neurale più semplici.

**Esempio:** `model = keras.Sequential([Dense(64, activation="relu"), Dense(10, activation="softmax")])` costruisce una rete a due strati.

#### Operazioni sugli insiemi: unione (|), intersezione (&), differenza (-)

Operazioni matematiche su due insiemi: `|` restituisce tutti gli elementi presenti in uno dei due insiemi; `&` restituisce solo gli elementi presenti in entrambi; `-` restituisce gli elementi presenti nel primo insieme ma non nel secondo.

**Esempio:** `{1,2,3} | {3,4,5}` dà `{1,2,3,4,5}`; `{1,2,3} & {3,4,5}` dà `{3}`; `{1,2,3} - {3,4,5}` dà `{1,2}`.

#### Tipo insieme (set) — collezione non ordinata di elementi unici

Un tipo di dato Python che memorizza un gruppo non ordinato di elementi in cui ogni valore può comparire una sola volta, rendendo gli insiemi ideali per rimuovere i duplicati ed eseguire operazioni matematiche sugli insiemi.

**Esempio:** `unique = {1, 2, 3, 2, 1}` memorizza solo `{1, 2, 3}` perché i duplicati vengono rimossi automaticamente.

#### Virgolette singole vs doppie

Due modi intercambiabili per delimitare una stringa in Python, dove `'text'` e `"text"` producono stringhe identiche; la scelta conta solo quando la stringa stessa contiene un tipo di virgoletta.

**Esempio:** Usa `"It's a great day!"` per includere un apostrofo senza doverlo escapare, oppure `'She said "wow"'` per includere virgolette doppie all'interno.

#### Sintassi della tupla a un solo elemento ((x,))

La sintassi speciale necessaria per creare una tupla con esattamente un elemento, in cui una virgola finale deve seguire l'elemento dentro le parentesi; senza la virgola, Python tratta le parentesi come un raggruppamento invece che come una tupla.

**Esempio:** `single = (42,)` crea una tupla con un elemento; `not_a_tuple = (42)` è solo l'intero `42` tra parentesi.

#### Convenzione di denominazione snake_case

Uno stile per scrivere nomi di variabili e funzioni composti da più parole in Python in cui tutte le lettere sono minuscole e le parole sono separate da underscore, rendendo i nomi leggibili senza spazi.

**Esempio:** `total_price`, `player_name` e `max_speed` sono tutti scritti in snake_case.

#### sorted() — restituire una lista ordinata

Una funzione built-in che restituisce una nuova lista ordinata a partire da qualsiasi iterabile, lasciando invariato l'originale; accetta gli argomenti opzionali `key` e `reverse`.

**Esempio:** `sorted([3, 1, 4, 1, 5])` restituisce `[1, 1, 3, 4, 5]`; `sorted(["banana", "apple"])` restituisce `["apple", "banana"]`.

#### Panoramica sugli algoritmi di ordinamento (bubble, selection, insertion)

Un'introduzione a tre semplici metodi di ordinamento basati su confronto: il bubble sort scambia ripetutamente gli elementi adiacenti fuori ordine; il selection sort trova il minimo a ogni passaggio; l'insertion sort colloca ogni elemento nella sua posizione corretta tra quelli già ordinati.

**Esempio:** Il bubble sort su `[3, 1, 2]` confronta e scambia ripetutamente gli elementi vicini finché la lista non diventa `[1, 2, 3]`.

#### Ordinare con una funzione chiave (sorted(list, key=...))

Una tecnica che personalizza il modo in cui `sorted()` o `.sort()` ordinano gli elementi passando una funzione `key` che associa a ogni elemento un valore di confronto; gli elementi vengono quindi ordinati in base a quei valori.

**Esempio:** `sorted(words, key=len)` ordina una lista di stringhe dalla più corta alla più lunga; `sorted(students, key=lambda s: s["score"])` ordina i dizionari degli studenti per punteggio.

#### Controllo della velocità: speed(value)

Un metodo della turtle che imposta la velocità con cui la turtle si muove e disegna, accettando valori da `0` (velocissima, senza animazione) a `10` (veloce) o stringhe descrittive come `"slow"`, `"normal"`, `"fast"`.

**Esempio:** `t.speed(0)` fa disegnare la turtle il più velocemente possibile, utile quando si disegnano molte forme complesse.

#### Spyder IDE — IDE Python scientifico

Un ambiente di sviluppo gratuito pensato per la data science e il lavoro Python matematicamente intensivo che include un esploratore di variabili, una console e un facile accesso a librerie come NumPy e Matplotlib.

#### Stack — LIFO (Last In, First Out)

Un tipo di dato astratto in cui gli elementi vengono aggiunti e rimossi dalla stessa estremità (la cima), così che l'elemento aggiunto più di recente è sempre il primo a essere rimosso.

**Esempio:** Le chiamate di funzione Python usano uno stack interno — la funzione chiamata più di recente è la prima a terminare ed essere rimossa.

#### str() — conversione a stringa

Una funzione built-in che converte qualsiasi valore — come un intero, un float o una lista — nella sua rappresentazione testuale come stringa, permettendo di concatenarlo o stamparlo insieme ad altre stringhe.

**Esempio:** `str(42)` restituisce `"42"`; `"Your score is " + str(score)` combina del testo con una variabile numerica.

#### __str__() — rappresentazione testuale di un oggetto

Un metodo speciale definito in una classe che controlla cosa viene restituito quando l'oggetto viene convertito in stringa (es. con `str()` o `print()`), facendo sì che gli oggetti vengano visualizzati in un formato leggibile dall'uomo.

**Esempio:** `def __str__(self): return f"Dog({self.name}, age {self.age})"` fa sì che `print(my_dog)` mostri `Dog(Buddy, age 3)`.

#### Concatenazione di stringhe con +

L'operazione di unire due o più stringhe una dopo l'altra usando l'operatore `+` per produrre un'unica stringa più lunga.

**Esempio:** `"Hello, " + "world!"` produce `"Hello, world!"`; `first + " " + last` combina un nome e un cognome con uno spazio tra i due.

#### Formattazione f-string con specificatori di formato (es. {x:.2f})

Una funzionalità delle f-string che permette un controllo preciso su come vengono mostrati i valori, usando codici di formato dentro le parentesi graffe dopo i due punti per specificare cifre decimali, larghezza, allineamento e altro.

**Esempio:** `f"Pi is approximately {math.pi:.2f}"` mostra `Pi is approximately 3.14` arrotondando a due cifre decimali.

#### Formattazione di stringhe con .format()

Un metodo delle stringhe che inserisce valori in una stringa modello sostituendo i segnaposto `{}` con gli argomenti forniti, permettendo di inserire in modo ordinato numeri e variabili nel testo.

**Esempio:** `"Hello, {}! You are {} years old.".format("Alex", 12)` produce `"Hello, Alex! You are 12 years old."`.

#### Immutabilità delle stringhe

La proprietà delle stringhe Python che impedisce di cambiare qualsiasi carattere dopo la creazione della stringa; le operazioni che sembrano modificare una stringa in realtà ne creano e restituiscono una nuova.

**Esempio:** `s = "hello"; s[0] = "H"` genera un `TypeError`; usa invece `s = "H" + s[1:]` per costruire una nuova stringa.

#### Indicizzazione delle stringhe (basata su 0)

Il metodo per accedere a un singolo carattere di una stringa tramite il suo numero di posizione, dove il primo carattere è all'indice `0`, il secondo all'indice `1`, e gli indici negativi contano all'indietro dalla fine.

**Esempio:** Se `word = "Python"`, allora `word[0]` è `'P'`, `word[2]` è `'t'`, e `word[-1]` è `'n'`.

#### Lunghezza di una stringa con len()

Una funzione built-in che conta e restituisce il numero di caratteri in una stringa, inclusi spazi e punteggiatura.

**Esempio:** `len("hello")` restituisce `5`; `len("Hi there!")` restituisce `9`.

#### I metodi delle stringhe come esempio di OOP

Un'osservazione per cui le stringhe Python sono oggetti, e chiamare metodi come `.upper()` o `.split()` su di esse dimostra la programmazione orientata agli oggetti — la stringa è l'oggetto e il metodo opera su di essa.

**Esempio:** `"hello".upper()` mostra l'OOP in azione: `"hello"` è l'oggetto e `.upper()` è il metodo che gli appartiene.

#### Metodi delle stringhe per l'elaborazione del testo: .strip(), .lower(), .replace()

Tre metodi delle stringhe usati frequentemente nell'elaborazione del contenuto dei file: `.strip()` rimuove gli spazi bianchi e gli a capo iniziali/finali; `.lower()` normalizza il maiuscolo/minuscolo; `.replace()` sostituisce sottostringhe.

**Esempio:** `line.strip().lower()` pulisce una riga letta da un file rimuovendo gli spazi bianchi circostanti e convertendola in minuscolo.

#### Metodi delle stringhe: .isdigit(), .isalpha(), .isalnum()

Metodi built-in delle stringhe che restituiscono `True` o `False` in base ai caratteri presenti in una stringa: `.isdigit()` verifica che ogni carattere sia una cifra; `.isalpha()` verifica che siano solo lettere; `.isalnum()` verifica che siano lettere o cifre senza spazi o simboli.

**Esempio:** `"123".isdigit()` restituisce `True`; `"abc123".isalpha()` restituisce `False` perché sono presenti delle cifre.

#### Metodi delle stringhe: .lower(), .upper(), .strip(), .lstrip(), .rstrip()

Metodi built-in delle stringhe che restituiscono copie modificate di una stringa: `.lower()` converte tutte le lettere in minuscolo; `.upper()` in maiuscolo; `.strip()` rimuove gli spazi bianchi iniziali e finali; `.lstrip()` rimuove solo quelli iniziali; `.rstrip()` solo quelli finali.

**Esempio:** `"  Hello  ".strip()` restituisce `"Hello"`; `"Python".lower()` restituisce `"python"`.

#### Metodi delle stringhe: .split(), .join(), .replace()

Metodi built-in delle stringhe che ristrutturano le stringhe: `.split()` suddivide una stringa in una lista in corrispondenza di un delimitatore; `.join()` unisce una lista di stringhe con un separatore; `.replace()` sostituisce ogni occorrenza di una sottostringa con un'altra.

**Esempio:** `"a,b,c".split(",")` restituisce `["a", "b", "c"]`; `",".join(["a", "b", "c"])` restituisce `"a,b,c"`.

#### Metodi delle stringhe: .startswith(), .endswith(), .find(), .count()

Metodi built-in delle stringhe che ispezionano il contenuto di una stringa: `.startswith()` e `.endswith()` verificano come inizia o finisce la stringa; `.find()` restituisce l'indice della prima corrispondenza (o `-1`); `.count()` conta le occorrenze non sovrapposte di una sottostringa.

**Esempio:** `"hello.py".endswith(".py")` restituisce `True`; `"banana".count("a")` restituisce `3`.

#### Ripetizione di stringhe con *

L'operazione di ripetere una stringa un numero specificato di volte usando l'operatore `*`, producendo una nuova stringa che contiene l'originale ripetuto consecutivamente.

**Esempio:** `"ha" * 3` produce `"hahaha"`; `"-" * 20` crea una riga divisoria di venti trattini.

#### Slicing delle stringhe (s[start:end:step])

L'operazione di estrarre una porzione di una stringa specificando un indice di inizio, un indice di fine (esclusivo) e un valore di passo opzionale tra parentesi quadre.

**Esempio:** `"Python"[0:3]` restituisce `"Pyt"`; `"abcdef"[::2]` restituisce `"ace"` prendendo un carattere ogni due.

#### Tipo stringa (str) — testo racchiuso tra virgolette

Un tipo di dato Python che memorizza una sequenza di caratteri — lettere, cifre, simboli e spazi — racchiusa tra virgolette singole o doppie corrispondenti.

**Esempio:** `greeting = "Hello, world!"` memorizza una stringa di 13 caratteri nella variabile `greeting`.

#### string — costanti di stringa (punteggiatura, cifre, ecc.)

Un modulo della libreria standard che fornisce utili costanti di stringa predefinite come `string.ascii_letters`, `string.digits` e `string.punctuation`, risparmiandoti di doverle digitare manualmente.

**Esempio:** `import string; string.digits` dà `"0123456789"`; puoi usarlo per verificare se un carattere è una cifra.

#### sum() — sommare i valori di un iterabile

Una funzione built-in che somma tutti gli elementi numerici di un iterabile e ne restituisce il totale, con un valore di partenza opzionale.

**Esempio:** `sum([10, 20, 30])` restituisce `60`; `sum(range(101))` restituisce `5050`, la somma da 1 a 100.

#### sys — operazioni a livello di sistema

Un modulo della libreria standard che fornisce accesso a variabili e funzioni relative all'interprete Python stesso, come gli argomenti da riga di comando, la versione di Python e la possibilità di terminare il programma.

**Esempio:** `import sys; sys.exit()` ferma immediatamente il programma da qualsiasi punto del codice.

#### sys.path — percorso di ricerca dei moduli Python

Una lista all'interno del modulo `sys` che contiene le cartelle in cui Python cerca, in ordine, quando usi un'istruzione `import`, determinando dove Python cerca i file dei moduli.

**Esempio:** Stampare `sys.path` mostra una lista di percorsi di cartelle; aggiungere una cartella a `sys.path` permette a Python di trovare i moduli lì memorizzati.

#### La REPL di Python (shell interattiva)

Un ambiente interattivo — abbreviazione di Read-Eval-Print Loop — in cui digiti un'espressione Python alla volta, l'interprete la valuta, ne stampa il risultato e aspetta il tuo input successivo.

**Esempio:** Digitare `2 + 3` nella REPL di Python mostra immediatamente `5` senza bisogno di scrivere un programma completo.

#### Panoramica sulla libreria standard di Python

Un'ampia collezione di moduli inclusa in ogni installazione di Python che fornisce strumenti già pronti per compiti come la matematica, l'I/O su file, la gestione delle date, il networking e molto altro.

**Esempio:** Senza installare nulla di aggiuntivo, puoi usare `import random`, `import math`, `import os` e decine di altri moduli della libreria standard.

#### Thonny — IDE Python per principianti

Un editor di codice gratuito e leggero progettato per chi sta imparando Python, che evidenzia le variabili, mostra ogni passo dell'esecuzione e visualizza messaggi di errore utili in un linguaggio semplice.

**Esempio:** In Thonny puoi cliccare il pulsante Step per guardare il tuo programma eseguirsi una riga alla volta, il che rende facile individuare gli errori.

#### time — operazioni sul tempo

Un modulo della libreria standard che fornisce funzioni per lavorare con il tempo, inclusi ottenere l'ora attuale, misurare il tempo trascorso e mettere in pausa l'esecuzione del programma.

**Esempio:** `import time; start = time.time()` registra l'ora di inizio così puoi misurare quanto tempo impiega un blocco di codice a essere eseguito.

#### time.sleep() — mettere in pausa l'esecuzione

Una funzione del modulo `time` che mette in pausa il programma per un numero specificato di secondi prima di continuare con la riga successiva, utile per creare ritardi in animazioni o giochi.

**Esempio:** `time.sleep(2)` fa sì che il programma aspetti due secondi prima di eseguire la riga successiva.

#### Trinket.io — ambiente Python basato sul web (deprecato)

Uno strumento gratuito basato sul browser che permetteva di scrivere ed eseguire programmi Python — inclusa la grafica turtle — direttamente in una pagina web senza installare alcun software. Questo libro usava originariamente Trinket, ma Trinket [chiuderà nell'agosto 2026](about.md#a-note-on-platform-history); il libro ora esegue ogni laboratorio con editor **Skulpt** incorporati.

**Esempio:** Le prime versioni di questo libro condividevano un link Trinket così gli studenti potevano cliccare Run e guardare una turtle disegnare un quadrato; oggi lo stesso laboratorio funziona direttamente nella pagina con Skulpt.

#### Veridicità e falsità dei valori (truthiness e falsiness)

La proprietà per cui i valori Python non booleani vengono trattati come `True` o `False` dentro una condizione `if` o `while`: stringhe vuote, `0`, `None` e collezioni vuote sono falsy; tutto il resto è truthy.

**Esempio:** `if name:` verifica se `name` è una stringa non vuota senza bisogno di scrivere `if name != ""`.

#### Blocco try...except

Una struttura di controllo del flusso che tenta di eseguire un blocco di codice dentro `try` e, se si verifica un'eccezione, esegue il blocco `except` corrispondente invece di far andare in crash il programma.

**Esempio:** `try: result = 10 / 0` / `except ZeroDivisionError: print("Can't divide by zero!")` cattura l'errore in modo controllato.

#### Indicizzazione e slicing delle tuple

Lo stesso metodo basato su parentesi usato per le liste che permette di accedere a singoli elementi tramite indice o estrarre una sotto-tupla tramite slicing, poiché le tuple sono sequenze ordinate.

**Esempio:** `point = (10, 20, 30); point[0]` restituisce `10`; `point[1:]` restituisce `(20, 30)`.

#### Tipo tupla (tuple) — collezione ordinata e immutabile

Un tipo di dato Python che memorizza una sequenza ordinata di elementi che non può essere modificata dopo la creazione, rendendo le tuple utili per dati fissi che non dovrebbero essere modificati accidentalmente.

**Esempio:** `point = (3, 7)` memorizza una coordinata x-y che non dovrebbe cambiare; `months = ("Jan", "Feb", "Mar")` memorizza un elenco fisso di nomi di mesi.

#### Spacchettamento delle tuple (tuple unpacking)

La possibilità di assegnare i singoli elementi di una tupla a più variabili in una singola istruzione abbinando il numero di variabili a sinistra al numero di elementi nella tupla.

**Esempio:** `x, y = (3, 7)` memorizza `3` in `x` e `7` in `y`; `first, *rest = (1, 2, 3, 4)` memorizza `1` in `first` e `[2, 3, 4]` in `rest`.

#### Aspetto della turtle: shape() (turtle, arrow, circle, square, triangle, classic)

Un metodo della turtle che cambia l'aspetto visivo del cursore turtle stesso, scegliendo tra forme integrate: `"turtle"`, `"arrow"`, `"circle"`, `"square"`, `"triangle"` o `"classic"`.

**Esempio:** `t.shape("turtle")` sostituisce il cursore a freccia predefinito con una piccola icona a forma di tartaruga.

#### type() — ottenere il tipo di un oggetto

Una funzione built-in che restituisce la classe (tipo di dato) di qualsiasi oggetto Python, utile durante il debug per confermare che tipo di valore contiene una variabile.

**Esempio:** `type(3.14)` restituisce `<class 'float'>`; `type([1, 2])` restituisce `<class 'list'>`.

#### type() — ispezionare il tipo di una variabile

Una funzione built-in che restituisce il tipo di dato di qualsiasi oggetto Python, utile per capire che tipo di valore contiene una variabile durante il debug.

**Esempio:** `type(42)` restituisce `<class 'int'>`; `type("hello")` restituisce `<class 'str'>`; `type(3.14)` restituisce `<class 'float'>`.

#### Tipi di errore: errori di sintassi vs errori di runtime vs errori logici

Tre categorie di errori di programmazione: gli errori di sintassi vengono rilevati prima che il programma venga eseguito (parole chiave scritte male, due punti mancanti); gli errori di runtime fanno andare in crash il programma durante l'esecuzione (divisione per zero); gli errori logici producono risposte sbagliate senza far andare in crash il programma.

**Esempio:** Dimenticare i due punti dopo `if x > 5` è un errore di sintassi; accedere all'indice 10 in una lista di 5 elementi è un errore di runtime; sommare invece di sottrarre è un errore logico.

#### Usare Google e Stack Overflow per fare debug degli errori

La competenza pratica di copiare un messaggio di errore Python in un motore di ricerca o visitare Stack Overflow per trovare spiegazioni e soluzioni pubblicate da altri programmatori che hanno incontrato lo stesso problema.

**Esempio:** Cercare `"Python IndexError: list index out of range"` su Google restituisce tipicamente diverse spiegazioni e soluzioni in pochi secondi.

#### Definizione e assegnazione di variabili (=)

L'atto di creare una posizione di memorizzazione nominata e assegnarle un valore usando l'operatore `=`, che lega il nome a sinistra all'oggetto a destra.

**Esempio:** `age = 13` crea una variabile chiamata `age` e vi memorizza l'intero `13` così puoi usare `age` più avanti nel tuo programma.

#### Regole per i nomi delle variabili (lettere, cifre, underscore)

L'insieme di regole che Python impone per i nomi di variabile validi: devono iniziare con una lettera o un underscore, contenere solo lettere, cifre e underscore, e non devono essere una parola chiave di Python.

**Esempio:** `player1_score` è un nome di variabile valido, ma `1player` non lo è perché inizia con una cifra.

#### Nozioni di base sul controllo di versione (panoramica su git)

Un'introduzione a git, uno strumento che tiene traccia dei cambiamenti ai file nel tempo, permettendoti di salvare istantanee del tuo lavoro, vedere cosa è cambiato e annullare errori tornando a una versione precedente.

**Esempio:** Eseguire `git commit -m "Added score display"` salva un'istantanea così puoi tornare a questa versione del tuo programma se modifiche successive dovessero rompere qualcosa.

#### Ambienti virtuali

Cartelle isolate che contengono ciascuna una propria copia di Python e delle librerie installate, permettendo a progetti diversi di usare versioni diverse dei pacchetti senza conflitti.

**Esempio:** Crei un ambiente virtuale per il tuo progetto di gioco così le sue librerie non entrano in conflitto con quelle usate dal tuo progetto di data science.

#### VS Code — editor di codice general-purpose

Un editor di codice gratuito e popolare realizzato da Microsoft che supporta molti linguaggi di programmazione incluso Python e può essere esteso con componenti aggiuntivi chiamati estensioni per aggiungere funzionalità come l'evidenziazione della sintassi e il debug.

**Esempio:** Dopo aver installato l'estensione Python in VS Code, l'editor sottolinea gli errori nel tuo codice ancora prima che tu lo esegua.

#### Quando usare le tuple invece delle liste

Una linea guida di progettazione: usa una tupla quando il numero di elementi e il loro significato sono fissi (come coordinate o valori RGB), e usa una lista quando la collezione deve crescere, ridursi o essere ordinata.

**Esempio:** Una posizione sullo schermo `(x, y)` si adatta bene a una tupla perché ha sempre esattamente due componenti; una lista della spesa si adatta bene a una `list` perché gli elementi vengono aggiunti e rimossi.

#### Ciclo while — ripetizione basata su condizione

Un'istruzione di controllo del flusso che esegue ripetutamente un blocco di codice finché una condizione specificata rimane `True`, verificando la condizione prima di ogni iterazione.

**Esempio:** `while count < 10: count += 1` continua ad aggiungere 1 a `count` finché non raggiunge 10.

#### Istruzione with (context manager) per la gestione sicura dei file

Un'istruzione Python che chiama automaticamente il metodo di pulizia di una risorsa (come `file.close()`) quando il blocco indentato termina, anche se si verifica un errore, rendendo la gestione dei file più sicura e concisa.

**Esempio:** `with open("data.txt", "r") as f: content = f.read()` chiude automaticamente il file quando il blocco termina.

#### Lavorare con le liste come dati x/y

La tecnica di preparare due liste parallele — una per i valori x e una per i valori y — e passarle a funzioni di plotting per definire i punti dati di un grafico.

**Esempio:** `x = [2020, 2021, 2022]; y = [150, 175, 210]` fornisce tre punti dati per un grafico a barre o a linee delle vendite annuali.

#### Scrivere testo: write(text, font=...)

Un metodo della turtle che posiziona una stringa di testo nella posizione attuale della turtle, con un argomento opzionale `font` che specifica nome, dimensione e stile del font come tupla.

**Esempio:** `t.write("Score: 100", font=("Arial", 16, "bold"))` mostra il punteggio in testo grande e in grassetto nella posizione della turtle.

#### zip() — iterare su più sequenze contemporaneamente

Una funzione built-in che abbina gli elementi di due o più iterabili in base alla posizione e restituisce tuple di elementi abbinati, fermandosi quando l'iterabile più corto si esaurisce.

**Esempio:** `for name, score in zip(names, scores): print(name, score)` stampa il nome di ogni studente accanto al suo punteggio corrispondente.
