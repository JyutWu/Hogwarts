import os
import sys
import time
import allure
import pytest
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'python'])
def test_demo(test_data1):
    driver = webdriver.Chrome()
    with allure.step('打开百度网页'):
        driver.get("https://www.baidu.com/")
    with allure.step('输入查询内容'):
        driver.find_element_by_id("kw").send_keys(test_data1)
    time.sleep(3)
    with allure.step('点击查询按钮'):
        driver.find_element_by_id("su").click()
    time.sleep(2)
    with allure.step('保存图片'):
        driver.save_screenshot('./image/b.png')
        allure.attach.file('./image/b.png', name='搜索截图', attachment_type=allure.attachment_type.PNG)
    with allure.step('退出浏览器'):
        driver.close()
