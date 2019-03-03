#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/15.
# Description: App Ui Auto
import threading
import os
from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from main.httputils.requests_params import *
from main.httputils.http_request import *

# comboBox item
number_data = ['alone', 'all']
server_list = ['www.baidu.com']
client_data = ['1', '2', '3', '4', '5', '10', '20', '50', '100']
time_interval = ['3', '5', '10', '20', '60']



# requests
# save_pc_path = 'D:\\apptool\\'
save_pc_path = os.getcwd()
requests_file = save_pc_path + 'requests\\'
requests_config = 'ListConfig.txt'
interface_list = ['api/v1/config/keys', 'api/v1/upgrade/apk', 'api/v1/feedback/upload', 'api/v1/deviceId/get',
                   'api/advertising/list', 'api/v1/commonConfig/keys', 'api/v1/cityLocator/getLocation',
                    'api/v1/adSwitch/getStatus']
excel_path = requests_file + 'params.xlsx'

timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
result_path = requests_file + 'result.txt'
def readConfig():
    try:
        txtSize = os.path.getsize(requests_file + requests_config)
        if txtSize == 0:
            print('本地配置为空')
        else:
            interface_list = []   # 清空默认数据，重新存储read 数据
            with open(requests_file + requests_config, 'r+') as text:
                for line in text:
                    interface_list .append(line.strip().rstrip(','))
    except:
        print('读取本地配置异常')


def create_file():
    try:
        if os.path.getsize(requests_file + requests_config) == 0:
            file_appauto = open(requests_file + requests_config, 'w+')
            for line in interface_list:
                file_appauto.write(line + '\n')
            file_appauto.closed
            print('appauto -> ' + requests_file)
    except:
        print('')



# read local default config
create_file()
thread_read = threading.Thread(target=readConfig())
thread_read.start()





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


class Ui_Tab_requests(QtGui.QMainWindow):
    """
        TabWidget -> app Auto
    """

    def __init__(self, parent=None):
        super(Ui_Tab_requests, self).__init__()
        self.setupUi(self)
        self.add_comboBox()
        self.add_pushbtn()

    def setupUi(self, Ui_Tab_requests):
        Ui_Tab_requests.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_requests.resize(700, 600)
        Ui_Tab_requests.setIconSize(QtCore.QSize(48, 48))

        self.centralwidget = QtGui.QWidget(Ui_Tab_requests)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_requests.setCentralWidget(self.centralwidget)
        # Label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 200, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText('Requests')
        # listWidget
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 110, 360, 260))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.addItems(interface_list )
        self.listWidget.clicked.connect(self.clicked_item)
        # self.listWidget.clicked.connect(self.clicked_item)
        # textBrowser
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 380, 680, 60))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        # pushButton
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText("Start")
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_http)
        # self.pushButton_1.setGeometry(QtCore.QRect(363, 90, 55, 20))
        # self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
        # self.pushButton_1.setText("Update")
        # label
        label = QtGui.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(452, 135, 54, 12))
        label.setObjectName(_fromUtf8("label"))
        label.setText("Number：")
        labe2 = QtGui.QLabel(self.centralwidget)
        labe2.setGeometry(QtCore.QRect(60, 96, 120, 12))
        labe2.setObjectName(_fromUtf8("label"))
        labe2.setText("Interface Selection：")
        labe3 = QtGui.QLabel(self.centralwidget)
        labe3.setGeometry(QtCore.QRect(570, 135, 54, 12))
        labe3.setObjectName(_fromUtf8("label"))
        labe3.setText("Client：")
        # comboBox
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(496, 132, 53, 18))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox"))
        for index in range(len(number_data)):
            self.comboBox_2.addItem(_fromUtf8(""))
            self.comboBox_2.setItemText(index, number_data[index])
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox_2)
        # line
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 363, 700, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

    def clicked(self, QModelIndex):
        self.textBrowser.append('** Selected interface：' + self.interface_list [QModelIndex.row()])

    def readCombox(self):
        """
        Server 选择
        """
        global SERVER_ID
        server_name = self.comboBox.currentText()
        self.textBrowser.append('** Server选择：' + server_name)
        SERVER_ID = server_name
    def add_comboBox(self):
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(500, 36, 150, 25))
        self.comboBox.setObjectName(_fromUtf8('comboBox'))
        for index in range(len(server_list)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(index, server_list[index])
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox)

        self.comboBox_1 = QtGui.QComboBox(self)
        self.comboBox_1.setGeometry(QtCore.QRect(614, 132, 41, 18))
        self.comboBox_1.setObjectName(_fromUtf8('comboBox'))
        for index in range(len(client_data)):
            self.comboBox_1.addItem(_fromUtf8(""))
            self.comboBox_1.setItemText(index, client_data[index])
        QtCore.QObject.connect(self.comboBox_1, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox_1)

    def add_pushbtn(self):
        # pushButton
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(530, 210, 55, 20))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_1.setText("Add")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 240, 55, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2.setText("Save")
        # self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(400, 90, 55, 20))
        # self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        # self.pushButton_3.setText("Update")
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doStart)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_input)
        # QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update_btn)

    def clicked_item(self):
        """
            listView item 点击监听
            INTERFACE_ITEM  Selected interface
        """

        global INTERFACE_ITEM
        global INTERFACE_INDEX
        item_str = interface_list[self.listWidget.currentRow()]
        self.textBrowser.append('** Selected interface：' + item_str)
        item = self.listWidget.currentRow()

        INTERFACE_ITEM = item_str
        INTERFACE_INDEX = item

    def readCombox_1(self):
        """
        Client数量选择
        """
        global CLIENT_GROUP
        client_num = self.comboBox_1.currentText()
        self.textBrowser.append('** Client数量选择：' + client_num)
        CLIENT_GROUP = int(client_num)

    def readCombox_2(self):
        """
        Interface 执行数量选择  alone / all
        """
        global INTERFACE_APPOINT
        interface_num = self.comboBox_2.currentText()
        self.textBrowser.append('** Interface数量选择：' + interface_num)
        INTERFACE_APPOINT = interface_num

    def update_text_r(self, message):
        self.textBrowser.insertPlainText(message)

    def add(self):
        # 添加
        add = case_listDlg('Add interface', self)
        if add.exec_():
            case_list_added = add.case_list
            self.listWidget.addItem(case_list_added)
            print(case_list_added)
            interface_list.append(case_list_added)
            for line in interface_list:
                print('line-add:' + line)

    def save_input(self):
        thread = MyThread_1(self)
        thread.trigger.connect(self.update_text_r)  # 连接信号！
        thread.start()

    def start_http(self):
        thread = MyThread_2(self)
        thread.trigger.connect(self.update_text_r)
        thread.start()


class MyThread_1(QtCore.QThread):
    """
        开启线程 save list update to local config
    """
    trigger = QtCore.pyqtSignal(str)  # trigger传输的内容是字符串

    def __init__(self, parent=True):
        super(MyThread_1, self).__init__(parent)

    def setup(self, args):
        self.args = args

    def run(self):
        self.my_update()

    def my_update(self):
        try:
            txtSize = os.path.getsize(requests_file + requests_config)
            if txtSize == 0:
                self.trigger.emit("\n** 本地 配置为空")
            else:
                self.trigger.emit("\n** 更新本地配置！")
                file_input = open(requests_file + requests_config, 'w+')
                for line in interface_list:
                    file_input.write(line + '\n')
                    print('line:' + line)
                file_input.closed

        except:
            self.trigger.emit("\n** 本地配置更新结束！")


class MyThread_2(QtCore.QThread):
    """
        开启线程  doStart http requests
    """
    trigger = QtCore.pyqtSignal(str)  # trigger传输的内容是字符串

    def __init__(self, parent=True):
        super(MyThread_2, self).__init__(parent)

    def setup(self, args):
        self.args = args

    def run(self):
        self.my_update()

    def my_update(self):
        try:
            url = 'http://' + SERVER_ID + '/' + INTERFACE_ITEM
            params = excel_read(filename=excel_path, sheetid=INTERFACE_INDEX, rownum=CLIENT_GROUP)
            for index in range(len(params)):
                result = http_post_from(url=url, params=params[index], filename=result_path)
                self.trigger.emit("\n** 执行第：" + str(index + 1) + '次\t' + result)
        except:
            self.trigger.emit("\n** 执行结束！")


class case_listDlg(QDialog):
    """
        弹出对话框
    """

    def __init__(self, title, case_list=None, parent=None):
        super(case_listDlg, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

        label_0 = QLabel(title)
        # 让标签字换行
        label_0.setWordWrap(True)
        self.case_list_edit = QLineEdit(case_list)
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

        validator = QRegExp(r'[^\s][\w\s]+')
        self.case_list_edit.setValidator(QRegExpValidator(validator, self))

        v_box = QVBoxLayout()
        v_box.addWidget(label_0)
        v_box.addWidget(self.case_list_edit)
        v_box.addWidget(btns)
        self.setLayout(v_box)

        self.case_list = None

    def accept(self):
        # OK按钮
        self.case_list = self.case_list_edit.text()
        # self.done(0)
        QDialog.accept(self)

    def reject(self):
        # self.done(1)
        QDialog.reject(self)


