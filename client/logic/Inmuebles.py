from PyQt6 import QtWidgets
from view import formInmuebles
from common.DBManager import DBManager


class Inmuebles(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = formInmuebles.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_combo_tipo()
        self.cargar_combo_sector()
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.ui.btnCaracteristicas.clicked.connect(self.caracteristicas)
        self.ui.btnAceptar.clicked.connect(self.aceptar)
        self.vl = None

    def cargar_combo_tipo(self):

        db = DBManager()
        tipos = db.select('Tipo_Inmueble', '*', 'true')
        db.close()

        for tipo in tipos:
            self.ui.cbxTipo.addItem(tipo[2])

    def cargar_combo_sector(self):

        db = DBManager()
        sectores = db.select('Sector', '*', 'true')
        db.close()

        for sector in sectores:
            self.ui.cbxSector.addItem(sector[1])

    def aceptar(self) -> None:

        nombre = self.ui.txtNombre.text()
        direccion = self.ui.txtDireccion.text()
        tipo = self.ui.cbxTipo.currentText()
        sector = self.ui.cbxSector.currentText()
        area = self.ui.txtArea.text()

    def caracteristicas(self) -> None:
        from client.logic import Caracteristicas
        self.vl = Caracteristicas.Caracteristicas(self)
        self.vl.show()

    def salir(self) -> None:
        self.close()
