from PyQt6 import QtWidgets
from view import formInmuebles
from common.DBManager import DBManager


def get_new_inmueble_id():

    db = DBManager()
    count = db.select('Inmueble', 'COUNT(*)', 'true')[0][0]
    db.close()

    return count + 1


class Inmuebles(QtWidgets.QMainWindow):

    def __init__(self, cbx=None, parent=None):
        super().__init__(parent)
        self.cbx = cbx
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

        id_inmueble = get_new_inmueble_id()
        nombre = self.ui.txtNombre.text()
        direccion = self.ui.txtDireccion.text()
        tipo = self.ui.cbxTipo.currentText()
        sector = self.ui.cbxSector.currentText()
        area = self.ui.txtArea.text()
        specs = self.vl.get_caracteristicas()
        estado = 'Disponible'
        anio = int(self.ui.txtAnio.text())

        sector_id = DBManager().select('Sector', 'id', f"nombre = '{sector}'")[0][0]
        tipo_id = DBManager().select('Tipo_Inmueble', 'id', f"nombre = '{tipo}'")[0][0]
        estado_id = DBManager().select('Estado_Inmueble', 'id', f"nombre = '{estado}'")[0][0]

        db = DBManager()
        db.insert('Inmueble', f"'{id_inmueble}', '{nombre}', '{direccion}', '{sector_id}', '{tipo_id}', '{estado_id}', '{area}', '{anio}'")

        if self.vl is not None:
            specs = self.vl.get_caracteristicas()

        for spec in specs:
            spec_id, _, valor = spec
            db.insert('Inmueble_Caracteristica', f"'{id_inmueble}', '{spec_id}', '{valor}'")

        db.close()

        self.cbx.addItem(nombre)
        self.cbx.setCurrentText(nombre)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Inmueble agregado correctamente")
        msg.setWindowTitle("Inmueble")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

        self.close()

    def caracteristicas(self) -> None:
        from client.logic import Caracteristicas
        self.vl = Caracteristicas.Caracteristicas()
        self.vl.show()

    def salir(self) -> None:
        self.close()
