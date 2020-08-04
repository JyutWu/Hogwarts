import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookies:

    def setup(self):
        chrome_options = Options()
        chrome_options.debugger_address = '127.0.0.1:8888'
        self.driver = webdriver.Chrome(options=chrome_options)

    def teardown(self):
        pass

    def test_save_cookies(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        print(self.driver.get_cookies())
        db = shelve.open('cookies')
        db['cookies'] = self.driver.get_cookies()
        db.close()
