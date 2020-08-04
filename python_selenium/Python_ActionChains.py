"""
WEB控件的交互操作
ActionChains:执行PC端的鼠标点击，双击，右键，拖拽等事件；
    常用的操作包括:
                1.send_keys_to_element(element,*keys_to_send)	向指定的元素发送键
                2.key_down(value,element=None)	只按下键盘，不释放
                3.key_up(value,element=None)	释放键
                4.click(on_element=None)	鼠标左键点击某元素
                5.click_and_hold(on_element=None)	鼠标左键点击一个元素并且保持
                6.double_click(on_element=None)	鼠标左键双击
                7.context_click(on_element=None)	点击鼠标右键， 在调用时需要指定元素定位
                8.drag_and_drop(source, target)	鼠标左键点击source元素，然后移动到target元素释放鼠标按键
                9.drag_and_drop_by_offset(source, xoffset,yoffset)	拖拽目标元素到指定的偏移点释放
                10.move_by_offset(xoffset,yoffset)	移动鼠标的位置
                11.move_to_element(to_element)	把鼠标移到一个元素的中间
                12.move_to_element_with_offset(to_element, xoffset, yoffset)  把鼠标移到一个元素的相对位置
                13.release(on_element=None)	释放一个元素上的鼠标按键
                14.reset_actions()	  清除存储的行为
                15.pause(seconds)	暂停所有动作
                16.perform()	执行所有 ActionChains 中存储的行为，可以理解成是对整个操作的提交动作

    执行原理：
        ※调用ActionChains的方法时，不会立即执行，而是将所有的操作，按顺序存放在一个队
          列里，当你调用perform()方法时，队列中的事件会依次执行
    基本用法
        ※生成一个动作 action=ActionChains(driver)
        ※动作添加方法1 action.方法1
        ※动作添加方法2 action.方法2
        ※调用perform()方法执行（action.perform()）

    具体写法：
        ※链式写法
            ActionChains(driver).move_to_element(element).click(element).perform()
        ※分布写法
            actions=ActionChains(driver)
            actions.move_to_element(element)
            actions.click(element)
            actions.perform()





"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    #     self.driver.quit()
    @pytest.mark.clicks
    def test_clicks(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element(By.CSS_SELECTOR, '[value="click me"]')
        element_double_click = self.driver.find_element(By.CSS_SELECTOR, '[value="dbl click me"]')
        element_right_click = self.driver.find_element(By.CSS_SELECTOR, '[value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_double_click)
        action.context_click(element_right_click)
        sleep(3)
        action.perform()
        sleep(3)

    @pytest.mark.move
    def test_movetoelement(self):
        self.driver.get('http://www.baidu.com')
        search = self.driver.find_element(By.CSS_SELECTOR, '#s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(search)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag = self.driver.find_element(By.XPATH, '//*[@class="drag"]')
        drop = self.driver.find_element(By.XPATH, '//div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag, drop)
        # action.click_and_hold(drag).release(drop)
        action.click_and_hold(drag).move_to_element(drop).release()
        action.perform()
        sleep(3)


    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        username = self.driver.find_element(By.CSS_SELECTOR,'label:nth-child(2) > input[type=textbox]')
        username.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACKSPACE).pause(1)
        action.perform()
        sleep(3)




