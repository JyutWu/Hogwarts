"""
OS模块
os模块主要是对文件，目录的操作
常用方法：
os.mkdir()创建目录
os.removedirs()删除文件
os.getcwd()获取当前目录
os.path.exists(dir or file)判断文件或者目录是否存在


"""
import os

# os.mkdir('testdir')
# print(os.listdir('../'))
# os.removedirs('testdir')
# print(os.getcwd())

# 在本地创建目录、文件，首先判断当前路径下是否已存在相同的目录和文件
print(os.path.exists('b')) #判断当前目录是否存在指定目录、文件
if not os.path.exists('b'):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    f = open('b/test.txt', 'w')
    f.write('hello hogwarts')
    f.close()
