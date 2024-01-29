from PyQt6 import QtWidgets
from view import empleadosView


class Empleados(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = empleadosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSalir.clicked.connect(self.salir)
        self.vl = None

    def start(self) -> None:
        pass

    def salir(self) -> None:
        self.close()
