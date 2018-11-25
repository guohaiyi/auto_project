# -*- coding: UTF-8 -*-
import requests
import json


class RunMethod:

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header).json()
        else:
            res = requests.get(url=url, params=data).json()
        return res

    def post_main(self, url, data, header=None):
        res = None
        data = json.dumps(data)
        if header != None:
            res = requests.post(url=url, data=data, headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def delete_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.delete(url=url, params=data, headers=header).json()
        else:
            res = requests.delete(url=url, params=data).json()
        return res

    # def delete_main(self, url, data=None, header=None):
    #     res = None
    #     data = str(data)
    #     if header != None:
    #         res = requests.delete(url=url, headers=headers).json()
    #         # res = requests.delete(url=url + '/' + data, headers=header).json()
    #         # print(data)
    #         # print(url + '/' + data)
    #     else:
    #         res = requests.delete(url=url).json()
    #         # res = requests.delete(url=url + '/' + data).json()
    #     return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        else:
            res = self.delete_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=False, indent=2)


if __name__ == "__main__":
    met = RunMethod()
    # POST示例
    # url = 'http://192.168.1.188:3002/orchestrator_admin/login'
    # header = {"Content-Type": "application/json"}
    # data = {
    #     "username": "orc_admin",
    #     "password": "orc_admin"
    # }
    # res = met.run_main('post', url, data, header)
    # dict_json = json.loads(res)  # 把json数据转换成字典对象
    # token = dict_json
    # print(token)

    # GET示例
    _id = "5bf9290d750678077e269623"
    url1 = 'http://192.168.1.188:3002/tenant_admin/' + _id
    header = {"Content-Type": "application/json", "Authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJvcmNfYWRtaW4iLCJhdWQiOiJQYW5lbCIsImlzcyI6IlBhbmVsIiwiaWF0IjoxNTQzMDU4NTQ4fQ.qKvLZNnLrlW7E63f_nDoN1DtawgXJtH3fc1WJ8_TtRo"}
    data1 = None
    res1 = met.run_main('get', url1, data1, header)
    print(res1)
