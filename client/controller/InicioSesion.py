from PyQt6 import QtWidgets
import sys
from view import loginView
import client.controller.VistaPrincipal as vistaPrincipal


class InicioSesion(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loginView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.vl = None
        self.ui.btnIngresar.clicked.connect(self.ingresar)

    def ingresar(self):
        self.vl = vistaPrincipal.VistaPrincipal()
        self.vl.show()
        self.close()

    @classmethod
    def salir(cls) -> None:
        sys.exit()

    @classmethod
    def start(cls) -> None:
        app = QtWidgets.QApplication(sys.argv)
        window = InicioSesion()
        window.show()
        app.exec()
