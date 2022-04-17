# encoding: utf-8
"""
  @author: 糖糖 
  @contact: 自我驱动@gmail.com
  @file: conftest.py
  @time: 2022/4/16 21:39
  @desc:这里写一些pytest fixure 的一些固定装置
"""
import pytest


@pytest.fixture(scope="session", autouse=True)
def first_data():
    print("First_Data")


@pytest.fixture(scope="session", autouse=True)
def data():
    return [3, 2, 1, 5, -3, 2, 0, -2, 11, 9]
