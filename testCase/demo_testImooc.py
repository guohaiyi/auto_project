import unittest
from common import HTMLTestRunnerCN
from demo_common.demo_configHttp import RunMian
from readConfig import ReadConfig

# ipPort = ReadConfig().get_http()
# run = RunMian()
global tenant_token

class TestLogin(unittest.TestCase):

    def setUp(self):    # 初始测试环境
        self.run = RunMian()
        self.ipPort = ReadConfig().get_http()

    def tearDown(self): # 还原测试环境
        pass

    def test_login(self):
        '''Tenang Admin登录'''
        url = self.ipPort + "/tenant_admin/login"
        print(url)
        header = {"Content-Type": "application/json"}
        data = {
         "username": "haiyi",
         "password": "123456",
         "tenant_name": "haiyitenant"
        }
        res = self.run.run_main("POST", url, header, data)
        print(res)
        # globals()["tenant_token"] = res["tenant_admin_token"]
        s = res["tenant_admin_token"]
        print(s)
        self.assertEqual(res["username"], "haiyi", "测试不通过")
        # try:
        #     res = self.run.run_main("POST", url, header, data)
        #     globals()["tenant_token"] = res["tenant_admin_token"]
        #     print("返回的结果：", tenant_token)
        #     self.assertEqual(res["username"], "haiyi", "测试不通过")
        # except Exception as e:
        #     print("test_login出错了！%s"%e)

    @unittest.skip("test_profile")  # 跳过测试
    def test_profile(self):
        '''获取Profile列表'''
        url = self.ipPort + "/profile"
        header = {'Authorization': 'Bearer ' + tenant_token}
        data = {"limit": 1}
        try:
            res = self.run.run_main("GET", url, header, data)
            print("返回的结果：", res)
            globals()["profile_id"] = res["results"][0]["_id"]  #定义全局变量
            self.assertTrue(res["status"], "测试不通过")
        except Exception as e:
            print("test_profile出错了！%s"%e)

    @unittest.skip("test_profileInfo")  # 跳过测试
    def test_profileInfo(self):
        '''获取profile详细信息'''
        url = self.ipPort + "/profile/" + profile_id
        header = {'Authorization': 'Bearer ' + tenant_token}
        try:
            res = self.run.run_main("GET", url, header)
            print("返回的结果：", res)
            self.assertTrue(res["status"], "测试不通过")
            self.assertEqual(res["_id"], profile_id, "测试不通过")
            self.assertEqual(res["profile_name"], "qqqqqqq", "测试不通过")
        except Exception as e:
            print("test_profileInfo出错了！%s"%e)


if __name__ == "__main__":
    filepath = "../report/htmlreport.html"
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    suite.addTest(TestLogin("test_profile"))
    suite.addTest(TestLogin("test_profileInfo"))
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='testqa', tester='haiyi')
    runner.run(suite)
