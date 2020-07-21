"""
测试脚手架
test fixture 表示为了开展一项或多项测试所需要进行的准备工作，以及所有相关的清理操作。举个例子，这可能包含创建临时或代理的数据库、目录，再或者启动一个服务器进程。

测试用例
一个测试用例是一个独立的测试单元。它检查输入特定的数据时的响应。 unittest 提供一个基类： TestCase ，用于新建测试用例。

测试套件
test suite 是一系列的测试用例，或测试套件，或两者皆有。它用于归档需要一起执行的测试。

测试运行器（test runner）
test runner 是一个用于执行和输出测试结果的组件。这个运行器可能使用图形接口、文本接口，或返回一个特定的值表示运行测试的结果。

编写规则：
1.测试模块首先 import unittest
2.测试类必须继承 unittest.TestCase
3.测试方法必须 ‘test_’开头


setUp 用来为测试准备环境 tearDown 用来清理环境

UnitTest断言方法
assertEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，相等则测试用例通过。

assertNotEqual(a,b，[msg='测试失败时打印的信息']):断言a和b是否相等，不相等则测试用例通过。

assertTrue(x，[msg='测试失败时打印的信息'])：断言x是否True，是True则测试用例通过。

assertFalse(x，[msg='测试失败时打印的信息'])：断言x是否False，是False则测试用例通过。

assertIs(a,b，[msg='测试失败时打印的信息']):断言a是否是b，是则测试用例通过。

assertIsNone(x，[msg='测试失败时打印的信息'])：断言x是否None，是None则测试用例通过。

assertIn(a,b，[msg='测试失败时打印的信息'])：断言a是否在b中，在b中则测试用例通过。


"""

import unittest


class TestStringMethods(unittest.TestCase):

    # setupClass和teardownClass 方法是在整个类的前后分别调用
    @classmethod
    def setUpClass(cls) -> None:
        print('set up class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear down class')

    # setup 和 teardown 方法是在每条测试用例前后分别调用的方法
    def setUp(self) -> None:
        print('\nsetup')

    def tearDown(self) -> None:
        print('tearDown')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
        print('test_upper')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print('test_isupper')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        print('test_split')


if __name__ == '__main__':
    unittest.main()
