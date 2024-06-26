# Form implementation generated from reading ui file 'formPersonas.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(235, 235, 239);\n"
"color: #1f1f1f;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")
        self.formulario = QtWidgets.QFormLayout(self.widget)
        self.formulario.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formulario.setObjectName("formulario")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formulario.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtCedula = QtWidgets.QLineEdit(parent=self.widget)
        self.txtCedula.setMinimumSize(QtCore.QSize(300, 0))
        self.txtCedula.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCedula.setFont(font)
        self.txtCedula.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtCedula.setObjectName("txtCedula")
        self.formulario.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCedula)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formulario.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtNombre = QtWidgets.QLineEdit(parent=self.widget)
        self.txtNombre.setMinimumSize(QtCore.QSize(300, 0))
        self.txtNombre.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtNombre.setFont(font)
        self.txtNombre.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtNombre.setObjectName("txtNombre")
        self.formulario.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNombre)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formulario.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txtCorreo = QtWidgets.QLineEdit(parent=self.widget)
        self.txtCorreo.setMinimumSize(QtCore.QSize(300, 0))
        self.txtCorreo.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtCorreo.setFont(font)
        self.txtCorreo.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtCorreo.setObjectName("txtCorreo")
        self.formulario.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCorreo)
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formulario.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtTelefono = QtWidgets.QLineEdit(parent=self.widget)
        self.txtTelefono.setMinimumSize(QtCore.QSize(300, 0))
        self.txtTelefono.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtTelefono.setFont(font)
        self.txtTelefono.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtTelefono.setObjectName("txtTelefono")
        self.formulario.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTelefono)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formulario.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtDireccion = QtWidgets.QLineEdit(parent=self.widget)
        self.txtDireccion.setMinimumSize(QtCore.QSize(300, 0))
        self.txtDireccion.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtDireccion.setFont(font)
        self.txtDireccion.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtDireccion.setObjectName("txtDireccion")
        self.formulario.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtDireccion)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAceptar = QtWidgets.QPushButton(parent=self.widget1)
        self.btnAceptar.setMinimumSize(QtCore.QSize(100, 25))
        self.btnAceptar.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #3081D0;\n"
"    color: white;\n"
"}")
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout.addWidget(self.btnAceptar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnCancelar = QtWidgets.QPushButton(parent=self.widget1)
        self.btnCancelar.setMinimumSize(QtCore.QSize(100, 25))
        self.btnCancelar.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #3081D0;\n"
"    color: white;\n"
"}")
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ingreso de Personas"))
        self.label_2.setText(_translate("MainWindow", "Cédula"))
        self.label_5.setText(_translate("MainWindow", "Nombre"))
        self.label_7.setText(_translate("MainWindow", "Correo"))
        self.label_6.setText(_translate("MainWindow", "Teléfono"))
        self.label_4.setText(_translate("MainWindow", "Dirección"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))
