# Python programa de ejemplo
# selenium
#ejemplo_2

#navegar con links

# importamos el webdriver
from selenium import webdriver 

# creamos el objeto driver
driver = webdriver.Chrome() 

# entramos a google y hacemos una busqueda
driver.get("https://www.google.com/search?q=whatsapp")

