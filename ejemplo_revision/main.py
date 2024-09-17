from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from login import login
import time
import getpass

def main():
    service = Service(executable_path='drivers/chromedriver.exe')
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        
        username = str(input("Ingresa tu usuario: "))
        password = getpass.getpass("Ingresa tu contraseña: ")
        
        login(driver, username, password)

        time.sleep(6)

    except Exception as e:
        print(f"Se produjo un error: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
