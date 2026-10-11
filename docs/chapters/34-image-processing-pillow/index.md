---
title: Elaborazione delle Immagini con Pillow
description: Apri, mostra, ridimensiona, ritaglia, converti, e salva immagini con la libreria Pillow (PIL) di Python — e capisci i dati a livello di pixel
generated_by: claude skill chapter-content-generator
date: 2026-06-28 15:40:00
version: 0.09
---

# Elaborazione delle Immagini con Pillow

Alla fine di questa lezione sarai in grado di:

- Aprire e mostrare immagini con **Pillow** (`PIL`)
- Ispezionare la dimensione, la modalità, e i dati dei pixel di un'immagine
- Ridimensionare, ritagliare, specchiare, e ruotare le immagini
- Convertire tra modalità di colore (RGB, scala di grigi, RGBA)
- Applicare filtri di base e salvare in diversi formati

Una fotografia sul tuo telefono è solo una griglia di pixel colorati. Python può leggere, analizzare, e trasformare quella griglia — automatizzando compiti come ridimensionare foto profilo, convertire formati, aggiungere watermark, o applicare filtri artistici.

!!! mascot-welcome "Benvenuto/a al Capitolo 34!"
    ![Monty waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Pillow è la libreria di riferimento di Python per il lavoro con le immagini — ed è sorprendentemente semplice.
    Da una foto scolastica a un'immagine satellitare, si applicano le stesse funzioni!
    Iniziamo a modificare! Programmiamo insieme!

<script src="https://skulpt.org/js/skulpt.min.js"></script>
<script src="https://skulpt.org/js/skulpt-stdlib.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.16/mode/python/python.min.js"></script>
<script src="../../js/codemirror-lab.js"></script>

## Cos'è Pillow?

**Pillow** è il fork mantenuto della classica **PIL** (Python Imaging Library). Lo installi con:

```bash
pip install pillow
```

Ma lo importi usando il nome originale:

```python
from PIL import Image
```

Pillow supporta oltre 30 formati di immagine incluso JPEG, PNG, GIF, BMP, TIFF, e WebP.

## Aprire e Ispezionare le Immagini

`Image.open(filepath)` carica un file immagine in memoria.
L'oggetto restituito ha diversi attributi utili:

| Attributo | Cosa ti dice |
|-----------|------------------|
| `image.size` | `(width, height)` in pixel |
| `image.width` | Larghezza in pixel |
| `image.height` | Altezza in pixel |
| `image.mode` | Modalità di colore: `"RGB"`, `"RGBA"`, `"L"` (scala di grigi), `"P"` (palette) |
| `image.format` | Formato del file: `"JPEG"`, `"PNG"`, ecc. (None se creato nel codice) |

```python
from PIL import Image

img = Image.open("photo.jpg")
print(img.size)    # (1920, 1080)
print(img.mode)    # "RGB"
img.show()         # opens in the system image viewer
```

!!! mascot-thinking "Cosa Pensi che Succederà?"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto crea una piccola immagine da zero usando i dati dei pixel.
    Di quale colore pensi che sarà il pixel (1,1) — rosso, verde, o blu?
    Prevedi prima, poi eseguilo!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab()">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab()">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle"></div>
  </div>
</div>
<script>
initCmLab('', `from PIL import Image

# Create a 3x3 RGB image manually:
# Each row is a list of (R, G, B) tuples
pixels = [
    [(255,   0,   0), (  0, 255,   0), (  0,   0, 255)],  # red, green, blue
    [(255, 255,   0), (  0, 255, 255), (255,   0, 255)],  # yellow, cyan, magenta
    [(255, 255, 255), (128, 128, 128), (  0,   0,   0)],  # white, gray, black
]

img = Image.new("RGB", (3, 3))
for row_idx, row in enumerate(pixels):
    for col_idx, color in enumerate(row):
        img.putpixel((col_idx, row_idx), color)

print("Image size:", img.size)
print("Image mode:", img.mode)
print("Pixel at (0,0):", img.getpixel((0, 0)))   # top-left
print("Pixel at (1,0):", img.getpixel((1, 0)))   # top-middle
print("Pixel at (1,1):", img.getpixel((1, 1)))   # center`);
</script>

## Capire i Dati dei Pixel

Un pixel in modalità RGB è una tupla di tre interi — `(red, green, blue)` — ognuno che va da 0 a 255.

| Colore | RGB |
|-------|-----|
| Rosso | (255, 0, 0) |
| Verde | (0, 255, 0) |
| Blu | (0, 0, 255) |
| Bianco | (255, 255, 255) |
| Nero | (0, 0, 0) |
| Giallo | (255, 255, 0) |
| Ciano | (0, 255, 255) |
| Grigio | (128, 128, 128) |

`img.getpixel((x, y))` restituisce il colore di un pixel. Nota: x = colonna (sinistra→destra), y = riga (alto→basso).

## Ridimensionare e Creare Miniature

`image.resize((width, height))` crea una nuova immagine alla dimensione richiesta.
L'originale non viene modificato — le operazioni di Pillow restituiscono sempre una nuova immagine.

```python
from PIL import Image

img = Image.open("photo.jpg")
small = img.resize((200, 150))
small.save("photo_small.jpg")
```

`image.thumbnail((max_width, max_height))` è più intelligente — rimpicciolisce l'immagine per adattarla al riquadro **mantenendo le proporzioni**. Modifica l'immagine sul posto:

```python
img.thumbnail((400, 400))   # fits in 400×400 box, keeps proportions
```

## Ritagliare le Immagini

`image.crop((left, upper, right, lower))` estrae una regione rettangolare.
I quattro numeri sono coordinate in pixel misurate dall'angolo in alto a sinistra.

```python
# Crop a 100×100 region starting at pixel (50, 30):
region = img.crop((50, 30, 150, 130))
region.save("cropped.jpg")
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-2"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-2')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-2')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-2"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-2"></div>
  </div>
</div>
<script>
initCmLab('-2', `from PIL import Image

# Create a 10x10 image with a color gradient:
img = Image.new("RGB", (10, 10))
for y in range(10):
    for x in range(10):
        r = int(x / 9 * 255)
        g = int(y / 9 * 255)
        b = 100
        img.putpixel((x, y), (r, g, b))

print("Original size:", img.size)

# Crop the top-right quadrant:
cropped = img.crop((5, 0, 10, 5))
print("Cropped size:", cropped.size)
print("Cropped pixel (0,0):", cropped.getpixel((0, 0)))
print("Cropped pixel (4,4):", cropped.getpixel((4, 4)))`);
</script>

## Specchiare e Ruotare

`image.transpose(method)` specchia o ruota l'immagine.
Le costanti del metodo vivono in `Image.Transpose` (o nel namespace `Image` più vecchio):

```python
from PIL import Image

img = Image.open("photo.jpg")
flipped_h = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)   # mirror horizontally
flipped_v = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)   # mirror vertically
rotated   = img.rotate(90)                                    # rotate 90° counter-clockwise
```

`img.rotate(angle)` ruota dell'angolo dato — gli angoli positivi ruotano in senso antiorario.

## Conversione della Modalità di Colore

`image.convert(mode)` cambia la modalità di colore di un'immagine.

Le conversioni più comuni sono:

| Conversione | Cosa fa |
|------------|-------------|
| `img.convert("L")` | Converti in scala di grigi (L = luminanza) |
| `img.convert("RGB")` | Converti in colore a 3 canali |
| `img.convert("RGBA")` | Aggiungi il canale di trasparenza |
| `img.convert("1")` | Converti in bianco e nero a 1 bit |

Convertire in scala di grigi è un modo semplice di applicare un classico effetto fotografico:

```python
from PIL import Image

img  = Image.open("photo.jpg")
gray = img.convert("L")
gray.save("photo_grayscale.jpg")
```

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-3"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-3')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-3')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-3"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-3"></div>
  </div>
</div>
<script>
initCmLab('-3', `from PIL import Image

# Create a small color image, then convert it to grayscale:
img = Image.new("RGB", (4, 4))
colors = [
    (255, 0,   0),   (0,   255, 0),   (0,   0,   255), (255, 255, 0),
    (255, 0, 255),   (0,   255, 255), (128, 0,   0),   (0,   128, 0),
    (0,   0, 128),   (128, 128, 0),   (128, 0,   128), (0,   128, 128),
    (255, 128, 0),   (128, 255, 0),   (0,   255, 128), (0,   128, 255),
]
for i, c in enumerate(colors):
    img.putpixel((i % 4, i // 4), c)

gray = img.convert("L")

print("Original RGB pixels (row 0):")
for x in range(4):
    print(f"  ({x},0): {img.getpixel((x, 0))}")

print("Grayscale pixels (row 0):")
for x in range(4):
    print(f"  ({x},0): {gray.getpixel((x, 0))}")`);
</script>

## Applicare Filtri

Il modulo `ImageFilter` di Pillow fornisce filtri già pronti:

```python
from PIL import Image, ImageFilter

img = Image.open("photo.jpg")

blurred   = img.filter(ImageFilter.BLUR)
sharpened = img.filter(ImageFilter.SHARPEN)
edges     = img.filter(ImageFilter.FIND_EDGES)
embossed  = img.filter(ImageFilter.EMBOSS)

edges.save("edges.png")
```

I filtri funzionano esaminando i vicini di ogni pixel e calcolando un nuovo valore — un processo chiamato **convoluzione**.

## Salvare le Immagini

`image.save(filepath)` salva in qualsiasi formato supportato.
Pillow rileva il formato dall'estensione del file:

```python
img.save("output.png")   # saves as PNG
img.save("output.jpg", quality=85)   # JPEG with quality setting (1-95)
img.save("output.bmp")   # BMP format
```

Per JPEG: qualità più bassa = file più piccolo ma più artefatti visivi. Qualità 80–90 è di solito un buon equilibrio.

## Verifica di Apprendimento

!!! mascot-thinking "Il Tuo Turno — Scrivi un Potenziatore di Luminosità"
    ![Monty thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Il codice sotto ha una funzione stub per `brighten(image, amount)`.
    Completala: per ogni pixel, aggiungi `amount` a ogni canale R, G, B — ma limita il risultato tra 0 e 255!

<div class="cm-lab cm-text-only">
  <div class="cm-editor-wrap">
    <div id="cm-editor-4"></div>
    <div class="cm-button-row">
      <button class="cm-run-btn" onclick="runCmLab('-4')">&#9654; Run</button>
      <button class="cm-reset-btn" onclick="resetCmLab('-4')">&#8635; Reset</button>
    </div>
    <pre class="cm-output" id="cm-output-4"></pre>
  </div>
  <div class="cm-canvas-wrap">
    <div id="cm-turtle-4"></div>
  </div>
</div>
<script>
initCmLab('-4', `from PIL import Image

def brighten(img, amount):
    result = Image.new("RGB", img.size)
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            # Add 'amount' to each channel, but clamp between 0 and 255:
            nr = r   # TODO: add amount and clamp
            ng = g   # TODO: add amount and clamp
            nb = b   # TODO: add amount and clamp
            result.putpixel((x, y), (nr, ng, nb))
    return result

# Test with a simple 3x3 image:
img = Image.new("RGB", (3, 3), (100, 150, 200))
print("Before brighten:", img.getpixel((0, 0)))
bright = brighten(img, 80)
print("After brighten:", bright.getpixel((0, 0)))`);
</script>

## Esperimenti

Prova questi cambiamenti. Prevedi cosa succederà prima, poi eseguilo per verificare!

1. Crea un'immagine 100×100 dove il valore R di ogni pixel è uguale alla sua coordinata x e il valore G è uguale alla sua coordinata y. Salvala come PNG e aprila.
   **Saprai che ha funzionato quando** vedi un gradiente che passa da scuro a brillante in due direzioni.

2. Apri una foto JPEG e usa `thumbnail((300, 300))` per rimpicciolirla, poi salvala come PNG.
   **Saprai che ha funzionato quando** il file di output è un'immagine più piccola in formato PNG.

3. Converti un'immagine RGB in scala di grigi e poi riconvertila in RGB. Stampa un pixel — è lo stesso dell'originale?
   **Saprai che ha funzionato quando** vedi che il colore grigio ha valori R, G, B uguali.

4. Usa `img.rotate(45)` su una foto. Nota che gli angoli sono neri (riempimento di sfondo). Aggiungi `expand=True` per vedere la differenza.
   **Saprai che ha funzionato quando** `expand=True` fa crescere il canvas per mostrare l'intera immagine ruotata.

5. Applica `ImageFilter.FIND_EDGES` a una foto. Salva il risultato e confrontalo con l'originale.
   **Saprai che ha funzionato quando** vedi linee brillanti dove l'originale aveva bordi di colore.

!!! mascot-celebration "Mago delle Immagini!"
    ![Monty celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Ora puoi aprire, ispezionare, trasformare, filtrare, e salvare immagini con Python!
    Queste stesse tecniche alimentano i sistemi di visione artificiale, le app di editing fotografico, e le pipeline di machine learning.
    Il prossimo capitolo ritorna alla grafica turtle per l'animazione guidata da eventi. Continuiamo a programmare!

[Fai il Quiz di Ripasso del Capitolo](./quiz.md)

[Vedi i Riferimenti Annotati](./references.md)
