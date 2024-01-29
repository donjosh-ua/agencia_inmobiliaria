from PyQt6 import QtWidgets
import sys
from view import loginView


class InicioSesion(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loginView.Ui_MainWindow()
        self.ui.setupUi(self)

    @classmethod
    def salir(cls) -> None:
        sys.exit()

    @classmethod
    def start(cls) -> None:
        app = QtWidgets.QApplication(sys.argv)
        window = InicioSesion()
        window.show()
        app.exec()
