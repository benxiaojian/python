# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import copy
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QPoint

global ui


class Rect:
    def __init__(self):
        self.start = QPoint()
        self.end = QPoint()

    def setStart(self, pos):
        self.start = pos

    def setEnd(self, pos):
        self.end = pos

    def paint(self, painter):
        painter.drawRect(self.start.x(), self.start.y(), self.end.x() - self.start.x(), self.end.y() - self.start.y())


class BtnLabel(QLabel):
    def __init__(self, parent=None):
        super(BtnLabel, self).__init__(parent)
        self.if_mouse_press = False
        self.rect_list = []
        self.sharp = None
        self.painter = QtGui.QPainter(self)
        self.paint_event = 0
        self.pos = None
        self.degree = 0
        self.action = None

    def clearPaint(self):
        self.if_mouse_press = False
        self.rect_list = []
        self.sharp = None
        self.painter = QtGui.QPainter(self)
        self.paint_event = 0
        self.pos = None
        self.degree = 0
        self.action = None

    def getRectList(self):
        return self.rect_list

    def mouseMoveEvent(self, e):
        if self.if_mouse_press:
            if self.sharp is not None:
                self.sharp.setEnd(e.pos())
                self.update()

    def mousePressEvent(self, e):
        self.if_mouse_press = True
        self.sharp = Rect()
        if self.sharp is not None:
            self.rect_list.append(self.sharp)
            self.sharp.setStart(e.pos())
            self.sharp.setEnd(e.pos())
        self.update()

    def mouseReleaseEvent(self, e):
        self.if_mouse_press = False
        self.sharp = None
        self.update()

    def paintEvent(self, e):
        super().paintEvent(e)
        self.painter.begin(self)
        self.painter.setPen(QtGui.QPen(Qt.red, 2, Qt.SolidLine))

        if self.action == "point":
            self.painter.setBrush(Qt.red)
            self.painter.drawEllipse(self.pos.x - 10, self.pos.y - 10, 20, 20)
        elif self.action == "rect":
            for sharp in self.rect_list:
                sharp.paint(self.painter)
                # print(sharp.rect)
        elif self.action == "lines":
            self.painter.setBrush(Qt.red)
            self.painter.drawEllipse(self.pos.x - 10, self.pos.y - 10, 20, 20)
            self.painter.translate(self.pos.x, self.pos.y)
            self.painter.setPen(QtGui.QPen(Qt.black, 2, Qt.SolidLine))
            self.painter.drawLine(QPoint(0, -400), QPoint(0, 400))
            self.painter.setPen(QtGui.QPen(Qt.red, 2, Qt.SolidLine))
            for i in range(0, 8):
                if i == 0:
                    self.painter.rotate(self.degree)
                else:
                    self.painter.rotate(i * 45)
                self.painter.drawLine(QPoint(0, 0), QPoint(0, 400))

        self.painter.end()

    def paintPoint(self, pos):
        self.pos = pos
        self.action = "point"
        self.update()

    def paintLines(self, degree):
        self.action = "lines"
        self.degree = degree
        self.update()

    def painRect(self):
        self.clearPaint()
        self.action = "rect"
        self.update()

    def paintClean(self):
        self.clearPaint()
        self.action = "rect"
        self.update()

class Eight:
    def __init__(self):
        self.mid_point = None
        self.mid_acreage = 0

    def calcMidPoint(self, rect_list):
        self.mid_point = None
        self.mid_acreage = 0
        mid = QPoint()
        for rect in rect_list:
            mid.x = (rect.start.x() + rect.end.x()) / 2
            mid.y = (rect.start.y() + rect.end.y()) / 2
            acreage = abs(rect.start.x() - rect.end.x()) * abs(rect.start.y() - rect.end.y())
            print(mid.x, mid.y, acreage)

            if self.mid_point is None:
                self.mid_point = QPoint()
                self.mid_point.x = mid.x
                self.mid_point.y = mid.y
                # self.mid_point = copy.deepcopy(mid)
                self.mid_acreage = acreage
            else:
                rate = acreage / (self.mid_acreage + acreage)
                print(rate)
                print("---", self.mid_point.x, self.mid_point.y)
                print(rate * (mid.x - self.mid_point.x))
                print(rate * (mid.y - self.mid_point.y))
                x = rate * (mid.x - self.mid_point.x) + self.mid_point.x
                y = rate * (mid.y - self.mid_point.y) + self.mid_point.y
                print(x, y)
                self.mid_point.x = x
                self.mid_point.y = y
                self.mid_acreage += acreage

    def getMidPoint(self, rect_list):
        self.calcMidPoint(rect_list)
        return self.mid_point

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 622)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = BtnLabel(self.centralwidget)
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

        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setGeometry(QtCore.QRect(430, 0, 80, 23))
        self.clean.setObjectName("clean")

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
        self.print_lines.clicked.connect(self.findMidPoint)
        self.eight_lines.clicked.connect(self.patinEightLines)
        self.clean.clicked.connect(self.patinClean)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "等待图片加载"))
        self.open_file.setText(_translate("MainWindow", "打开"))
        self.print_lines.setText(_translate("MainWindow", "定极点"))
        self.eight_lines.setText(_translate("MainWindow", "画八宫线"))
        self.clean.setText(_translate("MainWindow", "清空"))

    def openFile(self):
        img_name, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", "All Files (*);;*.jpg;;*.png;;*.jpeg;;*.bmp")
        if img_name == "":
            return

        pix = QtGui.QPixmap(img_name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pix)
        self.label.setCursor(Qt.CrossCursor)
        self.label.painRect()

    def findMidPoint(self):
        eight = Eight()
        pox = eight.getMidPoint(self.label.getRectList())
        print(pox.x, pox.y)
        self.label.paintPoint(pox)

    def patinEightLines(self):
        value, ok = QInputDialog.getDouble(self, "八宫线偏转角度", "输入加上天地人元龙角度后的偏转度数:", 22.5, -10000, 10000, 2)
        print(value)
        self.label.paintLines(value)

    def patinClean(self):
        self.label.paintClean()
        self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow(main_window)

    main_window.show()

    sys.exit(app.exec())