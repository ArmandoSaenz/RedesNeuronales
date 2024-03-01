# Fecha 28 de Febrero de 2024
# Script para crear una red neuronal que pueda digitalizar números scritos a mano
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Cargar y preparar datos
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Agregar una dimensión de canal a las imágenes
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

# Definir el modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

# Guardar los pesos del modelo entrenado
model.save_weights('model_weights.h5')

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)
