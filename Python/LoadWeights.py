# Fecha: 06 de Marzo de 2024
# Script para cargar los pesos de guardados
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Cargar y preparar datos (en este caso, no necesitamos los datos de entrenamiento)
(_, _), (test_images, test_labels) = datasets.mnist.load_data()
test_images = test_images / 255.0
test_images = test_images[..., tf.newaxis]

# Definir el modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Cargar los pesos guardados en el archivo model_weights.h5
model.load_weights('model_weights.h5')

# Evaluar el modelo cargado en los datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
