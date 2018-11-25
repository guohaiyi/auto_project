# -*- coding: UTF-8 -*-
import requests






url = self.ipPort + "/tenant_admin/login"
print(url)
header = {"Content-Type": "application/json"}
data = {
    "username": "haiyi",
    "password": "123456",
    "tenant_name": "haiyitenant"
}