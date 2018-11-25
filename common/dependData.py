# -*- coding: UTF-8 -*-
from common.readDepend_data import GetDependData
from common.readData_xlsx import GetData
from config.readConfig import ReadConfig
from common.httpCofing import RunMethod
from jsonpath_rw import jsonpath, parse
import json


class DependData:
    def __init__(self):
        self.get_dep_data = GetDependData()
        self.data = GetData()
        self.config = ReadConfig()
        self.run_method = RunMethod()

    # 执行依赖测试，获取结果
    def run_depedn_test(self, case_id):
        run_host = self.config.get_http()
        row = self.get_dep_data.in_case_id_get_depend_Case_id_lines(case_id)
        request_method = self.data.get_request_method(row)
        url = str(run_host) + str(self.data.get_request_url(row))
        data = self.data.get_request_data(row)
        header = self.data.get_request_header(row, self.config.get_orc_token())
        ress = self.run_method.run_main(method=request_method, url=url, data=data, header=header)
        return ress

    # 根据依赖的key获取执行依赖case的响应数据，然后返回
    def get_data_in_key(self, row, case_id):
        depent_key = self.data.get_depend_return_data_key(row)
        # print(depent_key)
        res_depent_data = self.run_depedn_test(case_id)
        dict_json = json.loads(res_depent_data)
        json_exe = parse(depent_key)
        madle = json_exe.find(dict_json)
        depent_data = [match.value for match in madle][0]
        return depent_data


if __name__ == "__main__":
    a = DependData()
    s = a.get_data_in_key(8, "DEV-006")
    print(s)
