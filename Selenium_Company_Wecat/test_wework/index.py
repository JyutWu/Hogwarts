import shelve


from selenium.webdriver.common.by import By

from Selenium_Company_Wecat.test_wework.add_member import AddMember
from Selenium_Company_Wecat.test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_add_member(self):
        """
        点击添加成员
        :return:
        """
        self.find(By.XPATH, '//*[@class="index_service_cnt js_service_list"]/a[1]').click()
        return AddMember(self._driver)
