# Form implementation generated from reading ui file 'empleadosView.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setStyleSheet("background-color: rgb(235, 235, 239);\n"
"color: #1f1f1f;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabAgregar = QtWidgets.QWidget()
        self.tabAgregar.setObjectName("tabAgregar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabAgregar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.tabAgregar)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget = QtWidgets.QWidget(parent=self.tabAgregar)
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
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
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCedula)
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
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
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtNombre)
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
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
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtCorreo)
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
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
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTelefono)
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
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
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtDireccion)
        self.label_13 = QtWidgets.QLabel(parent=self.widget)
        self.label_13.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.txtClave = QtWidgets.QLineEdit(parent=self.widget)
        self.txtClave.setMinimumSize(QtCore.QSize(300, 0))
        self.txtClave.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtClave.setFont(font)
        self.txtClave.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtClave.setObjectName("txtClave")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtClave)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.btnAgregar = QtWidgets.QPushButton(parent=self.tabAgregar)
        self.btnAgregar.setMinimumSize(QtCore.QSize(100, 25))
        self.btnAgregar.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #3081D0;\n"
"    color: white;\n"
"}")
        self.btnAgregar.setObjectName("btnAgregar")
        self.verticalLayout_2.addWidget(self.btnAgregar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.tabWidget.addTab(self.tabAgregar, "")
        self.tabModificar = QtWidgets.QWidget()
        self.tabModificar.setObjectName("tabModificar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabModificar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.tabModificar)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.cbxCedula = QtWidgets.QComboBox(parent=self.tabModificar)
        self.cbxCedula.setMinimumSize(QtCore.QSize(120, 0))
        self.cbxCedula.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cbxCedula.setFont(font)
        self.cbxCedula.setStyleSheet("QComboBox{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.cbxCedula.setObjectName("cbxCedula")
        self.verticalLayout_3.addWidget(self.cbxCedula, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.widget1 = QtWidgets.QWidget(parent=self.tabModificar)
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.widget1)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtModificarNombre = QtWidgets.QLineEdit(parent=self.widget1)
        self.txtModificarNombre.setMinimumSize(QtCore.QSize(300, 0))
        self.txtModificarNombre.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtModificarNombre.setFont(font)
        self.txtModificarNombre.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtModificarNombre.setObjectName("txtModificarNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModificarNombre)
        self.label_15 = QtWidgets.QLabel(parent=self.widget1)
        self.label_15.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.txtModificarCorreo = QtWidgets.QLineEdit(parent=self.widget1)
        self.txtModificarCorreo.setMinimumSize(QtCore.QSize(300, 0))
        self.txtModificarCorreo.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtModificarCorreo.setFont(font)
        self.txtModificarCorreo.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtModificarCorreo.setObjectName("txtModificarCorreo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModificarCorreo)
        self.label_5 = QtWidgets.QLabel(parent=self.widget1)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtModificarTelefono = QtWidgets.QLineEdit(parent=self.widget1)
        self.txtModificarTelefono.setMinimumSize(QtCore.QSize(300, 0))
        self.txtModificarTelefono.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtModificarTelefono.setFont(font)
        self.txtModificarTelefono.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtModificarTelefono.setObjectName("txtModificarTelefono")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModificarTelefono)
        self.label_14 = QtWidgets.QLabel(parent=self.widget1)
        self.label_14.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.txtModificarDireccion = QtWidgets.QLineEdit(parent=self.widget1)
        self.txtModificarDireccion.setMinimumSize(QtCore.QSize(300, 0))
        self.txtModificarDireccion.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtModificarDireccion.setFont(font)
        self.txtModificarDireccion.setStyleSheet("QLineEdit{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}")
        self.txtModificarDireccion.setObjectName("txtModificarDireccion")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtModificarDireccion)
        self.verticalLayout_3.addWidget(self.widget1, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.btnModificar = QtWidgets.QPushButton(parent=self.tabModificar)
        self.btnModificar.setMinimumSize(QtCore.QSize(100, 25))
        self.btnModificar.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnModificar.setFont(font)
        self.btnModificar.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #3081D0;\n"
"    color: white;\n"
"}")
        self.btnModificar.setObjectName("btnModificar")
        self.verticalLayout_3.addWidget(self.btnModificar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabWidget.addTab(self.tabModificar, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.btnSalir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSalir.setMinimumSize(QtCore.QSize(100, 25))
        self.btnSalir.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet("QPushButton{\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #3081D0;\n"
"    color: white;\n"
"}")
        self.btnSalir.setObjectName("btnSalir")
        self.verticalLayout.addWidget(self.btnSalir, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Empleados"))
        self.label_2.setText(_translate("MainWindow", "Agregar empleado"))
        self.label_7.setText(_translate("MainWindow", "Cédula"))
        self.label_9.setText(_translate("MainWindow", "Nombre"))
        self.label_8.setText(_translate("MainWindow", "Correo"))
        self.label_10.setText(_translate("MainWindow", "Teléfono"))
        self.label_11.setText(_translate("MainWindow", "Dirección"))
        self.label_13.setText(_translate("MainWindow", "Clave"))
        self.btnAgregar.setText(_translate("MainWindow", "Confirmar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAgregar), _translate("MainWindow", "Agregar"))
        self.label_3.setText(_translate("MainWindow", "Modificar datos de empleado"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_15.setText(_translate("MainWindow", "Correo"))
        self.label_5.setText(_translate("MainWindow", "Teléfono"))
        self.label_14.setText(_translate("MainWindow", "Dirección"))
        self.btnModificar.setText(_translate("MainWindow", "Confirmar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabModificar), _translate("MainWindow", "Modificar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
