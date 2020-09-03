from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestDevices():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True,
            # "chromedriverExecutable": "C:/Users/Administrator/Desktop/chromedriver52.exe"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # self.driver.make_gsm_call('15986609110', GsmCallActions.CALL)  # 模拟来电
        # self.driver.send_sms('15986609111', '测试模拟来短信')  # 模拟来短信
        # self.driver.start_recording_screen()#开始录屏，仅支持部分机型和8.0以上的系统
        self.driver.set_network_connection(1)  # 切换网络环境
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)
        self.driver.get_screenshot_as_file('./photo/xueqiu.png')  # 屏幕截图
        # self.driver.stop_recording_screen()#结束录屏，仅支持部分机型和8.0以上的系统
