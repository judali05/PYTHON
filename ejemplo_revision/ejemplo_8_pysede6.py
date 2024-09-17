import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Agregar valores a la lista")
        self.setGeometry(100, 100, 300, 200)

        # Crear la lista vacía
        self.lista_valores = []

        # Crear los widgets
        self.campo_texto = QLineEdit(self)
        self.boton_enviar = QPushButton("Enviar", self)
        self.etiqueta_resultado = QLabel("Valores ingresados: ", self)
        
        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.campo_texto)
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.etiqueta_resultado)
        self.setLayout(layout)
        
        # Conectar el botón a la función
        self.boton_enviar.clicked.connect(self.agregar_valor)
        
        # Conectar el evento de tecla presionada
        self.campo_texto.returnPressed.connect(self.agregar_valor)

    def agregar_valor(self):
        # Obtener el valor del campo de texto
        valor = self.campo_texto.text()

        # Si el campo de texto no está vacío, agregar a la lista
        if valor:
            self.lista_valores.append(valor)
            self.actualizar_resultado()

        # Limpiar el campo de texto
        self.campo_texto.clear()

    def actualizar_resultado(self):
        # Actualizar la etiqueta con los valores de la lista
        self.etiqueta_resultado.setText(f"Valores ingresados: {', '.join(self.lista_valores)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
