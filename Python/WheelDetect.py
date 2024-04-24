import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('C:/Users/Jose Armando/Dropbox/Viar/20240410_132327.jpg')
print(imagen.shape)
# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Aplicar un desenfoque gaussiano para reducir el ruido
desenfoque = cv2.GaussianBlur(gris, (7, 7), 1.5)
# Detectar círculos utilizando la Transformada de Hough
circulos = cv2.HoughCircles(desenfoque, cv2.HOUGH_GRADIENT, dp=1, minDist=1,
                            param1=60, param2=30, minRadius=50, maxRadius=100)

# Asegurarse de que se encontró al menos un círculo
if circulos is not None:
    circulos = np.round(circulos[0, :]).astype("int")
    for (x, y, r) in circulos:
        # Dibujar el círculo externo
        cv2.circle(imagen, (x, y), r, (0, 255, 0), 4)
        # Dibujar el centro del círculo
        cv2.rectangle(imagen, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
# Mostrar la imagen con los círculos detectados
cv2.imshow('Llantas Detectadas', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
