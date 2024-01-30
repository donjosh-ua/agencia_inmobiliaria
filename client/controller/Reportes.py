from PyQt6 import QtWidgets
from view import reportesView


class Reportes(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = reportesView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.vl = None
        self.ui.btnSalir.clicked.connect(self.salir)

    def salir(self) -> None:
        self.close()
