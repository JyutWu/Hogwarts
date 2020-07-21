"""
数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改
变。简单来说，就是参数化的应用。数据量小的测试用例可以使用代码的参数
化来实现数据驱动，数据量大的情况下建议大家使用一种结构化的文件（例如
yaml，json等）来对数据进行存储，然后在测试用例中读取这些数据。


App、web、接口自动化测试
※测试步骤的数据驱动
※测试数据的数据驱动
※配置的数据驱动
"""
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yaml')))
    def test_demo(self, env):
        if 'test' in env:
            print('这个是测试环境')
            print("测试环境的IP是：" ,env['test'])
        elif 'dev' in env:
            print('这个是开发环境')
            print("开发环境的IP是：", env['dev'])
