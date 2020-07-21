"""
函数代码块以def关键词开头，后接函数名称和圆括号0。
冒号起始
注意缩进
圆括号中定义参数
函数说明一文档字符串。
return[表达式]结束函数
选择性地返回一个值给调用方。
不带表达式的return或者不写数，相当于返回None

函数的调用形式
调用时的传参
位置参数
"""

##函数的定义
def func1(a,b,c):
    """
    函数func1的作用
    :param a:参数a是用来打印
    :param b:
    :param c:
    :return:
    """
    print("这是一个函数")
    print("这是一个参数a",a)
    #快捷键 ctrl+D 复制一行
    print("这是一个参数b", b)
    print("这是一个参数c", c)
    return

##函数的调用
func1(1,None,None)