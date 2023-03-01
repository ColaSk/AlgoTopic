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
# @return int整型
#

"""
描述
求给定二叉树的最大深度，
深度是指树的根节点到任一叶子节点路径上节点的数量。
最大深度是所有叶子节点的深度的最大值。
（注：叶子节点是指没有子节点的节点。）


数据范围：0 \le n \le 1000000≤n≤100000，树上每个节点的val满足 |val| \le 100∣val∣≤100
要求： 时间复杂度 O(n)O(n)
"""
class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        
        if not root:
            return 0
        
        depth = 1
        
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return depth
        