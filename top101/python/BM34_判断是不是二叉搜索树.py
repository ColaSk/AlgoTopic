# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @return bool布尔型
#

"""
描述
给定一个二叉树根节点，请你判断这棵树是不是二叉搜索树。

二叉搜索树满足每个节点的左子树上的所有节点均严格小于当前节点且右子树上的所有节点均严格大于当前节点。

解析
中序遍历: 中序遍历结果是递增的
"""
import sys
class Solution:
    pre = -sys.maxsize - 1 # 定义当前顺序值
    def isValidBST(self , root: TreeNode) -> bool:
        # write code here
        if not root:
            return True
        
        left_bst = self.isValidBST(root.left)
        

        if not left_bst:
            return False
        
        if root.val <= self.pre:
            return False
        
        self.pre = root.val
        
        right_bst = self.isValidBST(root.right)
        
        if not right_bst:
            return False
        
        return True
        
            