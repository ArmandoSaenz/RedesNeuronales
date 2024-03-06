import cv2

# Función que se activará con el evento de clic del mouse
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Coordenadas del punto central del clic
        centerX, centerY = x, y
        
        # Calcular las coordenadas del cuadro de 25x25 píxeles alrededor del clic
        topLeftX = max(centerX - 12, 0)
        topLeftY = max(centerY - 12, 0)
        bottomRightX = min(centerX + 13, imagen.shape[1])
        bottomRightY = min(centerY + 13, imagen.shape[0])

        # Recortar la región de 25x25 píxeles
        cropped_image = imagen[topLeftY:bottomRightY, topLeftX:bottomRightX]
        
        # Redimensionar la imagen recortada a 150x150 píxeles
        resized_image = cv2.resize(cropped_image, (400, 400), interpolation=cv2.INTER_AREA)
        
        # Mostrar la imagen recortada y redimensionada en una nueva ventana
        cv2.imshow("Imagen Recortada y Redimensionada", resized_image)

# Cargar la imagen
imagen = cv2.imread('C:/Users/LapArmando/Pictures/Nexus.jpg')

# Verificar que la imagen se ha cargado correctamente
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
else:
    # Crear una ventana y asignarle un callback para el evento de clic
    cv2.namedWindow('Imagen')
    cv2.setMouseCallback('Imagen', click_event)

    # Mostrar la imagen original
    cv2.imshow('Imagen', imagen)

    # Esperar indefinidamente hasta que el usuario presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()

