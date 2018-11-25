import configparser

conf = configparser.ConfigParser()
conf.read('dbconf.ini')

conf.set("section1", "name", "5165161151")  # 修改指定section 的option
conf.set("section1", "age", "21")  # 增加指定section 的option
conf.add_section("section3")  # 增加section
conf.set("section3", "site", "oschina.net")  # 给新增的section 写入option
conf.write(open('dbconf.ini', 'w'))