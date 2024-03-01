# 28 de Febrero de 2024
# Script para mostrar la cantidad de cámaras disponibles en la computadora
# Comando para instalar la librería opencv
# pip install opencv-python
import cv2

def list_cameras(max_checks=10):
    # Inicializa el arreglo
    available_cameras = []
    # Ciclo para revisar el maximo de cámaras indicadas
    for i in range(max_checks):
        # Abre comunicación con la cámara i
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        # Detecta si abrio la cámara y agrega el número de indice al arreglo
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
        else:
            break  # Acaba el bucle en el indice que ya no pueda abrir
    return available_cameras

cameras = list_cameras()
if cameras:
    print(f"Cámaras detectadas en los índices: {cameras}")
else:
    print("No se detectaron cámaras.")
