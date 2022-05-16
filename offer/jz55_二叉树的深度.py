# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot TreeNode类 
# @return int整型
#

"""
描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度，根节点的深度视为 1 。

数据范围：节点的数量满足 0 \le n \le 1000≤n≤100 ，节点上的值满足 0 \le val \le 1000≤val≤100
进阶：空间复杂度 O(1)O(1) ，时间复杂度 O(n)O(n)

解析: 二叉树的深度遍历
"""
class Solution:
    def TreeDepth(self , pRoot: TreeNode) -> int:
        # write code here
        
        if not pRoot:
            return 0
        
        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        
        if left_depth > right_depth:
            return 1 + left_depth
        else:
            return 1 + right_depth
        