# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。
数据范围：0≤n≤1000，-1000 −1000≤节点值≤1000
要求：空间复杂度 O(1)，时间复杂度 O(n)O
"""

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        
        if not pHead1 or not pHead2:
            return pHead2 if not pHead1 else pHead1
        
        p1 = pHead1
        p2 = pHead2
        p = head = ListNode(None)
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
            
        if not p1:
            p.next = p2
        else:
            p.next = p1
        return head.next
            
            
            
            