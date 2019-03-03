# Created by Hank on 2018/7/4.
import subprocess

package_name = 'com.tct.launcher'
def adbLogcat():
    device = deviceName()
    if device is True:
        cmd = 'adb logcat -c && adb logcat -v time *:E >d:/009.txt '
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def doMonkey(packagename):
    cmd = 'adb shell monkey -p ' + packagename + ' --pct-touch 30 --pct-motion 15 --pct-trackball 15 --pct-majornav 10 --pct-appswitch 30 -s %RANDOM% --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --monitor-native-crashes -v 10000000 >d:/monkey.txt'
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    adbLogcat()

def deviceName():
    cmd = 'adb devices'
    adb_cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = adb_cmd.stdout.read()
    print(text)
    str_length = len(text)
    if str_length > 29 :
        text_list = text.split()[4]
        print('device：' + text_list.decode())
        device_status = True
    else:
        print('device is not found!')
        device_status = False
    return device_status



if __name__ == '__main__':
    doMonkey(package_name)