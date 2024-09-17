import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configurar el servicio con el path del controlador
service = Service(executable_path='drivers/chromedriver.exe')

# Iniciar el controlador del navegador usando el servicio
driver = webdriver.Chrome(service=service)

try:
    # Abrir la página web donde se cargará el archivo
    driver.get('http://localhost/glpi/index.php?noAUTO=1')

    # Esperar hasta que los campos de usuario y contraseña estén presentes
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'login_name')))
    password_field = wait.until(EC.presence_of_element_located((By.ID, 'login_password')))
    
    # Enviar las credenciales
    username_field.send_keys('glpi')
    password_field.send_keys('glpi')
    
    # Esperar hasta que el botón de inicio de sesión esté presente y hacer clic
    login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'submit')))
    login_button.click()
    
    # Esperar hasta que el campo de búsqueda esté presente
    search_field = wait.until(EC.presence_of_element_located((By.NAME, 'globalsearch')))
    search_field.send_keys('DFR0FC3')
    
    # Localizar y hacer clic en el botón de búsqueda
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div/div[1]/form/div/span/button')))
    search_button.click()

    # Esperar 30 segundos después de hacer la búsqueda
    time.sleep(1)
    
# Localizar y hacer clic en el primer valor de la tabla
    primer_elemento = wait.until(EC.element_to_be_clickable((By.XPATH, '//table/tbody/tr[1]/td[1]/a')))
    primer_elemento.click()

    time.sleep(1)
    

    documento_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabspanel"]/li[8]/a')))
    documento_button.click()
    
    time.sleep(1)

        
# Esperar hasta que el campo de carga de archivo sea clicable
    upload_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[8]/div[1]/form[1]/table/tbody/tr[2]/td[3]/div/input')))

    # Enviar la ruta del archivo
    upload_element.send_keys('C:\\Users\\julrojsa\\Documents\\jajaj.png')

    
 
    
    time.sleep(30)
finally:
    # Cerrar el navegador
    driver.quit()







# # Localizar el campo de carga de archivos (input de tipo file)
# upload_element = driver.find_element(By.ID, "file-upload")

# # Enviar el path del archivo que quieres cargar
# file_path = "/path/to/your/document.pdf"
# upload_element.send_keys(file_path)

# # Esperar un poco antes de cerrar el navegador para ver el resultado
# time.sleep(5)

# Cerrar el navegador



