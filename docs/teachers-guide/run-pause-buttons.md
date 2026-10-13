# Il Pulsante Run ⇄ Pause

Ogni laboratorio Skulpt in questo manuale usa un singolo pulsante che cambia
etichetta man mano che lo stato del programma cambia. Questa pagina spiega
cosa fa il pulsante in ogni stato, come si confronta con altri ambienti
Python, e perché abbiamo scelto questo design per un pubblico post-Scratch.

## Cosa Fa il Pulsante

| Etichetta | Quando appare | Cosa fa il click |
|-------|----------------|-------------------|
| **▶ Run** | Nessun programma è in esecuzione | Esegue il codice nell'editor |
| **❚❚ Pause** | Un programma è in esecuzione | Blocca il programma al prossimo passo di disegno |
| **▶ Resume** | In pausa, codice invariato | Continua esattamente da dove il programma si era fermato |
| **▶ Run New Code** | In pausa, il codice è stato modificato | Scarta il programma in pausa, pulisce il canvas, ed esegue il codice modificato dall'inizio |

Il pulsante **Reset** ferma un programma in esecuzione o in pausa e
ripristina il codice originale.

La pausa è particolarmente utile nei laboratori di grafica turtle: frattali
e tassellature a lunga esecuzione possono essere bloccati a metà disegno così
la classe può discutere il pattern, o così uno studente può fare uno
screenshot di uno stato intermedio interessante.

Se uno studente modifica il codice durante la pausa e poi annulla le sue
modifiche (tornando esattamente al codice che era in esecuzione), l'etichetta
torna a **Resume** — il programma è realmente invariato, quindi può
continuare in sicurezza.

## Come lo Gestiscono Altri Ambienti Python

La maggior parte degli strumenti didattici per Python non ha affatto un
pulsante di pausa:

- **IDLE, il terminale e Thonny** offrono Run e Stop. Un programma in
  esecuzione può solo essere terminato (Ctrl+C o un pulsante di stop), e
  modificare il sorgente non influisce mai su un programma già in esecuzione
  — devi sempre fermarti e rieseguire.
- **I notebook Jupyter** ti permettono di interrompere il kernel, ma non
  esiste un "blocca e continua", e le modifiche al codice contano solo alla
  prossima esecuzione di una cella.
- **Trinket** (usato da un'edizione precedente di questo libro) usava un
  interruttore Run/Stop: il pulsante Run diventava Stop mentre il programma
  era in esecuzione.

Dove pausa/riprendi *è* standard è nei **debugger**: un programma fermato a
un breakpoint riprende esattamente da dove si era interrotto, eseguendo il
vecchio codice, perché Python non può scambiare nuovo codice sorgente dentro
un programma attivo. Alcuni IDE professionali offrono "modifica e continua",
ma la funzionalità è rara e fragile, e Python non l'ha mai davvero supportata.

Nel frattempo, i nostri studenti arrivano per lo più da **Scratch**, dove
modificare uno script *mentre è in esecuzione* ha effetto immediato. Il loro
istinto è: "Ho cambiato il codice, quindi la mia modifica dovrebbe apparire."

## Perché Abbiamo Scelto Questo Design

Il comportamento del pulsante è un ibrido deliberato di queste convenzioni:

1. **Pausa/riprendi viene dai debugger e dagli strumenti di simulazione** —
   esiste perché il disegno stesso vale la pena di essere fermato per essere
   osservato.
2. **Riavviare alla modifica rispetta onestamente l'istinto di Scratch.**
   Riprendere silenziosamente il vecchio codice dopo una modifica (pura
   semantica da debugger) violerebbe l'aspettativa dello studente; modificare
   dal vivo un programma Python in esecuzione è tecnicamente impossibile.
   Iniziare un'esecuzione nuova con il nuovo codice è la via di mezzo onesta.
3. **L'etichetta "Run New Code" rende il risultato prevedibile.** Nel momento
   in cui il codice di un programma in pausa viene modificato, il pulsante
   dice cosa succederà dopo — lo studente non è mai sorpreso da un canvas
   svuotato, perché gli è stato detto che sta eseguendo codice nuovo, non
   riprendendo.

C'è anche una vera lezione di Python nascosta in questo pulsante: **un
programma viene letto una sola volta, all'avvio.** Cambiare il sorgente non
cambia mai un programma già in esecuzione — un fatto vero su Python (e sulla
maggior parte dei linguaggi) che Scratch nasconde deliberatamente. Quando uno
studente chiede perché la sua modifica non ha cambiato il disegno finché non
ha riavviato, quello è un momento didattico, e l'etichetta del pulsante è la
risposta: le modifiche richiedono l'esecuzione di *codice nuovo*.

## Spunti di Discussione per la Classe

- "La pausa è una macchina fotografica, non un editor" — fai pausa per
  guardare, fare uno screenshot e discutere; modifica quando vuoi, ma
  modificare significa ricominciare.
- Chiedi agli studenti: *perché* Python non può spingere la tua modifica nel
  programma in esecuzione? (Il programma è già stato tradotto e avviato; il
  testo dell'editor è solo testo finché Run non lo legge.)
- Gli studenti che annullano le loro modifiche e vedono **Run New Code**
  tornare a **Resume** hanno scoperto la regola con precisione: il pulsante
  confronta l'editor con il codice effettivamente in esecuzione.
