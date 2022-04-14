import configparser
import os
from Untils.LogFile import Logger

class ConfigParams():
    curPath = os.path.pardir
    Path = os.path.join(curPath, r"Conf\Conf.ini")
    log = Logger().logger
    def __init__(self):
        self.Config = configparser.ConfigParser()
        self.Config.read(self.Path, encoding="utf-8")

    def MysqlParams(self):
        # 对MySql进行配置读取
        port = self.Config["MySql"]["port"]
        user = self.Config["MySql"]["user"]
        pwd = self.Config["MySql"]["pwd"]
        addr = self.Config["MySql"]["addr"]
        self.log.info("prot=%s,user=%s,pwd=%s,addr=%s"%(port,user,pwd,addr))
        return port,user,pwd,addr

    def RedisParams(self):
        #对redis进行配置读取
        addr = self.Config["Redis"]["addr"]
        self.log.info("addr=%s"%addr)
        return addr

    def Server(self):
        url = self.Config["Server"]["url"]
        self.log.info("url=%s"%url)
        return url
if __name__ == '__main__':
    Tes = ConfigParams()
    Tes.MysqlParams()
    Tes.RedisParams()
