"""
Pytest 常用插件
pip install pytest-ordering       控制用例的执行顺序
pip install pytest-dependency     控制用例的依赖关系
pip install pytest-xdist                 分布式并发执行测试用例
pip install pytest-rerunfailures 失败重跑
pip install pytest-assume        多重较验
pip intall  pytest-html           测试报告
"""
import pytest


# 失败重跑：根据装饰器参数reruns的值，规定失败重跑次数
@pytest.mark.flaky(reruns=5)
def test_add():
    assert 6 == 1 + 2


# 多重较验
def test_assume():
    # pytest-assume相当于assert
    # 但是使用pytest-assume会执行完所有断言，无论通过或失败，并且执行结束后会打印失败断言的信息
    # assert 执行到失败便结束
    pytest.assume(1 == 2)
    pytest.assume(1 == 1)
    pytest.assume(3 == 2)


# 控制用例的执行顺序
class TestOrdering:
    # 通过修饰器 pytest.mark.run以及参数order的值，控制用例执行顺序
    # 执行测试用例时，优先执行有pytest.mark.run修饰器的测试用例，再执行其他测试用例
    @pytest.mark.run(order=2)
    def test_foo(self):
        print('foo')

    @pytest.mark.run(order=1)
    def test_bar(self):
        print('bar')


# 控制用例的依赖关系

canshu = {'username': 'admin', 'pwd': '211'}


@pytest.fixture(scope='function')
def login():
    user = canshu['username']
    pwd = canshu['pwd']
    print(f'正在执行登录操作，用户名：{user},密码：{pwd}')
    if pwd == '111':
        return True
    else:
        return False


class TestLogin:
    @pytest.mark.dependency
    def test_login(self, login):
        # 获取登录结果
        assert login == True

    @pytest.mark.dependency(depends=['TestLogin::test_login'])
    def test_case1(self):
        print('登录成功后执行的操作1')

    @pytest.mark.dependency(depends=['TestLogin::test_login'])
    def test_case2(self):
        print('登录成功后执行的操作2')
