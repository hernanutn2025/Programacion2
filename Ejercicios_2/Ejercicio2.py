# Ejercicio 2: Selección de vuelo
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
# - QDateEdit permite seleccionar una fecha.
#
# Consigna:
# - Agregar QLabel “Origen:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Destino:” y QComboBox con al menos 3 ciudades.
# - Agregar QLabel “Fecha de vuelo:” y QDateEdit.
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QGridLayout,QComboBox,QDateEdit
from PyQt6.QtCore import QDate

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de pasaje aéreo")
        self.setGeometry(100, 100, 500 , 350)
        layout = QGridLayout()
        self.setLayout(layout)

        self.origen = QLabel("Origen")
        self.origen_combo = QComboBox()
        self.origen_combo.addItems(["Venado Tuerto","La Chispa","Rumipal"])
        self.destino = QLabel("Destino")
        self.destino_combo = QComboBox()
        self.destino_combo.addItems(["Italia","Johannesburgo","Timbuktu"])
        self.fecha_vuelo = QLabel("Fecha")
        self.fecha_edit = QDateEdit()
        self.fecha_edit.setDate(QDate.currentDate())
        self.fecha_edit.setCalendarPopup(True) #Memorizar este método

        layout.addWidget(self.origen,0,0)
        layout.addWidget(self.origen_combo, 0,1)
        layout.addWidget(self.destino,1,0)
        layout.addWidget(self.destino_combo,1,1)
        layout.addWidget(self.fecha_vuelo,2,0)
        layout.addWidget(self.fecha_edit,2,1)


app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())