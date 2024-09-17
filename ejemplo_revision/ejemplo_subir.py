import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_subir_archivo(self):
        self.driver.get('https://convertico.com/es/#google_vignette')
        time.sleep(4)
        self.driver.find_element_by_id('dropzone').send_keys('C:\\Users\\julrojsa\\Documents\\jajaj.png')
        time.sleep(4)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
              unittest.main()