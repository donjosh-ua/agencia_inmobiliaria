from PyQt6 import QtWidgets
from view import caracteristicasView
from common.DBManager import DBManager


class Caracteristicas(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = caracteristicasView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_combo_tipo()
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.ui.btnAgregarCaracteristica.clicked.connect(self.agregar)
        self.ui.btnQuitarCaracteristica.clicked.connect(self.quitar)

    def cargar_combo_tipo(self):
        db = DBManager()
        caracteristicas = db.select('Caracteristica', '*', 'true')
        db.close()
        for caracteristica in caracteristicas:
            self.ui.comboBox.addItem(caracteristica[1])

    def agregar(self):
        pass

    def quitar(self):
        pass

    def salir(self):
        self.close()
