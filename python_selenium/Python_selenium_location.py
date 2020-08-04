"""
1.只查找一个元素的时候:可以使用find_element(),find_elements()
  find_element()会返回一个WebElement节点对象,但是没找到会报错,而find_elements()不会,之后返回一个空列表
2.查找多个元素的时候:只能用find_elements(),返回一个列表,列表里的元素全是WebElement节点对象
3.找到都是节点(标签)
4.如果想要获取相关内容(只对find_element()有效,列表对象没有这个属性)  使用  .text;
5.如果想要获取相关属性的值(如href对应的链接等,只对find_element()有效,列表对象没有这个属性):使用   .get_attribute("href")
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocation:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_localtion(self):
        self.driver.find_element(By.NAME, 'wd').send_keys("霍格沃兹学院")
        self.driver.find_element(By.ID, 'su').click()
