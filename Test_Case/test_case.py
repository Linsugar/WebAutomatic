# encoding: utf-8
"""
  @author: 糖糖 
  @contact: 自我驱动@gmail.com
  @file: test_case.py
  @time: 2022/4/16 21:32
  @desc:开始你的骚操作
"""
import allure


@allure.epic("TestMain一级目录")
@allure.title("一级目录")
class TestMain:

    @allure.feature("关于测试第一条")
    @allure.title("第一条")
    def test_t1(self):
        print(1)

    @allure.feature("关于测试第二条")
    def test_t2(self):
        print(2)

    @allure.feature("关于测试第三条")
    def test_t3(self):
        print(3)
