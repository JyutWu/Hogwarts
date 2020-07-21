"""
文件读取

读写文件的操作步骤：
第一步：打开文件，获取文件描述符
第二步：操作作文件描述符（读|写）
第三步：关闭文件
注意：
文件读写操作完成后，应该及时关闭
"""
"""
open(file,mode='r',buffering=-l,encoding=None,errors=None,newline=None,closefd=True,opener=None)
参数说明：
file：文件名称的字符串值
mode：只读r，写入w，追加a，默认文件访问模式为只读（r).
buffering：寄存区缓存
    0:不寄存
    1：访问文件时会寄存行，
    >1寄存区的缓冲大小。
    负值，寄存区的缓冲大小则为系统默认。

"""
"""
最优写法：
with open('filename','r') as f:

读取文件常用方法
read()   读取文件中的所有内容（缺点；当文件内容非常大：大于内存时，无法使用这个方法）
readable() 判断文件是否可读
readline() 每次读取一行（包括行结束符），返回的是一个字符串对象，保持当前行的内存
readlines() 读取所有行的内容放到列表中
"""
# f = open('C:\/Users\/Administrator\/Desktop\/test.txt')
# print(f.readable())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# f.close()


# 使用with语句块，可以将文件打开，执行完毕后自动关闭文件
#如果是读取图片的话，mode参数使用 'rb'，读取二进制的格式
#正常的文本，mode参数使用'rt'，也就是默认模式
with open('data.txt') as f:
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.readlines())
