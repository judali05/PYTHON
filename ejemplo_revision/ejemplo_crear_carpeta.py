import os

def crear_carpeta(ruta_carpeta):
    # Verificar si la carpeta ya existe
    if not os.path.exists(ruta_carpeta):
        # Crear la carpeta si no existe
        os.makedirs(ruta_carpeta)
        print(f"Carpeta creada: {ruta_carpeta}")
    else:
        # Si la carpeta ya existe, omitir la creación
        print(f"La carpeta ya existe: {ruta_carpeta}")

# Especifica la ruta donde quieres crear la carpeta
ruta_carpeta = r'C:\Users\julrojsa\Downloads\nueva_carpetassssss'

# Llamar a la función para crear la carpeta
crear_carpeta(ruta_carpeta)
