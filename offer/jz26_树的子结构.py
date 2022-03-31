# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pRoot1 TreeNode类 
# @param pRoot2 TreeNode类 
# @return bool布尔型
#

"""
描述
输入两棵二叉树A，B，判断B是不是A的子结构。（我们约定空树不是任意一个树的子结构）
假如给定A为{8,8,7,9,2,#,#,#,#,4,7}，B为{8,9,2}，2个树的结构如下，可以看出B是A的子结构
解析
主要分为两个步骤: 1.查找到与子树头节点相同的节点 2.判断是否为子树结构
"""

class Solution:
    def HasSubtree(self , pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        # write code here
        
        def is_sub(p1: TreeNode, p2: TreeNode):
            if not p2:
                return True
            if not p1:
                return False
            if p1.val == p2.val:
                return is_sub(p1.right, p2.right) and is_sub(p1.left, p2.left)
            return False
                
        result = False
        
        if not pRoot1 or not pRoot2:
            return result
        
        if pRoot1.val == pRoot2.val:
            result = is_sub(pRoot1, pRoot2)
        
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
            
        return result
        