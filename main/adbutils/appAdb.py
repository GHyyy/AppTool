# Created by Hank on 2018/7/4.
import subprocess
import time
import os
import shutil
import threading

package_name = 'com.tct.launcher'

timeFile = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
# save_pc_path = 'D:\\apptool\\logcat\\'
save_pc_path = os.getcwd()
logcatErrorFile = 'LogcatError_' + timeFile + '.txt'
logcatAllFile = 'LogcatAll_' + timeFile + '.txt'
monkeyReport = 'Monkey_' + timeFile + '.txt'
appAutoReport = 'AppAuto_' + timeFile + '.txt'
install_apk = 'C:/Users/hankhe/Downloads/Singed_zipalign_JoyLauncher_google_v7.0.1.8.0727.1_201807271618_release.apk'
# 全局变量
DEVICE_NAME = ''

def adbLogcatError():
    device = deviceName()
    if device is True:
        cmd = 'adb logcat -c && adb logcat -v time *:E ' + '>' + save_pc_path + logcatErrorFile
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def adbLogcatAll():
    device = deviceName()
    if device is True:
        cmd = 'adb logcat -v time  ' + '>' + save_pc_path + logcatAllFile
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def doMonkey(packagename):
    device = deviceName()
    if device is True:
        adbLogcatError()
        cmd = 'adb shell monkey -p ' + packagename + ' --pct-touch 30 --pct-motion 15 --pct-trackball 15 --pct-majornav 10 --pct-appswitch 30 -s %RANDOM% --throttle 300 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v 10000000 ' + '>' + save_pc_path + monkeyReport
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def doMonkeyEdit(cmd):
    adbLogcatError()
    log_monkey = save_pc_path + monkeyReport
    subprocess.Popen(cmd + '>' + log_monkey, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def deviceName():
    cmd = 'adb devices'
    adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = adb_cmd.stdout.read()
    str_length = len(text)
    if str_length > 29:
        text_list = text.split()[4]
        #print('device：' + text_list.decode())
        device_name = text_list.decode()
        print('** Device：' + device_name)
        device_status = True
    else:
        print('** Device is not found!')
        device_status = False
    return device_status


def clearAppCathch(packagename):
    device = deviceName()
    if device is True:
        cmd = 'adb shell pm clear ' + packagename
        adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = adb_cmd.stdout.read()
        print(text)


def pullAnr():
    device = deviceName()
    if device is True:
        cmd = 'adb pull /data/anr ' + save_pc_path
        adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = adb_cmd.stdout.read()
        print(text)


def uninstallApp(packagename):
    device = deviceName()
    if device is True:
        cmd = 'adb uninstall  ' + packagename
        adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = adb_cmd.stdout.read()
        print(text)


def killApp(packagename):
    device = deviceName()
    if device is True:
        cmd = 'adb shell am force-stop  ' + packagename
        adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = adb_cmd.stdout.read()
        print(text)


def installApp(file_path):
    device = deviceName()
    if device is True:
        cmd = 'adb install -r  ' + file_path
        adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = adb_cmd.stdout.read()
        print(text)
        return text


def createFile():
    if os.path.exists(save_pc_path) is True:
        shutil.rmtree(save_pc_path)
        print('删除已存在文件夹')
        os.mkdir(save_pc_path)
        print('创建文件夹')


def stopMonkey():
    cmd1 = 'adb shell ps | findstr monkey '
    cmd2 = 'adb shell kill '
    p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = p1.stdout.read()
    text_length = len(text)
    print(text_length)
    if text_length > 0:
        text1 = text.split()[1]
        monkey_pid = text1.decode()
        print('monkey_pid:' + monkey_pid)
        p2 = subprocess.Popen(cmd2 + monkey_pid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        txt = p2.stdout.read()
        print(txt)
        return monkey_pid



def listener_Timer():
    device_name = checkDevice()
    global timer
    timer = threading.Timer(5, listener_Timer) # point 以秒为单位
    timer.start()


def checkDevice():
    cmd = 'adb devices'
    adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = adb_cmd.stdout.read()
    str_length = len(text)
    if str_length > 29:
        text_list = text.split()[4]
        device_name = text_list.decode()
        return device_name
    else:
        return


def runUiautomator2(case_name):
    cmd = 'adb shell am instrument -w -r   -e debug false -e class com.hankhe.autotest.testcase.joylaunchertest#' + case_name + ' com.hankhe.autotest.test/android.support.test.runner.AndroidJUnitRunner ' + '>' + save_pc_path + monkeyReport
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    text = p.stdout.read()
    print(text)

def string_split():
    text = 'H an k.he\ndede'
    print(text.split('\n'))




if __name__ == '__main__':
    # print(checkDevice())
    # timer = threading.Timer(1, listener_Timer)  #首次启动
    # timer.start()
    # installApp(install_apk)
    # string_split()
    # print(monkey_pid())
    stopMonkey()
