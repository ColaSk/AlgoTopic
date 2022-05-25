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
解析
层次遍历时 当遍历到空时如果还有其他非空节点遍历，将判断不是完全二叉树
"""
class Solution:
    def isCompleteTree(self , root: TreeNode) -> bool:
        # write code here
        
        if not root:
            return True
        
        queue = [root]
        end = False
        
        while queue:
            
            n = len(queue)
            for i in range(n):
                
                node = queue.pop(0)
                
                if not node:
                    end = True
                    
                else:
                    if end:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
        return True

                
        