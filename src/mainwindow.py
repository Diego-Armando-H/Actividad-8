from ui_mainwindow import Ui_MainWindow, QFileDialog, QMessageBox
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from listaParticulas import listaParticula
from Particula import Particula


class MainWindow(QMainWindow):
    __contador = 0

    def __init__(self):
        super(MainWindow, self).__init__()
        self.__lista = listaParticula()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAgregarInicio.clicked.connect(self.click_agregar_inicio)
        self.ui.btnAgregarFinal.clicked.connect(self.click_agregar_final)
        self.ui.btnMostrar.clicked.connect(self.mostrar)
        """ Metodos para el menu de la ventana """
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    """ Generación de eventos para acciones del menu """
    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.__lista.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                ("Se pudo crear el archivo " + ubicacion)
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                ("No pudo crear el archivo " + ubicacion)
            )

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            "Guardar archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.__lista.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                ("Se pudo abrir el archivo " + ubicacion)
            )
            self.ui.plainTextEdit.clear()
            self.ui.plainTextEdit.insertPlainText(str(self.__lista))
        else:
            QMessageBox.critical(
                self,
                "Error",
                ("No pudo abrir el archivo " + ubicacion)
            )

    @ Slot()
    def click_agregar_inicio(self):
        self.__lista.agregar_inicio(self.procesarParticula())
        self.__contador += 1

    @ Slot()
    def click_agregar_final(self):
        self.__lista.agregar_final(self.procesarParticula())
        self.__contador += 1

    @ Slot()
    def mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.__lista))

    def procesarParticula(self):
        """ id, origen_x, origen_y, destino_x, destino_y, veloicidad, red, green, blue, distancia """
        return Particula(self.__contador,
                         self.ui.spnnOrigenX.value(),
                         self.ui.spnnOrigenY.value(),
                         self.ui.spnnDestinoX.value(),
                         self.ui.spnnDestinoY.value(),
                         self.ui.spnnVelocidad.text(),
                         self.ui.spnnRed.value(),
                         self.ui.spnnBlue.value(),
                         self.ui.spnnGreen.value(),
                         self.ui.spnnDistancia.value())
