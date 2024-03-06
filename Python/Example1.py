# Fecha: 06 de Marzo de 2024
# Evaluar una imagen
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import models
#Carga la imagen
image = cv2.imread('ruta_de_la_imagen.jpg', cv2.IMREAD_GRAYSCALE)
#La ajusta a una resolución de 28 x 28 pixeles
image_resized = cv2.resize(image, (28, 28))
#Preparación de los datos
image_normalized = image_resized / 255.0
image_normalized = np.expand_dims(image_normalized, axis=-1)
image_normalized = np.expand_dims(image_normalized, axis=0)
#Se carga la red neuronal
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
#Se cargan los pesos
model.load_weights('model_weights.h5')
#Se realiza la predicción
predictions = model.predict(image_normalized)
#Se identifica el número con mayor porcentaje
predicted_class = np.argmax(predictions)
#Se imprime la salida
print("Clase predicha:", predicted_class)
