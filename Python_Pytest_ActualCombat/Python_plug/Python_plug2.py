"""
Pytest插件加载方式

内置plugin:
    从代码内部的_pytest目录加载

外部插件（第三方插件）
    通过setuptools entry points 机制发现的第三方插件

conftest.py存放的本地插件（重点）
    自动模块发现机制

hook(钩子)函数定制和扩展插件
conftest.py：本地插件库，存放fixture函数或者hook函数所用与该文件所在目录及其所有子目录

pytest_collection_modifyitems 收集上来的测试用例实现定制化功能
解决问题：1.自定义用例的执行顺序
        2.解决编码问题（中文的测试用例名称）
        3.自动添加标签

pytest --trace-config 查看当前pytest中所有的plugin(带有hook方法的文件)

（具体内容查看 conftest.py 文件）


"""


