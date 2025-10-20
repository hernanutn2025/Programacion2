import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QAction, QDesktopWidget,
    QTableWidget, QLineEdit, QCheckBox
)
from PyQt5.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Planilla NBA-FIBA")
        self.resize(1400, 900)
        self.centrar_ventana()

        # Marcadores y faltas
        self.marcador_local = 0
        self.marcador_visitante = 0
        self.faltas_local = 0
        self.faltas_visitante = 0

        # Barra de menú
        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("Archivo")
        accion_salir = QAction("Salir", self)
        accion_salir.triggered.connect(self.close)
        menu_archivo.addAction(accion_salir)

        # Widget central con QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Pantallas
        self.pantalla1 = self.crear_pantalla_principal()
        self.pantalla2 = self.crear_segunda_pantalla()

        self.stacked_widget.addWidget(self.pantalla1)
        self.stacked_widget.addWidget(self.pantalla2)

    # -------------------------------
    # Pantalla principal con planilla FIBA
    # -------------------------------
    def crear_pantalla_principal(self):
        widget = QWidget()
        layout_principal = QHBoxLayout(widget)

        # -------------------------------
        # Lado izquierdo: planilla
        # -------------------------------
        lado_izquierdo = QWidget()
        layout_izq = QVBoxLayout(lado_izquierdo)

        titulo = QLabel(" Planilla FIBA Digital")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout_izq.addWidget(titulo)

        self.tabla_local = self.crear_planilla_equipo("Equipo Local", "local")
        layout_izq.addWidget(self.tabla_local)

        self.tabla_visitante = self.crear_planilla_equipo("Equipo Visitante", "visitante")
        layout_izq.addWidget(self.tabla_visitante)

        boton_cambiar = QPushButton("Ver Estadísticas")
        boton_cambiar.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        boton_cambiar.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout_izq.addWidget(boton_cambiar, alignment=Qt.AlignCenter)

        layout_principal.addWidget(lado_izquierdo, 1)

        # -------------------------------
        # Lado derecho: marcador y faltas
        # -------------------------------
        lado_derecho = QWidget()
        layout_der = QVBoxLayout(lado_derecho)

        # Marcador Local
        self.label_marcador_local = QLabel(f"Local: {self.marcador_local}")
        self.label_marcador_local.setAlignment(Qt.AlignCenter)
        self.label_marcador_local.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout_der.addWidget(self.label_marcador_local)

        btns_local = QHBoxLayout()
        for val in [1,2,3]:
            btn = QPushButton(f"+{val}")
            btn.clicked.connect(lambda _, v=val: self.sumar_marcador("local", v))
            btns_local.addWidget(btn)
        btn_restar_local = QPushButton("-1")
        btn_restar_local.clicked.connect(lambda: self.sumar_marcador("local", -1))
        btns_local.addWidget(btn_restar_local)
        layout_der.addLayout(btns_local)

        # Marcador Visitante
        self.label_marcador_visitante = QLabel(f"Visitante: {self.marcador_visitante}")
        self.label_marcador_visitante.setAlignment(Qt.AlignCenter)
        self.label_marcador_visitante.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout_der.addWidget(self.label_marcador_visitante)

        btns_visitante = QHBoxLayout()
        for val in [1,2,3]:
            btn = QPushButton(f"+{val}")
            btn.clicked.connect(lambda _, v=val: self.sumar_marcador("visitante", v))
            btns_visitante.addWidget(btn)
        btn_restar_visitante = QPushButton("-1")
        btn_restar_visitante.clicked.connect(lambda: self.sumar_marcador("visitante", -1))
        btns_visitante.addWidget(btn_restar_visitante)
        layout_der.addLayout(btns_visitante)

        # Faltas totales
        self.label_faltas_local = QLabel(f"Faltas Local: {self.faltas_local}/5")
        self.label_faltas_local.setAlignment(Qt.AlignCenter)
        self.label_faltas_local.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout_der.addWidget(self.label_faltas_local)

        self.label_faltas_visitante = QLabel(f"Faltas Visitante: {self.faltas_visitante}/5")
        self.label_faltas_visitante.setAlignment(Qt.AlignCenter)
        self.label_faltas_visitante.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout_der.addWidget(self.label_faltas_visitante)

        # Reset faltas (solo total, sin tocar jugadores)
        btn_reset_faltas = QPushButton("Resetear Faltas Totales")
        btn_reset_faltas.clicked.connect(self.resetear_faltas_totales)
        layout_der.addWidget(btn_reset_faltas, alignment=Qt.AlignCenter)

        layout_der.addStretch()
        layout_principal.addWidget(lado_derecho, 1)

        return widget

    # -------------------------------
    # Crear planilla de un equipo
    # -------------------------------
    def crear_planilla_equipo(self, nombre_equipo="Equipo", equipo="local"):
        tabla = QTableWidget(15, 7)
        tabla.setHorizontalHeaderLabels(["N°", "Jugador", "F1", "F2", "F3", "F4", "F5"])
        tabla.setColumnWidth(0, 50)
        tabla.setColumnWidth(1, 200)
        for col in range(2,7):
            tabla.setColumnWidth(col, 35)

        for fila in range(15):
            tabla.setCellWidget(fila, 0, QLineEdit())
            tabla.setCellWidget(fila, 1, QLineEdit())
            for col in range(2,7):
                checkbox = QCheckBox()
                checkbox.setStyleSheet("margin-left:0px; margin-right:0px;")
                checkbox.stateChanged.connect(lambda _, r=fila, t=tabla, e=equipo: self.verificar_faltas(r, t, e))
                tabla.setCellWidget(fila, col, checkbox)
        return tabla

    # -------------------------------
    # Verificar faltas
    # -------------------------------
    def verificar_faltas(self, fila, tabla, equipo):
        contador = sum(1 for col in range(2,7) if tabla.cellWidget(fila,col).isChecked())
        color = "background-color: lightgreen" if contador<=2 else "background-color: yellow" if contador<=4 else "background-color: red"
        for col in range(2,7):
            checkbox = tabla.cellWidget(fila,col)
            checkbox.setStyleSheet(f"margin-left:0px; margin-right:0px; {color}")
            checkbox.setEnabled(contador<5 or checkbox.isChecked())
        self.actualizar_faltas_totales(equipo)

    # -------------------------------
    # Actualizar faltas totales
    # -------------------------------
    def actualizar_faltas_totales(self, equipo):
        tabla = self.tabla_local if equipo=="local" else self.tabla_visitante
        total = min(sum(checkbox.isChecked() for fila in range(15) for checkbox in (tabla.cellWidget(fila,col) for col in range(2,7))), 5)
        if equipo=="local":
            self.faltas_local = total
            self.label_faltas_local.setText(f"Faltas Local: {self.faltas_local}/5")
        else:
            self.faltas_visitante = total
            self.label_faltas_visitante.setText(f"Faltas Visitante: {self.faltas_visitante}/5")

    # -------------------------------
    # Resetear solo los totales de faltas
    # -------------------------------
    def resetear_faltas_totales(self):
        self.faltas_local = 0
        self.faltas_visitante = 0
        self.label_faltas_local.setText("Faltas Local: 0/5")
        self.label_faltas_visitante.setText("Faltas Visitante: 0/5")

    # -------------------------------
    # Sumar marcador
    # -------------------------------
    def sumar_marcador(self, equipo, valor):
        if equipo=="local":
            self.marcador_local = max(self.marcador_local + valor, 0)
            self.label_marcador_local.setText(f"Local: {self.marcador_local}")
        else:
            self.marcador_visitante = max(self.marcador_visitante + valor, 0)
            self.label_marcador_visitante.setText(f"Visitante: {self.marcador_visitante}")

    # -------------------------------
    # Segunda pantalla placeholder
    # -------------------------------
    def crear_segunda_pantalla(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        titulo = QLabel(" Estadísticas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(titulo)
        boton_volver = QPushButton("Volver a la ventana principal")
        boton_volver.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        boton_volver.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addStretch()
        layout.addWidget(boton_volver, alignment=Qt.AlignCenter)
        return widget

    # -------------------------------
    # Centrar ventana
    # -------------------------------
    def centrar_ventana(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


#if __name__ == "__main__":
#    app = QApplication(sys.argv)
    
#    sys.exit(app.exec_())
