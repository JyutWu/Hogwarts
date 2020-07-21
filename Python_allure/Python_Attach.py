"""
前端自动化测试-截图
场景：
※前端自动化测试经常需要附加图片或html，在适当的地方，适当的时机截图
解决：
@allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
步骤：
※在测试报告里附加网页：
   allure.attach(body(内容），name,attachment—type,extension):
   allure.attach('<head></head><bodY>首页</body>','这是错误页的结果信息'，allure.attachment_type.HTML)
※在测试报告里附加图片：
   allure.attach.file(source,name,attachment_type,extension):
   allure.attach.file("./result/b.png",attachment—type=allure.attachment—type.PNG)

"""

import allure
import pytest


def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段HTMLbody块</body>", 'HTML测试块', attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file('C:/Users/Administrator/Desktop/test.jpg', name='这是一张图片', attachment_type=allure.attachment_type.JPG)


if __name__ == '__main__':
    pytest
