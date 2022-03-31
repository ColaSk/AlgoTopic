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
class Solution:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        # write code here
        
        def is_symmetrical(pl: TreeNode, pr: TreeNode):
            
            if not pl and not pr:
                return True
            
            if not pl or not pr:
                return False
            
            if pl.val != pr.val:
                return False
            
            return (is_symmetrical(pl.left, pr.right) and
                   is_symmetrical(pl.right, pr.left))
            

        return is_symmetrical(pRoot, pRoot)

                
                
                
        
        