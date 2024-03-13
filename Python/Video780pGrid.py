import cv2

def grid(img, paso=28):
    altura = img.shape[0]
    ancho = img.shape[1]
    color = (0, 255, 0) 
    grosor = 1 
    
    for x in range(0, ancho, paso):
        cv2.line(img, (x, 0), (x, altura), color, grosor)
    
    for y in range(0, altura, paso):
        cv2.line(img, (0, y), (ancho, y), color, grosor)
def square(img)
    color = (0, 255, 0) 
    grosor = 1 
    topLeftX = 280
    topLeftY = 112
    bottomRightX = topLeftX+28
    bottomRightY = topLeftY+28
    imgcp = img.copy()
    cv2.line(imgcp, (topLeftX, topLeftY),(topLeftX,bottomRightY), color, grosor)
    cv2.line(imgcp, (topLeftX,bottomRightY),(bottomRightX,bottomRightY), color, grosor)
    cv2.line(imgcp, (bottomRightX,bottomRightY),(bottomRightX,topLeftY), color, grosor)
    cv2.line(imgcp, (bottomRightX,topLeftY),(topLeftX, topLeftY), color, grosor)
    return imgcp
    
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
        print(frame.shape)
        # Guardar la imagen capturada
        #grid(frame)
        cv2.imshow('digito', square(frame))
        presskey = cv2.waitKey(1)
        if presskey == ord('q') or presskey == ord('Q'):
            topLeftX = 280
            topLeftY = 112
            bottomRightX = topLeftX+28
            bottomRightY = topLeftY+28 
            cropped_image = frame[topLeftY:bottomRightY, topLeftX:bottomRightX]
            cv2.imwrite("digito.jpg",cropped_image)
            break
    else:
        print("Error al capturar la imagen.")

# Liberar la cámara y cerrar todas las ventanas abiertas
cap.release()
cv2.destroyAllWindows()
