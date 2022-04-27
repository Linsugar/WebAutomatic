# -*- coding: utf-8 -*-
"""
@Time    : 2022/4/15 0015 16:29
@Author  : 糖糖
@File    : UseDirXpath.py
@desc: 这里主要是为了获取到每个模块的路径
"""
import os

# 获取根路径-准备进行匹配
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#报告路径
report_path = os.path.join(root_path, "report")

#获取日志路径
log_path = os.path.join(root_path, "log")

#获取case路径
case_path = os.path.join(root_path, "Datas")

#获取配置路径
conf_path = os.path.join(root_path, "Conf")

#获取page-yaml路径
yaml_path = os.path.join(root_path, "Pages")

#获取工具路径
untils_path = os.path.join(root_path, "Untils")

if __name__ == '__main__':
    print(root_path,report_path,log_path,case_path,conf_path,untils_path)