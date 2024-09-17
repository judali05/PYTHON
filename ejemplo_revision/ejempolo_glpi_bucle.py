import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import shutil
from PySide6.QtWidgets import QApplication, QFileDialog

# Función para seleccionar múltiples archivos
def seleccionar_archivos():
    app = QApplication([])
    archivos, _ = QFileDialog.getOpenFileNames(None, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
    app.quit()
    return archivos

# Función principal para cargar archivos a GLPI
def cargar_archivos_a_glpi(archivos):
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
        search_field.send_keys('cnc12345678')

        # Localizar y hacer clic en el botón de búsqueda
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div/div[1]/form/div/span/button')))
        search_button.click()

        # Esperar 1 segundo después de hacer la búsqueda
        time.sleep(1)

        # Localizar y hacer clic en el primer valor de la tabla
        primer_elemento = wait.until(EC.element_to_be_clickable((By.XPATH, '//table/tbody/tr[1]/td[1]/a')))
        primer_elemento.click()

        time.sleep(1)

        # Navegar a la pestaña de documentos
        documento_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabspanel"]/li[13]/a')))
        documento_button.click()

        time.sleep(1)

        # Subir archivos uno por uno en un bucle
        for archivo in archivos:
            upload_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[13]/div[1]/form/table/tbody/tr[2]/td[3]/div/input')))
            upload_element.send_keys(archivo)
            print(f"Archivo {archivo} subido exitosamente.")
            time.sleep(2)  # Esperar un poco entre cada subida para evitar problemas de rendimiento
          
        time.sleep(30)
        
    finally:
        # Cerrar el navegador
        driver.quit()

# Ejecutar la selección de archivos y cargar los archivos
archivos_seleccionados = seleccionar_archivos()
if archivos_seleccionados:
    cargar_archivos_a_glpi(archivos_seleccionados)
else:
    print("No se seleccionaron archivos.")
