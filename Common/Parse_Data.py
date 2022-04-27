# encoding: utf-8
"""
  @author: 糖糖 
  @contact: 自我驱动@gmail.com
  @file: Parse_Data.py
  @time: 2022/4/16 21:19
  @desc:这里主要用于来解析yaml格式的数据-便于管理
"""

import yaml
import UseDirXpath
from Untils.LogFile import Logger

log = Logger().logger


def read_yaml(name: str = None):
    with open(name, mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        log.info("从哪个文件{0}，获取到的数据内容是{1}".format(UseDirXpath.conf_path + name, value))
        return value


def write_yaml(name: str = None, data: dict = None):
    with open(UseDirXpath.conf_path + name, mode="w") as f:
        log.info("写入数据到：{0}文件，写入的数据内容：{1},数据格式是：{2}".format(UseDirXpath.conf_path + name, data, type(data)))
        yaml.dump(f, data, yaml.FullLoader)


def clear_yaml(name: str = None):
    with open(UseDirXpath.conf_path + name, mode="w") as f:
        f.truncate()


if __name__ == '__main__':
    read_yaml(UseDirXpath.yaml_path+r"\HomePage\home.yaml")
