"""
TouchActions:模拟PC端和移动端的点击，滑动，拖拽，多点触控等多种手势操作
tap:在指定元素上敲击
double-tap:在指定元素上双敲击
tap-and_hold:在指定元素上点击不释放
move:手势移动指定偏移（未释放）
release:释放手势
scroll:手势点击并滚动
scroll-from-element:从某个元素位置开始手势点击并滚动（向下滑动为负数，向上滑动为正数〕
long-press:长按元素
flick:手势滑动
flick-element:从某个元素位置开始手势滑动（向上滑动为负数，向下滑动为正数）
Perform:执行
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchActions():

    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        pass

    def test_Touch(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('selenium 测试')
        sleep(2)
        ele = self.driver.find_element(By.XPATH, '//*[@id="su"]')
        action = TouchActions(self.driver)
        action.tap(ele)
        action.perform()
        sleep(3)

        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, '.n').click()
