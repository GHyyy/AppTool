#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/14.
import sys
from PyQt4 import QtGui,QtCore
from main.adbutils.appAdb import *

timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
# save_pc_path = 'D:\\apptool\\'
save_pc_path = os.getcwd()
monkey_file = save_pc_path + 'monkey\\'
apk_config = 'apkPath.txt'
monkey_config = 'monkey.txt'

# print 输出重定向   True:开启   False:关闭
print_red = True
# comboBox item 数据
pkg_list = ['com.qq.cn', 'com.baidu.searchbox']

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


class Ui_Tab_adb(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Tab_adb, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.workerThread = WorkThread()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 700)
        MainWindow.setIconSize(QtCore.QSize(48, 48))

        # comboBox
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(520, 36, 131, 22))
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        for index in range(len(pkg_list)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(index, pkg_list[index])

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 51, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 180, 353))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_1 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_1.setObjectName(_fromUtf8("commandLinkButton_1"))
        self.verticalLayout.addWidget(self.commandLinkButton_1)
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton_4 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_4.setObjectName(_fromUtf8("commandLinkButton_4"))
        self.verticalLayout.addWidget(self.commandLinkButton_4)
        self.commandLinkButton_5 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_5.setObjectName(_fromUtf8("commandLinkButton_5"))
        self.verticalLayout.addWidget(self.commandLinkButton_5)
        self.commandLinkButton_6 = QtGui.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_6.setObjectName(_fromUtf8("commandLinkButton_6"))
        self.verticalLayout.addWidget(self.commandLinkButton_6)
        # line vertical
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(450, 64, 20, 500))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        # textEdit
        self.textEdit = QtGui.QTextBrowser(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 80, 200, 330))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        # 重定向输出 print()
        if print_red is True:
            sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
            sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)
        # pushButton
        self.setAcceptDrops(True)
        # self.pushButton_1 = Button(self.centralwidget)
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setAcceptDrops(True)
        self.pushButton_1.setGeometry(QtCore.QRect(320, 80, 71, 31))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 130, 71, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 180, 71, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 230, 71, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 280, 71, 31))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 330, 71, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 380, 71, 31))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox)

        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doInstall_app)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doUninstall_app)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doClear_app)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doKill_app)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doLog_E)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doLog_v)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doPull_anr)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('main48.ico'))
        MainWindow.setWindowTitle(_translate("MainWindow", "AppTool", None))


        self.label.setText(_translate("MainWindow", "ADB", None))
        self.commandLinkButton.setText(_translate("MainWindow", "InstallApp", None))
        self.commandLinkButton_1.setText(_translate("MainWindow", "UninstallApp", None))
        self.commandLinkButton_2.setText(_translate("MainWindow", "ClearApp", None))
        self.commandLinkButton_3.setText(_translate("MainWindow", "KillApp", None))
        self.commandLinkButton_4.setText(_translate("MainWindow", "LogcatError", None))
        self.commandLinkButton_5.setText(_translate("MainWindow", "LogcatAll", None))
        self.commandLinkButton_6.setText(_translate("MainWindow", "PullAnr", None))
        self.pushButton_1.setText(_translate("MainWindow", "Start", None))
        self.pushButton_2.setText(_translate("MainWindow", "Start", None))
        self.pushButton_3.setText(_translate("MainWindow", "Start", None))
        self.pushButton_4.setText(_translate("MainWindow", "Start", None))
        self.pushButton_5.setText(_translate("MainWindow", "Start", None))
        self.pushButton_6.setText(_translate("MainWindow", "Start", None))
        self.pushButton_7.setText(_translate("MainWindow", "Start", None))

    def monkeyConfig(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Monkey setting',
                                              'Enter your config:')
        if ok:
            # self.le.setText(str(text))

            print('monkey_config:', str(text))

    def readCombox(self):
        packagen_name = self.comboBox.currentText()
        print('选择project ->' + packagen_name)
        return packagen_name

    def doMonkey(self):
        packagen_name = self.readCombox()
        doMonkey(packagen_name)

    def doKill_app(self):
        print('** 执行：killApp')
        packagen_name = self.readCombox()
        killApp(packagen_name)

    def doLog_E(self):
        print('** 执行：logcat Error')
        adbLogcatError()

    def doLog_v(self):
        print('** 执行：logcat All')
        adbLogcatAll()

    def doPull_anr(self):
        print('** 执行：pull Anr')
        pullAnr()

    def doClear_app(self):
        print('** 执行：clear App')
        packagen_name = self.readCombox()
        clearAppCathch(packagen_name)

    def doUninstall_app(self):
        print('** 执行：uninstall App')
        packagen_name = self.readCombox()
        uninstallApp(packagen_name)

    def doInstall_app(self):
        print('** 执行：instll App')
        self.workerThread.start()

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def normalOutputWritten(self, text):
        """
            textEdit 展示 print内容
        """
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Ui_Tab_adb, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(Ui_Tab_adb, self).dragMoveEvent(event)

    def dropEvent(self, event):
        """
             file 路径识别（拖动）
        """
        if event.mimeData().hasUrls():

            # 遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                self.write_path(file_path)
                print('** 拖入文件:\n' + file_path)
            event.acceptProposedAction()
        else:
            super(Ui_Tab_adb, self).dropEvent(event)

    def write_path(self, apk_path):
        file_input = open(monkey_file + apk_config, 'w+')
        file_input.write(apk_path)
        file_input.closed


class Ui_Tab_Other(QtGui.QMainWindow):
    """
        TabWidget -> Other
    """
    def __init__(self, parent=None):
        super(Ui_Tab_Other, self).__init__()
        self.setupUi(self)

    def setupUi(self, Ui_Tab_Other):
        Ui_Tab_Other.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_Other.resize(700, 600)
        Ui_Tab_Other.setIconSize(QtCore.QSize(48, 48))

        self.centralwidget = QtGui.QWidget(Ui_Tab_Other)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_Other.setCentralWidget(self.centralwidget)
        # Label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 200, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText('developing...')


class EmittingStream(QtCore.QObject):
    """
         textEdit 展示 print内容
    """
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


class WorkThread(QtCore.QThread):
    """
        子线程 进行耗时操作
    """

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        print('** 开始安装app')
        apk_path = self.read_path()
        installApp(apk_path)

    def read_path(self):
        file_input = open(monkey_file + apk_config, 'r+')
        app_path = file_input.read()
        file_input.closed
        print(app_path)
        return app_path


class Button(QtGui.QPushButton):
    """
        pushButton 监听拖动event
    """

    def __init__(self, parent):
        super(Button, self).__init__(parent)
        self.setAcceptDrops(True)
        self.thread_btn = WorkThread()
        # self.setDragDropMode(QAbstractItemView.InternalMove)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Button, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(Button, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            # 遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls():
                # print(url.toLocalFile()).decode('UTF-8').encode('GBK')
                file_path = url.toLocalFile()
                self.write_path(file_path)
                print('** 拖入文件：' + '\n' + file_path)
                self.thread_btn.start()
            event.acceptProposedAction()
        else:
            super(Button, self).dropEvent(event)

    def write_path(self, apk_path):
        file_input = open(monkey_file + apk_path, 'w+')
        file_input.write(apk_path)
        file_input.closed
