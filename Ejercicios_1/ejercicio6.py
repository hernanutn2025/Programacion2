import sys
from PyQt6.QtWidgets import QApplication, QWidget,QGridLayout,QPushButton,QMessageBox,QLabel,QLineEdit,QCheckBox
from PyQt6.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Términos y condiciones")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        self.etiqueta_mail = QLabel("Email: ")
        self.input_mail = QLineEdit()
        self.input_mail.setPlaceholderText("Ingresar Email")

        self.etiqueta_password = QLabel("Contraseña: ")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Ingrese Contraseña")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.boton_login = QPushButton("Ingresar")
        self.boton_login.clicked.connect(self.funcionLogin)
        
        self.boton_registro=QPushButton("Registrar")
        self.boton_registro.clicked.connect(self.funcionRegistrar)

        self.terminos=QCheckBox("Acepto los términos y condiciones")

        layout.addWidget(self.etiqueta_mail, 0 , 0 , alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.input_mail, 0 , 1)
        layout.addWidget(self.etiqueta_password, 1,0,alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.input_password, 1, 1)
        layout.addWidget(self.terminos,2 , 1)
        layout.addWidget(self.boton_login,3,0,1,1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.boton_registro,3,1,1,1,alignment=Qt.AlignmentFlag.AlignCenter)

    def funcionLogin(self):
        email = self.input_mail.text()
        password = self.input_password.text()
        print(f"Email: {email}, Password: {password}")
        QMessageBox.information(self,"Inicio de sesión",f"Bienvenido: {email}")

    def funcionRegistrar(self):
        email = self.input_mail.text()
        password = self.input_password.text()
        terminos_aceptados = self.terminos.isChecked()
        if not email or not password:
            QMessageBox.warning(self,"Error de registro","Por favor complete todos los campos")
        elif not terminos_aceptados:
            QMessageBox.warning(self,"Error de registro","Debe aceptar los terminos y condiciones")
        else:
            QMessageBox.information(self,"Registro exitoso","Su cuenta ha sido creada")
            print(f"Nuevo usuario registrado: Email{email}, Password{password}")

  
app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())