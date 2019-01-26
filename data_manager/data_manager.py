# -*- coding: utf-8 -*-
# @Project : mcm
# @Author  : Jinglin Chen
# @File    : data_manager.py
# @Time    : 2019/1/25 16:44
# @IDE     : PyCharm

import re
import xlrd

from data_models import MCM_NFLIS_Data, ACS_5YR_DP02


def read_xlsx():
    """
    read xlsx to list
    :return: list, all the data of the xlsx
    """
    workbook = xlrd.open_workbook('../datasets/MCM_NFLIS_Data.xlsx')
    booksheet = workbook.sheet_by_name('Data')
    data_list = list()
    for row in range(1, booksheet.nrows):
        row_data = list()
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            try:
                val = cel.value
                val = re.sub(r'\s+', '', val)
            except:
                pass
            if type(val) == float:
                val = int(val)
            else:
                val = str(val)
            row_data.append(val)
        data = MCM_NFLIS_Data(row_data)
        data_list.append(data)
    print(data_list[0].State)
    return data_list


def read_csv(year):
    """
       read csv
       :param: {String}year: the year of the file
       :param: {String}pattern:
       :return: {list}list: the data of the csv
    """
    file_path = '../datasets/ACS_' + str(year) + '_5YR_DP02_with_ann.csv'
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    data_list = list()
    row = []  # 定义行数组
    for line in lines:
        row.append(line.split(','))
    row[0][2] = "COUNTY"
    row[0].insert(3, "State")
    # print(row[0])
    for i in range(2, len(row)):
        row[i][2] = re.sub("County", "", row[i][2])
        row[i][2] = re.sub("\"", "", row[i][2])
        row[i][3] = re.sub("\"", "", row[i][3])
        # print(i)
        temp_data = ACS_5YR_DP02(row[0], row[i])
        data_list.append(temp_data)
    # print(data_list[0].COUNTY)
    return data_list


if __name__ == "__main__":
    read_xlsx()
