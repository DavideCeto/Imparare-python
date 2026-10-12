# Idee per Pattern di Grafica Turtle

Questa galleria raccoglie 100 idee di pattern per ispirare gli studenti a spingere oltre le loro abilità Python.
Ogni pattern è scelto perché insegna un concetto — cicli, funzioni, ricorsione, matematica dei colori,
o geometria — non solo perché è bello da vedere. Scorri le categorie, scegli qualcosa che
catturi il tuo occhio, e sfida te stesso a programmarlo.

---

## Categoria 1 — Cicli di Base e Ripetizione

### 1. Spirale di Quadrati Arcobaleno

Disegna un quadrato, gira leggermente, disegna un quadrato un po' più grande, ripeti 36 volte.
Ogni quadrato è di un colore diverso che scorre tra rosso, arancione, giallo, verde, blu, e viola.
Il risultato sembra un tunnel quadrato di colore che gira verso il centro.
Insegna: cicli `for`, liste di colori, e come un piccolo cambiamento di angolo crea una rotazione visiva drammatica.

### 2. Girandola di Triangoli

Disegna 12 triangoli equilateri disposti in cerchio, ognuno ruotato di 30° dal precedente.
Alterna i colori tra oro e rosso scuro per creare contrasto tra le pale.
Insegna: come ripetere una forma attorno a un punto centrale usando un ciclo e `right(360/n)`.

### 3. Cerchi Annidati

Disegna 20 cerchi concentrici iniziando con raggio 10 e crescendo di 15 pixel a ogni iterazione.
Coloralli con ciano e blu navy alternati così sembrano pulsare verso l'esterno.
Insegna: `range()` con un passo, `circle()`, e come alzare la penna e riposizionarsi tra i cerchi.

### 4. Raggiera a Stella

Dal centro, disegna 36 linee di uguale lunghezza che puntano verso l'esterno, ognuna ruotata di 10° dalla precedente.
Colora ogni linea con una tonalità che passa da giallo in alto a arancione a rosso in basso.
Insegna: calcolare l'indice del colore dal contatore del ciclo, simmetria radiale.

### 5. Griglia a Scacchiera

Disegna una griglia 8×8 di quadrati riempiti alternando nero e bianco come una scacchiera.
Usa cicli `for` annidati per iterare righe e colonne, calcolando la posizione x/y matematicamente.
Insegna: cicli annidati, aritmetica delle coordinate, e `begin_fill()` / `end_fill()`.

### 6. Campo di Strisce Diagonali

Riempi il canvas con 30 linee diagonali parallele, distanti 5 pixel l'una dall'altra, che vanno dal basso-sinistra all'alto-destra.
Alterna i colori delle linee tra verde acqua e corallo.
Insegna: tradurre un contatore di ciclo in una coordinata di partenza, riposizionamento con penna alzata.

### 7. Griglia di Punti

Posiziona un cerchio riempito (punto) a ogni intersezione di una griglia 10×10 spaziata di 40 pixel.
Varia la dimensione del punto in base al numero di riga — i punti crescono verso il basso.
Insegna: cicli annidati, `dot()`, e mappare una variabile di ciclo a una proprietà visiva.

### 8. Spicchi della Ruota dei Colori

Divide il canvas in 12 spicchi a fetta di torta, ognuno riempito con un colore della ruota dei colori HSL.
Usa `begin_fill()` e `end_fill()` con geometria in stile triangolo per disegnare ogni spicchio.
Insegna: dividere 360° in parti uguali, come le 12 tonalità si relazionano tra loro.

### 9. Catena di Pentagoni

Disegna 10 pentagoni in una riga orizzontale, ognuno a contatto con il successivo in un angolo.
Riempi i pentagoni alternati con viola e oro.
Insegna: calcolare l'angolo esterno di un poligono regolare (`360 / sides`), posizionamento orizzontale.

### 10. Quadrati Trasparenti Sovrapposti

Disegna 8 grandi quadrati spostati diagonalmente di 20 pixel ciascuno, con ogni colore di riempimento leggermente diverso.
Poiché i riempimenti di turtle sono opachi, ordina attentamente la sequenza di disegno così le sovrapposizioni sembrano intenzionali.
Insegna: ordine di disegno, pianificazione del colore di riempimento, posizionamento con offset.

---

## Categoria 2 — Funzioni e Riutilizzo

### 11. Fiore con Funzione Petalo

Scrivi una funzione `petal(size, color)` che disegna un petalo arrotondato usando due archi.
Chiamala 8 volte in un ciclo, ruotando di 45° tra ogni chiamata, per assemblare un fiore completo.
Insegna: definire e chiamare funzioni con parametri, come piccole unità riutilizzabili si compongono.

### 12. Griglia a Nido d'Ape

Scrivi una funzione `hexagon(x, y, size)`, poi chiamala in un ciclo annidato per tassellare il canvas con esagoni.
Alterna gli offset delle righe di mezza larghezza di esagono per creare un vero impacchettamento a nido d'ape.
Insegna: parametri delle funzioni, matematica della griglia con offset, e perché gli esagoni tassellano perfettamente.

### 13. Skyline Urbano

Scrivi `building(x, width, height, color)` per disegnare un grattacielo rettangolare con finestre.
Chiamala 10 volte con argomenti variati per costruire una sagoma di skyline attraverso il fondo del canvas.
Insegna: funzioni con più parametri, come comporre una scena da parti riutilizzabili.

### 14. Bracci del Fiocco di Neve

Scrivi `arm(length, levels)` per disegnare un ramo di un fiocco di neve (una linea con due rami laterali più piccoli).
Chiamala 6 volte ruotando di 60° tra le chiamate per formare il fiocco di neve completo a sei bracci.
Insegna: decomporre una forma simmetrica in un braccio più rotazione, riutilizzo delle funzioni.

### 15. Canvas a Pois

Scrivi `dot(x, y, radius, color)` e chiamala con posizioni e colori casuali 200 volte.
Insegna: scrivere una semplice funzione di disegno, usare `random.randint()` per il posizionamento e la scelta del colore.

### 16. Muro di Mattoni

Scrivi `brick(x, y, w, h, color)` per disegnare un rettangolo riempito con un bordo scuro sottile.
Chiamala in un ciclo annidato, spostando le righe alternate di metà larghezza di un mattone.
Insegna: il pattern delle righe con offset, come una piccola funzione nasconde il dettaglio ripetitivo del disegno.

### 17. Stelle di Diverse Dimensioni

Scrivi `star(x, y, size, color)` che disegna una stella a 5 punte usando il metodo della rotazione a 144°.
Chiamala 15 volte con dimensioni da 20 a 120 pixel in posizioni casuali.
Insegna: funzioni parametrizzate, la geometria di una stella a 5 punte (angolo esterno di 144°).

### 18. Semaforo

Scrivi `light(y, color)` per disegnare un cerchio nel colore e posizione corretti.
Chiamala tre volte per assemblare un semaforo dentro un rettangolo scuro.
Insegna: decomporre un oggetto del mondo reale in primitive di disegno e posizionamento tramite argomento della funzione.

### 19. Banco di Pesci

Scrivi `fish(x, y, size, direction)` che disegna una semplice forma di pesce (corpo a ellisse + coda a triangolo).
Chiamala 20 volte con posizioni e dimensioni leggermente variate per un banco di pesci che nuota a sinistra.
Insegna: come una funzione con argomenti diversi crea variazione, narrazione visiva.

### 20. Catena Montuosa

Scrivi `mountain(x, peak_y, width, color)` che disegna un triangolo riempito.
Sovrapponi tre chiamate con grigio-blu progressivamente più chiari per suggerire picchi in primo piano, piano medio, e sfondo.
Insegna: sovrapporre chiamate di disegno per la profondità, come il valore del colore (scuro contro chiaro) segnala la distanza.

---

## Categoria 3 — Spirali

### 21. Spirale Quadrata di Archimede

Muoviti avanti di una distanza crescente a ogni passo, girando esattamente di 90° ogni volta.
Dopo 200 passi la tartaruga traccia una spirale quadrata stretta che si espande verso l'esterno.
Insegna: come un angolo di rotazione fisso più una distanza crescente creano una spirale senza trigonometria.

### 22. Spirale di Linee Arcobaleno

Come il #21 ma colora ogni segmento scorrendo attraverso 6 colori.
Le fasce arcobaleno rendono ogni rivoluzione visivamente distinta.
Insegna: come `i % len(colors)` mappa un contatore di ciclo a un indice della lista di colori.

### 23. Spirale Esagonale

Gira di 60° invece di 90° per una spirale esagonale.
Usa un gradiente da blu a verde per colorare i segmenti.
Insegna: come l'angolo di rotazione da solo determina la forma poligonale della spirale.

### 24. Spirale Triangolare

Gira di 120° per una spirale triangolare.
Colora ogni terzo della spirale con un colore caldo diverso.
Insegna: 120° = angolo di un triangolo equilatero, come emerge la simmetria a tre pieghe.

### 25. Spirale che Collassa verso l'Interno

Inizia con una lunghezza di passo grande e diminuiscila a ogni iterazione finché non raggiunge 1.
La tartaruga si avvolge verso l'interno fino a un punto al centro.
Insegna: sequenze decrescenti, l'effetto visivo della convergenza.

### 26. Spirale Logaritmica Colorata

Usa la trigonometria (`cos`, `sin`) per posizionare la tartaruga lungo una curva a spirale logaritmica.
Colora ogni segmento in base alla sua posizione angolare nel ciclo 0–360°.
Insegna: importare `math`, usare `goto(x, y)` per disegnare curve tramite tracciamento punto per punto.

### 27. Spirale a Doppia Elica

Disegna due spirali interlacciate che iniziano a 180° di distanza, una in blu e una in rosso.
Entrambe si espandono alla stessa velocità così non si intersecano mai.
Insegna: eseguire due sequenze di disegno in un singolo ciclo, offset di fase.

### 28. Spirale di Fibonacci

Disegna archi a quarto di cerchio di raggi 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 in sequenza.
Ogni arco pivota di 90° per seguire la tassellatura del rettangolo di Fibonacci.
Insegna: la sequenza di Fibonacci, come una sequenza matematica produce una curva che sembra naturale.

### 29. Spirale di Spirali

Disegna 12 piccole spirali quadrate disposte in cerchio, ognuna ruotata così da guardare verso l'esterno dal centro.
Insegna: comporre una macro-forma da micro-forme ripetute, cicli annidati.

### 30. Spirale Pentagonale a Fasce Colorate

Spirale con una rotazione di 72° (pentagono) e cambia colore ogni 5 passi.
Fasce di colore distinte marciano verso l'esterno in strisce diagonali attraverso i bracci della spirale.
Insegna: come la scelta dell'intervallo di fasciatura interagisce con il periodo del poligono.

---

## Categoria 4 — Frattali e Ricorsione

### 31. Fiocco di Neve di Koch

Sostituisci ogni segmento di linea retta con quattro segmenti che formano una protuberanza triangolare verso l'esterno.
Ripeti questa sostituzione ricorsivamente 4 volte per ottenere il classico bordo a fiocco di neve.
Insegna: l'idea fondamentale del frattale — sostituire una regola con se stessa a una scala più piccola.

### 32. Triangolo di Sierpiński

Disegna un triangolo, poi disegna ricorsivamente tre triangoli di metà dimensione a ogni angolo.
Fermati alla profondità 5. Riempi i triangoli esterni e lascia vuoti gli spazi centrali.
Insegna: ricorsione con un limite di profondità, come i buchi auto-simili creano un frattale.

### 33. Albero Frattale

Disegna un tronco, poi dividilo in due rami angolati di ±25°, ognuno al 70% della lunghezza del genitore.
Ricorri finché i rami non sono più corti di 5 pixel.
Insegna: ricorsione binaria, il caso base, come l'angolo di ramificazione e il rapporto controllano l'aspetto dell'albero.

### 34. Curva del Dragone

Costruisci la Curva del Dragone piegando a metà ripetutamente una striscia di carta (nel codice).
Dopo 12 piegature, spiega la sequenza di rotazioni sinistra/destra e disegnala.
Insegna: manipolazione di liste per codificare una sequenza ricorsiva, poi riprodurla come movimenti della tartaruga.

### 35. Curva di Hilbert

Implementa la curva che riempie lo spazio di Hilbert con una funzione ricorsiva per ciascuna delle quattro regole del sistema-L.
Alla profondità 5 riempie completamente una regione quadrata senza incrociarsi.
Insegna: sistemi-L, ricorsione mutua (quattro funzioni che si chiamano a vicenda).

### 36. Polvere di Cantor

Disegna una linea orizzontale, poi disegna due linee a un terzo della lunghezza al livello successivo, saltando il terzo centrale.
Ripeti per 6 livelli verso il basso, spaziando ogni livello a una distanza fissa sotto il precedente.
Insegna: l'insieme triadico di Cantor, ricorsione che si riduce di un rapporto, auto-similarità visiva.

### 37. Albero di Pitagora

Disegna un quadrato, poi sul lato superiore fai crescere due quadrati più piccoli ruotati per formare un triangolo rettangolo.
Ricorri su ogni nuovo quadrato finché la dimensione non è sotto i 5 pixel.
Colora i quadrati da marrone (tronco) a verde (foglie) in base alla profondità.
Insegna: ricorsione geometrica, usare la profondità per guidare la transizione di colore.

### 38. Frattale a T-Square

Disegna un quadrato al centro. A ogni angolo, disegna un quadrato di metà dimensione ruotato di 45°.
Ripeti per 5 livelli di profondità. I quadrati sovrapposti creano un intreccio geometrico sorprendente.
Insegna: ricorsione ancorata agli angoli, quattro chiamate ricorsive per livello.

### 39. Curva C di Lévy

Sostituisci ogni segmento con due segmenti ad angoli di 45° (come una protuberanza verso l'alto).
Dopo 12 iterazioni, i segmenti si compattano in una forma che ricorda l'ala di un dragone.
Insegna: una diversa regola di sostituzione frattale, come 45° produce una forma qualitativamente diversa da 60°.

### 40. Curva di Gosper (Flowsnake)

Usa le regole di sostituzione del sistema-L di Gosper per disegnare una curva che tassella il piano.
Dopo 4 iterazioni riempie una regione esagonale con un bellissimo percorso avvolgente.
Insegna: riscrittura di stringhe del sistema-L, tradurre una sequenza di caratteri in comandi della tartaruga.

### 41. Pixel Art di Mandelbrot

Per ogni pixel in una griglia, verifica se l'iterazione di Mandelbrot fugge all'infinito.
Colora il pixel in base a quante iterazioni ci sono volute per fuggire (o nero se non fugge mai).
Questo è lento in Python ma insegna l'aritmetica dei numeri complessi e l'iterazione.
Insegna: numeri complessi, colorazione a tempo di fuga, cicli annidati per la grafica raster.

### 42. Pixel Art dell'Insieme di Julia

Come il Mandelbrot ma con una costante complessa c fissa.
Valori diversi di c producono forme riempite drammaticamente diverse — alcune connesse, alcune polvere.
Insegna: come cambiare un parametro trasforma il frattale, esplorazione dei parametri.

### 43. Tappeto di Sierpiński

Divide un quadrato in 9 sotto-quadrati uguali, rimuovi il centro, poi ricorri sugli 8 rimanenti.
Alla profondità 4, l'area riempita rimanente è un reticolo di buchi dentro buchi.
Insegna: ricorsione a 8 vie (non a 2 vie), come l'area si riduce dell'8/9 per livello.

### 44. Felce di Barnsley

Applica una delle quattro trasformazioni affini scelte casualmente a ogni passo, traccia il punto risultante.
Dopo 50.000 punti, emerge una foglia di felce fotorealistica dalla pura matematica.
Insegna: sistemi di funzioni iterate (IFS), scelta casuale pesata per probabilità, tracciamento a dispersione con `dot()`.

### 45. Variazione del Fiocco di Neve — Anti-Koch

Invece di sporgere verso l'esterno, sporgi verso l'interno a ogni altra iterazione.
Il risultato alterna tra bordi spinosi e intaccati man mano che la profondità aumenta.
Insegna: applicazione alternata della regola, come piccoli cambiamenti di regola creano forme radicalmente diverse.

---

## Categoria 5 — Simmetria e Tassellatura

### 46. Scarabocchio a Simmetria Quadrupla

Registra ogni movimento della tartaruga in una lista. Dopo aver disegnato un quadrante, riproduci la lista
ruotata di 90°, 180°, e 270° per produrre automaticamente un pattern a simmetria quadrupla.
Insegna: registrare comandi come dati, riprodurli con trasformazione.

### 47. Mandala a Simmetria Sestupla

Disegna un sesto di un pattern a mandala, poi stampalo altre 5 volte ruotando di 60° ogni volta.
Insegna: come 360/6 = 60° dà simmetria a sei pieghe, costruzione del mandala basata su funzioni.

### 48. Farfalla a Specchio

Disegna l'ala destra di una farfalla come una curva a mano libera usando punti di passaggio con `goto()`.
Rifletti negando le coordinate x per l'ala sinistra.
Insegna: simmetria bilaterale tramite negazione di x, usare liste di coordinate.

### 49. Fetta di Caleidoscopio

Disegna una fetta angolare casuale con forme riempite e colori vivaci.
Ruota e rifletti 12 volte per creare un caleidoscopio a 12 sezioni.
Insegna: combinare rotazione (30°) e riflessione (inversione x) per costruire simmetria radiale.

### 50. Tassellatura a Girandola

Tassella il canvas con la tassellatura a girandola di Penrose (triangoli divisi in 5 triangoli più piccoli).
Colora i triangoli in base al loro angolo di orientamento modulo 5.
Insegna: tassellatura aperiodica, ricorsione per la suddivisione delle tessere.

### 51. Piastrella di Pesci in Stile Escher

Definisci una singola forma di pesce usando punti di passaggio.
Trasla e ruota le copie così che la testa di ogni pesce si incastri nella coda del pesce vicino.
Insegna: come funzionano le tassellature in stile Escher — ogni tessera è sagomata per incastrarsi con le vicine.

### 52. Regioni Colorate di Voronoi

Posiziona 15 punti seme casuali. Per ogni pixel in una griglia, coloralo in base a quale seme gli è più vicino.
Insegna: formula della distanza, classificazione per vicino più prossimo, disegno raster pixel per pixel.

### 53. Piastrelle di Truchet

Riempi una griglia con tessere ognuna contenente un arco `/` o un arco `\`, scelto casualmente.
Gli archi si collegano attraverso i confini delle tessere per formare percorsi serpeggianti simili a fiumi.
Insegna: tassellatura randomizzata, come scelte casuali locali producono struttura globale.

### 54. Tassellatura a Rombi di Penrose

Suddividi ricorsivamente due tipi di rombo (spesso e sottile) seguendo le regole di deflazione di Penrose.
Colora i rombi spessi d'oro e quelli sottili di blu.
Insegna: suddivisione ricorsiva a due regole, geometria aperiodica.

### 55. Pattern a Stella Geometrica Islamica

Costruisci un pattern ripetuto di stelle a 8 punte e forme a croce trovate nei lavori di piastrelle islamiche.
Usa solo linee rette e angoli di 45°.
Insegna: costruzione geometrica esatta da regole angolari, ripetizione tramite traslazione.

---

## Categoria 6 — Natura e Scienza

### 56. Spirale dei Semi di Girasole

Posiziona 500 semi usando l'angolo d'oro (≈137,5°) — ogni seme un angolo d'oro più avanti.
La distanza dal centro cresce come la radice quadrata dell'indice del seme.
I semi si dispongono automaticamente nei bracci a spirale di Fibonacci visti nei girasoli reali.
Insegna: l'angolo d'oro, perché i numeri di Fibonacci appaiono in natura, `math.sqrt()`.

### 57. Ragnatela

Disegna 8 raggi radiali dal centro. Poi disegna anelli concentrici che collegano i raggi,
spaziandoli in una progressione logaritmica così gli anelli interni sono più vicini tra loro.
Insegna: mescolare struttura radiale e concentrica, spaziatura logaritmica.

### 58. Fulmine

Sposta ricorsivamente il punto medio di un segmento di linea verso l'alto o il basso di una quantità casuale,
poi ricorri su ciascuna metà. Dopo 7 livelli, il risultato frastagliato sembra un fulmine.
Insegna: spostamento del punto medio, come la casualità combinata con la ricorsione crea forme organiche.

### 59. Delta del Fiume

Inizia in alto con una linea larga. A ogni passo, dividi casualmente in due rami più sottili.
I rami che vanno fuori schermo vengono eliminati. Il risultato ricorda un delta di fiume o una radice d'albero.
Insegna: ramificazione casuale con potatura, come la ricorsione stocastica differisce da quella deterministica.

### 60. Ramo di Corallo

Usa una funzione di ramificazione ricorsiva ma permetti 1–3 sotto-rami casuali per nodo (non sempre 2).
Varia l'angolo del ramo casualmente entro ±40°. Colora da rosso scuro (base) a rosa (punte).
Insegna: ricorsione ad arità variabile, variazione casuale dell'angolo, gradiente di colore per profondità.

### 61. Bracci a Spirale della Galassia

Disegna quattro bracci a spirale logaritmica distanziati di 90° l'uno dall'altro.
Disperdi punti stellari lungo ogni braccio e aggiungi un ammasso centrale luminoso.
Insegna: spirali logaritmiche, dispersione di punti attorno a una curva usando `random.gauss()` per una diffusione naturale.

### 62. Nervatura della Foglia

Disegna una vena centrale, poi dirama vene più piccole da essa, poi vene ancora più piccole da quelle.
Ogni vena curva leggermente verso l'esterno dal bordo della foglia verso l'interno.
Insegna: struttura di ramificazione biologica, linee curve tramite piccoli passi avanti+rotazione.

### 63. Doppia Elica del DNA Vista di Lato

Traccia due onde sinusoidali distanziate di 180° come sequenze di punti. Collega i pioli tra loro ogni 10 punti.
Colora un filamento blu e uno rosso.
Insegna: `math.sin()`, tracciamento parametrico, come un offset di fase crea l'aspetto dell'elica.

### 64. Onde Concentriche

Disegna ellissi concentriche centrate su tre punti diversi.
Dove le ellissi si sovrappongono, l'interferenza visiva crea pattern di interferenza d'onda.
Insegna: più centri, come le ellissi differiscono dai cerchi, sovrapposizione visiva.

### 65. Mappa Topografica

Disegna curve concentriche irregolari chiuse (cerchi leggermente perturbati) a raggi crescenti.
Colora le fasce tra i contorni da verde (basso) a marrone (alto) a bianco (picco).
Insegna: colorazione dei contorni, come le mappe di elevazione usano le fasce di colore.

---

## Categoria 7 — Curve Matematiche

### 66. Figura di Lissajous

Traccia `x = A·sin(a·t + δ)` e `y = B·sin(b·t)` per t da 0 a 2π usando `goto()`.
Prova i rapporti a:b di 1:2, 2:3, 3:4 per vedere come il rapporto controlla il numero di cicli.
Insegna: equazioni parametriche, `math.sin()`, come il rapporto di frequenza determina la forma della curva.

### 67. Curva a Rosa (Rhodonea)

Traccia `r = cos(k·θ)` in coordinate polari, convertendo ogni punto in `(x, y)` per `goto()`.
Con k=3 ottieni 3 petali; k=4 dà 8 petali (la regola del conteggio dei petali è n o 2n a seconda di k).
Insegna: conversione da polare a cartesiano, come il parametro k cambia il conteggio dei petali.

### 68. Spirografo (Ipotrocoide)

Traccia la curva descritta da una penna in un disco piccolo che rotola dentro un disco più grande.
I parametri r (raggio interno), R (raggio esterno), e d (distanza della penna) controllano il pattern.
Insegna: curve parametriche, come tre parametri creano infinita varietà.

### 69. Epitrocoide (Spirografo Esterno)

Come l'ipotrocoide ma il disco piccolo rotola all'esterno del disco grande.
Produce anelli simili a fiori invece di curve verso l'interno.
Insegna: confrontare rotolamento interno contro esterno, la differenza di segno nella formula parametrica.

### 70. Curva a Farfalla (Temple H. Fay)

Traccia la curva trigonometrica a farfalla in forma polare.
La curva traccia una forma con quattro lobi simili ad ali.
Insegna: equazioni polari più complesse, come le funzioni trascendenti creano forme organiche.

### 71. Superellisse (Curva di Lamé)

Traccia `|x/a|^n + |y/b|^n = 1` per vari valori di n.
n=2 è un'ellisse; n=4 è un rettangolo arrotondato; n=0,5 produce una forma a stella.
Insegna: come cambiare un esponente trasforma continuamente una forma, famiglie parametriche.

### 72. Ovale di Cassini

Traccia l'insieme di punti dove il prodotto delle distanze da due fuochi fissi è uguale a una costante.
Quando la costante è uguale alla distanza tra i fuochi, l'ovale diventa una figura a otto (lemniscata).
Insegna: formula della distanza, come cambiare una costante crea un cambiamento topologico.

### 73. Spirale di Fermat

Traccia `r = ±√θ` in coordinate polari per θ da 0 a 8π.
Due bracci (uno per + e uno per −) si avvolgono verso l'esterno dall'origine simmetricamente.
Insegna: scala della radice quadrata, come ± crea bracci speculari.

### 74. Stella Epicicloidale

Traccia un punto sul bordo di un cerchio che rotola attorno all'esterno di un altro cerchio.
Quando il rapporto dei raggi è un intero n, ottieni una stella con n punte.
Insegna: epicicloidi, come un rapporto intero crea una curva chiusa a punte stellari.

### 75. Astroide (Ipocicloide a Quattro Cuspidi)

Fai rotolare un cerchio di raggio R/4 dentro un cerchio di raggio R.
Il punto tracciato disegna un astroide a quattro cuspidi — una forma come un quadrato gonfio con angoli pizzicati.
Insegna: ipocicloidi, forma parametrica `x = R·cos³(t)`, `y = R·sin³(t)`.

---

## Categoria 8 — Illusioni Ottiche e Op Art

### 76. Illusione dei Quadrati Rotanti

Disegna quadrati concentrici, alternando il loro orientamento d'angolo di 5° a ogni livello.
L'immagine statica appare ruotare o girare quando viene osservata.
Insegna: come il cambiamento di orientamento crea un'illusione cinetica, l'importanza del contrasto alternato.

### 77. Illusione del Muro del Caffè

Disegna righe orizzontali di rettangoli neri e bianchi spostati di mezza unità a ogni riga,
con linee di malta grigie sottili tra le righe.
Le righe appaiono inclinate anche se sono perfettamente orizzontali.
Insegna: il ruolo del contesto (colore della malta) nell'illusione percettiva, disegno preciso della griglia.

### 78. Bande di Mach

Disegna una serie di rettangoli riempiti in tonalità di grigio crescenti.
L'occhio umano percepisce bande scure e chiare ai bordi anche se ogni rettangolo è uniforme.
Insegna: disegnare approssimazioni di gradiente con bande discrete, aritmetica del valore di colore.

### 79. Motivo Moiré

Disegna due insiemi identici di linee parallele strettamente spaziate, uno leggermente ruotato rispetto all'altro.
L'interferenza crea un visibile pattern di battimento di fasce.
Insegna: come due pattern regolari con spaziatura o angolo leggermente diversi creano un terzo pattern emergente.

### 80. Sfera di Vasarely

Disegna una griglia di cerchi ma restringili e spostali verso il centro per creare l'illusione di una sfera che si gonfia fuori dal canvas.
Insegna: come distorcere una griglia regolare può comunicare curvatura tridimensionale.

### 81. Onde di Bridget Riley

Disegna 40 onde sinusoidali orizzontali impilate verticalmente, ognuna leggermente spostata in fase rispetto a quella sopra.
Usa bianco e nero ad alto contrasto.
Insegna: `math.sin()` per generare onde, come lo spostamento di fase crea l'effetto di movimento fluido dell'op-art.

### 82. Esagoni in Espansione

Disegna esagoni che crescono da minuscoli a grandi irradiandosi verso l'esterno dal centro.
Alterna riempimento nero e bianco così il pattern pulsa.
Insegna: ripetizione guidata dalla dimensione, come il contrasto alternato amplifica l'illusione di espansione.

### 83. Griglia Scintillante

Disegna una griglia di rettangoli scuri con intersezioni più chiare.
L'occhio percepisce punti scuri fantasma che tremolano alle intersezioni.
Insegna: posizionamento preciso della griglia, come il contrasto locale guida gli effetti percettivi globali.

### 84. Triangolo Impossibile (Triangolo di Penrose)

Costruisci il triangolo di Penrose usando tre parallelogrammi isometrici disegnati in tre tonalità di grigio.
Le giunzioni locali sembrano valide ma la forma globale è geometricamente impossibile.
Insegna: come viene costruita la prospettiva isometrica, come l'ombreggiatura implica profondità.

### 85. Pulsazione di Anelli Concentrici

Disegna anelli che alternano tra una tonalità calda e una fredda con larghezza decrescente mentre si avvicinano al centro.
Gli anelli appaiono vibrare o pulsare a causa del contrasto simultaneo tra caldo e freddo.
Insegna: contrasto di colore caldo/freddo, costruzione di anelli concentrici.

---

## Categoria 9 — Tipografia e Arte del Testo

### 86. Testo a Spirale

Stampa una parola o un messaggio carattere per carattere lungo un percorso a spirale usando `write()`.
Ogni lettera è posizionata alla posizione attuale della tartaruga, che avanza lungo la spirale.
Insegna: usare `write()` per il rendering del testo, combinare movimento con posizionamento del testo.

### 87. Nome in Lettere Blocco

Disegna ogni lettera di un nome come un disegno della tartaruga composto da segmenti di linea.
Costruisci una funzione `letter_H()`, `letter_A()`, ecc. per ogni lettera necessaria.
Insegna: decomporre forme complesse in primitive di linea, architettura una-funzione-per-carattere.

### 88. Display a Sette Segmenti

Simula un display LED a sette segmenti per le cifre 0–9.
Ogni segmento è un rettangolo riempito; una cifra viene disegnata accendendo o spegnendo i segmenti.
Insegna: mascheramento booleano per selezionare quali segmenti disegnare, codificare le cifre come pattern di bit.

### 89. Distintivo Circolare con Nome

Disponi le lettere di una parola attorno alla circonferenza di un cerchio usando `goto()` e matematica della rotazione.
Ogni lettera è ruotata per guardare radialmente verso l'esterno.
Insegna: posizionare il testo in posizioni calcolate, ruotare la tartaruga prima di scrivere.

### 90. Nome ad Albero Binario

Codifica un nome come una sequenza binaria (ASCII) e disegnalo come un albero binario verticale,
ramo sinistro per 0 e ramo destro per 1.
Insegna: rappresentazione binaria del testo, visualizzare strutture di dati come disegni.

---

## Categoria 10 — Animazione e Interattività

### 91. Pallina che Rimbalza

Muovi un punto attraverso lo schermo e inverti la sua direzione quando raggiunge il bordo del canvas.
Usa `ontimer()` per ridisegnare ogni fotogramma.
Insegna: variabili di velocità, rilevamento di collisione con i confini, il pattern del ciclo di animazione.

### 92. Quadrante dell'Orologio

Disegna un quadrante di orologio con lancette delle ore e dei minuti che si aggiornano ogni secondo.
Usa `ontimer()` e `time.localtime()` per calcolare gli angoli delle lancette dall'ora attuale.
Insegna: aggiornamenti in tempo reale, convertire il tempo in angoli (ora × 30°, minuto × 6°).

### 93. Caccia tra Tartarughe

Una tartaruga ne insegue un'altra. La preda si muove con una camminata casuale; il predatore si gira sempre verso la preda.
Insegna: programmi con due tartarughe, calcolare la direzione verso un punto obiettivo usando `math.atan2()`.

### 94. Disegnatore di Spirografi

Accetta i click del mouse dell'utente per impostare il raggio interno, il raggio esterno, e l'offset della penna.
Disegna l'ipotrocoide risultante ogni volta che l'utente clicca.
Insegna: `onscreenclick()`, input interattivo di parametri, ricalcolare un disegno su richiesta.

### 95. Motivo di Reazione-Diffusione

Simula un semplice sistema di reazione-diffusione Gray-Scott su una griglia di pixel.
A ogni passo, aggiorna ogni cella in base ai suoi vicini. Colora in base alla concentrazione.
Lento ma produce macchie e strisce di aspetto organico come i pattern della pelle animale.
Insegna: simulazione su griglia, regole di aggiornamento basate sui vicini, come la complessità emerge da semplici regole locali.

---

## Categoria 11 — Sfide Avanzate

### 96. Pianta a Sistema-L

Implementa un motore generale di sistema-L: un assioma iniziale, un insieme di regole di riscrittura, e un conteggio di iterazioni.
Applicalo ai sistemi-L delle piante di Prusinkiewicz per far crescere piante ramificate realistiche.
Insegna: riscrittura di stringhe, costruire un interprete generale, la potenza dei motori a regole generalizzate.

### 97. Generatore di Labirinti con la Turtle

Usa un algoritmo di backtracking ricorsivo per generare un labirinto perfetto su una griglia.
Disegna i muri come segmenti di linea della tartaruga.
Insegna: ricerca in profondità, usare uno stack (o la ricorsione) per la generazione di labirinti, strutture di dati a griglia.

### 98. Proiezione di Superficie Parametrica

Calcola punti 3D su una superficie parametrica (sfera, toro, sella) e proiettali su 2D
usando una semplice proiezione ortografica o isometrica.
Disegna la griglia wireframe delle linee UV.
Insegna: matematica della proiezione da 3D a 2D, superfici parametriche, rendering wireframe.

### 99. Collezione di Fiocchi di Neve di Lindenmayer

Implementa cinque diversi frattali a sistema-L (Koch, Lévy, Gosper, Dragone, Peano) in un singolo programma
con un menu per scegliere quale disegnare.
Insegna: organizzare più algoritmi dietro un'interfaccia unificata, riutilizzo del codice tra sistemi correlati.

### 100. Ciclo di Arte Generativa

Scrivi un programma che genera una composizione astratta diversa a ogni esecuzione usando un seme casuale controllato.
L'utente può inserire un numero seme per riprodurre qualsiasi composizione preferita.
Insegna: `random.seed()`, casualità riproducibile, il concetto di uno spazio di design generativo.

---

*Questi 100 pattern vanno da principiante (categorie 1–2) ad avanzato (categorie 9–11).
Inizia da dove la sfida sembra appena oltre la tua zona di comfort — è lì che avviene l'apprendimento.*
