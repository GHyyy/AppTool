#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/7/16.

import sys

from importlib import reload

reload(sys)
# sys.setdefaultencoding('utf8')
from PyQt4 import QtGui, QtCore


class OpenFile(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('打开文件')
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        open = QtGui.QAction(QtGui.QIcon('mail.ico'), '打开', self)
        open.setShortcut('Ctrl+O')
        open.setStatusTip('打卡新文件')

        self.connect(open, QtCore.SIGNAL('triggered()'), self.showDialog)

        memnubar = self.menuBar()
        file = memnubar.addMenu('&File')
        file.addAction(open)

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, '打开文件', './')
        file = open(filename)
        data = file.read()
        print(data)
        self.textEdit.setText(data)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = OpenFile()
    myapp.show()
    sys.exit(app.exec_())
