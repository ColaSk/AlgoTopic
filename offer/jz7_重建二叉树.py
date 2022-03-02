# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param pre int整型一维数组 
# @param vin int整型一维数组 
# @return TreeNode类
#

"""
# 描述
给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}

# 提示:
1.vin.length == pre.length
2.pre 和 vin 均无重复元素
3.vin出现的元素均出现在 pre里
4.只需要返回根结点，系统会自动输出整颗树做答案对比
数据范围：n \le 2000n≤2000，节点的值 -10000 \le val \le 10000−10000≤val≤10000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)

# 思路: 根据先序与中序遍历特点，递归构建左右子树
"""
class Solution:
    def reConstructBinaryTree(self , pre: List[int], vin: List[int]) -> TreeNode:
        # write code here
        
        if not len(pre) or not len(vin):
            return
        
        node_value = pre[0]
        node = TreeNode(node_value)
        
        for i in range(len(vin)):
            if node_value == vin[i]:
                break
        
        node.left = self.reConstructBinaryTree(pre[1:i+1], vin[:i])
        node.right = self.reConstructBinaryTree(pre[i+1:], vin[i+1:])
        
        return node