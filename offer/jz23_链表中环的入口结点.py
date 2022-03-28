# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
描述
给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。

数据范围： n≤10000，1<=结点值<=10000
要求：空间复杂度 O(1)，时间复杂度 O(n)
"""

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        
        if not pHead:
            return
        
        p = q = pHead
        
        while True:
            
            if not q or not q.next:
                return
            
            p = p.next
            q = q.next.next
            
            if p == q:
                break
                
        q = pHead
        
        while p != q:
            p = p.next
            q = q.next
        return p