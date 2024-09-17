# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


# create webdriver object
driver = webdriver.Chrome()


# get geeksforgeeks.org
driver.get("https://github.com/login")

# get element
element = driver.find_element(By.NAME, 'login')

# send keys
element.send_keys("hooolalallqa")


