import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog,
                               QVBoxLayout, QLabel, QWidget, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class GLPIUploader(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Subir Archivos a GLPI")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f5f5f5;")
        
        # Layout principal
        layout = QVBoxLayout()

        # Campo de texto para ingresar serial
        self.label_serial = QLabel("Ingrese el Serial:", self)
        self.label_serial.setFont(QFont("Arial", 12))
        layout.addWidget(self.label_serial)

        self.input_serial = QLineEdit(self)
        self.input_serial.setPlaceholderText("Ejemplo: cnc12345678")
        self.input_serial.setStyleSheet("padding: 10px; border: 1px solid #cccccc; border-radius: 5px;")
        layout.addWidget(self.input_serial)

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.setFont(QFont("Arial", 12))
        self.boton_archivos.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout.addWidget(self.boton_archivos)

        # Etiqueta para mostrar archivos seleccionados
        self.label_archivos = QLabel("Archivos seleccionados: Ninguno", self)
        self.label_archivos.setWordWrap(True)
        self.label_archivos.setFont(QFont("Arial", 10))
        layout.addWidget(self.label_archivos)

        # Botón para subir archivos
        self.boton_subir = QPushButton("Subir Archivos")
        self.boton_subir.setFont(QFont("Arial", 12))
        self.boton_subir.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: black;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
         
            QPushButton:hover {
                background-color: #1E88E5;
            }
        """)
        self.boton_subir.clicked.connect(self.subir_archivos)
        layout.addWidget(self.boton_subir)

        # Etiqueta de estado
        self.label_estado = QLabel("", self)
        self.label_estado.setFont(QFont("Arial", 10))
        layout.addWidget(self.label_estado)

        # Contenedor y layout principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Variables
        self.archivos_seleccionados = []

    def seleccionar_archivos(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
        if archivos:
            self.archivos_seleccionados = archivos
            self.label_archivos.setText(f"Archivos seleccionados: {', '.join(archivos)}")
        else:
            self.label_archivos.setText("Archivos seleccionados: Ninguno")

    def subir_archivos(self):
        serial = self.input_serial.text()
        if not serial:
            self.label_estado.setText("Error: Debe ingresar un serial.")
            return
        
        if not self.archivos_seleccionados:
            self.label_estado.setText("Error: No se seleccionaron archivos.")
            return

        self.label_estado.setText("Subiendo archivos a GLPI...")
        self.cargar_archivos_a_glpi(serial, self.archivos_seleccionados)
        self.label_estado.setText("Subida completa.")

    def cargar_archivos_a_glpi(self, serial, archivos):
        # Configurar el servicio con el path del controlador
        service = Service(executable_path='drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        try:
            # Abrir GLPI y hacer login
            driver.get('http://localhost/glpi/index.php?noAUTO=1')
            wait = WebDriverWait(driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.ID, 'login_name')))
            password_field = wait.until(EC.presence_of_element_located((By.ID, 'login_password')))
            username_field.send_keys('glpi')
            password_field.send_keys('glpi')

            login_button = wait.until(EC.element_to_be_clickable((By.NAME, 'submit')))
            login_button.click()

            # Buscar el serial
            search_field = wait.until(EC.presence_of_element_located((By.NAME, 'globalsearch')))
            search_field.send_keys(serial)

            search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/header/div/div[1]/form/div/span/button')))
            search_button.click()

            time.sleep(1)
            primer_elemento = wait.until(EC.element_to_be_clickable((By.XPATH, '//table/tbody/tr[1]/td[1]/a')))
            primer_elemento.click()

            time.sleep(1)
            documento_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabspanel"]/li[13]/a')))
            documento_button.click()

            # Subir los archivos
            for archivo in archivos:
                upload_element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/main/div/div/div[2]/div[2]/div/div[13]/div[1]/form/table/tbody/tr[2]/td[3]/div/input')))
                upload_element.send_keys(archivo)
                time.sleep(2)

            time.sleep(3)
        finally:
            driver.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GLPIUploader()
    window.show()
    sys.exit(app.exec())
