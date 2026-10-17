# Eseguire Python in Docker

Finora in questo corso hai eseguito i programmi Python in due modi:

1. **Skulpt**: Python funziona direttamente nel tuo browser, senza installare nulla.
2. **Il tuo computer**: Python installato sulla tua macchina.

Ora aggiungiamo una terza possibilità: **Docker**. Docker ti permette di eseguire Python dentro
una piccola scatola isolata chiamata *container*, direttamente sul tuo computer ma separata in
modo sicuro da tutto il resto. Il container non può vedere i tuoi file, non può collegarsi a
Internet e sparisce nel momento in cui il tuo programma finisce.

È proprio così che molte aziende vere eseguono il codice degli studenti sulle piattaforme di programmazione!

---

## Prima di cominciare: avvia il servizio Docker

Perché i laboratori di questa pagina funzionino, il servizio di esecuzione Docker deve essere
in funzione in un terminale separato.

**Apri un terminale nella cartella del progetto ed esegui:**

```sh
bash scripts/run-python-docker.sh
```

Se Docker non è installato, lo script stampa istruzioni dettagliate per ogni sistema operativo.
Quando il servizio è in funzione vedrai:

```
Python Docker execution service
Listening on:  http://127.0.0.1:5001
```

Lascia aperto quel terminale mentre lavori su questa pagina.

---

## Che cos'è un container?

Immagina un container come un portapranzo. Il tuo pranzo (Python + il tuo codice) sta dentro
la scatola, completamente separato da tutto il resto che hai nello zaino. Quando hai finito di
mangiare chiudi il coperchio, e il disordine resta dentro.

| Caratteristica | Descrizione |
|---------|-------------|
| **Isolato** | Il tuo codice non può leggere i file del computer che lo ospita |
| **Senza rete** | Il tuo codice non può collegarsi a Internet |
| **Risorse limitate** | Al massimo 64 MB di RAM e metà di un core della CPU |
| **Temporaneo** | Il container viene eliminato nel momento in cui il programma termina |
| **Riproducibile** | Ogni studente usa esattamente la stessa versione di Python |

---

## Laboratorio 1: Hello, World!

Il classico primo programma. Eseguilo, poi prova a cambiare il messaggio.

<div id="docker-lab-1">
<div id="docker-editor-1">
<textarea id="docker-code-1" rows="4" spellcheck="false">print("Hello, World!")</textarea>
<div id="docker-buttons-1">
  <button id="docker-run-1" onclick="runDocker('1')">&#9654; Run</button>
  <button id="docker-reset-1" onclick="resetDocker('1')">&#8635; Reset</button>
</div>
<pre id="docker-output-1" class="docker-output">L'output apparirà qui dopo che avrai cliccato Run.</pre>
</div>
</div>

**Prova questi esperimenti:**

- Cambia `"Hello, World!"` con il tuo nome, per esempio `"Hello, Alex!"`
- Aggiungi una seconda riga `print()` sotto la prima
- Prova `print(2 + 2)`: Python sa fare i calcoli?

---

## Laboratorio 2: variabili e aritmetica

Python può memorizzare dei valori nelle *variabili* e farci dei calcoli.

<div id="docker-lab-2">
<div id="docker-editor-2">
<textarea id="docker-code-2" rows="8" spellcheck="false">name = "Ada Lovelace"
year_born = 1815
current_year = 2025

age = current_year - year_born
print("Name:", name)
print("Age:", age, "years ago she was born")</textarea>
<div id="docker-buttons-2">
  <button id="docker-run-2" onclick="runDocker('2')">&#9654; Run</button>
  <button id="docker-reset-2" onclick="resetDocker('2')">&#8635; Reset</button>
</div>
<pre id="docker-output-2" class="docker-output">L'output apparirà qui dopo che avrai cliccato Run.</pre>
</div>
</div>

**Prova questi esperimenti:**

- Cambia `name` con il tuo nome
- Cambia `year_born` con il tuo anno di nascita: che cosa mostra `age`?
- Aggiungi una riga: `print("Python version check:", 3 * 7)`

---

## Laboratorio 3: cicli nel container

I cicli ti permettono di ripetere il codice molte volte. Questo conta da 1 a 5.

<div id="docker-lab-3">
<div id="docker-editor-3">
<textarea id="docker-code-3" rows="7" spellcheck="false">print("Counting with a loop:")
for i in range(1, 6):
    print(f"  Step {i} of 5")

print("Done!")
</textarea>
<div id="docker-buttons-3">
  <button id="docker-run-3" onclick="runDocker('3')">&#9654; Run</button>
  <button id="docker-reset-3" onclick="resetDocker('3')">&#8635; Reset</button>
</div>
<pre id="docker-output-3" class="docker-output">L'output apparirà qui dopo che avrai cliccato Run.</pre>
</div>
</div>

**Prova questi esperimenti:**

- Cambia `range(1, 6)` in `range(1, 11)` per contare fino a 10
- Sostituisci `Step` con `Rocket launch in` e fai un conto *alla rovescia* usando `range(10, 0, -1)`

---

## Laboratorio 4: quanto tempo ci vuole?

Ogni volta che clicchi **Run**, il tuo codice fa un viaggio di andata e ritorno attraverso
quattro fasi distinte. Questo laboratorio misura il tempo di ciascuna, così puoi vedere
esattamente dove vanno a finire i millisecondi.

| # | Fase | Che cosa succede |
|---|-------|-------------------|
| 1 | **Invio al servizio** | Il browser codifica il tuo codice in JSON e lo invia, tramite la rete di loopback, al servizio Docker in ascolto sulla porta 5001 |
| 2 | **Avvio del container** | Docker crea un container Python nuovo di zecca dall'immagine in cache, prepara il filesystem isolato e avvia il processo Python |
| 3 | **Esecuzione di Python** | Il tuo codice viene eseguito davvero dentro il container |
| 4 | **Ritorno al browser** | L'output del container torna indietro attraverso la rete di loopback e il browser mostra il risultato |

Modifica il codice qui sotto (prova un programma breve e poi un ciclo lungo), poi clicca
**Run** e osserva quali fasi cambiano.

<div id="docker-lab-4">
<div id="docker-editor-4">
<textarea id="docker-code-4" rows="6" spellcheck="false">print("Hello from the timed lab!")
total = 0
for i in range(100_000):
    total += i
print(f"Sum 0–99999 = {total}")</textarea>
<div id="docker-buttons-4">
  <button id="docker-run-4" onclick="runDockerTimed()">&#9654; Run + Time</button>
  <button id="docker-reset-4" onclick="resetDockerTimed()">&#8635; Reset</button>
</div>
</div>
<div id="docker-timing-display" style="display:none; margin-top:12px;">
  <table id="docker-timing-table">
    <thead>
      <tr><th>#</th><th>Fase</th><th style="text-align:right">Tempo (ms)</th><th>Barra</th></tr>
    </thead>
    <tbody>
      <tr id="tr-network-send">
        <td>1</td><td>Invio al servizio (rete)</td>
        <td id="td-network-send" style="text-align:right">—</td>
        <td><div class="timing-bar" id="bar-network-send"></div></td>
      </tr>
      <tr id="tr-startup">
        <td>2</td><td>Avvio del container</td>
        <td id="td-startup" style="text-align:right">—</td>
        <td><div class="timing-bar" id="bar-startup"></div></td>
      </tr>
      <tr id="tr-exec">
        <td>3</td><td>Esecuzione di Python</td>
        <td id="td-exec" style="text-align:right">—</td>
        <td><div class="timing-bar" id="bar-exec"></div></td>
      </tr>
      <tr id="tr-network-return">
        <td>4</td><td>Ritorno al browser (rete)</td>
        <td id="td-network-return" style="text-align:right">—</td>
        <td><div class="timing-bar" id="bar-network-return"></div></td>
      </tr>
      <tr style="font-weight:bold; border-top: 2px solid #642580;">
        <td colspan="2">Andata e ritorno totale</td>
        <td id="td-total" style="text-align:right">—</td>
        <td></td>
      </tr>
    </tbody>
  </table>
  <p id="docker-timing-note" style="font-size:0.85em; color:#666; margin-top:6px;"></p>
</div>
<pre id="docker-output-4" class="docker-output" style="margin-top:10px;">L'output apparirà qui dopo che avrai cliccato Run + Time.</pre>
</div>

**Risultati tipici** (misurati su un MacBook, con `python:3.11-alpine`):

| # | Fase | Avvio a freddo (1ª esecuzione) | A caldo (dalla 2ª in poi) |
|---|-------|---------------------:|----------------:|
| 1 | Invio al servizio (rete) | 3,2 ms | 3,2 ms |
| 2 | Avvio del container | ~4.700 ms | 258 ms |
| 3 | Esecuzione di Python | 9,5 ms | 9,5 ms |
| 4 | Ritorno al browser (rete) | 3,2 ms | 3,2 ms |
| | **Andata e ritorno totale** | **~5.000 ms** | **~274 ms** |

Il codice Python (il ciclo `range(100_000)`) è stato eseguito in 9,516 ms: appena il 3,5% del
tempo di andata e ritorno a caldo. In entrambi i casi è l'avvio del container a occupare la
maggior parte del tempo.

**Cose da notare:**

- La **prima esecuzione è lenta (~5 secondi)**: è un *avvio a freddo*. La prima volta Docker
  deve caricare dal disco alla RAM gli strati (layer) dell'immagine `python:3.11-alpine`.
  Ogni esecuzione successiva è un *avvio a caldo* (~300 ms), perché quegli strati restano
  nella cache delle pagine del sistema operativo (la RAM veloce).
- La fase di **avvio del container** occupa la maggior parte del tempo anche a caldo: Docker
  crea da zero un nuovo processo isolato ogni volta che clicchi Run. È il prezzo della
  sicurezza.
- L'**esecuzione di Python** dura pochi millisecondi anche con cicli su 100.000 numeri: una
  volta partito, Python è veloce.
- Il tempo di **rete** è minimo perché tutto resta su `127.0.0.1` (il tuo computer), senza mai
  passare da Internet.
- Riavviare il computer svuota la cache delle pagine, quindi la prima esecuzione successiva
  sarà di nuovo lenta.

---

## Come funziona

Quando clicchi **Run**, ecco che cosa succede dietro le quinte:

1. Il browser invia il tuo codice al servizio locale in ascolto su `http://127.0.0.1:5001/run`.
2. Il servizio chiede a Docker di avviare un nuovo container Python.
3. Docker esegue il tuo codice dentro il container (senza rete, con memoria limitata e un limite di tempo di 10 secondi).
4. Il container raccoglie tutto ciò che viene stampato sullo schermo.
5. Il servizio rimanda quell'output al tuo browser.
6. Il container viene eliminato automaticamente.

L'andata e ritorno richiede circa **5 secondi alla primissima esecuzione** (avvio a freddo:
Docker carica l'immagine dal disco alla RAM). Ogni esecuzione successiva richiede circa
**300 millisecondi**, perché l'immagine resta nella cache di memoria del sistema operativo
finché non riavvii il computer.

---

## Risoluzione dei problemi

**"Cannot connect to the Python Docker service"** (impossibile collegarsi al servizio Python Docker)
: Il servizio non è in funzione. Apri un terminale ed esegui `bash scripts/run-python-docker.sh`.

**"Docker error: ..."** (errore di Docker)
: Assicurati che Docker Desktop sia aperto (cerca l'icona della balena nella barra dei menu o nell'area di notifica).

**"Timed out after 10 seconds"** (tempo scaduto dopo 10 secondi)
: Il tuo programma è durato troppo. Controlla che non ci sia un ciclo infinito (`while True:` senza `break`).

---

