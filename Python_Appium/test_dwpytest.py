import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestXueQiuDW:
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
        self.driver.quit()

    def test_search(self):
        """
        2.打开雪球app
        2．点击搜索输入框
        3·向搜索输入框里面输入"阿里巴巴"
        4·在搜索结果里面选择“阿里巴巴“，然后进行点击
        5．获这只香港阿里巴巴的股价，并判断这只股价的价格>200

        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴-SW"]') \
            .click()
        valuation = float(self.driver.find_element_by_id('com.xueqiu.android:id/stock_current_price').text)
        print(valuation)
        assert valuation > 200

        # self.driver.back()

    def test_attribute(self):
        """
        打开{雪球]应用首页
        定位首页的搜索框
        判断搜索框的是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断〖阿里巴巴〗是否可见
        如果可见，打印“搜索成功“点击，如果不可见，打印“搜索失败“

        :return:
        """
        search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enable = search.is_enabled()
        print(search.get_attribute('name'))
        print(search.location)
        print(search.size)
        if search_enable:
            search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_displayed = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and '
                                                                  '@text="阿里巴巴"]').get_attribute('displayed')
            print(alibaba_displayed)
            if alibaba_displayed:
                print('搜索成功')
            else:
                print('搜索失败')
        else:
            print('搜索框不可见')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_prise = float(self.driver.find_element_by_xpath(
            '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        print(f'当前09988对应的股票价格是：{current_prise}')
        assert current_prise < 200

    def test_myinfo(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入到登录页面
        3.输入用户名，密码
        4.点击登录
        :return:
        """
        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='我的']").click()
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='帐号密码登录']").click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/login_account").send_keys('15986609110')
        # self.driver.find_element_by_id('com.xueqiu.android:id/login_password').send_keys('63452010')
        # self.driver.find_element_by_id('com.xueqiu.android:id/button_next')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        my = 'resourceId("com.xueqiu.android:id/tab_name").text("我的")'
        self.driver.find_element_by_android_uiautomator(my).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/login_account")').send_keys(
            '15986609110')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/login_password")').send_keys(
            '63452010')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.xueqiu.android:id/button_next")').click()
        tips = self.driver.find_element_by_id('com.xueqiu.android:id/md_content').text
        print(tips)
        assert tips == '用户名或密码错误' or tips == '请求太频繁，请稍后再试'

    def test_scrollfind(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("热门")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView(new UiSelector().text("雪山精选").instance(0));')


if __name__ == '__main__':
    pytest.main()
