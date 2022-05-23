# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head1 ListNode类 
# @param head2 ListNode类 
# @return ListNode类
#
"""
描述
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
数据范围：0 \le n,m \le 10000000≤n,m≤1000000，链表任意值 0 \le val \le 90≤val≤9
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
"""
class Solution:
    def addInList(self , head1: ListNode, head2: ListNode) -> ListNode:
        # write code here
        
        stack1 = []
        stack2 = []
        
        h1 = head1
        h2 = head2
        
        while h1:
            stack1.append(h1.val)
            h1 = h1.next
            
        while h2:
            stack2.append(h2.val)
            h2 = h2.next
            
        carry = 0
        res = None
        while stack1 or stack2:
            if stack1:
                num1 = stack1.pop()
            else:
                num1 = 0
            
            if stack2:
                num2 = stack2.pop()
            else:
                num2 = 0
                
            sums = num1 + num2 + carry
            carry = sums//10
            rem = sums%10
            node = ListNode(rem)
            node.next = res
            res = node
        
        if carry:
            node = ListNode(carry)
            node.next = res
            res = node
        
        return res
            