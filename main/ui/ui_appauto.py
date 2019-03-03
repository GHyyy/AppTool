#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/15.
# Description: App Ui Auto


from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from main.adbutils.appAdb import *
import threading

# appauto
# save_pc_path = 'D:\\apptool\\'
save_pc_path = os.getcwd()
appauto_file = save_pc_path + 'appauto\\'
appauto_config = 'AppAuto.txt'
case_list = ['testLauncherSetting', 'testLauncherLscreen', 'testLscreenBoost', 'testLscreenFiles', 'testLscreenCpu',
                   'testLscreenBattery', 'testLscreenCalendar', 'testLscreenNotes', 'testLscreenFavorites', 'testLscreenWeathre',
                   'testLscreenExchange', 'testLscreenHoroscope', 'testLscreenManager', 'testLauncherSearch', 'testLauncherSearchSet',
                   'testLauncherFeedback','testLauncherThemeStore', 'testLauncherSearchSet']


# comboBox item
combox_data = ['1', '3', '5', '10', '20', '50', '100']


# case_list = readConfig()

def readConfig():
    try:
        txtSize = os.path.getsize(appauto_file + appauto_config)
        if txtSize == 0:
            print('本地配置为空')

        else:
            case_list = []  # 清空默认数据，重新存储read 数据
            with open(appauto_file + appauto_config, 'r+') as text:
                for line in text:
                    case_list.append(line.strip().rstrip(','))
                    # print(case_list[line])
    except:
        print('读取本地配置异常')


def create_file():
    try:
        if os.path.getsize(appauto_file + appauto_config) == 0:
            file_appauto = open(appauto_file + appauto_config, 'w+')
            for line in case_list:
                file_appauto.write(line + '\n')
            file_appauto.closed
            print('appauto -> ' + appauto_file)
        else:
            print('appauto 文件已创建')
    except:
        print(appauto_file + appauto_config)
# read local default config
create_file()
thread_read = threading.Thread(target=readConfig)
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



class Ui_Tab_appAuto(QtGui.QMainWindow):
    """
        TabWidget -> app Auto
    """

    def __init__(self, parent=None):
        super(Ui_Tab_appAuto, self).__init__()
        self.setupUi(self)
        self.add_pushbtn()

    def setupUi(self, Ui_Tab_appAuto):
        Ui_Tab_appAuto.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_appAuto.resize(700, 600)
        Ui_Tab_appAuto.setIconSize(QtCore.QSize(48, 48))

        self.centralwidget = QtGui.QWidget(Ui_Tab_appAuto)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_appAuto.setCentralWidget(self.centralwidget)
        # Label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 200, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText('Appauto')

        # listWidget
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 110, 360, 260))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.addItems(case_list)
        self.listWidget.clicked.connect(self.clicked_item)
        # textBrowser
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(5, 380, 680, 60))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        # label
        label = QtGui.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(560, 42, 54, 12))
        label.setObjectName(_fromUtf8("label"))
        label.setText("循环：")
        labe2 = QtGui.QLabel(self.centralwidget)
        labe2.setGeometry(QtCore.QRect(100, 96, 120, 12))
        labe2.setObjectName(_fromUtf8("label"))
        labe2.setText("Test case Selection：")
        # comboBox
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 36, 43, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        for index in range(len(combox_data)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(index, combox_data[index])
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox)
        # line
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 363, 700, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

    def add_pushbtn(self):
        # pushButton
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(525, 340, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText("Start")
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(530, 150, 55, 20))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_1.setText("Add")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 180, 55, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2.setText("Save")
        # self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_3.setGeometry(QtCore.QRect(400, 90, 55, 20))
        # self.pushButton_3.setObjectName(_fromUtf8("pushButton"))
        # self.pushButton_3.setText("Update")
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doStart)
        QtCore.QObject.connect(self.pushButton_1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.add)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_input)
        # QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update_btn)

    def clicked_item(self):
        """
            listView item 点击监听
        :param QModelIndex:
        :return:
        """
        global CASE_SELECTION
        item_str = case_list[self.listWidget.currentRow()]
        self.textBrowser.append('** Selected case：' + item_str)
        CASE_SELECTION = item_str
        # QMessageBox.information(self, 'ListView', '你选择了：' + self.qList[QModelIndex.row()])

    def readCombox(self):
        """
            循环次数 选择
        :return: loop_num
        """
        loop_num = self.comboBox.currentText()
        self.textBrowser.append('** 循环次数：' + loop_num)
        return int(loop_num)

    def doStart(self):
        """
            脚本 start
            1.case selection
            2.循环次数
        :return:
        """
        global LOOP_NUM
        LOOP_NUM = self.readCombox()

        thread = MyThread(self)
        thread.trigger.connect(self.update_text_r)  # 连接信号！
        thread.start()

    def update_text_r(self, message):
        self.textBrowser.insertPlainText(message)

    def update_btn(self):
        data = []
        self.listWidget.addItems(data)
        new_list = readConfig()
        self.listWidget.addItems(new_list)

    def add(self):
        # 添加
        add = case_listDlg('Add case', self)
        if add.exec_():
            case_list_added = add.case_list
            self.listWidget.addItem(case_list_added)
            print(case_list_added)
            case_list.append(case_list_added)
            for line in case_list:
                print('line-add:' + line)

    def edit(self):
        # 编辑
        row = self.listWidget.currentRow()
        case_list = self.listWidget.takeItem(row)
        edit = case_listDlg('Edit case', case_list.text(), self)
        if edit.exec_():
            print(edit.case_list)
            self.listWidget.addItem(edit.case_list)

    def remove(self):
        # 移除
        if QMessageBox.warning(self, u'AppAuto', u'Delete case?', QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
            item_deleted = self.listWidget.takeItem(self.listWidget.currentRow())
            # 将读取的值设置为None
            print('delete:' + str(self.listWidget.currentRow()))
            item_deleted = None

    def save_input(self):
        thread = MyThread_1(self)
        thread.trigger.connect(self.update_text_r)  # 连接信号！
        thread.start()


class MyThread(QtCore.QThread):
    """
        开启线程 执行 runUiautomator2()
    """
    trigger = QtCore.pyqtSignal(str)  # trigger传输的内容是字符串

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def setup(self, args):
        self.args = args

    def run(self):  # 很多时候都必重写run方法, 线程start后自动运行
        self.my_function()

    def my_function(self):
        # 把代码中的print全部改为trigger.emit
        device_status = deviceName()
        if device_status is True:
            self.trigger.emit("\n** 开始执行脚本...")
            i = 0
            while i <= LOOP_NUM:
                try:
                    runUiautomator2(case_name=CASE_SELECTION)
                    self.trigger.emit("\n** 执行第：" + i + "次")
                    i += 1
                except:
                    self.trigger.emit("\n** 执行失败!")
                    break

            self.trigger.emit("\n** 执行结束！")
        else:
            self.trigger.emit("\n** Device is not found,please check your device adb!")


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
            txtSize = os.path.getsize(appauto_file + appauto_config)
            if txtSize == 0:
                self.trigger.emit("\n** 本地 配置为空")
            else:
                self.trigger.emit("\n** 更新本地配置！")
                file_input = open(appauto_file + appauto_config, 'w+')
                for line in case_list:
                    file_input.write(line + '\n')
                    print('line:' + line)
                file_input.closed

        except:
            self.trigger.emit("\n** 本地配置更新结束！")


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
