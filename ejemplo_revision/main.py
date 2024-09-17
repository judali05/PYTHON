from selenium import webdriver
from login import login
from navegacion import nav
import time
import getpass

def main():
    driver = webdriver.Chrome()
    
    try:
        username = str(input("Ingresa tu usuario: "))
        password = getpass.getpass("Ingresa tu contraseña: ")
        login(driver, username, password)

        time.sleep(5)


        lista_valores = []
       

        nav(lista_valores)        
        
          # Eliminar valores repetidos
        lista_valores = list(set(lista_valores))
 
        print(f"La cantidad de valores en el array son {len(lista_valores)}")
        print("Valores leídos desde el archivo:", lista_valores)
        # quitar los datos repetidos
        #que no ejecute si no aprueba el login
    except Exception as e:
        print(f"Se produjo un error: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()


