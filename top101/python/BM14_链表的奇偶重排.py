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
给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
注意是节点的编号而非节点的数值。

数据范围：节点数量满足 0 \le n \le 10^50≤n≤10 
5
 ，节点中的值都满足 0 \le val \le 10000≤val≤1000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

"""
class Solution:
    def oddEvenList(self , head: ListNode) -> ListNode:
        # write code here
        
        if not head:
            return head
        
        odd_p = odd = ListNode(-1)
        even_p = even = ListNode(-1)
        
        p = head
        i = 1
        while p:
            
            if i%2 == 0: # 偶数
                even_p.next = p
                even_p = even_p.next
            else:
                odd_p.next = p
                odd_p = odd_p.next
            i += 1
            p = p.next
        odd_p.next = None
        even_p.next = None
        odd_p.next = even.next
        
        return odd.next
                
            
        
        