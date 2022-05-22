# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param lists ListNode类一维数组 
# @return ListNode类
#

"""
描述
合并 k 个升序的链表并将结果作为一个升序的链表返回其头节点。

数据范围：节点总数满足 0 \le n \le 10^50≤n≤10 
5
 ，链表个数满足 1 \le k \le 10^5 \1≤k≤10 
5
   ，每个链表的长度满足 1 \le len \le 200 \1≤len≤200  ，每个节点的值满足 |val| <= 1000∣val∣<=1000
要求：时间复杂度 O(nlogk)O(nlogk)

1. 两个链表的合并
2. 划分区间
3. 递归合并
"""
class Solution:
    
    def merge2(self, head1: ListNode, head2: ListNode) -> ListNode:
        if not head1:
            return head2
        if not head2:
            return head1
        
        h = head = ListNode(-1)
        p = head1
        q = head2
        
        while p and q:
            if p.val < q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next 
            h = h.next
        if not p:
            h.next = q
        if not q:
            h.next = p
        return head.next
        
    
    def divideMerge(self, lists, left, right) -> ListNode:
        
        if left > right:
            return 
        elif left == right:
            return lists[left]
        else:
            mid = (left+right)//2
            return self.merge2(
                self.divideMerge(lists, left, mid), 
                self.divideMerge(lists, mid+1, right)
            )
    
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        # write code here
        return self.divideMerge(lists, 0, len(lists) - 1)