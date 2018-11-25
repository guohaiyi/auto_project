#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pymysql


class OperationDB:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "hai945yi", "auto_test")  # 打开数据库
        self.cursor = self.db.cursor()  # 使用cursor()方法创建一个游标对象cursor

    def get_db_data(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        self.db.close()
        return data


if __name__ == "__main__":
    sql = "SELECT * FROM demo"
    db = OperationDB()
    s = db.get_db_data(sql)
    print(s)
