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

"""
描述
不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。
例如输入{8,6,10,#,#,2,1}，如以下图中的示例二叉树，则依次
打印8,6,10,2,1(空节点不打印，跳过)，请你将打印的结果存放
到一个数组里面，返回。
"""

class Solution:
    def PrintFromTopToBottom(self , root: TreeNode) -> List[int]:
        # write code here
   
        result = []
        stack = [root]
        
        while stack:
            
            node = stack.pop(0)
            
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result
            
            
        