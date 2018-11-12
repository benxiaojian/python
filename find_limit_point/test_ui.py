# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
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

    def getRectList(self):
        return self.rect_list

    def mouseMoveEvent(self, e):
        if self.if_mouse_press:
            if self.sharp is not None:
                self.sharp.setEnd(e.pos())
                self.update()
            # self.rect_point[2] = e.pos().x()
            # self.rect_point[3] = e.pos().y()
            # self.update()

    def mousePressEvent(self, e):
        # print('mousePressEvent(%d,%d)\n' % (e.pos().x(), e.pos().y()))
        self.if_mouse_press = True
        self.sharp = Rect()
        if self.sharp is not None:
            self.rect_list.append(self.sharp)
            self.sharp.setStart(e.pos())
            self.sharp.setEnd(e.pos())
        self.update()
        # self.rect_point[0] = e.pos().x()
        # self.rect_point[1] = e.pos().y()
        # ui.move_point(e.pos().x(), e.pos().y())

    def mouseReleaseEvent(self, e):
        # print('mouseReleaseEvent(%d,%d)\n' % (e.pos().x(), e.pos().y()))
        self.if_mouse_press = False
        self.sharp = None
        self.update()

    def paintEvent(self, e):
        super().paintEvent(e)
        self.painter.begin(self)
        self.painter.setPen(QtGui.QPen(Qt.red, 2, Qt.SolidLine))

        if self.pos is not None:
            self.painter.setBrush(Qt.red)
            self.painter.drawEllipse(self.pos.x(), self.pos.y(), 20, 20)
            self.pos = None
        else:
            for sharp in self.rect_list:
                sharp.paint(self.painter)
                # print(sharp.rect)
        self.painter.end()

    def paintPoint(self, pos):
        self.pos = pos

class Eight:
    def __init__(self):
        self.mid_point = None
        self.mid_acreage = 0

    def calcMidPoint(self, rect_list):
        mid = QPoint()
        for rect in rect_list:
            mid.x = (rect.start.x() + rect.end.x()) / 2
            mid.y = (rect.start.y() + rect.end.y()) / 2
            acreage = abs(rect.start.x() - rect.end.x()) * (rect.start.y() - rect.end.y())

            if self.mid_point is None:
                self.mid_point = mid
                self.mid_acreage = acreage
            else:
                rate = self.acreage / (self.mid_acreage + acreage)
                x = (mid.x() - self.mid_point.x()) * rate + self.mid_point.x()
                y = (mid.y() - self.mid_point.y()) * rate + self.mid_point.y()
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.open_file.setText(_translate("MainWindow", "open"))
        self.print_lines.setText(_translate("MainWindow", "print line"))
        self.eight_lines.setText(_translate("MainWindow", "eight_lines"))

    def openFile(self):
        # img_name, img_type = QFileDialog.getOpenFileName(self, "打开图片", "", " *.jpg,*.png;;*.jpeg;;*.bmp;;All Files (*)")
        # if img_name == "":
        #     return

        img_name = 'timg.jpeg'

        pix = QtGui.QPixmap(img_name).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(pix)
        self.label.setCursor(Qt.CrossCursor)

    def findMidPoint(self):
        eight = Eight()
        pox = eight.getMidPoint(self.label.getRectList())
        print(pox.x, pox.y)
        self.label.paintPoint(pox)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow(main_window)

    main_window.show()

    sys.exit(app.exec())