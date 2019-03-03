#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/29.


import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Test(unittest.TestCase):
    #用于测试用例执行前的初始化工作
    def setUp(self):
        print("test start")

    def test_bbb(self):
        print("test bbb")

    def test_aaa(self):
        print("test aaa")

    def test_ccc(self):
        print("test ccc")
        #用于测试用例执行之后的善后工作
    def tearDown(self):
        print("test end")
if __name__ == '__main__':

    suite=unittest.TestSuite()
    suite.addTest(Test("test_bbb"))
    suite.addTest(Test("test_aaa"))
    suite.addTest(Test("test_ccc"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    #定义报告存放路径
    filename='D:\\'+ now +'result.html'
    fp=open(filename,'wb')
    #定义测试报告
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
    runner.run(suite)
    fp.close()#关闭报告文件
