"""
两种编程思想
面向过程：
1.一种以过程为中心的编程思想
2.简单的事情
面向对象：
1.一种更符合我们人类思维习惯的编程思想
2.面向对象开发就是不断的创建对象，使用对象，操作对象做事情
3.复杂的事情

什么是面向对象？
1.语言层面，封装代码和数据
2.规格层面，对象是一系列可以被使用的公共接口
3，从概念层面，对象是某种拥有责任的抽象

面向对象程序设计规则
1.首先分析有哪些类
2.每个类有哪些属性和行为
3.类与类之间存在的关系

类(Class):抽象的概念，一类事物。
方法：类中定义的函数，对外提供的服务。
类变量：类变量在整个实例化的对象中是公用的。
实例引用：实例化一个对象
实例变量：以'self.变量名'的方式定义的变量


"""


# 创建一个人类
# 通过class 关键字，定义了一个类

class Person:
    # 类变量
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问到的变量是实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print('init function')

    # def set_param(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age
    @classmethod
    def eat(self):
        print(f'{self.name} eating')

    def play(self):
        print(f'{self.name} playing')

    def dump(self):
        print(f'{self.name} dumping')


# 类方法和实例方法
# 类方法是不能访问实例方法的,通过@classmethod装饰器，将实例方法定义为类方法

Person.eat()
# zs = Person('zhangsan', '20', '男', '100')
# zs.eat()

# 类变量和实例变量的区别
# 类变量是需要类来访问的，实例变量需要实例来访问
# print(Person.name)
# Person.name = 'tom'
# print(Person.name)
#
# zs = Person('zhangsan', '20', '男', '100')
# print(zs.name)
# zs.name = 'hugo'
# print(zs.name)

# 类的实例化，创建了一个实例
# zs = Person('zhangsan', '20', '男', '100')
# zs.eat()
# # zs.set_param('zhangsan')
# # zs.set_age(9)
# print(f'zhangsan 的姓名是 {zs.name}，年龄是 {zs.age}\n性别是 {zs.gender},体重是{zs.weight}')
#
# ls = Person('李四', '28', '女', '120')
# ls.dump()
# # zs.set_param('zhangsan')
# # zs.set_age(9)
# print(f'ls 的姓名是 {ls.name}，年龄是 {ls.age}\n性别是 {ls.gender},体重是{ls.weight}')
