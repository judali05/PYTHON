import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QLineEdit


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz con Pestañas")
        self.setGeometry(100, 100, 500, 400)

        # Crear el widget de pestañas
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Agregar las pestañas
        self.crear_pestana_archivos()
        self.crear_pestana_entrada_texto()
        self.crear_pestana_informacion()

    def crear_pestana_archivos(self):
        # Crear el widget para la pestaña de archivos
        self.tab_archivos = QWidget()

        # Crear layout para la pestaña
        layout_archivos = QVBoxLayout()

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout_archivos.addWidget(self.boton_archivos)

        # Etiqueta para mostrar archivos seleccionados
        self.label_archivos = QLabel("Archivos seleccionados: Ninguno")
        layout_archivos.addWidget(self.label_archivos)

        # Establecer el layout en la pestaña
        self.tab_archivos.setLayout(layout_archivos)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_archivos, "Cargar Archivos")

    def crear_pestana_entrada_texto(self):
        # Crear el widget para la pestaña de entrada de texto
        self.tab_texto = QWidget()

        # Crear layout para la pestaña
        layout_texto = QVBoxLayout()

        # Campo de entrada de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setPlaceholderText("Ingrese algún texto")
        layout_texto.addWidget(self.campo_texto)

        # Botón para mostrar el texto ingresado
        self.boton_mostrar_texto = QPushButton("Mostrar Texto")
        self.boton_mostrar_texto.clicked.connect(self.mostrar_texto)
        layout_texto.addWidget(self.boton_mostrar_texto)

        # Etiqueta para mostrar el texto ingresado
        self.label_mostrar_texto = QLabel("")
        layout_texto.addWidget(self.label_mostrar_texto)

        # Establecer el layout en la pestaña
        self.tab_texto.setLayout(layout_texto)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_texto, "Entrada de Texto")

    def crear_pestana_informacion(self):
        # Crear el widget para la pestaña de información
        self.tab_info = QWidget()

        # Crear layout para la pestaña
        layout_info = QVBoxLayout()

        # Etiqueta con información
        self.label_info = QLabel("Esta es la pestaña de información general.")
        layout_info.addWidget(self.label_info)

        # Establecer el layout en la pestaña
        self.tab_info.setLayout(layout_info)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_info, "Información")

    def seleccionar_archivos(self):
        archivos, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Archivos", "", "Todos los archivos (*.*)")
        if archivos:
            self.label_archivos.setText(f"Archivos seleccionados: {', '.join([archivo for archivo in archivos])}")
        else:
            self.label_archivos.setText("Archivos seleccionados: Ninguno")

    def mostrar_texto(self):
        texto = self.campo_texto.text()
        self.label_mostrar_texto.setText(f"Texto ingresado: {texto}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

