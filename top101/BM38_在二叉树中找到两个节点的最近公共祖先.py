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
# @param o1 int整型 
# @param o2 int整型 
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self , root: TreeNode, o1: int, o2: int) -> int:
        # write code here
        
        def getpath(root: TreeNode, target: int) -> List[int]:
            
            if not root:
                return []
            
            if root.val == target:
                return [root.val]
            
            left = getpath(root.left, target)
            
            if left:
                left.append(root.val)
                return left
            
            right = getpath(root.right, target)
            
            if right:
                right.append(root.val)
                return right
            
            return []
        
        path1 = getpath(root, o1)[::-1]
        path2 = getpath(root, o2)[::-1]
        i = 0
        res = None
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                res = path1[i]
            i += 1
            
        return res
        
            
        