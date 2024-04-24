import cv2
import numpy as np
#Abriendo conexion con la cámara
camera = cv2.VideoCapture(0)
#Leyendo una imagen de la cámara
ret, frame = camera.read()
if ret:
    cv2.imshow("Foto", frame)
    b,g,r = cv2.split(frame)
    value = b+g+r
    print(np.amin(g))
    cv2.waitKey(0) 
camera.release()
cv2.destroyAllWindows()
