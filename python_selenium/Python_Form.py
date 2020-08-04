"""
什么是表单？
 ※表单是一个包含表单元素的区域。
 ※表单元素是允许用户在表单中（比如：文本域、下拉列表、单选框、复选框等等）输入
信息的元素。
※表单使用表单标签（<form>）定义。例如：<form><input/></form>
操作表单元素步骤：
※首先要定位到表单元素,然后去操作元素（清空，输入或者点击等）

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        pass

    def test_formAction(self):
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys('123')
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('password')
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click()
        self.driver.find_element(By.CSS_SELECTOR, '#new_user > div.form-actions > input').click()
        sleep(3)
