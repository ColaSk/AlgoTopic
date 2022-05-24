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
# @return int整型二维数组
#

"""
描述
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
"""
class Solution:
    def levelOrder(self , root: TreeNode) -> List[List[int]]:
        # write code here
        
        res = []
        queue = []
        
        if not root:
            return res
        
        queue.append(root)
        while queue:
            
            temp = []
            n = len(queue)
            
            for i in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(temp)
        return res
        