# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
        self.Rectangle_list = [0, 0, 0, 0]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 781, 531))
        self.label.setObjectName("label")
        self.open_file = QtWidgets.QPushButton(self.centralwidget)
        self.open_file.setGeometry(QtCore.QRect(20, 0, 80, 23))
        self.open_file.setObjectName("open_file")
        self.print_lines = QtWidgets.QPushButton(self.centralwidget)
        self.print_lines.setGeometry(QtCore.QRect(150, 0, 80, 23))
        self.print_lines.setObjectName("print_lines")
        self.eight_lines = QtWidgets.QPushButton(self.centralwidget)
        self.eight_lines.setGeometry(QtCore.QRect(290, 0, 80, 23))
        self.eight_lines.setObjectName("eight_lines")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_file.clicked.connect(self.openFile)
        self.print_lines.clicked.connect(self.printBox)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.open_file.setText(_translate("MainWindow", "open"))
        self.print_lines.setText(_translate("MainWindow", "print line"))
        self.eight_lines.setText(_translate("MainWindow", "eight_lines"))


    def openFile(self):
        img_name, img_type= QFileDialog.getOpenFileName(self, "打开图片", "", " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        if img_name == "":
            return

        pix = QtGui.QPixmap(img_name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pix)


    def printBox(self):
        painter = QtGui.QPainter(self)
        painter.drawRect(self.Rectangle_list[0], self.Rectangle_list[1], self.Rectangle_list[2], self.Rectangle_list[3])


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print("鼠标点击")
        self.Rectangle_list[0] = e.x()
        self.Rectangle_list[1] = e.y()

        if e.button() == Qt.RightButton:
            self.Point_list.clear()
            self.Rectangle_list = [0, 0, 0, 0]
            self.update()


    def mouseMoveEvent(self, e):
        print("鼠标移动")
        self.Rectangle_list[2] = e.x() - self.Rectangle_list[0]
        self.Rectangle_list[3] = e.y() - self.Rectangle_list[1]
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow(main_window)

    main_window.show()

    sys.exit(app.exec())