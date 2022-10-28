from ui_mainwindow import Ui_MainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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
        """ Metodos para trabajar con la tabla """
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id_tabla)

    @Slot()
    def mostrar_tabla(self):
        self.ui.tableParticulas.setColumnCount(10)
        headers = ["id", "origen_x", "origen_y", "destino_x",
                   "destino_y", "veloicidad", "red", "green", "blue", "distancia"]
        self.ui.tableParticulas.setHorizontalHeaderLabels(headers)
        self.ui.tableParticulas.setRowCount(len(self.__lista))
        """ Empezamos a rellenar la tabla """
        row = 0
        for particula in self.__lista:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            veloicidad_widget = QTableWidgetItem(str(particula.veloicidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tableParticulas.setItem(row, 0, id_widget)
            self.ui.tableParticulas.setItem(row, 1, origen_x_widget)
            self.ui.tableParticulas.setItem(row, 2, origen_y_widget)
            self.ui.tableParticulas.setItem(row, 3, destino_x_widget)
            self.ui.tableParticulas.setItem(row, 4, destino_y_widget)
            self.ui.tableParticulas.setItem(row, 5, veloicidad_widget)
            self.ui.tableParticulas.setItem(row, 6, red_widget)
            self.ui.tableParticulas.setItem(row, 7, green_widget)
            self.ui.tableParticulas.setItem(row, 8, blue_widget)
            self.ui.tableParticulas.setItem(row, 9, distancia_widget)

            row += 1

    @Slot()
    def buscar_id_tabla(self):
        idBusqueda = self.ui.searchEdit.text()

        for particula in self.__lista:
            if idBusqueda == str(particula.id):
                self.ui.tableParticulas.clear()
                self.ui.tableParticulas.setColumnCount(10)
                headers = ["id", "origen_x", "origen_y", "destino_x",
                           "destino_y", "veloicidad", "red", "green", "blue", "distancia"]
                self.ui.tableParticulas.setHorizontalHeaderLabels(headers)
                self.ui.tableParticulas.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                veloicidad_widget = QTableWidgetItem(str(particula.veloicidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tableParticulas.setItem(0, 0, id_widget)
                self.ui.tableParticulas.setItem(0, 1, origen_x_widget)
                self.ui.tableParticulas.setItem(0, 2, origen_y_widget)
                self.ui.tableParticulas.setItem(0, 3, destino_x_widget)
                self.ui.tableParticulas.setItem(0, 4, destino_y_widget)
                self.ui.tableParticulas.setItem(0, 5, veloicidad_widget)
                self.ui.tableParticulas.setItem(0, 6, red_widget)
                self.ui.tableParticulas.setItem(0, 7, green_widget)
                self.ui.tableParticulas.setItem(0, 8, blue_widget)
                self.ui.tableParticulas.setItem(0, 9, distancia_widget)

                return
        QMessageBox.warning(
            self,
            "Error",
            f'No se ha encontrado una particula con el id: "{idBusqueda}"'
        )

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
