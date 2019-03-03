#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/7/15.

import sys
from importlib import reload

#sys.setdefaultencoding('utf8')
from PyQt4 import QtGui,QtCore

reload(sys)

# menu
class MenuTools(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(550, 450)
        self.setWindowTitle('Python PyQt4')

        exit = QtGui.QAction(QtGui.QIcon('exit.png'), '退出', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('退出程序')
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('文件')
        file.addAction(exit)


app = QtGui.QApplication(sys.argv)
menu = MenuTools()
menu.show()
sys.exit(app.exec_())