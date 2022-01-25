#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        result = ListNode(0, None)
        top = result
        ten, unit = 0, 0
        while node1 or node2 or ten:
            ten, unit = self.addNode(node1, node2, ten)
            node = ListNode(unit, None)
            top.next = node
            top = top.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        return result.next

    
    def addNode(self, node1, node2, carry):
        val1, val2 = 0, 0
        if node1:
            val1 = node1.val
        if node2:
            val2 = node2.val
        num = val1 + val2 + carry
        if num >= 10:
            unit = num%10
            ten = 1
        else:
            unit = num
            ten = 0
        return ten, unit

# @lc code=end

