# -*- coding: UTF-8 -*-
import json
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
jsonPath = os.path.join(proDir, "../testData/data.json")


class OperationJson:

    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = jsonPath
        self.data = self.read_data()

    # 读取JSON文件
    def read_data(self):
        with open(self.file_name, 'r') as fp:
            data = json.load(fp)
            return data

    # # 写入JSON文件
    # def write_data(self):
    #     with open(self.file_name, 'w') as fp:
    #         data = json.load(fp)
    #         return data

    # 根据关键字获取JSON数据
    def get_data(self, key):
        data = self.read_data()[key]
        return data


if __name__ == "__main__":
    jsonPath1 = os.path.join(proDir, "../testData/data.json")
    #file_name = "../testData/token.json"
    oper = OperationJson(jsonPath1)
    #oper = OperationJson()
    s = oper.get_data("orc_login")
    print(s)
