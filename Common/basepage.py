import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Controllers.ControllerConfig import ConfigParams
class BasePage(ConfigParams):
    # driver_path = r"D:\tang\jiazu\venv\Scripts\chromedriver.exe"
    dr: webdriver = None

    def __init__(self):
        self.log.info("开始进行方法选择")
        super(BasePage, self).__init__()
        """
         #开启默认后台运行
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        self.dr = webdriver.Chrome(options=option)
        """
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        self.dr = webdriver.Chrome(options=option)
        self.dr.get("http://city.osmagic.com/#/login")
        # self.dr.get(self.Server())
        # self.By = By
        # if self.dr is None:
            # self.dr = webdriver.Chrome()
        # element = WebDriverWait(self.dr, 10).until(
        #     EC.presence_of_element_located((By.ID, "kw")))
        # print(element)
        # element.send_keys("tang")
        # value = self.dr.find_element(By.ID, "su")
        # time.sleep(10)
        # # value = self.dr.title
        # print(value.text)
    def get_dr(self):
        return self.dr


if __name__ == '__main__':
    BasePage()
