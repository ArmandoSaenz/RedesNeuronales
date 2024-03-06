import cv2
from matplotlib import pyplot as plt

# Cargar la imagen
imagen = cv2.imread('C:/Users/LapArmando/Pictures/Nexus.jpg')

# OpenCV carga las imágenes en formato BGR, así que convertimos a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Calcular los histogramas para cada canal
color = ('r','g','b')
for i, col in enumerate(color):
    histr = cv2.calcHist([imagen_rgb],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.title('Histograma de los Canales RGB')
plt.xlabel('Intensidad de Pixel')
plt.ylabel('Cantidad de Pixels')
plt.show()

