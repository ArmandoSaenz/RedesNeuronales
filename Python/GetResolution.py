import cv2

def get_available_resolutions(camera_index=0):
    # Inicializar la cámara
    camera = cv2.VideoCapture(camera_index)
    
    # Obtener las resoluciones soportadas
    resolutions = []
    for i in range(100):
        # Intentar cambiar a la siguiente resolución
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, i)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, i)
        
        # Leer la resolución actual
        width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Verificar si se ha alcanzado el final de las resoluciones soportadas
        if width == 0 or height == 0:
            break
        
        # Agregar la resolución a la lista
        resolutions.append((width, height))
    
    # Liberar la cámara
    camera.release()
    
    return resolutions

resolutions = get_available_resolutions(camera_index=1)
print("Resoluciones disponibles:")
for resolution in resolutions:
    print(f"{resolution[0]}x{resolution[1]}")
