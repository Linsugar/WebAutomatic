import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Controllers.ControllerConfig import ConfigParams


class Login(ConfigParams):
    # driver_path = r"D:\tang\jiazu\venv\Scripts\chromedriver.exe"
    def __init__(self):
        self.log.info("开始进行方法选择")
        super(Login, self).__init__()
        """
         #开启默认后台运行
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # self.dr = webdriver.Chrome(options=option)
        """
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get(self.Server())
        self.By = By
        #
        # element = WebDriverWait(self.dr, 10).until(
        #     EC.presence_of_element_located((By.ID, "kw")))
        # print(element)
        # element.send_keys("tang")
        # value = self.dr.find_element(By.ID, "su")
        # time.sleep(10)
        # # value = self.dr.title
        # print(value.text)

    def dr_return(self):
        """这里只为了返回一个dr驱动"""
        return self.dr

    def dr_close(self):
        """关闭窗口"""
        self.dr.close()

if __name__ == '__main__':
    Login()