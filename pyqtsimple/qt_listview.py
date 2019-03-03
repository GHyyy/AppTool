#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/14.
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Tab_Monkey(QtGui.QMainWindow):
    """
        TabWidget -> Monkey UI
    """

    def __init__(self, parent=None):
        super(Ui_Tab_Monkey, self).__init__()
        self.setupUi(self)
        self.listview(self)

    def setupUi(self, Ui_Tab_Monkey):
        Ui_Tab_Monkey.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_Monkey.resize(700, 600)
        Ui_Tab_Monkey.setIconSize(QtCore.QSize(48, 48))
        Ui_Tab_Monkey.setAutoFillBackground(True)
        # Ui_Tab_Monkey.setPalette(QPalette(QColor(255, 255, 250)))

        self.centralwidget = QtGui.QWidget(Ui_Tab_Monkey)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_Monkey.setCentralWidget(self.centralwidget)
        # Label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 100, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText('Monkey')
        # commandLinkButton
        commandLinkButton = QtGui.QCommandLinkButton(self)
        commandLinkButton.setGeometry(QtCore.QRect(100, 90, 131, 41))
        commandLinkButton.setObjectName(_fromUtf8(''))
        commandLinkButton.setText("Monkey")

    def listview_ctl(self):
        self.listview = QtGui.QListView(self)
        self.listview.setGeometry(QtCore.QRect(140, 90, 131, 41))
        self.listview.setObjectName(_fromUtf8(''))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = Ui_Tab_Monkey()
    myapp.show()
    sys.exit(app.exec_())
