#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/24.

import time
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def txt_write(fileName,data):
    """
        list 写入到 txt中
    :param fileName:
    :param data:
    :return:
    """
    file_input = open(fileName, 'w+')
    for line in data:
        file_input.write(line + '\n')
    file_input.closed


def txt_write_http(fileName, data):
    """
        list 写入到 txt中
    :param fileName:
    :param data:
    :return:
    """
    file_input = open(fileName, 'a+')  # a+ 追加
    file_input.write(time_stamp + '\t' + data + '\n')
    file_input.closed



if __name__ == '__main__':
    # txt_write()
    print(time_stamp)
