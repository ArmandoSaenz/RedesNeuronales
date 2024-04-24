#Agregar libreria OpenCV
#opencv-python
import cv2

#Establecer comunicación con la camara
cap = cv2.VideoCapture(0)
first = False
step = 100
#Coordenadas square
topsquare = 160
leftsquare = 258
bottomsquare = topsquare + step
rightsquare = leftsquare + step
#Coordenadas triangle
toptriangle = 30
lefttriangle = 380
bottomtriangle = toptriangle + step
righttriangle = lefttriangle + step
#Coordenadas circle
topcircle = 260
leftcircle = 405
bottomcircle = topcircle + step
rightcircle = leftcircle + step
#Ciclo para obtener las imagenes
while True:
    rest, frame = cap.read()
    framesquare = frame[topsquare:bottomsquare, leftsquare:rightsquare]
    frametriangle = frame[toptriangle:bottomtriangle, lefttriangle:righttriangle]
    framecircle = frame[topcircle:bottomcircle, leftcircle:rightcircle]
    if rest:
        if not first:
            print(frame.shape)
            first = True
        cv2.imshow("Imagen original", frame)
        cv2.imshow("Crop square", framesquare)
        cv2.imshow("Crop triangle", frametriangle)
        cv2.imshow("Crop circle", framecircle)
        keypress = cv2.waitKey(1)
        if keypress == ord('Q') or keypress == ord('q'):
            break
    else:
        print("Imagen no capturada")
        break
cap.release()
cv2.destroyAllWindows()
