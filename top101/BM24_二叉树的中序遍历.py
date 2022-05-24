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
# @return int整型一维数组
#
import sys
# 修改最大递归深度为2000
sys.setrecursionlimit(2000)

class Solution:
    def inorderTraversal(self , root: TreeNode) -> List[int]:
        # write code here
        
        if not root:
            return
        
        res = []
        
        left = self.inorderTraversal(root.left)
        
        if left:
            res += left
            
        res.append(root.val)
        
        right = self.inorderTraversal(root.right)
        
        
        if right:
            res += right
            
        return res