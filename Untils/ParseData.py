# -*- coding: utf-8 -*-
'''
@Time    : 2022/4/15 0015 17:06
@Author  : 糖糖
@File    : ParseData.py

'''
import yaml
import json
from Untils.LogFile import Logger
log = Logger().logger

def parse_data_yaml(xpath: str = None):
    log.info("开始进行解析{0},值是={1}".format(type(xpath), xpath))
    if xpath:
        with open(xpath, "r")as f:
            data = yaml.load(f, yaml.FullLoader)
            log.info("解析完成{0}".format(data))
            return data
    else:
        log.info("解析失败")
        return None

def pares_data_json(data):
    log.info("开始进行解析{0},值是={1}".format(type(data), data))
    if isinstance(data, str):
        data = json.loads(data)
        log.info("解析完成{0}".format(data))
        return data
    elif isinstance(data, dict):
        data = json.dumps(data)
        log.info("解析完成{0}".format(data))
        return data
    else:
        log.info("解析失败")
        return None


if __name__ == '__main__':
    s = '["123","123"]'
    pares_data_json(s)