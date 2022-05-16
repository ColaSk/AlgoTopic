# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#

"""
描述
输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）

数据范围： n \le 1000n≤1000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)

解析
双指针，同时遍历两个链表，当遍历完成时，切换到对方的链表，判断是否相等，如果相等了说明遍历完成，当有公共节点时返回的是节点
当没有节点时为空
"""
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        
        if not pHead1 or not pHead2:
            return 
        
        p1, p2 = pHead1, pHead2
        
        while p1 != p2:
            
            if p1:
                p1 = p1.next
            else:
                p1 = pHead2
            
            if p2:
                p2 = p2.next
            else:
                p2 = pHead1
                
        return p1