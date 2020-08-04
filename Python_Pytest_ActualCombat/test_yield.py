# yield 生成器


def func():
    for i in range(3):
        print(f'i={i}')
        yield # 相当于return 同时相当于暂停并且记住上一次的执行位置
        print('END')


f = func()
next(f)
next(f)
next(f)
