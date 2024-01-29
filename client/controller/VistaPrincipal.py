from PyQt6 import QtWidgets
from view import mainView
import client.controller.Reportes as Reportes
import client.controller.Contratos as Contratos
import client.controller.Empleados as Empleados


class VistaPrincipal(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.vl = None
        self.ui.btnEmpleados.clicked.connect(self.empleados)
        self.ui.btnInmuebles.clicked.connect(self.contratos)
        self.ui.btnReportes.clicked.connect(self.reportes)

    def reportes(self):
        self.vl = Reportes.Reportes()
        self.vl.show()

    def contratos(self):
        self.vl = Contratos.Contratos()
        self.vl.show()

    def empleados(self):
        self.vl = Empleados.Empleados()
        self.vl.show()
