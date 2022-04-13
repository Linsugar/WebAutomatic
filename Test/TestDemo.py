# import configparser
# import os
#
#
# class ConfigParams(object):
#     curPath = os.path.pardir
#     Path = os.path.join(curPath, r"Conf\Conf.ini")
#
#     def __init__(self):
#         self.Config = configparser.ConfigParser()
#         self.Config.read(self.Path, encoding="utf-8")
#
#     def MysqlParams(self):
#         # 对MySql进行配置读取
#         prot = self.Config["MySql"]["port"]
#         user = self.Config["MySql"]["user"]
#         pwd = self.Config["MySql"]["pwd"]
#         addr = self.Config["MySql"]["addr"]
#         print("prot=%s,user=%s,pwd=%s,addr=%s"%(prot,user,pwd,addr),)
#         return prot,user,pwd,addr
#
#     def RedisParams(self):
#         #对redis进行配置读取
#         addr = self.Config["Redis"]["addr"]
#         print("addr=%s"%(addr))
#         return addr
#
# if __name__ == '__main__':
#     Tes = ConfigParams()
#     Tes.MysqlParams()
#     Tes.RedisParams()

from Untils.LogFile import Logger

if __name__ == '__main__':
    va = Logger().logger
    va.info("dsadasdadad")

