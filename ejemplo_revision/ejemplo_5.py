# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By

# create webdriver object 
driver = webdriver.Chrome() 
	
# set implicit wait time 
 # seconds 
driver.implicitly_wait(50) # espera el tiempo indicado si el codigo no funciona asta dar error - da un tiempo de espera hasta que el elemento este disponible

# get geeksforgeeks.org 
driver.get("https://github.com/login") 
	
# get element after 10 seconds 
element = driver.find_element(By.NAME, 'login_')


# click element 
element.click() 

