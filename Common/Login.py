from selenium import  webdriver


class Login(object):
    url = "https://www.baidu.com/"

    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get(self.url)

    def __del__(self):
        self.dr.close()

if __name__ == '__main__':
    Login()