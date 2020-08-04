import pytest


# @pytest.fixture()
# def login():
#     print('登录操作')
#     #yield 激活fixture teardown方法
#     yield ['name','pwd']
#     print('teardown')

@pytest.mark.one
def test_case1():
    print('test_case1')


def test_case2():
    print('test_case2')


def test_case3():
    print('test_case3')
