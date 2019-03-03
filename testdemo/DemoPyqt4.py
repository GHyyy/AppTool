#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/7/15.

import sys
from importlib import reload

# sys.setdefaultencoding('utf8')
from PyQt4 import QtGui, QtCore

reload(sys)


def testWidget():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    widget.resize(350, 250)
    widget.setWindowTitle('widget')
    widget.show()
    sys.exit(app.exec_())


def testButton():
    app = QtGui.QApplication(sys.argv)
    btn = QtGui.QPushButton('关闭')
    btn.setWindowTitle('QPushButton')
    btn.show()
    sys.exit(app.exec_())


# button
class Quitbutton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Python PyQt4')

        # QPushButton
        quit = QtGui.QPushButton('close', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))


# menu
class MenuTools(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(550, 450)
        self.setWindowTitle('Python PyQt4')
        self.setWindowIcon(QtGui.QIcon('mail.ico'))

        exit = QtGui.QAction(QtGui.QIcon('exit.png'), '退出', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('退出程序')
        # 触发跳转事件
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('文件')
        file.addAction(exit)

        toolbar = self.addToolBar('toolbar')
        toolbar.addAction(exit)

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

class OpenFile(Q)

app = QtGui.QApplication(sys.argv)
menu = MenuTools()
menu.show()
sys.exit(app.exec_())
