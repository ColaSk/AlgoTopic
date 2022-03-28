# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。

数据范围：0≤n≤1000
要求：空间复杂度 O(1)，时间复杂度 O(n)。

"""
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        
        p = pHead
        q = None
        t = None
        while p:
            q = p.next
            p.next = t
            t = p
            p = q
        return t
            
            