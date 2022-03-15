# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @param val int整型 
# @return ListNode类
#

"""
描述
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。

1.此题对比原题有改动
2.题目保证链表中节点的值互不相同
3.该题只会输出返回的链表和结果做对比，所以若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

数据范围:
0<=链表节点值<=10000
0<=链表长度<=10000

"""
class Solution:
    def deleteNode(self , head: ListNode, val: int) -> ListNode:
        # write code here
        
        if not head:
            return head
        
        p = head
        
        if not p.next:
            if p.val == val:
                return None
            else:
                return p
        elif p.val == val:
            return p.next
        
        while p.next:
            
            next_node = p.next
            
            if next_node.val == val:
                p.next = next_node.next
                break
            p = p.next
            
        return head
            