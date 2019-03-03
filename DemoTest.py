#!/usr/bin/sh python
# -*- coding: utf-8 -*-
import tkinter
from  tkinter  import ttk

def go(*args):   #处理事件，*args表示可变参数
    print(comboxlist.get()) #打印选中的值

win=tkinter.Tk() #构造窗体
comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(win,textvariable=comvalue) #初始化
tkinter.Label(win, text='持续时间(分)').grid(row=3, column=5)
pkg_list = [5,10,20,30,60] #持续执行时间以分钟为单位
pkg_combox = ttk.Combobox(win, values=pkg_list, width=5)
pkg_combox.current(0)
pkg_combox.grid(row=3,column=6)

win.mainloop() #进入消息循环