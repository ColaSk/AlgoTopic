# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param pRootOfTree TreeNode类 
# @return TreeNode类
#

"""
描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表
数据范围：输入二叉树的节点数 0 \le n \le 10000≤n≤1000，二叉树中每个节点的值 0\le val \le 10000≤val≤1000
要求：空间复杂度O(1)O(1)（即在原树上操作），时间复杂度 O(n)O(n)

注意:
1.要求不能创建任何新的结点，只能调整树中结点指针的指向。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继
2.返回链表中的第一个节点的指针
3.函数返回的TreeNode，有左右指针，其实可以看成一个双向链表的数据结构
4.你不用输出双向链表，程序会根据你的返回值自动打印输出

解析:
中序遍历
"""
class Solution:
    
    head = None
    pre = None
    
    def Convert(self , pRootOfTree ):
        # write code here
        
        if not pRootOfTree:
            return
        
        self.Convert(pRootOfTree.left)
        
        if not self.pre:
            self.pre = pRootOfTree
            self.head = pRootOfTree
            
        else:
            self.pre.right = pRootOfTree
            pRootOfTree.left = self.pre
            self.pre = pRootOfTree
        
        self.Convert(pRootOfTree.right)
        
        return self.head
            
            
            
            
        
        