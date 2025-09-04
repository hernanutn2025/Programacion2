# Ejercicio 4: Confirmación y resumen
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Comprar”.
# - Al hacer clic, mostrar un resumen de la compra en un QMessageBox.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout,QPushButton,QMessageBox
from PyQt6.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Confirmación y Resumen")
        self.setGeometry(100,100,500,350)
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.comprar = QPushButton("Comprar")
        self.comprar.clicked.connect(self.mostrarMensaje)
        layout.addWidget(self.comprar,0,1)
        
    def mostrarMensaje(self):
        QMessageBox.information(self, "Resumen de la compra", "Este es el resumen de la compra.")

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())