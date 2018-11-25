# -*- coding: UTF-8 -*-
import requests
# from openpyxl import load_workbook
#
# file_name = 'Orc_TestCase_test.xlsx'
# wb = load_workbook(filename=file_name)
# ws = wb.active
#
# # 按照单元格的表示读取B3
# aa = ws['B3'].value
# ss = ws.max_row
# print(aa)
# print(ss)
#
# # 按照单元格坐标获取 (row=3, column=2)
# bb = ws.cell(row=3,column=2).value
# # ws.cell(row=3,column=2) = 'lllllllll'
# print(bb)
#
# # 全部行的遍历获取
# for row in ws.rows: #从第一行开始
#     for col in row:
#         print(col.value)
#
# for row in list(ws.rows)[0:1]: #从指定行获取
#     for col in row:
#         print(col.value)
#
# # 写入数据
# ws['B2'] = 'testqa'
#
# # 修改表名
# ws.title = "New Sheel"
#
# # 保存数据
# wb.save(filename=file_name)
#
# print('A'+str(1))

# for i in range(2, 5):
#     a = i
#     print(i)
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YmQ2YjEwNjQzY2M2ODQ0MjFlN2JkZDEiLCJhdWQiOiJQYW5lbCIsImlzcyI6IlBhbmVsIiwidGVuYW50IjoiaGFpeWl0ZW5hbnQiLCJpYXQiOjE1NDA3OTY2ODUsImV4cCI6MTU3MjM1NDI4NX0.xJvGCyyxdabwfbqOMiHb34lbQRjWXFdXw3SyoHsv7rU"}
url = "http://172.16.1.97:3002/user"
data = "enduser_qa"
#data.replace('"', '')
print(data)



# -*- coding: UTF-8 -*-
from common.httpCofing import RunMethod
from common.readData_xlsx import GetData
from common.compareResult import CompareResult
from readConfig import ReadConfig
import json

class RunTest:
    def __init__(self):
        self.method = RunMethod()
        self.data = GetData()
        self.com_result = CompareResult()
        self.config = ReadConfig()

    def start_on_run(self):
        res = None
        result = None
        rows_count = self.data.get_case_lines()
        run_host = self.config.get_http()
        if run_host:
            self.data.write_run_env(1, run_host)
        print("总共 %s 行" % (rows_count))
        print("总共 %s 个测试用例" % (rows_count - 2))
        print("测试结果：")
        for i in range(3, rows_count + 1):
            # print(i)
            global token
            is_run = self.data.get_is_run(i)
            request_method = self.data.get_request_method(i)
            url = str(run_host) + str(self.data.get_request_url(i))
            # url = run_host + self.data.get_request_url(i)
            data = self.data.get_request_data(i)
            expect_result = self.data.get_expect_result(i)
            if i == 3:
                header = self.data.get_request_header(i)
            else:
                header = self.data.get_request_header(i, token)
            if is_run == True:
                run_case_id = self.data.get_case_id(i)
                run_case_title = self.data.get_case_title(i)
                res = self.method.run_main(method=request_method, url=url, data=data, header=header)  # 参数顺序：method, url, data, header
                if i == 3:
                    dict_json = json.loads(res)  # 把json数据转换成字典对象
                    token = dict_json['tenant_admin_token']
                    global_dict['tenant_token'] = token
                    # print(token)
                if self.com_result.is_contain(res, expect_result):
                    print("编号%s（%s）: 测试通过" % (run_case_id, run_case_title))
                    self.data.write_data_actual(i, 'Pass')
                    self.data.write_data_run(i, res)
                else:
                    self.data.write_data_actual(i, 'Fail')
                    self.data.write_data_run(i, res)
                    print("编号%s（%s）: 测试失败" % (run_case_id, run_case_title))
            else:
                no_run_case_id = self.data.get_case_id(i)
                no_run_case_title = self.data.get_case_title(i)
                self.data.write_data_actual(i, 'NA')
                print("编号%s（%s）: 不需要执行" % (no_run_case_id, no_run_case_title))


if __name__ == "__main__":
    run = RunTest()
    run.start_on_run()
    print(run.tenant_token())
