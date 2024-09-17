from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.get('https://mesadeservicio.americasbps.com:8445/index.php?noAUTO=1')
    username_field = driver.find_element(By.ID, 'login_name').send_keys(username)
    password_field = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div/div[1]/div[2]/input').send_keys(password)
    login_button = driver.find_element(By.NAME, 'submit').click()
    WebDriverWait(driver, 30).until(
        EC.url_changes('https://mesadeservicio.americasbps.com:8445/index.php?noAUTO=1')
    )
