import configparser
import os
from Untils.LogFile import Logger
import json

class ConfigParams:
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
        self.log.info("prot={0},user={1},pwd={3},addr={3}".format(port, user, pwd, addr))
        return port, user, pwd, addr

    def RedisParams(self):
        #对redis进行配置读取
        redis_addr = self.Config["Redis"]["addr"]
        self.log.info("addr={0}".format(redis_addr))
        return redis_addr

    def Server(self):
        url = self.Config["Server"]["url"]
        self.log.info("url={0}".format(url))
        return url

    def Email(self):
        sender = self.Config["Email"]["sender"]
        receivers = json.loads(self.Config["Email"]["receivers"])
        email_host = self.Config["Email"]["mail_host"]
        email_user = self.Config["Email"]["mail_user"]
        email_pass = self.Config["Email"]["mail_pass"]
        self.log.info("邮件信息：sender:={0},receivers:={1} ".format(sender, receivers))
        return sender, receivers, email_host, email_user, email_pass

if __name__ == '__main__':
    ConfigParams().Email()
