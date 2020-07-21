"""
场景：
希望在报告中看到测试功能`子功能或场景，测试步骤`包括测试附加信息
解决：
@Feature,@story,@step,@attach
步骤：
import allure
功能上加@allure.feature('功能名称'）
子功能上加@allure.story('子功能名称'）
步骤上加@allure.step('步骤细节'）
@allure.attach('具体文本信息'），需要附加的信息，可以是数据。文本，图片，视频，网页
如果只测试登录功能运行的时候可以加限制过滤：
pytest文件名—allure-features'购物车功能'—allure-stories'加入购物车'（注意这里—allure_features中间是下划线）

"""
import pytest


def test_success():
    assert True


def test_faile():
    assert False


def test_skip():
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


if __name__ == '__main__':
    pytest
