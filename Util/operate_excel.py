# coding=utf-8

import xlrd
from xlutils.copy import copy


# data = excel.sheets()[0]
# print(data.cell(3,4).value)
class operaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path == None:
            self.file_path = "..\case\case.xls"
        else:
            self.file_path = file_path
        if i == None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheet(i)

    def get_excel(self):
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheet(self, i):
        # 获取sheet
        table = self.excel.sheets()[i]
        return table

    def get_lines(self):
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        # 获取单元格内容
        data = self.data.cell(row, cell).value
        return data

    def write_value(self, row, value):
        read_value = self.data
        write_data = copy(read_value)
        write_save = write_data.get_sheet(0)
        write_save.write(row, 8, value)
        write_data.save(self.file_path)


