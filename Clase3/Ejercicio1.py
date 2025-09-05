#Crear la ventana de contexto (formulario de afiliados)
# -----------------------------------------------------------------------------
# Consigna:
# - Crear una ventana principal (QWidget) de 500x350, título "Afiliados - Chacarita Juniors".
# - Agregar QLabel grande y centrado: "Formulario de Afiliación".
# - Agregar QLabel y QLineEdit para Nombre, Apellido, DNI y Fecha de nacimiento.
from PyQt6.QtWidgets import QGridLayout, QWidget, QLabel, QLineEdit,QDateEdit
from PyQt6.QtCore import Qt,QDate
from PyQt6.QtGui import QFont


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100,100,500,350)
        layout = QGridLayout()
        self.setLayout(layout)

        self.nombre = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        self.dni = QLabel("DNI:")
        self.dni_input = QLineEdit()
        self.apellido = QLabel("Apellido:")
        self.apellido_input = QLineEdit()
        self.fecha_nacimiento = QLabel("Fecha de nacimiento:")
        self.fecha_nacimiento_input = QDateEdit()
        self.fecha_nacimiento_input.setDate(QDate.currentDate())
        self.fecha_nacimiento_input.setCalendarPopup(True)
        self.titulo = QLabel("Formulario de Aficliación")
        self.fuente = QFont("Montserrat", 20)
        self.fuente2 = QFont("Monsterrat", 15)
        self.titulo.setFont(self.fuente)
        self.nombre.setFont(self.fuente2)
        self.apellido.setFont(self.fuente2)
        self.dni.setFont(self.fuente2)
        self.fecha_nacimiento.setFont(self.fuente2)
        
        layout.addWidget(self.titulo,0,0,0,2,alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.nombre,1,0,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.nombre_input,1,1,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.apellido,2,0,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.apellido_input,2,1,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.dni,3,0,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.dni_input,3,1,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.fecha_nacimiento,4,0,alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.fecha_nacimiento_input,4,1,alignment=Qt.AlignmentFlag.AlignBottom)
