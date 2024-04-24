#Instalar las librerias cv2, pyzbar
#pip install opencv-python
#pip install pyzbar

import cv2
from pyzbar.pyzbar import decode
import numpy as np

# Cargar la imagen
cap = cv2.VideoCapture(0)

while True:
    rest, imagen = cap.read();
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Decodificar códigos QR en la imagen
    codigos_qr = decode(imagen_gris)

    # Iterar sobre los códigos QR detectados
    for codigo_qr in codigos_qr:
        # Extraer la información del código QR
        datos = codigo_qr.data.decode('utf-8')
        
        # Obtener las coordenadas del contorno del código QR
        puntos = codigo_qr.polygon
        
        # Convertir las coordenadas a un arreglo NumPy
        puntos = np.array(puntos, dtype=np.int32)
        
        # Dibujar un contorno alrededor del código QR
        cv2.polylines(imagen, [puntos], True, (0, 255, 0), 2)
        
        # Mostrar la información del código QR
        cv2.putText(imagen, datos, (puntos[0][0], puntos[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(puntos)
    # Mostrar la imagen con los códigos QR detectados
    cv2.imshow('Codigos QR detectados', imagen)
    keyp = cv2.waitKey(1)
    if keyp == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
