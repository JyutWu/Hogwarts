from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "browserName": "Browser",
            "deviceName": "127.0.0.1:7555",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "chromedriverExecutable": "C:/Users/Administrator/Desktop/chromedriver52.exe"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        sleep(3)
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_bn=(By.ID,'index-bn')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(search_bn))
        self.driver.find_element(*search_bn).click()