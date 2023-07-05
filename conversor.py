import os
import rawpy
from PIL import Image

def convertir_nef_a_jpg(carpeta_nef, carpeta_jpg):
    # Verificar si la carpeta de salida no existe, crearla si es necesario
    if not os.path.exists(carpeta_jpg):
        os.makedirs(carpeta_jpg)

    # Recorrer los archivos en la carpeta NEF
    for archivo in os.listdir(carpeta_nef):
        if archivo.endswith(".NEF"):
            archivo_nef = os.path.join(carpeta_nef, archivo)
            archivo_jpg = os.path.splitext(archivo)[0] + ".jpg"
            archivo_jpg = os.path.join(carpeta_jpg, archivo_jpg)

            # Abrir el archivo NEF con rawpy
            with rawpy.imread(archivo_nef) as raw:
                # Obtener la imagen en formato RGB
                imagen_rgb = raw.postprocess()

            # Crear un objeto de imagen PIL desde la matriz RGB
            imagen_pil = Image.fromarray(imagen_rgb)

            # Guardar la imagen en formato JPEG con la mayor calidad
            imagen_pil.save(archivo_jpg, "JPEG", quality=100)

            print(f"Convertido: {archivo_nef} -> {archivo_jpg}")

# Ruta de la carpeta que contiene las imágenes .NEF
carpeta_nef = "RUTA COMPLETA"

# Ruta de la carpeta de salida para las imágenes .jpg convertidas
carpeta_jpg = "RUTA COMPLETA"
# Llamar a la función para convertir las imágenes
convertir_nef_a_jpg(carpeta_nef, carpeta_jpg)

