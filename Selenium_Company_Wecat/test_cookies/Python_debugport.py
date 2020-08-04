from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDebug():

    def setup(self):
        # 在命令窗口中执行chrome --remote-debugging-port=8888 ， 启动指定调试端口的浏览器，在代码中指定开放的端口，即可复用浏览器，不用重复打开新浏览器
        chrome_options = Options()
        chrome_options.debugger_address = '127.0.0.1:8888'
        self.driver = webdriver.Chrome(options=chrome_options)

    def teardown(self):
        self.driver.quit()

    def test_Debug(self):
        self.driver.get('http://www.baidu.com')

        self.driver.find_element_by_id('kw').send_keys('霍格沃兹测试学院')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.find_element_by_link_text('霍格沃兹测试学院 – 测试开发工程师的黄埔军校').click()
        sleep(3)

    def test_wework(self):
        self.driver.find_element_by_id('menu_contacts').click()
        print(self.driver.get_cookies())

