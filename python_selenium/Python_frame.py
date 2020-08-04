"""
在web自动化中，如果一个元素定位不到，那么很大可能是在 iframe 中。
什么是frame?
1.frame是html中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页而。
2.基于html的框架，又分为垂直框架和水平框架（cols，rows）
Frame分类
frame标签包含frameset、frame、iframe二种，
frameset和普通的标签一样，不会影响正常的定位，可以使用index、id、name、webelement任意种方式定位frame。
而frame与iframe对selenium定位而言是一样的。seienium有一组方法对frame进行操作

frame存在两种：
一种是嵌套的，一种是未嵌套的

切换frame：
driver.switch_to.frame()#根据元素id或者index(索引值)切换切换frame
driver.switch_to.default_content()#切换到默认frame
driver.switch_to.parent_frame()#切换到父级frame

"""
from time import sleep

from selenium.webdriver import ActionChains

from python_selenium.base import Base


class TestFrame(Base):

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        # self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)

        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id('submitBTN').text)

