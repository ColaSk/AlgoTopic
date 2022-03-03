# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

"""
描述
    给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
    下图为一棵有9个节点的二叉树。树中从父节点指向子节点的指针用实线表示，从子节点指向父节点的用虚线表示

示例:
    输入:{8,6,10,5,7,9,11},8
    返回:9
解析:这个组装传入的子树根节点，其实就是整颗树，中序遍历{5,6,7,8,9,10,11}，根节点8的下一个节点就是9，应该返回{9,10,11}，后台只打印子树的下一
    个节点，所以只会打印9

数据范围：节点数满足 1 \le n \le 50 \1≤n≤50  ，节点上的值满足 1 \le val \le 100 \1≤val≤100 

要求：空间复杂度 O(1) \O(1)  ，时间复杂度 O(n)\O(n) 
输入描述：
输入分为2段，第一段是整体的二叉树，第二段是给定二叉树节点的值，后台会将这2个参数组装为一个二叉树局部的子树传入到函数GetNext里面，用户得到的输入只有一个子树根节点
返回值描述：
返回传入的子树根节点的下一个节点，后台会打印输出这个节点

解析: 两种情况：1）这个节点有右孩子，那下一个节点（根据中序遍历）肯定就是右孩子子树的最左边的叶节点；2）这个节点没有右孩子，那就往上走；如果这个节点是他父亲节点的左孩子，
    那就返回这个父亲节点；如果该节点是父亲节点的右孩子，那就一直往上走，直到找到那个满足是左孩子节点的父节点即可。
"""
class Solution:
    def GetNext(self, pNode):
        # write code here
        
        node = pNode
        
        if not node:
            return
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        elif node.next:
            while node.next and node.next.left is not node:
                node = node.next
            node = node.next
            return node
        else:
            return 
        
            
            