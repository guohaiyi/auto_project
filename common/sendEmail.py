# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

email_host = "smtp.163.com"

send_user = "omgtest_haiyi"
send_user_pw = "omgtest789"
send_user_em = "omgtest_haiyi@163.com"


# send_user = "18270721318"
# send_user_pw = "hai945yi"
# send_user_em = "18270721318@163.com"


# user_list = ["1250933942@qq.com"]
# title = "测试邮件"
# content = "这个是测试内容"


class SendEmail:
    def __init__(self):
        self.email_host = email_host  # 邮箱服务器
        self.send_user = send_user  # 发件人用户名
        self.send_user_pw = send_user_pw  # 发件人邮箱授权码，非登录密码
        self.send_user_em = send_user_em  # 发件人邮箱

    def send_email(self, user_list, title, content):
        message = MIMEText(content, 'plain', 'utf-8')  # 内容，格式，编码
        message['From'] = "{}".format(self.send_user_em)  # 发件人
        message['To'] = ",".join(user_list)  # 收件人
        message['Subject'] = title  # 标题

        try:
            server = smtplib.SMTP_SSL(self.email_host, 465)  # 启用SMTP发信
            server.login(self.send_user, self.send_user_pw)  # 登录验证
            server.sendmail(self.send_user_em, user_list, message.as_string())  # 发送
            server.quit()  # 关闭
            print("邮件发送成功！")
        except smtplib.SMTPException as e:
            print("邮件发送失败！")
            print(e)

    def start_send(self, pass_list, fail_list):
        pass_number = float(len(pass_list))
        fail_number = float(len(fail_list))
        total_number = pass_number + fail_number
        pass_rate = "%.2f%%" % (pass_number / total_number * 100)
        fail_rate = "%.2f%%" % (fail_number / total_number * 100)
        print("通过率：", pass_rate)
        print("失败率：", fail_rate)

        user_list = ["omgtest_haiyi@163.com", "18270721318@163.com", "496527978@qq.com"]
        title = "接口测试报告"
        content = "此次测试一共运行了%s个测试用例，通过个数：%s个，失败个数：%s个；通过率为：%s，失败率为：%s" % (
            int(total_number), int(pass_number), int(fail_number), pass_rate, fail_rate)
        self.send_email(user_list, title, content)


if __name__ == "__main__":
    s = SendEmail()
    s.start_send([1, 2, 3], [4, 5, 6, 7, 8, 9])
