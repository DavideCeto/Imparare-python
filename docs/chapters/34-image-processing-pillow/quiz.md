# Quiz: Elaborazione delle Immagini con Pillow

Verifica la tua comprensione di Pillow (PIL), delle modalità delle immagini, dei dati dei pixel, del ridimensionamento, del ritaglio, e del salvataggio delle immagini con queste domande. Clicca su "Mostra risposta" per rivelare la risposta corretta e la spiegazione.

---

#### 1. Come installi e importi Pillow in Python?

<div class="upper-alpha" markdown>
1. Installa con `pip install PIL`; importa con `import pillow`
2. Installa con `pip install pillow`; importa con `from PIL import Image`
3. Installa con `pip install image`; importa con `import Image`
4. Pillow fa parte della libreria standard — nessuna installazione necessaria
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. Installa con `pip install pillow` (il nome del pacchetto è minuscolo `pillow`), ma importa usando il nome originale: `from PIL import Image`. Questo perché Pillow è il fork mantenuto della più vecchia PIL (Python Imaging Library) e ha mantenuto lo stesso nome di import per compatibilità retroattiva.

    **Concept Tested:** Importing Pillow

---

#### 2. Cosa restituisce `img.size` per un'immagine Pillow?

<div class="upper-alpha" markdown>
1. La dimensione del file in byte
2. Una tupla `(width, height)` in pixel
3. Il numero totale di pixel (width × height)
4. Una tupla `(height, width)` seguendo la convenzione matematica
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `img.size` restituisce una tupla `(width, height)` — le dimensioni dell'immagine in pixel. Per esempio, un'immagine 1920×1080 ha `img.size = (1920, 1080)`. Nota che questo è `(width, height)` — l'opposto degli array NumPy che usano `(rows, cols)` o `(height, width)`. Puoi anche accedere separatamente a `img.width` e `img.height`.

    **Concept Tested:** Image Attributes

---

#### 3. Cosa significa `"L"` per `image.mode`?

<div class="upper-alpha" markdown>
1. Large format — l'immagine è più grande della dimensione standard
2. Formato di compressione senza perdita
3. Luminanza — modalità scala di grigi dove ogni pixel è un singolo valore di luminosità 0-255
4. Layered — l'immagine ha più livelli trasparenti
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. Nel sistema di modalità di Pillow, `"L"` significa scala di grigi (luminanza). Ogni pixel è un singolo intero da 0 (nero) a 255 (bianco). `"RGB"` usa tre valori per pixel (rosso, verde, blu), e `"RGBA"` aggiunge un quarto canale alpha per la trasparenza. Converti in scala di grigi con `img.convert("L")`.

    **Concept Tested:** Image Mode

---

#### 4. Quali sono i valori RGB per il bianco puro?

<div class="upper-alpha" markdown>
1. `(0, 0, 0)`
2. `(255, 255, 255)`
3. `(128, 128, 128)`
4. `(255, 0, 0)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. In modalità RGB, ogni canale (rosso, verde, blu) va da 0 a 255. Il bianco ha il valore massimo per tutti e tre i canali: `(255, 255, 255)`. Il nero è `(0, 0, 0)` — minimo per tutti i canali. Il grigio è quando tutti e tre sono uguali: `(128, 128, 128)`. Il rosso puro è `(255, 0, 0)`.

    **Concept Tested:** Pixel Data

---

#### 5. Come ridimensioni un'immagine Pillow a 200×100 pixel?

<div class="upper-alpha" markdown>
1. `img.resize = (200, 100)`
2. `img.scale(200, 100)`
3. `small = img.resize((200, 100))`
4. `img.setSize(200, 100)`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `img.resize((width, height))` restituisce un **nuovo** oggetto immagine alle dimensioni specificate — non modifica l'originale. Assegna sempre il risultato a una variabile. Per una migliore qualità quando riduci la dimensione, passa un filtro di resampling: `img.resize((200, 100), Image.LANCZOS)`. Non esiste un metodo `.scale()` o `.setSize()` in Pillow.

    **Concept Tested:** Resizing Images

---

#### 6. Cosa fa `img.crop((left, top, right, bottom))`?

<div class="upper-alpha" markdown>
1. Elimina il bordo attorno all'immagine
2. Restituisce una nuova immagine contenente solo la regione rettangolare definita dalle coordinate
3. Ruota l'immagine per rimuovere lo spazio vuoto ai bordi
4. Converte l'immagine in bianco e nero rimuovendo le informazioni sul colore
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `img.crop((left, top, right, bottom))` restituisce una nuova immagine che è un ritaglio rettangolare dell'originale. Le coordinate sono in pixel dall'angolo in alto a sinistra: `left` e `top` definiscono l'angolo in alto a sinistra del riquadro di ritaglio, e `right` e `bottom` definiscono l'angolo in basso a destra. Come `resize()`, `crop()` restituisce una nuova immagine senza cambiare l'originale.

    **Concept Tested:** Cropping Images

---

#### 7. Come salvi un'immagine Pillow come file PNG?

<div class="upper-alpha" markdown>
1. `img.export("output.png")`
2. `img.write("output.png")`
3. `Image.save(img, "output.png")`
4. `img.save("output.png")`
</div>

??? question "Mostra risposta"
    La risposta corretta è **D**. `img.save("filename.ext")` salva l'immagine in un file. Pillow determina il formato dall'estensione del file — `.png` salva come PNG, `.jpg` salva come JPEG, `.gif` salva come GIF, ecc. Non esiste una funzione `.export()`, `.write()`, o `Image.save()`.

    **Concept Tested:** Saving Images

---

#### 8. Cosa fa `img.convert("L")`?

<div class="upper-alpha" markdown>
1. Converte l'immagine in una versione a grande formato e alta risoluzione
2. Converte l'immagine da RGB in scala di grigi
3. Converte il file immagine in un formato senza perdita
4. Converte le coordinate dei pixel da ordine (x, y) a (row, col)
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. `img.convert("L")` restituisce una nuova immagine in modalità scala di grigi. Ogni pixel diventa un singolo valore di luminosità da 0 (nero) a 255 (bianco). Altre conversioni utili: `img.convert("RGB")` converte alla modalità colore standard, `img.convert("RGBA")` aggiunge un canale alpha (trasparenza), `img.convert("1")` converte in bianco e nero (binario).

    **Concept Tested:** Color Mode Conversion

---

#### 9. Cosa restituisce `img.getpixel((x, y))` per un'immagine RGB?

<div class="upper-alpha" markdown>
1. Un singolo intero che rappresenta la luminosità del pixel
2. Una lista di tutti i pixel nella riga y
3. Una tupla `(R, G, B)` con i valori rosso, verde, e blu di quel pixel
4. Il codice colore esadecimale del pixel come stringa come `"#FF5500"`
</div>

??? question "Mostra risposta"
    La risposta corretta è **C**. `img.getpixel((x, y))` restituisce il colore del pixel alla colonna `x`, riga `y` come tupla. Per un'immagine RGB, questo è `(R, G, B)` — tre interi 0–255. Per RGBA, include un quarto valore alpha. Per la scala di grigi (modalità `"L"`), restituisce un singolo intero. Le coordinate sono `(x, y)` dove (0,0) è l'angolo in alto a sinistra.

    **Concept Tested:** Pixel Data

---

#### 10. Qual è la differenza principale tra i formati immagine JPEG e PNG?

<div class="upper-alpha" markdown>
1. JPEG è per le foto; PNG non può memorizzare fotografie affatto
2. JPEG usa la compressione lossy (perde un po' di qualità per ridurre la dimensione del file); PNG usa la compressione lossless (nessuna perdita di qualità) e supporta la trasparenza
3. JPEG supporta la trasparenza; PNG no
4. PNG è un formato più vecchio che la maggior parte dei computer non può aprire
</div>

??? question "Mostra risposta"
    La risposta corretta è **B**. JPEG usa la compressione lossy — scarta alcuni dati dell'immagine per ottenere dimensioni di file più piccole, il che va bene per le fotografie ma causa artefatti visibili con alta compressione. PNG usa la compressione lossless — nessun dato viene perso, e supporta la trasparenza (canale alpha). Usa JPEG per le foto dove la dimensione piccola del file è importante; usa PNG per i loghi, gli screenshot, e le immagini dove la qualità e la trasparenza sono importanti.

    **Concept Tested:** Image Formats

---
