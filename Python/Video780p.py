import cv2

# Iniciar la captura de video de la webcam (el índice 0 se refiere a la webcam predeterminada)
cap = cv2.VideoCapture(1)
# Ajustar la resolución a 720p
# Estas líneas establecen la anchura (WIDTH) a 1280 y la altura (HEIGHT) a 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # Leer un fotograma del video
    ret, frame = cap.read()

    if ret:
        # Guardar la imagen capturada
        cv2.imshow('foto_webcam.jpg', frame)
        presskey = cv2.waitKey(1)
        if presskey == ord('q') or presskey == ord('Q'):
            break
    else:
        print("Error al capturar la imagen.")

# Liberar la cámara y cerrar todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()
