import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel, 
                               QFileDialog, QLineEdit, QSpacerItem, QSizePolicy)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz con Pestañas Mejorada")
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget de pestañas
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Agregar las pestañas
        self.crear_pestana_archivos()
        self.crear_pestana_entrada_texto()
        self.crear_pestana_informacion()

        # Estilo general para eliminar líneas de separación y mezclar pestañas con el contenido
        self.setStyleSheet("""
            QTabWidget::pane { 
                border: 0px; 
            }
            QTabBar::tab { 
                background: #ffffff; 
                border: 0px solid #A9A9A9;
                padding: 10px;
                font-size: 14px;
                color: white;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                margin-left: 5px;
                margin-right: 5px;
            }
            QTabBar::tab:selected { 
                background: #F0F0F0;
                color: #34495E;
                font-weight: bold;
            }
            QTabBar::tab:hover { 
                background: #AED6F1;
            }
            QPushButton {
                background-color: #28B463;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1D8348;
            }
            QLineEdit {
                border: 2px solid #D3D3D3;
                padding: 8px;
                font-size: 14px;
                border-radius: 5px;
            }
            QLabel {
                font-size: 14px;
                color: #34495E;
            }
            QWidget {
                background-color: #F0F0F0;
            }
        """)

    def crear_pestana_archivos(self):
        # Crear el widget para la pestaña de archivos
        self.tab_archivos = QWidget()

        # Crear layout para la pestaña
        layout_archivos = QVBoxLayout()

        # Título de la pestaña
        titulo_archivos = QLabel("Carga de Archivos")
        titulo_archivos.setFont(QFont("Arial", 16, QFont.Bold))
        layout_archivos.addWidget(titulo_archivos, alignment=Qt.AlignCenter)

        # Espaciador
        layout_archivos.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Botón para seleccionar archivos
        self.boton_archivos = QPushButton("Seleccionar Archivos")
        self.boton_archivos.clicked.connect(self.seleccionar_archivos)
        layout_archivos.addWidget(self.boton_archivos, alignment=Qt.AlignCenter)

        # Etiqueta para mostrar archivos seleccionados
        self.label_archivos = QLabel("Archivos seleccionados: Ninguno")
        layout_archivos.addWidget(self.label_archivos, alignment=Qt.AlignCenter)

        # Espaciador
        layout_archivos.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Establecer el layout en la pestaña
        self.tab_archivos.setLayout(layout_archivos)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_archivos, QIcon("icons/files.png"), "Cargar Archivos")

    def crear_pestana_entrada_texto(self):
        # Crear el widget para la pestaña de entrada de texto
        self.tab_texto = QWidget()

        # Crear layout para la pestaña
        layout_texto = QVBoxLayout()

        # Título de la pestaña
        titulo_texto = QLabel("Entrada de Texto")
        titulo_texto.setFont(QFont("Arial", 16, QFont.Bold))
        layout_texto.addWidget(titulo_texto, alignment=Qt.AlignCenter)

        # Espaciador
        layout_texto.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Campo de entrada de texto
        self.campo_texto = QLineEdit(self)
        self.campo_texto.setPlaceholderText("Ingrese algún texto aquí")
        layout_texto.addWidget(self.campo_texto, alignment=Qt.AlignCenter)

        # Botón para mostrar el texto ingresado
        self.boton_mostrar_texto = QPushButton("Mostrar Texto")
        self.boton_mostrar_texto.clicked.connect(self.mostrar_texto)
        layout_texto.addWidget(self.boton_mostrar_texto, alignment=Qt.AlignCenter)

        # Etiqueta para mostrar el texto ingresado
        self.label_mostrar_texto = QLabel("")
        layout_texto.addWidget(self.label_mostrar_texto, alignment=Qt.AlignCenter)

        # Espaciador
        layout_texto.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Establecer el layout en la pestaña
        self.tab_texto.setLayout(layout_texto)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_texto, QIcon("icons/text.png"), "Entrada de Texto")

    def crear_pestana_informacion(self):
        # Crear el widget para la pestaña de información
        self.tab_info = QWidget()

        # Crear layout para la pestaña
        layout_info = QVBoxLayout()

        # Título de la pestaña
        titulo_info = QLabel("Información General")
        titulo_info.setFont(QFont("Arial", 16, QFont.Bold))
        layout_info.addWidget(titulo_info, alignment=Qt.AlignCenter)

        # Etiqueta con información
        self.label_info = QLabel("Aquí puedes mostrar alguna información relevante o notas importantes.")
        self.label_info.setWordWrap(True)
        layout_info.addWidget(self.label_info, alignment=Qt.AlignCenter)

        # Espaciador
        layout_info.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Establecer el layout en la pestaña
        self.tab_info.setLayout(layout_info)

        # Agregar la pestaña al widget de pestañas
        self.tab_widget.addTab(self.tab_info, QIcon("icons/info.png"), "Información")

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
