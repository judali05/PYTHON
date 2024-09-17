import sys
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QListWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Copiar Archivos a una Carpeta")
        self.setGeometry(100, 100, 500, 300)

        # Crear layout principal
        layout = QVBoxLayout()

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout.addWidget(self.boton_archivos)

        # Lista para mostrar los archivos seleccionados
        self.lista_archivos = QListWidget()
        layout.addWidget(self.lista_archivos)

        # Botón para seleccionar carpeta de destino
        self.boton_carpeta = QPushButton("Seleccionar Carpeta de Destino")
        self.boton_carpeta.clicked.connect(self.seleccionar_carpeta_destino)
        layout.addWidget(self.boton_carpeta)

        # Etiqueta para mostrar la carpeta de destino seleccionada
        self.label_destino = QLabel("Carpeta de destino: No seleccionada")
        layout.addWidget(self.label_destino)

        # Botón para iniciar la copia de archivos
        self.boton_copiar = QPushButton("Copiar Archivos")
        self.boton_copiar.clicked.connect(self.copiar_archivos_ordenados)
        layout.addWidget(self.boton_copiar)

        # Contenedor principal
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # Inicializar variables
        self.archivos_seleccionados = []
        self.carpeta_destino = ""

    def seleccionar_archivos(self):
        # Abrir diálogo para seleccionar archivos
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
        if archivos:
            self.archivos_seleccionados = archivos
            self.lista_archivos.clear()  # Limpiar la lista antes de mostrar los nuevos archivos
            self.lista_archivos.addItems(archivos)  # Agregar archivos a la lista visual

    def seleccionar_carpeta_destino(self):
        # Abrir diálogo para seleccionar carpeta de destino
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta de Destino")
        if carpeta:
            self.carpeta_destino = carpeta
            self.label_destino.setText(f"Carpeta de destino: {self.carpeta_destino}")

    def copiar_archivos_ordenados(self):
        # Copiar archivos a la carpeta de destino en orden con un bucle
        if self.archivos_seleccionados and self.carpeta_destino:
            for index, archivo in enumerate(sorted(self.archivos_seleccionados)):  # Ordenar archivos alfabéticamente
                nombre_archivo = os.path.basename(archivo)
                destino = os.path.join(self.carpeta_destino, f"{index+1}_{nombre_archivo}")  # Numerar los archivos
                shutil.copy(archivo, destino)  # Copiar archivo
                print(f"Archivo {nombre_archivo} copiado a {self.carpeta_destino} como {index+1}_{nombre_archivo}")
            self.archivos_seleccionados = []  # Reiniciar lista de archivos
            self.lista_archivos.clear()  # Limpiar la lista visual después de copiar

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
