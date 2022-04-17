from selenium.webdriver.support.wait import WebDriverWait
from Untils.LogFile import Logger
from Common.basepage import BasePage
import time

def driver_wait(dr, by, value):
    # log = Logger().logger
    #
    # try:
    #     element = WebDriverWait(dr, 10).until(lambda driver: dr.find_element(by, value))
    #     return element
    # except Exception as e:
    #     log.info(e)
    # finally:
    #     log.info("driver_wait结束")
    element = WebDriverWait(dr, 10).until(lambda driver: dr.find_element(by, value))
    return element


class MethodDo(BasePage):
    log = Logger().logger

    def __init__(self):
        super().__init__()
        self.log.info("开始进行方法选择")

    @staticmethod
    def select_method(value):
        value = str(value).lower()
        print(value)

    def method_common(self, loc):
        return self.dr.find_element(*loc)

    def method_input(self, loc, value):
        self.method_common(loc).send_keys(value)

    def method_click(self, loc):
        self.method_common(loc).click()

    def method_value(self, loc):
        res = self.method_common(loc).text
        return res

    def method_clear(self, loc):
        self.method_common(loc).clear()

    @staticmethod
    def method_wait(t: int = None):
        time.sleep(t)

def test():
    print(1)


if __name__ == '__main__':
    m = MethodDo()
    f = getattr(m, "method_xpath", None)
    f("xpath")
    # 类似与improt MthodDo
    # imp = input("请输入模块:")
    # dd = __import__("test")  # 等价于import imp
    # # inp_func = input("请输入要执行的函数：")
    # f = getattr(MethodDo, "method_xpath", None)
    # print(f)
    # 作用:从导入模块中找到你需要调用的函数inp_func,然后
    # 返回一个该函数的引用.没有找到就烦会None
    # 执行该函数
