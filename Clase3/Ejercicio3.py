# Ejercicio 3: Mostrar ambas ventanas a la vez
# -----------------------------------------------------------------------------
# Teoría:
# - Puedes crear y mostrar varias ventanas instanciando varias clases QWidget.
# - show() en cada ventana las hace visibles simultáneamente.
#
# Consigna:
# - Modifica el script para que ambas ventanas se muestren al ejecutar el programa.
import sys
from PyQt6.QtWidgets import QApplication
from Ejercicio1 import Ventana
from Ejercicio2 import Ventana2

if __name__  == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana()
    ventana2 = Ventana2(ventana1)
    ventana1.show()
    ventana2.show()
    sys.exit(app.exec())
    