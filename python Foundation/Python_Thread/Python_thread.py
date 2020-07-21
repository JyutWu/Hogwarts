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
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


def loop(nloop, nsec, lock):
    logging.info(f"start {nloop} at " + ctime())
    sleep(nsec)
    logging.info(f"end {nloop} at " + ctime())
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:  # 锁处理
        lock = _thread.allocate_lock()  # 声明 锁
        lock.acquire()  # 将锁锁上
        locks.append(lock)  # 将锁传递给 locks 列表

    for i in nloops:  # 启动线程
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:  # 判断锁是否都被释放
        while locks[i].locked(): pass

    logging.info("end all at " + ctime())
    # sleep(6) # _thread不成文的规定：当主线程结束的时候，所有子线程会强制杀死(没有守护线程的概念)，所以这个主线程需要加睡眠时间，保证子线程也可以运行


if __name__ == '__main__':
    main()
