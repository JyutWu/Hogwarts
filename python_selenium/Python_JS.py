"""
使用selenium直接在当前页面中进行JS交互

Selenium能够执行js，这使得Seleniu拥有更为强大的能力。既然能执行js，
那么js能做的事，Selenium应该大部分也能做
1.直接使用js操作页面，能解决很多click()不生效的问题
2.页面滚动到底部，顶部
3.处理富文本，时间控件的输入


selenium中如何调用JS
execute_script:执行JS
return:可以返回JS的返回结果
execute_script:arguments 传参

处理时间控件：
大部分时间控件都是readonly属性，需要手动去选择对应的时间，手工测试中
很容易做到，自动化中对控件的操作可以使用js来操作。
处理时间控件思路：
1．要取消日期的readonly属性
2．给value赋值
3. 写js代码来实现如上的1，2点，再webdriver对js进行处理


"""
from time import sleep

from selenium.webdriver.common.by import By

from python_selenium.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        # self.driver.find_element_by_id('su').click()
        sleep(3)
        elemt = self.driver.execute_script('return document.getElementById("su")')  # 使用JS的形式定位元素
        elemt.click()
        sleep(3)
        self.driver.execute_script('document.documentElement.scrollTop=2000')
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#page > div > a.n').click()
        sleep(3)

        # 获取页面性能指标数据
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))

    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index/')
        # 用JS去掉readonly属性，然后直接输入日期文本
        self.driver.execute_script('a = document.getElementById("train_date");a.removeAttribute('
                                   '"readonly")')
        sleep(3)
        self.driver.execute_script('document.getElementById("train_date").value="2020-07-26"')
        sleep(3)

        print(self.driver.execute_script('return document.getElementById("train_date").value'))
