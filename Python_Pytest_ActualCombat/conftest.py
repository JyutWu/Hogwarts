from typing import List

import pytest
import yaml


@pytest.fixture()
def login():
    print('登录操作')
    # yield 激活fixture teardown方法
    yield ['name', 'pwd']
    print('teardown')


@pytest.fixture()
def Tips():
    print('计算开始')
    # yield 激活fixture teardown方法
    yield
    print('计算结束')


"""
pytest_collection_modifyitems 收集测试用例实现定制化功能
解决问题：1.自定义用例的执行顺序
        2.解决编码问题（中文的测试用例名称）
        3.自动添加标签
"""


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)  # 收集测试用例，存放在列表中，执行时便是按照列表中的顺序执行
    print(len(items))
    # 倒序执行
    items.reverse()
    # 含有中文的测试用例名称，改写编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 给测试用例添加mark标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)


# 命令行去添加一个自定义参数
def pytest_addoption(parser):
    mygroup = parser.getgroup('Hugo')  # 将下面的的自定义参数都展示到 Hugo 下
    mygroup.addoption('--env',  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    mygroup.addoption('--env1',  # 注册一个命令行选项
                      default='test',
                      dest='env1',
                      help='set your run env'
                      )


# 处理命令行传来的参数，设置成fixture,将test 环境和dev环境或者其他环境
# 分别处理，获取想要的不同环境下的测试数据
# test_env.py
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption('--env', default='test')

    if myenv == 'dev':
        datapath = './datas/dev/data.yaml'

    if myenv == 'test':
        datapath = './datas/test/data.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过这个方法动态的生成测试用例(test_param.py)
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if 'param' in metafunc.fixturenames:
        metafunc.parametrize('param',
                              metafunc.module.datas,  # 获取测试用例方法的参数（自定义的data 数据集）
                              ids=metafunc.module.myids,  # 获取测试用例名称（自定义的myids 数据集）
                              scope='function')
