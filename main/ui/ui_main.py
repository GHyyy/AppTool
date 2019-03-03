# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hankhe\Desktop\test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
# Created by Hank on 2018/7/11.
# Description: Main UI

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication

from main.adbutils.appAdb import *
from main.ui.ui_adb import Ui_Tab_adb
from main.ui.ui_monkey import Ui_Tab_monkey
from main.ui.ui_performance import Ui_Tab_performance
from main.ui.ui_appauto import Ui_Tab_appAuto
from main.ui.ui_httprequests import Ui_Tab_requests
from main.otherutils.fileprocess import *
from main.httputils.requests_params import *

# default config
timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
# save_pc_path = 'D:\\apptool\\'
save_pc_path = os.getcwd()
monkey_file = save_pc_path + 'monkey\\'
apk_config = 'apkPath.txt'
monkey_config = 'monkey.txt'
monkey_path = monkey_file + monkey_config
monkey_default = 'adb shell monkey -p  com.threegene.yeemiao  --pct-touch 30 --pct-motion 15 --pct-trackball 15 --pct-majornav 10 --pct-appswitch 30 -s %RANDOM% --throttle 300 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v 10000000'
logcatErrorFile = 'LogcatError_' + timeFile + '.txt'
logcatAllFile = 'LogcatAll_' + timeFile + '.txt'
monkeyapptool = 'Monkey_' + timeFile + '.txt'
performance_file = save_pc_path + 'performance\\'
# logcat
logcat_file = save_pc_path + 'logcat\\'
# appauto
appauto_file = save_pc_path + 'appauto\\'
appauto_config = 'AppAuto.txt'
appauto_default = []
# httpRequests
requests_file = save_pc_path + 'requests\\'
requests_config = 'ListConfig.txt'
requests_default = []
excel_path = requests_file + 'params.xlsx'
result_path = requests_file + 'result.txt'
result_data = ''

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


def createFile():
    """
        创建文件路径 ：D:/apptool
    """
    # apptool
    if os.path.exists(save_pc_path) is True:
        print('路径已存在 -> ' + save_pc_path)
    else:
        os.mkdir(save_pc_path)
        print('创建保存路径 -> ' + save_pc_path)
    # config
    if os.path.exists(monkey_file) is True:
        print('monkey文件已存在 -> ' + monkey_file)
    else:
        os.mkdir(monkey_file)
        print('monkey文件已创建 -> ' + monkey_file)
    # logcat
    if os.path.exists(logcat_file) is True:
            print('logcat文件已存在 -> ' + logcat_file)
    else:
        os.mkdir(logcat_file)
        print('logcat文件已创建 -> ' + logcat_file)
    # performance
    if os.path.exists(performance_file) is True:
        print('performance文件已存在 -> ' + performance_file)
    else:
        os.mkdir(performance_file)
        print('performance文件已创建 -> ' + performance_file)
    # appauto
    if os.path.exists(appauto_file) is True:
        print('appauto文件已存在 -> ' + appauto_file)
    else:
        os.mkdir(appauto_file)
        txt_write(appauto_file + appauto_config, appauto_default)
        print('appauto文件已创建 -> ' + appauto_file)
    # httpRequests
    if os.path.exists(requests_file) is True:
        print('httpRequests文件已存在 -> ' + requests_file)
    else:
        os.mkdir(requests_file)
        txt_write(requests_file + requests_config, requests_default)
        excel_create(excel_path)
        txt_write_http()
        print('httpRequests文件已创建 -> ' + requests_file)


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


class Ui_Main(QtGui.QMainWindow):
    """
        主UI，UI父框架
    """

    def __init__(self, parent=None):
        super(Ui_Main, self).__init__()
        self.setupUi(self)
        self.Tab_Widget()
        self.CommandLink_Button()
        self.pushbutton_check()

    def setupUi(self, Ui_Main):
        Ui_Main.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Main.resize(700, 600)
        Ui_Main.setIconSize(QtCore.QSize(48, 48))
        Ui_Main.setWindowIcon(QtGui.QIcon('main48.ico'))
        Ui_Main.setWindowTitle(_translate("Ui_Main", "AppTool", None))
        # 屏蔽窗口最大化
        Ui_Main.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

        # menuebar
        exit = QtGui.QAction(QtGui.QIcon('main48.ico'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        #


        # Event 监听
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

    def Tab_Widget(self):
        # 嵌套 一个 QTabWidget
        tabwidget = QtGui.QTabWidget(self)
        tabwidget.addTab(Ui_Tab_adb(), 'Adb')
        tabwidget.addTab(Ui_Tab_monkey(), 'Monkey')
        tabwidget.addTab(Ui_Tab_performance(), 'Performance')
        tabwidget.addTab(Ui_Tab_appAuto(), 'AppAuto')
        tabwidget.addTab(Ui_Tab_requests(), 'HttpRequests')

        tabwidget.setGeometry(QtCore.QRect(3, 25, 697, 462))  # 500 tab widget height

    def CommandLink_Button(self):
        commandLinkButton_1 = QtGui.QCommandLinkButton(self)
        commandLinkButton_1.setGeometry(QtCore.QRect(40, 520, 131, 41))
        commandLinkButton_1.setObjectName(_fromUtf8(''))
        commandLinkButton_1.setText("查看文件")
        QtCore.QObject.connect(commandLinkButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openWin)

    def pushbutton_check(self):
        pushbutton = QtGui.QPushButton(self)
        pushbutton.setGeometry(QtCore.QRect(520, 520, 100, 35))
        pushbutton.setObjectName(_fromUtf8(''))
        pushbutton.setText("检查设备")
        QtCore.QObject.connect(pushbutton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.check_device)

    def openWin(self):
        try:
            filename = QtGui.QFileDialog.getOpenFileName(self, '打开文件', save_pc_path)
            file = open(filename)
            data = file.read()
            print(data)
            self.textEdit.setText(data)
        except:
            print('无EditText控件展示')

    def check_device(self):
        device_status = checkDevice()
        if device_status is not None:
            self.statusBar().showMessage('Device：' + device_status)
        else:
            self.statusBar().showMessage('Device is not found!')



if __name__ == '__main__':
    thread_file = threading.Thread(target=createFile)
    thread_file.start()
    app = QApplication(sys.argv)
    myapp = Ui_Main()
    myapp.show()
    sys.exit(app.exec_())
