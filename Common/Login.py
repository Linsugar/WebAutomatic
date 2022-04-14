import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#
class Login(object):
    url = "https://www.baidu.com/"
    # driver_path = r"D:\tang\jiazu\venv\Scripts\chromedriver.exe"
    def __init__(self):
        """
         #开启默认后台运行
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # self.dr = webdriver.Chrome(options=option)
        """
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get(self.url)

        time.sleep(5)
        self.dr.find_element(By.XPATH, "/s_kw_wrap").send_keys("tang")
        time.sleep(5)
        value = self.dr.find_element(By.ID, "kw")
        # value = self.dr.title
        print(value.text)
        time.sleep(10)

    def __del__(self):
        time.sleep(10)
        self.dr.close()
if __name__ == '__main__':
    Login()