from PyQt6 import QtWidgets
from view import formPersonas


class Clientes(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = formPersonas.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.ui.btnAceptar.clicked.connect(self.aceptar)

    def aceptar(self) -> None:

        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        telefono = self.ui.txtTelefono.text()
        direccion = self.ui.txtDireccion.text()
        correo = self.ui.txtCorreo.text()

        self.salir()

    def salir(self) -> None:
        self.close()
