import cv2
import numpy as np

# Cargar la imagen original
imagen = cv2.imread('Wheel1.jpg')

print(imagen.shape)
#540

#640
#1280
#1920
imagen1 = imagen[0:540,0:640]
imagen2 = imagen[0:540,640:1280]
imagen3 = imagen[0:540,1280:1920]
imagen4 = imagen[540:1080,0:640]
imagen5 = imagen[540:1080,640:1280]
imagen6 = imagen[540:1080,1280:1920]
cv2.imwrite("Rueda1.jpg",imagen1)
cv2.imwrite("Rueda2.jpg",imagen2)
cv2.imwrite("Rueda3.jpg",imagen3)
cv2.imwrite("Rueda4.jpg",imagen4)
cv2.imwrite("Rueda5.jpg",imagen5)
cv2.imwrite("Rueda6.jpg",imagen6)
