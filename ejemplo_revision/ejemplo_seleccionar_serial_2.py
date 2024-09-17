import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel, QTextEdit, QListWidget, QListWidgetItem

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cargar Archivos a GLPI")
        self.setGeometry(100, 100, 400, 400)

        # Layout principal
        layout = QVBoxLayout()

        # Campo de texto para ingresar múltiples seriales
        self.input_seriales = QTextEdit(self)
        self.input_seriales.setPlaceholderText("Ingrese los seriales (uno por línea)")
        layout.addWidget(self.input_seriales)

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout.addWidget(self.boton_archivos)

        # Etiqueta para mostrar archivos seleccionados
        self.label_archivos = QLabel("Archivos seleccionados: Ninguno")
        layout.addWidget(self.label_archivos)

        # Lista para mostrar los seriales y archivos que se van a subir
        self.lista_seriales_archivos = QListWidget(self)
        layout.addWidget(self.lista_seriales_archivos)

        # Botón para agregar los seriales y los archivos a la lista
        self.boton_agregar = QPushButton("Agregar Seriales y Archivos")
        self.boton_agregar.clicked.connect(self.agregar_seriales_y_archivos)
        layout.addWidget(self.boton_agregar)

        # Etiqueta para mostrar el estado
        self.label_estado = QLabel("")
        layout.addWidget(self.label_estado)

        # Botón para subir todos los archivos
        self.boton_subir = QPushButton("Subir Archivos a GLPI")
        self.boton_subir.clicked.connect(self.subir_archivos)
        layout.addWidget(self.boton_subir)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Lista para almacenar los seriales y los archivos seleccionados
        self.serial_y_archivos = []
        self.archivos_seleccionados = []

    def seleccionar_archivos(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
        if archivos:
            self.archivos_seleccionados = archivos
            self.label_archivos.setText(f"Archivos seleccionados: {', '.join([os.path.basename(a) for a in archivos])}")
        else:
            self.label_archivos.setText("Archivos seleccionados: Ninguno")

    def agregar_seriales_y_archivos(self):
        seriales = self.input_seriales.toPlainText().splitlines()  # Obtener los seriales uno por línea
        seriales = [s.strip() for s in seriales if s.strip()]  # Eliminar líneas vacías o espacios innecesarios

        if seriales and self.archivos_seleccionados:
            # Guardar los seriales junto con los archivos en la lista
            for serial in seriales:
                self.serial_y_archivos.append((serial, self.archivos_seleccionados.copy()))

                # Mostrar en la lista de seriales y archivos que se subirán
                item_text = f"Serial: {serial} - Archivos: {', '.join([os.path.basename(a) for a in self.archivos_seleccionados])}"
                item = QListWidgetItem(item_text)
                self.lista_seriales_archivos.addItem(item)

            self.label_estado.setText(f"{len(seriales)} seriales y {len(self.archivos_seleccionados)} archivos agregados.")

            # Limpiar el campo de texto y la lista de archivos seleccionados
            self.input_seriales.clear()
            self.archivos_seleccionados.clear()
            self.label_archivos.setText("Archivos seleccionados: Ninguno")
        else:
            self.label_estado.setText("Debe ingresar seriales y seleccionar archivos.")

    def subir_archivos(self):
        if self.serial_y_archivos:
            # Iniciar el proceso de login una sola vez
            driver = self.iniciar_sesion_glpi()

            if driver:
                # Subir archivos para cada serial
                for serial, archivos in self.serial_y_archivos:
                    self.cargar_archivos_a_glpi(driver, serial, archivos)

                # Cerrar el navegador al final del proceso
                driver.quit()

                self.serial_y_archivos.clear()
                self.lista_seriales_archivos.clear()  # Limpiar la lista visible de seriales y archivos
                self.label_estado.setText("Todos los archivos han sido subidos.")
            else:
                self.label_estado.setText("Error en el inicio de sesión.")
        else:
            self.label_estado.setText("No hay seriales y archivos para subir.")

    def iniciar_sesion_glpi(self):
        try:
            # Configurar el servicio con el path del controlador
            service = Service(executable_path='drivers/chromedriver.exe')

            # Iniciar el controlador del navegador usando el servicio
            driver = webdriver.Chrome(service=service)

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

            return driver

        except Exception as e:
            print(f"Error al iniciar sesión en GLPI: {e}")
            return None

    def cargar_archivos_a_glpi(self, driver, serial, archivos):
        try:
            wait = WebDriverWait(driver, 10)

            # Esperar hasta que el campo de búsqueda esté presente
            search_field = wait.until(EC.presence_of_element_located((By.NAME, 'globalsearch')))
            search_field.clear()  # Limpiar el campo de búsqueda antes de ingresar un nuevo serial
            search_field.send_keys(serial)

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

        except Exception as e:
            print(f"Error al subir archivos para el serial {serial}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
