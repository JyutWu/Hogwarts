"""
字面量插值
"""
"""
格式化输出
转换说明符      解释
%d、%i        转换为带符号的十进制整数
％o	          转换为带符号的八进制整数
%X、%x        转换为带符号的十六进制整数
%e            转化为科学计数法表示的浮点数(e小写）
%E	          转化为科学计数法表示的浮点数(E大写）
%f、%F         转化为十进制浮点数
%g            智能选择使用%f或%e格式
%G            智能选择使用%F或%E格式
%c	          格式化字符及其CII码
%r            使用repr()函数将表达式转换为字符串
%s	          使用str()函数将表达式转换为字符串
"""

# name="hogwarts"
# age=3
# print("my name is %s,my age is %d,number is %.2f"%(name,age,3.141525))


"""
format()方法
用法：str.format()可以将	
字符串举例：print("we are the{}and{}".format('Tom','Jerry'))	
列表举例：print("we the{0}and{l}".format(*listdata))	
字典举例：print("my name is{name},age is{age}".format(**dictdata))	

"""

# name="hogwarts"
# age=3
# list1=[1,2,3,4,5]
# dict1 = {'name':'tom','gender':'male'}
# print("my name is {},my age is {},my num is {}".format(name,age,3.1452))
#
# print("my list is {},my dict is {}".format(list1,dict1))
#
# namelist=["tom","lisa","hugo"]
#
# print ("we are the {0} and {2}".format(*namelist)) #列表参数前加*，解包
# print ("my name is {name},my gender is {gender}".format(**dict1)) #字典参数前加**，解包
#


"""
F-string:字符串格式化机制
使用方法：f'{变量名},'
注意：大括号里可以是表达式或者函数，大括号内不能转义，不能使用‘\’
"""
name = "HOGWARTS"
age = 3
list1 = [1, 2, 3, 4, 5]
dict1 = {'name': 'tom', 'gender': 'male'}

print(f"my name is \n {name},my age is {age},my list is {list1[1]}, my dict is {dict1}")

# 大括号里可以是表达式或者函数
print(f'my name is {name.lower()}')

print(f'result is {(lambda x: x + 1)(2)}')  # 如果花括号{}中需要用到冒号：，则使用括号将表达式包括起来

print(f'my age is {28}')  # F-string 中的{} 中也可放入常量
