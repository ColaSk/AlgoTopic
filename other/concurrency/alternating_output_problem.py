
"""交替输出问题
描述: 两个线程，一个输出数字，一个输出字母交替输出 1A2B3C....
解析: 
1.获取对方的锁, 释放自己的锁
2.使用条件锁，一次释放一个线程执行
"""

import time
from threading import Thread, Lock, Condition
from typing import Iterable

## 1.获取对方的锁, 释放自己的锁
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


def LockThreadPrintTest():

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


## 2.条件锁
class ConditionThreadPrint(object):

    def __init__(self, id: int, condition: Condition, data: Iterable) -> None:
        self.id = id
        self.condition = condition
        self.data = data
        self.thread = Thread(target=self.prin)
        self.thread.setDaemon(True)

    def start(self):
        self.thread.start()

    def prin(self):
        self.condition.acquire()
        for d in self.data:
            self.condition.wait()
            print(d, end='', flush=True)
            
        self.condition.release()


def ConditionThreadPrintTest():

    condition_lock = Condition()
    th1 = ConditionThreadPrint(0, condition_lock, "1234567")
    th2 = ConditionThreadPrint(1, condition_lock, "ABCDEFG")
    th3 = ConditionThreadPrint(1, condition_lock, "HIGKLMN")

    th1.start()
    th2.start()
    th3.start()

    for i in range(31):
        time.sleep(1)
        condition_lock.acquire()
        condition_lock.notify(1)  # 放行
        condition_lock.release()


if __name__ == "__main__":

    # LockThreadPrintTest()
    ConditionThreadPrintTest()