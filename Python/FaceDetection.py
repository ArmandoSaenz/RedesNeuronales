#Instalar librería opencv
#pip install opencv-python

import cv2
cap = cv2.VideoCapture(0)

substitute_image = cv2.imread('imagen a sustituir')

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
  ret,frame = cap.read()
  frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = faceClassif.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    substitute_resized = cv2.resize(substitute_image, (w, h))
    input_image[y:y+h, x:x+w] = substitute_resized
  cv2.imshow('frame',frame)
  keyp = cv2.waitKey(1)
  if  keyp == ord('q') or keyp == ord('Q'):
    break
cv2.imwrite("rostro.jpg", frame)
cap.release()
cv2.destroyAllWindows()
