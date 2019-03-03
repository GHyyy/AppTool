#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/14.
from PyQt4 import QtCore, QtGui
from main.adbutils.appAdb import *

timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
# save_pc_path = 'D:\\apptool\\'
save_pc_path = os.getcwd()
monkey_file = save_pc_path + 'monkey\\'
apk_config = 'apkPath.txt'
monkey_config = 'monkey.txt'
monkey_path = monkey_file + monkey_config
monkey_default = 'adb shell monkey -p com.baidu.searchbox --pct-touch 30 --pct-motion 15 --pct-trackball 15 --pct-majornav 10 --pct-appswitch 30 -s %RANDOM% --throttle 300 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v 10000000'


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

    
class Ui_Tab_monkey(QtGui.QMainWindow):
    """
        TabWidget -> Monkey UI
    """
    def __init__(self, parent=None):
        super(Ui_Tab_monkey, self).__init__()
        self.setupUi(self)
        self.update_ui()

    def setupUi(self, Ui_Tab_monkey):
        Ui_Tab_monkey.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_monkey.resize(700, 600)
        Ui_Tab_monkey.setIconSize(QtCore.QSize(48, 48))

        self.centralwidget = QtGui.QWidget(Ui_Tab_monkey)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_monkey.setCentralWidget(self.centralwidget)
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
        # pushButton()
        pushButton = QtGui.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(510, 90, 71, 30))
        pushButton.setObjectName(_fromUtf8(''))
        pushButton.setText("Stop")

        pushButton_1 = QtGui.QPushButton(self)
        pushButton_1.setGeometry(QtCore.QRect(510, 250, 71, 30))
        pushButton_1.setObjectName(_fromUtf8(''))
        pushButton_1.setText("Save")

        pushButton_2 = QtGui.QPushButton(self)
        pushButton_2.setGeometry(QtCore.QRect(100, 250, 71, 30))
        pushButton_2.setObjectName(_fromUtf8(''))
        pushButton_2.setText("Edit")

        # TextEdit
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(100, 180, 480, 68))
        self.textEdit.setObjectName(_fromUtf8(''))
        self.textEdit.setText(monkey_default)
        self.textEdit.setReadOnly(True)
        # print(textEdit.toPlainText())

        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 300, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_monkey.setCentralWidget(self.centralwidget)
        # textEdit
        self.textEdit_1 = QtGui.QTextBrowser(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(10, 320, 670, 110))
        self.textEdit_1.setObjectName(_fromUtf8("textEdit"))


        # 控件添加 监听（钩子）
        QtCore.QObject.connect(commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doMonkey)
        QtCore.QObject.connect(pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.killMonkey)
        QtCore.QObject.connect(pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_monkey)
        QtCore.QObject.connect(pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.setText_edit)


    def doMonkey(self):
        # device = checkDevice()
        # self.textEdit_1.append('** Device：' + device)
        if os.path.exists(monkey_path) is True:
            cmd = self.read_input()
            doMonkeyEdit(cmd)
            self.textEdit_1.append('** 执行Monkey:\n' + cmd)
        else:
            doMonkeyEdit(monkey_default)
            self.textEdit_1.append('** 执行Monkey:\n' + monkey_default)

    def killMonkey(self):
        monkey_pid = stopMonkey()
        if monkey_pid is not None:
            self.textEdit_1.append('** stopMonkey:\n' + 'monkey PID：' +monkey_pid)
        else:
            self.textEdit_1.append('** 未找到对应monkey pid')

    def update_ui(self):
        if os.path.exists(monkey_path) is True:
            self.textEdit.setText(self.read_input())
            self.textEdit.setReadOnly(True)

    def setText_edit(self):
        self.textEdit.setReadOnly(False)
        self.textEdit_1.append('** 进行编辑...')

    def save_monkey(self):
        cmd = self.textEdit.toPlainText()
        self.write_input(cmd)
        self.textEdit.setReadOnly(True)
        self.textEdit_1.append('** 保存成功')

    def write_input(self, cmd):
        file_input = open(monkey_file + monkey_config, 'w+')
        file_input.write(cmd)
        file_input.closed

    def read_input(self):
        file_input = open(monkey_file + monkey_config, 'r+')
        cmd = file_input.read()
        file_input.closed
        return cmd


