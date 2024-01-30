from PyQt6 import QtWidgets
from view import reportesView
from common import DBManager


class Reportes(QtWidgets.QMainWindow):

    db = DBManager.DBManager()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = reportesView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.esconder_elementos()
        self.cargar_combo_tipo_inmueble()
        self.vl = None
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.cbxTipoReporte.currentTextChanged.connect(self.esconder_elementos)

    def cargar_combo_tipo_inmueble(self):
        tipos = Reportes.db.select('Tipo_Inmueble', '*', 'true')
        for tipo in tipos:
            self.ui.cbxTipoInmueble.addItem(tipo[2])

    def esconder_elementos(self):

        self.ui.lbl_fecha_fin.setVisible(False)
        self.ui.lbl_fecha_inicio.setVisible(False)
        self.ui.lblInmuebleElegido.setVisible(False)
        self.ui.cbxTipoInmueble.setVisible(False)
        self.ui.dateInicio.setVisible(False)
        self.ui.dateFin.setVisible(False)

        if self.ui.cbxTipoReporte.currentText() == 'Inmuebles de un tipo especifico':
            self.ui.lblInmuebleElegido.setVisible(True)
            self.ui.cbxTipoInmueble.setVisible(True)

        if self.ui.cbxTipoReporte.currentText() == 'Ventas en un rango de fechas':
            self.ui.lbl_fecha_fin.setVisible(True)
            self.ui.lbl_fecha_inicio.setVisible(True)
            self.ui.dateInicio.setVisible(True)
            self.ui.dateFin.setVisible(True)

    def salir(self) -> None:
        self.close()
