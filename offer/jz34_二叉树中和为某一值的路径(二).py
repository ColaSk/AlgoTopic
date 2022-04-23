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
# @param target int整型 
# @return int整型二维数组
#

"""
描述
输入一颗二叉树的根节点root和一个整数expectNumber，找出二叉树中结点值的和为expectNumber的所有路径。
1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
2.叶子节点是指没有子节点的节点
3.路径只能从父节点到子节点，不能从子节点到父节点
4.总节点数目为n
解析: 先序遍历
"""
class Solution:
    def FindPath(self , root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        result = []
        path = []
        
        if not root:
            return result
        
        self.DFS(root, target, path, result)
        
        return result
        
    def DFS(self, root: TreeNode, target: int, path: list, result: list):
        
        path.append(root.val)
        tar = target-root.val
        
        if not root.left and not root.right:
            if tar == 0:
                result.append(path.copy())
            path.pop()
            return
        elif not root.left:
            self.DFS(root.right, tar, path, result)
            path.pop()
        elif not root.right:
            self.DFS(root.left, tar, path, result)
            path.pop()
        else:
            self.DFS(root.left, tar, path, result)
            self.DFS(root.right, tar, path, result)
            path.pop()
        

        