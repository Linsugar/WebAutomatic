# encoding: utf-8
"""
  @author: 糖糖 
  @contact: 自我驱动@gmail.com
  @file: RunApp.py
  @time: 2022/4/16 21:34
  @desc: 这里用于统一执行
"""
import pytest
import os
import time

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system("allure generate ./ReportData -o ./reports --clean")
