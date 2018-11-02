# coding:utf-8
import os
import ConfigParser


cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "cfg.ini")
conf = ConfigParser.ConfigParser()
conf.read(configPath)

smtp_server = conf.get("email", "smtp_server")

sender = conf.get("email", "sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver")

port = conf.get("email", "port")

# class ReadConfig:
#     def __init__(self):
#         self.config=ConfigParser()
#         self.config.read('./cconfig.ini')
#
#     def get_server(self,name):
#         print (self.config.section)
#         # 读取配置文件
#         value=self.config.get("testServer",name)
#         return value
#
#     def get_dbserver(self,name):
#         # 读取配置文件
#         value = self.config.get("testServer", name)
#         return value




