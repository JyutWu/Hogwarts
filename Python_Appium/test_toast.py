from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.touchboarder.android.api.demos",
            "appActivity": "com.example.android.apis.view.PopupMenu1",
            # 使用【 adb shell dumpsys window|grep mCurrent 】获取模拟器当前应用页面的 appPackage和appActivity
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Make a Popup!"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()
        print(self.driver.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Search")]').text)
