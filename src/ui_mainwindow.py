# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(699, 430)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 281, 381))
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label)

        self.spnnDestinoX = QSpinBox(self.groupBox)
        self.spnnDestinoX.setObjectName(u"spnnDestinoX")
        self.spnnDestinoX.setMaximum(500)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spnnDestinoX)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_2)

        self.spnnDestinoY = QSpinBox(self.groupBox)
        self.spnnDestinoY.setObjectName(u"spnnDestinoY")
        self.spnnDestinoY.setMaximum(500)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.spnnDestinoY)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.spnnRed = QSpinBox(self.groupBox)
        self.spnnRed.setObjectName(u"spnnRed")
        self.spnnRed.setMaximum(255)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.spnnRed)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.spnnGreen = QSpinBox(self.groupBox)
        self.spnnGreen.setObjectName(u"spnnGreen")
        self.spnnGreen.setMaximum(255)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.spnnGreen)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_7)

        self.spnnBlue = QSpinBox(self.groupBox)
        self.spnnBlue.setObjectName(u"spnnBlue")
        self.spnnBlue.setMaximum(255)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.spnnBlue)

        self.btnAgregarFinal = QPushButton(self.groupBox)
        self.btnAgregarFinal.setObjectName(u"btnAgregarFinal")
        self.btnAgregarFinal.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(13, QFormLayout.SpanningRole, self.btnAgregarFinal)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.spnnOrigenX = QSpinBox(self.groupBox)
        self.spnnOrigenX.setObjectName(u"spnnOrigenX")
        self.spnnOrigenX.setMaximum(500)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spnnOrigenX)

        self.spnnOrigenY = QSpinBox(self.groupBox)
        self.spnnOrigenY.setObjectName(u"spnnOrigenY")
        self.spnnOrigenY.setMaximum(500)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spnnOrigenY)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.spnnVelocidad = QSpinBox(self.groupBox)
        self.spnnVelocidad.setObjectName(u"spnnVelocidad")
        self.spnnVelocidad.setMaximum(500)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.spnnVelocidad)

        self.btnAgregarInicio = QPushButton(self.groupBox)
        self.btnAgregarInicio.setObjectName(u"btnAgregarInicio")
        self.btnAgregarInicio.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(14, QFormLayout.SpanningRole, self.btnAgregarInicio)

        self.btnMostrar = QPushButton(self.groupBox)
        self.btnMostrar.setObjectName(u"btnMostrar")
        self.btnMostrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.formLayout.setWidget(15, QFormLayout.SpanningRole, self.btnMostrar)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_9)

        self.spnnDistancia = QSpinBox(self.groupBox)
        self.spnnDistancia.setObjectName(u"spnnDistancia")
        self.spnnDistancia.setMaximum(255)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.spnnDistancia)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(280, 10, 411, 361))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 699, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Destino X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Destino Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.btnAgregarFinal.setText(QCoreApplication.translate("MainWindow", u"Agregar final", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Origen X:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Origen Y: ", None))
        self.btnAgregarInicio.setText(QCoreApplication.translate("MainWindow", u"Agregar inicio", None))
        self.btnMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Distancia:", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

