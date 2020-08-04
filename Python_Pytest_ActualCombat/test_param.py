# datas = [[1, 2, 3], [0.2, 0.3, 0.4]]
# myids = ['整数', '浮点数']
import yaml

with open('./datas/testparam.yaml') as f:
    myparam = yaml.safe_load(f)
    # datas和myids 要与conftest.py 里的钩子函数的
    # metafunc.module.datas,  ids=metafunc.module.myids 保持一致
    datas = myparam.values()
    myids = myparam.keys()


# param 要与conftest.py里面处理的param 保持一致
# if 'param' in metafunc.fixturenames:
#        metafunc.parametrize('param',
def test_param(param):
    print(f'param = {param}')
    print('动态生成测试用例')


def test_yaml():
    print(f'{myparam}')
