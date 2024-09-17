import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Iniciar el controlador del navegador
driver = webdriver.Chrome()

# Abrir la página web de Imgbb
driver.get("https://imgbb.com/")

# Localizar el botón para subir una imagen y hacer clic en él
upload_button = driver.find_element(By.CSS_SELECTOR, 'a.btn-primary')
upload_button.click()

# Esperar a que el diálogo de selección de archivos se abra
time.sleep(2)

# Usar PyAutoGUI para escribir la ruta del archivo (reemplaza con tu ruta local)
pyautogui.write("C:\\Documents\\jajaj.png")
pyautogui.press('enter')

# Esperar un tiempo para que el archivo se cargue
time.sleep(10)

# Cerrar el navegador
driver.quit()
