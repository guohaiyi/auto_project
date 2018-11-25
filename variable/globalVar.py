# -*- coding: UTF-8 -*-

dcit = {}
dcit['aa'] = 'rrrr'
print(dcit)


class SetGlobalVar:
    def __init__(self):
        global global_dict
        global_dict = {}

    def set_value(self, key, value):
        global_dict[key] = value
        return global_dict

    def get_tenant_token(self):
        tenant_token = global_dict['tenant_token']
        return tenant_token

if __name__ == "__main__":
    a = SetGlobalVar()
    #q = a.set_value("tenant_token", "ssd")
    s = a.get_tenant_token()
    #print(q)
    print(s)