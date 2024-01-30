from PyQt6 import QtWidgets
from view import contratosView
from common.DBManager import DBManager


class Contratos(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = contratosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.currentTextChanged.connect(self.esconder_elementos)
        self.cargar_combo_tipo()
        self.cargar_combo_inmueble()
        self.cargar_combo_cliente()
        self.cargar_combo_vendedor()
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnIngresarInmueble.clicked.connect(self.ingresar_inmueble)
        self.ui.btnIngresarCliente.clicked.connect(self.ingresar_cliente)
        self.vl = None

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
            self.ui.cbxInmuebles.addItem(inmueble[1])
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
