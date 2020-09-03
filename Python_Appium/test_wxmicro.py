from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWXMicro:
    def setup(self):
        """
        微信小程序自动化关键：
        1.设置正确的chromedriver版本；
        2.设置chrome option传递给chromedriver
        3.使用adb proxy解决fix chromedriver的bug
          adb proxy:使用代理技术解决了chromedriver和微信定制的chrome内核之间的调试问题，可以用于微信小程序的自动化测试。
          [shell mock技术
                用于欺骗adb和appium，选择合适的chromedriver版本。个人使用可以先简单使用chromedriverExecutable代替]
        :return:
        """
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.mm",
            "appActivity": "com.tencent.mm.ui.LauncherUI",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "unicodeKeyBoard": True,
            "dontStopAppOnReset": True,
            "resetKeyBoard": True,
            "chromedriverExecutable": "C:/Users/Administrator/Desktop/chromedriver52.exe",
            "chromeOptions": {'androidProcess': 'com.tencent.mm:appbrand0'},  # 将小程序的进程名写入
            "adbport": 5038  # 通过使用adb proxy中的5038端口，fix chromedriver的bug,并且转至默认的5037端口
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass

    def test_wxmicro(self):
        # size = self.driver.get_window_size()
        # self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width'] * 0.5, size['height'] * 0.8)
        # action = TouchAction(self.driver)
        # action.press(x=400, y=600).wait(300).move_to(x=400, y=1200).release().perform()
        self.driver.find_element_by_id('com.tencent.mm:id/f8y').click()
        self.driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys('雪球')
        self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tencent.mm:id/gbv' and "
                                          "@text='雪球']").click()
        print(self.driver.contexts)
        # 进入WebView
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.implicitly_wait(10)
        self.find_top_window()
        self.driver.find_element_by_xpath('//*[@class="_div data-v-5667385e input"]').click()
        WebDriverWait(self.driver,20).until(lambda x:len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, '._input').click()

        self.driver.switch_to.context('NATIVE_APP')
        ActionChains(self.driver).send_keys('alibaba').perform()
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='阿里巴巴']").click()

    def find_top_window(self):
        """
        查找顶层可见的窗口（非后台运行的），即当前操作的窗口，用于操作前后的窗口切换
        :param driver:
        :return:
        """
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)
