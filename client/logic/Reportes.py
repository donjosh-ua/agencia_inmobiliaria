from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem

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
        data = db.execute(f"SELECT Inmueble.Nombre as Inmueble, Empleado.Nombre as Agente, Cliente.Nombre as Cliente"
                          f" FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id"
                          f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"
                          f" JOIN Empleado on Contrato.Agente = Empleado.Cedula"
                          f" JOIN Cliente on Contrato.Comprador = Cliente.Cedula"
                          f" WHERE Tipo_Contrato.Nombre = 'Compra' and '{fecha_inicio}' < Contrato.Fecha_Venta and '{fecha_fin}' > Contrato.Fecha_Venta")
        if data == None: return
        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def inmuebles_para_venta(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(8)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Inmueble", "Tipo","Clasificacion","Estado","Sector","Ciudad","Cliente"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(f"SELECT Inmueble.ID, Inmueble.Nombre, ti.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre,Ciudad.Nombre,Cliente.Nombre"
                          f" FROM Contrato"
                          f" JOIN Inmueble on Contrato.Inmueble = Inmueble.id"
                          f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"
                          f" JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID"
                          f" JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID"
                          f" JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID"
                          f" JOIN Sector on Inmueble.Sector = Sector.ID"
                          f" JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID"
                          f" JOIN Cliente on Inmueble.Dueño = Cliente.Cedula"
                          f" WHERE ti.Nombre = 'Venta'"
                          f" AND Inmueble.ID NOT IN (SELECT Inmueble.ID"
                            f" FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id"
                            f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"
                            f" WHERE Tipo_Contrato.Nombre = 'Compra')")
        if data == None: return
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
        data = db.execute(f"SELECT Sector.ID, Sector.Nombre, count(DISTINCT Inmueble.ID)"
                          f" FROM Contrato"
                          f" JOIN Inmueble on Contrato.Inmueble = Inmueble.ID"
                          f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"
                          f" JOIN sector on Inmueble.Sector = Sector.ID"
                          f" WHERE Tipo_Contrato.Nombre = 'Compra'"
                          f" GROUP BY Sector.ID")
        if data == None: return
        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def inmuebles_d_tipo_especifico(self):
        # Configurar la tabla con tres columnas
        self.ui.tblReportes.setColumnCount(7)
        # Establecer las etiquetas de las columnas
        self.ui.tblReportes.setHorizontalHeaderLabels(["Id", "Inmueble", "Clasificacion","Estado","Sector","Ciudad","Cliente"])
        # Llenar la tabla con datos de la lista de tuplas
        db = DBManager()
        data = db.execute(f"SELECT Inmueble.ID, Inmueble.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre,Ciudad.Nombre,Cliente.Nombre"
                          f" FROM Inmueble"
                          f" JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID"
                          f" JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID"
                          f" JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID"
                          f" JOIN Sector on Inmueble.Sector = Sector.ID"
                          f" JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID"
                          f" JOIN Cliente on Inmueble.Dueño = Cliente.Cedula"
                          f" WHERE ti.Nombre = '{self.ui.cbxTipoInmueble.currentText()}'")
        if data == None: return
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
        data = db.execute(f"SELECT ag.Cedula, ag.Nombre, count(1)"
                f" FROM Empleado as ag"
                f" JOIN Contrato as con on ag.Cedula = con.Agente"
                f" JOIN Tipo_Contrato on con.Tipo = Tipo_Contrato.ID"
                f" WHERE Tipo_Contrato.Nombre = 'Compra'"
                f" GROUP BY ag.Cedula, ag.Nombre")
        if data == None: return
        for row_index, row_data in enumerate(data):
            self.ui.tblReportes.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tblReportes.setItem(row_index, col_index, item)

    def cargar_combo_tipo_inmueble(self):
        db = DBManager()
        tipos = db.select('Tipo_Inmueble', '*', 'true')
        for tipo in tipos:
            self.ui.cbxTipoInmueble.addItem(tipo[2])
        db.close()

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
