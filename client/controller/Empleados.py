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
        self.ui.btnModificar.clicked.connect(self.modificar)
        self.vl = None

    def salir(self) -> None:
        self.close()

    def agregar(self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        correo = self.ui.txtCorreo.text()
        telefono = self.ui.txtTelefono.text()
        direccion = self.ui.txtDireccion.text()
        clave = self.ui.txtClave.text()
        db = DBManager()
        db.insert('Empleado',f"'{cedula}','{nombre}','{telefono}','{correo}','{direccion}'")
        db.close()
        self.salir()

    def modificar(self):
        nombre = self.ui.txtModificarNombre.text()
        correo = self.ui.txtModificarCorreo.text()
        telefono = self.ui.txtModificarTelefono.text()
        direccion = self.ui.txtModificarDireccion.text()
        cedula = self.ui.cbxCedula.currentText()
        db = DBManager()
        db.update('Empleado',f"Nombre = '{nombre}',Telefono = '{telefono}',Correo = '{correo}',Direccion = '{direccion}'",f"Cedula = '{cedula}'")
        db.close()