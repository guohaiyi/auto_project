# coding=utf-8
import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self):
        value = self.cf.get("HTTP", "baseurl")
        return value

    def write_orc_token(self, orc_token):
        self.cf.set("TOKEN", "orc_token", orc_token)
        self.cf.write(open(configPath, 'w'))

    def get_orc_token(self):
        value = self.cf.get("TOKEN", "orc_token")
        return value


if __name__ == "__main__":
    a = ReadConfig()
    z = a.get_orc_token()
    print(z)
