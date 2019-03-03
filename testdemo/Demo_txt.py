#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/20.
save_pc_path = 'D:\\report\\'
appauto_file = save_pc_path + 'appauto\\'
appauto_config = 'AppAuto.txt'
case_list = ['22','33','66']

def read_txt():
    file_txt = open(appauto_file + appauto_config, 'r+')
    text = file_txt.read()
    case_list.append(text)
    file_txt.close()

    for index in range(len(case_list)):
        print('demo：' + case_list[index])

def read():
    case_list = []
    with open(appauto_file + appauto_config, 'r+') as f:
        for line in f:
            case_list.append(line.strip().rstrip(','))
    print(case_list)


if __name__ == '__main__':
    # read_txt()
    read()