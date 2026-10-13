# Classificazione di Cifre Scritte a Mano

Programmeremo e addestreremo un modello di machine learning per riconoscere numeri scritti a mano. Il codice per questa lezione si trova [qui](https://github.com/dmccreary/python/blob/master/advanced/machineLearning/mnist.ipynb).

## Ma Cos'È *Davvero* il Machine Learning?

Il processo di determinare la funzione che restituisce un risultato plausibile **y** per un insieme di input, nella forma di un vettore **x**. Nella sua forma più semplice, questo potrebbe essere la regressione lineare, dove troviamo la retta che meglio si adatta ai dati.

In forme più complesse, tuttavia, questo può essere addestrare una rete neurale per adattarsi a dati molto non lineari. Useremo un tipo di rete neurale per riconoscere i nostri numeri scritti a mano.

![Image of Machine Learning Algorithms](https://www.7wdata.be/wp-content/uploads/2017/04/CheatSheet.png)

## Tipi di Reti Neurali
![Types of Neural Networks](https://miro.medium.com/max/4000/1*cuTSPlTq0a_327iTPJyD-Q.png)

Come puoi vedere, ci sono molti tipi diversi, o **architetture**, di reti neurali. Alcune delle più comuni sono le reti neurali Feed Forward, Ricorrenti, LSTM, e AutoEncoder. L'altra più comune è quella che useremo, cioè una Rete Neurale Convoluzionale.

## Rete Neurale Convoluzionale
Poiché abbiamo dati di immagini, useremo una Rete Neurale Convoluzionale (CNN). Una CNN funziona facendo scorrere delle "finestre" sopra l'immagine in ingresso e aggregando insieme i pixel vicini.
![CNN Windowing](https://miro.medium.com/max/790/1*nYf_cUIHFEWU1JXGwnz-Ig.gif)

## Importare i Pacchetti
Per questo progetto, useremo un pacchetto di machine learning chiamato Keras. Questo rende davvero facile costruire la nostra rete neurale. Importiamo anche matplotlib per visualizzare i nostri dati, e numpy per alcune utilità.
```python
import keras
from keras.datasets import mnist  # Get dataset
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten  # Need these types of layers
from keras.layers import Conv2D, MaxPooling2D  # Need convolutional layers

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

import numpy as np 
```

## Caricare i Dati
È importante caricare sia un insieme di addestramento che uno di test per assicurarsi che la CNN non stia "memorizzando" l'insieme di immagini su cui si addestrerà. Questo porterebbe a una pessima accuratezza nel "mondo reale"
```python
# input image dimensions (pixels)
img_rows, img_cols = 28, 28

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# manipulate the data for the CNN
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)
```

## Preelaborazione dei Dati
Vogliamo che la nostra CNN lavori con numeri tra 0 e 1. Poiché i valori dei pixel vanno da 0 a 255, dividiamo tutti i numeri per 255 per portarli tra 0 e 1. Possiamo poi vedere quanti campioni di addestramento e di test abbiamo.
```python
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
```
## Osservare i Dati
Nelle prossime celle, osserveremo un esempio di cifra e vedremo quale numero è nell'insieme di addestramento.

```python
x_train[0]
```
```python
pixels = x_train[0].reshape((28, 28))

plt.imshow(pixels, cmap='gray')
```
```python
print(y_train[0])
```

## Output Desiderato
Vogliamo convertire l'output desiderato da un numero n a un vettore dove l'ennesimo elemento è 1 e il resto sono 0.

Esempio: n = 5 Vettore Risultante = {0, 0, 0, 0, 0, 1, 0, 0, 0, 0}

```python
num_classes = 10

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
```

## Definire il Modello
Ed ecco la parte divertente. Costruire il modello! Avremo una rete neurale a 5 livelli. Sentiti libero di giocare con alcuni dei parametri e vedere cosa funziona meglio o peggio!

```python
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # Prevent overfitting
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.summary()
```

## Impostare i Parametri
Qui, impostiamo due parametri per la rete. Il primo è la dimensione del batch, che determina quanti esempi di addestramento osserveremo prima di cambiare i pesi nel modello. Imposteremo anche il numero di epoche, ovvero le iterazioni attraverso l'intero insieme di addestramento.

```python
batch_size = 128  # How many training examples will we look at before updating the weights in the matrix
epochs = 12 # How many times we will run through the complete training set
```

## Compilare e Addestrare il Modello
Qui, compiliamo il modello e poi lo addestriamo. Un paio di cose da notare. Stiamo usando l'ottimizzatore Adam, rispetto ad altri come la discesa del gradiente stocastica. Misuriamo il successo del modello attraverso la metrica di perdita categorical crossentropy, che determina come aggiustare i pesi all'interno del modello.

```python
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adam(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
```
## Testare il Modello
Ed ecco il gran finale, vediamo quanto bene si comporta il modello! Lo faremo eseguendo il nostro insieme di test e facendo produrre al modello una previsione. Per fortuna, c'è già una funzione integrata nel modello per questo.
```python
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

Vediamo cosa succede a livello di singola immagine:
```python
to_predict = np.array([x_test[0]])

output = model.predict(to_predict)

pixels = to_predict[0].reshape((28, 28))

plt.imshow(pixels, cmap='gray')
```
```python
output
```
```python
np.argmax(output)
```
Ed ecco fatto! Congratulazioni per aver creato, addestrato e testato con successo la tua rete neurale.
