"""
场景：
希望在报告中看到测试功能`子功能或场景，测试步骤`包括测试附加信息
解决：
@Feature,@story,@step,@attach
步骤：
import allure
功能上加@allure.feature('功能名称'）
子功能上加@allure.story('子功能名称'）
@allure.step('步骤细节'）:以装饰器的形式放在类或者方法上面
with allure.step('步骤细节'）:可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
@allure.attach('具体文本信息'），需要附加的信息，可以是数据。文本，图片，视频，网页
如果只测试登录功能运行的时候可以加限制过滤：
pytest 文件名 --allure-features'购物车功能'    --allure-stories'加入购物车'（注意这里--allure-features中间是横杠）

"""
import allure
import pytest


@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        print('这是登录: 测试用例，登录成功')
        pass

    @allure.story('登录失败')
    def test_login_success_a(self):
        print('这是登录: 测试用例，登录成功')
        pass

    @allure.story('用户名缺失')
    def test_login_success_b(self):
        allure.step('用户名缺失步骤')
        print('用户名缺失')
        pass

    @allure.story('密码缺失')
    def test_login_failure(self):
        with allure.step('点击用户名'):
            print('请输入用户名')
        with allure.step('点击密码'):
            print('请输入密码')
        print('点击登录')
        with allure.step('点击登录之后登录失败'):
            assert '1' == 1
            print('登录失败')
        pass

    @allure.story('登录失败')
    def test_login_failure_a(self):
        print('这是登录： 测试用例，登录失败')
        pass


if __name__ == '__main__':
    pytest


