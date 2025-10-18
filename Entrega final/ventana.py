import basededatos
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,QLabel,QLineEdit,QPushButton,QMessageBox)

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NBA FIBA - Login")
        self.resize(400,150)

        self.conexion = basededatos.conectar_base()
        if not self.conexion:
            QMessageBox.critical(self,"Error","No se pudo conectar a la base de datos NBA")
            QApplication.instance().quit()
            return
        
        self.constructor_login()
    def constructor_login(self):
        layout = QVBoxLayout()

        self.etiqueta_usuario=QLabel("Usuario")
        self.datos_usuario=QLineEdit()
        self.datos_usuario.setPlaceholderText("Ingresar usuario..")

        self.etiqueta_contraseña=QLabel("Contraseña")
        self.datos_contraseña=QLineEdit()
        self.datos_contraseña.setEchoMode(QLineEdit.Password)
        self.datos_contraseña.setPlaceholderText("Ingresar contraseña..")

        self.boton_login=QPushButton("Iniciar Sesión")
        self.boton_login.clicked.connect(self.intentar_logear)

        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.datos_usuario)
        layout.addWidget(self.etiqueta_contraseña)
        layout.addWidget(self.datos_contraseña)
        layout.addWidget(self.boton_login)

        self.setLayout(layout)

    def intentar_logear(self):
        usuario = self.datos_usuario.text()
        contraseña = self.datos_contraseña.text()

        if not usuario or not contraseña:
            QMessageBox.warning(self,"¡Advertencia!","Por favor, complete los campos para ingresar.")
            return
        if self.conexion and self.conexion.is_connected():
            if basededatos.autenticar_usuario(self.conexion,usuario,contraseña):
                QMessageBox.information(self,f"Ingreso exitoso","Bienvenido "+usuario+"!")
                self.ventana_principal()
            else:
                QMessageBox.critical(self,"Error al ingresar","Usuario o contraseña incorrectos.")
        else:
            QMessageBox.critical(self,"Error de Conexión", "Conexión a la base de datos perdida..")      

    def ventana_principal(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            self.close()
            