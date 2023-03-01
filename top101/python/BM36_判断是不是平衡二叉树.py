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
# @return bool布尔型
#

"""
描述
输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
"""
class Solution:
    def IsBalanced_Solution(self , pRoot: TreeNode) -> bool:
        # write code here
        
        def getdepth(root) -> int:
            
            if not root:
                return 0
            
            left = getdepth(root.left)
            if left < 0:
                return -1
            right = getdepth(root.right)
            if right < 0:
                return -1
            
            return -1 if abs(left-right) > 1 else 1 + max([left, right])   
        
        if not pRoot:
            return True
        
        return getdepth(pRoot) != -1