# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

"""
描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）。 下图是一个含有5个结点的复杂链表。图中实线箭头表示next指针，虚线箭头表示random指针。为简单起见，指向null的指针没有画出。
解析
1. 使用字典记录所有指针信息
2. 在原队列中记录指针信息，然后用双指针指定链接指针
"""
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        
        if pHead is None:
            return None
        
        node_dict = {}
        p = pHead
        
        while p:
            node_dict[p] = RandomListNode(p.label)
            p = p.next
        
        p = pHead
        while p:
            node_dict[p].next = node_dict.get(p.next)
            node_dict[p].random =  node_dict.get(p.random)
            p = p.next
        
        return node_dict[pHead]
        
        