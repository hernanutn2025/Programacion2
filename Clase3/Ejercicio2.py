# Ejercicio 2: Crear la ventana de herramientas
# -----------------------------------------------------------------------------
# Teoría:
# - Otra instancia de QWidget puede funcionar como ventana secundaria.
# - QPushButton permite crear botones de acción.
# - QVBoxLayout organiza widgets en columna.
#
# Consigna:
# - Crear una ventana secundaria de 200x300, título "Herramientas".
# - Agregar botones: "Guardar", "Abrir", "Buscar", "Salir".
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
class Ventana2(QWidget):
    def __init__(self,ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.setWindowTitle("Herramientas")
        self.setGeometry(700,100,200,300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.guardar = QPushButton("Guardar")
        self.abrir = QPushButton("Abrir")
        self.buscar = QPushButton("Buscar")
        self.salir = QPushButton("Salir")

        layout.addWidget(self.guardar)
        layout.addWidget(self.abrir)
        layout.addWidget(self.buscar)
        layout.addWidget(self.salir)

        self.guardar.clicked.connect(self.guardar_mensaje)
        self.salir.clicked.connect(self.funcion_salir)

    def guardar_mensaje(self):
        nombre = self.ventana_principal.nombre_input.text()
        apellido = self.ventana_principal.apellido_input.text()
        dni = self.ventana_principal.dni_input.text()
        fecha = self.ventana_principal.fecha_nacimiento_input.text()

        if not nombre or not apellido or not dni or not fecha:
            QMessageBox.warning(self,"Campos incompletos", "Por favor completar todos los campos.")
            return

        mensaje = QMessageBox(self)
        mensaje.setWindowTitle("Datos guardados")
        mensaje.setText(f"Los datos de afiliado son:\n\n"
                        f"Nombre: {nombre}\n"
                        f"Apellido: {apellido}\n"
                        f"DNI: {dni}\n"
                        f"Fecha de nacimiento: {fecha}")
        mensaje.exec()

    def funcion_salir(self):
        self.ventana_principal.close()
        self.close()


