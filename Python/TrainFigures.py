# Fecha 03 de Mayo de 2024
# Script para crear una red neuronal que pueda identificar entre un triangulo un cuadrado y un circulo
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import cv2
import numpy as np

#definiendo listas
train_images = []
train_labels = []
test_images = []
test_labels = []
for i in range(1,9):
    #Agregando triangulo
    url = f"fotos/t_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    print()
    image_normalized = image/255.0;
    train_images.append(image_normalized)
    train_labels.append(0);
    #Agregando triangulo
    url = f"fotos/s_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    image_normalized = image/255.0;
    train_images.append(image_normalized)
    train_labels.append(1);
    #Agregando triangulo
    url = f"fotos/c_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    image_normalized = image/255.0;
    train_images.append(image_normalized)
    train_labels.append(2);

for i in range(9,11):
    #Agregando triangulo
    url = f"fotos/t_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    image_normalized = image/255.0;
    test_images.append(image_normalized)
    test_labels.append(0);
    #Agregando triangulo
    url = f"fotos/s_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    image_normalized = image/255.0;
    test_images.append(image_normalized)
    test_labels.append(1);
    #Agregando triangulo
    url = f"fotos/c_{i}.jpg"
    print(url)
    image = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
    image_normalized = image/255.0;
    test_images.append(image_normalized)
    test_labels.append(2);

# Definir el modelo CNN
print(f"Cargando modelo")
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(3, activation='softmax')
])

# Compilar el modelo
print(f"Compilando")
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
print("Entrenando")
model.fit(np.array(train_images), np.array(train_labels), epochs=30, validation_data=(np.array(test_images), np.array(test_labels)))

# Guardar los pesos del modelo entrenado
model.save_weights('model_weights_tsc.h5')

# Evaluar el modelo
test_loss, test_acc = model.evaluate(np.array(test_images), np.array(test_labels))
print('Test accuracy:', test_acc)
