"""
Hamcrest断言
Hamcrest是一个为了测试为目的，能组合成灵活表达式的匹配器类库。用于编写
断言的框架，使用这个框架编写断言，提高可读性及开发测试的效率
Hamcrest提供了大量被称为"匹配器"的方法。每个匹配器都设计用于执行特定的
比较操作。
Hamcrest的可扩展性强，让你能够创建自定义的匹配器。

"""
from appium import webdriver
from hamcrest import *


class TestGetAttribute:
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
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_getattr(self):
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))  # 返回元素左上角和右下角的坐标

    def test_hamcrest(self):
        # assert_that(10, equal_to(9),'这是一个提示')
        # assert_that(13, close_to(10, 2))  # 判断 8 是否在以10为基准，浮动为2的范围内
        assert_that('contains for string', contains_string('string')) #是否包含某个字符串
