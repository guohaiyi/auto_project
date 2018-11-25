# -*- coding: UTF-8 -*-
class Get_Constant_xls:
    '''
    .xls 表格的常量参数
    '''

    def __init__(self):
        self.case_id = '0'
        self.url = '3'
        self.header = '4'
        self.request_way = '5'
        self.request_data = '6'
        self.expect_result = '7'
        self.actual_results = '8'
        self.run = '9'

    # 获取Case id在Excel表格所在的列数
    def to_case_id(self):
        return self.case_id

    # 获取url在Excel表格所在的列数
    def to_url(self):
        return self.url

    # 获取header在Excel表格所在的列数
    def to_header(self):
        return self.header

    # 获取请求方式在Excel表格所在的列数
    def to_request_way(self):
        return self.request_way

    # 获取请求数据在Excel表格所在的列数
    def to_request_data(self):
        return self.request_data

    # 获取预期结果在Excel表格所在的列数
    def to_expect_result(self):
        return self.expect_result

    # 获取实际结果在Excel表格所在的列数
    def to_actual_results(self):
        return self.actual_results

    # 获取是否执行在Excel表格所在的列数
    def to_run(self):
        return self.run

    # 获取header的值
    def to_header_value(self):
        header = {"Content-Type": "application/json"}
        return header


class Get_Constant_xlsx:
    '''
    .xlsx 表格的常量参数
    '''

    def __init__(self):
        self.case_id = 'A'
        self.run = 'B'
        self.title = 'C'
        self.condition = 'D'
        self.url = 'E'
        self.header = 'F'
        self.request_way = 'G'
        self.is_depend = 'H'
        self.depend_case_id = 'I'
        self.depend_data = 'J'
        self.depend_field = 'K'
        self.request_data = 'L'
        self.expect_result = 'M'
        self.actual_results = 'N'
        self.run_results = 'O'

    # 获取Case id在Excel表格所在的列数
    def to_case_id(self):
        return self.case_id

    # 获取是否执行在Excel表格所在的列数
    def to_is_run(self):
        return self.run

    # 获取Case title在Excel表格所在的列数
    def to_case_title(self):
        return self.title

    # 获取前提条件在Excel表格所在的列数
    def to_condition(self):
        return self.condition

    # 获取url在Excel表格所在的列数
    def to_url(self):
        return self.url

    # 获取header在Excel表格所在的列数
    def to_header(self):
        return self.header

    # 获取请求方式在Excel表格所在的列数
    def to_request_way(self):
        return self.request_way

    # 获取判断是否需要依赖在Excel表格所在的列数
    def to_is_depend(self):
        return self.is_depend

    # 获取依赖的case_id在Excel表格所在的列数
    def to_depend_case_id(self):
        return self.depend_case_id

    # 获取依赖的返回数据在Excel表格所在的列数
    def to_depend_data(self):
        return self.depend_data

    # 获取数据依赖字段在Excel表格所在的列数
    def to_data_depend_field(self):
        return self.depend_field

    # 获取请求数据在Excel表格所在的列数
    def to_request_data(self):
        return self.request_data

    # 获取预期结果在Excel表格所在的列数
    def to_expect_result(self):
        return self.expect_result

    # 获取实际结果在Excel表格所在的列数
    def to_actual_results(self):
        return self.actual_results

    # 获取运行结果在Excel表格所在的列数
    def to_run_results(self):
        return self.run_results

    # 获取header的值
    def to_header_value(self, token=None):
        header = None
        if token == None:
            header = {"Content-Type": "application/json"}
        else:
            header = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        return header

    # # 获取header的值
    # def to_header_value(self):
    #     file_name = "../testData/token.json"
    #     oper = OperationJson(file_name)
    #     header = oper.get_data("tenant_token")
    #     return header


if __name__ == "__main__":
    getCons = Get_Constant_xlsx()
    s = getCons.to_is_run()
    print(s)
