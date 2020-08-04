from selenium import webdriver
from selenium.webdriver.common.by import By

from Selenium_Company_Wecat.test_wework_login.login import Login
from Selenium_Company_Wecat.test_wework_login.register import Register


class Index:
    """
    首页PO
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_register(self):
        """
        点击立即注册
        进入到注册PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self.driver)
