"""
列表的特性
list.append(x)：在列表的末尾添加一个元素。相当于a[len(a):l=卜]。
list.insert(i,x):在给定的位置插人一个元素。第一个参数是要插入的元素的索引，以a.insert(0,x)插入列表头部，a.insert(len(a),x)等同于a.append(x)。
list.remove(x)：移除列表中第一个值为x的元素。如果没有这样的元素，则抛出ValueError异常。
list.pop([i])：删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop()将会删除并返回列表中的最后一个元素。
list.sort(key=None,reverse=False):对列表中的元素进行排序（参数可用于自定义排序，解释请参
见sorted())
list.reverse()：反转列表中的元素。


list.clear()删除列表中所有的元素。相当于del a[:]。
list.extend(iterable)：使用可迭代对象中的所有元素来扩展列表。相当于 a[len(a):]=iterable。
1ist.index(x[,start[,end]])返回列表中第一个值为x的元素的从零开始的索引。如果没有这样的元素将会抛出ValueError异常。可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是start参数。
list.count(x)：返回元素x在列表中出现的次数。
list.copy()：返回列表的一个浅拷贝。相当于a[:]。
注意：
insert，remove或者sort方法，只修改列表，没有打印出返回值
。并非所有数据或可以排序或比较（字符串和数字等）
它们返回默认值None。这是Python中所有可变数据结构的设计原则。

"""
# list_hogwarts=[1,4,2,6]
# list_hogwarts.append(0)
# list_hogwarts.insert(0,11)
# list_hogwarts.remove(0)
# list_hogwarts.pop(0)
# list_hogwarts.sort(reverse=True)  #reverse=True 降序
# list_hogwarts.reverse()
#
#
# print(list_hogwarts)


"""
生成平方列表
"""
# list_square=[]
#
# for i in range(1,4):
#     list_square.append(i*i)
#
# print(list_square)
#
#
# list_square2=[ i**2 for i in range(1,4)]
# print("list_square2",list_square2)
#
# list_square3=[i**2 for i in range(1,4) if i !=1]
# # for i in range(1,4):
# #     if i != 1:
# #         list_square3.append(i**2)
# print ("list_square3",list_square3)
#

list_square4=[i*j for i in range(1,4) for j in range(1,4)]

# for i in range(1,4):
#     for j in range(1,4):
#         list_square4.append(i*j)
print ("list_square4",list_square4)