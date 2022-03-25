"""生产者消费者问题
描述:有多个消费者和生产者，生产者会向队列中生产商品，消费者会从队列中获取商品

"""
import queue
import threading
from abc import ABC, abstractmethod
# queue.Queue 线程安全

class Worker(object):
    def __init__(self, id: int, queue: queue.Queue):

        self.id = id
        self.queue = queue
        self.thread = threading.Thread(target=self.run)
        self.thread.setDaemon(True)
    
    
    @abstractmethod
    def run(self): ...

    def start(self):
        self.thread.start()

class Producer(Worker):

    def run(self):
        for i in range(10):
            data = f'id: {self.id} message: {i}'
            self.queue.put(data)
            print(f"put: {data}")
    

class Consumer(Worker):

    def run(self):
        while True:
            data = self.queue.get()
            print(f"Consumer {self.id} get: {data}")

if __name__ == "__main__":

    q = queue.Queue(5)

    allproducers = [Producer(i, q) for i in range(10)]
    allconsumers = [Consumer(i, q) for i in range(10)]

    for p in allproducers:
        p.start()
    
    for c in allconsumers:
        c.start()

    while True: ...