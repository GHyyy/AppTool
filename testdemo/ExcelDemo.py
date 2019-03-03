# Created by Hank on 2018/6/29.
import xlsxwriter
import time

package_name_mysdk = 'com.tct.launcher'
timelong = 3600
timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
save_pc_path = 'D:\\mobile\\' + 'TestDemo_' + timeFile + '.xlsx'


def getCPU(package_name):
    # 用adb获取信息adb shell "dumpsys cpuinfo | grep com.tcl.live"
    p = subprocess.Popen('adb shell "dumpsys cpuinfo | grep" ' + package_name + '" "', stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    text = p.stdout.read()
    print(type(text))
    listoftext = text.split()
    # print ('PSS=' +
    # return int(listoftext[0])
    a = listoftext[0]
    return a.decode()


def getMemory(package_name):
    # 用adb获取信息adb shell "dumpsys meminfo com.aiwinn.lockscreen | grep "TOTAL""
    p = subprocess.Popen('adb shell "dumpsys meminfo" ' + package_name + '" | grep TOTAL"', stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    text = p.stdout.read()
    print(type(text))
    listoftext = text.split()
    # print ('PSS=' +
    # return int(listoftext[1])
    a = listoftext[1]
    return a.decode()


def saveExcel(timelong, cpu_list):
    test_book = xlsxwriter.Workbook(save_pc_path)  # 创建excel，并保存到指定路径
    worksheet = test_book.add_worksheet('test1')  # create sheet
    bold = test_book.add_format({'bold': True})  # 加粗
    headings = ['Time', 'PSS', 'CPU']  # titleName
    worksheet.write_row('A1', headings, bold)  # title

    data_cpu = [timelong, cpu_list]
    worksheet.write_comment('A2', data_cpu[0])
    worksheet.write_comment('B2', data_cpu[1])

    test_book.close()

def getApprunInfo():

    time_start = 0
    time_end = 0

    cpu_list = []
    while time_end <= 3600:
        try:
            cpu_info = getCPU(package_name_mysdk)
            cpu_list.append(float(cpu_info.split('%')[0]))
            saveExcel(timelong, cpu_list)
        except:
            print('异常')
    time_end += 1
    time.sleep(4)


getApprunInfo()