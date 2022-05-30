# -*- coding:utf-8 -*-

"""
描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

数据范围：1 \leq n \leq 401≤n≤40
要求：时间复杂度：O(n)O(n) ，空间复杂度： O(1)O(1)
"""
class Solution:
    def jumpFloor(self, number):
        # write code here
        
        if number < 3:
            return number
        
        p1 = 1
        p2 = 2
        res = 3
        
        for i in range(3, number+1):
            res = p1 + p2
            p1 = p2
            p2 = res
        
        return res
        
        
        