# -*- coding: UTF-8 -*-
from dataUtil.operationExcel_openpyxl import OperationExcel
from common.readData_xlsx import GetData
import xlrd
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
excelPath = os.path.join(proDir, "../testData/Orc_dev_TestCase_test.xlsx")


class GetDependData:
    def __init__(self):
        self.oper_excel = OperationExcel()
        self.data = GetData()
        self.file_name = excelPath

    # 获取依赖Case_id
    def get_depend_Case_id(self, row):
        depend_case_id = self.data.get_depend_Case_id(row)
        return depend_case_id

    # 根据Case_id获取行号
    def in_case_id_get_lines(self, case_id):
        num = 1
        col_data = self.get_column_data()
        for column_data in col_data:
            if case_id == column_data:
                return num
            num = num + 1

    # 根据列数，获取某一列的内容
    def get_column_data(self, column_id=None):
        book = xlrd.open_workbook(self.file_name)
        tables = book.sheet_by_index(0)
        if column_id != None:
            column_data = tables.col_values(column_id)
        else:
            column_data = tables.col_values(0)
        return column_data

    # 根据Case_id获取依赖Case的行号
    def in_case_id_get_depend_Case_id_lines(self, case_id):
        num = 1
        col_data = self.get_column_data()
        depend_Case_id = self.get_depend_Case_id(self.in_case_id_get_lines(case_id))
        for column_data in col_data:
            if depend_Case_id == column_data:
                return num
            num = num + 1

    # # 根据行号，获取某一行的内容
    # def get_row_data(self, row):
    #     book = xlrd.open_workbook(self.file_name)
    #     tables = book.sheet_by_index(0)
    #     row_data = tables.row_values(row - 1)
    #     return row_data
    #
    # # 根据Case_id获取对应行的内容
    # def in_case_id_get_data(self, case_id):
    #     row = self.in_case_id_get_lines(case_id)
    #     row_data = self.get_row_data(row)
    #     return row_data


if __name__ == "__main__":
    s = GetDependData()
    a = s.in_case_id_get_depend_Case_id_lines("DEV-006")
    print(a)
