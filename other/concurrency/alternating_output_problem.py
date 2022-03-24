
"""交替输出问题
描述: 两个线程，一个输出数字，一个输出字母交替输出 1A2B3C....
解析: 获取对方的锁, 释放自己的锁
"""
from threading import Thread, Lock
from typing import Iterable

class ThreadPrint(object):

    def __init__(self, id: int, data: Iterable):

        self.id = id
        self.data = data
        self.lock = Lock()
        self.thread = Thread(target=self.prin)
        self.thread.setDaemon(True)

    def set_other_lock(self, other_lock: Lock):
        self.other_lock = other_lock

    def prin(self):
        for d in self.data:
            self.other_lock.acquire()
            print(d, end='')
            self.lock.release()
    
    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()

if __name__ == "__main__":
    
    th1 = ThreadPrint(0, "1234567")
    th2 = ThreadPrint(0, "ABCDEFG")

    th1.set_other_lock(th2.lock)
    th2.set_other_lock(th1.lock)

    th1.lock.acquire()

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print('')

    # while True: ...

    