import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestWebDriverWait:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        locator = (MobileBy.XPATH, '//*[@text="09988"]/..//../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        current_prise = float(self.driver.find_element(*locator).text)
        expected_prise = 250
        print(f'当前09988对应的股票价格是：{current_prise}')
        # assert current_prise > 200
        assert_that(current_prise,close_to(expected_prise,expected_prise*0.1))


# if __name__ == '__main__':
#     pytest.main()
