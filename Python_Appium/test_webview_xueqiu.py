from time import sleep

from appium import webdriver


class TestWebViewXueQiu():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            "chromedriverExecutable": "C:/Users/Administrator/Desktop/chromedriver52.exe"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_xueqiuweb(self):
        self.driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']").click()
        print(self.driver.contexts)

        self.driver.find_element_by_xpath("//android.view.View[@content-desc='A股开户']").click()
        sleep(3)
        print(self.driver.contexts)

        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element_by_id('phone-number').send_keys('15986612345')
        self.driver.find_element_by_id('code').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@class="btn-submit"]').click()
