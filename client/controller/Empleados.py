from PyQt6 import QtWidgets

from common.DBManager import DBManager
from view import empleadosView


class Empleados(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = empleadosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnAgregar.clicked.connect(self.agregar)
        self.vl = None

    def salir(self) -> None:
        self.close()

    def agregar(self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        correo = self.ui.txtCorreo.text()
        telefono = self.ui.txtTelefono.text()
        direccion = self.ui.txtDireccion.text()
        sueldo = self.ui.txtSueldo.text()
        clave = self.ui.txtClave.text()
        db = DBManager()
        db.insert('Empleado',f"'{cedula}','{nombre}','{telefono}','{correo}','{direccion}',{float(sueldo)},'{clave}'")
        db.close()