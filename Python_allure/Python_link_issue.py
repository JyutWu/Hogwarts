import allure


@allure.link('http://www.baidu.com', name='链接')  # 可以在测试报告的对应用例详情中增加链接
def test_link_issue():
    print('这是一条加了链接的测试')
    pass


TEST_CASE_LINK = 'https：//github.com/qameta/allure-integrations/issues/8#issuecomment-2683136371'


@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase_Link():
    print('这是一条测试用例的链接， 链接到测试用例系统里面')
    pass


# --allure-Link-pattern=issue:http：//www.mytesttracker.com/issue/{}
@allure.issue('140', '这是一个issue')
def test_with_issue_link():
    pass
