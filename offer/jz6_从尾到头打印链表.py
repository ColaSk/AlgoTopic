# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param listNode ListNode类 
# @return int整型一维数组
#
"""描述
输入一个链表的头节点，按链表从尾到头的顺序返回每个节点的值（用数组返回）。

如输入{1,2,3}的链表

返回一个数组为[3,2,1]

0 <= 链表长度 <= 10000

解析: 采用栈的结构
"""
class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        stack = []
        p = listNode
        
        while p:
            stack.append(p.val)
            p = p.next
        return stack[::-1]
        