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

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

ret, frame = cap.read()
print(frame.shape)
if ret:
    grid(frame)
    cv2.imshow('Image', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error al capturar la imagen.")
cap.release()
