import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QLabel, QLineEdit, QMessageBox, QVBoxLayout, QWidget, QPushButton
from ui_design import Ui_MainWindow
import resources_rc
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botonNuevaTarea.clicked.connect(self.anyadirTarea)
        self.botonEliminarTodo.clicked.connect(self.eliminarTodo)
        self.actionBorrar_tarea.triggered.connect(self.eliminarTarea)
        tareas = self.leerJsonInicial()

    def leerJson(self):
        try:
            with open("tareas.json") as fichero:
                tareas = json.load(fichero)

        except Exception:
            tareas = {}
            with open("tareas.json", "w") as file:
                json.dump(tareas, file)
        return tareas

    def leerJsonInicial(self):
        tareas = self.leerJson()
        
        for key in tareas:
            self.listaTareas.addItem(QListWidgetItem(tareas.get(key)))
        
        return tareas


    def anyadirTarea(self):
        tareas = self.leerJson()

        with open("tareas.json", "w") as file:
            json.dump(tareas, file)

        if(len(tareas)>0):
            ultimo = str(list(tareas)[-1])
        else: ultimo = 0
        siguiente = str((int(ultimo) + 1))

        tareas[siguiente] = self.nuevaTarea.toPlainText()  #Se añade al diccionario
        self.listaTareas.addItem(QListWidgetItem(tareas.get(siguiente))) #Se añade al ListWidget
        with open("tareas.json", "w") as file:
                json.dump(tareas, file)
                
        self.nuevaTarea.setPlainText("") #Una vez añadida la tarea, borramos el input

    def eliminarTarea(self):
        with open("tareas.json", "r") as fichero:
            tareas = json.load(fichero)

        
        indice = self.listaTareas.indexFromItem(self.listaTareas.currentItem()).row()
        indiceString = str(indice + 1)
        del tareas[''+ indiceString +'']  #Eliminamos la tarea del diccionario
        self.listaTareas.takeItem(indice) #Eliminamos la tarea del ListWidget

        #Restamos 1 unidad a todas las claves de los items siguientes al eliminado.
        if(len(tareas)!=0):
            ultimo = int(list(tareas)[-1])
            for i in range(indice+2, ultimo+1): #A partir del siguiente al eliminado los desplazamos un lugar hacia atrás
                tareas[''+str(i-1)+''] = tareas.pop(''+str(i)+'')

        with open("tareas.json", "w") as fichero:
            json.dump(tareas, fichero)


    def eliminarTodo(self):
        with open("tareas.json", "r") as fichero:
            tareas = json.load(fichero)

        ultimo = int(list(tareas)[-1])
        for i in range(1, ultimo+1):
            del tareas[''+ str(i) +'']   #Eliminamos la tarea del diccionario
            self.listaTareas.takeItem(0) #Eliminamos la tarea del ListWidget

        with open("tareas.json", "w") as fichero:
            json.dump(tareas, fichero)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()