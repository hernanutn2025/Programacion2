# Clase y cantidad de pasajeros
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción (Ej: clase turista o ejecutiva).
# - QSpinBox permite elegir un número (Ej: cantidad de pasajeros).
#
# Consigna:
# - Agregar QRadioButton para “Turista” y “Ejecutiva”.
# - Agregar QLabel “Cantidad de pasajeros:” y QSpinBox (mínimo 1, máximo 10).

import sys 
from PyQt6.QtWidgets import QRadioButton, QSpinBox, QWidget,QGridLayout,QLabel,QApplication

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clase y Cantidad de pasajeros")
        self.setGeometry(100,100,500,350)
        layout = QGridLayout()
        self.setLayout(layout)

        self.etiqueta_turista = QLabel("Turista: ")
        self.etiqueta_ejecutiva = QLabel("Ejecutiva: ")
        self.turista = QRadioButton()
        self.ejecutiva = QRadioButton()
        self.cantidad_pasajeros = QLabel("Cantidad de pasajeros:")
        self.spin_turista = QSpinBox()
        self.spin_turista.setMaximum(10)
        self.spin_ejecutiva = QSpinBox()
        self.spin_ejecutiva.setMaximum(10)

        layout.addWidget(self.etiqueta_turista,0,0)
        layout.addWidget(self.etiqueta_ejecutiva,1,0)
        layout.addWidget(self.turista,0,1)
        layout.addWidget(self.ejecutiva,1,1)
        layout.addWidget(self.spin_turista,0,2)
        layout.addWidget(self.spin_ejecutiva,1,2)

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())


