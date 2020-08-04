import selenium
from selenium import webdriver
from time import sleep


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get('http://testerhome.com')

        self.driver.find_element_by_link_text('社团').click()

        self.driver.find_element_by_link_text('霍格沃兹测试学院').click()

        # self.driver.find_element_by_css_selector('topic-24883 .title > a').click()
