
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from Selenium_Company_Wecat.test_wework_login.register import Register


class Login:
    """
    登录PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        点击企业注册
        进入到注册PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
