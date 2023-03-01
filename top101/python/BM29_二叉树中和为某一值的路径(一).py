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
# @param sum int整型 
# @return bool布尔型
#

"""
描述
给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
2.叶子节点是指没有子节点的节点
3.路径只能从父节点到子节点，不能从子节点到父节点
4.总节点数目为n
解析
1. 到达叶子节点并且数值等于sum时判断成功
2. 不能通过判断节点数据与sum的大小关系作为终止条件，因为可能存在负数
3.判断叶子节点通过左右子树为空判断，不能通过none判断，因为头节点可能为空并满足条件
"""
class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        # write code here
        
        if not root:
            return False
        
        if not root.left and not root.right and sum == root.val:
            return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
        
        