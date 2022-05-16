# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param proot TreeNode类 
# @param k int整型 
# @return int整型
#
"""
描述
给定一棵结点数为n 二叉搜索树，请找出其中的第 k 小的TreeNode结点值。
1.返回第k小的节点值即可
2.不能查找的情况，如二叉树为空，则返回-1，或者k大于n等等，也返回-1
3.保证n个节点的值不一样

解析

二叉搜索树中序遍历

"""
class Solution:
    count = 0
    res = -1
    
    def KthNode(self , proot: TreeNode, k: int) -> int:
        
        self.dfs(proot, k)
        return self.res
        
    def dfs(self , proot: TreeNode, k: int) -> int:
        # write code here
        if not proot:
            return
        
        if proot.left:
            self.KthNode(proot.left, k)
        
        if self.count == k:
            return 
        
        self.count += 1
        
        if self.count == k:
            self.res = proot.val
        
        if proot.right:
            self.KthNode(proot.right, k)
        