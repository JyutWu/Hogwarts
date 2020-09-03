import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import close_to
from hamcrest.core import assert_that


class TestParam():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": True,  # 保留上次操作痕迹（比如登录状态）
            "skipServerInstallation": True,
            "dontStopAppOnReset": True,
            "unicodeKeyBoard": True,
            "resetKeyBoard": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    # @pytest.mark.parametrize('searchkeys,type,price', (
    #         ['alibaba', 'BABA', 260],
    #         ['xiaomi', '01810', 20]
    # ))
    @pytest.mark.parametrize('searchkeys,type,price', yaml.safe_load(open('./searchdata.yaml')))
    def testParam(self, searchkeys, type, price):
        """
        1.打开雪球应用
        2.点击搜索框
        3.输入搜索词 'alibaba' or 'xiaomi'
        4.点击第一个搜索结果
        5.判断 股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(searchkeys)
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        current_prise = float(self.driver.find_element(MobileBy.XPATH, f'//*[@text="{type}"]/..//../..//*['
                                                                       '@resource-id="com.xueqiu.android:id'
                                                                       '/current_price"]').text)

        assert_that(current_prise, close_to(price, price * 0.1))
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/action_close').click()
