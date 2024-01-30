from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem
import common.querys as querys

from view import reportesView
from common.DBManager import DBManager


class Reportes(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = reportesView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.esconder_elementos()
        self.cargar_combo_tipo_inmueble()
        self.vl = None
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.cbxTipoReporte.currentTextChanged.connect(self.esconder_elementos)

    def vendidos_x_temporada(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(3)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Inmueble", "Agente", "Cliente"])
        # Llenar la tabla con datos de la lista de tuplas
        fecha_inicio = self.ui.dateInicio.date().toPyDate().strftime('%Y-%m-%d')
        fecha_fin = self.ui.dateFin.date().toPyDate().strftime('%Y-%m-%d')

        db = DBManager()
        data = db.execute(querys.vendidos_por_temporada(fecha_inicio, fecha_fin))
        db.close()

        if data is None:
            return

        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def inmuebles_para_venta(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(8)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Inmueble", "Tipo", "Clasificacion", "Estado", "Sector", "Ciudad", "Cliente"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(querys.inmuebles_para_venta())
        db.close()

        if data is None:
            return

        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def inmuebles_vendidos_x_sector(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(3)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Sector", "Inmuebles"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(querys.inmuebles_vendidos_x_sector())
        db.close()

        if data is None:
            return

        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def inmuebles_d_tipo_especifico(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(7)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Inmueble", "Clasificacion", "Estado", "Sector", "Ciudad", "Cliente"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(querys.inmuebles_tipo_especifico(self.ui.cbxTipoInmueble.currentText()))
        db.close()

        if data is None:
            return

        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def ventas_x_agente(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(3)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Nombre", "Ventas"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(querys.ventas_x_agente())
        db.close()

        if data is None:
            return

        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def cargar_combo_tipo_inmueble(self):

        db = DBManager()
        tipos = db.select('Tipo_Inmueble', '*', 'true')
        db.close()

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

        if self.ui.cbxTipoReporte.currentText() == 'Ventas por agente':
            self.ventas_x_agente()
            return

        if self.ui.cbxTipoReporte.currentText() == 'Inmuebles de un tipo especifico':
            self.inmuebles_d_tipo_especifico()
            return

        if self.ui.cbxTipoReporte.currentText() == 'Inmuebles vendidos por sector':
            self.inmuebles_vendidos_x_sector()
            return

        if self.ui.cbxTipoReporte.currentText() == 'Inmuebles disponibles para la venta':
            self.inmuebles_para_venta()
            return

        if self.ui.cbxTipoReporte.currentText() == 'Ventas en un rango de fechas':
            self.vendidos_x_temporada()
            return

    def salir(self) -> None:
        self.close()
