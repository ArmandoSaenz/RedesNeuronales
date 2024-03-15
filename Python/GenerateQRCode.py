import qrcode

def generar_qr(texto, nombre_archivo):
    # Crear un objeto QRCode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    
    # Agregar los datos al objeto QRCode
    qr.add_data(texto)
    
    # Compilar el código QR
    qr.make(fit=True)
    
    # Crear una imagen PIL (Python Imaging Library) a partir del código QR
    imagen_qr = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen QR en un archivo
    imagen_qr.save(nombre_archivo)

# Texto que quieres convertir en código QR
texto_a_convertir = "¡Hola, mundo!"

# Nombre del archivo donde se guardará el código QR (con extensión .png, .jpg, etc.)
nombre_archivo = "codigo_qr.png"

# Generar el código QR
generar_qr(texto_a_convertir, nombre_archivo)

print(f"El código QR se ha generado y guardado como '{nombre_archivo}'.")
