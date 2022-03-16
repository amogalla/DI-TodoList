import sys
from PySide6 import QtGui
from PySide6.QtCore import QAbstractListModel
from PySide6.QtGui import QStandardItemModel, Qt
from PySide6.QtWidgets import QApplication, QListView, QListWidgetItem, QMainWindow, QLabel, QLineEdit, QMessageBox, QVBoxLayout, QWidget, QPushButton
from ui_designmodel import Ui_MainWindow
import resources_rc
import json

class TaskModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.tareas = []

    def data(self, index, role):
        if(role == Qt.DisplayRole):
            return list(self.tareas)[index.row()]

    def rowCount(self, index):
        return len(self.tareas)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TaskModel()
        self.listView.setModel(self.model)
        self.botonNuevaTarea.clicked.connect(self.anyadirTarea)
        self.botonEliminarTodo.clicked.connect(self.eliminarTodo)
        self.actionBorrar_tarea.triggered.connect(self.eliminarTarea)
        self.model.tareas = self.leerJson()

    def leerJson(self):
        try:
            with open("tareas2.json") as fichero:
                tareas = json.load(fichero)
        except Exception:
            tareas = []
            with open("tareas2.json", "w") as file:
                json.dump(tareas, file)
        return tareas

    def anyadirTarea(self):
        self.model.tareas.append(self.nuevaTarea.toPlainText())

        with open("tareas2.json", "w") as fichero:
            json.dump(self.model.tareas, fichero)

        self.model.layoutChanged.emit()
        self.nuevaTarea.setPlainText("") #Una vez añadida la tarea, borramos el input

    def eliminarTarea(self):
        indice = int(self.listView.selectedIndexes()[0].row())
        self.model.tareas.remove(self.model.tareas[indice])
        self.listView.clearSelection() #Ya se ha eliminado del listview, por lo que borramos la selección de la tarea

        with open("tareas2.json", "w") as fichero:
            json.dump(self.model.tareas, fichero)

        self.model.layoutChanged.emit()

    def eliminarTodo(self):
        self.model.tareas = []

        with open("tareas2.json", "w") as fichero:
            json.dump(self.model.tareas, fichero)

        self.model.layoutChanged.emit() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()