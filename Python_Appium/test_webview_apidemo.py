from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWebViewAPI():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "io.appium.android.apis",
            "appActivity": "io.appium.android.apis.ApiDemos",
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

    def test_webview(self):
        self.driver.find_element_by_xpath('//*[@content-desc="Views"]').click()
        sleep(2)
        print(self.driver.contexts)  # 打印上下文
        webview = 'WebView'
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            f'scrollIntoView(new UiSelector().text("{webview}").instance(0))').click()
        # self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='i_am_a_textbox' and @text='i has "
        #                                   "no focus']").clear().send_keys('this is test string')
        # sleep(2)
        # self.driver.find_element_by_accessibility_id('i am a link').click()
        # print(self.driver.page_source)
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])  # 切换到webview进行后续操作，类似与selenium中切换frame
        self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').clear().send_keys('this is test string')
        self.driver.find_element(MobileBy.ID, 'i am a link').click()
        print(self.driver.page_source)
