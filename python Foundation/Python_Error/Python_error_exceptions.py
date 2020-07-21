"""
错误：语法错误、逻辑错误、系统错误
异常：1.程序执行过程中出现的未知错误；
    2.语法和逻辑都是正常的；
    3.程序业务逻辑不完善引起的程序漏洞（bug）

错误与异常的区别：异常可以被捕获和处理，错误一般是编码错误、逻辑错误、系统错误

常见的异常类型：除零异常、名称异常、索引异常、键异常、值异常、属性异常等等。
异常/错误处理流程:检测到错误>>>引发异常>>>捕获异常操作
1.如果是拼写/配置等引起的错误,根据错误信息排查错误出现的位置进行解决
2.如果是程序设计不完善引起的错误,根据漏洞的情况进行设计处理漏洞的逻辑
"""


# 除零异常
# def div(a, b):
#     return a / b
#
#
# print(div(1, 0))

# 名称异常
# num = 1
# if name > 0:
#     print("num > 1")

# 索引异常

# list1 = [1, 2, 3]
# print(list1[3])  # 指定索引不在列表范围内

# 键异常

# dict1 = {'name': 'tom', 'gender': 'male'}
# print(dict1['num'])  # 指定键不在字典内

# 值异常
# num = input("请输入一个值:")
# print(int(num))  # 要求整型，但是输入字符串


# 异常处理

# def div(a, b):
#     return a / b
#
#
# f = open('D:/Hogwarts/python/Python_IO/data.txt')
#
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[2])
#     print(f.readlines())
#
# except Exception as error:
#     print(error)
#     print("出现异常")
# else:
#     print("没有异常的时候执行")
#
# finally:  # finally 最终都会被执行,无论有异常还是没异常的情况
#     print("finally")
#     f.close()

def set_age(num):
    if num <= 0 or num > 200:
        raise ValueError(f'值错误:{num}')
    else:
        print(f'设置的年龄值为:{num}')


set_age(-1)
