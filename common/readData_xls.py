# -*- coding: UTF-8 -*-
from common.dataConfig import Get_Constant_xls
from dataUtil.operationExcel import OperationExcel
from dataUtil.operationJson import OperationJson

class GetData:

    def __init__(self):
        self.operation_excel = OperationExcel()
        self.get_cons = Get_Constant_xls()

    # 获取Excel行数，即Case的个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取Case是否执行
    def get_is_run(self, row):
        flag = None
        column = int(self.get_cons.to_run())
        run_model = self.operation_excel.get_cell_value(row, column)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取url
    def get_request_url(self, row):
        column = int(self.get_cons.to_url())
        url = self.operation_excel.get_cell_value(row, column)
        return url

    # 获取header
    def get_request_header(self, row):
        column = int(self.get_cons.to_header())
        request_header = self.operation_excel.get_cell_value(row, column)
        # print(request_header)
        if request_header == 'yes':
            return self.get_cons.to_header_value()
        else:
            None

    # 获取请求方式
    def get_request_method(self, row):
        column = int(self.get_cons.to_request_way())
        request_method = self.operation_excel.get_cell_value(row, column)
        return request_method

    # 获取请求数据
    def get_request_data(self, row):
        column = int(self.get_cons.to_request_data())
        data = self.operation_excel.get_cell_value(row, column)
        if data == '':
            return None
        return data

    # 通过关键字获取请求json数据
    def get_data_for_json(self, row):
        operation_json = OperationJson()
        column = int(self.get_cons.to_request_data())
        key = self.operation_excel.get_cell_value(row, column)
        request_data = operation_json.get_data(key)
        return request_data

    # 获取预期结果
    def get_expect_result(self, row):
        column = int(self.get_cons.to_expect_result())
        expect = self.operation_excel.get_cell_value(row, column)
        return expect


if __name__ == "__main__":
    getRequest = GetData()
    qa = getRequest.get_expect_result(1)
    print(qa)