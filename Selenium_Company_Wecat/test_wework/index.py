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
        self.find(By.CSS_SELECTOR, '#menu_contacts').click()

        def add_member_condition(x):
            # 判断“添加成员”的功能是否可以使用，即通过判断点击“添加成员”后，是否出现添加成员操作界面（用是否出现“姓名”输入框来判断）
            # 如果查找元素返回的列表内容为空，说明未出现添加成员操作界面，也说明点击“添加成员”功能未生效，则继续点击“添加成员”，直至成功便返回
            # True,传参给wait_for_condition结束显示等待方法，继续执行下一步
            element_len = len(self.finds(By.ID, 'username'))
            if element_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            else:
                return True

        # self.wait_for_click((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        self.wait_for_condition(add_member_condition)
        return AddMember(self._driver)
