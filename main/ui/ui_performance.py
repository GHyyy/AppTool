#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/13.



from PyQt4 import QtCore, QtGui

from main.adbutils.performance import *

# comboBox item 数据
pkg_list = ['com.threegene.yeemiao']

time_long = ['5', '10', '20', '30', '60', '90', '120']
time_interval = ['3', '5', '10', '20', '60']

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


class Ui_Tab_performance(QtGui.QMainWindow):
    """
        TabWidget -> Other
    """

    def __init__(self, parent=None):
        super(Ui_Tab_performance, self).__init__()
        self.setupUi(self)
        self.add_comboBox()
        self.add_label()
        self.add_pushBtn()

    def setupUi(self, Ui_Tab_performance):
        Ui_Tab_performance.setObjectName(_fromUtf8("Ui_Main"))
        Ui_Tab_performance.resize(700, 600)
        Ui_Tab_performance.setIconSize(QtCore.QSize(48, 48))

        self.centralwidget = QtGui.QWidget(Ui_Tab_performance)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        # line horizontal
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 690, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        Ui_Tab_performance.setCentralWidget(self.centralwidget)
        # Label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 200, 40))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Agency FB\";\n"
                                           "font: 20pt \"黑体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setText('pss/cpu/流量')
        # textBrowser
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(56, 170, 571, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

    def add_comboBox(self):
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(520, 36, 131, 22))
        self.comboBox.setObjectName(_fromUtf8('comboBox'))
        for index in range(len(pkg_list)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(index, pkg_list[index])
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox)

        self.comboBox_1 = QtGui.QComboBox(self)
        self.comboBox_1.setGeometry(QtCore.QRect(136, 146, 41, 18))
        self.comboBox_1.setObjectName(_fromUtf8('comboBox'))
        for index in range(len(time_long)):
            self.comboBox_1.addItem(_fromUtf8(""))
            self.comboBox_1.setItemText(index, time_long[index])
        QtCore.QObject.connect(self.comboBox_1, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox_1)

        self.comboBox_2 = QtGui.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(564, 146, 41, 18))
        self.comboBox_2.setObjectName(_fromUtf8('comboBox'))
        for index in range(len(time_interval)):
            self.comboBox_2.addItem(_fromUtf8(""))
            self.comboBox_2.setItemText(index, time_interval[index])
        QtCore.QObject.connect(self.comboBox_2, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.readCombox_2)

    def add_label(self):
        label = QtGui.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(76, 150, 54, 12))
        label.setObjectName(_fromUtf8("label"))
        label.setText("时长/min：")
        label_2 = QtGui.QLabel(self.centralwidget)
        label_2.setGeometry(QtCore.QRect(516, 150, 54, 12))
        label_2.setObjectName(_fromUtf8("label_2"))
        label_2.setText("间隔/s：")

    def add_pushBtn(self):
        self.pushBtn = QtGui.QPushButton(self)
        self.pushBtn.setGeometry(QtCore.QRect(536, 370, 75, 23))
        self.pushBtn.setText("Start")

        QtCore.QObject.connect(self.pushBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.doCollection)

    def readCombox(self):
        package_name = self.comboBox.currentText()
        self.textBrowser.append('** 选择包名：' + package_name)
        # print('选择project ->' + packagen_name)
        return package_name

    def readCombox_1(self):
        time_long = self.comboBox_1.currentText()
        self.textBrowser.append('** 选择时长：' + time_long)
        print('选择时长 ->' + time_long)
        return time_long

    def readCombox_2(self):
        time_interval = self.comboBox_2.currentText()
        self.textBrowser.append('** 选择间隔：' + time_interval)
        # print('选择间隔 ->' + time_interval)
        return time_interval

    def doCollection(self):
        """
            采集
        """
        pkg_name = self.readCombox()
        time_long = int(self.readCombox_1())
        time_int = int(self.readCombox_2())
        time_fr = int(time_long * 60 / time_int)

        global PACKAGE_NAME
        global TIME_FREQUENCY
        global TIME_INTERVAL_1

        PACKAGE_NAME = pkg_name
        TIME_INTERVAL_1 = time_int
        TIME_FREQUENCY = time_fr

        thread = MyThread_r(self)  # 创建线程
        thread.trigger.connect(self.update_text_r)  # 连接信号！
        # thread.setup(range(10, 20)) # 传递参数
        thread.start()  # 启动线程

    def update_text_r(self, message):
        self.textBrowser.insertPlainText(message)


class MyThread_r(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)  # trigger传输的内容是字符串

    def __init__(self, parent=None):
        super(MyThread_r, self).__init__(parent)

    def setup(self, args):
        self.args = args

    def run(self):  # 很多时候都必重写run方法, 线程start后自动运行
        self.my_function()

    def my_function(self):
        # 把代码中的print全部改为trigger.emit
        device_status = deviceName()
        if device_status is True:
            self.trigger.emit("\n** 开始采集...\n")
            app_uid = get_uid(PACKAGE_NAME)
            if app_uid is None:
                self.trigger.emit("\n** 找不到目标app的进程...\n")
            time_list = []
            pss_list = []
            cpu_list = []
            tcp_rcv = []
            tcp_snd = []
            tcp_rcv_cal = []
            tcp_snd_cal = []
            tcp_sum = []
            tcp_total = []
            i = 0
            while i <= TIME_FREQUENCY:
                try:
                    time_Now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    pss = getMemory(PACKAGE_NAME)
                    cpu = getCPU(PACKAGE_NAME)
                    rcv = get_rev(app_uid)
                    snd = get_sen(app_uid)

                    time_list.append(time_Now)
                    cpu_list.append(float(cpu.split('%')[0]))
                    pss_list.append(int(pss))

                    tcp_rcv.append(rcv)
                    tcp_snd.append(snd)
                    if len(tcp_rcv) > 1:
                        tcp_rcv_cal.append(tcp_rcv[i] - tcp_rcv[i - 1])
                    else:
                        tcp_rcv_cal.append(float('0.0'))
                    print(tcp_snd)
                    if len(tcp_snd) > 1:
                        tcp_snd_cal.append(tcp_snd[i] - tcp_snd[i - 1])
                    else:
                        tcp_snd_cal.append(float('0.0'))
                    print(tcp_rcv_cal)
                    tcp_sum.append(tcp_rcv_cal[i] + tcp_snd_cal[i])
                    total_t = 0
                    for x in range(len(tcp_sum)):
                        total_t += tcp_sum[x]
                    tcp_total.append(total_t)

                    self.trigger.emit("** " + time_Now + '\t' + "pss：" + pss + '\t' + "cpu：" + cpu + '\t'
                                      + "下行流量：" + str(tcp_rcv_cal[i]) + '\t'
                                      + "上行流量：" + str(tcp_snd_cal[i]) + '\n')

                    saveExcel(time_id=time_list, app_pss=pss_list, app_cpu=cpu_list, tcp_rev=tcp_rcv_cal,
                              tcp_snd=tcp_snd_cal, tcp_sum=tcp_total, package_name=PACKAGE_NAME)
                    i += 1
                    time.sleep(TIME_INTERVAL_1)

                except:
                    self.trigger.emit("\n** Data get Failed!")
                    break

            self.trigger.emit("\n** Data get Completed！")
        else:
            self.trigger.emit("\n** Device is not found,please check your device adb!")
