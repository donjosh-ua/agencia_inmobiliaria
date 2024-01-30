from PyQt6 import QtWidgets
from view import formInmuebles


class Inmuebles(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = formInmuebles.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCancelar.clicked.connect(self.salir)

    def salir(self) -> None:
        self.close()
