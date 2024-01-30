from PyQt6 import QtWidgets
from view import caracteristicasView
from common.DBManager import DBManager


class Caracteristicas(QtWidgets.QMainWindow):

    def __init__(self, specs=None, parent=None):
        super().__init__(parent)
        self.ui = caracteristicasView.Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_combo_tipo()
        self.specs = specs
        self.ui.btnCancelar.clicked.connect(self.salir)
        self.ui.btnAceptar.clicked.connect(self.aceptar)
        self.ui.btnAgregarCaracteristica.clicked.connect(self.agregar)
        self.ui.btnQuitarCaracteristica.clicked.connect(self.quitar)

    def cargar_combo_tipo(self):
        db = DBManager()
        caracteristicas = db.select('Caracteristica', '*', 'true')
        db.close()
        for caracteristica in caracteristicas:
            self.ui.comboBox.addItem(caracteristica[1])

    def get_caracteristicas(self):

        caracteristicas = []
        num_rows = self.ui.tblCaracteristicas.rowCount()

        for row in range(num_rows):
            codigo = self.ui.tblCaracteristicas.item(row, 0).text()
            descripcion = self.ui.tblCaracteristicas.item(row, 1).text()
            valor = self.ui.tblCaracteristicas.item(row, 2).text()

            caracteristicas.append((codigo, descripcion, valor))

        return caracteristicas

    def aceptar(self):

        self.specs = self.get_caracteristicas()

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Caracteristicas agregadas correctamente")
        msg.setWindowTitle("Caracteristicas")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

        self.close()

    def agregar(self):

        selected_item = self.ui.comboBox.currentText()

        db = DBManager()
        caracteristica = db.select('Caracteristica', '*', f"Descripcion='{selected_item}'")
        db.close()

        if not caracteristica:
            return

        codigo, nombre = caracteristica[0][0], caracteristica[0][1]
        valor = self.ui.txtValor.text()

        # Create a new row in the table
        row_position = self.ui.tblCaracteristicas.rowCount()
        self.ui.tblCaracteristicas.insertRow(row_position)

        # Add the details to the new row
        self.ui.tblCaracteristicas.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(codigo)))
        self.ui.tblCaracteristicas.setItem(row_position, 1, QtWidgets.QTableWidgetItem(nombre))
        self.ui.tblCaracteristicas.setItem(row_position, 2, QtWidgets.QTableWidgetItem(valor))

    def quitar(self):
        self.ui.tblCaracteristicas.removeRow(self.ui.tblCaracteristicas.currentRow())

    def salir(self):
        self.close()
