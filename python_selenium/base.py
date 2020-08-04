import os

from selenium import webdriver


class Base():
    def setup(self):
        #初始化一个参数，在终端运行的时候，最前面增加 browser=浏览器名称，即可实现多浏览器执行用例
        #如选择使用谷歌浏览器：browser=chrome pytest XXXX.py
        # browser = os.getenv()
        # if browser == 'firefox':
        #     self.driver=webdriver.Firefox()
        # elif browser == 'headless':
        #     self.driver = webdriver.phantomjs()
        # else :
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()