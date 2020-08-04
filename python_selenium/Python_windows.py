"""
多窗口处理：
    1.点击某些链接，会重新打开一个窗口，对于这种情况，想要在新页面上操作，就得先切换窗口。
    2.获取窗口的唯一标识用句柄表示，所有只需要切换句柄，就可以在多个页面上灵活操作了。

    操作流程：
    1．先获取到当前的窗口句柄（driver.current_window_handle）
    2. 再获取到所有的窗口句柄(driver.window-handles)
    3．判断是否是想要操作的窗口，如果是，就可以对窗口进行操作，如果不是，跳转到另外一个窗口，对另一个窗口进行操作(driver.switch_to_window)
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from python_selenium.base import Base


class TestWindows(Base):

    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.LINK_TEXT, '登录').click()
        sleep(3)
        print(self.driver.current_window_handle) #打印当前窗口句柄
        print(self.driver.window_handles)  # 打印所有窗口句柄
        self.driver.find_element_by_link_text('立即注册').click()
        print(self.driver.window_handles) #打印所有窗口句柄
        windows = self.driver.window_handles  #所有窗口句柄以列表形式保存，将句柄列表赋值给一个参数
        self.driver.switch_to_window(windows[-1]) #以切换窗口句柄方式切换窗口
        self.driver.find_element_by_name('userName').send_keys('username')
        sleep(3)
        self.driver.find_element_by_name('phone').send_keys('15986609110')
        sleep(3)
        self.driver.switch_to_window(windows[0])
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        sleep(3)
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)









