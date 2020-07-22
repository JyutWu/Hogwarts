import pytest


@pytest.fixture()
def login():
    print('登录操作')
    #yield 激活fixture teardown方法
    yield ['name','pwd']
    print('teardown')

@pytest.fixture()
def Tips():
    print('计算开始')
    #yield 激活fixture teardown方法
    yield
    print('计算结束')
