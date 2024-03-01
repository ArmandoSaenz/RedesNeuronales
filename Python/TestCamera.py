# Fecha: 28 de Febrero de 2024
# Script para tomar una foto de la cámara (trigger)

import cv2

def check_camera(index=0):
    # Abriendo la cámara
    cap = cv2.VideoCapture(index)
    # En caso de no poderse abrir manda el error y acaba la rutina
    if not cap.isOpened():
        print(f"La cámara con índice {index} no pudo ser abierta.")
        return
    
    print(f"La cámara con índice {index} es compatible y ha sido abierta exitosamente.")
    
    # Captura un cuadro de video para verificar que la cámara funciona
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f"Prueba de la Cámara {index}", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"La cámara con índice {index} no pudo capturar un cuadro.")

    # Libera la cámara
    cap.release()

# Pruebando la cámara
check_camera(0)

