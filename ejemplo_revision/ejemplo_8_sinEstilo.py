def main():
    # Crear una lista vacía para almacenar los valores
    lista_valores = []

    print("Ingresa valores para agregar a la lista. Presiona Enter sin ingresar un valor para terminar.")

    while True:
        # Solicitar al usuario que ingrese un valor
        valor = input("Ingresa un valor (o presiona Enter para terminar): ")
        
        # Salir del bucle si el usuario presiona Enter sin ingresar un valor
        if valor == "":
            break
        
        # Agregar el valor a la lista
        lista_valores.append(valor)

        # Mostrar la lista actualizada
        print(f"Valores ingresados: {', '.join(lista_valores)}")

    # Mostrar la lista final
    print("Lista final de valores:", lista_valores)

if __name__ == "__main__":
    main()
