# Fecha: 28 de febrero de 2024
# Script para guardar video y adquirir 
import cv2

def capture_video(camera_index=0):
    # Inicia la captura de video
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"No se pudo abrir la cámara con índice {camera_index}.")
        return

    # Define el codec y crea un objeto VideoWriter para MP4
    # Nota: En algunos sistemas, puedes necesitar cambiar 'mp4v' por 'avc1' o 'h264'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480), True)

    while True:
        # Captura cuadro por cuadro
        ret, frame = cap.read()
        
        if not ret:
            print("No se pudo recibir el cuadro. Saliendo...")
            break
        
        # Escribe el cuadro en el archivo (en MP4)
        out.write(frame)
        
        # Muestra el cuadro resultante
        cv2.imshow('frame', frame)
        
        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cuando todo esté hecho, libera la captura y el escritor
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video()
