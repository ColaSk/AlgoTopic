#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param sequence int整型一维数组 
# @return bool布尔型
#

"""
描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回 true ,否则返回 false 。假设输入的数组的任意两个数字都互不相同。

数据范围： 节点数量 0 \le n \le 10000≤n≤1000 ，节点上的值满足 1 \le val \le 10^{5}1≤val≤10 
5
  ，保证节点上的值各不相同
要求：空间复杂度 O(n)O(n) ，时间时间复杂度 O(n^2)O(n 
2
 )
提示：
1.二叉搜索树是指父亲节点大于左子树中的全部节点，但是小于右子树中的全部节点的树。
2.该题我们约定空树不是二叉搜索树
3.后序遍历是指按照 “左子树-右子树-根节点” 的顺序遍历
"""

class Solution:
    def VerifySquenceOfBST(self , sequence: List[int]) -> bool:
        # write code here
        
        if not sequence:
            return False
        
        l = len(sequence)
        
        root_node = sequence[l-1]
        
        index = 0
        
        for i in range(l):
            if sequence[i] >= root_node:
                index = i
                break
        
        for j in range(index, l):
            if sequence[j] < root_node:
                return False
        
        left = True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[0: index])
        
        right = True
        if index < l-1:
            right = self.VerifySquenceOfBST(sequence[index: -1])
        
        return left and right
        
        