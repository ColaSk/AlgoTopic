# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#

"""
描述
给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
例如：
给出的链表为1 \-> 2\-> 3\-> 3\-> 4\-> 4\to51→2→3→3→4→4→5, 返回1\-> 2\to51→2→5.
给出的链表为1\-> 1 \-> 1\-> 2 \-> 31→1→1→2→3, 返回2\-> 32→3.

数据范围：链表长度 0 \le n \le 100000≤n≤10000，链表中的值满足 |val| \le 1000∣val∣≤1000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

解析 
双指针
"""
class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        
        if not head:
            return head
        
        H = ListNode(-1)
        H.next = head
        pre = H
        p = q = head
        
        while q:
            while q and p.val == q.val:
                q = q.next
            
            if p.next != q:
                pre.next = q
            else:
                pre.next = p
                pre = pre.next # 只有在没有重复的情况就下切换到下一个
            
            p = q
        
        return H.next
            
                
                
                
                
                
                
        
        