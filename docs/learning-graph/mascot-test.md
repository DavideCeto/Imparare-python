---
title: Monty the Python - Test della Mascotte
description: Pagina di test che mostra tutte le immagini della mascotte e gli stili delle ammonizioni per Monty the Python, il nostro agente pedagogico.
---
# Monty the Python — Test della Mascotte

Questa pagina mostra tutte le immagini della mascotte e gli stili delle ammonizioni come riferimento.
Controlla che tutte le immagini abbiano uno sfondo trasparente e nessuna spaziatura eccessiva.
Il bordo blu tratteggiato intorno a ogni immagine rende visibile la spaziatura.

<style>
img { border: 1px dashed blue; }
</style>

## Test delle Ammonizioni

!!! mascot-neutral "Una Nota da Monty"
    ![Monty neutral pose](../img/mascot/neutral.png){ class="mascot-admonition-img" }
    Ecco una nota amichevole da Monty. Questo è lo stile **neutral**, usato per barre laterali generali o introduzioni.

!!! mascot-welcome "Monty ti dà il Benvenuto!"
    ![Monty waving welcome](../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Benvenuto, programmatore! Sono Monty the Python, e sono qui per aiutarti a imparare a programmare. Questo è lo stile **welcome**, usato all'inizio di ogni lezione.

!!! mascot-thinking "L'Intuizione Chiave di Monty"
    ![Monty thinking](../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Pensiamoci insieme! Questo è lo stile **thinking**, usato per evidenziare concetti chiave e idee importanti.

!!! mascot-tip "Il Consiglio di Monty"
    ![Monty sharing a tip](../img/mascot/tip.png){ class="mascot-admonition-img" }
    Ecco un suggerimento utile da Monty. Questo è lo stile **tip**, usato per indizi e scorciatoie.

!!! mascot-warning "Attenzione!"
    ![Monty warning you](../img/mascot/warning.png){ class="mascot-admonition-img" }
    Attenzione a questo — è un errore comune! Questo è lo stile **warning**, usato per segnalare insidie.

!!! mascot-encourage "Ce la Puoi Fare!"
    ![Monty encouraging you](../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Puoi farcela! Credo in te! Questo è lo stile **encouraging**, usato quando il contenuto diventa impegnativo.

!!! mascot-celebration "Ottimo Lavoro!"
    ![Monty celebrating](../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Congratulazioni — ce l'hai fatta! Questo è lo stile **celebration**, usato alla fine delle lezioni.

## Test della Spaziatura delle Immagini

Verifica che non ci sia spaziatura eccessiva intorno alle immagini.
Se c'è, esegui `scripts/trim-padding-from-image.py docs/img/mascot/FILENAME.png`.

<div class="grid cards" markdown>

- **Welcome**

    ![](../img/mascot/welcome.png){ width="150px" }

- **Thinking**

    ![](../img/mascot/thinking.png){ width="150px" }

- **Tip**

    ![](../img/mascot/tip.png){ width="150px" }

- **Warning**

    ![](../img/mascot/warning.png){ width="150px" }

- **Encouraging**

    ![](../img/mascot/encouraging.png){ width="150px" }

- **Celebration**

    ![](../img/mascot/celebration.png){ width="150px" }

- **Neutral**

    ![](../img/mascot/neutral.png){ width="150px" }

</div>
