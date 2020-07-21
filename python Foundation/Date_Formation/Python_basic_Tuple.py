#元组的定义
# tuple_hogwarts=(1,2,3)
# tuple_hogwarts2=1,2,3
# print("tuple_hogwarts",tuple_hogwarts)
# print("tuple_hogwarts2",tuple_hogwarts2)
#

#元组的不可变特性

# a=[1,2,3]
# tuple_hogwarts3=(1,2,a)
# print(id(tuple_hogwarts3[2]))
# tuple_hogwarts3[2][0]="a"
# print(id(tuple_hogwarts3[2]))
# print(tuple_hogwarts3)


#元组的内置函数

a=(1,2,3)
print(a.count(2))#返回数组元素数量
print(a.index(3))#返回数组元素索引，如果有重复的以第一个的索引为准