## Perché Jupyter Notebook
Eseguiremo questa libreria dentro un Jupyter Notebook. I Jupyter Notebook fanno parte di un tipo importante di programmazione chiamato [Programmazione Letterata](https://en.wikipedia.org/wiki/Literate_programming) dove il codice e la spiegazione del tuo codice sono intervallati in celle. I Jupyter Notebook vengono a volte chiamati il "nuovo Excel" perché entrambi sono modi popolari per analizzare dati. I Jupyter Notebook sono anche popolari tra i Data Scientist e gli sviluppatori di Intelligenza Artificiale e hanno quasi completamente sostituito il linguaggio di programmazione [R](https://trends.google.com/trends/explore?date=all&geo=US&q=Jupyter,R%20Programming).

Pensiamo che imparare Python usando Jupyter sia l'ideale se hai un qualche modo interattivo di vedere i risultati del tuo codice. Combinando la grafica turtle con Jupyter ottieni il meglio di entrambi i mondi.

## Due Modi per Vedere la Grafica Turtle
Ci sono due modi per vedere la grafica turtle in Jupyter:

1. Con la turtle disegnata in una finestra separata
2. Con la turtle disegnata "in linea" direttamente sotto il tuo codice

In generale, in linea è preferibile perché puoi tenere traccia di molti piccoli esercizi semplicemente scorrendo verso il basso. Puoi anche stampare i notebook per mostrare il tuo lavoro ad altri.

In molti di questi laboratori useremo una versione speciale della libreria turtle sviluppata da [Thomas Kluyver](https://github.com/takluyver) dal Regno Unito chiamata "mobilechelonian". Vogliamo ringraziarlo per questo lavoro. Se vuoi puoi mettere una "stella" al seguente repository github: https://github.com/takluyver/mobilechelonian

Nota che i "Chelonia" sono animali dell'ordine Chelonia (o Testudines), che include le tartarughe e le testuggini. Scegliendo un nome molto distintivo per la sua implementazione della libreria turtle, Thomas ha evitato collisioni con altre librerie Python che avevano lo stesso nome.

## Passaggi
Ecco i passaggi che seguiremo per far funzionare la turtle nel nostro Jupyter Notebook:

1. Installare i sistemi dell'ambiente Python conda
2. Creare un nuovo ambiente conda per la nostra turtle e attivarlo
3. Usare lo strumento pip per installare la libreria turtle
4. Installare il software Jupyter Notebook
5. Avviare Jupyter Notebook
6. Testare il programma della turtle

## Installare Conda
Cerca su Google "install python" per il tuo sistema operativo.
Cerca su Google "install conda"

## Creare un Nuovo Ambiente Conda:
Apri il tuo terminale. Digita i seguenti comandi.

```shell
conda env list
conda create -n turtle python=3.6
conda activate turtle
pip install mobilechelonian
juypter notebook
```

Dopo aver eseguito l'ultimo comando si aprirà un Jupyter Notebook in un browser web. Ora puoi verificare che la libreria turtle sia stata installata correttamente.

```python
from mobilechelonian import Turtle
t = Turtle()
t.forward(100)
```

![](../img/jupyter-inline-turtle.png)

```python
help(Turtle)
```

## Riferimenti
[Documentazione Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

