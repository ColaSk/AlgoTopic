#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#

"""
描述
在一个二维数组array中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
给定 target = 7，返回 true。

给定 target = 3，返回 false。

数据范围：矩阵的长宽满足 5000≤n,m≤500 ， 矩阵中的值满足 10^90≤val≤10 
9
 
进阶：空间复杂度 O(1)O(1) ，时间复杂度 O(n+m)O(n+m)
"""
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        
        h = len(array)
        if h == 0:
            return False
        w = len(array[0])
        if w == 0:
            return False
        
        i, j = 0, w-1
        while i < h and j >= 0:
            if target == array[i][j]:
                return True

            if target < array[i][j]:
                j -= 1
            else:
                i += 1
        return False
                
                
        