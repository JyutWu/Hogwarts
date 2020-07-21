"""
什么是进程？
1.进程是执行中的程序
2.拥有独立地址空间、内存、数据栈等
4.操作系统管理
5.派生(fork或spawn)新进程
6.进程间通信（IPC)方式共享信息

什么是线程？
1.同进程下执行，并共享相同的上下文
2.线程间的信息共享和通信更加容易
3.多线程并发执行（不是指多个线程同时执行，而是指多个线程轮换执行）
4.需要同步原语

Python与线程
1.解释器主循环
2.主循环中只有一个控制线程在执行
3.使用全局解释器锁（GIL）

Python线程管理
-thread：提供了基本的线程和锁
threading:提供了更高级别，功能更全面的线程管理
1.支持同步机制
2.支持守护线程

"""
import _thread
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info(f"start {nloop} at " + ctime())
    sleep(nsec)
    logging.info(f"end {nloop} at " + ctime())





def main():
    logging.info("start all at " + ctime())
    threads=[]
    nloops = range(len(loops))
    for i in nloops:  # 声明线程，并且保存至列表
        t = MyThread(loop, (i, loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:  # 启动线程
        threads[i].start()

    for i in nloops:
        threads[i].join() #判断线程是否结束，如果未结束，则将main方法堵塞在此处

    logging.info("end all at " + ctime())
    # sleep(6) # _thread不成文的规定：当主线程结束的时候，所有子线程会强制杀死(没有守护线程的概念)，所以这个主线程需要加睡眠时间，保证子线程也可以运行


if __name__ == '__main__':
    main()

#原语
#锁（文件的互斥访问）
#信号量