#Datos y pasajero
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt6.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Compra de pasaje aéreo")
        self.setGeometry(300, 200, 500 , 350)
        layout = QGridLayout()
        self.setLayout(layout)

        self.titulo = QLabel("Formulario de Compra")
        self.nombre = QLabel("Nombre: ")
        self.input_nombre = QLineEdit()
        self.apellido = QLabel("Apellido: ")
        self.input_apellido = QLineEdit()
        self.dni = QLabel("DNI: ")
        self.dni_input = QLineEdit()
        
        layout.addWidget(self.titulo,0,0,1,2,alignment = Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.nombre,1,0,alignment = Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.input_nombre,1,1)
        layout.addWidget(self.apellido,2,0,alignment = Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.input_apellido,2,1)
        layout.addWidget(self.dni,3,0, alignment = Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.dni_input,3,1)

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())