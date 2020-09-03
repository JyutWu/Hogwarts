import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "cn.kmob.screenfingermovelock",
            "appActivity": "com.samsung.ui.FlashActivity",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        # self.driver.find_element_by_id('cn.kmob.screenfingermovelock:id/setPatternLayout').click()
        action = TouchAction(self.driver)
        action.press(x=138, y=200).wait(300).move_to(x=400, y=200).wait(300).move_to(x=670, y=200).wait(300).move_to(
            x=670, y=460) \
            .wait(300).move_to(x=670, y=730).release().perform()


if __name__ == '__main__':
    pytest.main()
