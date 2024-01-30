from PyQt6 import QtWidgets
from view import contratosView


class Contratos(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = contratosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnIngresarInmueble.clicked.connect(self.ingresar_inmueble)
        self.ui.btnIngresarCliente.clicked.connect(self.ingresar_cliente)
        self.vl = None

    def ingresar_inmueble(self) -> None:
        from client.controller import Inmuebles
        self.vl = Inmuebles.Inmuebles(self)
        self.vl.show()

    def ingresar_cliente(self) -> None:
        from client.controller import Clientes
        self.vl = Clientes.Clientes(self)
        self.vl.show()

    def salir(self) -> None:
        self.close()
