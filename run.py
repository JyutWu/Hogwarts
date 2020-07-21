import unittest

from HTMLTestRunner_PY3 import HTMLTestRunner
from test_search import TestSearch

if __name__ == "__main__":
    report_title = '我的用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'result_HTML_TestRunner.html'

    test_dir = './Python_Unittest'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_*.py")
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)