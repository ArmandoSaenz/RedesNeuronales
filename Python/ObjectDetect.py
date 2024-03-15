#Importando la librería de opencv
import cv2

#Abriendo comunicación con la cámara
cap = cv2.VideoCapture(0)
while True:
    # Tomando captura
    res, frame =  cap.read()

    if res:
        # Mostrar imagen
        cv2.imshow('Imagen Original', frame)
        # Convertir a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar desenfoque Gaussiano
        desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
        # Detección de bordes Canny
        bordes = cv2.Canny(desenfoque, 10, 150)
        # Encontrar contornos
        contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contornos_superiores = [contorno for i, contorno in enumerate(contornos) if jerarquia[0][i][3] == -1]
        # Dibujar contornos
        cv2.drawContours(frame, contornos_superiores, -1, (0, 255, 0), 3)
        print(len(contornos))
        # Mostrar resultados
        cv2.imshow('Objetos Detectados', frame)
    keyp = cv2.waitKey(1)
    if keyp == ord('q') or keyp == ord('Q'):
        break
cap.release()
cv2.destroyAllWindows()
