#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/6/29.
import re
import os
import xlsxwriter
import time
import subprocess

timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
save_pc_path = 'D:\\apptool\\performance\\' + 'Performance_' + timeFile + '.xlsx'
package_name = 'com.threegene.yeemiao'


def getCPU(package_name):
    cmd = 'adb shell "dumpsys cpuinfo | grep" ' + package_name + '" "'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = p.stdout.read()
    listoftext = text.split()
    if listoftext:
        a = listoftext[0]
        print('CPU:' + a.decode())
        return a.decode()
    else:
        return 0


def get_cpu_top(package_name):
    li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    for line in li:
        if re.findall(package_name, line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == package_name:
                while '' in cuplist:
                    cuplist.remove('')
                return int(cuplist[2].strip('%'))


def getMemory(package_name):
    cmd = 'adb shell "dumpsys meminfo" ' + package_name + '" | grep TOTAL"'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = p.stdout.read()
    listoftext = text.split()
    a = listoftext[1]
    print('PSS:' + a.decode())
    return a.decode()


def deviceName():
    cmd = 'adb devices'
    adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = adb_cmd.stdout.read()
    print(text)
    str_length = len(text)
    if str_length > 29:
        text_list = text.split()[4]
        print('device：' + text_list.decode())
        device_status = True
    else:
        print('device is not found!')
        device_status = False
    return device_status


def get_uid(package_name):
    uid_cmd = 'adb shell "dumpsys package %s  | grep userId"' % (package_name)
    p1 = subprocess.Popen(uid_cmd, shell=True, stdout=subprocess.PIPE)
    uidLongString = p1.stdout.read()
    uid_info = uidLongString.decode('UTF-8', 'strict')
    uidLongList = uid_info.split()
    if uidLongList:
        uidMap = uidLongList[0]
        uid = uidMap.split("=")
        uid = uid[1]
        return uid
    else:
        return None


def get_rev(uid):
    """
    get tcp_rcv 接收流量 不区分 wifi/移动流量
    :return: bytes
    """
    rev_cmd = 'adb shell "cd proc && cd uid_stat && cd ' + uid + ' && cat tcp_rcv"'
    try:
        p_rev = subprocess.Popen(rev_cmd, shell=True, stdout=subprocess.PIPE)
        flo_rec = float(p_rev.stdout.read()) // 1024
        return flo_rec
    except:
        print(' No such file or directory')


def get_sen(uid):
    """
    get tcp_snd 发送流量   不区分 wifi/移动流量
    :return: bytes
    """
    sen_cmd = 'adb shell "cd proc && cd uid_stat && cd ' + uid + ' && cat tcp_snd"'
    try:
        p_rev = subprocess.Popen(sen_cmd, shell=True, stdout=subprocess.PIPE)
        flo_sen = float(p_rev.stdout.read()) // 1024
        return flo_sen
    except:
        print(' No such file or directory')


def saveExcel(time_id, app_pss, app_cpu, tcp_rev, tcp_snd, tcp_sum, package_name):
    workbook = xlsxwriter.Workbook(save_pc_path)
    worksheet = workbook.add_worksheet('性能数据')
    bold = workbook.add_format({'bold': 1})
    headings = ['Time', 'CPU', 'PSS', 'TCP_rcv', 'TCP_snd', 'TCP_sum', package_name]
    data = [time_id, app_cpu, app_pss, tcp_rev, tcp_snd, tcp_sum]
    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    worksheet.write_column('E2', data[4])
    worksheet.write_column('F2', data[5])
    print('Save success')
    workbook.close()


def doStartapp(package, time_fr, time_interval):
    device_status = deviceName()
    if device_status is True:
        app_uid = get_uid(package)
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
        while i <= time_fr:
            try:
                time_Now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                pss = getMemory(package)
                cpu = get_cpu_top(package_name)
                rcv = get_rev(app_uid)
                snd = get_sen(app_uid)
                print(pss)

                time_list.append(time_Now)
                cpu_list.append(cpu)
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
                tcp_sum .append(tcp_rcv_cal[i] + tcp_snd_cal[i])
                total_t = 0
                for x in range(len(tcp_sum)):
                    total_t += tcp_sum[x]
                tcp_total.append(total_t)
                # print(tcp_rcv_cal)

                saveExcel(time_id=time_list, app_pss=pss_list, app_cpu=cpu_list, tcp_rev=tcp_rcv_cal, tcp_snd=tcp_snd_cal,
                          tcp_sum=tcp_total, package_name=package)
                i += 1
                time.sleep(time_interval)
            except:
                print('Data get Failed!')
                break

def test_cpu():
    while True:
        print(get_cpu_top(package_name))

if __name__ == '__main__':
    time_frequency = 10  # 次数
    time_interval = 5  # 单位 s
    # doStartapp()
    # t = threading.Thread(target=doStartapp(package_name=package_name,time_frequency=time_frequency,time_interval=time_interval))
    # t.start()
    doStartapp(package_name, 100, 2)
    # test_cpu()