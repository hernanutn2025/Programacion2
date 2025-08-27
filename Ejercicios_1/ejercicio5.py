import sys
from PyQt6.QtWidgets import QApplication, QWidget,QGridLayout, QCheckBox,QPushButton
from PyQt6.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Términos y condiciones")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        self.terminos = QCheckBox("Acepto los términos y condiciones")
        self.aceptar = QPushButton("Aceptar")
        self.aceptar.setEnabled(False)

        self.terminos.clicked.connect(self.verificarTerminos)
        self.aceptar.clicked.connect(self.aceptarTerminos)
        
        layout.addWidget(self.terminos)
        layout.addWidget(self.aceptar)
        self.setLayout(layout)

    def verificarTerminos(self):
        if self.terminos.isChecked():
            self.aceptar.setEnabled(True)
        else:
            self.aceptar.setEnabled(False)

    def aceptarTerminos(self):
        print(f"Términos y condiciones de uso aceptados.")
    
app = QApplication(sys.argv)
screen = Ventana()
screen.show()
sys.exit(app.exec())