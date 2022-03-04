# -*- coding:utf-8 -*-
"""
描述
    用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能。 
    队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素。

数据范围： n\le1000n≤1000
要求：存储n个元素的空间复杂度为 O(n)O(n) ，插入与删除的时间复杂度都是 O(1)O(1)

解析:

队列是一端进行插入操作，一端进行删除操作 栈是一端进行插入删除操作，且遵循FILO或LIFO即先进后出或者后进先出的特性两个
栈实现队列就是说将两个栈一个当做入队操作，一个当做出队操作 入队操作的栈需要进行增加数据的操作，即push() 出队操作的
栈需要进行删除数据的操作，即pop() 但是明确一下，删除操作的栈需要先把增加数据的栈中的数据加到栈中才可以删除

"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                node = self.stack1.pop()
                self.stack2.append(node)
                
        if self.stack2:
            return self.stack2.pop()
        return