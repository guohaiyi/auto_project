# -*- coding: UTF-8 -*-
from config.dataConfig import Get_Constant_xlsx
from dataUtil.operationExcel_openpyxl import OperationExcel
from dataUtil.operationJson import OperationJson


class GetData:

    def __init__(self):
        self.operation_excel = OperationExcel()
        self.get_cons = Get_Constant_xlsx()

    # 获取Excel行数，即Case的个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取Case是否执行
    def get_is_run(self, row):
        flag = None
        cell_name = self.get_cons.to_is_run()
        run_model = self.operation_excel.get_cell_value(cell_name, row)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    # 获取测试用例编号
    def get_case_id(self, row):
        cell_name = self.get_cons.to_case_id()
        case_id = self.operation_excel.get_cell_value(cell_name, row)
        return case_id

    # 获取测试用例标题
    def get_case_title(self, row):
        cell_name = self.get_cons.to_case_title()
        title = self.operation_excel.get_cell_value(cell_name, row)
        return title

    # 获取url
    def get_request_url(self, row):
        cell_name = self.get_cons.to_url()
        url = self.operation_excel.get_cell_value(cell_name, row)
        return url

    # 获取header
    def get_request_header(self, row, token=None):
        cell_name = self.get_cons.to_header()
        request_header = self.operation_excel.get_cell_value(cell_name, row)
        # print(request_header)
        if request_header == 'yes':
            return self.get_cons.to_header_value(token)
        else:
            None

    # 获取请求方式
    def get_request_method(self, row):
        cell_name = self.get_cons.to_request_way()
        request_method = self.operation_excel.get_cell_value(cell_name, row)
        return request_method

    # 获取请求数据
    def get_request_data(self, row):
        #request_data = None
        cell_name = self.get_cons.to_request_data()
        data = self.operation_excel.get_cell_value(cell_name, row)
        if data == None:
            request_data = None
        else:
            request_data = self.get_data_for_json(row)
        return request_data

    # 通过关键字获取请求json数据
    def get_data_for_json(self, row):
        operation_json = OperationJson()
        cell_name = self.get_cons.to_request_data()
        key = self.operation_excel.get_cell_value(cell_name, row)
        request_json_data = operation_json.get_data(key)
        return request_json_data

    # 获取预期结果
    def get_expect_result(self, row):
        cell_name = self.get_cons.to_expect_result()
        expect = self.operation_excel.get_cell_value(cell_name, row)
        return expect

    # 获取是否有依赖
    def get_is_depend(self, row):
        cell_name = self.get_cons.to_is_depend()
        is_depend = self.operation_excel.get_cell_value(cell_name, row)
        if is_depend == "yes":
            # return self.get_request_depend_field(row)
            return True
        else:
            return False

    # 获依赖case_id
    def get_depend_Case_id(self, row):
        cell_name = self.get_cons.to_depend_case_id()
        case_depend = self.operation_excel.get_cell_value(cell_name, row)
        return case_depend

    # 获依赖的返回数据key
    def get_depend_return_data_key(self, row):
        cell_name = self.get_cons.to_depend_data()
        data_key = self.operation_excel.get_cell_value(cell_name, row)
        if data_key == None:
            return None
        else:
            return data_key

    # 获数据请求依赖字段
    def get_request_depend_field(self, row):
        cell_name = self.get_cons.to_data_depend_field()
        depend_field = self.operation_excel.get_cell_value(cell_name, row)
        return depend_field

    # 写入实际结果数据
    def write_data_actual(self, row, wr_value):
        cell_name = self.get_cons.to_actual_results()
        wr_data = self.operation_excel.write_result(cell_name, row, wr_value)
        if wr_data == None:
            return True

    # 写入运行结果数据
    def write_data_run(self, row, wr_value):
        cell_name = self.get_cons.to_run_results()
        wr_data = self.operation_excel.write_result(cell_name, row, wr_value)
        if wr_data == None:
            return True

    # 写入运行运行环境数据
    def write_run_env(self, row, wr_value):
        cell_name = self.get_cons.to_is_run()
        wr_data = self.operation_excel.write_result(cell_name, row, wr_value)
        if wr_data == None:
            return True


if __name__ == "__main__":
    getRequest = GetData()
    a = getRequest.get_is_depend(7)
    print(a)