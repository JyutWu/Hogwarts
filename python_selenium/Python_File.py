"""
文件上传：
input标签可以直接使用send_keys（文件地址）上传文件
用法：
el=driver.find_element_by_id('上传按钮id')
el.send-keys("文件路径+文件名"）

"""
from time import sleep

from selenium.webdriver.common.by import By

from python_selenium.base import Base


class TestFile(Base):

    def test_fileupload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element(By.CSS_SELECTOR, '[class="st_camera_off"]').click()
        #文件上传：send_keys() 中填写文件路径
        self.driver.find_element(By.CSS_SELECTOR, '[id="stfile"]').send_keys(
            'C:/Users/Administrator/Desktop/SeleniumIDE介绍.png')
        sleep(3)
