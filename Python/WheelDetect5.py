import cv2
import numpy as np

# Cargar la imagen original
imagen = cv2.imread('Wheel1.jpg')

# Convertir la imagen de BGR a HSV
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de color que quieres detectar
# Por ejemplo, para detectar el color verde
verde_bajo = np.array([0, 0, 0])
verde_alto = np.array([200, 30, 200])

# Crear una máscara que identifique los píxeles dentro del rango verde
mascara = cv2.inRange(hsv, verde_bajo, verde_alto)

# Opcional: aplicar la máscara para obtener el resultado sobre la imagen original
resultado = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Mostrar la máscara y el resultado
cv2.imshow('Mascara', imagen)
cv2.imshow('Imagen Filtrada', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
