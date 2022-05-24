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
# @return int整型二维数组
#
class Solution:
    def Print(self , pRoot: TreeNode) -> List[List[int]]:
        # write code here
        
                
        res = []
        queue = []
        sign = 1
        
        if not pRoot:
            return res
        
        queue.append(pRoot)
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
            
            if sign%2:
                res.append(temp)
            else:
                res.append(temp[::-1])
            sign += 1
        return res