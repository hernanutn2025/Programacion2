# Ejercicio 4: Agregar diálogos informativos
# -----------------------------------------------------------------------------
# Teoría:
# - QMessageBox permite mostrar mensajes, advertencias y preguntas al usuario.
# - QMessageBox.information() muestra información.
# - QMessageBox.question() hace preguntas con botones Sí/No.
#
# Consigna:
# - Implementar acerca_de(): mostrar información del programa.
# - Modificar salir(): preguntar si desea guardar antes de cerrar.
import sys 
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, QFileDialog, QMessageBox, QStatusBar,QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de texto")
        self.setGeometry(100,100,800,600)
    
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escriba su texto aquí...")

        self.crear_menus()
        self.statusBar()
        self.statusBar().showMessage("Listo para escribir")

    def crear_menus (self):
        menubar = self.menuBar()

        menu_archivo = menubar.addMenu("Archivo")
        accion_nuevo = QAction("&Nuevo",self)
        accion_guardar = QAction("&Guardar",self)
        accion_abrir = QAction("&Abrir",self)
        accion_salir = QAction("&Salir",self)
        accion_nuevo.setShortcut("Ctrl+N")
        accion_abrir.setShortcut("Ctrl+O")
        accion_guardar.setShortcut("Ctrl+S")
        accion_salir.setShortcut("Ctrl+Q")
        menu_archivo.addAction(accion_nuevo)
        menu_archivo.addAction(accion_guardar)
        menu_archivo.addAction(accion_abrir)
        menu_archivo.addAction(accion_salir)
        accion_salir.triggered.connect(self.funcion_salir)
        accion_nuevo.triggered.connect(self.nuevo_archivo)
        accion_abrir.triggered.connect(self.abrir_archivo)
        accion_guardar.triggered.connect(self.guardar_archivo)

        menu_editar = menubar.addMenu("Editar")
        accion_cortar = QAction("&Cortar",self)
        accion_copiar = QAction("&Copiar",self)
        accion_pegar = QAction("&Pegar",self)
        accion_cortar.setShortcut("Ctrl+X")
        accion_copiar.setShortcut("Ctrl+C")
        accion_pegar.setShortcut("Ctrl+V")
        menu_editar.addAction(accion_cortar)
        menu_editar.addAction(accion_copiar)
        menu_editar.addAction(accion_pegar)

        menu_ayuda = menubar.addMenu("Ayuda")
        accion_acercade = QAction("&Acerca de..",self)
        accion_acercade.setShortcut("F1")
        accion_acercade.triggered.connect(self.funcion_acercade)
        menu_ayuda.addAction(accion_acercade)

        pass
   
    def funcion_salir(self):
        respuesta = QMessageBox.question(self,"Salir","Desea guardar antes de salir?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
        if respuesta == QMessageBox.StandardButton.Yes:
            self.guardar_archivo()
        elif respuesta == QMessageBox.StandardButton.No:
            self.close()
        pass

    def funcion_acercade(self):
        QMessageBox.information(self,"Acerca de", 
                          "Editor de Texto v1.0\n\nCreado con PyQt5\nPara aprender desarrollo de interfaces")  

    def nuevo_archivo(self):
        self.editor.clear()
    
    def abrir_archivo(self):
        archivo,_ = QFileDialog.getOpenFileName(self,"Abrir archivo","","Archivos de texto(*.txt)")
        
        if archivo:
            try:
                with open(archivo,"r",encoding="utf-8") as f:
                    contenido = f.read()
                    self.editor.setPlainText(contenido)
            except Exception as e:
                QMessageBox.warning(self,"Error", f"No se pudo abrir el archivo:\n{e}")      
    pass              
    
    def guardar_archivo(self):
        archivo,_= QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivo de texto(*.txt)")
        if archivo:
            try:
                with open(archivo,"w") as f:
                    texto = self.editor.toPlainText()
                    f.write(texto)
                self.statusBar().showMessage(f"Archivo guardado: {archivo}",3000)
            except  Exception as e:
                self.statusBar().showMessage(f"Error al guardar: {e}")
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EditorTexto()
    ventana.show()
    sys.exit(app.exec())
