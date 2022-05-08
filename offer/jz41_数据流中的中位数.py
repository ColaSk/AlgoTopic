# -*- coding:utf-8 -*-
"""
描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

数据范围：数据流中数个数满足 1 \le n \le 1000 \1≤n≤1000  ，大小满足 1 \le val \le 1000 \1≤val≤1000 

解析:
插入法
大顶锥
"""
class Solution:
    def __init__(self):
        self.val = []
    
    def Insert(self, num):
        # write code here
        i = 0
        
        for v in self.val:
            if num <= v:
                break
            i += 1
        
        self.val.insert(i, num)
        
    def GetMedian(self):
        # write code here
        l = len(self.val)
        
        if l%2 == 1:
            return self.val[l//2]
        
        return (self.val[l // 2] + self.val[l // 2 - 1]) / 2.0
        
        