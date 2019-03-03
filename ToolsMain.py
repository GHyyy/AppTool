#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Hank on 2018/6/16.
# @Description    py to .exe

import threading
import tkinter
import time,datetime
from tkinter import *
from tkinter import messagebox,ttk

from com.tool.utils.log import logger,LOG
from com.tool.utils.py_excel import saveStartAppResult,saveCpuResult
from com.tool.adb.adbcommand import getDevicesStatus,starttime_app,getMemory,getCpu,getFlow
FLAG = True

@logger('cpu占用率,上传下载流量，内存的测试')
def cpuAppTest():

    status_devices = getDevicesStatus()
    if status_devices == 'device':
        cpupackagename = cpu_packagename.get('0.0', END).split()[0]
        sleepTime = int(intervaTime_t.get())  #间隔时间
        chixunTime = int(chixuntime_t.get())  #持续执行时间

        if len(cpupackagename) <= 5:
            LOG.info('包名必须真实有效')
            messagebox.showwarning('警告', '请检查您的包名')
        cishu_list = []
        cpu_list = []
        rescv_list = []
        send_list = []
        total_list = []
        pass_list = []
        i = 0

        current_time = datetime.datetime.now()
        time_end = current_time + datetime.timedelta(minutes=chixunTime) #最后结束时间

        while contrast(current_time,time_end):
            time.sleep(sleepTime)
            memory = getMemory(cpupackagename)
            rescv, send, flow_sum = getFlow(cpupackagename)
            cpu = getCpu(cpupackagename)
            memory_t['state'] = 'normal'
            pass_list.append(int(memory[:-1]))
            memory_t.insert(tkinter.END, ('Pass值：%s' % memory))
            LOG.info('第%s次：Pass：%s' % (i, memory))
            memory_t.insert(tkinter.END, '\n')
            memory_t.see(END)
            memory_t['state'] = 'disabled'

            cpu_t['state'] = 'normal'
            print(cpu.split('%')[0])
            cpu_list.append(float(cpu.split('%')[0]))
            cpu_t.insert(tkinter.END, ('CPU占有率：%s' % cpu))
            LOG.info('第%s次：CPU占用率：%s' % (i, cpu))
            cpu_t.insert(tkinter.END, '\n')
            cpu_t.see(END)
            cpu_t['state'] = 'disabled'

            flow_t['state'] = 'normal'
            total_list.append(int(flow_sum))
            rescv_list.append(int(rescv))
            send_list.append(int(send))
            flow_t.insert(tkinter.END, ('总流量：%sk,上传流量:%sk,下载流量：%sk' % (flow_sum, rescv, send)))
            LOG.info('第%s次：总流量：%sk,上传流量:%sk,下载流量：%sk' % (i, flow_sum, rescv, send))
            flow_t.insert(tkinter.END, '\n')
            flow_t.see(END)
            flow_t['state'] = 'disabled'
            cpu_btn['state'] = 'disabled'
            i+=1
            cishu_list.append(int(i))
            current_time = datetime.datetime.now()
        saveCpuResult(cishu=cishu_list, start_cpu=cpu_list, recv_list=rescv_list, send_list=send_list, total_list=total_list,
                      Pass_list=pass_list)
        cpu_btn['state'] = 'normal'
        LOG.info('测试完成')
        messagebox.showinfo('提醒', '测试完毕，测试报告已经生成！')
    else:
        LOG.info('测试的设备必须正常连接，请注意')
        messagebox.showwarning('警告', '设备连接异常 请重新连接设备!')


@logger('用线程来启动测试,采集cpu占用率,上传下载流量，内存')
def teread_cpu():
    for i in range(1):
        t = threading.Thread(target=cpuAppTest,args=())
        t.start()
    return t;

def contrast(data1,data2):
    datatime1 = datetime.datetime.strftime(data1,'%Y-%m-%d %H:%M:%S')
    datatime2 = datetime.datetime.strftime(data2,'%Y-%m-%d %H:%M:%S')
    if datatime1 <= datatime2:
        return True
    else:
        return False

if __name__ == "__main__":
    LOG.info('测试开启！')
    try:
        status_devices= getDevicesStatus() #获取设备状态
        if status_devices == 'device':
            root = tkinter.Tk()
            root.title("AppTestTool")
            # root.geometry("800x500")
            tkinter.Label(root, text='Performance', fg='red', font=("黑体", 13, "bold"), ).grid(row=1, column=3)

            tkinter.Label(root, text='包名：').grid(row=2, column=1)
            cpu_packagename = tkinter.Text(root, height=1, width=30)
            cpu_packagename.grid(row=2, column=2)

            tkinter.Label(root, text='cpu').grid(row=4, column=1)
            cpu_t = tkinter.Text(root, height=5, width=30)
            cpu_t.grid(row=4, column=2)

            tkinter.Label(root, text='内存').grid(row=3, column=1)
            memory_t = tkinter.Text(root, height=5, width=30)
            memory_t.grid(row=3, column=2,padx=10, pady=10)
            memory_t.see(END)

            tkinter.Label(root, text='流量').grid(row=2, column=3)
            flow_t = tkinter.Text(root, height=5, width=40)
            flow_t.grid(row=2, column=4,columnspan=3)
            flow_t.see(END)



            tkinter.Label(root, text='间隔时间(s)').grid(row=3, column=3)
            intervaTime_ev = [2,3, 5, 10, 15]  # 抓取时间间隔
            intervaTime_t = ttk.Combobox(root, values=intervaTime_ev, width=5)
            intervaTime_t.current(0)
            intervaTime_t.grid(row=3, column=4)

            tkinter.Label(root, text='持续时间(分)').grid(row=3, column=5)
            chixuntime_ev = [5,10,20,30,60] #持续执行时间以分钟为单位
            chixuntime_t = ttk.Combobox(root, values=chixuntime_ev, width=5)
            chixuntime_t.current(0)
            chixuntime_t.grid(row=3,column=6)

            cpu_btn = tkinter.Button(root, text='开始测试', font=("黑体", 15, "bold"), command=teread_cpu)
            cpu_btn.grid(row=7, column=3)

            root.mainloop()


        else:
            LOG('设备未连接或者连接异常!目前连接状态:%s' % status_devices)
            print(status_devices)
            print('设备未连接或者连接异常')
    except Exception as e:
        print(e)
        LOG.info('测试异常，原因：%s' % e)

