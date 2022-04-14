from selenium.webdriver.support.wait import WebDriverWait
from Untils.LogFile import Logger
from Common.Login import Login


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

class MethodDo(Login):
    log = Logger().logger

    def __init__(self):
        super().__init__()
        self.log.info("开始进行方法选择")

    @staticmethod
    def select_method(value):
        value = str(value).lower()
        print(value)
        if value == "xapth":
            print("22")

    def method_xpath(self, value):
        return driver_wait(self.dr, self.By.XPATH, value)

    def method_id(self, value):
        return driver_wait(self.dr, self.By.ID, value)

    def method_name(self, value):
        return driver_wait(self.dr, self.By.NAME, value)

    def method_class(self, value):
        return driver_wait(self.dr, self.By.CLASS_NAME, value)

    @staticmethod
    def method_text(self, value):
        return driver_wait(self.dr, self.By.LINK_TEXT, value)

    def __del__(self):
        self.dr.quit()

def test():
    print(1)

if __name__ == '__main__':
    m = MethodDo()
    f = getattr(m, "method_xpath", None)
    f("xpath")
    #类似与improt MthodDo
    # imp = input("请输入模块:")
    # dd = __import__("test")  # 等价于import imp
    # # inp_func = input("请输入要执行的函数：")
    # f = getattr(MethodDo, "method_xpath", None)
    # print(f)
    # 作用:从导入模块中找到你需要调用的函数inp_func,然后
    # 返回一个该函数的引用.没有找到就烦会None
    # 执行该函数
