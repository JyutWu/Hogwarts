"""
只执行一定范围内的测试用例
场景
通常测试有PO、冒烟测试、验证上线测试。按重要性级别来分别执行的，比如上线要把主流程和重要模块都跑一遍
解决：
1.通过附加pytest.mark标记
2.通过allure.feature,allure.story
3.也可以通过allure.severity来附加标记
级别：Trivial不重要，Minor不太重要，Normal正常问题，Critical严重,Blocker:阻塞
步骤：
在方法，函数和类上面加 @allure.severity(allure.severity_level.TRIVIAL)
执行时
pytest -s -v文件名 --allure-severities normal,critical
Blocker级别：中断缺陷(客户端程序无响应，无法执行下一步操作)
Critical级别：临界缺陷（功能点缺矢）
Normal级别：普通缺陷（数值计算错误）
Minor级别：次要缺陷（界面错误与UI需求不符）
Trivial级别：轻微缺陷（必输项无提示．或者提示不规范）

"""