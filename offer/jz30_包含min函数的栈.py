# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。

此栈包含的方法有：
push(value):将value压入栈中
pop():弹出栈顶元素
top():获取栈顶元素
min():获取栈中最小元素
"""
class Solution:
    
    def __init__(self):
        self.datastack = []
        self.minstack = []
    
    def push(self, node):
        # write code here
        m = self.min()
        if m and m <= node:
            self.minstack.append(m)
        else:
            self.minstack.append(node)
        self.datastack.append(node)
        
    def pop(self):
        # write code here
        node = None
        if self.datastack:
            node = self.datastack.pop()
            self.minstack.pop()
        
        return node
        
    def top(self):
        # write code here
        data = None
        if self.datastack:
            data = self.datastack[-1]
        return data
        
    def min(self):
        # write code here
        data = None
        if self.minstack:
            data = self.minstack[-1]
        return data
        