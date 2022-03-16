# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QLabel,
    QLayout, QListView, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 387)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionBorrar_tarea = QAction(MainWindow)
        self.actionBorrar_tarea.setObjectName(u"actionBorrar_tarea")
        icon = QIcon()
        icon.addFile(u":/figuras/document--minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBorrar_tarea.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.nuevaTarea = QPlainTextEdit(self.centralwidget)
        self.nuevaTarea.setObjectName(u"nuevaTarea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nuevaTarea.sizePolicy().hasHeightForWidth())
        self.nuevaTarea.setSizePolicy(sizePolicy1)
        self.nuevaTarea.setMinimumSize(QSize(28, 28))
        self.nuevaTarea.setMaximumSize(QSize(16777215, 27))
        self.nuevaTarea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_2.addWidget(self.nuevaTarea, 4, 0, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 32))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)

        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.listView, 2, 0, 1, 4)

        self.botonEliminarTodo = QPushButton(self.centralwidget)
        self.botonEliminarTodo.setObjectName(u"botonEliminarTodo")
        sizePolicy1.setHeightForWidth(self.botonEliminarTodo.sizePolicy().hasHeightForWidth())
        self.botonEliminarTodo.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.botonEliminarTodo, 1, 0, 1, 1)

        self.botonNuevaTarea = QPushButton(self.centralwidget)
        self.botonNuevaTarea.setObjectName(u"botonNuevaTarea")
        sizePolicy1.setHeightForWidth(self.botonNuevaTarea.sizePolicy().hasHeightForWidth())
        self.botonNuevaTarea.setSizePolicy(sizePolicy1)
        self.botonNuevaTarea.setMinimumSize(QSize(28, 28))
        self.botonNuevaTarea.setMaximumSize(QSize(16777215, 27))
        self.botonNuevaTarea.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.botonNuevaTarea, 4, 2, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 459, 22))
        self.menuAcci_n = QMenu(self.menubar)
        self.menuAcci_n.setObjectName(u"menuAcci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuAcci_n.menuAction())
        self.menuAcci_n.addAction(self.actionBorrar_tarea)
        self.toolBar.addAction(self.actionBorrar_tarea)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBorrar_tarea.setText(QCoreApplication.translate("MainWindow", u"Borrar tarea", None))
#if QT_CONFIG(statustip)
        self.actionBorrar_tarea.setStatusTip(QCoreApplication.translate("MainWindow", u"Elimina una tarea de la lista", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionBorrar_tarea.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.nuevaTarea.setPlainText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Tareas pendientes</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.botonEliminarTodo.setStatusTip(QCoreApplication.translate("MainWindow", u"Elimina todas las tareas mostradas", None))
#endif // QT_CONFIG(statustip)
        self.botonEliminarTodo.setText(QCoreApplication.translate("MainWindow", u"Eliminar todas las tareas", None))
#if QT_CONFIG(statustip)
        self.botonNuevaTarea.setStatusTip(QCoreApplication.translate("MainWindow", u"A\u00f1ade una tarea a la lista", None))
#endif // QT_CONFIG(statustip)
        self.botonNuevaTarea.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir tarea", None))
        self.menuAcci_n.setTitle(QCoreApplication.translate("MainWindow", u"Acci\u00f3n", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

