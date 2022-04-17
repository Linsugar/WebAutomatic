import pytest
from Controllers.ControllerData import CaseFile

import allure


@allure.title("一级目录")
@allure.epic("TestCase一级目录")
class TestCase(object):
    # def setup_class(self):
    #     print("setup_class：所有用例执行之前")
    #
    # def teardown_class(self):
    #     print("teardown_class：所有用例执行之后")
    def setup(self):
        print("setup：每个用例开始前都会执行")

    def teardown(self):
        print("teardown：每个用例结束后都会执行")

    def test_three(self):
        value = CaseFile().read_sheet()
        print("得到反馈：" + str(value))


        print("正在执行测试类----test_three")
        x = "this"
        assert 'h' in x

    #
    # def test_four(self):
    #     print("正在执行测试类----test_four")
    #     x = "hello"
    #     #hasattr  判断该对象是否有这个方法
    #     assert hasattr(x, 'hello')

    def test_case(self):
        pass


if __name__ == '__main__':
    # 针对该文件进行测试
    pytest.main(["-s", "test_main.py"])
