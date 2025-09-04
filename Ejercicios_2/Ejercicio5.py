# Ejercicio 5: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Centrar el formulario en la ventana.
import sys
from PyQt6.QtWidgets import QApplication,QGridLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana con colores")
        self.setGeometry(100,100,500,350)
        layout = QGridLayout()
        self.setLayout(layout)

        self.fuente_montserrat = QFont("Monserrat", 16)
        self.fuente_arial = QFont("Arial", 28)
        self.etiqueta1 = QLabel("Color Rojo")
        self.etiqueta2 = QLabel("Color Verde")
        self.etiqueta1.setFont(self.fuente_montserrat)
        self.etiqueta2.setFont(self.fuente_arial)
        self.etiqueta1.setStyleSheet("color : red")
        self.etiqueta2.setStyleSheet("color : green")

        layout.addWidget(self.etiqueta1,0,0,1,1,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.etiqueta2,0,0,2,1,alignment=Qt.AlignmentFlag.AlignCenter)
        
app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())