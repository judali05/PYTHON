from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get('https://github.com/login')
    username_field = driver.find_element(By.NAME, 'login').send_keys(username)
    password_field = driver.find_element(By.NAME, 'password').send_keys(password)
    login_button = driver.find_element(By.NAME, 'commit').click()
    WebDriverWait(driver, 10).until(
        EC.url_changes('https://github.com/login')
    )

#username_field = driver.find_element(By.ID, 'login_name').send_keys(username)
   # password_field = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(password)
   # login_button = driver.find_element(By.NAME, 'submit').click()
    #WebDriverWait(driver, 10).until(
#