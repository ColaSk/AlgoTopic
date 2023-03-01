# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param t1 TreeNode类 
# @param t2 TreeNode类 
# @return TreeNode类
#

"""
描述
已知两颗二叉树，将它们合并成一颗二叉树。
合并规则是：都存在的结点，就将结点值加起来，否则空的位置就由另一个树的结点来代替。
"""
class Solution:
    def mergeTrees(self , t1: TreeNode, t2: TreeNode) -> TreeNode:
        # write code here
        
        if not t1:
            return t2
        
        if not t2:
            return t1
        
        node = TreeNode(t1.val+t2.val)
        
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        
        return node
    