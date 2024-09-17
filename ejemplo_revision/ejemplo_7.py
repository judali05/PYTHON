# Crear una lista vacía para almacenar los valores
lista_valores = []

# Bucle para solicitar y agregar valores a la lista hasta que el usuario decida parar
while True:
    valor = input("Ingresa un valor (o escribe 'fin' para terminar): ")
    
    if valor.lower() == 'fin':
        break  # Rompe el bucle si el usuario escribe 'fin'
    
    lista_valores.append(valor)  # Agrega el valor a la lista

# Mostrar la lista final
print("Los valores ingresados son:", lista_valores)
