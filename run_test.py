# -*- coding: UTF-8 -*-
from config.httpCofing import RunMethod
from config.readConfig import ReadConfig
from common.readData_xlsx import GetData
from common.compareResult import CompareResult
from common.dependData import DependData
from common.sendEmail import SendEmail
import json


class RunTest:
    def __init__(self):
        self.method = RunMethod()
        self.data = GetData()
        self.com_result = CompareResult()
        self.config = ReadConfig()
        self.depend = DependData()
        self.sendemail = SendEmail()

    def start_on_run(self):
        res = None
        result = None
        pass_num = []
        fail_num = []
        no_run_num = []
        rows_count = self.data.get_case_lines()
        run_host = self.config.get_http()
        if run_host:
            self.data.write_run_env(1, run_host)
        print("总共 %s 行" % (rows_count))
        print("总共 %s 个测试用例" % (rows_count - 2))
        print("测试结果：")
        for i in range(3, rows_count + 1):
            is_run = self.data.get_is_run(i)
            is_depend = self.data.get_is_depend(i)
            request_method = self.data.get_request_method(i)
            case_id = self.data.get_case_id(i)
            data = self.data.get_request_data(i)
            # print(case_id)
            # print("是否有依赖：%s"%is_depend)
            if is_depend:
                url = run_host + self.data.get_request_url(i) + self.depend.get_data_in_key(i, case_id)
                # print(url)
            else:
                url = run_host + self.data.get_request_url(i)
                # print(url)
            if i <= 4:
                header = self.data.get_request_header(i)
            else:
                header = self.data.get_request_header(i, self.config.get_orc_token())
            expect_result = self.data.get_expect_result(i)
            if is_run:
                run_case_id = self.data.get_case_id(i)
                run_case_title = self.data.get_case_title(i)
                res = self.method.run_main(method=request_method, url=url, data=data, header=header)
                # print("====>>>")
                # print(res)
                if i == 3:
                    dict_json = json.loads(res)  # 把json数据转换成字典对象
                    orc_token = dict_json['orchestrator_admin_token']
                    # print(dict_json)
                    self.config.write_orc_token(orc_token)
                    # print(orc_token)
                if self.com_result.is_contain(res, expect_result):
                    print("编号%s（%s）: 测试通过" % (run_case_id, run_case_title))
                    self.data.write_data_actual(i, 'Pass')
                    self.data.write_data_run(i, res)
                    pass_num.append(i)
                else:
                    print("编号%s（%s）: 测试不通过" % (run_case_id, run_case_title))
                    self.data.write_data_actual(i, 'Fail')
                    self.data.write_data_run(i, res)
                    fail_num.append(i)
            else:
                no_run_case_id = self.data.get_case_id(i)
                no_run_case_title = self.data.get_case_title(i)
                print("编号%s（%s）: 不需要执行" % (no_run_case_id, no_run_case_title))
                self.data.write_data_actual(i, 'NA')
                no_run_num.append(i)
        # 以邮件方式发送测试报告
        self.sendemail.start_send(pass_num, fail_num)


if __name__ == "__main__":
    run = RunTest()
    run.start_on_run()
