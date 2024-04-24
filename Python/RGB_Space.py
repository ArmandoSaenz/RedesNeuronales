#La cantidad de puntos en el espacio RGB discretizado a 8 bits
# es de 256*256*256 = 16,777,216
# 256*256 = 65,536
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

raxis = np.full(1,0)
gaxis = np.full(256,0)
baxis = np.full(65536,0)
for i in range(1,256, 3):
    raxis = np.hstack((raxis,i))
    gaxis = np.hstack((gaxis,np.full(256, i)))
    baxis = np.hstack((baxis,np.full(65536, i)))
raxis = np.tile(raxis, 65536)
gaxis = np.tile(gaxis, 256)
print(raxis.shape)
print(gaxis.shape)
print(baxis.shape)
# Dibujar la nube de puntos en 3D
# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(raxis,gaxis,baxis, c=colors)
ax.scatter(raxis,gaxis,baxis)
# Personalizar el gráfico
ax.set_title('Espacio RGB')
ax.set_xlabel('Rojo')
ax.set_ylabel('Verde')
ax.set_zlabel('Azul')

# Mostrar el gráfico
plt.show()
