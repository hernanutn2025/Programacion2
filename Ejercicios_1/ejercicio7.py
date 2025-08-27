import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QCheckBox, QMessageBox, QVBoxLayout
from PyQt6.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout(self)
        grid_layout = QGridLayout()
        self.setStyleSheet("background-color: #F8F9FA;")
        
        self.label_email = QLabel("Email:")
        self.label_email.setStyleSheet("color: #333333; font-size: 16px; font-weight: bold;")
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Ingrese su email")
        self.input_email.setStyleSheet("border: 1px solid #CCCCCC; padding: 5px; border-radius: 3px;")
        
        self.label_pass = QLabel("Contraseña:")
        self.label_pass.setStyleSheet("color: #333333; font-size: 16px; font-weight: bold;")
        self.input_pass = QLineEdit()
        self.input_pass.setPlaceholderText("Ingrese su contraseña")
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_pass.setStyleSheet("border: 1px solid #CCCCCC; padding: 5px; border-radius: 3px;")

        self.boton_login = QPushButton("Ingresar")
        self.boton_login.clicked.connect(self.login)
        self.boton_login.setStyleSheet("background-color: #3498DB; color: white; padding: 8px 16px; border-radius: 5px; font-size: 14px;")

        self.boton_registro = QPushButton("Registrarse")
        self.boton_registro.clicked.connect(self.validar_registro)
        self.boton_registro.setStyleSheet("background-color: #2ECC71; color: white; padding: 8px 16px; border-radius: 5px; font-size: 14px;")
        
        self.checkbox_terminos = QCheckBox("Acepto los términos y condiciones")
        self.checkbox_terminos.setStyleSheet("color: #555555; font-size: 12px;")

        grid_layout.addWidget(self.label_email, 0, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.input_email, 0, 1)

        grid_layout.addWidget(self.label_pass, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid_layout.addWidget(self.input_pass, 1, 1)

        grid_layout.addWidget(self.checkbox_terminos, 2, 1)

        grid_layout.addWidget(self.boton_login, 3, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(self.boton_registro, 3, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        main_layout.addLayout(grid_layout)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def login(self):
        email = self.input_email.text()
        password = self.input_pass.text()
        QMessageBox.information(self, "Inicio de Sesión", f"Bienvenido: {email}")

    def validar_registro(self):
        email = self.input_email.text()
        password = self.input_pass.text()
        terminos_aceptados = self.checkbox_terminos.isChecked()

        if not email or not password:
            QMessageBox.warning(self, "Error de Registro", "Por favor, complete todos los campos.")
        elif not terminos_aceptados:
            QMessageBox.warning(self, "Error de Registro", "Debe aceptar los términos y condiciones.")
        else:
            QMessageBox.information(self, "Registro Exitoso", "¡Registro completado! Su cuenta ha sido creada.")

app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())