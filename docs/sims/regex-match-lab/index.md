---
title: Laboratorio di Corrispondenze Regex
description: Digita un pattern, guarda ogni corrispondenza illuminarsi dal vivo nel testo campione, e leggi il pattern come gettoni in inglese semplice.
image: /sims/regex-match-lab/regex-match-lab.png
og:image: /sims/regex-match-lab/regex-match-lab.png
twitter:image: /sims/regex-match-lab/regex-match-lab.png
social:
   cards: false
quality_score: 95
---

# Laboratorio di Corrispondenze Regex

<iframe src="main.html" height="372" width="100%" scrolling="no"></iframe>

[Esegui il Laboratorio di Corrispondenze Regex a Schermo Intero](./main.html){ .md-button .md-button--primary }

## Informazioni su questo MicroSim

Le espressioni regolari sono un linguaggio di regole invisibili, e i
principianti non riescono a dire quale parte del pattern corrisponde a
quali caratteri. Questo laboratorio colma il divario in due modi
contemporaneamente: ogni battitura nella casella del pattern riaccende
tutte le corrispondenze nel testo campione (con una riga di risultato
`re.findall` dal vivo), e una striscia di gettoni traduce il pattern in
inglese semplice — `\d` "una cifra 0-9", `{3}` "3 volte", `-` "il
carattere -". I pulsanti preset coprono gli elementi fondamentali del
capitolo: escape, quantificatori, classi di caratteri e alternanza.

**Obiettivo di apprendimento:** Lo studente sarà in grado di testare
un'espressione regolare contro un testo campione e di attribuire ogni
corrispondenza all'elemento del pattern che l'ha prodotta.

- **Tassonomia di Bloom (2001):** Applicare → Analizzare — *usare,
  testare, scomporre*
- **Pattern di interazione:** editor del pattern dal vivo con una striscia
  esplicativa in inglese semplice
- **Libreria:** HTML personalizzato (nessuna libreria di grafici
  necessaria)

## Come Usarlo

1. Leggi ad alta voce i gettoni per il pattern iniziale `\d{3}-\d{4}`,
   prevedi le corrispondenze, poi controlla le evidenziazioni.
2. Elimina un carattere alla volta dal pattern e osserva quali
   corrispondenze sopravvivono.
3. Prova ogni preset: `\d+`, `[A-Z]\w+`, `cat|dog` e `\w+ing`.
4. Costruisci il tuo: riesci a scrivere un pattern che corrisponda solo a
   "sleeping" e "singing" ma non a "ing"?

## Codice di Incorporamento Iframe

Puoi aggiungere questo MicroSim a qualsiasi pagina web aggiungendo questo al
tuo HTML:

```html
<iframe src="https://dmccreary.github.io/learning-python/sims/regex-match-lab/main.html"
        height="372px"
        width="100%"
        scrolling="no"></iframe>
```

## Piano della Lezione

### Livello Scolastico

Scuola primaria superiore e scuola media (10-14 anni), Capitolo 29 (Elaborazione del testo ed espressioni regolari)

### Durata

10-15 minuti

### Prerequisiti

- Stringhe e stringhe raw (Capitoli 8 e 29)
- re.findall() (Capitolo 29)

### Attività

1. **Esercizio di lettura ad alta voce** (4 min): Per ogni preset, gli
   studenti leggono ad alta voce la striscia di gettoni prima di guardare
   le evidenziazioni, poi verificano.
2. **Esperimenti a un carattere** (4 min): Gli studenti cambiano `{3}` in
   `{2}` nel pattern del telefono e spiegano il risultato.
3. **Golf del pattern** (5 min): Sfida — fai corrispondere tutte e tre le
   parole "-ing" con il pattern più corto possibile.

### Verifica

- Lo studente sa tradurre in inglese semplice un pattern del livello del
  capitolo
- Lo studente prevede il numero di corrispondenze di findall per un dato
  pattern e testo
- Lo studente scrive un pattern funzionante per un bersaglio descritto
  (es. "ogni parola con la maiuscola")

## Riferimenti

1. [Python Documentation — re module](https://docs.python.org/3/library/re.html) — documentazione ufficiale delle espressioni regolari
2. [Python HOWTO — Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) — una guida ufficiale più accessibile
