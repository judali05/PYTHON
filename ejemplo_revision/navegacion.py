from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def nav(lista_valores):
    #serial_number = driver.find_element(By.NAME, 'globalsearch').send_keys(seriales)
    
    

    print("Ingresa valores para agregar a la lista. Presiona Enter sin ingresar un valor para terminar.")

    while True:
        valor = input("Ingresa un valor (o presiona Enter para terminar): ")

        if valor == "":
            break

        lista_valores.append(valor)

        print(f"Valores ingresados: {', '.join(lista_valores)}")

    print("Lista final de valores:", lista_valores)
    
    
    

if __name__ == "__main__":
   main()
