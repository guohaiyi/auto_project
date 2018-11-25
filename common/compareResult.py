# -*- coding: UTF-8 -*-
class CompareResult:

    def is_contain(self, str_one, str_two):
        '''
        判断一个字符串是否包含另外一个字符串
        str_one: 实际结果
        str_two: 预期结果
        :return:
        '''
        flag = None
        if str_two in str_one:
            flag = True
        else:
            flag = False
        return flag

if __name__ == "__main__":
    a = CompareResult()
    str_one = "haiyitenant"
    str_two = "haiyi"
    b = a.is_contain(str_one, str_two)
    print(b)