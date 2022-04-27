import json

import pytest

from Common.UseDirXpath import conf_path
from Controllers.ControllerData import CaseFile

import allure
from Untils.ParseData import parse_data_yaml
from Common.basepage import BasePage
from Common.Domethod import MethodDo

@allure.title("一级目录")
@allure.epic("TestCase一级目录")
class TestCase(object):
    def setup_class(self):
        print("setup_class：所有用例执行之前")
        self.do = MethodDo()
        self.dr = BasePage().dr


    # def teardown_class(self):
    #     print("teardown_class：所有用例执行之后")

    # def setup(self):
    #     print("setup：每个用例开始前都会执行")
    #     BasePage()
    #
    # def teardown(self):
    #     print("teardown：每个用例结束后都会执行")

    @pytest.mark.parametrize("case_data", parse_data_yaml(conf_path+'/Login.yaml'))
    def test_three(self, case_data):
        print("当前数据：" +str(case_data))
        if case_data['method'] == "value":
            print(1)
            self.do.method_input(case_data,dr=self.dr)
        elif case_data['method'] == "click":
            print(2)
            self.do.method_click(case_data,dr=self.dr)
        # MethodDo().method_common(case_data)
        print("正在执行测试类----test_three")

    #
    # def test_four(self):
    #     print("正在执行测试类----test_four")
    #     x = "hello"
    #     #hasattr  判断该对象是否有这个方法
    #     assert hasattr(x, 'hello')
    #


if __name__ == '__main__':
    # 针对该文件进行测试
    pytest.main(["-s", "test_main.py"])
