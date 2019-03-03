#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Hank on 2018/8/27.

import xlsxwriter
import xlrd

excel_path = 'D:\\apptool\\requests\\params.xlsx'

data_key = []
data_value = []

def excel_create(filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})
    title_name = ['keys', 'country', 'model', 'pkg', 'sign']
    worksheet.write_row('A1', title_name, bold)
    workbook.close()


def excel_read(filename, sheetid, rownum):
    """
    :param filename: excel文件
    :param sheetname: sheet index  type: int
    :param rownum: clinet数 对应excel 行数  type: int
    :return:
    """
    params_list = []
    workbook = xlrd.open_workbook(filename)
    data_sheet = workbook.sheets()[sheetid]  # sheet 1
    row_num = data_sheet.nrows  # row num
    print('row_num' + str(row_num))
    data_key = data_sheet.row_values(0)  # row 1  params : key

    if rownum > row_num:
        print('client数量大于excel实际数量')
    else:
        # params: value
        line_num = 1
        while line_num <= rownum:
            data_value = data_sheet.row_values(line_num)  # row 2
            params_dict = dict(zip(data_key, data_value))
            params_list.append(params_dict)
            # print('paramse_dict:' + str(params_dict))
            line_num += 1
    return params_list






if __name__ == '__main__':
    # excel_create(path=save_path)
    text = excel_read(excel_path, 0, 2)
    print(text[0])