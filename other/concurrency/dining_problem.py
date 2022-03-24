import time
from threading import Lock, Thread

# 筷子
class Chopsticks(object):

    def __init__(self, id: int):
        self.id = id
        self._lock = Lock()
    
    @property
    def lock(self):
        return self._lock

# 哲学家
class Philosopher(object):

    def __init__(self, id, lchopsticks: Chopsticks, rchopsticks: Chopsticks):
        self.id = id
        self.lc = lchopsticks # left chopsticks
        self.rc = rchopsticks # right chopsticks
        self.thread = Thread(target=self.eat)
        self.thread.setDaemon(True)

    def eat(self):
        while True:
            with self.rc.lock:
                time.sleep(1)
                print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                with self.lc.lock:
                    time.sleep(1)
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                    time.sleep(1)
            print(f'哲学家ID: {self.id} 进餐完毕')

    def start(self):
        self.thread.start()                



"""哲学家就餐问题的解决方案
1.两把锁合并成一把锁(将五把锁合并成一把锁), 但是会造成资源浪费，就餐过程中仅需要两根筷子，但是会把
  五根筷子资源全部锁住，造成资源浪费
2.混入一个左撇子的方式(其他所有人都是先抢右边在抢左边，同时只有一个人在吃，所以效率和1相同)
3.混入多个左撇子的方式(将编号为奇数的作为左撇子)

"""

class LockPhilosopher(Philosopher):

    """
    1.
    """
    
    lock = Lock()

    def eat(self):
        while True:
            with self.__class__.lock:
                with self.rc.lock:
                    time.sleep(1)
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                    with self.lc.lock:
                        time.sleep(1)
                        print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                        time.sleep(1)
                print(f'哲学家ID: {self.id} 进餐完毕')


# 左撇子哲学家
class LeftPhilosopher(Philosopher):

    """
    2.
    """

    def eat(self, left_id: int = 0):
        while True:
            
            if self.id == left_id:
                with self.lc.lock: 
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                    with self.rc.lock:
                        print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                        time.sleep(2)
            else:
                with self.rc.lock:
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                    with self.lc.lock:
                        print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                        time.sleep(2)
            print(f'哲学家ID: {self.id} 进餐完毕')


# 有效率的左撇子哲学家
class EfficientLeftPhilosopher(Philosopher):

    """
    3.
    """

    def eat(self):
        while True:
            
            if self.id%2:
                with self.lc.lock: 
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                    with self.rc.lock:
                        print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                        time.sleep(2)
            else:
                with self.rc.lock:
                    print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.rc.id}')
                    with self.lc.lock:
                        print(f'哲学家ID: {self.id} 已经获取筷子ID: {self.lc.id}')
                        time.sleep(2)
            print(f'哲学家ID: {self.id} 进餐完毕')

def main(philosopher_class: Philosopher):
    
    allchopsticks = [Chopsticks(i) for i in range(5)]

    allphilosophers = [philosopher_class(i, allchopsticks[i-1], allchopsticks[i]) for i in range(5)]

    for p in allphilosophers:
        p.start()
    
    while True:
        pass

if __name__ == '__main__':
    main(EfficientLeftPhilosopher)
