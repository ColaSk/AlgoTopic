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
# @return TreeNode类
#

"""
描述
操作给定的二叉树，将其变换为源二叉树的镜像。
数据范围：二叉树的节点数 0≤n≤1000 ， 二叉树每个节点的值 0≤val≤1000
要求： 空间复杂度 O(n) 。本题也有原地操作，即空间复杂度 O(1) 的解法，时间复杂度 O(n)

解析
遍历二叉树并将左右子树互换位置既可
"""

class Solution:
    def Mirror(self , pRoot: TreeNode) -> TreeNode:
        # write code here
        
        if pRoot:
            self.Mirror(pRoot.left)
            self.Mirror(pRoot.right)
            pRoot.left, pRoot.right = pRoot.right, pRoot.left
        
        return pRoot