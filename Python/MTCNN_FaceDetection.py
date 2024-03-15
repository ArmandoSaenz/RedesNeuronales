#Requiere de las librerías
# opencv-python o opencv-python-headless
# facenet-pytorch

import cv2
from facenet_pytorch import MTCNN
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Crear una instancia de MTCNN
mtcnn = MTCNN(keep_all=True, device=device)

#Imagen a sustituir
substitute_image = cv2.imread('imagen a sustituir')

# Inicializar la captura de video de la cámara web
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    if not ret:
        break
    
    frame = cv2.rotate(frame, cv2.ROTATE_180_COUNTERCLOCKWISE)

    # Convertir el frame a RGB para MTCNN
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detectar rostros en el frame
    boxes, _ = mtcnn.detect(frame_rgb)

    # Dibujar los cuadros alrededor de los rostros detectados
    if boxes is not None:
        for box in boxes:
            # Coordenadas del rectángulo para OpenCV
            start_point = (int(box[0]), int(box[1]))
            end_point = (int(box[2]), int(box[3]))
            color = (255, 0, 0)  # Color del rectángulo, en BGR
            thickness = 2  # Espesor del rectángulo
            #frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
            w = int(box[2]) - int(box[0])
            h = int(box[3]) - int(box[1])
            substitute_resized = cv2.resize(substitute_image, (w, h))
            frame[int(box[1]):int(box[3]), int(box[0]):int(box[2])] = substitute_resized

    # Mostrar el frame resultante
    cv2.imshow('Video', frame)
    
    # Romper el ciclo con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Al final, liberar la captura
cap.release()
cv2.destroyAllWindows()
