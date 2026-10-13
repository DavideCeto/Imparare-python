## Barre Colorate sul Canvas
Possiamo disegnare direttamente nel canvas di Jupyter Lab usando il componente di disegno Canvas.

Quello che segue disegna diverse barre orizzontali di colori diversi.

```python
from ipycanvas import Canvas

canvas = Canvas(width=400, height=170)

# draw a some lines of different colors and widths

canvas.translate(10,10)

canvas.fill_style = 'red';
canvas.fill_rect(0, 0, 400, 10)

canvas.fill_style = 'orange';
canvas.fill_rect(0, 25, 400, 10)

canvas.fill_style = 'yellow';
canvas.fill_rect(0, 50, 400, 10)

canvas.fill_style = 'green';
canvas.fill_rect(0, 75, 400, 10)

canvas.fill_style = 'blue';
canvas.fill_rect(0, 100, 400, 10)

canvas.fill_style = 'purple';
canvas.fill_rect(0, 125, 400, 10)

canvas.fill_style = 'pink';
canvas.fill_rect(0, 150, 400, 10)

canvas
```
# Esperimenti
Riesci a modificare quanto sopra per usare una lista di colori e un ciclo for?
La lista dei colori potrebbe essere:

## Usare le Liste
```
from ipycanvas import Canvas
canvas = Canvas(width=400, height=250)

colors =['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown',
         'cyan', 'lightgreen', 'lightblue']
canvas.font = '16px serif'

# draw some boxes of different colors

canvas.translate(10,10)
for i in range(len(colors)):
   canvas.fill_style = colors[i];
   canvas.fill_text(colors[i], 0, 25*i + 10)
   canvas.fill_rect(70, i*25, 400, 15)

canvas
```