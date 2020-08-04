from selenium.webdriver.chrome.webdriver import WebDriver


class Register:
    """
    注册页面PO
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element_by_id('corp_name').send_keys('霍格沃兹学院')
        self.driver.find_element_by_id('manager_name').send_keys('Hugo')
        return True
