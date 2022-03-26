"""多线程事务回滚问题
描述:一个问题被多个线程分解并发执行，当其中一个失败时，取消其他线程并回滚
解析: 
"""

from __future__ import barry_as_FLUFL
import threading
import time
import typing
import sys
import inspect
import ctypes

# 终止线程方案
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
 
def stop_thread(thread: threading.Thread):
    _async_raise(thread.ident, SystemExit)

class TaskStatus(object):
    notend = 1
    success = 2
    failed = 3

class Worker(object):

    def __init__(self, boss, id: int, times: float, success: bool):
        self.id = id
        self.times = times
        self.success = success
        self._result = TaskStatus.notend
        self.boss = boss
        self.cancel_bool = False

        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(True)

    @property
    def result(self):
        return self._result

    def run(self):
        print(f"task {self.id} start work ...")

        t = 0
        while True:

            time.sleep(1)
            t += 1
            
            if self.cancel_bool:
                self.rollback()
                break

            if t > self.times:
                print(f"task {self.id} end work success...")
                break

            # 模拟任务失败
            if not self.success:
                self._result = TaskStatus.failed
                self.boss.end(self)
    
    def cancel(self):
        print(f'task {self.id} cancel')
        self.cancel_bool = True
    
    def rollback(self):
        # 事务回滚
        print(f"task {self.id} rollback success...")

    def start(self):
        self.thread.start()

    def join(self):
        self.thread.join()


class Boss(object):
    def __init__(self, id: int):
        self.id = id
        self.tasks: typing.List[Worker] = []
        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(True)
        self.cancel_bool = False
    
    def add_task(self, task:Worker):
        self.tasks.append(task)
    
    def end(self, task: Worker):
        if task.result == TaskStatus.failed:
            print(f"task {task.id} error, end")
            self.cancel(task)

    def cancel(self, task: Worker):
        for t in self.tasks:
            print(f"boss cancel task: {t.id}")
            t.cancel()
        self.cancel_bool = True
    
    def start(self):
        self.thread.start()
    
    def join(self):
        self.thread.join()

    def run(self):
        for task in self.tasks:
            task.start()

        while True:
            if self.cancel_bool:
                break

            time.sleep(1)

        print('boss end')

def main():

    boss = Boss(1)

    tasks = [Worker(boss, 1, 10, True), Worker(boss,2, 6, True), Worker(boss, 3, 1, False)]

    for task in tasks:
        boss.add_task(task)
    
    boss.start()
    boss.join()

if __name__ == '__main__':
    main()