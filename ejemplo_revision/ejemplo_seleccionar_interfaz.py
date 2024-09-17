import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cargar Archivos a GLPI")
        self.setGeometry(100, 100, 400, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout.addWidget(self.boton_archivos)

        # Etiqueta para mostrar archivos seleccionados
        self.label_archivos = QLabel("Archivos seleccionados: Ninguno")
        layout.addWidget(self.label_archivos)

        # Botón para subir archivos
        self.boton_subir = QPushButton("Subir Archivos a GLPI")
        self.boton_subir.clicked.connect(self.subir_archivos)
        layout.addWidget(self.boton_subir)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Lista para almacenar los archivos seleccionados
        self.archivos_seleccionados = []

    def seleccionar_archivos(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
        if archivos:
            self.archivos_seleccionados = archivos
            self.label_archivos.setText(f"Archivos seleccionados: {', '.join([os.path.basename(a) for a in archivos])}")
        else:
            self.label_archivos.setText("Archivos seleccionados: Ninguno")

    def subir_archivos(self):
        if self.archivos_seleccionados:
            self.cargar_archivos_a_glpi(self.archivos_seleccionados)
        else:
            self.label_archivos.setText("No se seleccionaron archivos para subir.")

    def cargar_archivos_a_glpi(self, archivos):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
