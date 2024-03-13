import cv2
import numpy as np

# Cargando imagen
image = cv2.imread('Monedas.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado para reducir el ruido
gray_blurred = cv2.medianBlur(gray, 5)

# Detectar círculos utilizando la transformada de Hough circular
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=50)

# Dibujar círculos detectados
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)

# Mostrar la imagen resultante
cv2.imshow('Imagen suavizada', gray_blurred)
cv2.imshow('Circulos detectados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
