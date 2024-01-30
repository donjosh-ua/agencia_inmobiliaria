from PyQt6 import QtWidgets, QtCore
from view import contratosView
from common.DBManager import DBManager


def get_new_contrato_id():

    db = DBManager()
    count = db.select('Contrato', 'COUNT(1)', 'true')[0][0]
    db.close()

    return count + 1


class Contratos(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = contratosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.currentTextChanged.connect(self.esconder_elementos)
        self.limpiar_campos()
        self.cargar_combo_tipo()
        self.cargar_combo_inmueble()
        self.cargar_combo_cliente()
        self.cargar_combo_vendedor()
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnIngresarInmueble.clicked.connect(self.ingresar_inmueble)
        self.ui.btnIngresarCliente.clicked.connect(self.ingresar_cliente)
        self.ui.btnConfirmar.clicked.connect(self.agregar_contrato)
        self.vl = None

    def limpiar_campos(self):
        self.ui.cbxInmuebles.setCurrentIndex(0)
        self.ui.cbxClientes.setCurrentIndex(0)
        self.ui.cbxAgentes.setCurrentIndex(0)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.dateInicioContrato.setDate(QtCore.QDate.currentDate())
        self.ui.dateFinContrato.setDate(QtCore.QDate.currentDate())
        self.ui.txtValor.setText("")
        self.ui.txtComision.setText("")

    def agregar_contrato(self):

        id_contrato = get_new_contrato_id()
        inmueble = self.ui.cbxInmuebles.currentText()
        cliente = self.ui.cbxClientes.currentText()
        agente = self.ui.cbxAgentes.currentText()
        tipo = self.ui.comboBox.currentText()
        fecha_inicio = self.ui.dateInicioContrato.date().toPyDate().strftime('%Y-%m-%d')
        fecha_fin = "null"

        if tipo == "Venta":
            fecha_fin = self.ui.dateFinContrato.date().toPyDate().strftime('%Y-%m-%d')

        if not inmueble or not cliente or not agente or not tipo or not fecha_inicio or not fecha_fin:
            return

        inmueble = inmueble.split('-')[0]

        try:
            precio = float(self.ui.txtValor.text())
            comision = float(self.ui.txtComision.text())
        except ValueError:
            return

        db = DBManager()

        tipo = db.select('Tipo_Contrato', '*', f"nombre = '{self.ui.comboBox.currentText()}'")[0][0]
        db.insert('Contrato', f"'{id_contrato}', '{inmueble}', '{cliente}', '{agente}', '{tipo}', '{fecha_inicio}', {fecha_fin}, '{comision}', '{precio}'")

        db.close()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Contrato realizado correctamente")
        msg.setWindowTitle("Inmueble")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

        self.limpiar_campos()

    def cargar_combo_tipo(self):
        db = DBManager()
        tipos = db.select('Tipo_Contrato', '*', 'true')
        for tipo in tipos:
            self.ui.comboBox.addItem(tipo[1])
        db.close()

    def cargar_combo_inmueble(self):
        db = DBManager()
        inmuebles = db.select('Inmueble', '*', 'true')
        for inmueble in inmuebles:
            self.ui.cbxInmuebles.addItem(f"{inmueble[0]}-{inmueble[1]}")
        db.close()

    def cargar_combo_cliente(self):
        db = DBManager()
        clientes = db.select('Cliente', '*', 'true')
        for cliente in clientes:
            self.ui.cbxClientes.addItem(cliente[0])
        db.close()

    def cargar_combo_vendedor(self):
        db = DBManager()
        vendedores = db.select('Empleado', '*', 'true')
        for vendedor in vendedores:
            self.ui.cbxAgentes.addItem(vendedor[0])
        db.close()

    def ingresar_inmueble(self) -> None:
        from client.logic import Inmuebles
        self.vl = Inmuebles.Inmuebles(cbx=self.ui.cbxInmuebles)
        self.vl.show()

    def ingresar_cliente(self) -> None:
        from client.logic import Clientes
        self.vl = Clientes.Clientes(cbx=self.ui.cbxClientes)
        self.vl.show()

    def esconder_elementos(self):

        self.ui.lblFechaFin.setVisible(False)
        self.ui.dateFinContrato.setVisible(False)

        if self.ui.comboBox.currentText() == 'Venta':
            self.ui.lblFechaFin.setVisible(True)
            self.ui.dateFinContrato.setVisible(True)

    def salir(self) -> None:
        self.close()
