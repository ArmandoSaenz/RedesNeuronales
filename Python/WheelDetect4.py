import cv2
import numpy as np

# Leer imagen
image = cv2.imread('Wheel1.jpg', cv2.IMREAD_GRAYSCALE)

# Configurar parámetros para el detector de blobs
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = True
params.blobColor = 20

# Crear un detector de blobs con los parámetros configurados
detector = cv2.SimpleBlobDetector_create(params)

# Detectar blobs
keypoints = detector.detect(image)

# Dibujar círculos alrededor de los blobs detectados en la imagen original
blobs_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255),
                                cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# Mostrar imagen con blobs detectados
cv2.imshow('Blobs Detected', blobs_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
