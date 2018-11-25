# -*- coding: UTF-8 -*-
import xlrd
from xlutils.copy import copy
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
excelPath = os.path.join(proDir, "../testData/Orc_dev_TestCase_test.xlsx")


class OperationExcel:

    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = excelPath
        self.data = self.get_data()

    # 读取Excel表格
    def get_data(self):
        book = xlrd.open_workbook(self.file_name)
        tables = book.sheet_by_index(0)
        return tables

    # 获取单元格的行数
    def get_lines(self):
        line = self.data.nrows
        return line

    # 获取某一个单元格的内容
    def get_cell_value(self, row, column):
        value = self.data.cell(row, column).value
        return value

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

    # 写入数据
    def write_result(self):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, column, value)
        write_data.save(self.file_name)


if __name__ == "__main__":
    # file_name = '../testData/Orc_TestCase_test.xlsx'
    # oper = OperationExcel(file_name).get_data().nrows
    oper = OperationExcel().get_cols_data(1)
    print(oper)
