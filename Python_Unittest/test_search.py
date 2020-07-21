import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner


class Search:
    def search_fun(self):
        # print('\nsearch')
        return True


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('set up class')
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tear down class')

    def test_search1(self):
        print('\ntestsearch1')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print('\ntestsearch2')
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print('\ntestsearch3')
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        # print("断言相等")
        self.assertEqual(1, 1, '断言 不相等')

    def test_notequal(self):
        # print("断言不相等")
        self.assertNotEqual(1, 2, '断言相等 ')
        # self.assertTrue(1 == 2, "verify")


##执行当前文件所有测试用例
if __name__ == '__main__':
    # 方法一 执行当前文件所有测试用例
    # unittest.main()

    ##方法二 通过测试套件，管理多个测试用例，选择性批量执行测试用例
    # 创建一个测试套件，testsuite
    # suite=unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search2"))
    # unittest.TextTestRunner().run(suite)

    ##方法三 执行某个测试类,将测试类添加到测试套件里，批量执行测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    # suite = unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite)

    """方法四 ：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
        test_dir='./test_case'
        discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py'）
        1.discover可以一次调用多个脚本
        2.test-dir被测试脚本的路径
        3.pattern脚本名称匹配规则
"""
    # test_dir = '../Python_Unittest'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    ## 使用HTMLTestRunner 生成报告
    report_title = '我的用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'result_HTML_TestRunner.html'

    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSearch))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
