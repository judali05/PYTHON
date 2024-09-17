
# Python programa de ejemplo
# selenium
#ejemplo_1

#conexion al driver del navegador seleccionado

# importamos el webdriver
from selenium import webdriver

# creamos el objeto driver
driver = webdriver.Chrome()

# entramos a
driver.get("https://google.co.in")

#si no funciona se coloca este codigo 
# driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe') 