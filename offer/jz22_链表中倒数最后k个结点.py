# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pHead ListNode类 
# @param k int整型 
# @return ListNode类
#

"""
输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。
如果该链表长度小于k，请返回一个长度为 0 的链表。
 
要求：空间复杂度 O(n)，时间复杂度 O(n)
进阶：空间复杂度 O(1)，时间复杂度 O(n)
"""

class Solution:
    def FindKthToTail(self , pHead: ListNode, k: int) -> ListNode:
        # write code here
        p = q = pHead
        
        if not p:
            return 
        if k <= 0:
            return
        
        for _ in range(k-1):
            q = q.next
            if not q:
                return 
        
        while q.next:
            q = q.next
            p = p.next
            
        return p
            
            