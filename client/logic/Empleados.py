from PyQt6 import QtWidgets
from view import empleadosView
from common.DBManager import DBManager


class Empleados(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = empleadosView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_combo_box()
        self.cargar_datos()
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnAgregar.clicked.connect(self.agregar)
        self.ui.btnModificar.clicked.connect(self.modificar)
        self.ui.cbxCedula.currentTextChanged.connect(self.cargar_datos)
        self.vl = None

    def cargar_combo_box(self):
        db = DBManager()
        cedulas = db.select('Empleado', 'Cedula', 'true')
        db.close()
        for ced in cedulas:
            self.ui.cbxCedula.addItem(ced[0])

    def cargar_datos(self):
        cedula = self.ui.cbxCedula.currentText()

        if cedula == '':
            return

        db = DBManager()
        datos = db.select('Empleado', '*', f"Cedula = '{cedula}'")
        db.close()
        
        self.ui.txtModificarNombre.setPlaceholderText(datos[0][1])
        self.ui.txtModificarTelefono.setPlaceholderText(datos[0][2])
        self.ui.txtModificarCorreo.setPlaceholderText(datos[0][3])
        self.ui.txtModificarDireccion.setPlaceholderText(datos[0][4])

    def salir(self) -> None:
        self.close()

    def limpiar_campos_agregar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtCedula.setText('')
        self.ui.txtCorreo.setText('')
        self.ui.txtTelefono.setText('')
        self.ui.txtDireccion.setText('')

    def limpiar_campos_modificar(self):
        self.ui.txtModificarNombre.setText('')
        self.ui.txtModificarCorreo.setText('')
        self.ui.txtModificarTelefono.setText('')
        self.ui.txtModificarDireccion.setText('')

    def agregar(self):

        cedula = self.ui.txtCedula.text()
        nombre = self.ui.txtNombre.text()
        telefono = self.ui.txtTelefono.text()
        correo = self.ui.txtCorreo.text()
        direccion = self.ui.txtDireccion.text()

        db = DBManager()
        db.insert('Empleado', f"'{cedula}', '{nombre}', '{telefono}', '{correo}', '{direccion}'")
        db.close()

        self.cargar_combo_box()
        self.limpiar_campos_agregar()
        self.salir()

    def modificar(self):

        cedula = self.ui.cbxCedula.currentText()

        if cedula == '':
            return

        nombre = self.ui.txtModificarNombre.text() if self.ui.txtModificarNombre.text() != '' else self.ui.txtModificarNombre.placeholderText()
        telefono = self.ui.txtModificarTelefono.text() if self.ui.txtModificarTelefono.text() != '' else self.ui.txtModificarTelefono.placeholderText()
        email = self.ui.txtModificarCorreo.text() if self.ui.txtModificarCorreo.text() != '' else self.ui.txtModificarCorreo.placeholderText()
        direccion = self.ui.txtModificarDireccion.text() if self.ui.txtModificarDireccion.text() != '' else self.ui.txtModificarDireccion.placeholderText()

        db = DBManager()
        db.update('Empleado', f"Nombre = '{nombre}', Telefono = '{telefono}', Email = '{email}', Direccion = '{direccion}'", f"Cedula = '{cedula}'")
        db.close()

        self.limpiar_campos_modificar()
        self.cargar_datos()
