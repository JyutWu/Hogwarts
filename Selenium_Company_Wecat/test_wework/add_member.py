from selenium.webdriver.common.by import By

from Selenium_Company_Wecat.test_wework.base_page import BasePage


class AddMember(BasePage):
    """
    添加成员操作页面
    """

    def add_member(self):
        """
        成员添加
        :return:
        """
        self.find(By.ID, 'username').send_keys('Hugo')
        self.find(By.ID, 'memberAdd_acctid').send_keys('63452010')
        self.find(By.ID, 'memberAdd_phone').send_keys('15986609111')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
